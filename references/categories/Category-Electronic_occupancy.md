<!-- Source: https://vasp.at/wiki/index.php/Category:Electronic_occupancy | revid: 37023 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Electronic occupancy


Within the
<a href="/wiki/PAW_method" class="mw-redirect" title="PAW method">PAW
method</a> there is the occupation $f_k$ for the
plane-wave part and the on-site occupation matrix
$\rho$ that characterize the
<a href="/wiki/Electronic_ground-state_properties" class="mw-redirect"
title="Electronic ground-state properties">electronic state</a>. Below
we list tags and sections that can be used to influence the occupation,
besides the obvious influence of the specific
<a href="/wiki/Ionic_minimization" class="mw-redirect"
title="Ionic minimization">structure</a> and
<a href="/wiki/XC_functional" class="mw-redirect"
title="XC functional">exchange-correlation effects</a>.

## Modeling excited states by constrained occupation calculations\[<a
href="/wiki/index.php?title=Category:Electronic_occupancy&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Modeling excited states by constrained occupation calculations">edit</a> \| (./index.php.md)\]

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
<sup>[\[1\]](#cite_note-Freysoldt2014-1)</sup>.

- [$\Delta\mathrm{SCF}$
  calculations](/wiki/Delta_self-consistent_field "Delta self-consistent field"):
  example of zero-phonon line calculation of $\mathrm{NV}^-$ center in diamond

## Density-functional theory plus dynamical mean-field theory\[<a
href="/wiki/index.php?title=Category:Electronic_occupancy&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Density-functional theory plus dynamical mean-field theory">edit</a> \| (./index.php.md)\]

**Density-functional theory plus dynamical mean-field theory
(DFT+DMFT)**<sup>[\[2\]](#cite_note-kotliar:rmp:2006-2)</sup>
is a method that provides a more accurate treatment of [**strongly
correlated
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
  example of performing DFT+DMFT calculations using the
  <a href="https://triqs.github.io/triqs" class="external text"
  rel="nofollow">TRIQS software</a><sup>[\[3\]](#cite_note-parcollet:cpc:196-3)</sup>

## References\[<a
href="/wiki/index.php?title=Category:Electronic_occupancy&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-Freysoldt2014_1-0)
    <a href="http://dx.doi.org/10.1103/RevModPhys.86.253"
    class="external text" rel="nofollow">Christoph Freysoldt, Blazej
    Grabowski, Tilmann Hickel, Jörg Neugebauer, Georg Kresse, and Anderson
    Janotti, Rev. Mod. Phys. (2014).</a>
2.  [↑](#cite_ref-kotliar:rmp:2006_2-0)
    <a href="https://link.aps.org/doi/10.1103/RevModPhys.78.865"
    class="external text" rel="nofollow">G. Kotliar, S. Y. Savrasov, K.
    Haule, V. S. Oudovenko, O. Parcollet, and C. A. Marianetti,
    <em>Electronic structure calculations with dynamical mean-field
    theory</em>, Rev. Mod. Phys. <strong>78</strong>, 865 (2006)</a>
3.  [↑](#cite_ref-parcollet:cpc:196_3-0)
    <a href="http://dx.doi.org/10.1016/j.cpc.2015.04.023"
    class="external text" rel="nofollow">O. Parcollet, M. Ferrero, T. Ayral,
    H. Hafermann, I. Krivenko, L. Messio and P. Seth, Computer Physics
    Communications <strong>196</strong>, 398 (2015).</a>


------------------------------------------------------------------------


