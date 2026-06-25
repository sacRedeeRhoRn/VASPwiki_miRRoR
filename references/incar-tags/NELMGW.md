<!-- Source: https://vasp.at/wiki/index.php/NELMGW | revid: 26712 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NELMGW


NELMGW = \[integer\]  
Default: **NELMGW** = 1 

Description: NELMGW sets the
number of self-consistent GW steps. Available as of 6.3.0.

------------------------------------------------------------------------

This tag is effective for [ALGO](ALGO.md)=EVGW\[0\] \|
QPGW\[0\] \| GW\[0\]\[R\]\[K\] and ignored otherwise. For instance

    ALGO = EVGW0
    NELMGW = 4

performs a <a href="/wiki/GW_calculations#gw0" class="mw-redirect"
title="GW calculations">partially self-consistent GW calculations</a>,
where $G$ is updated
four times.

Omit [NBANDS](NBANDS.md) and [NELM](NELM.md) to
select the
<a href="/wiki/GW_calculations#GW_in_one_go" class="mw-redirect"
title="GW calculations">single-step GW procedure</a>.

  

## Related tags and articles\[<a href="/wiki/index.php?title=NELMGW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ALGO](ALGO.md),
<a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW calculations</a>

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NELMGW-_incategory-Examples)

------------------------------------------------------------------------


