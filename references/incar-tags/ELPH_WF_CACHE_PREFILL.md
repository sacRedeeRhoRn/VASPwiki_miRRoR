<!-- Source: https://vasp.at/wiki/index.php/ELPH_WF_CACHE_PREFILL | revid: 37222 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_WF_CACHE_PREFILL
ELPH_WF_CACHE_PREFILL = logical  
Default: **ELPH_WF_CACHE_PREFILL** = .TRUE. 

Description: Pre-fills the wavefunction cache before the main
electron-phonon loop begins.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

When computing electron-phonon matrix elements, VASP caches
wavefunctions fetched from remote MPI ranks (see
[ELPH_WF_CACHE_MB](ELPH_WF_CACHE_MB.md)). With
`ELPH_WF_CACHE_PREFILL = .TRUE.` (the default), all required
wavefunctions are gathered into the cache in a single communication
phase before the main loop starts. This means the loop itself runs with
little or no inter-rank MPI traffic.

Setting `ELPH_WF_CACHE_PREFILL = .FALSE.` disables pre-filling;
wavefunctions are then fetched on demand during the loop. This reduces
the upfront communication cost but increases total MPI traffic and is
generally slower.

## Related tags and articles
- [ELPH_WF_CACHE_MB](ELPH_WF_CACHE_MB.md)
- [ELPH_WF_REDISTRIBUTE](ELPH_WF_REDISTRIBUTE.md)
- [ELPH_WF_COMM_OPT](ELPH_WF_COMM_OPT.md)
