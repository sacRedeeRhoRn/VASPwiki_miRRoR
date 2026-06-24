<!-- Source: https://vasp.at/wiki/index.php/Category:Hybrid_functionals | revid: 36697 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Hybrid functionals
**Hybrid functionals** go beyond the semilocal approximations by mixing
the Hartree-Fock (HF) and semilocal (SL)
exchange^([\[1\]](#cite_note-becke:jcp:93-1)):

$E_{\mathrm{xc}}^{\mathrm{hybrid}}=a
E_{\mathrm{x}}^{\mathrm{HF}} + (1-a)E_{\mathrm{x}}^{\mathrm{SL}} +
E_{\mathrm{c}}^{\mathrm{SL}}$

where $a$ is the mixing parameter that
determines the relative weights of HF and semilocal exchange.

Depending on the type of systems or the property under consideration
they can be more accurate than semilocal (GGA, meta-GGA) functionals.
For instance, hybrid functionals are usually more suited for calculating
the electronic and magnetic properties of nonmetallic systems. They are
particularly recommended for bandgap
calculations.^([\[2\]](#cite_note-heyd:jcp:05-2)[\[3\]](#cite_note-chen2018nonempirical-3))
Polarons^([\[4\]](#cite_note-franchini:nrm:21-4)) or defect
states^([\[5\]](#cite_note-oba:prb:08-5)) are among properties that can
also be better described by hybrid functionals. Note that hybrid
functionals are also often good at treating [strongly correlated
electrons](Category-Strongly_correlated_electrons.md).^([\[6\]](#cite_note-liu2019assessing-6))

- 

[TABLE]

## Contents

- [1 Overview](#Overview)
- [2 Technical points](#Technical_points)
- [3 Additional resources](#Additional_resources)
  - [3.1 Tutorials](#Tutorials)
  - [3.2 Lectures](#Lectures)
  - [3.3 How to](#How_to)
  - [3.4 Further reading](#Further_reading)
- [4 References](#References)

## Overview
The hybrid functionals can be divided into families according to the
type of semilocal approximation that is used (LDA, GGA, or MGGA) and the
interelectronic range at which the HF exchange is applied: at full range
(unscreened hybrids) or either at short or long range (called screened
or range-separated hybrids). From the practical point of view, the
short-range hybrid functionals like
HSE06^([\[7\]](#cite_note-krukau:jcp:06-7)) are preferable for periodic
solids, since leading to faster convergence with respect to the number
of k-points (or size of the unit cell).

The different families of hybrid functionals available in VASP are
described in details at [formalism of the HF method and
hybrids](Hybrid_functionals-_formalism.md)
along with examples and links to the corresponding
[INCAR](../input-files/INCAR.md) files.

Details about the implementation of the unscreened hybrid functionals
can be found in the work of Paier et
al.,^([\[8\]](#cite_note-paier:jcp:05-8)) while details specific to the
screened hybrid functionals can be found in Refs.
^([\[9\]](#cite_note-paier:jcp:06-9)[\[10\]](#cite_note-angyan:jpa:2006-10))
Refs.
^([\[11\]](#cite_note-cui2018doubly-11)[\[6\]](#cite_note-liu2019assessing-6))
report the development of dielectric-dependent hybrid functionals, which
provide very accurate band gaps and are also available in VASP.

Note that as in most other codes, hybrid functionals are implemented in
VASP within the generalized KS
scheme,^([\[12\]](#cite_note-seidl:prb:96-12)) which means that the
total energy is minimized, as in the HF theory, with respect to the
orbitals instead of the electron density.

VASP offers a convenient way to generate the [band structure with hybrid
functionals](Band-structure_calculation_using_hybrid_functionals.md).

## Technical points
- The unscreened Coulomb potential used to evaluate the exchange
  integral in HF has an integrable Coulomb singularity that leads to
  slow convergence with respect to supercell size (or equivalently **k**
  point sampling). To make the computations feasible requires special
  treatment of the [Coulomb
  singularity](Coulomb_singularity.md).

&nbsp;

- The [Downsampling of the HF
  operator](Downsampling_of_the_Hartree-Fock_operator.md)
  allows for the use of a coarser **k** point sampling for the HF
  operator, and therefore faster
  calculations.^([\[9\]](#cite_note-paier:jcp:06-9)) However, this
  option should be use with care for metals.

&nbsp;

- The Adaptively Compressed Exchange
  Operator,^([\[13\]](#cite_note-linlin:jctc:2016-13)) that allows for a
  more efficient evaluation of the Fock operator, is used if the
  Davidson algorithm ([ALGO](../incar-tags/ALGO.md) = Normal, the default)
  is selected (see [LFOCKACE](../incar-tags/LFOCKACE.md) for more
  details).

## Additional resources
### Tutorials
- Tutorial for [hybrid
  calculations](https://www.vasp.at/tutorials/latest/hybrids/part1).

### Lectures
- Lecture on [hybrid functionals](https://youtu.be/zNc0bx8FTlU).

### How to
- [Formalism of the HF method and
  hybrids](Hybrid_functionals-_formalism.md).
  The various families are described.
- [List of available hybrid
  functionals](List_of_hybrid_functionals.md)
  and how to specify them in the [INCAR](../input-files/INCAR.md) file.
- [Downsampling of the Hartree-Fock
  operator](Downsampling_of_the_Hartree-Fock_operator.md)
  to reduce the computational cost.
- [band-structure calculation using hybrid
  functionals](Band-structure_calculation_using_hybrid_functionals.md).

### Further reading
In addition to the works already cited above, the selected publications
listed below describe methodological developments or computational
studies performed using the hybrid functionals implemented in VASP.

- The B3LYP functional applied to solid-state systems and its failure
  for metals^([\[14\]](#cite_note-paier:jcp:07-14)).
- Applications of hybrid functionals to selected materials:
  Ceria,^([\[15\]](#cite_note-juarez:prb:07-15)) lead
  chalcogenides,^([\[16\]](#cite_note-hummer:prb:07-16)) CO adsorption
  on
  metals,^([\[17\]](#cite_note-stroppa:prb:07-17)[\[18\]](#cite_note-stroppa:njp:08-18))
  excitonic properties,^([\[19\]](#cite_note-paier:prb:08-19)) SrTiO and
  BaTiO, ^([\[20\]](#cite_note-wahl:prb:08-20))
  perovskites,^([\[21\]](#cite_note-franchini:jpcm:14-21)) and
  transition-metal oxides.^([\[22\]](#cite_note-gopidi:prb:26-22))
- HSEsol hybrid functional.^([\[23\]](#cite_note-schimka:jcp:11-23))
- Analysis of the HSE parameter
  space.^([\[24\]](#cite_note-moussa:jcp:12-24))
- Automated workflow for non-empirical Wannier-localized optimal tuning
  of range-separated hybrid
  functionals.^([\[25\]](#cite_note-gant:cpc:26-25))

## References
1.  [↑](#cite_ref-becke:jcp:93_1-0) [A. D. Becke, J. Chem. Phys. **98**,
    5648 (1993).](https://doi.org/10.1063/1.464913)
2.  [↑](#cite_ref-heyd:jcp:05_2-0) [J. Heyd, J. E. Peralta, G. E.
    Scuseria, and R. L. Martin, *Energy band gaps and lattice parameters
    evaluated with the Heyd-Scuseria-Ernzerhof screened hybrid
    functional*, J. Chem. Phys. **123**, 174101
    (2005).](https://doi.org/10.1063/1.2085170)
3.  [↑](#cite_ref-chen2018nonempirical_3-0) [W. Chen, G. Miceli, G.M.
    Rignanese, and A. Pasquarello, *Nonempirical dielectric-dependent
    hybrid functional with range separation for semiconductors and
    insulators*, Phys. Rev. Mater. **2**, 073803
    (2018).](https://doi.org/10.1103/PhysRevMaterials.2.073803)
4.  [↑](#cite_ref-franchini:nrm:21_4-0) [C. Franchini, M. Reticcioli, M.
    Setvin, and U. Diebold, *Polarons in Materials*, Nat. Rev. Mat.
    **6**, 560 (2021).](https://doi.org/10.1038/s41578-021-00289-w)
5.  [↑](#cite_ref-oba:prb:08_5-0) [F. Oba, A. Togo, I. Tanaka, J. Paier,
    and G. Kresse, Phys. Rev. B **77**, 245202
    (2008).](https://doi.org/10.1103/PhysRevB.77.245202)
6.  ↑ ^([a](#cite_ref-liu2019assessing_6-0))
    ^([b](#cite_ref-liu2019assessing_6-1)) [P. Liu, C. Franchini, M.
    Marsman, and G. Kresse, *Assessing model-dielectric-dependent hybrid
    functionals on the antiferromagnetic transition-metal monoxides MnO,
    FeO, CoO, and NiO*, J. Phys.: Condens. Matter **32**, 015502
    (2020).](https://doi.org/10.1088/1361-648x/ab4150)
7.  [↑](#cite_ref-krukau:jcp:06_7-0) [A. V. Krukau , O. A. Vydrov, A. F.
    Izmaylov, and G. E. Scuseria, J. Chem. Phys. **125**, 224106
    (2006).](https://doi.org/10.1063/1.2404663)
8.  [↑](#cite_ref-paier:jcp:05_8-0) [J. Paier, R. Hirschl, M. Marsman,
    and G. Kresse, J. Chem. Phys. **122**, 234102
    (2005).](https://doi.org/10.1063/1.1926272)
9.  ↑ ^([a](#cite_ref-paier:jcp:06_9-0))
    ^([b](#cite_ref-paier:jcp:06_9-1)) [J. Paier, M. Marsman, K.
    Hummer, G. Kresse, I.C. Gerber, and J.G. Ángyán, J. Chem. Phys.
    **124**, 154709 (2006).](https://doi.org/10.1063/1.2187006)
10. [↑](#cite_ref-angyan:jpa:2006_10-0) [J. G. Ángyán, I. Gerber, and M.
    Marsman, *Spherical harmonic expansion of short-range screened
    Coulomb interactions*, J. Phys. A: Math. Gen. **39**, 8613
    (2006).](http://dx.doi.org/10.1088/0305-4470/39/27/005)
11. [↑](#cite_ref-cui2018doubly_11-0) [Z.H. Cui, Y.C. Wang, M.Y.
    Zhang, X. Xu, and H. Jiang, *Doubly Screened Hybrid Functional: An
    Accurate First-Principles Approach for Both Narrow- and Wide-Gap
    Semiconductors* J. Phys. Chem. Lett., **9**, 2338-2345
    (2018).](https://doi.org/10.1021/acs.jpclett.8b00919)
12. [↑](#cite_ref-seidl:prb:96_12-0) [A. Seidl, A. Görling, P. Vogl,
    J.A. Majewski, and M. Levy, Phys. Rev. B **53**, 3764
    (1996).](https://doi.org/10.1103/PhysRevB.53.3764)
13. [↑](#cite_ref-linlin:jctc:2016_13-0) [L. Lin, J. Chem. Theory
    Comput. **12**, 2242-2249
    (2016).](https://doi.org/10.1021/acs.jctc.6b00092)
14. [↑](#cite_ref-paier:jcp:07_14-0) [J. Paier, M. Marsman, and G.
    Kresse, J. Chem. Phys. **127**, 024103
    (2007).](https://doi.org/10.1063/1.2747249)
15. [↑](#cite_ref-juarez:prb:07_15-0) [J. L. F. Da Silva, M. V.
    Ganduglia-Pirovano, J. Sauer, V. Bayer, and G. Kresse, Phys. Rev. B
    **75**, 045121 (2007).](https://doi.org/10.1103/PhysRevB.75.045121)
16. [↑](#cite_ref-hummer:prb:07_16-0) [Hummer, A. Grüneis, and G.
    Kresse, Phys. Rev. B **75**, 195211
    (2007).](https://doi.org/10.1103/PhysRevB.75.195211)
17. [↑](#cite_ref-stroppa:prb:07_17-0) [A. Stroppa, K. Termentzidis, J.
    Paier, G. Kresse, and J. Hafner, Phys. Rev. B **76**, 195440
    (2007).](https://doi.org/10.1103/PhysRevB.76.195440)
18. [↑](#cite_ref-stroppa:njp:08_18-0) [A. Stroppa and G. Kresse, New
    Journal of Physics **10**, 063020
    (2008).](https://doi.org/10.1088/1367-2630/10/6/063020)
19. [↑](#cite_ref-paier:prb:08_19-0) [J. Paier, M. Marsman, and G.
    Kresse, Phys. Rev. B **78**, 121201(R)
    (2008).](https://doi.org/10.1103/PhysRevB.78.121201)
20. [↑](#cite_ref-wahl:prb:08_20-0) [R. Wahl, D. Vogtenhuber, and G.
    Kresse, Phys. Rev. B **78**, 104116
    (2008).](https://doi.org/10.1103/PhysRevB.78.104116)
21. [↑](#cite_ref-franchini:jpcm:14_21-0) [C. Franchini, *Hybrid
    functionals applied to perovskites*, J. Phys.: Condens. Matter
    **26**, 253202
    (2014).](http://dx.doi.org/10.1088/0953-8984/26/25/253202)
22. [↑](#cite_ref-gopidi:prb:26_22-0) [H. R. Gopidi, R. Zhang, Y.
    Wang, A. Patra, J. Sun, A. Ruzsinszky, J. P. Perdew, and P. Canepa,
    *Reducing self-interaction error in transition-metal oxides with
    different exact-exchange fractions for energy and density*, Phys.
    Rev, B **113**, 165115 (2026).](https://doi.org/10.1103/myd5-l4f4)
23. [↑](#cite_ref-schimka:jcp:11_23-0) [L. Schimka, J. Harl, and G.
    Kresse, J. Chem. Phys. **134**, 024116
    (2011).](https://doi.org/10.1063/1.3524336)
24. [↑](#cite_ref-moussa:jcp:12_24-0) [J. E. Moussa, P. A. Schultz,
    and J. R. Chelikowsky, *Analysis of the Heyd-Scuseria-Ernzerhof
    density functional parameter space*, J. Chem. Phys. **136**, 204117
    (2012).](http://doi.org/10.1063/1.4722993)
25. [↑](#cite_ref-gant:cpc:26_25-0) [S. E. Gant, F. Ricci, G. Ohad, A.
    Ramasubramaniam, L. Kronik, and J. B. Neaton, *Automated workflow
    for non-empirical Wannier-localized optimal tuning of
    range-separated hybrid functionals*, Comput. Phys. Commun. **320**,
    109995 (2026).](https://doi.org/10.1016/j.cpc.2025.109995)
