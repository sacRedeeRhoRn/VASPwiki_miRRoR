<!-- Source: https://vasp.at/wiki/index.php/LMIXTAU | revid: 29384 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LMIXTAU


LMIXTAU = .TRUE. \| .FALSE.  
Default: **LMIXTAU** = .FALSE. 

Description: send the kinetic-energy density through the
<a href="/wiki/Density_mixing" class="mw-redirect"
title="Density mixing">density mixer</a> as well.

------------------------------------------------------------------------

In many cases, the <a href="/wiki/Density_mixing" class="mw-redirect"
title="Density mixing">density-mixing scheme</a> works well enough
without passing the kinetic-energy density through the mixer. Therefore
VASP uses LMIXTAU=.FALSE. per
default. However, when the self-consistency cycle fails to converge for
one of the algorithms exploiting
<a href="/wiki/Density_mixing" class="mw-redirect"
title="Density mixing">density mixing</a>, e.g,
[IALGO](IALGO.md)=38 or 48, we recommend setting
LMIXTAU=.TRUE..

## Related tags and articles\[<a href="/wiki/index.php?title=LMIXTAU&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[METAGGA](METAGGA.md), [LMAXTAU](LMAXTAU.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LMIXTAU-_incategory-Examples)

------------------------------------------------------------------------


