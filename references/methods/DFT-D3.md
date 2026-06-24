<!-- Source: https://vasp.at/wiki/index.php/DFT-D3 | revid: 34379 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DFT-D3
In the DFT-D3 method of Grimme et
al.^([\[1\]](#cite_note-grimme:jcp:10-1)), the following expression for
the vdW dispersion energy-correction term is used:

$E_{\mathrm{disp}} = -\frac{1}{2}
\sum_{i=1}^{N_{at}} \sum_{j=1}^{N_{at}} \sum_{\mathbf{L}}{}^\prime
\left ( f_{d,6}(r_{ij,L})\\\frac{C_{6ij}}{r_{ij,{L}}^6}
+f_{d,8}(r_{ij,L})\\\frac{C_{8ij}}{r_{ij,L}^8} \right ).$

Unlike in the older [DFT-D2](DFT-D2.md) method, the
dispersion coefficients $C_{6ij}$ are
geometry-dependent as they are calculated on the basis of the local
geometry (coordination number) around atoms $i$ and $j$. Two variants of
DFT-D3, that differ in the mathematical form of the damping functions
$f_{d,n}$, are available. More variants
of the damping function are available via the
[simple-DFT-D3](Simple-DFT-D3.md) external package
([IVDW](../incar-tags/IVDW.md)=15).

## Contents

- [1 DFT-D3(zero)](#DFT-D3(zero))
- [2 DFT-D3(BJ)](#DFT-D3(BJ))
- [3 Related tags and articles](#Related_tags_and_articles)
- [4 References](#References)

### DFT-D3(zero)
In the zero-damping variant of
DFT-D3,^([\[1\]](#cite_note-grimme:jcp:10-1)) invoked by setting
[IVDW](../incar-tags/IVDW.md)=11, the damping function reads

$f_{d,n}(r_{ij}) =
\frac{s_n}{1+6(r_{ij}/(s_{R,n}R_{0ij}))^{-\alpha_{n}}}$

where $R_{0ij} = \sqrt{\frac{C_{8ij}}{C_{6ij}}}$, $\alpha_6=14$ and
$\alpha_8=16$ are fixed (there is no tag
to change their values), and the others parameters, whose default values
depend on the choice of the exchange-correlation functional, can be
modified as follows:

- [VDW_S6](../incar-tags/VDW_S6.md)=\[real\] : scaling
  $s_6$ of the dipole-dipole dispersion.
  **Available since VASP.6.6.0**.
- [VDW_S8](../incar-tags/VDW_S8.md)=\[real\] : scaling
  $s_8$ of the dipole-quadrupole
  dispersion
- [VDW_SR](../incar-tags/VDW_SR.md)=\[real\] : radii scaling
  $s_{r,6}$ in the dipole-dipole
  damping function
- [VDW_SR8](../incar-tags/VDW_SR8.md)=\[real\] : radii scaling
  $s_{r,8}$ in the dipole-quadrupole
  damping function. **Available since VASP.6.6.0**.
- [VDW_RADIUS](../incar-tags/VDW_RADIUS.md)=\[real\] : two-body
  interaction cutoff (in Å)
- [VDW_CNRADIUS](../incar-tags/VDW_CNRADIUS.md)=\[real\] :
  coordination number cutoff (in Å)

### DFT-D3(BJ)
In the rational Becke-Johnson (BJ) damping variant of
DFT-D3,^([\[2\]](#cite_note-grimme:jcc:11-2)), invoked by setting
[IVDW](../incar-tags/IVDW.md)=12, the damping function is given by

$f_{d,n}(r_{ij}) =
\frac{s_n\\r_{ij}^n}{r_{ij}^n + (a_1\\R_{0ij}+a_2)^n}$

where $s_6$, $s_8$, $a_1$, and
$a_2$ are parameters whose default
values depend on the choice of the exchange-correlation functional, but
can also be modified as follows:

- [VDW_S6](../incar-tags/VDW_S6.md)=\[real\] : scaling
  $s_6$ of the dipole-dipole dispersion.
  **Available since VASP.6.6.0**.
- [VDW_S8](../incar-tags/VDW_S8.md)=\[real\] : scaling
  $s_8$ of the dipole-quadrupole
  dispersion
- [VDW_A1](../incar-tags/VDW_A1.md)=\[real\] : scaling
  $a_{1}$ of the critical radii
- [VDW_A2](../incar-tags/VDW_A2.md)=\[real\] : offset
  $a_{2}$ of the critical radii
- [VDW_RADIUS](../incar-tags/VDW_RADIUS.md)=\[real\] : two-body
  interaction cutoff (in Å)
- [VDW_CNRADIUS](../incar-tags/VDW_CNRADIUS.md)=\[real\] :
  coordination number cutoff (in Å)

  

[TABLE]

## Related tags and articles
[IVDW](../incar-tags/IVDW.md), [VDW_S6](../incar-tags/VDW_S6.md),
[VDW_S8](../incar-tags/VDW_S8.md), [VDW_SR](../incar-tags/VDW_SR.md),
[VDW_SR8](../incar-tags/VDW_SR8.md), [VDW_A1](../incar-tags/VDW_A1.md),
[VDW_A2](../incar-tags/VDW_A2.md),
[VDW_RADIUS](../incar-tags/VDW_RADIUS.md),
[VDW_CNRADIUS](../incar-tags/VDW_CNRADIUS.md),
[DFT-D2](DFT-D2.md),
[simple-DFT-D3](Simple-DFT-D3.md),
[DFT-D4](DFT-D4.md), [DFT-ulg](DFT-ulg.md)

## References
1.  ↑ ^([a](#cite_ref-grimme:jcp:10_1-0))
    ^([b](#cite_ref-grimme:jcp:10_1-1))
    ^([c](#cite_ref-grimme:jcp:10_1-2))
    ^([d](#cite_ref-grimme:jcp:10_1-3)) [S. Grimme, J. Antony, S.
    Ehrlich, and S. Krieg, J. Chem. Phys. **132**, 154104
    (2010).](https://doi.org/10.1063/1.3382344)
2.  ↑ ^([a](#cite_ref-grimme:jcc:11_2-0))
    ^([b](#cite_ref-grimme:jcc:11_2-1)) [S. Grimme, S. Ehrlich, and L.
    Goerigk, J. Comput. Chem. **32**, 1456
    (2011).](https://doi.org/10.1002/jcc.21759)

------------------------------------------------------------------------
