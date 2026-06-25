<!-- Source: https://vasp.at/wiki/index.php/VDW_BETA | revid: 34380 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VDW_BETA


VDW_BETA = \[real\] 

Description: VDW_BETA sets the
offset for the damping radius or the power for the zero-damping
component in the DFT-D3 methods implemented in the
[simple-DFT-D3](../methods/Simple-DFT-D3.md) package.

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

VDW_BETA allows to set the
value of a parameter in the following versions of DFT-D3 (only available
in the [simple-DFT-D3](../methods/Simple-DFT-D3.md) package):

- Offset $\beta$ for
  the damping radius in the modified zero-damping function
  ([IVDW](IVDW.md)=15 with
  [SDFTD3_DAMPING](SDFTD3_DAMPING.md)=mzero).
- Power $\beta$ for
  the zero-damping component in the optimized-power damping function
  ([IVDW](IVDW.md)=15 with
  [SDFTD3_DAMPING](SDFTD3_DAMPING.md)=optimizedpower).
  Note that $\beta-6$
  corresponds to the values of $\beta$
  reported in
  Ref.<sup>[\[1\]](#cite_note-witte:jctc:2017-1)</sup>.

## Related tags and articles\[<a href="/wiki/index.php?title=VDW_BETA&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IVDW](IVDW.md),
[SDFTD3_DAMPING](SDFTD3_DAMPING.md),
[simple-DFT-D3](../methods/Simple-DFT-D3.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-VDW_BETA-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=VDW_BETA&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-witte:jctc:2017_1-0)
    <a href="http://dx.doi.org/10.1021/acs.jctc.7b00176"
    class="external text" rel="nofollow">J. Witte, N. Mardirossian, J. B.
    Neaton, and M. Head-Gordon, <em>Assessing DFT-D3 Damping Functions
    Across Widely Used Density Functionals: Can We Do Better?</em>, J. Chem.
    Theory Comput. <strong>13</strong>, 2043 (2017).</a>


------------------------------------------------------------------------


