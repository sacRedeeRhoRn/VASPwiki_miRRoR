<!-- Source: https://vasp.at/wiki/index.php/Category:Electronic_occupancy | revid: 37023 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Electronic occupancy
Within the [PAW method](../redirects/PAW_method.md) there is the
occupation $f_k$ for the plane-wave part
and the on-site occupation matrix $\rho$
that characterize the [electronic
state](../redirects/Electronic_ground-state_properties.md).
Below we list tags and sections that can be used to influence the
occupation, besides the obvious influence of the specific
[structure](../redirects/Ionic_minimization.md) and
[exchange-correlation effects](../redirects/XC_functional.md).

## Modeling excited states by constrained occupation calculations
The **delta self-consistent field (ΔSCF)** method provides a practical
way to obtain neutral excitation energies within density functional
theory (DFT) by explicitly constraining the electronic **occupations**
of selected orbitals. In contrast to
[linear-response](Category-Linear_response.md)
or [many-body
approaches](Category-Many-body_perturbation_theory.md),
ΔSCF directly evaluates the total energy difference between ground and
excited electronic configurations from self-consistent calculations.
This approach connects closely to experimental observables such as the
**vertical absorption energy (VAE)**, **vertical emission energy
(VEE)**, and **zero-phonon lines (ZPLs)**, which are key quantities in
the [optical
spectroscopy](Category-Dielectric_properties.md)
of point defects in semiconductors and insulators
^([\[1\]](#cite_note-Freysoldt2014-1)).

- [$\Delta\mathrm{SCF}$
  calculations](/wiki/Delta_self-consistent_field "Delta self-consistent field"):
  example of zero-phonon line calculation of $\mathrm{NV}^-$ center in diamond

## Density-functional theory plus dynamical mean-field theory
**Density-functional theory plus dynamical mean-field theory
(DFT+DMFT)**^([\[2\]](#cite_note-kotliar:rmp:2006-2)) is a method that
provides a more accurate treatment of [**strongly correlated
materials**](../methods/Category-Strongly_correlated_electrons.md)
compared to [DFT+U](../methods/Category-DFT+U.md). While
[DFT+U](../methods/Category-DFT+U.md) is computationally much
more affordable, it incorporates a static correction for localized
electron interactions. DFT+DMFT, on the other hand, goes further by
treating these interactions dynamically, capturing frequency-dependent
electron correlations. A key feature of DFT+DMFT is that the charge
density is updated using the DMFT solution, ensuring a self-consistent
feedback between the correlated electronic states and the DFT potential.
This not only improves the description of phenomena like
**metal-insulator transitions** and quasiparticle renormalization but
also allows for the calculation of spectral properties such as
**photoemission spectra**, **transport properties**, and **total
energies relevant to structural distortions**. To facilitate DFT+DMFT
calculations, VASP provides a general interface to DMFT codes, allowing
occupation updates [ICHARG](../incar-tags/ICHARG.md)=5 via an external
file [vaspgamma.h5](../input-files/Vaspgamma.h5.md) /
[GAMMA](../input-files/GAMMA.md) to update the charge density.

- [DFT+DMFT
  calculations](../tutorials/DFT+DMFT_calculations.md):
  example of performing DFT+DMFT calculations using the [TRIQS
  software](https://triqs.github.io/triqs)^([\[3\]](#cite_note-parcollet:cpc:196-3))

## References
1.  [↑](#cite_ref-Freysoldt2014_1-0) [Christoph Freysoldt, Blazej
    Grabowski, Tilmann Hickel, Jörg Neugebauer, Georg Kresse, and
    Anderson Janotti, Rev. Mod. Phys.
    (2014).](http://dx.doi.org/10.1103/RevModPhys.86.253)
2.  [↑](#cite_ref-kotliar:rmp:2006_2-0) [G. Kotliar, S. Y. Savrasov, K.
    Haule, V. S. Oudovenko, O. Parcollet, and C. A. Marianetti,
    *Electronic structure calculations with dynamical mean-field
    theory*, Rev. Mod. Phys. **78**, 865
    (2006)](https://link.aps.org/doi/10.1103/RevModPhys.78.865)
3.  [↑](#cite_ref-parcollet:cpc:196_3-0) [O. Parcollet, M. Ferrero, T.
    Ayral, H. Hafermann, I. Krivenko, L. Messio and P. Seth, Computer
    Physics Communications **196**, 398
    (2015).](http://dx.doi.org/10.1016/j.cpc.2015.04.023)

------------------------------------------------------------------------
