<!-- Source: https://vasp.at/wiki/index.php/Langevin_thermostat | revid: 32301 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Langevin thermostat
The Langevin
thermostat^([\[1\]](#cite_note-allen:book:1991-1)[\[2\]](#cite_note-hoover:prl:1982-2)[\[3\]](#cite_note-evans:jcp:1983-3))
maintains the temperature through a modification of Newton's equations
of motion

$\dot{r_i} = p_i/m_i \qquad \dot{p_i} = F_i -
{\gamma}_i\\p_i + f_i,$

where *F_(i)* is the force acting on atom *i* due to the interaction
potential, γ_(i) is a friction coefficient, and *f_(i)* is a random
force simulating the random kicks by the damping of particles between
each other due to friction. The random numbers are chosen from a
Gaussian distribution with the following variance

$\sigma_i^2 =
2\\m_i\{\gamma}_i\\k_B\\T/{\Delta}t$

with Δ*t* being the time-step used in the MD to integrate the equations
of motion. Obviously, Langevin dynamics is identical to the classical
Hamiltonian in the limit of vanishing γ.

- [NVT ensemble](../misc/NVT_ensemble.md):

The friction coefficient is set by the
[LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md) parameter.

- [NpT ensemble](../misc/NpT_ensemble.md):

As for the [NVT ensemble](../misc/NVT_ensemble.md) the
[LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md) parameter has to
be set. If the [NpT ensemble](../misc/NpT_ensemble.md) is used
(by setting [ISIF](../incar-tags/ISIF.md)=3) additionally the friction
coefficient of the lattice
[LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md) has to be
provided too.

The Langevin thermostat is selected by MDALGO=3.

## Related tags and articles
[Molecular-dynamics
calculations](../redirects/Molecular_dynamics_calculations.md),
[Andersen thermostat](Andersen_thermostat.md),
[Nosé-Hoover
thermostat](Nosé-Hoover_thermostat.md),
[CSVR thermostat](../theory/CSVR_thermostat.md), [Nosé-Hoover
chain
thermostat](../misc/Nosé-Hoover_chain_thermostat.md),
[ISIF](../incar-tags/ISIF.md), [MDALGO](../incar-tags/MDALGO.md),
[LANGEVIN_GAMMA](../incar-tags/LANGEVIN_GAMMA.md),
[LANGEVIN_GAMMA_L](../incar-tags/LANGEVIN_GAMMA_L.md)

## References
1.  [↑](#cite_ref-allen:book:1991_1-0) [M. P. Allen and D. J. Tildesley,
    *Computer simulation of liquids* (Oxford university press: New York,
    1991).](https://books.google.co.jp/books?id=WFExDwAAQBAJ&lpg=PP1&hl=ja&pg=PP1#v=onepage&q&f=false)
2.  [↑](#cite_ref-hoover:prl:1982_2-0) [W. G. Hoover, A. J. C. Ladd,
    and B. Moran, Phys. Rev. Lett. **48**, 1818
    (1982).](https://doi.org/10.1103/PhysRevLett.48.1818)
3.  [↑](#cite_ref-evans:jcp:1983_3-0) [D. J. Evans, J. Chem. Phys.
    **78**, 3297 (1983).](https://doi.org/10.1063/1.445195)

  

------------------------------------------------------------------------
