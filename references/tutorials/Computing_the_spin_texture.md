<!-- Source: https://vasp.at/wiki/index.php/Computing_the_spin_texture | revid: 37285 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Computing the spin texture
The spin texture is the momentum-resolved expectation value of the spin,
$\langle\boldsymbol{\sigma}(\mathbf{k})\rangle$, of the
[Kohn-Sham](Band-structure_calculation_using_density-functional_theory.md)
orbitals. In crystals that lack inversion symmetry, [spin-orbit
coupling](../incar-tags/LSORBIT.md) lifts the spin degeneracy of the
bands and locks the spin direction to the crystal momentum **k**. The
resulting winding patterns of the in-plane spin, such as the Rashba and
Dresselhaus textures, are a direct fingerprint of the underlying
symmetry. This page describes how to compute the spin texture as a
noncollinear calculation with spin-orbit coupling, sampled on a
two-dimensional **k** plane, and how to read out and plot the
$\sigma_x$, $\sigma_y$, and $\sigma_z$ spin
projections with [py4vasp](https://vasp.at/py4vasp/latest/index.html).

|  |
|----|
| **Mind:** [py4vasp](https://vasp.at/py4vasp/latest/index.html) reads the [vaspout.h5](../output-files/Vaspout.h5.md) file, which VASP writes only when it is compiled with HDF5 support. |

The procedure applies to any inversion-asymmetric system once the
relevant spin-split bands and the appropriate **k** plane have been
identified.

## Contents

- [1 Step-by-step instructions](#Step-by-step_instructions)
  - [1.1 Step 1: Compute the self-consistent ground
    state](#Step_1:_Compute_the_self-consistent_ground_state)
  - [1.2 Step 2: Compute the band structure and identify the
    Rashba-split
    bands](#Step_2:_Compute_the_band_structure_and_identify_the_Rashba-split_bands)
  - [1.3 Step 3: Choose the **k** plane from the crystal
    symmetry](#Step_3:_Choose_the_k_plane_from_the_crystal_symmetry)
  - [1.4 Step 4: Run the non-self-consistent calculation on the planar
    mesh](#Step_4:_Run_the_non-self-consistent_calculation_on_the_planar_mesh)
  - [1.5 Step 5: Plot the spin texture with
    py4vasp](#Step_5:_Plot_the_spin_texture_with_py4vasp)
- [2 Troubleshooting](#Troubleshooting)
  - [2.1 Probe explicit **k** points near the
    center](#Probe_explicit_k_points_near_the_center)
- [3 Symmetry requirements and cell
  orientation](#Symmetry_requirements_and_cell_orientation)
  - [3.1 Which symmetry allows a spin
    texture](#Which_symmetry_allows_a_spin_texture)
  - [3.2 Locating the axis and orienting the
    cell](#Locating_the_axis_and_orienting_the_cell)
- [4 Recommendations and advice](#Recommendations_and_advice)
- [5 Related tags and articles](#Related_tags_and_articles)

## Step-by-step instructions
### Step 1: Compute the self-consistent ground state
Set up a self-consistent noncollinear calculation with spin-orbit
coupling and run it with the `vasp_ncl` executable. In addition to the
tags for [Setting up an electronic
minimization](Setting_up_an_electronic_minimization.md),
the relevant [INCAR](../input-files/INCAR.md) tags here are:

    LSORBIT = .TRUE.       ! spin-orbit coupling (also sets LNONCOLLINEAR)
    MAGMOM = 9*0           ! three components per atom; here three atoms, no initial moment
    SAXIS = 0 0 1          ! spin-quantization axis (default)
    GGA_COMPAT = .FALSE.   ! improves the numerical precision of GGA with SOC
    LASPH = .TRUE.         ! aspherical one-center contributions
    LMAXMIX = 4            ! 4 (d electrons) or 6 (f electrons): write the charge density to higher l
    LCHARG = .TRUE.        ! write the converged density for the restart

[LSORBIT](../incar-tags/LSORBIT.md)=.TRUE. switches on spin-orbit
coupling and automatically sets
[LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md)=.TRUE., so the
calculation treats the full 2×2 spin density. In the noncollinear case,
[MAGMOM](../incar-tags/MAGMOM.md) takes three components per atom; the
example uses a nonmagnetic starting guess. The spin-quantization axis is
fixed by [SAXIS](../incar-tags/SAXIS.md), and all spin projections are
reported in this basis. Keeping symmetry switched on for the ground
state speeds up the self-consistent run.

|  |
|----|
| **Important:** Set [`LMAXMIX`](../incar-tags/LMAXMIX.md)` = 4` for d-electron systems and [`LMAXMIX`](../incar-tags/LMAXMIX.md)` = 6` for f-electron systems so that the one-center PAW charge densities are written to the [CHGCAR](../input-files/CHGCAR.md) file for the non-self-consistent restart. |

### Step 2: Compute the band structure and identify the Rashba-split bands
[![](https://vasp.at/wiki/images/thumb/4/43/Spin-texture-band-structure.png/400px-Spin-texture-band-structure.png)](https://vasp.at/wiki/File:Spin-texture-band-structure.png)

Example band structure along a high-symmetry path through the
time-reversal-invariant point. The spin-split pairs are degenerate at
the point and split away from it, with the band extrema displaced off
the point. This example is bulk BiTeI along *H*-*A*-*L*.

Before sampling a plane, compute the one-dimensional band structure
along a high-symmetry path and locate the spin splitting. Follow the
procedure in [Band-structure calculation using density-functional
theory](Band-structure_calculation_using_density-functional_theory.md)
to set up and plot the band structure; restart from the converged
density of Step 1.

Choose a path that passes through the time-reversal-invariant point
where you expect the splitting. The Rashba signature in the band
structure is:

- The spin-split bands are **Kramers-degenerate** at the
  time-reversal-invariant point and **split** as **k** moves away from
  it.
- The dispersion shows the characteristic **Rashba shape**: the band
  extremum is displaced off the high-symmetry point, so the band
  develops a local extremum at the point and a ring of true extrema
  around it (the "camelback" for a conduction band).

This identification tells you which bands carry the texture and on which
point to center the planar mesh in the following steps. The spin texture
is a symmetry effect and is well-defined even for small splittings, so a
small splitting does not prevent resolving the texture. However, if the
Rashba splitting is smaller than expected, it may indicate a problem
with the setup, such as an inaccurate geometry or a too-small bandgap.

### Step 3: Choose the **k** plane from the crystal symmetry
The spin texture is a two-dimensional quantity, so the
non-self-consistent run samples a planar **k** mesh rather than a path.
Using the band structure from Step 2, pick the band extremum where the
spin splitting appears — it does not have to be the largest splitting —
as the point on which to center the mesh.

Sample a regular mesh in the plane perpendicular to the axis around
which the texture is organized, with a single subdivision along the
out-of-plane direction (for example `n n 1`). Center the plane on the
chosen extremum through the [KPOINTS](../input-files/KPOINTS.md) shift.
The components to plot are the two in-plane spin components (for example
$\sigma_x$ and $\sigma_y$): a nonzero in-plane winding (a vortex or
anti-vortex) is the Rashba signature, and the out-of-plane component is
close to zero near the center.

For how to find that axis for your crystal from its symmetry, and what
to do when the cell is not oriented with the axis along a Cartesian
direction, see [Symmetry requirements and cell
orientation](#Symmetry_requirements_and_cell_orientation) below.

### Step 4: Run the non-self-consistent calculation on the planar mesh
Create a directory for the planar run and copy the input files together
with the converged density:

[TABLE]

Provide the planar **k** mesh in the [KPOINTS](../input-files/KPOINTS.md)
file. The shift selects the plane that contains the extremum identified
in Step 2. If the band extremum is at the $\Gamma$ point, no shift is needed. Otherwise, choose the shift so
that a mesh point coincides with the extremum: shift the out-of-plane
component to select the plane that contains the extremum, and shift the
in-plane components if the extremum is not at the projected zone center.

The following is an example for bulk BiTeI, where the extremum (the *A*
point) lies at the zone boundary along the out-of-plane direction, so
the third component is shifted to 1/2:

    Planar mesh (example: BiTeI A-plane)
    0
    Gamma
    11 11 1
    0 0 0.5

Add the following tags to the [INCAR](../input-files/INCAR.md) file from
Step 1 for a restart at fixed density:

    ICHARG = 11        ! restart from CHGCAR, density held fixed
    ISYM = -1          ! keep the full planar mesh
    LORBIT = 11        ! write the spin projections
    LWAVE = .FALSE.
    LCHARG = .FALSE.

[`ICHARG`](../incar-tags/ICHARG.md)` = 11` reads the converged charge
density and keeps it fixed. [`ISYM`](../incar-tags/ISYM.md)` = -1` switches
off symmetry, which is essential here: with symmetry on, VASP reduces
the planar mesh to the irreducible wedge, but the quiver plot requires
the full planar mesh. [`LORBIT`](../incar-tags/LORBIT.md)` = 11` writes
the site- and orbital-resolved spin projections that
[py4vasp](https://vasp.at/py4vasp/latest/index.html) reads.

To refine the texture, increase the mesh density (for example, to
21×21×1); the plane always spans the full Brillouin zone, and the shift
only selects the fixed component.

### Step 5: Plot the spin texture with py4vasp
[![](https://vasp.at/wiki/images/thumb/8/8f/Spin-texture-bitei-full-bz.png/400px-Spin-texture-bitei-full-bz.png)](https://vasp.at/wiki/File:Spin-texture-bitei-full-bz.png)

Example of the `to_quiver` output over the full Brillouin zone: the
in-plane spin arrows wind around the band extremum, and the threefold
pattern reflects the crystal symmetry. This example is bulk BiTeI on a
plane through the top face of the Brillouin zone.

[py4vasp](https://vasp.at/py4vasp/latest/calculation/band/#from_path-to_quiver)
draws the in-plane spin as a quiver plot. Run the following in a Python
notebook:

    import py4vasp
    calc = py4vasp.Calculation.from_path("/path/to/calculation")
    conduction_band = 29  # replace with the index of the conduction band in your calculation
    calc.band.to_quiver(f"sigma_x~sigma_y(band={conduction_band})")

The arguments of `to_quiver` are `selection`, which names the two
in-plane spin components and the band index, `supercell`, which
replicates the plane periodically, and `normal` which rotates the cell
in the plane. Refer to the
[py4vasp](https://vasp.at/py4vasp/latest/calculation/band/#from_path-to_quiver)
documentation for the details.

## Troubleshooting
A spin-texture plot is hard to judge in isolation. Probe a few explicit
**k** points near the center of the plane and read out the spin
components directly to isolate the physics from any meshing or plotting
artifact.

### Probe explicit **k** points near the center
Pick a few **k** points a small distance from the band extremum and read
out the spin components directly. First, provide an explicit Cartesian
[KPOINTS](../input-files/KPOINTS.md) list with small displacements along
$\pm x$ and $\pm y$:

    Explicit k points near the band extremum
    4
    Cartesian
      0.01  0.00  0.00  1
     -0.01  0.00  0.00  1
      0.00  0.01  0.00  1
      0.00 -0.01  0.00  1

Set the third component so that the points lie on the plane of the
extremum, as in Step 4, and mind the Cartesian-unit caveat noted under
[Recommendations](#Recommendations_and_advice). Run this with the same
restart [INCAR](../input-files/INCAR.md) as Step 4.

Then read the spin components and print one of them for the band of
interest:

    import py4vasp
    calc = py4vasp.Calculation.from_path("/path/to/calculation")
    spin = calc.band.read("x, y, z")  # keys "x","y","z"; each array has shape [k point, band]
    # read() returns a 0-based array, while the band index in the to_quiver selection
    # string is 1-based, so subtract one here
    print(spin["x"][:, conduction_band - 1])  # sigma_x at every k point for the conduction band

The expected pattern depends on the type of spin-orbit coupling:

- **Rashba** (polar, $C_{nv}$): the
  spin is tangential, perpendicular to **k** in the plane, winding in a
  single circular sense, with $\sigma_z\approx0$ near the center. For a point along the Cartesian *x* axis
  only $\sigma_y$ is nonzero, and along
  *y* only $\sigma_x$.
- **Dresselhaus** (bulk-inversion asymmetry, for example zinc-blende):
  the pattern is not a simple circle; the spin direction follows the
  cubic angular dependence, so the perpendicular-to-**k** rule does not
  hold in the same way.

The idea of sampling near the center and checking the component signs
against the expected symmetry is general; only the expected pattern
changes with the type of coupling.

## Symmetry requirements and cell orientation
[![](https://vasp.at/wiki/images/thumb/e/e6/Rashba-dresselhaus.png/400px-Rashba-dresselhaus.png)](https://vasp.at/wiki/File:Rashba-dresselhaus.png)

Spin textures of the Rashba (left) and Dresselhaus (right) spin-orbit
fields: arrows give the spin direction along a constant-k circle for
each effective Hamiltonian - tangential/chiral for Rashba,
mirror-symmetric for Dresselhaus

Step 3 samples a plane perpendicular to a particular axis. Assuming the
crystal symmetry is known, this section explains how to find that axis,
how to confirm that a spin texture is allowed at all, and how to orient
the cell so that the planar mesh and the in-plane spin components are
set up consistently.

### Which symmetry allows a spin texture
A spin texture requires broken inversion symmetry, and the type of
texture is fixed by the point group:

- **Rashba** textures require a **polar** point group, that is, one with
  a unique polar axis (the polar classes, such as $C_{2v}$, $C_{3v}$,
  $C_{4v}$, and $C_{6v}$). The Rashba spin-orbit field, and hence the
  in-plane winding, lies in the plane **perpendicular to the polar
  axis**.
- **Dresselhaus** textures arise from bulk inversion asymmetry in
  crystals that are non-centrosymmetric but **not** polar, such as
  zinc-blende ($T_d$). The texture is
  anisotropic rather than a simple tangential winding, so the plane is
  chosen to expose that pattern (for example a (001) **k** plane).

If the crystal is centrosymmetric, the bands are spin-degenerate and
there is no spin texture to compute.

### Locating the axis and orienting the cell
For a Rashba system the plane to sample is perpendicular to the polar
axis, which is the unique direction left invariant by all symmetry
operations of the point group (the principal rotation axis of
$C_{nv}$). A regular `n n 1` mesh
samples the plane spanned by the first two reciprocal lattice vectors,
and the [py4vasp](https://vasp.at/py4vasp/latest/index.html)
`sigma_x~sigma_y` selection assumes the plane normal points along the
Cartesian *z* axis. Two points therefore need checking:

- **The orientation in the [POSCAR](../input-files/POSCAR.md) may differ
  from the standard setting.** The cell can be written with its lattice
  vectors rotated relative to the conventional crystallographic
  orientation, so the polar axis does not necessarily lie along the
  third lattice vector or along a Cartesian axis. Determine where the
  polar axis actually points in your [POSCAR](../input-files/POSCAR.md).
- **The polar axis must align with a Cartesian axis.** To use `n n 1`
  with the $\sigma_x$–$\sigma_y$ in-plane
  components, the polar axis (the plane normal) must lie along Cartesian
  *z*. If it does not, either reorient the cell — rotate the lattice
  vectors so the polar axis is along *z* — and use `n n 1`, or choose
  the mesh that places the single subdivision along the matching
  direction (`n n 1`, `n 1 n`, or `1 n n`) and plot the corresponding
  pair of in-plane components. This concerns the orientation of the
  real-space cell, which is separate from the units of an explicit
  `Cartesian` [KPOINTS](../input-files/KPOINTS.md) list discussed under
  [Recommendations and advice](#Recommendations_and_advice).

As an example, BiTeI is trigonal (space group $P3m1$, point group $C_{3v}$),
so it is polar and the polar axis is the *c* axis. The plane to sample
is the $k_x$–$k_y$ plane. In the conventional hexagonal setting the *c* axis is
along Cartesian *z*, so an `n n 1` mesh together with the
`sigma_x~sigma_y` selection works directly.

## Recommendations and advice
- **Use the noncollinear executable.** Spin-orbit coupling requires
  `vasp_ncl`; the standard or gamma-only executables do not include it.
- **Mind the k-point units.** A `Cartesian`
  [KPOINTS](../input-files/KPOINTS.md) list is given in units of
  $2\pi/\text{SCALE}$, where SCALE is
  the [POSCAR](../input-files/POSCAR.md) scaling factor. A value of 0.05
  then corresponds to $0.05\cdot2\pi\approx0.31$ Å⁻¹, which can fall far outside the linear Rashba region
  and into a regime of warping with a spurious $\sigma_z$. A `Reciprocal` (fractional) list avoids the
  $2\pi$ factor, but its axes are the
  reciprocal lattice vectors, which are non-orthogonal for a hexagonal
  cell. There, $\mathbf{b}_1$ is 30°
  off the Cartesian *x* axis, so a fractional $(\delta, 0, \*)$ point is not along *x* and its tangential
  spin acquires a nonzero $\sigma_x$
  even for an ideal Rashba state. To test the "only
  $\sigma_y$ along *x*" rule, use small
  `Cartesian` coordinates so the point truly lies on the Cartesian axis.
- **Place the plane correctly in Cartesian coordinates.** In a
  `Cartesian` list the third coordinate is also scaled by
  $2\pi/\text{SCALE}$. To sit on a plane
  at fractional $k_z=1/2$ use
  $k_z=0.5/c$ rather than 0.5.
- **to_quiver needs a full regular mesh.** The quiver routine reads the
  grid dimensions from the mesh metadata and rejects an explicit **k**
  list. The plotted plane therefore always spans the whole Brillouin
  zone; refine the texture by increasing the mesh density, not by
  narrowing the window. The routine plots the in-plane components only
  and does not color the arrows by $\sigma_z$.
- **Keep symmetry off for the spin-texture calculation.** Set
  [`ISYM`](../incar-tags/ISYM.md)` = -1` so that all **k** points are kept;
  the full mesh is needed for plotting.

## Related tags and articles
[Band-structure calculation using density-functional
theory](Band-structure_calculation_using_density-functional_theory.md)

Files: [KPOINTS](../input-files/KPOINTS.md),
[vaspout.h5](../output-files/Vaspout.h5.md),
[PROCAR](../output-files/PROCAR.md)

Tags: [LSORBIT](../incar-tags/LSORBIT.md),
[LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md),
[SAXIS](../incar-tags/SAXIS.md), [MAGMOM](../incar-tags/MAGMOM.md),
[LORBIT](../incar-tags/LORBIT.md), [ISYM](../incar-tags/ISYM.md),
[ICHARG](../incar-tags/ICHARG.md), [LMAXMIX](../incar-tags/LMAXMIX.md),
[GGA_COMPAT](../incar-tags/GGA_COMPAT.md),
[LASPH](../incar-tags/LASPH.md)
