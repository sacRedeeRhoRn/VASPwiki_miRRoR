<!-- Source: https://vasp.at/wiki/index.php/LSPIN_VDW | revid: 24543 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSPIN_VDW


LSPIN_VDW = \[logical\]  
Default: **LSPIN_VDW** = .FALSE. 

Description: LSPIN_VDW=.TRUE.
switches on the use of the spin-polarized
formulation<sup>[\[1\]](#cite_note-thonhauser:prl:2015-1)</sup>
for the nonlocal part of a van der Waals functional (available as of
VASP.6.4.0).

------------------------------------------------------------------------

|  |
|----|
| **Mind:** LSPIN_VDW=.TRUE. is possible only for van der Waals functionals that consist of a [GGA](GGA.md) for the semilocal part and the kernel type of Dion *et al.*<sup>[\[2\]](#cite_note-dion:prl:2004-2)</sup> ([IVDW_NL](IVDW_NL.md)=1) for the nonlocal part. |

## Related tags and articles\[<a
href="/wiki/index.php?title=LSPIN_VDW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LUSE_VDW](LUSE_VDW.md),
[IVDW_NL](IVDW_NL.md), [Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)

## References\[<a
href="/wiki/index.php?title=LSPIN_VDW&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-thonhauser:prl:2015_1-0)
    <a href="http://doi.org/10.1103/PhysRevLett.115.136402"
    class="external text" rel="nofollow">T. Thonhauser, S. Zuluaga, C. A.
    Arter, K. Berland, E. Schröder, and P. Hyldgaard, Phys. Rev. Lett.
    <strong>115</strong>, 136402 (2015).</a>
2.  [↑](#cite_ref-dion:prl:2004_2-0)
    <a href="https://doi.org/10.1103/PhysRevLett.92.246401"
    class="external text" rel="nofollow">M. Dion, H. Rydberg, E. Schröder,
    D. C. Langreth, and B. I. Lundqvist, Phys. Rev. Lett.
    <strong>92</strong>, 246401 (2004).</a>


