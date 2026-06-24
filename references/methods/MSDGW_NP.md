<!-- Source: https://vasp.at/wiki/index.php/MSDGW_NP | revid: 33473 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# MSDGW NP
MSDGW_NP = \[integer\]  
Default: **MSDGW_NP** = 2\*max(NELECT/2+NIONS/2,NELECT\*0.6) 

Description: Number of protected bands in mixed stochastic-deterministic
compression algorithm.^([\[1\]](#cite_note-altman:prl:2024-1))

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

MSDGW_NP determines how many bands are protected by the mixed
stochastic-deterministic compression of unoccupied bands. Bands beyond
MSDGW_NP are compressed. This tag is set in combination with
[MSDGW_F](../incar-tags/MSDGW_F.md), the constant energy ratio
$F$ of the compression algorithm. If a
positive value of [MSDGW_F](../incar-tags/MSDGW_F.md) is found, states
beyond MSDGW_NP are subdivided into energy bins of width
$\Delta E_i$ and replaced by their
average energy $E_i$, such that
$F=\Delta E_i/E_i$. The original
orbitals are replaced by [MSDGW_NXI](MSDGW_NXI.md)
randomly linear combined orbitals. Larger values of
[MSDGW_NXI](MSDGW_NXI.md) decrease the compression level
and improve accuracy of results. The same holds true for smaller values
of [MSDGW_F](../incar-tags/MSDGW_F.md).

## Related tags and articles
[MSDGW_F](../incar-tags/MSDGW_F.md),
[MSDGW_NXI](MSDGW_NXI.md),
[MSDGW_SEED](MSDGW_SEED.md)

## References
1.  [↑](#cite_ref-altman:prl:2024_1-0) [Altman, A. R. and Kundu, S. and
    da Jornada, F. H., *Mixed Stochastic-Deterministic Approach for
    Many-Body Perturbation Theory Calculations*, Phys. Rev. Lett.
    **132**, 086401
    (2024).](https://doi.org/10.1103/PhysRevLett.132.086401)

------------------------------------------------------------------------
