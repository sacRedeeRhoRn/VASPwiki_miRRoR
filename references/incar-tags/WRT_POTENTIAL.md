<!-- Source: https://vasp.at/wiki/index.php/WRT_POTENTIAL | revid: 34638 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# WRT_POTENTIAL
WRT_POTENTIAL = string  
Default: **WRT_POTENTIAL** = None 

Description: Select which component of the local potential to be written
as a post-processing step.

------------------------------------------------------------------------

WRT_POTENTIAL can select one or multiple local potentials on the
real-space grid in the unit cell to be written, e.g.,

     WRT_POTENTIAL = total

or

     WRT_POTENTIAL = hartree ionic

The output is written to [vaspout.h5](../output-files/Vaspout.h5.md) and
can be accessed either by
[py4vasp](https://vasp.at/py4vasp/latest/index.html) or HDF5
command-line tools (h5ls, h5dump).

      import py4vasp as pv
      calc = pv.Calculation.from_path(".")
      pot_dict = calc.potential.read("total")

The above allows the creation of a Python dictionary with the potential
data.

     h5ls -r vaspout.h5

The above shows the table of contents of
[vaspout.h5](../output-files/Vaspout.h5.md). Depending on the keywords
specified with WRT_POTENTIAL and the system it yields

     /results/potential       Group
     /results/potential/grid  Dataset {3}
     /results/potential/hartree Dataset {1, 24, 24, 24}
     /results/potential/ionic Dataset {1, 24, 24, 24}
     /results/potential/total Dataset {4, 24, 24, 24}
     /results/potential/xc    Dataset {4, 24, 24, 24}

The grid density can be increased by choosing a higher value for
[ENCUT](ENCUT.md) or explicitly by [NGXF](NGXF.md),
[NGYF](NGYF.md), [NGZF](NGZF.md).

The first dimension of the datasets in /results/potential is 1 for
nonmagnetic calculation, 2 for spin-polarized calculation, and 4 for
noncollinear calculations. In case the potential is scalar, i.e., has no
B-field-like contribution that couples to the magnetization, only the
1st component exists. Hence, for *hartree* and *ionic*, the first
dimension is 1. The components for the magnetic calculations correspond
to the spinor representation with the scalar potential in the first
component and the B-field in the second ([ISPIN](ISPIN.md)=2)
or $B_1$, $B_2$ and $B_3$ in the 2nd, 3rd and
4th component ([LNONCOLLINEAR](LNONCOLLINEAR.md)=T)
in the basis of Pauli matrices $\\\sigma_1$, $\sigma_2$,
$\mathbf{\sigma}_3\\$ given by
[SAXIS](SAXIS.md).

|  |
|----|
| **Mind:** As a convention, the $\mathbf{G}{{=}}0$ component in reciprocal-space representations of both, the Hartree and ionic, potentials are set to zero. This implies that considering the sum of the Hartree and ionic potentials is more meaningful to visualize than either potential individually. |

WRT_POTENTIAL can be run as a post-processing step by restarting from a
converged [CHGCAR](../input-files/CHGCAR.md) and setting
[ALGO](ALGO.md)=None. It is available for VASP \>= 6.4.3.

## Contents

- [1 Options to select](#Options_to_select)
  - [1.1 total](#total)
  - [1.2 hartree](#hartree)
  - [1.3 ionic](#ionic)
  - [1.4 xc](#xc)
  - [1.5 xcmu](#xcmu)
- [2 Related tags and articles](#Related_tags_and_articles)

## Options to select
### total
$V_{\text{total}}(\mathbf{r}) +
B_{\text{total}}(\mathbf{r}) = V_{\text{ionic}}(\mathbf{r}) +
V_{\text{hartree}}(\mathbf{r})+ V_{\text{xc}}(\mathbf{r}) +
B_{\text{xc}}(\mathbf{r})$

The output is written to `/results/potential/total`, as well as
[LOCPOT](../output-files/LOCPOT.md).

### hartree
$V_{\text{hartree}}(\mathbf{r}) = \int
\frac{n(\mathbf{r'})}{|\mathbf{r}-\mathbf{r'}|}d\mathbf{r'}$

The output is written to `/results/potential/hartree`.

### ionic
$V_{\text{ionic}}(\mathbf{r})$ as
mimicked by the pseudopotentials of the [PAW
method](../methods/Projector-augmented-wave_formalism.md).
The output is written to `/results/potential/ionic`.

### xc
$V_{\text{xc}}(\mathbf{r}) +
B_{\text{xc}}(\mathbf{r})$ as defined by the selected
[exchange-correlation
functional](../redirects/Exchange-correlation_functional.md).
The output is written to `/results/potential/xc`.

|  |
|----|
| **Mind:** This only corresponds to the (semi-)local functionals, i.e., LDA, GGA, non-local vdW-DF functionals, and does not account for either the potential $\mu$ associated with the kinetic energy density in [METAGGA](METAGGA.md) or the nonlocal Fock exchange considered in hybrid functionals. |

### xcmu
$\mu_{\text{xc}}(\mathbf{r}) +
\mathbf{\mu}_{m,\text{xc}}(\mathbf{r})$ is the scalar and
magnetic contribution of the [metaGGA](METAGGA.md)
potential associated to the kinetic-energy density as defined by the
selected [exchange-correlation
functional](../redirects/Exchange-correlation_functional.md).
The output is written to `/results/potential/xcmu`.

## Related tags and articles
[LVACPOTAV](LVACPOTAV.md), [LVTOT](LVTOT.md),
[LVHAR](LVHAR.md), WRT_POTENTIAL,
[LDIPOL](LDIPOL.md), [ENCUT](ENCUT.md),
[NGXF](NGXF.md), [NGYF](NGYF.md),
[NGZF](NGZF.md),
[WRT_DENSITY](WRT_DENSITY.md)
