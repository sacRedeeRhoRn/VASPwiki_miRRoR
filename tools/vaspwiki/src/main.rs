use std::env;
use std::path::{Path, PathBuf};
use std::process::exit;

use serde::Deserialize;

#[derive(Deserialize)]
struct Index {
    pages: Vec<Page>,
}

#[derive(Deserialize)]
struct Page {
    path: String,
    title: String,
    #[serde(default)]
    bucket: String,
    #[serde(default)]
    categories: Vec<String>,
    #[serde(default)]
    summary: String,
    #[serde(default)]
    aliases: Vec<String>,
    #[serde(default)]
    keywords: Vec<String>,
}

fn tokenize(s: &str) -> Vec<String> {
    s.to_lowercase()
        .split(|c: char| !c.is_alphanumeric())
        .filter(|t| !t.is_empty())
        .map(|t| t.to_string())
        .collect()
}

fn usage() {
    eprintln!("vaspwiki — offline VASP wiki search");
    eprintln!();
    eprintln!("Usage:");
    eprintln!("  vaspwiki search \"<query>\" [--top N] [--bucket B] [--index PATH]");
}

fn resolve_index(cli_index: Option<&str>) -> Result<PathBuf, String> {
    let mut tried: Vec<String> = Vec::new();

    // 1. --index PATH
    if let Some(p) = cli_index {
        let pb = PathBuf::from(p);
        if pb.exists() {
            return Ok(pb);
        }
        tried.push(format!("--index {}", p));
    }

    // 2. VASPWIKI_INDEX env var
    if let Ok(p) = env::var("VASPWIKI_INDEX") {
        if !p.is_empty() {
            let pb = PathBuf::from(&p);
            if pb.exists() {
                return Ok(pb);
            }
            tried.push(format!("$VASPWIKI_INDEX={}", p));
        }
    }

    // 3. Walk UP from current working dir.
    if let Ok(cwd) = env::current_dir() {
        if let Some(found) = walk_up_for_index(&cwd) {
            return Ok(found);
        }
        tried.push(format!("walk-up from cwd {}", cwd.display()));
    }

    // 4. Exe-relative: walk UP from the exe directory.
    if let Ok(exe) = env::current_exe() {
        if let Some(exe_dir) = exe.parent() {
            if let Some(found) = walk_up_for_index(exe_dir) {
                return Ok(found);
            }
            tried.push(format!("walk-up from exe dir {}", exe_dir.display()));
        }
    }

    Err(format!(
        "could not locate _meta/index.json. Tried:\n  {}",
        tried.join("\n  ")
    ))
}

fn walk_up_for_index(start: &Path) -> Option<PathBuf> {
    let mut cur: Option<&Path> = Some(start);
    while let Some(dir) = cur {
        let candidate = dir.join("_meta").join("index.json");
        if candidate.exists() {
            return Some(candidate);
        }
        cur = dir.parent();
    }
    None
}

struct Args {
    query: String,
    top: usize,
    bucket: Option<String>,
    index: Option<String>,
}

fn parse_args(argv: &[String]) -> Result<Args, ()> {
    // argv excludes program name; first must be "search".
    if argv.is_empty() || argv[0] != "search" {
        return Err(());
    }

    let mut query: Option<String> = None;
    let mut top: usize = 8;
    let mut bucket: Option<String> = None;
    let mut index: Option<String> = None;

    let mut i = 1;
    while i < argv.len() {
        let a = &argv[i];
        match a.as_str() {
            "--top" => {
                i += 1;
                if i >= argv.len() {
                    return Err(());
                }
                match argv[i].parse::<usize>() {
                    Ok(n) => top = n,
                    Err(_) => return Err(()),
                }
            }
            "--bucket" => {
                i += 1;
                if i >= argv.len() {
                    return Err(());
                }
                bucket = Some(argv[i].clone());
            }
            "--index" => {
                i += 1;
                if i >= argv.len() {
                    return Err(());
                }
                index = Some(argv[i].clone());
            }
            _ => {
                if query.is_none() {
                    query = Some(a.clone());
                } else {
                    // ignore extra positional args
                }
            }
        }
        i += 1;
    }

    let query = match query {
        Some(q) if !q.trim().is_empty() => q,
        _ => return Err(()),
    };

    Ok(Args {
        query,
        top,
        bucket,
        index,
    })
}

