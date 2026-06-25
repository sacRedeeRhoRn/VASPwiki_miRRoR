<!-- Source: https://vasp.at/wiki/index.php/LVTOT | revid: 27052 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LVTOT


LVTOT = \[logical\]  
Default: **LVTOT** = .FALSE. 

Description: Determines whether the total local potential
$V_{\text{LOCPOT}}(\mathbf{r})$ (in eV) is written to
the [LOCPOT](../output-files/LOCPOT.md) file.

------------------------------------------------------------------------

$V_{\text{LOCPOT}}(\mathbf{r}) = V_{\text{ionic}}(\mathbf{r}) + \int
\frac{n(\mathbf{r'})}{|\mathbf{r}-\mathbf{r'}|}d\mathbf{r'}+
V_{\text{xc}}(\mathbf{r})$

where $V_{\text{ionic}}(\mathbf{r})$ is the ionic potential, the second term is the Hartree
potential, and $V_{\text{xc}}(\mathbf{r})$ is the (semi-)local exchange-correlation potential.

If LVTOT=.TRUE., the
$V_{\text{LOCPOT}}(\mathbf{r})$ is written to the
[LOCPOT](../output-files/LOCPOT.md) file and the [POT](../output-files/POT.md)
file. The [POT](../output-files/POT.md) file additionally contains the
augmentation part.

|  |
|----|
| **Warning:** [LVHAR](LVHAR.md)=T changes the content of the [LOCPOT](../output-files/LOCPOT.md) file. |

[WRT_POTENTIAL](WRT_POTENTIAL.md) also gives access
to the total local potential and offers more options.

## Related tags and articles\[<a href="/wiki/index.php?title=LVTOT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[Computing the work
function](../tutorials/Computing_the_work_function.md),
[LVHAR](LVHAR.md), [LOCPOT](../output-files/LOCPOT.md),
[WRT_POTENTIAL](WRT_POTENTIAL.md),
[LVACPOTAV](LVACPOTAV.md), [POT](../output-files/POT.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LVTOT-_incategory-Examples)

------------------------------------------------------------------------


