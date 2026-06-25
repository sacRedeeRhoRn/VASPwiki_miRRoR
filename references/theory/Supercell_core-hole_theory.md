<!-- Source: https://vasp.at/wiki/index.php/Supercell_core-hole_theory | revid: 31970 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Supercell core-hole theory


In the Supercell core-hole
method[^karsai:prb:2018-1]
(SCH) a chosen core electron is removed from the core leaving behind a
positive charge, cf. [ICORELEVEL](../incar-tags/ICORELEVEL.md). Since
one wants to simulate the excitation of this electron into energetically
higher-lying states, one electron is added to valence/conduction bands
resembling the final state of the excitation process (this is also
referred to as the final state approximation). With this setup a fully
self-consistent electronic minimization is carried out. The core hole is
perfectly screened by the other electrons in metals so there should be
no difference between core-hole calculations and regular calculations.
In semiconductors and insulators, this screening is very weak and a very
strong attraction between the electrons and hole occurs, which results
in not only a lowering of the excited states compared to the valence
states, but also a very strong change of the valence/conduction band
structure. Hence the relaxation of the valence/conduction electrons is
the main effect in core-hole calculations. Fortunately the relaxation of
the core states in core-hole calculations is negligible. This makes the
implementation into a PAW framework smooth, since no on-the fly
recalculation of PAW potentials is needed in every step of the
electronic self-consistent cycle.

|  |
|----|
| **Mind:** It is important to use a sufficiently large supercell to minimize the interaction of neighboring core holes within periodic boundary conditions. Hence the computational expense within these methods comes mainly from the use of large super cells. Nevertheless this method is usually still computationally cheaper than the BSE method for core electrons. |

## Excited electron treatment\[<a
href="/wiki/index.php?title=Supercell_core-hole_theory&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Excited electron treatment">edit</a> \| (./index.php.md)\]

<figure class="mw-halign-right" typeof="mw:File/Thumb">
<a href="/wiki/File:Fch_xch.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/2/28/Fch_xch.png/300px-Fch_xch.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/2/28/Fch_xch.png/450px-Fch_xch.png 1.5x, /wiki/images/thumb/2/28/Fch_xch.png/600px-Fch_xch.png 2x"
width="300" height="300" /></a>
<figcaption>Schematic representation of the self-interaction effects in
the XCH spectra.</figcaption>
</figure>

Two different approaches can be used to treat the excited electron in
SCH. The excited electron can be placed into the lowest conduction band
in the **excited electron and core-hole
(XCH)**[^hetenyi:jcp:2004-2]
approach, alternatively the excited electron can be accounted for by a
negative background charge to ensure that the cell remains neutral in
the **full core-hole (FCH)**
[^Prendergasst:prl:2006-3]
method. These two approaches are discussed and compared in great detail
in Ref.
[^unzog:prb:2022-4].
The main shortcoming of the XCH approach comes from the self-interaction
effects of the electron exchange and correlation functional caused when
the excited electron is placed in the conduction band, which is more
pronounced for strongly localized conduction bands. The effects of the
self-interaction error are depicted in the figure on the right, which
schematically represents the excitations from the core *s*-orbital to
the lowest unoccupied *p*-orbital, i.e., the *K*-edge. The
self-interaction error in turn causes two effects: First, it shifts up
the energy level of the conduction band occupied by the excited electron
from the initial energy *C* to the new energy *C'*. Second, it
delocalizes the orbital. Furthermore, the conduction band electron
additionally contributes to the screening of the core hole, which in
turn shifts the higher-lying unoccupied states, as shown in the figure
for *a* and *b* bands. In FCH, by placing the negative charge in the
homogeneous background we avoid such self-interaction effects. For
systems, where the lowest conduction bands are strongly delocalized,
both XCH and FCH produce very similar results. However, for systems with
localized conduction states, e.g. Li-halides, the FCH has been shown to
yield better agreement with the results of the [BSE+GW
calculations](../tutorials/Bethe-Salpeter_equation_for_core_excitations.md)
as well as the experimental spectra
[^unzog:prb:2022-4].

## Dielectric function used in the SCH method\[<a
href="/wiki/index.php?title=Supercell_core-hole_theory&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Dielectric function used in the SCH method">edit</a> \| (./index.php.md)\]

Since the wavelength of the electromagnetic waves in absorption
spectroscopy is usually much larger than the characteristic momentum in
solids, we start from the transversal expression for the imaginary part
of the dielectric function in the long wavelength limit
($\mathbf{q}=0$) which is directly proportional to the
absorption spectrum

$\epsilon_{\alpha \beta}^{(2)} (\omega,\mathbf{q}=0) = \frac{4 \pi^{2}
e^{2} \hbar^{4}}{\Omega \omega^{2} m_{e}^{2}}
\sum\limits_{c,v,\mathbf{k}} 2w_{\mathbf{k}}
\delta(\varepsilon_{c\mathbf{k}}-\varepsilon_{v\mathbf{k}}-\omega)
\times M_{\alpha}^{v\rightarrow c} {M_{\beta}^{v\rightarrow c}}^{\*}$

