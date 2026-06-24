---
name: vasp-wiki
description: Use when answering any question about VASP setup, an INCAR tag's meaning / default / allowed options, input or output file formats (POSCAR, KPOINTS, OUTCAR, CHGCAR, ...), a calculation method or workflow (GW, BSE, RPA, hybrid functionals, machine-learned force fields), or a step-by-step tutorial: this bundle is an offline mirror of the full VASP wiki (vasp.at) covering INCAR tags, input/output file formats, methods, and tutorials.
---

# VASP Wiki Offline Mirror — Precision Retrieval

Offline VASP wiki mirror, snapshot 2026-06-24, 1601 pages, GFDL 1.2 © VASP wiki contributors. Each reference file carries its source URL and revision id.

**CRITICAL RULE: NEVER read the whole `references/` tree. This is a router, not a dump.**

## Phase 0 — Goal Formulation
Before retrieving anything, state the specific knowledge needed. Examples:
- "What is ENCUT and when do I need to change it?"
- "How do I set up a hybrid functional calculation?"
- "What does the OUTCAR file contain?"

## Phase 1 — Map (Search & Shortlist)
Run the search tool to find candidate pages:
```
tools/vaspwiki/target/release/vaspwiki search "<query>"
```

Optional flags: `--top N` (show top N results), `--bucket B` (limit to bucket), `--index PATH` (custom index).

If the binary isn't built: `cargo build --release --manifest-path tools/vaspwiki/Cargo.toml`

**Fallback:** scan `INDEX.md` or `_meta/index.json` manually (fields: `path`, `title`, `bucket`, `summary`, `aliases`, `related`, `keywords`).

**Aliases resolve automatically** — e.g., ENMAX → ENCUT.

Return a **short ranked list** of the most relevant `references/<path>` files.

## Phase 2 — Read Essential Pages
Open ONLY the shortlisted files from Phase 1. No exploration beyond that list.

## Phase 3 — Traverse & Refine
If knowledge gaps remain:
- Follow `related` links in `_meta/index.json` or in-page markdown links
- Re-query with refined terms
- Repeat until the question is fully covered

Don't settle for incomplete answers. No hard ceiling on pages read — retrieval is purely goal-driven.

## Quick Reference: Buckets

- **incar-tags** (626): INCAR tag definitions, defaults, allowed values
- **input-files** (28): POSCAR, KPOINTS, POTCAR, INCAR format specs
- **output-files** (40): OUTCAR, OSZICAR, CHGCAR, vasprun.xml, DOSCAR parsing
- **methods** (48): GW, BSE, RPA, ACFDT, hybrid functionals, machine-learned force fields
- **tutorials** (303): step-by-step workflows and examples
- **theory** (43): theoretical background and physics explanations
- **categories** (66): topical collections and cross-cuts
- **misc** (187): tools, FAQ, miscellaneous
- **redirects** (260): non-primary pages (excluded from primary count)

Internal links are relative paths within `references/`; links outside this snapshot point to https://vasp.at/wiki/.

Snapshot 2026-06-24, GFDL 1.2.
