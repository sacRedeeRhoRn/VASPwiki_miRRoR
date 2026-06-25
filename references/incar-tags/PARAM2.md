<!-- Source: https://vasp.at/wiki/index.php/PARAM2 | revid: 24427 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PARAM2


PARAM2 = \[real\]  
Default: **PARAM2** = 1.0 

Description: $\kappa$ for
[GGA](GGA.md)=MK, or $\mu$ for
[GGA](GGA.md)=BO.

------------------------------------------------------------------------

The PARAM2 tag determines the
value corresponding to different parameters depending on the
[GGA](GGA.md) functional that is chosen:

- $\kappa$ in the
  optB86b[^klimes:prb:2011-1]
  ($\kappa$ is not shown in this work since implicitly
  set to 1.0),
  B86R[^hamada:prb:2014-2],
  and
  DF3-opt2[^chakraborty:jctc:2020-3]
  exchange functionals, which have the same analytical form and
  correspond to [GGA](GGA.md)=MK.
  PARAM2 should in principle
  be set to 1.0 for the nonlocal optB86b-vdW
  functional[^klimes:prb:2011-1],
  to 0.711357 for the nonlocal
  rev-vdW-DF2[^hamada:prb:2014-2]
  functional, or to $0.58$ for
  the vdW-DF3-opt2 nonlocal
  functional[^chakraborty:jctc:2020-3].
- $\mu$ in the
  optB88[^klimes:jpcm:2010-4]
  and
  DF3-opt1[^chakraborty:jctc:2020-3]
  exchange functionals, which have the same analytical form and
  correspond to [GGA](GGA.md)=BO.
  PARAM2 should in principle
  be set to 0.22 for the nonlocal optB88-vdW
  functional[^klimes:jpcm:2010-4]
  or to $10/81\approx0.1234568$ for the
  vdW-DF3-opt1[^chakraborty:jctc:2020-3]
  nonlocal functional.

The complete [INCAR](../input-files/INCAR.md) file for the nonlocal van der
Waals functionals mentioned above can be found at [Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md).

## Related tags and articles\[<a href="/wiki/index.php?title=PARAM2&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[PARAM1](PARAM1.md), [GGA](GGA.md), [Nonlocal
vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PARAM2-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=PARAM2&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^klimes:prb:2011-1]: [J. Klimeš, D. R. Bowler, and A. Michaelides, Phys. Rev. B **83**, 195131 (2011).](https://doi.org/10.1103/PhysRevB.83.195131)
[^hamada:prb:2014-2]: [I. Hamada, Phys. Rev. B **89**, 121103(R) (2014).](https://doi.org/10.1103/PhysRevB.89.121103)
[^chakraborty:jctc:2020-3]: [D. Chakraborty, K. Berland, and T. Thonhauser, *Next-Generation Nonlocal van der Waals Density Functional*, J. Chem. Theory Comput. **16**, 5893 (2020).](https://doi.org/10.1021/acs.jctc.0c00471)
[^klimes:jpcm:2010-4]: [J. Klimeš, D. R. Bowler, and A. Michaelides, J. Phys.: Condens. Matter **22**, 022201 (2010).](https://doi.org/10.1088/0953-8984/22/2/022201)
