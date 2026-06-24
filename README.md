# VASP Wiki Offline Mirror

An **UNOFFICIAL** offline mirror of the VASP wiki (https://vasp.at/wiki/), packaged as an LLM skill with precision retrieval and smart indexing. Contains 1601 mirrored pages (1341 primary content) as of 2026-06-24.

## Disclaimer

> **This is an UNOFFICIAL repository.** Not affiliated with or endorsed by VASP or the VASP Software GmbH. VASP is commercial software (https://www.vasp.at/); the mirrored documentation content is © its wiki contributors and redistributed under GFDL 1.2. Each file retains its source URL and revision id. Full license text: https://www.gnu.org/licenses/old-licenses/fdl-1.2.html

## Repository Layout

```
vasp-wiki/
├── SKILL.md                      # LLM skill entry point (Claire Claude)
├── AGENTS.md                     # Codex agent instructions
├── README.md                     # This file
├── LICENSE                       # Dual-license (code MIT, docs GFDL 1.2)
├── INDEX.md                      # Master list of all 1601 pages, grouped by bucket
├── .gitignore                    # (_raw/, target/, __pycache__, .DS_Store)
├── references/                   # Mirrored VASP wiki content
│   ├── incar-tags/               # 626 INCAR tag definitions
│   ├── input-files/              # 28 input file format specs
│   ├── output-files/             # 40 output file parsers
│   ├── methods/                  # 48 calculation methods
│   ├── tutorials/                # 303 step-by-step guides
│   ├── theory/                   # 43 theoretical background
│   ├── categories/               # 66 topical collections
│   ├── misc/                     # 187 tools, FAQ, misc
│   └── redirects/                # 260 non-primary (excluded from count)
├── _meta/                        # Machine-readable metadata
│   ├── index.json                # Full structured index (path, title, bucket, summary, aliases, related, keywords)
│   ├── pages.json                # Complete page metadata dump
│   └── slugmap.json              # Slug-to-path mapping
├── scripts/                      # Build and refresh pipeline
│   ├── crawl_index.py            # Crawl vasp.at/wiki to extract index
│   ├── fetch_pages.py            # Download page content from wiki
│   ├── convert.py                # Convert HTML to markdown
│   ├── organize.py               # Sort pages into bucket directories
│   ├── gen_skill.py              # Generate SKILL.md
│   └── build_index.py            # Generate index.json, INDEX.md, slugmap.json
└── tools/vaspwiki/               # Rust binary for smart search
    ├── src/                      # Rust source
    ├── Cargo.toml                # Cargo manifest
    └── target/release/vaspwiki   # Compiled binary (after build)
```

## Smart Retrieval Protocol

This bundle uses a **4-phase precision protocol** to avoid loading the entire tree. Every query follows:

1. **Phase 0 — Goal:** State the specific knowledge needed.
2. **Phase 1 — Map:** Run `vaspwiki search "<query>"` to find candidate pages.
3. **Phase 2 — Read:** Open ONLY the shortlisted files.
4. **Phase 3 — Traverse:** Follow related links if gaps remain.

**Example commands:**

```bash
# Find pages about plane wave cutoff energy
vaspwiki search "plane wave cutoff energy"

# Search specifically in INCAR tags
vaspwiki search "smearing" --bucket incar-tags

# Alias resolution: ENMAX is an old name for ENCUT
vaspwiki search "ENMAX"  # → returns ENCUT
```

## Use with Claude

1. Copy or symlink this repository into `~/.claude/skills/vasp-wiki/`
2. SKILL.md is the entry point — Claude Code will auto-discover it
3. Queries will invoke the Phase 0–3 retrieval protocol

## Use with Codex

1. Clone this repository into your Codex vault workspace
2. AGENTS.md is auto-read by Codex CLI
3. Build the search binary:
   ```bash
   cargo build --release --manifest-path tools/vaspwiki/Cargo.toml
   ```
4. Use `vaspwiki search` in your Codex workflows

## Refreshing the Mirror

To update the offline mirror with fresh content from https://vasp.at/wiki/:

```bash
# Run the full pipeline in order
scripts/crawl_index.py          # Extract pages list from live wiki
scripts/fetch_pages.py          # Download page content (HTML)
scripts/convert.py              # Convert HTML to markdown
scripts/organize.py             # Sort into bucket directories
scripts/gen_skill.py            # Generate/update SKILL.md
scripts/build_index.py          # Generate index.json, INDEX.md, slugmap.json
```

Then rebuild the Rust binary:
```bash
cargo build --release --manifest-path tools/vaspwiki/Cargo.toml
```

## License

**Code (scripts/, tools/) — MIT License**

Copyright (c) 2026 sacRedeeRhoRn

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

**Documentation content — GFDL 1.2**

The mirrored VASP wiki documentation content (everything under `references/`) is licensed under the GNU Free Documentation License version 1.2, © the VASP wiki contributors. Full license text: https://www.gnu.org/licenses/old-licenses/fdl-1.2.html. Original source: https://vasp.at/wiki/. Each mirrored file retains its own source URL and revision id.
