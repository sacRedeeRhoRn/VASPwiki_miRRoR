<!-- Source: https://vasp.at/wiki/index.php/Nos%C3%A9-Hoover_chain_thermostat | revid: 33054 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Nosé-Hoover chain thermostat


The [standard Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md)
suffers from well-known issues, such as the ergodicity violation in the
case of simple harmonic
oscillator<sup>[\[1\]](#cite_note-martyna:jcp:92-1)</sup>.
As proposed by Martyna and
Klein<sup>[\[1\]](#cite_note-martyna:jcp:92-1)</sup>,
these problems can be solved by using multiple Nosé-Hoover thermostats
connected in a chain. Although the underlining dynamics is
non-Hamiltonian, the corresponding equations of motion conserve the
following energy term:

$\mathcal{H'} = \mathcal{H}(\mathbf{r},\mathbf{p}) +
\sum\limits_{j=1}^{M} \frac{p_{\eta_j}^2}{2Q_j} + (3N-N_c)k_{B} T
\eta_1 + k_{B} T \sum\limits_{j=2}^{M} \eta_j,$

where $\mathcal{H}(\mathbf{r},\mathbf{p})$ is the Hamiltonian
of the physical system, $M$,
$N$ and $N_c$ are the
numbers of thermostats, atoms in the cell, and geometric constraints,
respectively, and $\eta_{j}$,
$p_{\eta_j}$, and $Q_{j}$ are
the position, momentum, and mass-like parameter associated with the
thermostat $j$. Just like
the total energy in the NVE ensemble,$\mathcal{H'}$
is valuable for diagnostics purposes. Indeed, a significant drift in
$\mathcal{H'}$ indicates that the corresponding
computational setting is suboptimal. Typical reasons for this behavior
involve noisy forces (e.g., because of a poor SCF convergence) and/or a
too large integration step (defined via [POTIM](../incar-tags/POTIM.md)).

The number of thermostats is controlled by the flag
[NHC_NCHAINS](../incar-tags/NHC_NCHAINS.md). Typically, this flag is
set to a value between 1 and 5, the maximal allowed value is 20. In the
special case of [NHC_NCHAINS](../incar-tags/NHC_NCHAINS.md)=0, the
thermostat is switched off, leading to a MD in the microcanonical
ensemble. Another special case of
[NHC_NCHAINS](../incar-tags/NHC_NCHAINS.md)=1 corresponds to the
standard [Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md).

The only parameter of this thermostat is the characteristic time scale
($\tau$), defined via flag
[NHC_PERIOD](NHC_PERIOD.md). This parameter is used to
setup the mass-like variables via the relations:

$Q_1 = 3 (N -N_c)k_{B} T \tau^2$

$Q_j = k_{B} T \tau^2; \\ \\ \\ j=2,\dots,M$

Furthermore, due to rapidly varying forces in thermostat variables
propagators, the standard velocity Verlet algorithm with fixed
integration step might be insufficiently accurate. As proposed by
Tuckerman<sup>[\[2\]](#cite_note-2)</sup>,
the
RESPA<sup>[\[3\]](#cite_note-3)</sup>
methodology can be used to overcome this problem, in which the
integration step used in thermostat variables propagation is split into
[NHC_NRESPA](../incar-tags/NHC_NRESPA.md) equal parts, each of which
may be further divided into [NHC_NS](../incar-tags/NHC_NS.md) smaller
parts treated by Suzuki-Yoshida scheme of fourth or sixth order.

## Related tags and articles\[<a
href="/wiki/index.php?title=Nos%C3%A9-Hoover_chain_thermostat&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">Molecular-dynamics
calculations</a>, [Andersen
thermostat](../tutorials/Andersen_thermostat.md),
[Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md),
[Langevin thermostat](../tutorials/Langevin_thermostat.md),
[CSVR thermostat](../theory/CSVR_thermostat.md),
[ISIF](../incar-tags/ISIF.md),
[MDALGO](../incar-tags/MDALGO.md),[NHC_NCHAINS](../incar-tags/NHC_NCHAINS.md),[NHC_PERIOD](NHC_PERIOD.md),[NHC_NRESPA](../incar-tags/NHC_NRESPA.md),[NHC_NS](../incar-tags/NHC_NS.md)

## References\[<a
href="/wiki/index.php?title=Nos%C3%A9-Hoover_chain_thermostat&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-martyna:jcp:92_1-0)</sup>
    <sup>[b](#cite_ref-martyna:jcp:92_1-1)</sup>
    <a href="https://doi.org/10.1063/1.463940" class="external text"
    rel="nofollow">J. Martyna, M. L. Klein, and M. Tuckerman, J. Chem. Phys.
    <strong>97</strong>, 2635 (1992).</a>
2.  [↑](#cite_ref-2)
    M. E. Tuckerman, Statistical mechanics:
    theory and molecular simulation, Oxford University Press Inc., New
    York, 2010; pp 194-199.
3.  [↑](#cite_ref-3)
    <a
    href="https://pubs.aip.org/aip/jcp/article/97/3/1990/221848/Reversible-multiple-time-scale-molecular"
    class="external text" rel="nofollow">M. Tuckerman, B. J. Berne, and G.
    J. Martyna, J. Chem. Phys. 97, 1900 (1992)</a>


