<!-- Source: https://vasp.at/wiki/index.php/NSW | revid: 33294 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NSW


NSW = \[integer\]  
Default: **NSW** = 0 

Description: NSW sets the
maximum number of ionic steps.

------------------------------------------------------------------------

[IBRION](IBRION.md) = 0:

NSW gives the number of steps
in all <a href="/wiki/Molecular_dynamics" class="mw-redirect"
title="Molecular dynamics">molecular dynamics</a> runs. It *has* to be
supplied, otherwise VASP exits immediately after having started. We
recommend splitting long MD runs containing ab-initio calculations into
multiple calculations with
NSW⪅20000. For
[ML_MODE](ML_MODE.md)=run larger values of
NSW should be possible, but
consider setting [ML_OUTBLOCK](ML_OUTBLOCK.md).

[IBRION](IBRION.md) != 0:

In all minimization algorithms (quasi-Newton, conjugate gradient, and
damped molecular dynamics) NSW
defines the maximum number of ionic steps.

Within each ionic step at most [NELM](NELM.md) electronic
steps are performed. It is fewer if the convergence criterion set by
[EDIFF](EDIFF.md) is met before. Forces and stresses are
calculated according to the setting of [ISIF](ISIF.md) for
each ionic step.

## Related tags and articles\[<a href="/wiki/index.php?title=NSW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[structure
optimization](../tutorials/Structure_optimization.md),
[NBLOCK](NBLOCK.md), [KBLOCK](KBLOCK.md),
[ML_OUTBLOCK](ML_OUTBLOCK.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NSW-_incategory-Examples)


