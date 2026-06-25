<!-- Source: https://vasp.at/wiki/index.php/SHAKEMAXITER | revid: 36165 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SHAKEMAXITER


SHAKEMAXITER = \[Integer\]  
Default: **SHAKEMAXITER** = 1000 

Description: SHAKEMAXITER
specifies the maximum number of iterations in the SHAKE algorithm (in
case VASP was compiled with
[-Dtbdyn](../misc/Precompiler_options.md)).

------------------------------------------------------------------------

Constrained molecular dynamics ([MDALGO](MDALGO.md)=1 \| 2)
are performed using a [SHAKE
algorithm](MDALGO.md).[^Ryckaert77-1]

If the error for all geometric constraints does not decrease below a
predefined tolerance ([SHAKETOL](SHAKETOL.md)) within the
allowed number of iterations, VASP terminates with an error message. The
aforementioned maximum number of iterations is set by means of the
SHAKEMAXITER tag.

## Related tags and articles\[<a
href="/wiki/index.php?title=SHAKEMAXITER&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[SHAKETOL](SHAKETOL.md),
[SHAKETOLSOFT](SHAKETOLSOFT.md),
[MDALGO](MDALGO.md)

[Constrained molecular
dynamics](../theory/Constrained_molecular_dynamics.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-SHAKEMAXITER-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=SHAKEMAXITER&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^Ryckaert77-1]: [J. P. Ryckaert, G. Ciccotti, and H. J. C. Berendsen, J. Comp. Phys. 23, 327 (1977).](http://dx.doi.org/10.1016/0021-9991(77)90098-5)
