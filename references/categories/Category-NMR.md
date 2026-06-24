<!-- Source: https://vasp.at/wiki/index.php/Category:NMR | revid: 35930 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:NMR
**Nuclear magnetic resonance** (NMR) spectroscopy is a highly sensitive
technique for probing the atomic-scale structure of molecules, liquids,
and solids. However, directly extracting structural information from NMR
spectra is often challenging. Consequently, *ab-initio* quantum
mechanical simulations, such as those performed using VASP, play a
crucial role in accurately linking NMR spectra to atomic-scale
structural properties.

This page presents an overview of nuclear-electron interactions that can
be computed and are relevant to interpret NMR spectra.

## Contents

- [1 Chemical shielding](#Chemical_shielding)
  - [1.1 Nuclear-independent chemical
    shielding](#Nuclear-independent_chemical_shielding)
- [2 Magnetic susceptibility](#Magnetic_susceptibility)
- [3 Quadrupolar nuclei - electric field
  gradient](#Quadrupolar_nuclei_-_electric_field_gradient)
- [4 Hyperfine coupling](#Hyperfine_coupling)
- [5 Additional resources](#Additional_resources)
  - [5.1 Lectures](#Lectures)
  - [5.2 Tutorials](#Tutorials)
- [6 References](#References)

## Chemical shielding
[![](https://vasp.at/wiki/images/thumb/5/52/Chemical_shielding.png/200px-Chemical_shielding.png)](https://vasp.at/wiki/File:Chemical_shielding.png)

The external magnetic field **B***_(ext)* (purple) induces currents in
the electrons in atoms. These NMR response currents (black arrows) in
turn induce an opposing magnetic field **B***_(in)* (red), reducing the
magnetic field at the position of the nucleus, effectively shielding the
nucleus from **B***_(ext)*.

The effective B-field felt by a nucleus with finite nuclear spin is
related to the applied B field via the chemical shielding tensor. The
applied B-field induces a para- and diamagnetic NMR response current in
the electrons and screens the nucleus with an induced B-field that
follows from the Biot-Savart law, c.f. figure. The chemical shift is the
difference in chemical shielding σ relative to a reference σ_(ref).

$\delta_{ij} = \sigma_{ij}^{\mathrm{ref}} -
\sigma_{ij}.$

VASP can efficiently compute electronic properties in bulk systems
thanks to the [projector-augmented
wave](../redirects/Projector-augmented_wave.md) (PAW)
method which takes advantage of
[pseudopotentials](../redirects/Pseudopotentials.md) and a
[frozen core
approximation](Category-Pseudopotentials.md).
However, the [standard PAW
transformation](../redirects/PAW_formalism.md) does not fully
account for how the gauge field $A$
interacts with the reconstructed wavefunctions in the augmentation
regions (near atomic cores). Thus, NMR calculations
([`LCHIMAG`](../incar-tags/LCHIMAG.md)` = True`) are based on an extended
version of the [PAW method](../redirects/PAW_method.md), the
gauge-invariant PAW (GIPAW)
method^([\[1\]](#cite_note-pickard:prb:2001-1)[\[2\]](#cite_note-yates:prb:2007-2))
that properly ensures the gauge invariance. The NMR currents
([WRT_NMRCUR](../incar-tags/WRT_NMRCUR.md)) are computed using linear
response theory.

- Learn [how to calculate the chemical
  shielding](../tutorials/Calculating_the_chemical_shieldings.md).

### Nuclear-independent chemical shielding
Nuclear-independent chemical shielding (NICS) is a computational method
used to quantify aromaticity in molecules by calculating the magnetic
shielding at a virtual point (not at a nucleus) in space, typically at
the center of a ring or above it
^([\[3\]](#cite_note-schleyer:1996-3)[\[4\]](#cite_note-chen:schleyer:2005-4)).
See [NUCIND](../incar-tags/NUCIND.md) for more information.

## Magnetic susceptibility
The macroscopic magnetic susceptibility $\chi$ is defined by ^([\[5\]](#cite_note-mauri:louie:1996-5))

$\textbf{B}_{\textrm{in}}^{(1)}(\textbf{G}=0) =
\frac{8 \pi}{3} \chi \textbf{B}_{ext},$

where $\textbf{B}_{ext}$ is the
external magnetic field and $\textbf{B}_{\textrm{in}}^{(1)}$ is the induced magnetic
field. This must be taken into account for the chemical shielding as a
G=0 contribution.

It is calculated within linear response theory
([`LCHIMAG`](../incar-tags/LCHIMAG.md)` = True`), where a key variable
*Q_(ij)* is approximated in two ways. The so-called *pGv* approximation
is used by default ^([\[2\]](#cite_note-yates:prb:2007-2)), where *p* is
momentum, *v* is velocity, and *G* is a Green's function. An alternative
approach, the *vGv* approximation is available to calculate the
susceptibility ^([\[6\]](#cite_note-avezac:prb:2007-6)). See
[LVGVCALC](../incar-tags/LVGVCALC.md) and
[LVGVAPPL](../incar-tags/LVGVAPPL.md) to control the approximation.

- Learn [how to perform a magnetic susceptibility
  calculation.](../tutorials/Calculating_the_magnetic_susceptibility.md)

## Quadrupolar nuclei - electric field gradient
[![](https://vasp.at/wiki/images/thumb/7/73/Quadrupolar_efg.png/250px-Quadrupolar_efg.png)](https://vasp.at/wiki/File:Quadrupolar_efg.png)

The quadrupolar electric field of a nitrogen nucleus coupling to
electric field gradient *V* in MAPbI3 (methyl ammonium lead (III)
iodide)

Nuclei with **I** \> ± ½ have a non-zero electric field gradient (EFG)
and an electronic quadrupolar moment. The electric quadrupolar moment
couples with the EFG and so the chemical environment of the nucleus may
be probed using nuclear quadrupole resonance (NQR)
^([\[7\]](#cite_note-nqr:web-7)) (sometimes called zero-field NMR
spectroscopy). The EFG is the second derivative of the potential
$V$:

$V_{ij} = \frac{\partial^2 V}{\partial x_i
\partial x_j}$,

which is a sum of three parts along the Cartesian *i*,*j* axes:

$V_{i,j} = \tilde{V}_{i,j} -\tilde{V}_{i,j}^1 +
V_{i,j}^1$

where $\tilde{V}_{i,j}$ is the
plane-wave part of the AE potential, $\tilde{V}_{i,j}^1$ is the one-center expansion of the
pseudopotential method, and $V_{i,j}^1$
is the one-center expansion of the AE potential.

In VASP, the EFG is calculated using the [LEFG](../incar-tags/LEFG.md) tag.
The commonly reported nuclear quadrupolar coupling constant *C_(q)* is
then printed using isotope-specific quadrupole moment defined using
[QUAD_EFG](../incar-tags/QUAD_EFG.md)
^([\[8\]](#cite_note-petrilli:prb:1998-8)).

- Learn [how to perform an electric field gradient
  calculation](../tutorials/Calculating_the_electric_field_gradient.md).

## Hyperfine coupling
[![](https://vasp.at/wiki/images/thumb/7/7b/Hyperfine_coupling.png/250px-Hyperfine_coupling.png)](https://vasp.at/wiki/File:Hyperfine_coupling.png)

Hyperfine coupling between the nuclear spin and the electronic spin of
the unpaired electron at a nitrogen-vacancy (NV) center in diamond.

The hyperfine tensor $A^I$ describes the
interaction between a nuclear spin $S^I$
and the electronic spin distribution $S^e$. In most cases associated with a paramagnetic defect state
measureable by electron paramagnetic resonance (EPR)
^([\[9\]](#cite_note-weil:bolton:2007-9)):

$E=\sum_{ij} S^e_i A^I_{ij} S^I_j.$

The hyperfine tensor is split into two terms, isotropic (or Fermi
contact) $A^I_{iso}$ and anisotropic
(or dipolar contributions) $A^I_{ani}$:

$A^I_{i,j} = (A^I_{iso})_{i,j} +
(A^I_{ani})_{i,j}.$

$A^I_{iso}$ is calculated based on the
spin-density^([\[10\]](#cite_note-szasz:prb:2013-10)) and
$A^I_{ani}$ is calculated based on the
dipolar-dipolar contribution terms $W_{i,j}(\textbf{R})$. The hyperfine tensor calculation itself
is defined using [`LHYPERFINE`](../incar-tags/LHYPERFINE.md)` = True`.
Both the Fermi contact and dipolar contribution terms are related to the
nuclear gyromagnetic moment γ, which are controlled by setting
[NGYROMAG](../incar-tags/NGYROMAG.md).

- Learn [how to perform a hyperfine coupling
  calculation.](../redirects/Calculating_the_hyperfine_coupling_constant.md)

## Additional resources
### Lectures
- Lecture on [PAW, GIPAW, and NMR theory](https://youtu.be/CyALJ8Qb1yk).
- Lecture on [NMR theory and
  calculations](https://youtu.be/Jw8oFzh9Z3k).

### Tutorials
- Tutorial for [chemical shielding
  calculations](https://www.vasp.at/tutorials/latest/nmr/part1).
- Tutorial for [coupling constants and two-center correction
  calculations](https://www.vasp.at/tutorials/latest/nmr/part2).
- Tutorial for [NICS and current
  calculations](https://www.vasp.at/tutorials/latest/nmr/part3).

## References
1.  [↑](#cite_ref-pickard:prb:2001_1-0) [C. J. Pickard and F. Mauri,
    *All-electron magnetic response with pseudopotentials: NMR chemical
    shifts*, Phys. Rev. B **63**, 245101
    (2001).](https://doi.org/10.1103/PhysRevB.63.245101)
2.  ↑ ^([a](#cite_ref-yates:prb:2007_2-0))
    ^([b](#cite_ref-yates:prb:2007_2-1)) [J. R. Yates, C. J. Pickard,
    and F. Mauri, *Calculation of NMR chemical shifts for extended
    systems using ultrasoft pseudopotentials*, Phys. Rev. B **76**,
    024401 (2007).](https://doi.org/10.1103/PhysRevB.76.024401)
3.  [↑](#cite_ref-schleyer:1996_3-0) [P. von Ragué Schleyer, C.
    Maerker, A. Dransfeld, H. Jiao, and N. J. R. van Eikema Hommes,
    *Nucleus-Independent Chemical Shifts:  A Simple and Efficient
    Aromaticity Probe*, J. Am. Chem. Soc. **118**, 6317
    (1996).](https://doi.org/10.1021/ja960582d)
4.  [↑](#cite_ref-chen:schleyer:2005_4-0) [Z. Chen, C. S. Wannere, C.
    Corminboeuf, R. Puchta, and P. von Ragué Schleyer,
    *Nucleus-Independent Chemical Shifts (NICS) as an Aromaticity
    Criterion*, Chem. Rev. 10, **105**, 3842–3888
    (2005).](https://doi.org/10.1021/cr030088+)
5.  [↑](#cite_ref-mauri:louie:1996_5-0) [F. Mauri and S. G. Louie,
    *Magnetic Susceptibility of Insulators from First Principles*, Phys.
    Rev. Lett. **76**, 4246
    (1996).](https://doi.org/10.1103/PhysRevLett.76.4246)
6.  [↑](#cite_ref-avezac:prb:2007_6-0) [M. d'Avezac, N. Marzari, and F.
    Mauri, *Spin and orbital magnetic response in metals: Susceptibility
    and NMR shifts*, Phys. Rev. B **76**, 165122
    (2007).](https://doi.org/10.1103/PhysRevB.76.165122)
7.  [↑](#cite_ref-nqr:web_7-0) [Nuclear quadrupole resonance,
    www.wikipedia.org
    (2025)](https://en.wikipedia.org/wiki/Nuclear_quadrupole_resonance)
8.  [↑](#cite_ref-petrilli:prb:1998_8-0) [H. M. Petrilli, P. E.
    Blöchl, P. Blaha, and K. Schwarz, *Electric-field-gradient
    calculations using the projector augmented wave method*, Phys. Rev.
    B **57**, 14690 (1998).](https://doi.org/10.1103/PhysRevB.57.14690)
9.  [↑](#cite_ref-weil:bolton:2007_9-0) [J. Weil and J. Bolton,
    *Electron Paramagnetic Resonance: Elementary Theory and Practical
    Applications*, (2007).](https://doi.org/10.1002/0470084987)
10. [↑](#cite_ref-szasz:prb:2013_10-0) [K. Szasz, T. Hornos, M. Marsman,
    and A. Gali, *Hyperfine coupling of point defects in semiconductors
    by hybrid density functional calculations: The role of core spin
    polarization*, Phys. Rev. B, **88**, 075202
    (2013).](https://doi.org/10.1103/PhysRevB.88.075202)