fn score_page(page: &Page, tokens: &[String], full_query: &str) -> i64 {
    let title_lc = page.title.to_lowercase();
    let title_tokens = tokenize(&page.title);
    let summary_tokens: Vec<String> = tokenize(&page.summary);

    let aliases_lc: Vec<String> = page.aliases.iter().map(|a| a.to_lowercase()).collect();
    let categories_lc: Vec<String> = page.categories.iter().map(|c| c.to_lowercase()).collect();
    let keywords_lc: Vec<String> = page.keywords.iter().map(|k| k.to_lowercase()).collect();

    let mut score: i64 = 0;

    for tok in tokens {
        // Title token / substring.
        if title_tokens.iter().any(|t| t == tok) {
            score += 10;
        } else if title_lc.contains(tok.as_str()) {
            score += 6;
        }

        // Alias: at most one bonus per token, prefer exact (+9) else substring (+5).
        let alias_exact = aliases_lc.iter().any(|a| a == tok);
        if alias_exact {
            score += 9;
        } else if aliases_lc.iter().any(|a| a.contains(tok.as_str())) {
            score += 5;
        }

        // Category: token equality OR category-substring-contains-token, once per token.
        let cat_match = categories_lc
            .iter()
            .any(|c| c == tok || c.contains(tok.as_str()));
        if cat_match {
            score += 4;
        }

        // Summary token set.
        if summary_tokens.iter().any(|s| s == tok) {
            score += 2;
        }

        // Keyword set.
        if keywords_lc.iter().any(|k| k == tok) {
            score += 1;
        }
    }

    // Exact full-query boost.
    if full_query == title_lc || aliases_lc.iter().any(|a| a == full_query) {
        score += 20;
    }

    score
}

fn main() {
    let argv: Vec<String> = env::args().skip(1).collect();

    let args = match parse_args(&argv) {
        Ok(a) => a,
        Err(()) => {
            usage();
            exit(2);
        }
    };

    let index_path = match resolve_index(args.index.as_deref()) {
        Ok(p) => p,
        Err(e) => {
            eprintln!("error: {}", e);
            exit(1);
        }
    };

    let raw = match std::fs::read_to_string(&index_path) {
        Ok(s) => s,
        Err(e) => {
            eprintln!("error: failed to read {}: {}", index_path.display(), e);
            exit(1);
        }
    };

    let index: Index = match serde_json::from_str(&raw) {
        Ok(idx) => idx,
        Err(e) => {
            eprintln!(
                "error: failed to parse JSON index at {}: {}",
                index_path.display(),
                e
            );
            exit(1);
        }
    };

    let full_query = args.query.trim().to_lowercase();
    let tokens = tokenize(&args.query);

    let mut scored: Vec<(i64, &Page)> = Vec::new();
    for page in &index.pages {
        if let Some(b) = &args.bucket {
            if &page.bucket != b {
                continue;
            }
        }
        let s = score_page(page, &tokens, &full_query);
        if s > 0 {
            scored.push((s, page));
        }
    }

    // Sort: score DESC; tie-break shorter title length; then title alphabetical.
    scored.sort_by(|a, b| {
        b.0.cmp(&a.0)
            .then_with(|| a.1.title.len().cmp(&b.1.title.len()))
            .then_with(|| a.1.title.cmp(&b.1.title))
    });

    if scored.is_empty() {
        eprintln!("no matches for \"{}\"", args.query);
        exit(0);
    }

    for (score, page) in scored.into_iter().take(args.top) {
        println!(
            "references/{}  —  {}  [{}]",
            page.path, page.summary, score
        );
    }
}
