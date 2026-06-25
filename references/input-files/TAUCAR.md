<!-- Source: https://vasp.at/wiki/index.php/TAUCAR | revid: 37155 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# TAUCAR


The TAUCAR file stores
kinetic-energy density

$\tilde \tau_{\sigma\sigma'} = \frac{\hbar^2}{2m} \sum_{n\mathbf{k}}
f_{n\mathbf{k}} \mathbf{\nabla} \tilde \psi_{n\mathbf{k}\sigma} \cdot
\nabla \tilde \psi_{n\mathbf{k}\sigma'}$

in VASP units (eV $\AA^{-3}$),
i.e. the valence contribution of the pseudo expectation value on the
plane-wave grid. Here, $\mathbf{\nabla} \tilde
\psi_{n\mathbf{k}\sigma}$ is the gradient of the
pseudo Kohn-Sham orbitals within the
<a href="/wiki/PAW_method" class="mw-redirect" title="PAW method">PAW
method</a>. The TAUCAR file is
written by default for a [metaGGA](../incar-tags/METAGGA.md) calculation,
but it can also be written for
<a href="/wiki/XC_functionals" class="mw-redirect"
title="XC functionals">XC functionals</a> that are independent of
$\tau$ by setting [`LTAU`](../incar-tags/LTAU.md)` = T`. The
kinetic energy density can also be redirected to
[vaspwave.h5](../output-files/Vaspwave.h5.md) using
[LH5](../incar-tags/LH5.md).

To avoid writing $\tau$ for a
[metaGGA](../incar-tags/METAGGA.md) calculation use
[`LCHARG`](../incar-tags/LCHARG.md)` = F`. This controls the writing of
both the charge density and the kinetic energy density.

The TAUCAR file (together with
the [CHGCAR](CHGCAR.md) file) can be read to restart a
calculation ([ICHARG](../incar-tags/ICHARG.md)).

|  |
|----|
| **Tip:** We recommend starting from the density files when repeatedly restarting with small changes in the input parameters, e.g., the **k**-point mesh ([KPOINTS](KPOINTS.md)). |

|  |
|----|
| **Mind:** Available as of VASP 6.6. |

## Format\[<a href="/wiki/index.php?title=TAUCAR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Format">edit</a> \| (./index.php.md)\]

The format is the same as the [CHGCAR](CHGCAR.md) file
except for the lack of augmentation occupancies. In other words the
TAUCAR file consists of the
following block:

- Structure in [POSCAR](POSCAR.md) format
- FFT-grid dimensions [NGXF](../incar-tags/NGXF.md),
  [NGYF](../incar-tags/NGYF.md), [NGZF](../incar-tags/NGZF.md)
- Kinetic energy density

### Magnetic calculations\[<a href="/wiki/index.php?title=TAUCAR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Magnetic calculations">edit</a> \| (./index.php.md)\]

For magnetic calculations, the
TAUCAR file contains
additional data blocks for the magnetic part of
$\tau$. In particular, for spin-polarized calculations
([ISPIN](../incar-tags/ISPIN.md)=2), the first set contains the total
kinetic energy density (spin up + spin down) and the second one is the
magnetization density (spin up - spin down). For noncollinear
calculation ([LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)=T), it
contains the total charge density and the magnetic part
$\tau_m$ in the spinor basis set by
[SAXIS](../incar-tags/SAXIS.md).

## Related tags and articles\[<a href="/wiki/index.php?title=TAUCAR&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Restart and output files cheat
sheet](../tutorials/Restart_and_output_files_cheat_sheet.md)

[CHGCAR](CHGCAR.md), [LTAU](../incar-tags/LTAU.md),
[ICHARG](../incar-tags/ICHARG.md),

FFT-grid dimensions: [ENCUT](../incar-tags/ENCUT.md),
[NGXF](../incar-tags/NGXF.md), [NGYF](../incar-tags/NGYF.md),
[NGZF](../incar-tags/NGZF.md)


