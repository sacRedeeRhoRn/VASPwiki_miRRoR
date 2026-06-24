<!-- Source: https://vasp.at/wiki/index.php/LORBIT | revid: 37170 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LORBIT
LORBIT = 0 \| 1 \| 2 \| 5 \| 10 \| 11 \| 12  
Default: **LORBIT** = 0 

Description: Selects a projection method onto local quantum numbers
($lm$) and writes
[PROCAR](../output-files/PROCAR.md)/[PROOUT](../output-files/PROOUT.md) file.

------------------------------------------------------------------------

When LORBIT is set, VASP performs a post-processing step of the
Kohn-Sham (KS) orbitals to decompose the KS orbitals into local quantum
numbers ($lm$) and obtain local
properties, e.g., the on-site charge density or on-site magnetic moments
due to the spin degrees of freedom. The decomposition is achieved by
means of one of several projection methods selected by LORBIT. All these
projections rely on the fact that most of the charge density is close to
the ion center, and interstitial regions separate them well. This is
merely a qualitative approach in contrast to performing a
[wannierization](https://vasp.at/wiki/index.php/Wannier_functions) in order
to obtain a localized basis, but often it serves as a good estimate.

|  |
|----|
| **Tip:** As this is a post-processing step, LORBIT can be added/changed when restarting a converged calculation. To this end, set [ALGO](ALGO.md)=None and the desired LORBIT, and restart from [WAVECAR](../input-files/WAVECAR.md). |

For VASP version \< 6 with LORBIT \>= 11 and [ISYM](ISYM.md) =
2, see [known issues](../misc/Known_issues.md).

## Contents

- [1 Projection methods](#Projection_methods)
  - [1.1 For LORBIT \< 10](#For_LORBIT_%3C_10)
  - [1.2 For LORBIT \>= 10](#For_LORBIT_%3E=_10)
  - [1.3 Phase factors](#Phase_factors)
- [2 On-site partial charge densities and
  magnetization](#On-site_partial_charge_densities_and_magnetization)
- [3 Partial density of states
  (pDOS)](#Partial_density_of_states_(pDOS))
- [4 References](#References)
- [5 Related tags and articles](#Related_tags_and_articles)

## Projection methods
See the table for an overview:

|  |  |  |
|----|----|----|
| LORBIT | [RWIGS](RWIGS.md) tag | files written |
| 0 | required | [DOSCAR](../output-files/DOSCAR.md) and [PROCAR](../output-files/PROCAR.md) |
| 1 | required | [DOSCAR](../output-files/DOSCAR.md) and *lm*-decomposed [PROCAR](../output-files/PROCAR.md) |
| 2 | required | [DOSCAR](../output-files/DOSCAR.md) and *lm*-decomposed [PROCAR](../output-files/PROCAR.md) + phase factors |
| 5 | required | [DOSCAR](../output-files/DOSCAR.md) and [PROOUT](../output-files/PROOUT.md) |
| 10 | ignored | [DOSCAR](../output-files/DOSCAR.md) and [PROCAR](../output-files/PROCAR.md) |
| 11 | ignored | [DOSCAR](../output-files/DOSCAR.md) and *lm*-decomposed [PROCAR](../output-files/PROCAR.md) |
| 12 | ignored | [DOSCAR](../output-files/DOSCAR.md) and *lm*-decomposed [PROCAR](../output-files/PROCAR.md) + phase factors (not recommended) |
| 13 | ignored | [DOSCAR](../output-files/DOSCAR.md) and *lm*-decomposed [PROCAR](../output-files/PROCAR.md) + phase factors, choose best projector for each band (not recommended) |
| 14 | ignored | [DOSCAR](../output-files/DOSCAR.md) and *lm*-decomposed [PROCAR](../output-files/PROCAR.md) + phase factors, choose single projector for interval [EMIN](EMIN.md),[EMAX](EMAX.md) |

### For LORBIT \< 10
The projection is onto spherical harmonics at each ionic site within a
sphere defined by [RWIGS](RWIGS.md). The radius must be
specified for each atomic species, and there is some uncertainty
introduced depending on the size of the sphere.

### For LORBIT \>= 10
The projection uses the projector functions that are provided by the
[PAW method](../redirects/PAW_formalism.md). This is, of course,
still a qualitative approach because also, for the PAW projectors, the
radius was somehow defined, and it is not guaranteed to be the best
choice for that particular system as it depends on the chemical
composition and crystal or molecular structure.

### Phase factors
For LORBIT\>=12: The **phase factors** written by VASP can usually only
be used as a qualitative measure of the projection of the orbitals into
the atomic sphere. The main issue is that most VASP
[POTCAR](../input-files/POTCAR.md) files have two or three projectors per
$l$-quantum number, and projecting an
orbital onto two projectors will yield two complex numbers. VASP
combines these two numbers into a single number. The precise algorithms
differ in different versions of VASP, and we recommend that you inspect
the source code for more details. From vasp.6 onward, an improved scheme
has been implemented and can be selected using LORBIT=14. In this case,
VASP first selects a single projector for each $l$-quantum number by linearly combining all projectors with the
same $l$-quantum number. This is done in
such a way that the new projector is optimally chosen to represent the
calculated orbitals in the energy interval specified by
[EMAX](EMAX.md) and [EMIN](EMIN.md). In the second
step, VASP projects onto these optimized projectors, yielding a single
complex number for each orbital, site and $l$-quantum number, which is written to the
[PROCAR](../output-files/PROCAR.md) file. For details we also refer to
^([\[1\]](#cite_note-Schuler:JPCM:2018-1)). LORBIT=12 should no longer
be used except for qualitative calculations. LORBIT=13 chooses the
projectors also automatically, but allows for different optimal linear
combinations for each orbital. Note that this is generally not
desirable, since the resultant projection is not compatible with the
required properties of a projection operator (a projection operator
needs to use energy and orbital independent projectors). Hence, do not
use LORBIT=13 for anything but a qualitative analysis.

LORBIT=13 and LORBIT=14 are only supported by version \>=5.4.4.

## On-site partial charge densities and magnetization
The partial charge densities can be found in the
[OUTCAR](../output-files/OUTCAR.md)

    total charge     

    # of ion       s       p       d       tot
    ------------------------------------------
        1        1.514   0.000   0.000   1.514
        2        0.123   0.345   0.000   0.468

Here, the first column corresponds to the ion index
$\alpha$, the s, p, d,... columns
correspond to the partial charges for $l=0,1,2,\cdots$ defined as

$\rho_{\alpha l}=\frac{1}{N_{\bf k}}
\sum_{n{\bf k}}f_{n{\bf k}} \sum_{m=-l}^{l}|\langle
Y_{lm}^{\alpha}|\phi_{n\mathbf{k}}\rangle|^2$

The $\langle
Y_{lm}^{\alpha}|\phi_{n\mathbf{k}}\rangle$ are obtained
from the projection of the (occupied) KS orbitals $|\phi_{n{\bf k}}\rangle$ onto spherical harmonics that are
non zero within spheres of a radius [RWIGS](RWIGS.md)
centered at ion $\alpha$ and the last
column is the sum $\sum_{l}\rho_{\alpha l}$.

Note that depending on the system, an "f" column is written as well.

- In case of spin-polarized magnetic calculations
  ([ISPIN](ISPIN.md)=2), the partial magnetization densities
  are written to the [OUTCAR](../output-files/OUTCAR.md)

&nbsp;

    magnetization (x)
     
    # of ion       s       p       d       tot
    ------------------------------------------
        1        0.000   0.000   0.000   0.000
        2        0.000   0.245   0.000   0.245

Here, the magnetization density is calculated from the difference in the
up and down spin channel $m^{\alpha l}_z =
\rho_{\alpha l}^{\uparrow}-\rho_{\alpha l}^{\downarrow}$
Although the direction of the magnetization densities is meaningless in
a spin-polarized calculation (no spin-orbit coupling, see
[LSORBIT](LSORBIT.md)), here the projection axis is the
z-axis. This is consistent withe the behavior upon restarting a
noncollinear calculation from a spin-polarized one with default
[SAXIS](SAXIS.md).

- In case of noncollinear calculations
  ([LNONCOLLINEAR](LNONCOLLINEAR.md)=.TRUE.), the
  lines after "total charge" correspond to the diagonal average

$\frac{\rho_{\alpha l}^{\uparrow\uparrow} -
\rho_{\alpha l}^{\downarrow \downarrow}}{2}$ of the density
tensor

$\rho_{\alpha l} = \left(\begin{matrix}
\rho_{\alpha l}^{\uparrow \uparrow } & \rho_{\alpha l}^{\uparrow
\downarrow} \\ \rho_{\alpha l}^{\downarrow \uparrow} & \rho_{\alpha
l}^{\downarrow \downarrow} \\ \end{matrix}\right),$

which is determined from the projected components

$\rho^{\mu\nu}_{\alpha l} = \frac{1}{N_{\bf k}}
\sum_{n{\bf k}}f_{n{\bf k}} \sum_{m=-l}^{l} \langle \chi_{n {\bf
k}}^\mu | Y_{lm}^\alpha \rangle \langle Y_{lm}^\alpha | \chi_{n
{\bf k}}^\nu \rangle$

of the spinor $|\Psi_{n{\bf
k}}\rangle=\left(\begin{matrix}\chi_{n{\bf k}}^\uparrow \\\chi_{n{\bf
k}}^\downarrow \end{matrix}\right)$

Similarly, the lines after "magnetization (x)", "magnetization (y)", and
"magnetization (z)"correspond to the partial magnetization density

$m_{\alpha l}^j = \frac{1}{2}\sum_{\mu,\nu=1}^2
\sigma^j_{\mu \nu} \rho_{\alpha l}^{\mu \nu}.$

projected onto Pauli matrices $\\\sigma_1$, $\sigma_2$,
$\mathbf{\sigma}_3\\$. By default, this
corresponds to Cartesian directions $\sigma_1=\hat
x$, $\sigma_2 =\hat y$,
$\sigma_3 = \hat z$, but the orientation
can be changed using [SAXIS](SAXIS.md).

## Partial density of states (pDOS)
The partial density of states (pDOS) is the DOS projected onto specific
ions or atomic orbitals. The output for it can be found in the following
output files:

- [PROCAR](../output-files/PROCAR.md): the primary output for pDOS data.
  Each block lists the projection weight onto each atomic site and
  angular-momentum channel ($s$,
  $p$, $d$, ...) for every band and k-point.
- [vasprun.xml](../output-files/Vasprun.xml.md): the pDOS is stored in
  the `<dos><partial>` block, organized by ion and spin:

    <dos>
     <partial>
      <array>
       <dimension dim="1">gridpoints</dimension>
       <dimension dim="2">spin</dimension>
       <dimension dim="3">ion</dimension>
       <field>energy</field>
       <field>s</field>
       <field>py</field>
       <field>pz</field>
       <field>px</field>
       <field>dxy</field>
       ...
       <set>
        <set comment="ion 1">
         <set comment="spin 1">
          <r> -5.0000  5.5689  1.5445  1.5445  1.5445  0.0009 ... </r>
          ...

- [vaspout.h5](../output-files/Vaspout.h5.md): pDOS data is accessible
  via [py4vasp](https://vasp.at/py4vasp/latest/index.html):

    import py4vasp
    calc = py4vasp.Calculation.from_path(".")

    # Plot pDOS projected onto specific atoms (e.g., ions 3 and 5)
    calc.dos.plot(selection="3, 5")

    # Plot by element and orbital character
    calc.dos.plot(selection="Fe(d)")

You can learn more about plotting and calculating it in our tutorials:

- [Ni(100)
  surface](https://www.vasp.at/tutorials/latest/surface/part1/#surface-e02)
- [NiO
  bulk](https://vasp.at/tutorials/latest/strongly_correlated/part1/#strongly_correlated-e02)
- [CO
  molecule](https://www.vasp.at/tutorials/latest/molecules/part2/#molecules-e07)
- [STM simulations](https://www.vasp.at/tutorials/latest/surface/part3)

## References
1.  [↑](#cite_ref-Schuler:JPCM:2018_1-0) [M. Schüler, O.E. Peil, G.J.
    Kraberger, R. Pordzik, M. Marsman, G. Kresse, T.O. Wehling, and M.
    Aichhorn, J. Phys.: Condens. Matter **30**, 475901
    (2018).](https://doi.org/10.1088/1361-648X/aae80a)

## Related tags and articles
[RWIGS](RWIGS.md), [PROCAR](../output-files/PROCAR.md),
[PROOUT](../output-files/PROOUT.md), [DOSCAR](../output-files/DOSCAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LORBIT-_incategory-Examples)
