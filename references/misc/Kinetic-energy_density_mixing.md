<!-- Source: https://vasp.at/wiki/index.php/Kinetic-energy_density_mixing | revid: 8126 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Kinetic-energy density mixing


For the density mixing schemes to work reliably, the charge density
mixer must be aware of all quantities that affect the total energy
during the self-consistency cycle. For a standard DFT functional, this
is solely the charge density. In case of meta-GGAs, however, the total
energy depends on the kinetic energy density as well.

In many cases the density mixing scheme works well enough without
passing the kinetic energy density through the mixer, which is why
[LMIXTAU](../incar-tags/LMIXTAU.md)=.FALSE., per default. However, when
the selfconsistency cycle fails to converge for one of the
density-mixing algorithms (for instance, [IALGO](../incar-tags/IALGO.md)=38
or 48), one may set [LMIXTAU](../incar-tags/LMIXTAU.md)=.TRUE. to have
VASP pass the kinetic energy density through the mixer as well. This
sometimes helps to cure convergence problems in the selfconsistency
cycle.


