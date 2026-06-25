<!-- Source: https://vasp.at/wiki/index.php/Vaspwave.h5 | revid: 37117 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# vaspwave.h5


The vaspwave.h5 file is the
hdf5 counterpart of the [WAVECAR](../input-files/WAVECAR.md) and
[CHGCAR](../input-files/CHGCAR.md) and other files used inside a more
elaborate workflow, like for instance GW. This file is written if
[LH5](../incar-tags/LH5.md)=.TRUE. is set in the [INCAR](../input-files/INCAR.md)
file.

|  |
|----|
| **Mind:** As of version 6.6.0 this files stores optionally following datasets. |

- energies and orbitals from [WAVECAR](../input-files/WAVECAR.md)
- charge density from [CHGCAR](../input-files/CHGCAR.md)
- optical transition elements from [WAVEDER](../input-files/WAVEDER.md)
- Wannier projection matrices [WANPROJ](../input-files/WANPROJ.md)
- local potential [POT](POT.md)

## Related tags and articles\[<a
href="/wiki/index.php?title=Vaspwave.h5&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Restart and output files cheat
sheet](../tutorials/Restart_and_output_files_cheat_sheet.md)

[LCHARGH5](../incar-tags/LCHARGH5.md), [LH5](../incar-tags/LH5.md),
[WAVECAR](../input-files/WAVECAR.md), [CHGCAR](../input-files/CHGCAR.md),
[WAVEDER](../input-files/WAVEDER.md), [WANPROJ](../input-files/WANPROJ.md),
[POT](POT.md)


