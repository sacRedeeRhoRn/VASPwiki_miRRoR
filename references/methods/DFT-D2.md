<!-- Source: https://vasp.at/wiki/index.php/DFT-D2 | revid: 33265 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# DFT-D2
In the DFT-D2 method of Grimme^([\[1\]](#cite_note-grimme:jcc:06-1)) the
correction term takes the form:

$E_{\mathrm{disp}} = -\frac{1}{2}
\sum_{i=1}^{N_{at}} \sum_{j=1}^{N_{at}} \sum_{\mathbf{L}}
{}^{\prime} \frac{C_{6ij}}{r_{ij,L}^{6}}
f_{d,6}({r}_{ij,\mathbf{L}})$

where the first two summations are over all $N_{at}$ atoms in the unit cell and the third summation is
over all translations of the unit cell ${\mathbf{L}}=(l_1,l_2,l_3)$ where the prime indicates that
$i\not=j$ for ${\mathbf{L}}=0$. $C_{6ij}$
denotes the dispersion coefficient for the atom pair
$ij$, ${r}_{ij,\mathbf{L}}$ is the distance between atom
$i$ located in the reference cell
$\mathbf{L}=0$ and atom
$j$ in the cell $L$ and the term $f(r_{ij})$ is
a damping function whose role is to scale the force field such as to
minimize the contributions from interactions within typical bonding
distances. In practice, the terms in the equation for
$E_{\mathrm{disp}}$ corresponding to
interactions over distances longer than a certain suitably chosen cutoff
radius ([VDW_RADIUS](../incar-tags/VDW_RADIUS.md), see below)
contribute only negligibly to $E_{\mathrm{disp}}$ and can be ignored. Parameters $C_{6ij}$ and $R_{0ij}$ are
computed using the following combination rules:

$C_{6ij} = \sqrt{C_{6ii} C_{6jj}}$

and

$R_{0ij} = R_{0i}+ R_{0j}.$

The values for $C_{6ii}$ and
$R_{0i}$ are tabulated for each element
and are insensitive to the particular chemical situation (for instance,
$C_6$ for carbon in methane takes
exactly the same value as that for C in benzene within this
approximation). In the DFT-D2 method, a Fermi-type damping function is
used:

$f_{d,6}(r_{ij}) =
\frac{s_6}{1+e^{-d(r_{ij}/(s_R\\R_{0ij})-1)}}$

whereby the global scaling parameter $s_6$ has been optimized for several different DFT functionals such
as PBE ($s_6=0.75$), BLYP
($s_6=1.2$) or B3LYP
($s_6=1.05$). The parameter
$s_R$ is usually fixed at 1.00.

The performance of PBE-D2 method in optimization of various crystalline
systems has been tested systematically in reference
^([\[2\]](#cite_note-bucko:jpca:10-2)).

|  |
|----|
| **Important:** It is recommended to use the more advanced and more accurate method [DFT-D3](DFT-D3.md).^([\[3\]](#cite_note-grimme:jcp:10-3)) |

## Usage
The DFT-D2 method is activated by setting [IVDW](../incar-tags/IVDW.md)=1 or
10 (or the obsolete [LVDW](../redirects/LVDW.md)=*.TRUE.*). Optionally, the
damping function and the vdW parameters can be controlled using the
following flags (the given values are the default ones):

- [VDW_RADIUS](../incar-tags/VDW_RADIUS.md)=50.0 : cutoff radius (in
  Å) for pair interactions
- [VDW_S6](../incar-tags/VDW_S6.md)=0.75 : global scaling factor
  $s_6$ (available in VASP.5.3.4 and
  later)
- [VDW_SR](../incar-tags/VDW_SR.md)=1.00 : scaling factor
  $s_R$ (available in VASP.5.3.4 and
  later)
- [VDW_SCALING](../redirects/VDW_SCALING.md)=0.75 : the same as
  [VDW_S6](../incar-tags/VDW_S6.md) (obsolete as of VASP.5.3.4)
- [VDW_D](../incar-tags/VDW_D.md)=20.0 : damping parameter
  $d$
- [VDW_C6](../incar-tags/VDW_C6.md)=\[real array\] :
  $C_6$ parameters
  ($\mathrm{Jnm}^{6}\mathrm{mol}^{-1}$)
  for each species defined in the [POSCAR](../input-files/POSCAR.md) file
- [VDW_R0](../incar-tags/VDW_R0.md)=\[real array\] :
  $R_0$ parameters (Å) for each species
  defined in the [POSCAR](../input-files/POSCAR.md) file
- [LVDW_EWALD](../incar-tags/LVDW_EWALD.md)=*.FALSE.* : the lattice
  summation in $E_{\mathrm{disp}}$
  expression is computed by means of Ewald's summation (*.TRUE.* ) or
  via a real space summation over all atomic pairs within cutoff radius
  [VDW_RADIUS](../incar-tags/VDW_RADIUS.md) (*.FALSE.*). (available in
  VASP.5.3.4 and later)

  

[TABLE]

## Related tags and articles
[VDW_RADIUS](../incar-tags/VDW_RADIUS.md),
[VDW_S6](../incar-tags/VDW_S6.md), [VDW_SR](../incar-tags/VDW_SR.md),
[VDW_SCALING](../redirects/VDW_SCALING.md),
[VDW_D](../incar-tags/VDW_D.md), [VDW_C6](../incar-tags/VDW_C6.md),
[VDW_R0](../incar-tags/VDW_R0.md),
[LVDW_EWALD](../incar-tags/LVDW_EWALD.md), [IVDW](../incar-tags/IVDW.md),
[DFT-ulg](DFT-ulg.md), [DFT-D3](DFT-D3.md),
[DFT-D4](DFT-D4.md)

## References
1.  [↑](#cite_ref-grimme:jcc:06_1-0) [S. Grimme, J. Comput. Chem.
    **27**, 1787 (2006).](https://doi.org/10.1002/jcc.20495)
2.  [↑](#cite_ref-bucko:jpca:10_2-0) [T. Bučko, J. Hafner, S. Lebègue,
    and J. G. Ángyán, J. Phys. Chem. A **114**, 11814
    (2010).](https://doi.org/10.1021/jp106469x)
3.  [↑](#cite_ref-grimme:jcp:10_3-0) [S. Grimme, J. Antony, S. Ehrlich,
    and S. Krieg, J. Chem. Phys. **132**, 154104
    (2010).](https://doi.org/10.1063/1.3382344)
4.  [↑](#cite_ref-kerber:jcc:08_4-0) [T. Kerber, M. Sierka, and J.
    Sauer, J. Comput. Chem. **29**, 2088
    (2008).](https://doi.org/10.1002/jcc.21069)

------------------------------------------------------------------------
