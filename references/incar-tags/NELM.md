<!-- Source: https://vasp.at/wiki/index.php/NELM | revid: 25364 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NELM


NELM = \[integer\]  
Default: **NELM** = 60 

Description: NELM sets the
maximum number of electronic SC (self-consistency) steps.

------------------------------------------------------------------------

Normally, there is no need to change the default value: if the
self-consistency loop does not converge within 40 steps, it will
probably not converge at all. In this case you should reconsider the
tags [IALGO](IALGO.md) or [ALGO](ALGO.md),
[LSUBROT](LSUBROT.md), and the [mixing
parameters](../categories/Category-Density_mixing.md).

The same stands for [ALGO](ALGO.md) = TIMEEV, as the value is
set to be sufficient to ensure numerical stability when propagating in
time. If you wish to set it by yourself, be advised that the input value
must be greater than 100, otherwise VASP will ignore it and fall to the
default settings.

## Related tags and articles\[<a href="/wiki/index.php?title=NELM&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NELMDL](NELMDL.md), [NELMIN](NELMIN.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NELM-_incategory-Examples)


