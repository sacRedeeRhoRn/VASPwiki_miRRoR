<!-- Source: https://vasp.at/wiki/index.php/ALPHA_VDW | revid: 24421 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ALPHA_VDW


ALPHA_VDW = \[real\] 

|  |  |  |
|----|----|----|
| Default: **ALPHA_VDW** | = 0.94950 | for [IVDW_NL](IVDW_NL.md)=3 or |
|  | = 0.28248 | for [IVDW_NL](IVDW_NL.md)=4 |

Description: Specify $\alpha$ in
vdW-DF3-opt1/vdW-DF3-opt2.

------------------------------------------------------------------------

The ALPHA_VDW tag allows to
specify the value of the parameter $\alpha$ in
the kernel of the vdW-DF3-opt1/vdW-DF3-opt2 nonlocal van der Waals
functionals.[^chakraborty:jctc:2020-1]

## Related tags and articles\[<a
href="/wiki/index.php?title=ALPHA_VDW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[GAMMA_VDW](GAMMA_VDW.md),
[PARAM1](PARAM1.md), [PARAM2](PARAM2.md),
[Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ALPHA_VDW-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=ALPHA_VDW&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^chakraborty:jctc:2020-1]: [D. Chakraborty, K. Berland, and T. Thonhauser, *Next-Generation Nonlocal van der Waals Density Functional*, J. Chem. Theory Comput. **16**, 5893 (2020).](https://doi.org/10.1021/acs.jctc.0c00471)
