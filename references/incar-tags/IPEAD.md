<!-- Source: https://vasp.at/wiki/index.php/IPEAD | revid: 19210 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IPEAD


IPEAD = 1 \| 2 \| 3 \| 4  
Default: **IPEAD** = 4 

Description: IPEAD specifies
the order of the finite difference stencil used to compute the
derivative of the cell-periodic part of the orbitals w.r.t. **k**,
\|∇<sub>**k**</sub>u<sub>n**k**</sub>⟩
([LPEAD](LPEAD.md)=.TRUE.), and the derivative of the
polarization w.r.t. the orbitals, δ**P**/δ⟨ψ<sub>n**k**</sub>\| for
([LCALCEPS](LCALCEPS.md)=.TRUE., or
[EFIELD_PEAD](EFIELD_PEAD.md)≠**0**).

------------------------------------------------------------------------

A central finite differences formula or order
IPEAD is used to compute the
first-order derivative of the cell-periodic part of the orbitals w.r.t.
**k**. The coefficients for the different orders can be found <a
href="https://en.wikipedia.org/wiki/Finite_difference_coefficient#Central_finite_difference"
class="external text" rel="nofollow">here</a>.

## Related tags and articles\[<a href="/wiki/index.php?title=IPEAD&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LPEAD](LPEAD.md), [LCALCEPS](LCALCEPS.md),
[EFIELD_PEAD](EFIELD_PEAD.md), [Berry phases and finite
electric
fields](../theory/Berry_phases_and_finite_electric_fields.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-IPEAD-_incategory-Examples)

------------------------------------------------------------------------


