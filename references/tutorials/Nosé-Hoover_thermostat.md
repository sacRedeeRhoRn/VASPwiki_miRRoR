<!-- Source: https://vasp.at/wiki/index.php/Nos%C3%A9-Hoover_thermostat | revid: 32315 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Nosé-Hoover thermostat


In the approach by Nosé and
Hoover[^nose:jcp:1984-1][^nose:ptp:1991-2][^hoover:pra:1985-3][^frenkel:book:1996-4],
an extra degree of freedom is introduced in the Hamiltonian. The heat
bath is considered as an integral part of the system and has a fictious
coordinate $s$ which is
introduced into the Lagrangian of the system. This Lagrangian for a
$N$ particle system is written as

$\mathcal{L} = \sum\limits_{i=1}^{N} \frac{m_{i}}{2} s^{2}
\dot{\mathbf{r}}_{i}^{2} - U(\mathbf{r}) + \frac{Q}{2} \dot{s}^{2}-g
k_{B} T \mathrm{ln} \\ s$

where $m_{i}$ and
$k_{B}$ are the mass of ion $i$ and the
Boltzmann constant, respectively. The first two terms are the kinetic
and potential energy of the system. The third and fourth term represent
the kinetic and potential energy of the fictitious coordinate
$s$. These terms also ensure the energy conservation of
the Nosé-Hoover thermostat. The parameter $g$ is usually
equal to the number of degrees of freedom of the system
$g=3N - N_{\mathrm{constraint}}$, where
$N_{\mathrm{constraint}}$ is equal to the number of
constraint set (fixed coordinates in the [POSCAR](../input-files/POSCAR.md)
file). The parameter $Q$ is an
effective "mass" of $s$, which
controls the coupling of the system to the heat bath. It is set by the
[INCAR](../input-files/INCAR.md) tag [SMASS](../incar-tags/SMASS.md).

The Nosé-Hoover thermostat is selected by
[MDALGO](../incar-tags/MDALGO.md)=2.

  

## Related tags and articles\[<a
href="/wiki/index.php?title=Nos%C3%A9-Hoover_thermostat&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">Molecular-dynamics
calculations</a>, [Andersen
thermostat](Andersen_thermostat.md), [Langevin
thermostat](Langevin_thermostat.md), [CSVR
thermostat](../theory/CSVR_thermostat.md), [Nosé-Hoover chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md),
[ISIF](../incar-tags/ISIF.md), [MDALGO](../incar-tags/MDALGO.md),
[SMASS](../incar-tags/SMASS.md)

## References\[<a
href="/wiki/index.php?title=Nos%C3%A9-Hoover_thermostat&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^nose:jcp:1984-1]: [S. Nosé, J. Chem. Phys. **81**, 511 (1984).](https://doi.org/10.1063/1.447334)
[^nose:ptp:1991-2]: [S. Nosé, Prog. Theor. Phys. Suppl. **103**, 1 (1991).](https://doi.org/10.1143/PTPS.103.1)
[^hoover:pra:1985-3]: [W. G. Hoover, Phys. Rev. A **31**, 1695 (1985).](https://doi.org/10.1103/PhysRevA.31.1695)
[^frenkel:book:1996-4]: [D. Frenkel and B. Smit, Understanding Molecular Simulation (Academic Press, London, 1996).](https://doi.org/10.1016/B978-0-12-267351-1.X5000-7)
