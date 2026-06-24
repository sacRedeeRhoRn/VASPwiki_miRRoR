<!-- Source: https://vasp.at/wiki/index.php/LOPTICS | revid: 31076 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LOPTICS
LOPTICS = .TRUE. \| .FALSE.  
Default: **LOPTICS** = .FALSE. 

Description: LOPTICS=.TRUE. calculates the frequency dependent
dielectric matrix after the electronic ground state has been determined.

------------------------------------------------------------------------

The imaginary part is determined by a summation over empty states using
the equation:

$\epsilon^{(2)}_{\alpha \beta}\left(\omega\right)
= \frac{4\pi^2 e^2}{\Omega} \mathrm{lim}_{q \rightarrow 0}
\frac{1}{q^2} \sum_{c,v,\mathbf{k}} 2 w_\mathbf{k} \delta(
\epsilon_{c\mathbf{k}} - \epsilon_{v\mathbf{k}} - \omega) \times
\langle u_{c\mathbf{k}+\mathbf{e}_\alpha q} | u_{v\mathbf{k}}
\rangle \langle u_{v\mathbf{k}} | u_{c\mathbf{k}+\mathbf{e}_\beta q}
\rangle$

here the indices *c* and *v* refer to conduction and valence band states
respectively, and *u*_(*c***k**) is the cell periodic part of the
orbitals at the k-point **k**. The real part of the dielectric tensor
ε⁽¹⁾ is obtained by the usual Kramers-Kronig transformation

$\epsilon^{(1)}_{\alpha \beta} (\omega) = 1 +
\frac{2}{ \pi} P \int_0^{\infty} \frac{ \epsilon^{(2)}_{\alpha \beta}
(\omega') \omega'}{ \omega'^2- \omega^2 + i \eta } d \omega'$

where *P* denotes the principle value. The method is explained in detail
in the paper by Gajdoš *et al.* (see Eqs. 15, 29, and
30).^([\[1\]](#cite_note-gajdos:prb:06-1)) The complex shift η is
determined by the parameter [CSHIFT](CSHIFT.md).

Note that local field effects, i.e. changes of the cell periodic part of
the potential are neglected in this approximation. These can be
evaluated using either the implemented density functional perturbation
theory ([LEPSILON](LEPSILON.md)=.TRUE.), or the GW
routines.

The method selected using LOPTICS=.TRUE. requires an appreciable number
of empty conduction band states. Reasonable results are usually only
obtained, if the parameter [NBANDS](NBANDS.md) is roughly
doubled or tripled in the [INCAR](../input-files/INCAR.md) file with respect
to the VASP default. Furthermore it is emphasized that the routine works
properly even for [HF and screened exchange type calculations and hybrid
functionals](../methods/Category-Hybrid_functionals.md).
In this case, finite differences are used to determine the derivatives
of the Hamiltonian with respect to **k**.

Note that the number of frequency grid points is determined by the
parameter [NEDOS](NEDOS.md). In many cases it is desirable to
increase this parameter significantly from its default value. Values
around [NEDOS](NEDOS.md)=2000 are strongly recommended.

VASP posses multiple other routines to calculate the frequency dependent
dielectric function. Specifically, one can use [ALGO](ALGO.md)
= TDHF (Casida/[BSE
calculations](../redirects/BSE_calculations.md)),
[ALGO](ALGO.md) = GW ([GW
calculations](../redirects/GW_calculations.md)) and
[ALGO](ALGO.md) = TIMEEV ([Time
Evolution](../redirects/Time_Evolution.md): apply a delta kick
and follow the induced dipoles). Compared to LOPTICS=.TRUE., all those
routines have the advantage to include effects beyond the independent
particle approximation, however, they are usually also much more
expensive than LOPTICS=.TRUE.

### Spectral broadening
The dielectric function calculated with LOPTICS includes broadening due
to the smearing method [ISMEAR](ISMEAR.md) and the
Lorentzian broadening due to the complex shift in the Kramers-Kronig
transformation. For example, the combination of LOPTICS=.TRUE. and
[ISMEAR](ISMEAR.md)=0 produces the dielectric function
broadened by a Gaussian with the width [SIGMA](SIGMA.md) and
a Lorentzian with the width [CSHIFT](CSHIFT.md). To avoid
using two different broadening methods simultaneously and only include
the Lorentzian broadening, one should set [SIGMA](SIGMA.md)
to a much smaller value than [CSHIFT](CSHIFT.md).

Note, that the imaginary part of the dielectric function is also
broadened by the Lorentzian as long as [CSHIFT](CSHIFT.md)
is not too small, in which case a warning is printed. This means that
first a Gaussian broadening is added directly when the imaginary part of
the dielectric function is calculated, and successively afterwards a
Loretzian broadening is applied. Mind, that this especially affects the
life time, i.e. long tails of the transitions, and can influence the
dielectric function significantly and produce artifacts if the cut-off
frequency [OMEGAMAX](OMEGAMAX.md) is chosen close to a
large transition element.

|  |
|----|
| **Warning:** Note that LOPTICS = .TRUE. with [ISMEAR](ISMEAR.md) = -2 is currently not supported. |

|  |
|----|
| **Mind:** Furthermore the combination of LOPTICS = .TRUE. and [ISMEAR](ISMEAR.md) selecting the tetrahedron method is only supported as of VASP 6.3. |

## Related tags and articles
[CSHIFT](CSHIFT.md), [LNABLA](LNABLA.md),
[LEPSILON](LEPSILON.md), [Time
Evolution](../redirects/Time_Evolution.md),
[WPLASMAI](WPLASMAI.md)

See also: [Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LOPTICS-_incategory-Examples)

## References
1.  [↑](#cite_ref-gajdos:prb:06_1-0) [M. Gajdoš, K. Hummer, G.
    Kresse, J. Furthmüller, and F. Bechstedt, Phys. Rev. B 73, 045112
    (2006).](http://link.aps.org/doi/10.1103/PhysRevB.73.045112)

------------------------------------------------------------------------
