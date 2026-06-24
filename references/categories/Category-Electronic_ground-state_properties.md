<!-- Source: https://vasp.at/wiki/index.php/Category:Electronic_ground-state_properties | revid: 25261 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Electronic ground-state properties
At the end of an [electronic
minimization](Category-Electronic_minimization.md),
VASP has obtained a converged set of orbitals
([WAVECAR](../input-files/WAVECAR.md)). Based on the orbitals also the
corresponding density is computed via [k-point
integration](../redirects/K-point_integration.md)
([CHGCAR](../input-files/CHGCAR.md)). The orbitals and the density reveal
important insights into material properties and are often the first step
towards analyzing and understanding a material.

An easy way to visualize the properties discussed below is using
[py4vasp](https://vasp.at/py4vasp/latest/index.html).

## Properties of orbitals
For practical purposes, one is most interested in the energy eigenvalues
of the orbitals and their local projections. Consider first the
eigenvalues: Counting all orbitals with eigenvalues in a certain energy
interval yields the [density of states
(DOS)](Category-Density_of_states.md)
([DOSCAR](../output-files/DOSCAR.md)). Often, looking at the DOS can provide
valuable insight into the electronic properties of a material, e.g., an
estimate of the electron itinerancy or specific heat. It is, therefore,
often the first step to start towards understanding a novel material.

[![Band structure plot of energy eigenvalues of
orbitals](https://vasp.at/wiki/images/thumb/c/c0/Band.jpg/534px-Band.jpg)](https://vasp.at/wiki/File:Band.jpg "Band structure plot of energy eigenvalues of orbitals")

The [band
structure](Category-Band_structure.md)
contains even more details about the electronic eigenvalues
([EIGENVAL](../output-files/EIGENVAL.md)) by resolving them with respect
to the Bloch vector **k**. Usually, one uses high-symmetry paths in the
Brillouin zone for band structures. They make it easy to recognize
fundamental and direct bandgaps of the material. Alternatively, VASP
directly reports the bandgaps to the [OUTCAR](../output-files/OUTCAR.md)
file with the verbosity controlled by the
[BANDGAP](../incar-tags/BANDGAP.md) tag. The electronic eigenvalues
determine the occupations of each orbital in conjunction with the
settings for [ISMEAR](../incar-tags/ISMEAR.md),
[SIGMA](../incar-tags/SIGMA.md), and [EFERMI](../incar-tags/EFERMI.md).

Next, we consider the projections of the orbitals that you activate with
the [LORBIT](../incar-tags/LORBIT.md) tag. VASP projects each orbital onto
functions with defined angular momentum within the [PAW
sphere](../redirects/PAW_formalism.md) of each ion. This site
projection augments the data produced by DOS and band-structure
calculations. In addition, the projections describe how much charge has
a particular angular momentum and spin near an ion. This serves as a
good approximation for the magnetic structure of the system.

## Properties on the grid
The [charge
density](Category-Charge_density.md) is
defined on a real-space grid in the unit cell and results from a sum
over bands and **k** points of all occupied orbitals. The grid is often
called FFT grid because the underlying calculation requires repeatedly
switching between real and reciprocal space via FFTs on that grid. For
magnetic calculations ([ISPIN](../incar-tags/ISPIN.md)=2 or
[LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)=T), the orbitals
and charge density have additional spin indices and include the
magnetization. VASP stores the charge density in the
[CHGCAR](../input-files/CHGCAR.md) file and can use it to restart a
calculation ([ICHARG](../incar-tags/ICHARG.md)≥10), which is particularly
relevant for non-self-consistent calculations like band-structure
calculations.

Most of the time, the total charge density is not specific enough to get
insight into material properties. For this reason, VASP offers the
possibility of creating [band-decomposed charge
densities](../redirects/Band-decomposed_charge_densities.md).
Selecting a specific band index or **k** point can shed light, e.g., on
the localization of defects. This feature is helpful in computing the
charge density in the vicinity of the Fermi energy. At a surface, this
density is a good first approximation to compare to experimental
scanning-tunneling-microscopy (STM) images.

[![Average potential perpendicular to the surface of the
system.](https://vasp.at/wiki/images/thumb/b/b2/Work_function.png/500px-Work_function.png)](https://vasp.at/wiki/File:Work_function.png "Average potential perpendicular to the surface of the system.")

During the electronic optimization, VASP also computes the [total
potential](Category-Potential.md). If you want
to analyze the potential, use the
[WRT_POTENTIAL](../incar-tags/WRT_POTENTIAL.md) tag to select the
potential that should be written. Alternatively, use the legacy tag
[LVTOT](../incar-tags/LVTOT.md) if you only need the total potential. A
common application is to inspect planar averages parallel to surfaces or
interfaces. VASP will compute these averages automatically depending on
the [IDIPOL](../incar-tags/IDIPOL.md) setting. Compute the difference of
the average potential and the Fermi energy to get the [work
function](../tutorials/Computing_the_work_function.md).
