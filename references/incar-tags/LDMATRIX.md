<!-- Source: https://vasp.at/wiki/index.php/LDMATRIX | revid: 32893 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LDMATRIX


LDMATRIX = .TRUE. \| .FALSE.  
Default: **LDMATRIX** = .FALSE. 

Description: Computes the zero-field splitting (ZFS) matrix.

------------------------------------------------------------------------

To compute the zero-field-splitting (ZFS) tensor due to spin-spin
interactions in a collinear magnetic calculation
([`ISPIN`](ISPIN.md)` = 2`), set:

     LDMATRIX = True
     # sets default LHFCALC = True ; AEXX=0.0

The ZFS arises from spin-spin interactions between unpaired electrons in
a high-spin state with a total spin $S \geq 1$.
The ZFS matrix, also called D matrix, is measured in electron-spin
resonance (ESR) experiments and provides insights into the local
electronic environment of defect centers.

The implementation follows the formalism of Rayson and Briddon
(2008)<sup>[\[1\]](#cite_note-rayson:prb:2008-1)</sup>,
which efficiently evaluates the spin-spin interaction within periodic
density-functional theory (DFT) using reciprocal space methods. This
approach avoids expensive six-dimensional real-space integrations,
leading to a stable and computationally efficient method. The
expressions are similar to integrals used to evaluate the exact exchange
energies for [hybrid and HF-type
calculation](../methods/Category-Hybrid_functionals.md),
hence VASP sets [`LHFCALC`](LHFCALC.md)` = True`. This
still allows for simple DFT calculations
([`AEXX`](AEXX.md)` = 0.0` default), however mind that the
default symmetrization is [`ISYM`](ISYM.md)` = 3`.
LDMATRIX should not be
combined with [`ISYM`](ISYM.md)` = 1`, or `2`.


## Contents


- [1
  Output](#output)
- [2
  Advice](#advice)
- [3 Related tags
  an articles](#related-tags-an-articles)
- [4
  References](#references)


## Output\[<a href="/wiki/index.php?title=LDMATRIX&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Output">edit</a> \| (./index.php.md)\]

The computed zero-field splitting is written in MHz to the stdout:

     Jij:    -0.0003356     0.0003475    -0.0000119   965.1231107   965.1238969   965.1238508
    -Kij:    -0.0002748    -0.0000059     0.0002807    64.8471208    64.8472015    64.8471523
     D1c:    -0.0000541     0.0000275     0.0000267    11.1897131    11.1897125    11.1897272

and the [OUTCAR](../output-files/OUTCAR.md) file:

    Spin-spin contribution to zero-field splitting tensor (MHz)
    ---------------------------------------------------------------
         D_xx      D_yy      D_zz      D_xy      D_xz      D_yz 
    ---------------------------------------------------------------
         0.001     0.000    -0.001  1042.316  1020.260  1041.130
    ---------------------------------------------------------------

    after diagonalization
    ---------------------------------------------
        D_diag          eigenvector (x,y,z)
    ---------------------------------------------
     -1020.244      -0.697    -0.019     0.717
     -1048.926      -0.427     0.814    -0.393
      2069.171      -0.576    -0.580    -0.576
    ---------------------------------------------

## Advice\[<a href="/wiki/index.php?title=LDMATRIX&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Advice">edit</a> \| (./index.php.md)\]

- [Choice of PAW
  potentials](../tutorials/Choosing_pseudopotentials.md):
  The ZFS tensor values can be sensitive to the specific [PAW
  potential](../categories/Category-Pseudopotentials.md)
  used, as different
  [pseudopotentials](../categories/Category-Pseudopotentials.md)
  include varying number of electrons in the valence. In particular, it
  is crucial that the states that give rise to the magnetic moment are
  included.
- [NUPDOWN](NUPDOWN.md) tag can be used to obtain a
  high-spin state.
- The LDMATRIX implementation
  is best tested for `vasp_std`. A bug for `vasp_gam` with
  [`NCORE`](NCORE.md)` > 1` has been fixed, see [D-matrix
  broken for vasp_gam](../misc/Known_issues.md).

|  |
|----|
| **Warning:** LDMATRIX cannot be used with noncollinear magnetic calculations ([LNONCOLLINEAR](LNONCOLLINEAR.md) and/or [LSORBIT](LSORBIT.md)). |

- Spin-contamination corrections: Some users have modified the source
  code to include spin-contamination corrections, particularly for
  low-spin states ($S=0$).
  These modifications are *not* included in the default VASP version but
  can be implemented manually. See forum discussion:
  <a href="https://vasp.at/forum/viewtopic.php?p=29801p29801"
  class="external free"
  rel="nofollow">https://vasp.at/forum/viewtopic.php?p=29801p29801</a>

## Related tags an articles\[<a href="/wiki/index.php?title=LDMATRIX&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags an articles">edit</a> \| (./index.php.md)\]

[LHFCALC](LHFCALC.md), [NUPDOWN](NUPDOWN.md),
[ISPIN](ISPIN.md)

## References\[<a href="/wiki/index.php?title=LDMATRIX&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-rayson:prb:2008_1-0)
    <a href="https://doi.org/10.1103/PhysRevB.77.035119"
    class="external text" rel="nofollow">Rayson, M. J., and Briddon, P. R.,
    <em>First principles method for the calculation of zero-field splitting
    tensors in periodic systems</em>, Phys. Rev. B, <strong>77</strong>,
    035119 (2008).</a>


