<!-- Source: https://vasp.at/wiki/index.php/MSDGW_NXI | revid: 33472 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# MSDGW NXI
MSDGW_NXI = \[integer\]  
Default: **MSDGW_NXI** = 2 

Description: Number of pseudo orbitals per compressed energy of mixed
stochastic-deterministic compression
algorithm.^([\[1\]](#cite_note-altman:prl:2024-1))

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

MSDGW_NXI sets the number of stochastic orbitals per energy in the
unprotected space beyond band [MSDGW_NP](MSDGW_NP.md).
This tag is set in combination with [MSDGW_F](../incar-tags/MSDGW_F.md),
the constant energy ratio $F$ of the
compression algorithm. If a positive value of
[MSDGW_F](../incar-tags/MSDGW_F.md) is found, energies beyond the
protected space defined by [MSDGW_NP](MSDGW_NP.md) are
subdivided into energy bins of width $\Delta E_i$ and replaced by their average energy $E_i$, such that $F=\Delta E_i/E_i$. The original orbitals are replaced by MSDGW_NXI randomly
linear combined orbitals. Larger values of MSDGW_NXI decrease the
compression level and improve accuracy of results. The same holds true
for smaller values of [MSDGW_F](../incar-tags/MSDGW_F.md).

## Use cases
The pseudo-random phases used to construct the stochastic orbitals are
generated from the seed [MSDGW_SEED](MSDGW_SEED.md).

## Related tags and articles
[MSDGW_F](../incar-tags/MSDGW_F.md),
[MSDGW_SEED](MSDGW_SEED.md),
[MSDGW_NP](MSDGW_NP.md)

## References
1.  [↑](#cite_ref-altman:prl:2024_1-0) [Altman, A. R. and Kundu, S. and
    da Jornada, F. H., *Mixed Stochastic-Deterministic Approach for
    Many-Body Perturbation Theory Calculations*, Phys. Rev. Lett.
    **132**, 086401
    (2024).](https://doi.org/10.1103/PhysRevLett.132.086401)

------------------------------------------------------------------------
