<!-- Source: https://vasp.at/wiki/index.php/EINT | revid: 27582 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EINT


EINT = \[real1\] \[real2\] \|
\[real1\]  
Default: **EINT** = not set 

Description: EINT sets the
energy interval for bands contributing to the calculation of the
<a href="/wiki/Band-decomposed_charge_densities" class="mw-redirect"
title="Band-decomposed charge densities">partial charge density</a> in
eV.

------------------------------------------------------------------------

- EINT= \[real1\] \[real2\]:

If two values are given, the energy interval between those values is
used.

- EINT= \[real1\]:

If only one value is given, the Fermi energy $\epsilon_f$
is used as the other limit \[real2\] of the interval.

------------------------------------------------------------------------

|  |
|----|
| **Important:** The energies passed in EINT are used as set if [NBMOD](NBMOD.md) = -2, but will be added to the Fermi energy ($\epsilon_f$ + real1 and $\epsilon_f$ + real2) if [NBMOD](NBMOD.md) = -3. |

If \[real1\] is larger than \[real2\], the two values will be flipped
internally, so a meaningful energy interval is used.

If EINT is set, but
[NBMOD](NBMOD.md) is not, it will be internally set to
[NBMOD](NBMOD.md) = -2, and the input values of
EINT will be treated as
absolute energies.

EINT can be conveniently used
in combination with [NBMOD](NBMOD.md) = -3 to mimic the
bias-voltage for [simulating a scanning-tunneling-microscope
image](../misc/STM_of_graphene.md).

## Related tags and articles\[<a href="/wiki/index.php?title=EINT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LPARD](LPARD.md), [NBMOD](NBMOD.md),
[IBAND](IBAND.md), [KPUSE](KPUSE.md),
[LSEPB](LSEPB.md), [LSEPK](LSEPK.md),
[LPARDH5](LPARDH5.md), [PARCHG](../output-files/PARCHG.md),
[vaspout.h5](../output-files/Vaspout.h5.md),
<a href="/wiki/Band-decomposed_charge_densities" class="mw-redirect"
title="Band-decomposed charge densities">Band-decomposed charge
densities</a>

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-EINT-_incategory-Examples)

------------------------------------------------------------------------


