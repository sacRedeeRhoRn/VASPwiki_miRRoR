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
rVV10,[^sabatini:prb:2013-1]
SCAN+rVV10,[^peng:prx:2016-2]
PBE+rVV10L,[^peng:prb:2017-3]
and r$^2$SCAN+rVV10
[^ning:prb:2022-4]
functionals, respectively.

## Related tags and articles\[<a href="/wiki/index.php?title=BPARAM&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[CPARAM](CPARAM.md), [Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)

## References\[<a href="/wiki/index.php?title=BPARAM&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^sabatini:prb:2013-1]: [R. Sabatini, T. Gorni, and S. de Gironcoli, Phys. Rev. B **87**, 041108(R) (2013).](http://doi.org/10.1103/PhysRevB.87.041108)
[^peng:prx:2016-2]: [H. Peng, Z.-H. Yang, J. P. Perdew, and J. Sun, Phys. Rev. X **6**, 041005 (2016).](https://doi.org/10.1103/PhysRevX.6.041005)
[^peng:prb:2017-3]: [H. Peng and J. P. Perdew, *Rehabilitation of the Perdew-Burke-Ernzerhof generalized gradient approximation for layered materials*, Phys. Rev. B **95**, 081105(R) (2017).](https://doi.org/10.1103/PhysRevB.95.081105)
[^ning:prb:2022-4]: [J. Ning, M. Kothakonda, J. W. Furness, A. D. Kaplan, S. Ehlert, J. G. Brandenburg, J. P. Perdew, and J. Sun, *Workhorse minimally empirical dispersion-corrected density functional with tests for weakly bound systems: r²SCAN+rVV⁢10*, Phys. Rev. B **106**, 075422 (2022).](https://doi.org/10.1103/PhysRevB.106.075422)
