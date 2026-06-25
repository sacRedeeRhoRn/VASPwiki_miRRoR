<!-- Source: https://vasp.at/wiki/index.php/CSVR_thermostat | revid: 32310 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CSVR thermostat


One popular strategy to control the temperature in NVT MD is based on
rescaling atomic velocities ($\mathbf{v}_{i}$) at a certain predefined frequency by a factor
$\alpha = \sqrt{\bar{K}/K}$ in such a way that the total
kinetic energy of the system

$K=
\frac{1}{2} \sum\limits_{i=1}^{N} m_i |\mathbf{v}_{i}|^2,$

is equal to the average kinetic energy corresponding to a given
temperature:

$\bar{K} = \frac{1}{2}N_f k_B T$

where $N_f$ is the
number of degrees of freedom (e.g., $N_f = 3N -3$
in the case of 3D periodic systems) and $N$ is the
number of atoms per the simulation cell. Such a method, however, suffers
from several problems. First, the ensemble generated is not strictly
canonical. Second, rescaling velocities creates discontinuities in
trajectories. As a consequence, the method has no conserved quantity
that could be used to guide the choice of simulation parameters, such as
the size of the integration step. Also, the rescaling introduces
artificial fast fluctuations to velocities, making the evaluation of
time correlations problematic. Finally, the trajectories generated via a
naïve rescaling method often suffer from ergodicity issues, such as the
flying ice-cube problem, in which kinetic energy of a part of the
vibrational degrees of freedom is transferred into translations and/or
rotations, violating the equipartition principle.

The canonical sampling through velocity rescaling (CSVR) proposed by
Bussi et
al.<sup>[\[1\]](#cite_note-:0-1)</sup>
removes most of the difficulties of the naïve rescaling approach. Here,
the term $\bar{K}$ is
replaced by $K_{t}$
obtained for each time step by propagating in time via auxiliary
dynamics

$dK
= (\bar{K} - K) \frac{dt}{\tau} + 2\sqrt{\frac{K\bar{K}}{N_f}}
\frac{dW}{\sqrt{\tau}}$

where $dW$ is a
Wiener noise and $\tau$
determines the characteristic time scale of the CSVR thermostat. The
latter is the only parameter of this thermostat and can be defined via
flag [CSVR_PERIOD](../misc/CSVR_PERIOD.md). Importantly, the
auxiliary dynamics generates canonical distribution for kinetic energy:

$P(K_t) dK_t \propto K_t^{(N_f/2 - 1)} e^{-K_t/k_B T} dK_t$

The conserved quantity of the CSVR thermostat is the effective energy
$\tilde{H}$ defined as:

$\tilde{H}(t) = H(t) - \int_0^{t'} (\bar{K}-K)\frac{dt'}{\tau} -
2\int_0^{t} \sqrt{\frac{K{t'}\bar{K}}{N_f}} \frac{dW(t')}{\sqrt{\tau}}$

As shown by Bussi et
al.<sup>[\[1\]](#cite_note-:0-1)</sup>,
the CSVR thermostat does not significantly affect the evaluation of
dynamical properties, such as the velocity autocorrelation functions or
diffusion coefficients.

## Related tags and articles\[<a
href="/wiki/index.php?title=CSVR_thermostat&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">Molecular-dynamics
calculations</a>, [Andersen
thermostat](../tutorials/Andersen_thermostat.md),
[Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md),
[Langevin thermostat](../tutorials/Langevin_thermostat.md),
[Nosé-Hoover chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md),
[ISIF](../incar-tags/ISIF.md), [MDALGO](../incar-tags/MDALGO.md),
[CSVR_PERIOD](../misc/CSVR_PERIOD.md)

------------------------------------------------------------------------

## References\[<a
href="/wiki/index.php?title=CSVR_thermostat&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑ <sup>[a](#cite_ref-:0_1-0)</sup>
    <sup>[b](#cite_ref-:0_1-1)</sup> <a
    href="https://pubs.aip.org/aip/jcp/article-abstract/126/1/014101/186581/Canonical-sampling-through-velocity-rescaling?redirected"
    class="external text" rel="nofollow">G. Bussi, D. Donadio, and M.
    Parrinello, <em>J. Chem. Phys.</em> 126, 014101 (2007)</a>


