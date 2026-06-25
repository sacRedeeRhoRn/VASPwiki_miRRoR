<!-- Source: https://vasp.at/wiki/index.php/Restart_and_output_files_cheat_sheet | revid: 37187 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Restart and output files cheat sheet


VASP can continue a calculation from the converged results of a previous
run instead of restarting the electronic minimization from scratch. The
wavefunctions are reused through [ISTART](../incar-tags/ISTART.md) and the
charge density through [ICHARG](../incar-tags/ICHARG.md); some methods
additionally need the kinetic energy density or the local potential. The
files that store these quantities are the *restart files*.

The restart files are [WAVECAR](../input-files/WAVECAR.md)
(wavefunctions), [CHGCAR](../input-files/CHGCAR.md) (charge density
together with the PAW one-center occupancies),
[TAUCAR](../input-files/TAUCAR.md) (kinetic energy density, for meta-GGA
functionals), and [POT](../output-files/POT.md) (local potential, for OEP
calculations). Alternatively, these quantities are written to the single
HDF5 file [vaspwave.h5](../output-files/Vaspwave.h5.md). The restart
files differ from analysis and visualization output such as
[CHG](../output-files/CHG.md), [LOCPOT](../output-files/LOCPOT.md),
[DOSCAR](../output-files/DOSCAR.md), or
[vasprun.xml](../output-files/Vasprun.xml.md): the latter store derived
or reduced quantities (for example, [CHG](../output-files/CHG.md) omits the PAW
one-center occupancies) and are not read back to continue a calculation.

Which restart files are written, and whether in the legacy format or in
[vaspwave.h5](../output-files/Vaspwave.h5.md), is controlled by
[LWAVE](../incar-tags/LWAVE.md), [LCHARG](../incar-tags/LCHARG.md),
[LTAU](../incar-tags/LTAU.md), [LVTOT](../incar-tags/LVTOT.md),
[LH5](../incar-tags/LH5.md), and [LCHARGH5](../incar-tags/LCHARGH5.md).


## Contents


