<!-- Source: https://vasp.at/wiki/index.php/DFT-ulg | revid: 33613 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DFT-ulg


In the DFT-ulg method of Kim et
al.<sup>[\[1\]](#cite_note-kim:jpcl:2012-1)</sup>,
the correction term takes the form:

$E_{\mathrm{disp}} = -\frac{1}{2} s_{lg}\sum_{i=1}^{N_{at}}
\sum_{j=1}^{N_{at}} \sum_{\mathbf{L}} {}^{\prime}
\frac{C_{6ij}}{r_{ij,L}^{6}+b_{lg}(R_{0}^{ij})^{6}}$

where the first two summations are over all $N_{at}$
atoms in the unit cell and the third summation is over all translations
of the unit cell ${\mathbf{L}}=(l_1,l_2,l_3)$ where the prime indicates that
$i\not=j$ for ${\mathbf{L}}=0$. $C_{6ij}$
denotes the dispersion coefficient for the atom pair
$ij$, ${r}_{ij,\mathbf{L}}$ is the distance between atom
$i$ located in the reference cell
$\mathbf{L}=0$ and atom $j$ in the
cell $L$.

## Usage\[<a href="/wiki/index.php?title=DFT-ulg&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Usage">edit</a> \| (./index.php.md)\]

The DFT-ulg method can be activated by setting
[IVDW](../incar-tags/IVDW.md)=3. The parameters in the DFT-ulg method (see
Ref.
<sup>[\[1\]](#cite_note-kim:jpcl:2012-1)</sup>
for details) that can be modified are listed below.

- [VDW_RADIUS](../incar-tags/VDW_RADIUS.md)=50.0 : cutoff radius (in
  $\AA$) for pair interactions
- [VDW_S6](../incar-tags/VDW_S6.md)=0.7012 : global scaling parameter
  $s_{lg}$
- [VDW_D](../incar-tags/VDW_D.md)=0.6966 : universal correction parameter
  $b_{lg}$
- [VDW_C6](../incar-tags/VDW_C6.md)=\[real array\] :
  $C_6$ parameters ($\mathrm{Jnm}^{6}\mathrm{mol}^{-1}$) for each species
  defined in the [POSCAR](../input-files/POSCAR.md) file
- [VDW_R0](../incar-tags/VDW_R0.md)=\[real array\] :
  $R_0$ parameters ($\AA$) for
  each species defined in the [POSCAR](../input-files/POSCAR.md) file
- [LVDW_EWALD](../incar-tags/LVDW_EWALD.md)=*.FALSE.* : the lattice
  summation in $E_{\mathrm{disp}}$ expression is computed by means of Ewald's summation
  (*.TRUE.* ) or via a real space summation over all atomic pairs within
  cutoff radius [VDW_RADIUS](../incar-tags/VDW_RADIUS.md) (*.FALSE.*).
  (available in VASP.5.3.5 and later)

|  |
|----|
| **Mind:** The default value of the parameter $s_{lg}$ (0.7012) was determined in conjunction with the PBE [GGA](../incar-tags/GGA.md) functional<sup>[\[1\]](#cite_note-kim:jpcl:2012-1)</sup>. Therefore, it is not recommended to use the DFT-ulg dispersion correction with a [GGA](../incar-tags/GGA.md) functional other than PBE, unless $s_{lg}$ is reoptimized. |

## Related tags and articles\[<a href="/wiki/index.php?title=DFT-ulg&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[VDW_RADIUS](../incar-tags/VDW_RADIUS.md),
[VDW_S6](../incar-tags/VDW_S6.md), [VDW_D](../incar-tags/VDW_D.md),
[VDW_C6](../incar-tags/VDW_C6.md), [VDW_R0](../incar-tags/VDW_R0.md),
[LVDW_EWALD](../incar-tags/LVDW_EWALD.md), [IVDW](../incar-tags/IVDW.md),
[DFT-D2](DFT-D2.md)

## References\[<a href="/wiki/index.php?title=DFT-ulg&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-kim:jpcl:2012_1-0)</sup>
    <sup>[b](#cite_ref-kim:jpcl:2012_1-1)</sup>
    <sup>[c](#cite_ref-kim:jpcl:2012_1-2)</sup>
    <a href="https://doi.org/10.1021/jz2016395" class="external text"
    rel="nofollow">H. Kim, J.-M. Choi, and W. A. Goddard, III, J. Phys.
    Chem. Lett. <strong>3</strong>, 360 (2012).</a>


------------------------------------------------------------------------


