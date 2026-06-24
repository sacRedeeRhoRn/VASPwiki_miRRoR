# VASP Wiki — Codex Agent Instructions

This repository is an offline mirror of the VASP wiki (https://vasp.at/wiki/), snapshot 2026-06-24, GFDL 1.2. It contains 1601 mirrored pages organized into searchable buckets and indexed by machine-readable metadata.

## Precision Retrieval Protocol

Apply this four-phase protocol for every query. DO NOT bulk-load the references/ tree.

### Phase 0 — Goal Formulation
State the specific knowledge needed before searching. Examples:
- "What does the ENCUT INCAR tag control, and what are typical values?"
- "How do I set up a GW calculation?"
- "Parse the OUTCAR file format."

### Phase 1 — Map (Search)
Use the search binary to find candidate pages:

```bash
tools/vaspwiki/target/release/vaspwiki search "<query>"
```

**Build first if needed:**
```bash
cargo build --release --manifest-path tools/vaspwiki/Cargo.toml
```

**Optional flags:**
- `--top N` — return top N results
- `--bucket B` — restrict to bucket (incar-tags, input-files, output-files, methods, tutorials, theory, categories, misc)
- `--index PATH` — custom index path

**Fallback if cargo unavailable:**
- Scan `INDEX.md` (master list by bucket)
- Or read `_meta/index.json` directly (machine-readable, fields: path, title, bucket, categories, summary, aliases, related, keywords)

**Aliases resolve automatically** — e.g., ENMAX → ENCUT, NELM → NELMIN.

Return a **ranked shortlist** of the 2–4 most relevant `references/<path>` files.

### Phase 2 — Read Essential Pages
Open ONLY the shortlisted files. No exploration beyond that list.

### Phase 3 — Traverse & Refine
If knowledge gaps remain:
- Follow `related` links in `_meta/index.json`
- Follow in-page markdown links
- Re-query with refined terms
- Repeat until the question is fully covered

**No hard ceiling on pages** — retrieval is purely goal-driven.

## Machine-Readable Index

`_meta/index.json` is a structured map of all 1601 pages. Fields:
- `path` — relative path within references/
- `title` — page title
- `bucket` — category (incar-tags, input-files, etc.)
- `categories` — list of concept tags
- `summary` — one-line description
- `aliases` — alternate names (for alias resolution)
- `related` — array of related page paths
- `keywords` — searchable terms

A Codex or vault-codex tool can consume this directly for efficient traversal.

## Navigation Quick Map

- INCAR tag → `references/incar-tags/<TAG>.md` (626 pages)
- Input file (POSCAR, KPOINTS, POTCAR, INCAR) → `references/input-files/<NAME>.md` (28 pages)
- Output file (OUTCAR, OSZICAR, CHGCAR, vasprun.xml, DOSCAR) → `references/output-files/<NAME>.md` (40 pages)
- Method / functional / workflow → `references/methods/` (48 pages)
- Tutorial / how-to → `references/tutorials/` (303 pages)
- Theory / background → `references/theory/` (43 pages)
- Category landing page → `references/categories/` (66 pages)
- Misc / tools / FAQ → `references/misc/` (187 pages)
- Redirects (non-primary) → `references/redirects/` (260 pages, excluded from primary count)

## About This Repository

**License:** Mirrored documentation content is GFDL 1.2, © VASP wiki contributors. Each file retains its source URL and revision id. Scripts and tools are MIT.

**Source:** https://vasp.at/wiki/

**Snapshot date:** 2026-06-24

**Primary pages:** 1341 (1601 total minus 260 redirects)

**IMPORTANT:** No absolute paths. All file paths are relative to the repository root. Links to pages outside this snapshot point to the live wiki at https://vasp.at/wiki/.