- [1 How the tags
  interact](#how-the-tags-interact)
  - [1.1
    Defaults](#defaults)
- [2 Overview
  table](#overview-table)
- [3 Recognizing
  which restart file was
  read](#recognizing-which-restart-file-was-read)
- [4 Related tags
  and articles](#related-tags-and-articles)


## How the tags interact\[<a
href="/wiki/index.php?title=Restart_and_output_files_cheat_sheet&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: How the tags interact">edit</a> \| (./index.php.md)\]

[LWAVE](../incar-tags/LWAVE.md), [LCHARG](../incar-tags/LCHARG.md),
[LTAU](../incar-tags/LTAU.md), and [LVTOT](../incar-tags/LVTOT.md) decide
**whether** the wavefunctions, the charge density, the kinetic energy
density, and the local potential are written. [LH5](../incar-tags/LH5.md)
decides the **format**: the legacy files for
[`LH5`](../incar-tags/LH5.md)` = .FALSE.`, or
[vaspwave.h5](../output-files/Vaspwave.h5.md) for
[`LH5`](../incar-tags/LH5.md)` = .TRUE.`, which suppresses the legacy files
entirely. [LCHARGH5](../incar-tags/LCHARGH5.md) is the exception: rather
than switching the format, it writes the charge density to
[vaspwave.h5](../output-files/Vaspwave.h5.md) *in addition*, so that
the density is available for plotting with
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> while the restart
information is still written to the legacy files.

The files are written according to the following rules:

- [WAVECAR](../input-files/WAVECAR.md) —
  [`LWAVE`](../incar-tags/LWAVE.md)` = .TRUE.` and
  [`LH5`](../incar-tags/LH5.md)` = .FALSE.`; the
  [vaspwave.h5](../output-files/Vaspwave.h5.md) group `/wave` —
  [`LWAVE`](../incar-tags/LWAVE.md)` = .TRUE.` and
  [`LH5`](../incar-tags/LH5.md)` = .TRUE.`
- [CHGCAR](../input-files/CHGCAR.md) —
  [`LCHARG`](../incar-tags/LCHARG.md)` = .TRUE.` and
  [`LH5`](../incar-tags/LH5.md)` = .FALSE.`; the
  [vaspwave.h5](../output-files/Vaspwave.h5.md) group `/charge` —
  [`LCHARGH5`](../incar-tags/LCHARGH5.md)` = .TRUE.`
- [TAUCAR](../input-files/TAUCAR.md) — like
  [CHGCAR](../input-files/CHGCAR.md), but additionally requires
  [`LTAU`](../incar-tags/LTAU.md)` = .TRUE.`; the
  [vaspwave.h5](../output-files/Vaspwave.h5.md) group
  `/kinetic_energy_density` follows the `/charge` rule.
  [LTAU](../incar-tags/LTAU.md) defaults to
  [`LTAU`](../incar-tags/LTAU.md)` = .TRUE.` for meta-GGA functionals.
- [POT](../output-files/POT.md) — [`LVTOT`](../incar-tags/LVTOT.md)` = .TRUE.` and
  [`LH5`](../incar-tags/LH5.md)` = .FALSE.`; the
  [vaspwave.h5](../output-files/Vaspwave.h5.md) group `/potential`
  requires [`LVTOT`](../incar-tags/LVTOT.md)` = .TRUE.` and
  [`LH5`](../incar-tags/LH5.md)` = .TRUE.`. Only OEP and hybrid-functional
  OEP calculations write [POT](../output-files/POT.md).

### Defaults\[<a
href="/wiki/index.php?title=Restart_and_output_files_cheat_sheet&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Defaults">edit</a> \| (./index.php.md)\]

The defaults of [LWAVE](../incar-tags/LWAVE.md),
[LCHARG](../incar-tags/LCHARG.md), [LH5](../incar-tags/LH5.md), and
[LVTOT](../incar-tags/LVTOT.md) are fixed and do not depend on the other
tags:

- [`LWAVE`](../incar-tags/LWAVE.md)` = .TRUE.`
- [`LCHARG`](../incar-tags/LCHARG.md)` = .TRUE.`
- [`LH5`](../incar-tags/LH5.md)` = .FALSE.`
- [`LVTOT`](../incar-tags/LVTOT.md)` = .FALSE.`

[LTAU](../incar-tags/LTAU.md) defaults to
[`LTAU`](../incar-tags/LTAU.md)` = .TRUE.` for meta-GGA functionals that
need the kinetic energy density, and to
[`LTAU`](../incar-tags/LTAU.md)` = .FALSE.` otherwise.
[LCHARGH5](../incar-tags/LCHARGH5.md) also has no fixed default: when it
is not set, its value is [LH5](../incar-tags/LH5.md) `.AND.`
[LCHARG](../incar-tags/LCHARG.md). As a result, switching to HDF5 output
with [`LH5`](../incar-tags/LH5.md)` = .TRUE.` writes the charge density to
[vaspwave.h5](../output-files/Vaspwave.h5.md) automatically (as long as
[`LCHARG`](../incar-tags/LCHARG.md)` = .TRUE.`), while an explicit
[`LCHARGH5`](../incar-tags/LCHARGH5.md)` = .FALSE.` suppresses it.

|  |
|----|
| **Tip:** To plot the charge density with <a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> while still writing restart information to the legacy [WAVECAR](../input-files/WAVECAR.md), set [`LCHARGH5`](../incar-tags/LCHARGH5.md)` = .TRUE.` together with [`LH5`](../incar-tags/LH5.md)` = .FALSE.`. |

## Overview table\[<a
href="/wiki/index.php?title=Restart_and_output_files_cheat_sheet&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Overview table">edit</a> \| (./index.php.md)\]

The table gives an overview of written restart files for every
combination of effective (i.e., after applying the defaults) tag values.
✓ marks a written file, — a file that is not written. The highlighted
row is the default configuration. The kinetic energy density
([TAUCAR](../input-files/TAUCAR.md)) and the OEP local potential
([POT](../output-files/POT.md)) follow the same pattern as the charge density,
additionally gated by [LTAU](../incar-tags/LTAU.md) and
[LVTOT](../incar-tags/LVTOT.md).

|  |  |  |  |  |  |  |  |
|----|----|----|----|----|----|----|----|
| [LWAVE](../incar-tags/LWAVE.md) | [LCHARG](../incar-tags/LCHARG.md) | [LH5](../incar-tags/LH5.md) | [LCHARGH5](../incar-tags/LCHARGH5.md) | [WAVECAR](../input-files/WAVECAR.md) | [CHGCAR](../input-files/CHGCAR.md) | [vaspwave.h5](../output-files/Vaspwave.h5.md) /wave | [vaspwave.h5](../output-files/Vaspwave.h5.md) /charge |
| .TRUE. | .TRUE. | .FALSE. | .FALSE. | ✓ | ✓ | — | — |
| .TRUE. | .TRUE. | .FALSE. | .TRUE. | ✓ | ✓ | — | ✓ |
| .TRUE. | .FALSE. | .FALSE. | .FALSE. | ✓ | — | — | — |
| .TRUE. | .FALSE. | .FALSE. | .TRUE. | ✓ | — | — | ✓ |
| .FALSE. | .TRUE. | .FALSE. | .FALSE. | — | ✓ | — | — |
| .FALSE. | .TRUE. | .FALSE. | .TRUE. | — | ✓ | — | ✓ |
| .FALSE. | .FALSE. | .FALSE. | .FALSE. | — | — | — | — |
| .FALSE. | .FALSE. | .FALSE. | .TRUE. | — | — | — | ✓ |
| .TRUE. | .TRUE. | .TRUE. | .FALSE. | — | — | ✓ | — |
| .TRUE. | .TRUE. | .TRUE. | .TRUE. | — | — | ✓ | ✓ |
| .TRUE. | .FALSE. | .TRUE. | .FALSE. | — | — | ✓ | — |
| .TRUE. | .FALSE. | .TRUE. | .TRUE. | — | — | ✓ | ✓ |
| .FALSE. | .TRUE. | .TRUE. | .FALSE. | — | — | — | — |
| .FALSE. | .TRUE. | .TRUE. | .TRUE. | — | — | — | ✓ |
| .FALSE. | .FALSE. | .TRUE. | .FALSE. | — | — | — | — |
| .FALSE. | .FALSE. | .TRUE. | .TRUE. | — | — | — | ✓ |

Restart files written for each effective tag combination (wavefunctions
and charge density)

|  |
|----|
| **Mind:** The tag [LWAVEH5](../incar-tags/LWAVEH5.md) has no effect in current versions of VASP and is ignored. Use [LH5](../incar-tags/LH5.md) to redirect the wavefunctions to [vaspwave.h5](../output-files/Vaspwave.h5.md). |

|  |
|----|
| **Mind:** Reading the charge density back from [vaspwave.h5](../output-files/Vaspwave.h5.md) is not yet implemented. A fixed-density restart ([`ICHARG`](../incar-tags/ICHARG.md)` = 11`) cannot use a [vaspwave.h5](../output-files/Vaspwave.h5.md) that was written with [`LH5`](../incar-tags/LH5.md)` = .TRUE.`; write the [CHGCAR](../input-files/CHGCAR.md) for such restarts. See [Known issues#KnownIssue73](../misc/Known_issues.md). |

|  |
|----|
| **Mind:** This page describes VASP 6.5 and later. HDF5 output ([vaspwave.h5](../output-files/Vaspwave.h5.md)) is available as of VASP 6.0, and additional datasets are written as of VASP 6.6.0. In VASP 6.0 to 6.4.2 the default of [LCHARG](../incar-tags/LCHARG.md) was `.NOT.`[LH5](../incar-tags/LH5.md), and some combinations with [`LH5`](../incar-tags/LH5.md)` = .TRUE.` still wrote the legacy [CHGCAR](../input-files/CHGCAR.md). |

## Recognizing which restart file was read\[<a
href="/wiki/index.php?title=Restart_and_output_files_cheat_sheet&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Recognizing which restart file was read">edit</a> \| (./index.php.md)\]

At startup VASP reports on the standard output which restart files it
found and read, just before the `entering main loop` line. The excerpts
below are for the wavefunction and charge-density restart.

No restart file present — the wavefunctions are initialized from scratch
and the charge density from overlapping atoms:

     WAVECAR not read
     entering main loop

Wavefunctions read from [WAVECAR](../input-files/WAVECAR.md)
([`ISTART`](../incar-tags/ISTART.md)` = 1`); the charge density is then
built from these wavefunctions:

     found WAVECAR, reading the header
     reading WAVECAR
     the WAVECAR file was read successfully
     initial charge from wavefunction
     entering main loop

Wavefunctions and charge density read from the legacy files
([`ISTART`](../incar-tags/ISTART.md)` = 1`,
[`ICHARG`](../incar-tags/ICHARG.md)` = 1`):

     found WAVECAR, reading the header
     reading WAVECAR
     the WAVECAR file was read successfully
     charge density read from file: CHGCAR, restart
     entering main loop

Wavefunctions read from [vaspwave.h5](../output-files/Vaspwave.h5.md)
([`LH5`](../incar-tags/LH5.md)` = .TRUE.`,
[`ISTART`](../incar-tags/ISTART.md)` = 1`):

     found vaspwave.h5, reading the header of group: wave
     reading vaspwave.h5
     found vaspwave.h5, reading group = wave
     the vaspwave.h5 file was read successfully
     initial charge from wavefunction
     entering main loop

Here the charge density is taken from the wavefunctions (*initial charge
from wavefunction*); the charge density stored in
[vaspwave.h5](../output-files/Vaspwave.h5.md) is not read (see [Known
issues#KnownIssue73](../misc/Known_issues.md)).

## Related tags and articles\[<a
href="/wiki/index.php?title=Restart_and_output_files_cheat_sheet&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

Files: [WAVECAR](../input-files/WAVECAR.md),
[CHGCAR](../input-files/CHGCAR.md), [CHG](../output-files/CHG.md),
[TAUCAR](../input-files/TAUCAR.md), [POT](../output-files/POT.md),
[LOCPOT](../output-files/LOCPOT.md),
[vaspwave.h5](../output-files/Vaspwave.h5.md)

Tags: [LWAVE](../incar-tags/LWAVE.md), [LCHARG](../incar-tags/LCHARG.md),
[LCHARGH5](../incar-tags/LCHARGH5.md), [LTAU](../incar-tags/LTAU.md),
[LVTOT](../incar-tags/LVTOT.md), [LH5](../incar-tags/LH5.md),
[ISTART](../incar-tags/ISTART.md), [ICHARG](../incar-tags/ICHARG.md)


