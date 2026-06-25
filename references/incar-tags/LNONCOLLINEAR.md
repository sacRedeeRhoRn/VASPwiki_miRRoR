<!-- Source: https://vasp.at/wiki/index.php/LNONCOLLINEAR | revid: 36602 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LNONCOLLINEAR


LNONCOLLINEAR = .True. \|
.False. 

|  |  |  |
|----|----|----|
| Default: **LNONCOLLINEAR** | = .False. |  |
|  | = .True. | if spin-orbit coupling is included ([LSORBIT](LSORBIT.md)=.True.) |

Description: Switch on noncollinear magnetic calculations.

------------------------------------------------------------------------

For noncollinear magnetic calculations, set
LNONCOLLINEAR = True in the
[INCAR](../input-files/INCAR.md) file and use the `vasp_ncl` executable. The
electronic minimization treats the full 2x2 spin
density<sup>[\[1\]](#cite_note-hobbs:prb:00-1)</sup>

$n_{\sigma\sigma'}(\mathbf{r}) = \sum_{n=1}^N
\psi_{n\sigma}(\mathbf{r})\psi^\*_{n\sigma'}(\mathbf{r}),$

which is written to the [CHGCAR](../input-files/CHGCAR.md) file. In spinor
space, the part of the spin density proportional to the 2x2 unit matrix
corresponds to the charge density, and the part proportional to the
vector of Pauli matrices is the magnetization density. This enables the
consideration of noncollinear magnetic structures within
spin-density-functional theory. [MAGMOM](MAGMOM.md) sets the
initial magnetic moments. Write the final magnetic moments by setting
[LORBIT](LORBIT.md).

It is possible to **restart a noncollinear calculation** from a previous
nonmagnetic calculation ([ISPIN](ISPIN.md)=1 and
LNONCOLLINEAR=F) or
spin-polarized calculation ([ISPIN](ISPIN.md)=2) by reading
[WAVECAR](../input-files/WAVECAR.md) or [CHGCAR](../input-files/CHGCAR.md)
files. The magnetization of the spin-polarized calculation is
interpreted to point along [SAXIS](SAXIS.md) (default:
Cartesian direction $\hat z$). It
is not possible to rotate the magnetic moment locally on selected atoms
when restarting with a magnetization density. The magnetic configuration
can globally be rotated with respect to the lattice by restarting with a
different [SAXIS](SAXIS.md).

In practice, we recommend performing noncollinear calculations in two
steps:

- First, calculate the nonmagnetic ground state and generate a
  [WAVECAR](../input-files/WAVECAR.md) and a
  [CHGCAR](../input-files/CHGCAR.md) file.
- Second, read the [WAVECAR](../input-files/WAVECAR.md) and
  [CHGCAR](../input-files/CHGCAR.md) file, and supply initial magnetic
  moments using the [MAGMOM](MAGMOM.md) tag.

We recommend setting [GGA_COMPAT](GGA_COMPAT.md) = False
and [LASPH](LASPH.md)= True for noncollinear calculations
since this improves the numerical precision of calculations using the
generalized-gradient approximation (GGA).

Consider setting [AMIX_MAG](AMIX_MAG.md) and
[BMIX_MAG](BMIX_MAG.md) for better convergence when using
<a href="/wiki/Density_mixing" class="mw-redirect"
title="Density mixing">density mixing</a>.

The [I_CONSTRAINED_M](I_CONSTRAINED_M.md) tag can
constrain the on-site magnetic moments.

Supported as of VASP.4.5.

|  |
|----|
| **Important:** For noncollinear calculations [ISPIN](ISPIN.md) is ignored. In VASP 6.5.0, the calculation will exit with an error message if [ISPIN](ISPIN.md)=2 and [MAGMOM](MAGMOM.md) is used in combination with the LNONCOLLINEAR=.TRUE. |

## Related tags and articles\[<a
href="/wiki/index.php?title=LNONCOLLINEAR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[MAGMOM](MAGMOM.md), [LSORBIT](LSORBIT.md),
[SAXIS](SAXIS.md),
[GGA_COMPAT](GGA_COMPAT.md),
[LASPH](LASPH.md), [AMIX_MAG](AMIX_MAG.md),
[BMIX_MAG](BMIX_MAG.md),

  
[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LNONCOLLINEAR-_incategory-Examples)

------------------------------------------------------------------------


1.  [↑](#cite_ref-hobbs:prb:00_1-0)
    <a href="http://doi.org/10.1103/PhysRevB.62.11556" class="external text"
    rel="nofollow">Hobbs, D., G. Kresse, and J. Hafner, <em>Fully
    unconstrained noncollinear magnetism within the projector augmented-wave
    method.</em>, Phys. Rev. B <strong>62</strong>, 11556 (2000).</a>


