<!-- Source: https://vasp.at/wiki/index.php/BPARAM | revid: 35886 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# BPARAM
BPARAM = \[real\]  
Default: **BPARAM** = 6.3 

Description: The tag BPARAM specifies the value of the parameter
$b$ in the kernel of the nonlocal rVV10
correlation functional.

------------------------------------------------------------------------

BPARAM should be set to 6.3, 15.7, 10, or 11.95 for the
rVV10,^([\[1\]](#cite_note-sabatini:prb:2013-1))
SCAN+rVV10,^([\[2\]](#cite_note-peng:prx:2016-2))
PBE+rVV10L,^([\[3\]](#cite_note-peng:prb:2017-3)) and
r$^2$SCAN+rVV10
^([\[4\]](#cite_note-ning:prb:2022-4)) functionals, respectively.

## Related tags and articles
[CPARAM](CPARAM.md), [Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)

## References
1.  [↑](#cite_ref-sabatini:prb:2013_1-0) [R. Sabatini, T. Gorni, and S.
    de Gironcoli, Phys. Rev. B **87**, 041108(R)
    (2013).](http://doi.org/10.1103/PhysRevB.87.041108)
2.  [↑](#cite_ref-peng:prx:2016_2-0) [H. Peng, Z.-H. Yang, J. P. Perdew,
    and J. Sun, Phys. Rev. X **6**, 041005
    (2016).](https://doi.org/10.1103/PhysRevX.6.041005)
3.  [↑](#cite_ref-peng:prb:2017_3-0) [H. Peng and J. P. Perdew,
    *Rehabilitation of the Perdew-Burke-Ernzerhof generalized gradient
    approximation for layered materials*, Phys. Rev. B **95**, 081105(R)
    (2017).](https://doi.org/10.1103/PhysRevB.95.081105)
4.  [↑](#cite_ref-ning:prb:2022_4-0) [J. Ning, M. Kothakonda, J. W.
    Furness, A. D. Kaplan, S. Ehlert, J. G. Brandenburg, J. P. Perdew,
    and J. Sun, *Workhorse minimally empirical dispersion-corrected
    density functional with tests for weakly bound systems:
    r²SCAN+rVV⁢10*, Phys. Rev. B **106**, 075422
    (2022).](https://doi.org/10.1103/PhysRevB.106.075422)
