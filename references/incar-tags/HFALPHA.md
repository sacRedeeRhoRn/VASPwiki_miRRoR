<!-- Source: https://vasp.at/wiki/index.php/HFALPHA | revid: 21505 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# HFALPHA


HFALPHA = \[real\] 

|  |  |  |
|----|----|----|
| Default: **HFALPHA** | = 6/sqrt(<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>)/(2π) | if [HFRCUT](HFRCUT.md) is 0 |

Description: HFALPHA sets the
decay constant used in the method of Massida, Posternak, and
Baldereschi, which is activated by [HFRCUT](HFRCUT.md)=0.

------------------------------------------------------------------------

HFALPHA sets the decay
constant in the error-function-like charge distribution for the method
of Massida, Posternak, and
Baldereschi<sup>[\[1\]](#cite_note-massidda:prb:93-1)</sup>.
The error-function-like charge distribution is used to calculate the
difference between the isolated probe charge and the periodically
repeated probe charge in a homogenous background. The default for
HFALPHA is
6/sqrt(<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>)/(2π)
in atomic units. This usually yields robust and accurate results in the
range of meV compared to the Ewald summation used for a regular k-mesh.
This is the default approach used to implement the convergence
corrections of the [Coulomb
singularity](../methods/Coulomb_singularity.md) in
Hartree-Fock calculations. This does not work correctly for
bandstructure calculations using the [0-weight
scheme](../misc/Si_HSE_bandstructure.md) or
[KPOINTS_OPT](../input-files/KPOINTS_OPT.md) because the correction is
only applied for points in the regular grid. To overcome this problem we
recommend using the Coulomb truncation methods using
[HFRCUT](HFRCUT.md).

## Related tags and articles\[<a href="/wiki/index.php?title=HFALPHA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[AEXX](AEXX.md), [ALDAX](ALDAX.md),
[ALDAC](ALDAC.md), [AGGAX](AGGAX.md),
[AGGAC](AGGAC.md), [AMGGAX](AMGGAX.md),
[AMGGAC](AMGGAC.md), [LHFCALC](LHFCALC.md),
[HFRCUT](HFRCUT.md), [LTHOMAS](LTHOMAS.md),
[List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md),
[Coulomb singularity](../methods/Coulomb_singularity.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-HFALPHA-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=HFALPHA&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-massidda:prb:93_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.48.5058" class="external text"
    rel="nofollow">S. Massidda, M. Posternak, and A. Baldereschi, Phys. Rev.
    B <strong>48</strong>, 5058 (1993).</a>


