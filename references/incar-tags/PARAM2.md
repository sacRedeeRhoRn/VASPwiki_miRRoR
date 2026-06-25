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
  optB86b<sup>[\[1\]](#cite_note-klimes:prb:2011-1)</sup>
  ($\kappa$ is not shown in this work since implicitly
  set to 1.0),
  B86R<sup>[\[2\]](#cite_note-hamada:prb:2014-2)</sup>,
  and
  DF3-opt2<sup>[\[3\]](#cite_note-chakraborty:jctc:2020-3)</sup>
  exchange functionals, which have the same analytical form and
  correspond to [GGA](GGA.md)=MK.
  PARAM2 should in principle
  be set to 1.0 for the nonlocal optB86b-vdW
  functional<sup>[\[1\]](#cite_note-klimes:prb:2011-1)</sup>,
  to 0.711357 for the nonlocal
  rev-vdW-DF2<sup>[\[2\]](#cite_note-hamada:prb:2014-2)</sup>
  functional, or to $0.58$ for
  the vdW-DF3-opt2 nonlocal
  functional<sup>[\[3\]](#cite_note-chakraborty:jctc:2020-3)</sup>.
- $\mu$ in the
  optB88<sup>[\[4\]](#cite_note-klimes:jpcm:2010-4)</sup>
  and
  DF3-opt1<sup>[\[3\]](#cite_note-chakraborty:jctc:2020-3)</sup>
  exchange functionals, which have the same analytical form and
  correspond to [GGA](GGA.md)=BO.
  PARAM2 should in principle
  be set to 0.22 for the nonlocal optB88-vdW
  functional<sup>[\[4\]](#cite_note-klimes:jpcm:2010-4)</sup>
  or to $10/81\approx0.1234568$ for the
  vdW-DF3-opt1<sup>[\[3\]](#cite_note-chakraborty:jctc:2020-3)</sup>
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


1.  ↑
    <sup>[a](#cite_ref-klimes:prb:2011_1-0)</sup>
    <sup>[b](#cite_ref-klimes:prb:2011_1-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.83.195131"
    class="external text" rel="nofollow">J. Klimeš, D. R. Bowler, and A.
    Michaelides, Phys. Rev. B <strong>83</strong>, 195131 (2011).</a>
2.  ↑
    <sup>[a](#cite_ref-hamada:prb:2014_2-0)</sup>
    <sup>[b](#cite_ref-hamada:prb:2014_2-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.89.121103"
    class="external text" rel="nofollow">I. Hamada, Phys. Rev. B
    <strong>89</strong>, 121103(R) (2014).</a>
3.  ↑
    <sup>[a](#cite_ref-chakraborty:jctc:2020_3-0)</sup>
    <sup>[b](#cite_ref-chakraborty:jctc:2020_3-1)</sup>
    <sup>[c](#cite_ref-chakraborty:jctc:2020_3-2)</sup>
    <sup>[d](#cite_ref-chakraborty:jctc:2020_3-3)</sup>
    <a href="https://doi.org/10.1021/acs.jctc.0c00471" class="external text"
    rel="nofollow">D. Chakraborty, K. Berland, and T. Thonhauser,
    <em>Next-Generation Nonlocal van der Waals Density Functional</em>, J.
    Chem. Theory Comput. <strong>16</strong>, 5893 (2020).</a>
4.  ↑
    <sup>[a](#cite_ref-klimes:jpcm:2010_4-0)</sup>
    <sup>[b](#cite_ref-klimes:jpcm:2010_4-1)</sup>
    <a href="https://doi.org/10.1088/0953-8984/22/2/022201"
    class="external text" rel="nofollow">J. Klimeš, D. R. Bowler, and A.
    Michaelides, J. Phys.: Condens. Matter <strong>22</strong>, 022201
    (2010).</a>


