<!-- Source: https://vasp.at/wiki/index.php/DAMP_NEWTON | revid: 34930 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DAMP NEWTON


DAMP_NEWTON = real number 

|                          |       |         |
|--------------------------|-------|---------|
| Default: **DAMP_NEWTON** | = 0.8 |  |

Description: Sets the damping factor applied to the RPA forces during
Newton-step structure relaxation.

------------------------------------------------------------------------

DAMP_NEWTON controls the step
size of the Newton-step geometry update performed during
<a href="https://vasp.at/wiki/ACFDT/RPA_calculations"
class="external text" rel="nofollow">Random Phase Approximation</a>
(RPA) force calculations. The updated atomic positions are computed as:

**x**<sub>new</sub> = **x**<sub>current</sub> + DAMP_NEWTON ×
**H**<sup>−1</sup> · **F**<sub>RPA</sub>

where **H**<sup>−1</sup> is the inverse of the DFT Hessian (computed
during the RPA force calculation) and **F**<sub>RPA</sub> are the RPA
forces.<sup>[\[1\]](#cite_note-ramberger:prl:118-1)</sup>
The resulting updated positions are written to the
[CONTCAR](../output-files/CONTCAR.md) file (provided
[NSW](../incar-tags/NSW.md)=0). Iterating this procedure—by copying
[CONTCAR](../output-files/CONTCAR.md) to [POSCAR](../input-files/POSCAR.md)
and re-running—should converge the system toward its ground-state
structure.

|  |
|----|
| **Mind:** Available as of VASP 6.1.0 |


## Contents


- [1 Available
  options](#Available_options)
  - [1.1
    DAMP_NEWTON=1.0: No
    damping](#DAMP_NEWTON=1.0:_No_damping)
  - [1.2
    DAMP_NEWTON=0.8: Default
    damping](#DAMP_NEWTON=0.8:_Default_damping)
  - [1.3
    DAMP_NEWTON\<0.8: Strong
    damping](#DAMP_NEWTON%3C0.8:_Strong_damping)
- [2 Related tags
  and articles](#Related_tags_and_articles)
- [3
  References](#References)


## Available options\[<a
href="/wiki/index.php?title=DAMP_NEWTON&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Available options">edit</a> \| (./index.php.md)\]

### DAMP_NEWTON=1.0: No damping\[<a
href="/wiki/index.php?title=DAMP_NEWTON&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: DAMP_NEWTON=1.0: No damping">edit</a> \| (./index.php.md)\]

No damping is applied; the full Newton step is taken. This is
appropriate when the RPA forces

are well-behaved and the optimization is proceeding stably.

### DAMP_NEWTON=0.8: Default damping\[<a
href="/wiki/index.php?title=DAMP_NEWTON&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: DAMP_NEWTON=0.8: Default damping">edit</a> \| (./index.php.md)\]

The default value. A mild damping factor of 0.8 is applied to the Newton
step, providing a

small degree of stabilization during the iterative relaxation without
significantly slowing convergence.

### DAMP_NEWTON\<0.8: Strong damping\[<a
href="/wiki/index.php?title=DAMP_NEWTON&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: DAMP_NEWTON&lt;0.8: Strong damping">edit</a> \| (./index.php.md)\]

Use smaller values if numerical instabilities are observed during the
RPA relaxation.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vred); --box-emph-color: var(--vred); padding: 5px; color: var(--vdefault-text-nb); background: var(--vred-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vred);">Warning:</span></strong>
Excessively small values will slow convergence considerably. Reduce
<span class="mw-selflink selflink">DAMP_NEWTON</span>
<p>only when large or erratic RPA forces are encountered.</p></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a
href="/wiki/index.php?title=DAMP_NEWTON&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[CONTCAR](../output-files/CONTCAR.md), [POSCAR](../input-files/POSCAR.md),
[NSW](../incar-tags/NSW.md), [IBRION](../incar-tags/IBRION.md) [Workflows that
use RPA force
relaxation](https://vasp.at/wiki/index.php/Special-Search/-DAMP_NEWTON-_incategory-HowTo)

## References\[<a
href="/wiki/index.php?title=DAMP_NEWTON&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-ramberger:prl:118_1-0)
    <a href="https://doi.org/10.1103/PhysRevLett.118.106403"
    class="external text" rel="nofollow">B. Ramberger, T. Schäfer and G.
    Kresse, Phys. Rev. Lett <strong>118</strong>, 106403 (2017).</a>


