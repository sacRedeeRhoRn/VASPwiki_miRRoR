<!-- Source: https://vasp.at/wiki/index.php/LHYPERFINE | revid: 31025 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LHYPERFINE
LHYPERFINE = .TRUE. \| .FALSE.  
Default: **LHYPERFINE** = .FALSE. 

Description: compute the hyperfine tensors at the atomic sites
(available as of vasp.5.3.2).

------------------------------------------------------------------------

To have VASP compute the hyperfine tensors at the atomic sites, set

    LHYPERFINE = .TRUE.

|  |
|----|
| **Mind:** Spin-polarized calclulations [ISPIN](ISPIN.md) = 2 **must** be used. |

|  |
|----|
| **Warning:** Noncollinear calculations [LNONCOLLINEAR](LNONCOLLINEAR.md) = .TRUE. are not currently implemented for LHYPERFINE. There is not a warning message for this, which will be added in future releases, see [known issues.](../misc/Known_issues.md) |

The hyperfine tensor A^(I) describes the interaction between a nuclear
spin S^(I) (located at site **R**_(I)) and the electronic spin
distribution S^(e) (in most cases associated with a paramagnetic defect
state) ^([\[1\]](#cite_note-szasz:prb:2013-1)):

$E=\sum_{ij} S^e_i A^I_{ij} S^I_j$

In general it is written as the sum of an isotropic part, the so-called
Fermi contact term, and an anisotropic (dipolar) part.

The Fermi contact term is given by

$(A^I_{\mathrm{iso}})_{ij}=
\frac{2}{3}\frac{\mu_0\gamma_e\gamma_I}{\langle
S_z\rangle}\delta_{ij}\int
\delta_T(\mathbf{r})\rho_s(\mathbf{r}+\mathbf{R}_I)d\mathbf{r}$

where ρ_(s) is the spin density, μ₀ is the magnetic susceptibility of
free space, γ_(e) the electron gyromagnetic ratio, γ_(I) the nuclear
gyromagnetic ratio of the nucleus at **R**_(I), and
$\langle S_z \rangle$ the expectation
value of the *z*-component of the total electronic spin.

δ_(T)(**r**) is a smeared out δ function, as described in the Appendix
of Ref. ^([\[2\]](#cite_note-bloechl:prb:2000-2)).

The dipolar contributions to the hyperfine tensor are given by

$(A^I_{\mathrm{ani}})_{ij}=\frac{\mu_0}{4\pi}\frac{\gamma_e\gamma_I}{\langle
S_z\rangle} \int
\frac{\rho_s(\mathbf{r}+\mathbf{R}_I)}{r^3}\frac{3r_ir_j-\delta_{ij}r^2}{r^2}
d\mathbf{r}$

In the equations above *r*=\|**r**\|, *r*_(i) the i-th component of
**r**, and **r** is taken relative to the position of the nucleus
**R**_(I).

The nuclear gyromagnetic ratios should be specified by means of the
[NGYROMAG](NGYROMAG.md)-tag.

A guide for [calculating the hyperfine coupling
constant](../redirects/Calculating_the_hyperfine_coupling_constant.md)
is available.

|  |
|----|
| **Mind:** The Zeroth Order Regular Approximation (ZORA) is used to account for the relativistic effects in the hyperfine tensor calculations. |

## Contents

- [1 Output](#Output)
- [2 Units](#Units)
- [3 Advice](#Advice)
- [4 Related tags and articles](#Related_tags_and_articles)
- [5 References](#References)

## Output
As usual, all output is written to the [OUTCAR](../output-files/OUTCAR.md)
file. VASP writes three blocks of data. The first is for the Fermi
contact coupling parameter:

     Fermi contact (isotropic) hyperfine coupling parameter (MHz)
     -------------------------------------------------------------
      ion      A_pw      A_1PS     A_1AE     A_1c      A_tot
     -------------------------------------------------------------
       1       ...       ...       ...       ...       ...
      ..       ...       ...       ...       ...       ...

     -------------------------------------------------------------

with an entry for each ion on the [POSCAR](../input-files/POSCAR.md) file.
A_(pw), A_(1PS), A_(1AE), and A_(1c) are the plane wave, pseudo
one-center, all-electron one-center, and one-center core contributions
to the Fermi contact term, respectively. The total Fermi contact term is
given by A_(tot).

[TABLE]

The dipolar contributions are listed next:

     Dipolar hyperfine coupling parameters (MHz)
     ---------------------------------------------------------------------
      ion      A_xx      A_yy      A_zz      A_xy      A_xz      A_yz
     ---------------------------------------------------------------------
       1       ...       ...       ...       ...       ...       ...
      ..       ...       ...       ...       ...       ...       ...

     ---------------------------------------------------------------------

Again one line per ion in the [POSCAR](../input-files/POSCAR.md) file.

The total hyperfine tensors are written as:

     Total hyperfine coupling parameters after diagonalization (MHz)
     (convention: |A_zz| > |A_xx| > |A_yy|)
     ----------------------------------------------------------------------
      ion      A_xx      A_yy      A_zz     asymmetry (A_yy - A_xx)/ A_zz
     ----------------------------------------------------------------------
       1       ...       ...       ...         ...
      ..       ...       ...       ...         ...

     ----------------------------------------------------------------------

i.e., the tensors have been diagonalized and rearranged.

[TABLE]

## Units
The Fermi contact term $A$ is measured
in following units

$\[A\]= \left\[\mu_0\right\]\times \left\[g_e
\mu_e\right\]\times \left\[g_j \mu_j\right\]\times
\left\[|\psi(0)|^2\right\] = \frac{T^2m^3}{J}\times \frac{J}{T}\times
\frac{MHz}{T}\times \frac{1}{m^3} = MHz$

with $\mu_0=4\pi\times 10^{-7} T^2 m^3 J^{-1}$, $g_e\mu_e=9.28476377\times 10^{-24} J
T^{-1}, |\psi(0)|^2=10^{30}m^{-3}$.
[NGYROMAG](NGYROMAG.md) is given in units of MHz/T.

## Advice
It is possible that your system relaxes to a non-magnetic solution,
causing the hyperfine splitting to disappear (i.e. all zeros). If you
think your system should be magnetic, you can enforce it using
[NUPDOWN](NUPDOWN.md), which will return the hyperfine
splitting, cf. forum post:
[https://vasp.at/forum/viewtopic.php?t=16921](https://vasp.at/forum/viewtopic.php?t=16921).
[NUPDOWN](NUPDOWN.md) will change the
`Total magnetic moment S=` at the start of the hyperfine coupling
section in the [OUTCAR](../output-files/OUTCAR.md).

|  |
|----|
| **Important:** For some cells, the total magnetic moment S can be very small (`grep " mag=" OSZICAR`), near zero. In the above equations, the isotropic and anisotropic components of the hyperfine coupling parameter (A^(I)_(iso) and A^(I)_(ani)) are calculated by dividing through by S (cf. ⟨S_(z)⟩). To avoid division by zero, S is reset to 1 when S \< 10⁻³. `Total magnetic moment S=` is changed, changing the hyperfine coupling constants, too. These hyperfine coupling constants are likely not meaningful. In future versions of the code, there will be a warning message stating that S has been reset and the correct total magnetic moment will be printed. |

## Related tags and articles
[NGYROMAG](NGYROMAG.md)

[Calculating the hyperfine coupling
constant](../redirects/Calculating_the_hyperfine_coupling_constant.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LHYPERFINE-_incategory-Examples)

## References
------------------------------------------------------------------------

1.  ↑ ^([a](#cite_ref-szasz:prb:2013_1-0))
    ^([b](#cite_ref-szasz:prb:2013_1-1)) [K. Szasz, T. Hornos, M.
    Marsman, and A. Gali, *Hyperfine coupling of point defects in
    semiconductors by hybrid density functional calculations: The role
    of core spin polarization*, Phys. Rev. B, **88**, 075202
    (2013).](https://doi.org/10.1103/PhysRevB.88.075202)
2.  [↑](#cite_ref-bloechl:prb:2000_2-0) [P. Bloechl, *First-principles
    calculations of defects in oxygen-deficient silica exposed to
    hydrogen*, Phys. Rev. B, **62**, 6158
    (2000).](https://doi.org/10.1103/PhysRevB.62.6158)
3.  [↑](#cite_ref-yazyev:prb:2005_3-0) [O. V. Yazyev, I. Tavernelli, L.
    Helm, and U. R. Roethlisberger, *Core spin-polarization correction
    in pseudopotential-based electronic structure calculations*, Phys.
    Rev. B **71**, 115110
    (2006).](https://doi.org/10.1103/PhysRevB.71.115110)
