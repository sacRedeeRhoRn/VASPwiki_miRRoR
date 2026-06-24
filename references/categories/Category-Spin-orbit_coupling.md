<!-- Source: https://vasp.at/wiki/index.php/Category:Spin-orbit_coupling | revid: 37098 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Spin-orbit coupling
**Spin-orbit coupling** (SOC) is the relativistic interaction between
the spin of an electron and its orbital motion. It is one of the
**relativistic corrections** that become important for systems
containing heavy elements, where it lifts spin degeneracies, splits
energy bands, and couples the magnetic moments to the crystal lattice.
Capturing this interaction is essential for properties such as magnetic
anisotropy, orbital magnetic moments, the Rashba and Dresselhaus
effects, and the spin texture of electronic states. In VASP, spin-orbit
coupling is treated within the noncollinear framework, so that the
wavefunction is described by two-component spinors rather than scalar
orbitals.

## Contents

- [1 Enabling spin-orbit coupling](#Enabling_spin-orbit_coupling)
- [2 When to include spin-orbit
  coupling](#When_to_include_spin-orbit_coupling)
- [3 Magnetic anisotropy energy](#Magnetic_anisotropy_energy)
- [4 Band structure and spin texture](#Band_structure_and_spin_texture)
- [5 Tutorials](#Tutorials)

## Enabling spin-orbit coupling
Spin-orbit coupling is switched on with a single tag
([LSORBIT](../incar-tags/LSORBIT.md)), which automatically activates the
[noncollinear
framework](Category-Noncollinear_magnetism.md)
([LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)). It is
implemented for the projector-augmented-wave (PAW) method only and must
be run with the noncollinear VASP executable `vasp_ncl`. Because the
calculation now uses two-component spinors, the magnetic configuration
is specified by three components per atom
([MAGMOM](../incar-tags/MAGMOM.md)).

## When to include spin-orbit coupling
Even when you are not after a property that intrinsically requires
spin-orbit coupling, it can still change your results. For heavy
elements the effect on total energies, equilibrium geometries, and band
energies may be far from negligible. Rather than assuming the
interaction can be ignored, test its influence explicitly: run the
property of interest once without and once with spin-orbit coupling and
compare. If the difference is within your target accuracy, you may
safely neglect it for that system; if not, keep it switched on. As a
rule of thumb, the heavier the elements in your structure, the more
likely spin-orbit coupling matters, since the SOC constant \$\propto
Z^4\$.

## Magnetic anisotropy energy
With spin-orbit coupling the energy is no longer invariant under a
global rotation of the spins, so it depends on the orientation of the
spins relative to the crystal axes. The total-energy differences between
calculations with different spin-quantization axes
([SAXIS](../incar-tags/SAXIS.md)) is called magnetic anisotropy energy. In
these calculations, the orbital magnetic moments may become nonzero and
can be written to the output ([LORBMOM](../incar-tags/LORBMOM.md)). For
the details, see [Noncollinear
magnetism](Category-Noncollinear_magnetism.md).

## Band structure and spin texture
Spin-orbit coupling splits bands that would otherwise be degenerate and
gives each Bloch state a spin expectation value that varies across the
Brillouin zone, the spin texture seen in Rashba and topological systems.
After a [self-consistent
calculation](../tutorials/Setting_up_an_electronic_minimization.md)
with spin-orbit coupling, the spin-resolved band structure is obtained
from a non-self-consistent run along a **k**-point path, and the site-
and orbital-projected spin components are written with the projection
tag ([LORBIT](../incar-tags/LORBIT.md)). A step-by-step workflow for
computing and visualizing the spin texture is given in the how-to
[Computing the spin
texture](../tutorials/Computing_the_spin_texture.md).

## Tutorials
- [Spin-orbit coupling for bcc Fe
  bulk.](https://www.vasp.at/tutorials/latest/magnetism/part2/#mag-e06)
