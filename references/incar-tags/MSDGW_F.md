<!-- Source: https://vasp.at/wiki/index.php/MSDGW_F | revid: 36380 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# MSDGW F


MSDGW_F = \[real\]  
Default: **MSDGW_F** = -1 

Description: A positive value of
MSDGW_F triggers the mixed
stochastic-deterministic compression algorithm of Altman and
co-workers.[^altman:prl:2024-1]

------------------------------------------------------------------------

MSDGW_F is the constant energy
ratio $F$ of the
compression algorithm. If set to a positive value, energies beyond the
protected space defined by [MSDGW_NP](../methods/MSDGW_NP.md) are
subdivided into energy bins of width $\Delta E_i$
and replaced by other energies $E_i$, such
that $F=\Delta E_i/E_i$. The original orbitals are replaced by
[MSDGW_NXI](../methods/MSDGW_NXI.md) randomly linear combined
orbitals. Larger values of
MSDGW_F increase the
compression level at the expense of accuracy. The same holds true for
smaller values of [MSDGW_NXI](../methods/MSDGW_NXI.md).

This compression algorithm has been developed to reduce the large number
of unoccupied states required for the calculation of the screened
interaction in [GW
calculations](../methods/Practical_guide_to_GW_calculations.md).
It has been demonstrated that one can reduce the unoccupied manifold by
more than 50 per cent and speed up the GW step by a factor of 2 or more
with a resulting error of only 50 meV or less on the quasi-particle band
gap.[^altman:prl:2024-1]

|  |
|----|
| **Mind:** Available as of VASP.6.6.0. |

|  |
|----|
| **Warning:** Not recommended for [LRPAFORCE](LRPAFORCE.md)=T. |


## Contents


- [1 Use
  cases](#use-cases)
- [2
  Caveats](#caveats)
- [3 Related tags
  and articles](#related-tags-and-articles)
- [4
  References](#references)


## Use cases\[<a href="/wiki/index.php?title=MSDGW_F&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Use cases">edit</a> \| (./index.php.md)\]

- Recommended for
  [ALGO](ALGO.md)=EVG0W\[R\|RK\]\|CRPA\[R\|RK\]:

The compression can be used for all type of [GW
calculations](../methods/Practical_guide_to_GW_calculations.md)
regardless if the calculation is performed in steps or in the all-in-one
mode. Following lines in stdout and [OUTCAR](../output-files/OUTCAR.md)
indicate that the compression has been performed:

     => avg. energy ratio F (%):  1.00                                                                                                                                                                                                                                                                                          
     bands after compression:      240  

To test different compression settings, it is recommended perform the
GW/CRPA calculation in steps and to set
MSDGW_F only in the actual GW
step. This avoids repeating the expensive exact diagonalization of the
Kohn-Sham Hamiltonian.

## Caveats\[<a href="/wiki/index.php?title=MSDGW_F&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Caveats">edit</a> \| (./index.php.md)\]

Care must be taken for GW/(c)RPA calculations that are performed in
steps and include the long-wave limit stored in
[WAVEDER](../input-files/WAVEDER.md). After band compression, this limit
must be re-calculated by setting [LOPTICS](LOPTICS.md) in
combination with [LPEAD](LPEAD.md).

## Related tags and articles\[<a href="/wiki/index.php?title=MSDGW_F&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[MSDGW_NXI](../methods/MSDGW_NXI.md),
[MSDGW_SEED](../methods/MSDGW_SEED.md),
[MSDGW_NP](../methods/MSDGW_NP.md)

## References\[<a href="/wiki/index.php?title=MSDGW_F&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^altman:prl:2024-1]: [Altman, A. R. and Kundu, S. and da Jornada, F. H., *Mixed Stochastic-Deterministic Approach for Many-Body Perturbation Theory Calculations*, Phys. Rev. Lett. **132**, 086401 (2024).](https://doi.org/10.1103/PhysRevLett.132.086401)
