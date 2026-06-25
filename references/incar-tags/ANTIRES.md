<!-- Source: https://vasp.at/wiki/index.php/ANTIRES | revid: 15891 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ANTIRES


ANTIRES = 0 \| 1 \| 2  
Default: **ANTIRES** = 0 

Description: ANTIRES
determines whether the Tamm-Dancoff approximation is used or not.

------------------------------------------------------------------------

- ANTIRES=0 Tamm-Dancoff
  approximation (TDA)
- ANTIRES=1 yields exact
  results at ω=0 at roughly the same cost as TDA
- ANTIRES=2 beyond
  Tamm-Dancoff, coupling between positive and negative frequencies

VASP uses the procedures outlined in reference
[^Sander-1]
to include contributions beyond TDA. Beyond-TDA calculations increase
the computational time and memory requirements by typically a factor of
2.

## Related tags and articles\[<a href="/wiki/index.php?title=ANTIRES&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a>

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ANTIRES-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=ANTIRES&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^Sander-1]: [T. Sander, E. Maggio and G. Kresse, Phys. Rev. B 92, 045209 (2015).](http://journals.aps.org/prb/abstract/10.1103/PhysRevB.92.045209)
