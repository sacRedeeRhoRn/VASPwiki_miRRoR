<!-- Source: https://vasp.at/wiki/index.php/POT | revid: 37315 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# POT


The POT file contains the
total local potential (in eV), including the PAW augmentation part. It
is written for optimized-effective-potential (OEP)-type calculations —
such as the local Hartree-Fock and EXX-OEP methods, when
[`LVTOT`](../incar-tags/LVTOT.md)` = True`, and it stores the local
potential as the restart quantity for such calculations.

As of VASP 6.6.0, [`LVTOT`](../incar-tags/LVTOT.md)` = True` together with
[`LH5`](../incar-tags/LH5.md)` = True` writes the content of the
POT file to the restart file
[vaspwave.h5](Vaspwave.h5.md) instead. When restarting,
a legacy POT file is used in
preference to [vaspwave.h5](Vaspwave.h5.md) if both are
present.

|  |
|----|
| **Tip:** If you are interested in the local potential as a quantity (and not in restarting a calculation), use the [LOCPOT](LOCPOT.md) file and/or the [WRT_POTENTIAL](../incar-tags/WRT_POTENTIAL.md) tag instead. |

## Format\[<a href="/wiki/index.php?title=POT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Format">edit</a> \| (./index.php.md)\]

The POT file uses the same
block format as the [CHGCAR](../input-files/CHGCAR.md) file, with the
potential (in eV) in place of the charge density. Each block consists
of:

- Structure in [POSCAR](../input-files/POSCAR.md) format
- FFT-grid dimensions [NGXF](../incar-tags/NGXF.md),
  [NGYF](../incar-tags/NGYF.md), [NGZF](../incar-tags/NGZF.md)
- The local potential on the FFT grid, written with multiple real
  numbers per line (data runs fastest over NX, slowest over NZ, as for
  [CHGCAR](../input-files/CHGCAR.md))
- The PAW augmentation part

Unlike [CHGCAR](../input-files/CHGCAR.md), which stores the charge density
and magnetization, the potential is written in the following spin
representation:

- Non-spin-polarized calculations: a single block with the total local
  potential.
- Collinear spin-polarized calculations
  ([`ISPIN`](../incar-tags/ISPIN.md)` = 2`): two blocks, the spin-up and
  spin-down potentials.
- Noncollinear calculations
  ([`LNONCOLLINEAR`](../incar-tags/LNONCOLLINEAR.md)` = True`): the
  (density, magnetization) representation, i.e., the scalar potential
  and the three components of the magnetic field, in the spinor basis
  set by [SAXIS](../incar-tags/SAXIS.md).

Each potential block is followed by its corresponding PAW augmentation
part.

|  |
|----|
| **Warning:** The augmentation occupancies are written up to the *l*-quantum number set by [LMAXMIX](../incar-tags/LMAXMIX.md). See [LMAXMIX](../incar-tags/LMAXMIX.md) for the consequences of restarting without the appropriate one-center occupancies. |

## Related tags and articles\[<a href="/wiki/index.php?title=POT&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Restart and output files cheat
sheet](../tutorials/Restart_and_output_files_cheat_sheet.md)

[CHGCAR](../input-files/CHGCAR.md), [LOCPOT](LOCPOT.md),
[vaspwave.h5](Vaspwave.h5.md),
[LVTOT](../incar-tags/LVTOT.md), [LVHAR](../incar-tags/LVHAR.md),
[WRT_POTENTIAL](../incar-tags/WRT_POTENTIAL.md),
[LH5](../incar-tags/LH5.md), [LMAXMIX](../incar-tags/LMAXMIX.md)