where $M$ and
$\varepsilon$ denote momentum matrix elements and
orbital energies. Here we consider excitations only between valence
($v$) and conduction ($c$) bands.
The components of the dielectric tensor are indexed by the Cartesian
indices $\alpha$ and
$\beta$. $\Omega$,
$e$ and $m_{e}$
denote the unit cell volume, electron charge and mass of the electron,
respectively. In the PAW method the all-electron orbitals
$|\psi_{n\mathbf{k}}\rangle$ are given by a linear
transformation of the pseudo orbitals $|\tilde{\psi}_{n\mathbf{k}}\rangle$:

$|\psi_{n\mathbf{k}}\rangle = |\tilde{\psi}_{n\mathbf{k}}\rangle +
\sum\limits_{i} (|\phi_{i}\rangle - |\tilde{\phi}_{i}\rangle)
\langle \tilde{p}_{i} |\tilde{\psi}_{n\mathbf{k}}\rangle.$

The pseudo orbitals depend on the band index $n$ and
crystal momentum $\mathbf{k}$.
$|\phi_{i}\rangle$, $|\tilde{\phi}_{i}\rangle$ and $|\tilde{p}_{i}\rangle$ are all-electron partial waves, pseudo partial waves
and the projectors, respectively. The index $i$ is a
shorthand for the atomic site and other indices enumerating these
quantities at each site (such as angular and magnetic quantum numbers).
In the PAW formalism, the matrix elements are given by

$M_{\alpha}^{v\rightarrow c} = \langle \psi_{c \mathbf{k}} |i
\nabla_{\alpha} - \mathbf{k}_{\alpha}| \psi_{v\mathbf{k}} \rangle =
\langle \tilde{\psi}_{c\mathbf{k}}| i
\nabla_{\alpha}-\mathbf{k}_{\alpha}|\tilde{\psi}_{v\mathbf{k}}
\rangle + \sum\limits_{ij} \langle \tilde{\psi}_{c\mathbf{k}} |
\tilde{p}_{i} \rangle \langle \tilde{p}_{j} |
\tilde{\psi}_{v\mathbf{k}} \rangle i \left(\langle \phi_{i}|
\nabla_{\alpha}| \phi_{j} \rangle - \langle \tilde{\phi}_{i}|
\nabla_{\alpha}| \tilde{\phi}_{j} \rangle \right).$

where the one-center terms are calculated within the PAW sphere for each
atom.

Since in X-ray absorption spectroscopy, one only considers one core hole
at a single site, we can from now on restrict the equations to a single
site. The index $i$ then only
enumerates the main quantum number, the angular and the magnetic quantum
numbers. As usual in the PAW method, using the completeness relation,
$\sum_{i} |\tilde{p}_{i}\rangle \langle \tilde{\phi}_{i}| = 1$, the first and third term in the previous equation
cancel each other leading to the following simplified matrix elements
$M^{\mathrm{core}\rightarrow
c\mathbf{k}}_{\alpha}=\sum\limits_{i}\langle
\tilde{\psi}_{c\mathbf{k}} | \tilde{p}_{i} \rangle \langle\phi_{i}|
\nabla_{\alpha}| \phi_{\mathrm{core}}\rangle.$

Also the summation over bands can be limited to the conduction bands
$c$

$\epsilon_{\alpha \beta}^{(2)} (\omega) = \frac{4 \pi^{2} e^{2}
\hbar^{4}}{\Omega \omega^{2} m_{e}^{2}} \sum\limits_{c,\mathbf{k}}
2w_{\mathbf{k}}\delta(\varepsilon_{c\mathbf{k}}-\varepsilon_{\mathrm{core}}-\omega)
\times M^{\mathrm{core}\rightarrow c\mathbf{k}}_\alpha
{M^{\mathrm{core}\rightarrow c\mathbf{k}}_\beta}^\*.$

## References\[<a
href="/wiki/index.php?title=Supercell_core-hole_theory&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^karsai:prb:2018-1]: [F. Karsai, M. Humer, E. Flage-Larsen, P. Blaha, and G. Kresse, Phys. Rev. B **98**, 235205 (2018).](https://doi.org/10.1103/PhysRevB.98.235205)
[^hetenyi:jcp:2004-2]: [B. Hetényi, F. De Angelis, P. Giannozzi, and R. Car, *Calculation of near-edge x-ray-absorption fine structure at finite temperatures: spectral signatures of hydrogen bond breaking in liquid water* , J. Chem. Phys. **120**, 8632 (2004).](https://doi.org/10.1063/1.1703526)
[^Prendergasst:prl:2006-3]: [D. Prendergasst and G. Galli, *X-Ray Absorption Spectra of Water from First Principles Calculations*, Phys. Rev. Lett. **96**, 215502 (2006).](https://doi.org/10.1103/PhysRevLett.96.215502)
[^unzog:prb:2022-4]: [M. Unzog, A. Tal, G. Kresse, *X-ray absorption using the projector augmented-wave method and the Bethe-Salpeter equation*, Phys. Rev. B **106**, 155133 (2022).](http://doi.org/10.1103/PhysRevB.106.155133)
