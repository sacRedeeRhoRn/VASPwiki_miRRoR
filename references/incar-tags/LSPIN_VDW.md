<!-- Source: https://vasp.at/wiki/index.php/LSPIN_VDW | revid: 24543 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSPIN_VDW
LSPIN_VDW = \[logical\]  
Default: **LSPIN_VDW** = .FALSE. 

Description: LSPIN_VDW=.TRUE. switches on the use of the spin-polarized
formulation^([\[1\]](#cite_note-thonhauser:prl:2015-1)) for the nonlocal
part of a van der Waals functional (available as of VASP.6.4.0).

------------------------------------------------------------------------

|  |
|----|
| **Mind:** LSPIN_VDW=.TRUE. is possible only for van der Waals functionals that consist of a [GGA](GGA.md) for the semilocal part and the kernel type of Dion *et al.*^([\[2\]](#cite_note-dion:prl:2004-2)) ([IVDW_NL](IVDW_NL.md)=1) for the nonlocal part. |

## Related tags and articles
[LUSE_VDW](LUSE_VDW.md),
[IVDW_NL](IVDW_NL.md), [Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)

## References
1.  [↑](#cite_ref-thonhauser:prl:2015_1-0) [T. Thonhauser, S.
    Zuluaga, C. A. Arter, K. Berland, E. Schröder, and P. Hyldgaard,
    Phys. Rev. Lett. **115**, 136402
    (2015).](http://doi.org/10.1103/PhysRevLett.115.136402)
2.  [↑](#cite_ref-dion:prl:2004_2-0) [M. Dion, H. Rydberg, E.
    Schröder, D. C. Langreth, and B. I. Lundqvist, Phys. Rev. Lett.
    **92**, 246401
    (2004).](https://doi.org/10.1103/PhysRevLett.92.246401)
