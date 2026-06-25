<!-- Source: https://vasp.at/wiki/index.php/BPARAM | revid: 35886 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# BPARAM


BPARAM = \[real\]  
Default: **BPARAM** = 6.3 

Description: The tag BPARAM
specifies the value of the parameter $b$ in the
kernel of the nonlocal rVV10 correlation functional.

------------------------------------------------------------------------

BPARAM should be set to 6.3,
15.7, 10, or 11.95 for the
rVV10,<sup>[\[1\]](#cite_note-sabatini:prb:2013-1)</sup>
SCAN+rVV10,<sup>[\[2\]](#cite_note-peng:prx:2016-2)</sup>
PBE+rVV10L,<sup>[\[3\]](#cite_note-peng:prb:2017-3)</sup>
and r$^2$SCAN+rVV10
<sup>[\[4\]](#cite_note-ning:prb:2022-4)</sup>
functionals, respectively.

## Related tags and articles\[<a href="/wiki/index.php?title=BPARAM&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[CPARAM](CPARAM.md), [Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)

## References\[<a href="/wiki/index.php?title=BPARAM&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-sabatini:prb:2013_1-0)
    <a href="http://doi.org/10.1103/PhysRevB.87.041108"
    class="external text" rel="nofollow">R. Sabatini, T. Gorni, and S. de
    Gironcoli, Phys. Rev. B <strong>87</strong>, 041108(R) (2013).</a>
2.  [↑](#cite_ref-peng:prx:2016_2-0)
    <a href="https://doi.org/10.1103/PhysRevX.6.041005"
    class="external text" rel="nofollow">H. Peng, Z.-H. Yang, J. P. Perdew,
    and J. Sun, Phys. Rev. X <strong>6</strong>, 041005 (2016).</a>
3.  [↑](#cite_ref-peng:prb:2017_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.95.081105"
    class="external text" rel="nofollow">H. Peng and J. P. Perdew,
    <em>Rehabilitation of the Perdew-Burke-Ernzerhof generalized gradient
    approximation for layered materials</em>, Phys. Rev. B
    <strong>95</strong>, 081105(R) (2017).</a>
4.  [↑](#cite_ref-ning:prb:2022_4-0)
    <a href="https://doi.org/10.1103/PhysRevB.106.075422"
    class="external text" rel="nofollow">J. Ning, M. Kothakonda, J. W.
    Furness, A. D. Kaplan, S. Ehlert, J. G. Brandenburg, J. P. Perdew, and
    J. Sun, <em>Workhorse minimally empirical dispersion-corrected density
    functional with tests for weakly bound systems: r²SCAN+rVV⁢10</em>, Phys.
    Rev. B <strong>106</strong>, 075422 (2022).</a>


