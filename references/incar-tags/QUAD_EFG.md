<!-- Source: https://vasp.at/wiki/index.php/QUAD_EFG | revid: 30853 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# QUAD_EFG


  
QUAD_EFG = \[real array\]  
Default: **QUAD_EFG** = NTYP\*1.0 

Description: nuclear quadrupole moment (in millbarn) for the atomic
types on the [POTCAR](../input-files/POTCAR.md) file.

------------------------------------------------------------------------

Setting the QUAD_EFG tag
allows the conversion of the *V*<sub>zz</sub> (see
[LEFG](LEFG.md)) values into the quadrupole coupling constants
*C*<sub>q</sub> often encountered in NMR literature. The conversion
formula is as follows (*Q* is the element and isotope specific
quadrupole moment):

$C_q = \frac{e Q V_{zz}}{h}.$

|  |
|----|
| **Tip:** Several definitions of $C_q$ are used in the NMR community. |

The QUAD_EFG tag specifies the
nuclear quadrupole moment in millibarns for each atomic species, in the
same order as in the [POTCAR](../input-files/POTCAR.md) file. The output
*C*<sub>q</sub> is in MHz. An online compilation of nuclear quadrupole
moments can be found online in a database
[^pyykko:web-1]
or in Ref.
[^pyykko:molphys:2008-2]
(updated numbers in Ref.
[^pyykko:molphys:2017-3]).

Suppose a solid contains Al, C, and Si, then the
QUAD_EFG tag could read:

    QUAD_EFG = 146.6 33.27 0.0

<sup>27</sup>Al is the stable isotope of Al with a natural abundance of
100% and *Q*=146.6. The stable isotopes <sup>12</sup>C and
<sup>13</sup>C are not quadrupolar nuclei, however, the radioactive
<sup>11</sup>C is. It has *Q*=33.27. For Si, all stable isotopes have
I≤1/2, making it redundant to calculate a *C*<sub>q</sub>. No moments
are known for the other isotopes.

|  |
|----|
| **Important:** For heavy nuclei inaccuracies are to be expected because of an incomplete treatment of relativistic effects. |

## Related tags and articles\[<a href="/wiki/index.php?title=QUAD_EFG&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LEFG](LEFG.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-QUAD_EFG-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=QUAD_EFG&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^pyykko:web-1]: [Year-2008 Nuclear Quadrupole Moments, https://www.chem.helsinki.fi (2025)](http://www.chem.helsinki.fi/~pyykko/Q2008.pdf)
[^pyykko:molphys:2008-2]: [P. Pyykkö, *Year-2008 nuclear quadrupole moments*, Mol. Phys. **106**, 1965-1974 (2008).](https://doi.org/10.1080/00268970802018367)
[^pyykko:molphys:2017-3]: [P. Pyykkö, *Year-2017 nuclear quadrupole moments*, Mol. Phys. **116**, 1328-1338 (2018).](https://doi.org/10.1080/00268976.2018.1426131)
