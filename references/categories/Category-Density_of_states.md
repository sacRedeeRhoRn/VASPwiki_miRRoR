<!-- Source: https://vasp.at/wiki/index.php/Category:Density_of_states | revid: 36281 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Density of states
[![](https://vasp.at/wiki/images/thumb/e/e2/Si.png/400px-Si.png)](https://vasp.at/wiki/File:Si.png)

Density of states for silicon in the diamond structure.

[![](https://vasp.at/wiki/images/thumb/a/aa/NiO.png/400px-NiO.png)](https://vasp.at/wiki/File:NiO.png)

Density of states of spin-polarized nickel(II) oxide.

The electronic density of states (DOS) describes how many electronic
states are available at a given energy. It is a useful tool for
analyzing the electronic structure of materials, identifying band gaps,
and distinguishing between metallic and insulating behavior. The DOS can
also reveal the contribution of different atoms and orbitals to the
electronic states.

In VASP, the density of states is typically calculated after a
self-consistent calculation using a dense k-point mesh. The DOS is
written to the DOSCAR file, while projected contributions from atoms and
orbitals can be obtained using tags such as
[LORBIT](../incar-tags/LORBIT.md). After obtaining a converged charge
density, a non-self-consistent DOS calculation using a denser k-point
mesh is often recommended for smoother and more accurate DOS curves.

For non-spin-polarized systems, the DOS is identical for both spin
channels. Silicon in the diamond structure is a typical example of a
nonmagnetic semiconductor, where the DOS shows a band gap between the
occupied valence states and the empty conduction states.

For spin-polarized systems, the electronic structure is calculated
separately for the two spin channels. In antiferromagnetic NiO, the
total spin-up and spin-down DOS are identical because the opposite
magnetic moments compensate each other globally, while the material
still shows an insulating band gap.

## Plotting the density of states
You can conveniently plot the density of states using the Python package
py4vasp. After completing a VASP calculation, load the calculation
directory and call the DOS plotting routine:

    from py4vasp import Calculation

    calc = Calculation.from_path("./CALC/PATH")
    calc.dos.plot()

This command reads the DOS data from the calculation directory and
generates a plot of the density of states.
