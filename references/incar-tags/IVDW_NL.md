<!-- Source: https://vasp.at/wiki/index.php/IVDW_NL | revid: 19710 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IVDW_NL
IVDW_NL = \[integer\] 

|                      |     |                                          |
|----------------------|-----|------------------------------------------|
| Default: **IVDW_NL** | = 1 | for a [GGA](GGA.md)             |
|                      | = 2 | for a [METAGGA](METAGGA.md) |

Description: IVDW_NL allows to select the kernel of the nonlocal van der
Waals part of a functional (available as of VASP.6.4.0).

------------------------------------------------------------------------

IVDW_NL=1 corresponds to the kernel of Dion *et
al.*^([\[1\]](#cite_note-dion:prl:2004-1)) and IVDW_NL=2 to the kernel
rVV10^([\[2\]](#cite_note-sabatini:prb:2013-2)). Note that the kernel of
Dion *et al.* contains one adjustable parameter
([ZAB_VDW](../redirects/ZAB_VDW.md)), while the rVV10 kernel contains
two such parameters ([BPARAM](BPARAM.md) and
[CPARAM](CPARAM.md)).

## Related tags and articles
[GGA](GGA.md), [METAGGA](METAGGA.md),
[LUSE_VDW](LUSE_VDW.md),
[ZAB_VDW](../redirects/ZAB_VDW.md), [BPARAM](BPARAM.md),
[CPARAM](CPARAM.md), [Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-IVDW_NL-_incategory-Examples)

------------------------------------------------------------------------

1.  [↑](#cite_ref-dion:prl:2004_1-0) [M. Dion, H. Rydberg, E.
    Schröder, D. C. Langreth, and B. I. Lundqvist, Phys. Rev. Lett.
    **92**, 246401
    (2004).](https://doi.org/10.1103/PhysRevLett.92.246401)
2.  [↑](#cite_ref-sabatini:prb:2013_2-0) [R. Sabatini, T. Gorni, and S.
    de Gironcoli, Phys. Rev. B **87**, 041108(R)
    (2013).](http://doi.org/10.1103/PhysRevB.87.041108)
