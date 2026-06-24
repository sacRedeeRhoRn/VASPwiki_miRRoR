<!-- Source: https://vasp.at/wiki/index.php/ELPH_WF_REDISTRIBUTE | revid: 32991 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELPH_WF_REDISTRIBUTE
ELPH_WF_REDISTRIBUTE = \[logical\]  
Default: **ELPH_WF_REDISTRIBUTE** = .FALSE. 

Description: After computing the electronic states, they are
redistributed among the CPUs such that the workload to compute the
electron self-energy is similar among the different CPUs.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

------------------------------------------------------------------------

The computational effort for each Kohn–Sham state is first estimated,
and then the states are distributed among MPI ranks to balance the
workload as evenly as possible. This redistribution is most relevant
when used in combination with
[`ELPH_SELFEN_IMAG_SKIP`](ELPH_SELFEN_IMAG_SKIP.md)` = .TRUE.`.
When [`ELPH_MODE`](ELPH_MODE.md)` = TRANDPORT`, the
default value is `ELPH_WF_REDISTRIBUTE`` = .TRUE.`.

## Related tags and articles
[ELPH_MODE](ELPH_MODE.md),
[ELPH_SELFEN_IMAG_SKIP](ELPH_SELFEN_IMAG_SKIP.md),
[ELPH_RUN](ELPH_RUN.md),
[ELPH_WF_COMM_OPT](ELPH_WF_COMM_OPT.md),
[ELPH_WF_CACHE_PREFILL](ELPH_WF_CACHE_PREFILL.md)
