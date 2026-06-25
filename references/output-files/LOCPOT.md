<!-- Source: https://vasp.at/wiki/index.php/LOCPOT | revid: 37157 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LOCPOT


The LOCPOT file stores the
local potential (in eV). The definition of the written local potential
depends on the settings for [LVTOT](../incar-tags/LVTOT.md),
[LVHAR](../incar-tags/LVHAR.md), and
[WRT_POTENTIAL](../incar-tags/WRT_POTENTIAL.md).

The format is similar to that of the [CHGCAR](../input-files/CHGCAR.md)
file, but it does not have the same data arrangement. For
spin-unpolarized calculations ([ISPIN](../incar-tags/ISPIN.md)=1,
[LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)=F), it contains a
single dataset with the scalar potential. For spin-polarized
calculations ([ISPIN](../incar-tags/ISPIN.md)=2), it contains two datasets:
spin up and spin down. For noncollinear calculations
([LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)=T), it contains
four datasets in the spinor representation of the potential. In other
words, it contains the scalar potential and the B-field-like potential
$B_1$, $B_2$, and
$B_3$ in the basis defined by
[SAXIS](../incar-tags/SAXIS.md) (see [LOCPOT-format issue for
VASP\<6.4.3](../misc/Known_issues.md)).

|  |
|----|
| **Warning:** Note for versions older than vasp.5.1.12: please check whether your version supports this tag (it is written out at the beginning of the OUTCAR file). Versions not supporting [LVHAR](../incar-tags/LVHAR.md) might or not add $V_{\text{XC}}(\mathbf{r})$. Please check this by searching for `LEXCHG=-1` in `main.F`. If the line `LEXCHG=-1` is commented out $V_{\text{XC}}(\mathbf{r})$ is added otherwise it is not. |

## Related tags and articles\[<a href="/wiki/index.php?title=LOCPOT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Restart and output files cheat
sheet](../tutorials/Restart_and_output_files_cheat_sheet.md)

[LVACPOTAV](../incar-tags/LVACPOTAV.md), [LVTOT](../incar-tags/LVTOT.md),
[LVHAR](../incar-tags/LVHAR.md),
[WRT_POTENTIAL](../incar-tags/WRT_POTENTIAL.md),
[POT](POT.md)


