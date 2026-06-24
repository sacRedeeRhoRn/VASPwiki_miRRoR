<!-- Source: https://vasp.at/wiki/index.php/ELPH_WF_CACHE_MB | revid: 37241 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_WF_CACHE_MB
ELPH_WF_CACHE_MB = real  
Default: **ELPH_WF_CACHE_MB** = 1000 

Description: Maximum memory (in MB) allocated for caching wavefunctions
during electron-phonon matrix element calculations.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.1 |

------------------------------------------------------------------------

Electron-phonon matrix elements are sandwiches of the form

$\langle \psi_{n\mathbf{k}} | \Delta
V_{\mathbf{q}} | \psi_{m\mathbf{k}'} \rangle,$

where $\mathbf{k}' = \mathbf{k} + \mathbf{q}$. Because k-points are distributed across MPI ranks, the
wavefunction $\psi_{n\mathbf{k}}$
needed to form the bra may reside on a different rank than the one
computing the matrix element. ELPH_WF_CACHE_MB sets the maximum memory
(in megabytes) used to cache these remotely fetched wavefunctions
locally, avoiding repeated inter-rank MPI communication.

A separate cache for the PAW projections is also sized proportionally to
ELPH_WF_CACHE_MB.

The wavefunction cache works together with
[ELPH_WF_CACHE_PREFILL](ELPH_WF_CACHE_PREFILL.md)
(default: `.TRUE.`), which pre-populates the cache before the main
electron-phonon loop begins. When pre-fill succeeds, almost all
subsequent wavefunction accesses are served from the cache without MPI
communication.

## Related tags and articles
- [ELPH_WF_CACHE_PREFILL](ELPH_WF_CACHE_PREFILL.md)
- [ELPH_WF_COMM_OPT](ELPH_WF_COMM_OPT.md)
- [ELPH_WF_REDISTRIBUTE](ELPH_WF_REDISTRIBUTE.md)
- [ELPH_RUN](ELPH_RUN.md)
