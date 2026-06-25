<!-- Source: https://vasp.at/wiki/index.php/PARAM1 | revid: 24425 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PARAM1


PARAM1 = \[real\]  
Default: **PARAM1** = 0.1234 

Description: $\mu$ for
[GGA](GGA.md)=MK, $\beta$ for
[GGA](GGA.md)=BO.

------------------------------------------------------------------------

The PARAM1 tag determines the
value corresponding to different parameters depending on the
[GGA](GGA.md) functional that is chosen:

- $\mu$ in the
  optB86b[^klimes:prb:2011-1],
  B86R[^hamada:prb:2014-2],
  and
  DF3-opt2[^chakraborty:jctc:2020-3]
  exchange functionals, which have the same analytical form and
  correspond to [GGA](GGA.md)=MK.
  PARAM1 should in principle
  be set to 0.1234 for the optB86b-vdW nonlocal
  functional[^klimes:prb:2011-1]
  or to $10/81\approx0.1234568$ for the
  rev-vdW-DF2[^hamada:prb:2014-2]
  and
  vdW-DF3-opt2[^chakraborty:jctc:2020-3]
  nonlocal functionals.
- $\beta$ in the
  optB88[^klimes:jpcm:2010-4]
  exchange functional or $\mu/\kappa$
  in the
  DF3-opt1[^chakraborty:jctc:2020-3]
  exchange functional, which have the same analytical form and
  correspond to [GGA](GGA.md)=BO.
  PARAM1 should in principle
  be set to $0.22/1.2\approx0.1833333333$ for the optB88-vdW nonlocal
  functional[^klimes:jpcm:2010-4]
  or to $(10/81)/1.1\approx0.1122334456$ for the
  vdW-DF3-opt1[^chakraborty:jctc:2020-3]
  nonlocal functional.

The complete [INCAR](../input-files/INCAR.md) file for the nonlocal van der
Waals functionals mentioned above can be found at [Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md).

## Related tags and articles\[<a href="/wiki/index.php?title=PARAM1&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[PARAM2](PARAM2.md), [GGA](GGA.md), [Nonlocal
vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PARAM1-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=PARAM1&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^klimes:prb:2011-1]: [J. Klimeš, D. R. Bowler, and A. Michaelides, Phys. Rev. B **83**, 195131 (2011).](https://doi.org/10.1103/PhysRevB.83.195131)
[^hamada:prb:2014-2]: [I. Hamada, Phys. Rev. B **89**, 121103(R) (2014).](https://doi.org/10.1103/PhysRevB.89.121103)
[^chakraborty:jctc:2020-3]: [D. Chakraborty, K. Berland, and T. Thonhauser, *Next-Generation Nonlocal van der Waals Density Functional*, J. Chem. Theory Comput. **16**, 5893 (2020).](https://doi.org/10.1021/acs.jctc.0c00471)
[^klimes:jpcm:2010-4]: [J. Klimeš, D. R. Bowler, and A. Michaelides, J. Phys.: Condens. Matter **22**, 022201 (2010).](https://doi.org/10.1088/0953-8984/22/2/022201)
