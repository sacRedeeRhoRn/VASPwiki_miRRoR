<!-- Source: https://vasp.at/wiki/index.php/LVHAR | revid: 24756 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LVHAR
LVHAR = \[logical\]  
Default: **LVHAR** = .FALSE. 

Description: Determines whether the local potential
$V_{\text{ionic}}(\mathbf{r})
+V_{\text{hartree}}(\mathbf{r})$ (in eV) is written to the
[LOCPOT](../output-files/LOCPOT.md) file.

------------------------------------------------------------------------

$V_{\text{ionic}}(\mathbf{r})+V_{\text{hartree}}(\mathbf{r}) =
V_{\text{ionic}}(\mathbf{r}) + \int
\frac{n(\mathbf{r'})}{|\mathbf{r}-\mathbf{r'}|}d\mathbf{r'}$

where $V_{\text{ionic}}(\mathbf{r})$ is
the ionic potential as mimicked by the pseudopotentials and
$V_{\text{hartree}}(\mathbf{r})$ is the
Hartree potential.

The local potential is written to the [LOCPOT](../output-files/LOCPOT.md)
file and hence to the same file as the local potential for
[LVTOT](LVTOT.md)=T. Carefully check that the
[LOCPOT](../output-files/LOCPOT.md) file contains the potential you expect.
[WRT_POTENTIAL](WRT_POTENTIAL.md) also gives access
to the ionic and Hartree potentials and offers more options.

|  |
|----|
| **Warning:** Setting LVHAR=True will set [LVTOT](LVTOT.md)=False. |

See [LOCPOT](../output-files/LOCPOT.md) to find out how to write
$V_{\text{ionic}}(\mathbf{r})
+V_{\text{hartree}}(\mathbf{r})$ in VASP \< 5.2.12.

## Related tags and articles
[Computing the work
function](../tutorials/Computing_the_work_function.md),
[LVTOT](LVTOT.md), [LOCPOT](../output-files/LOCPOT.md),
[WRT_POTENTIAL](WRT_POTENTIAL.md),
[LVACPOTAV](LVACPOTAV.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LVHAR-_incategory-Examples)
