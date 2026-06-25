<!-- Source: https://vasp.at/wiki/index.php/LVGVAPPL | revid: 29601 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LVGVAPPL


LVGVAPPL = .TRUE. \| .FALSE.  
Default: **LVGVAPPL** = .FALSE. 

Description: LVGVAPPL
determines whether the *vGv* orbital magnetic susceptibility is applied
in the calculation of the CSA tensor.

LVGVAPPL is available as of
VASP.6.4.0.

------------------------------------------------------------------------

When performing a chemical shift calculation the standard *pGv*
susceptibility is used to calculate the $\mathbf{G=0}$
contribution to the CSA tensor by default. This can be overruled with
LVGVAPPL. In case
LVGVAPPL is true, the *vGv*
susceptibility is applied for the calculation of the
$\mathbf{G=0}$ contribution to the CSA tensor. For
details see [LVGVCALC](LVGVCALC.md).

## Related tags and articles\[<a href="/wiki/index.php?title=LVGVAPPL&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md),
[LVGVCALC](LVGVCALC.md)

------------------------------------------------------------------------


