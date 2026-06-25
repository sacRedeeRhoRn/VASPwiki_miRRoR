<!-- Source: https://vasp.at/wiki/index.php/LFXC | revid: 37075 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LFXC


LFXC = .TRUE. \| .FALSE.  
Default: **LFXC** = .FALSE. 

Description: LFXC enables the
(semi-)local exchange-correlation kernel in
[Casida](../methods/Time-dependent_density-functional_theory_calculations.md)
and
[time-evolution](../tutorials/Time-evolution_algorithm.md)
TDDFT calculations.

------------------------------------------------------------------------

In linear-response TDDFT, the density-density response function
$\chi$ obeys the Dyson equation

$\chi(\mathbf r, \mathbf r'; \omega) = \chi_\mathrm{KS}(\mathbf r,
\mathbf r'; \omega) + \int \mathrm d\mathbf r_1 \mathrm d\mathbf r_2 \\
\chi_\mathrm{KS}(\mathbf r, \mathbf r_1; \omega) \left\[ v(\mathbf r_1,
\mathbf r_2) + f_\mathrm{xc}(\mathbf r_1, \mathbf r_2; \omega) \right\]
\chi(\mathbf r_2, \mathbf r'; \omega),$

where $\chi_\mathrm{KS}$ is the non-interacting Kohn-Sham response function,
$v$ is the bare Coulomb interaction, and
$f_\mathrm{xc}$ is the exchange-correlation kernel.
VASP uses the adiabatic approximation, $f_\mathrm{xc}(\mathbf r,
\mathbf r'; \omega) \approx f_\mathrm{xc}(\mathbf r, \mathbf r')$.

Setting LFXC=.TRUE. includes
the (semi-)local part of $f_\mathrm{xc}$ in both the Casida eigenvalue problem
([ALGO](ALGO.md)=TDHF) and the time-evolution TDDFT (or
real-time TDDFT) ([ALGO](ALGO.md)=TIMEEV).


## Contents


- [1 (Semi-)local
  exchange-correlation
  kernel](#(Semi-)local_exchange-correlation_kernel)
  - [1.1 Casida
    TDDFT](#Casida_TDDFT)
  - [1.2
    Time-evolution TDDFT (Real-time
    TDDFT)](#Time-evolution_TDDFT_(Real-time_TDDFT))
- [2 Hybrid
  functionals](#Hybrid_functionals)
- [3 Compare Casida
  and time-evolution TDDFT
  results](#Compare_Casida_and_time-evolution_TDDFT_results)
- [4 Related tags
  and articles](#Related_tags_and_articles)
- [5
  References](#References)


## (Semi-)local exchange-correlation kernel\[<a href="/wiki/index.php?title=LFXC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: (Semi-)local exchange-correlation kernel">edit</a> \| (./index.php.md)local exchange-correlation kernel")\]

The exchange-correlation kernel is computed very differently in the
Casida and time-evolution TDDFT approaches. It is defined as the second
functional derivative of the exchange-correlation energy density with
respect to the charge density,

$f_\mathrm{xc}(\mathbf r, \mathbf r') = \frac{\partial^2
\varepsilon_\mathrm{xc}}{\partial n(\mathbf r) \\ \partial n(\mathbf
r')}\delta(\mathbf r - \mathbf r').$

The Casida approach requires the derivative to be evaluated explicitly
and therefore implemented for each functional. The time-evolution TDDFT
does not require an explicit kernel: its contribution is included
implicitly through the propagation of the charge density and the
exchange-correlation potential.

### Casida TDDFT\[<a href="/wiki/index.php?title=LFXC&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Casida TDDFT">edit</a> \| (./index.php.md)\]

For an
[LDA](../categories/Category-Exchange-correlation_functionals.md)
functional,

$f_\mathrm{xc}^\mathrm{LDA}(\mathbf r, \mathbf r') = \frac{\partial^2
\varepsilon_\mathrm{xc}}{\partial n^2} \\ \delta(\mathbf r - \mathbf
r').$

For a
[GGA](../categories/Category-Exchange-correlation_functionals.md)
functional, gradient terms appear,

$f_\mathrm{xc}^\mathrm{GGA}(\mathbf r, \mathbf r') = \frac{\partial^2
\varepsilon_\mathrm{xc}}{\partial n^2}(\mathbf r) \\ \delta(\mathbf r -
\mathbf r') - \left\[\nabla \frac{\partial^2
\varepsilon_\mathrm{xc}}{\partial n \\ \partial \nabla n}(\mathbf
r)\right\] \delta(\mathbf r - \mathbf r') - \nabla_i \frac{\partial^2
\varepsilon_\mathrm{xc}}{\partial \nabla_i n \\ \partial \nabla_j
n}(\mathbf r) \\ \nabla_j \delta(\mathbf r - \mathbf r'),$

where $i, j$ are
summed Cartesian indices. In the Casida approach these gradient terms
are dropped and only the density derivatives are kept.
[Meta-GGA](../categories/Category-Exchange-correlation_functionals.md)
kernels are not supported.

### Time-evolution TDDFT (Real-time TDDFT)\[<a href="/wiki/index.php?title=LFXC&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Time-evolution TDDFT (Real-time TDDFT)">edit</a> \| (./index.php.md)")\]

The real-time propagation applies $f_\mathrm{xc}$ directly to the time-dependent density, so
[LDA](../categories/Category-Exchange-correlation_functionals.md)
and
[GGA](../categories/Category-Exchange-correlation_functionals.md)
kernels are used in full, including the gradient terms.

For
[meta-GGA](../categories/Category-Exchange-correlation_functionals.md)
functionals, the dependence of $\varepsilon_\mathrm{xc}$ on the kinetic-energy density
$\tau(\mathbf r)$ makes $\delta v_\mathrm{xc}/\delta n$ non-local through the orbital dependence of
$\tau$<sup>[\[1\]](#cite_note-nazarov:vignale:2011-1)</sup>.
These non-local contributions are not implemented in VASP, so the
$1/q^2$ long-range component of
$f_\mathrm{xc}$ responsible for excitonic effects is
missing.

## Hybrid functionals\[<a href="/wiki/index.php?title=LFXC&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Hybrid functionals">edit</a> \| (./index.php.md)\]

For a [hybrid
functional](../categories/Category-Exchange-correlation_functionals.md),
a fraction $c_\mathrm{x}$ of the (semi-)local exchange is replaced by exact
(Fock) exchange in both
solvers<sup>[\[2\]](#cite_note-sander:prb:15-2)</sup>,

$f_\mathrm{xc}(\mathbf r, \mathbf r') = \left(1-c_\mathrm{x}\right)
\frac{\partial^2 \varepsilon_\mathrm{x}}{\partial n(\mathbf r) \\
\partial n(\mathbf r')} + \frac{\partial^2
\varepsilon_\mathrm{c}}{\partial n(\mathbf r) \\ \partial n(\mathbf
r')} + c_\mathrm{x} \frac{\partial^2
\varepsilon_\mathrm{x}^\mathrm{Exact}}{\partial^2 n(\mathbf r, \mathbf
r')},$

where $c_\mathrm{x}$ is set by [AEXX](AEXX.md) and
$n(\mathbf r, \mathbf r')$ is the one-particle density
matrix. LFXC=.TRUE. enables
the first two terms only; the Fock contribution is enabled separately by
[LADDER](LADDER.md)=.TRUE..

## Compare Casida and time-evolution TDDFT results\[<a href="/wiki/index.php?title=LFXC&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Compare Casida and time-evolution TDDFT results">edit</a> \| (./index.php.md)\]

The Casida and time-evolution approaches produce very similar results
for LDA exchange-correlation. Small differences typically remain because
one-center terms in the PAW method are treated differently in the two
approaches. To bring the Casida results into closer agreement, increase
[ENCUTGW](ENCUTGW.md) beyond its default value and set
[ANTIRES](ANTIRES.md)=2 in the Casida TDDFT calculation.

## Related tags and articles\[<a href="/wiki/index.php?title=LFXC&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

Tags  
[LADDER](LADDER.md), [LHARTREE](LHARTREE.md),
[AEXX](AEXX.md), [ENCUTGW](ENCUTGW.md)

Articles  
[Time-dependent density-functional theory
calculations](../methods/Time-dependent_density-functional_theory_calculations.md),
[Time-evolution
algorithm](../tutorials/Time-evolution_algorithm.md)

[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LFXC-_incategory-Howto)

## References\[<a href="/wiki/index.php?title=LFXC&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-nazarov:vignale:2011_1-0)
    <a href="https://doi.org/10.1103/PhysRevLett.107.216402"
    class="external text" rel="nofollow">V. U. Nazarov, G. Vignale,
    <em>Optics of semiconductors from
    meta-generalized-gradient-approximation-based time-dependent
    density-functional theory</em>, Phys. Rev. Lett. <strong>107</strong>,
    216402 (2011).</a>
2.  [↑](#cite_ref-sander:prb:15_2-0)
    <a href="https://doi.org/10.1103/PhysRevB.92.045209"
    class="external text" rel="nofollow">T. Sander, E. Maggio, and G.
    Kresse, <em>Beyond the Tamm-Dancoff approximation for extended systems
    using exact diagonalization</em>, Phys. Rev. B <strong>92</strong>,
    045209 (2015).</a>


