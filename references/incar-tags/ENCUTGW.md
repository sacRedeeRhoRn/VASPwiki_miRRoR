<!-- Source: https://vasp.at/wiki/index.php/ENCUTGW | revid: 20307 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ENCUTGW


ENCUTGW = \[real\]  
Default: **ENCUTGW** = 2/3 [ENCUT](ENCUT.md) 

  
Description: The tag ENCUTGW
sets the energy cutoff for the response function. It controls the basis
set for the response functions in exactly the same manner as
[ENCUT](ENCUT.md) does for the orbitals.

  


## Contents


- [1 FFT grid and
  PRECFOCK](#fft-grid-and-precfock)
- [2 Related tags
  and articles](#related-tags-and-articles)
- [3 Further
  reading](#further-reading)
- [4
  References](#references)


------------------------------------------------------------------------

In GW and random-phase-approximation (RPA) calculations, storing and
manipulating the response function dominates the computational work
load:

$\chi_{{\mathbf{q}}}^0 ({\mathbf{G}}, {\mathbf{G}}',
\omega)=\frac{1}{\Omega} \sum_{n,n',{\mathbf{k}}}2 w_{{\mathbf{k}}}
(f_{n'{\mathbf{k}}+{\mathbf{q}}} - f_{n{\mathbf{k}}}) \times
\frac{\langle \psi_{n{\mathbf{k}}}| e^{-i
({\mathbf{q}}+{\mathbf{G}}){\mathbf{r}}} |
\psi_{n'{\mathbf{k}}+{\mathbf{q}}}\rangle \langle
\psi_{n'{\mathbf{k}}+{\mathbf{q}}}| e^{i
({\mathbf{q}}+{\mathbf{G}}'){\mathbf{r'}}} |
\psi_{n{\mathbf{k}}}\rangle} {
\epsilon_{n'{\mathbf{k}}+{\mathbf{q}}}-\epsilon_{n{\mathbf{k}}} -
\omega - i \eta }.$

ENCUTGW controls how many
$\mathbf{G}$ vectors are included in the the response
function $\chi_{{\mathbf{q}}}^0
({\mathbf{G}}, {\mathbf{G}}', \omega)$.

Our experience suggests that choosing
ENCUTGW= 2/3
[ENCUT](ENCUT.md) yields reasonable results at fairly modest
computational cost, although, the response function contains
contributions up to twice the plane wave cutoff
$G_{\rm cut}$, see [ALGO](ALGO.md) tag.
Furthermore, RPA correlation energies are reported using an internal
extrapolation of the correlation energy by varying the value of
ENCUTGW inside VASP between
the largest value given in the [INCAR](../input-files/INCAR.md) file and
smaller values
[^harl:prb:08-1].
Mind: The extrapolated value is only reliable, if
ENCUTGW is smaller then
[ENCUT](ENCUT.md). The cutoff extrapolation with respect to
ENCUTGW would be precise if
the plane wave basis for the orbitals were infinite. Again, the VASP
defaults yield very reasonable values for the extrapolated correlation
energy. In fact, it is unwise to increase
ENCUTGW only, without
increasing [ENCUT](ENCUT.md). To converge RPA correlation
energies, simply increase [ENCUT](ENCUT.md) and the number of
orbitals, and use the VASP default for
ENCUTGW.

|  |
|----|
| **Mind:** More details on how the infinite basis set limit is extrapolated in RPA/ACFDT can be found [here](../methods/ACFDT__RPA_calculations.md). |

For quasiparticle (QP) bandgaps, it is sometimes possible to set
ENCUTGW to values between 150
to 200 eV, and even 100 eV can yield gaps that are accurate to within a
few tens of an eV for main group elements. Be aware, however, that the
absolute values of the QP energies depend inverse proportionally on the
number of plane waves. Thus, the convergence of absolute QP energies is
very slow, although QP gaps might seem converged.

The recommended procedure to obtain accurate QP energies is discussed in
the reference below. Specifically, for reference type calculations we
recommend the following procedure:

- Use the default for ENCUTGW,
  or even decrease ENCUTGW to
  half the value of [ENCUT](ENCUT.md).
- Calculate all orbitals that the plane-wave basis set allows to
  calculate. This number can be determined by searching for "maximum
  number of plane-waves" in the ground-state DFT
  [OUTCAR](../output-files/OUTCAR.md) file, and setting
  [NBANDS](NBANDS.md) to this value.
- Increase [ENCUT](ENCUT.md) systematically and plot the QP
  energies versus the number of plane-wave coefficients, which equals
  the number of orbitals. This means
  ENCUTGW and
  [NBANDS](NBANDS.md) increase as
  [ENCUT](ENCUT.md) increases.

This procedure can be carried out using few k points. Other commonly
applied methods can yield less accurate results and are not considered
to be reliable.

## FFT grid and [PRECFOCK](PRECFOCK.md)\[<a href="/wiki/index.php?title=ENCUTGW&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: FFT grid and PRECFOCK">edit</a> \| (./index.php.md)\]

The [PRECFOCK](PRECFOCK.md) tag determines the fast
Fourier transformation (FFT) grid in all GW (and Hartree-Fock) related
routines. For small systems, the computational time is often dominated
by FFT operations. Therefore, the [PRECFOCK](PRECFOCK.md)
tag can have a significant impact on the compute time for QP
calculations. For large systems, the FFT's usually do not dominate the
computational workload, and savings are expected to be small for
[PRECFOCK](PRECFOCK.md) = *fast*. QP shifts are usually
not very sensitive to the setting of
[PRECFOCK](PRECFOCK.md) and therefore there is no harm in
setting [PRECFOCK](PRECFOCK.md) = *fast*), whereas for RPA
calculations we recommend to set [PRECFOCK](PRECFOCK.md) =
*normal* to avoid numerical errors.

## Related tags and articles\[<a href="/wiki/index.php?title=ENCUTGW&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[PRECFOCK](PRECFOCK.md), [ENCUT](ENCUT.md),
[ENCUTGWSOFT](ENCUTGWSOFT.md),
<a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW calculations</a>, [Basis set
convergence](../methods/ACFDT__RPA_calculations.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ENCUTGW-_incategory-Examples)

## Further reading\[<a href="/wiki/index.php?title=ENCUTGW&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Further reading">edit</a> \| (./index.php.md)\]

- Generally, QP energies converge like one over the number of orbitals
  and one over the number of plane waves in the response function. For
  basis set converged calculations, we recommend using the strategies
  outlined in Ref.
  [^klimes:prb:14-2],
  which contains a comprehensive study of the performance of the
  convergence of GW calculations.

## References\[<a href="/wiki/index.php?title=ENCUTGW&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

[^harl:prb:08-1]: [J. Harl and G. Kresse, Phys. Rev. B **77**, 045136 (2008).](https://doi.org/10.1103/PhysRevB.77.045136)
[^klimes:prb:14-2]: [J. Klimeš, M. Kaltak, and G. Kresse, Phys. Rev. B **90**, 075125 (2014).](https://doi.org/10.1103/PhysRevB.90.075125)
