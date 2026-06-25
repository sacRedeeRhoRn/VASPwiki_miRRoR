<!-- Source: https://vasp.at/wiki/index.php/Category:2D_materials | revid: 35853 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:2D materials



## Contents


- [1 Surfaces, thin
  films, and 2D
  materials](#surfaces-thin-films-and-2d-materials)
  - [1.1
    Nomenclature](#nomenclature)
    - [1.1.1
      Surfaces](#surfaces)
    - [1.1.2 Thin
      films](#thin-films)
    - [1.1.3 2D
      materials](#2d-materials)
  - [1.2 Slab
    symmetry and stoichiometry](#slab-symmetry-and-stoichiometry)
    - [1.2.1 Slab
      symmetry](#slab-symmetry)
    - [1.2.2 Slab
      stoichiometry](#slab-stoichiometry)
  - [1.3 Advice and
    recommendations](#advice-and-recommendations)
    - [1.3.1
      Creating slab
      models](#creating-slab-models)
    - [1.3.2
      In-plane lattice
      parameters](#in-plane-lattice-parameters)
    - [1.3.3
      Out-of-plane lattice
      parameters](#out-of-plane-lattice-parameters)
    - [1.3.4
      Surface-energy
      calculations](#surface-energy-calculations)
    - [1.3.5
      Adsorption at a
      surface](#adsorption-at-a-surface)
    - [1.3.6
      Computing the work
      function](#computing-the-work-function)
    - [1.3.7
      Simulation of STM
      pictures](#simulation-of-stm-pictures)
    - [1.3.8
      Electrostatic
      corrections](#electrostatic-corrections)
  - [1.4
    Tutorials](#tutorials)
  - [1.5
    References](#references)


# Surfaces, thin films, and 2D materials\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Surfaces, thin films, and 2D materials">edit</a> \| (./index.php.md)\]

Every real crystal or material has a **surface**. In VASP simulations,
however, periodic boundary conditions typically model an infinite
crystal, the perfect bulk. To model a **surface**, a **thin film**, or
an intrinsically **2D material**, therefore, requires breaking these
periodic boundary conditions intentionally. This is done by elongating
the simulation cell in one direction (normal to the intended surface)
without adding more atoms. This creates a vacuum region between repeated
images of thin films of material (commonly called surface slabs, or just
slabs), each of which has two surfaces.

|  |
|----|
| **Mind:** It is not possible to create only a single surface in an atomistic model with periodic boundary conditions. Cleaving a bulk material inevitably produces two surfaces. These two surfaces are generally nonequivalent, although they may be identical depending on the material and the cleavage plane. |

### Nomenclature\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Nomenclature">edit</a> \| (./index.php.md)\]

#### Surfaces\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Surfaces">edit</a> \| (./index.php.md)\]

As discussed above, in atomistic simulations employing periodic boundary
conditions, surfaces are modeled as thin films of a material separated
by a vacuum region of sufficient thickness. When the surface itself is
the primary focus, the slab model must be constructed to mimic a
semi-infinite bulk crystal beneath the surface. The second surface,
located on the opposite side of the slab, should be sufficiently
separated to prevent strong interactions between the two surfaces.

#### Thin films\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Thin films">edit</a> \| (./index.php.md)\]

Although thin-film simulations often employ the same computational setup
and slab model as surface calculations, their objective differs. In
thin-film studies, the goal is to investigate the behavior and
properties of the entire system — including both surfaces and the
bulk-like interior region — rather than isolating the characteristics of
a single surface.

#### 2D materials\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: 2D materials">edit</a> \| (./index.php.md)\]

This class of materials comprises ultrathin films consisting of only a
few atomic layers. Prototypical examples include graphene, which is one
atomic layer thick, and molybdenum disulfide (MoS\$_2\$), which
consists of three atomic layers. Such materials can occur naturally as
van der Waals–bonded layered crystals, but they can also be exfoliated
and studied as mono-, bi-, or few-layer systems.

## Slab symmetry and stoichiometry\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Slab symmetry and stoichiometry">edit</a> \| (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:NaCl_001.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/f/fd/NaCl_001.png/300px-NaCl_001.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/f/fd/NaCl_001.png/450px-NaCl_001.png 1.5x, /wiki/images/thumb/f/fd/NaCl_001.png/600px-NaCl_001.png 2x"
width="300" height="150" /></a>
<figcaption>Fig 1. Side (a) and top (b) view of a symmetric and
stoichiometric, 6-layer-thick NaCl 001 slab.</figcaption>
</figure>

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:NaCl_111_asymm.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/f/f3/NaCl_111_asymm.png/300px-NaCl_111_asymm.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/f/f3/NaCl_111_asymm.png/450px-NaCl_111_asymm.png 1.5x, /wiki/images/thumb/f/f3/NaCl_111_asymm.png/600px-NaCl_111_asymm.png 2x"
width="300" height="150" /></a>
<figcaption>Fig 2. Side (a) and top (b) view of a non-symmetric but
stoichiometric, 6-layer-thick NaCl 111 slab.</figcaption>
</figure>

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:NaCl_111_symm.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/c/ce/NaCl_111_symm.png/300px-NaCl_111_symm.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/c/ce/NaCl_111_symm.png/450px-NaCl_111_symm.png 1.5x, /wiki/images/thumb/c/ce/NaCl_111_symm.png/600px-NaCl_111_symm.png 2x"
width="300" height="150" /></a>
<figcaption>Fig 3. Side (a) and top (b) view of a symmetric but
non-stoichiometric, 5-layer-thick NaCl 111 slab.</figcaption>
</figure>

<a href="/wiki/Symmetry" class="mw-redirect"
title="Symmetry">Symmetry</a> and stoichiometry are important concepts
for surface slabs. Figs. 1 to 3 show three different surface slabs of
NaCl, a 001 and two 111 slabs. All 001 lattice planes contain an equal
amount of Na and Cl atoms, so slabs of all thicknesses are both
symmetric (both surfaces are equivalent) and stoichiometric (the bulk
ratio 1:1 of the atom types is preserved in the slab). The 111 lattice
planes contain either Na or Cl. Thus, the slabs can either be
stoichiometric (Fig. 2) or symmetric (Fig. 3), but it is impossible to
achieve both.

### Slab symmetry\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Slab symmetry">edit</a> \| (./index.php.md)\]

If a slab is non-symmetric, it is important to consider [dipole
corrections](../tutorials/Electrostatic_corrections.md).
The non-symmetric 111 NaCl slab (Fig. 2) is forming a dipole, with
\$Cl^{-}\$ and \$Na^{+}\$ terminations on opposite sides of the slab.
This leads to a potential gradient through the vacuum, which is not
physical and leads to extra interaction between the slab replicas. In
general, this can be true for any non-symmetric slabs, not only for
ionic crystals like NaCl. In those cases, dipole corrections should
always be turned on and the size of the dipole checked in the
[OUTCAR](../output-files/OUTCAR.md) file. However, energy differences due to
dipole interactions are usually smaller than energy differences due to a
different
<a href="/wiki/Exchange-correlation_functional" class="mw-redirect"
title="Exchange-correlation functional">exchange-correlation
functional</a>. They can also interfere with convergence during
[relaxations](../tutorials/Structure_optimization.md). It
is thus usually advisable to initially relax the system without dipole
corrections and then turn on the corrections in a static follow-up
calculation. If there is a resulting dipole, a follow-up relaxation can
be performed using the [WAVECAR](../input-files/WAVECAR.md) file from the
static calculation as a starting point.

Slab symmetry is also important for surface calculations. If the two
surfaces of a slab are not equal, the [computation of the surface
energy](#surface-energy-calculations) becomes more cumbersome.

### Slab stoichiometry\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Slab stoichiometry">edit</a> \| (./index.php.md)\]

Slab stoichiometry is usually less important than symmetry for the
computation setup. But in
[surface-energy-calculation](#surface-energy-calculations) methods that
reference the bulk energy (which is always stoichiometric),
complications can arise.

## Advice and recommendations\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Advice and recommendations">edit</a> \| (./index.php.md)\]

### Creating slab models\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Creating slab models">edit</a> \| (./index.php.md)\]

A clean surface is defined uniquely by the bulk crystal, the lattice
plane along which the cut should be placed, and the termination of the
surface. For a slab model, additional parameters are important — mainly
the slab thickness and the thickness of the vacuum region. Both need to
be converged independently to ensure accurate results.

While it is entirely possible to create a slab model by visualizing a
crystal and thinking hard about lattice planes and stacking, it is
usually more convenient and less error-prone to use available tools. The
Python packages
ASE[^ase-1]
and
Pymatgen[^pymatgen-2]
both provide surface-building capabilities. The following ASE code
snippet creates an NaCl (001) slab with six layers and 10 Å vacuum, for
example:


    from ase.build import bulk, surface
    from ase.io import write
    nacl_bulk = bulk('NaCl', 'rocksalt', a=5.64, cubic=True)
    slab_001 = surface(nacl_bulk, (0,0,1), 3)
    slab_001.center(vacuum=10.0, axis=2)
    write('POSCAR_NaCl_001_6layers.vasp', slab_001, format='vasp', direct=True, sort=True)


### In-plane lattice parameters\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: In-plane lattice parameters">edit</a> \| (./index.php.md)\]

When two surfaces are created by cleaving a crystal, bonds are broken,
and energy needs to be spent. This energy is called the surface energy,
and it can differ significantly between different lattice planes and
surface terminations. In real materials, the surface energy is
vanishingly small compared to the bonding energy in the bulk crystal,
but for a surface-slab model, it can be comparatively large. Thus, the
in-plane lattice parameter will usually shrink compared to the bulk
crystal and depend on the number of layers in the slab.

|  |
|----|
| **Tip:** For surface calculations, it is prudent to use the in-plane lattice parameter of the bulk, and not relax it, since the surface of a semi-infinite bulk would retain the bulk lattice parameter as well. For a thin-film calculation, however, the in-plane lattice parameters should be relaxed to relieve in-plane strain. |

### Out-of-plane lattice parameters\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Out-of-plane lattice parameters">edit</a> \| (./index.php.md)\]

Since bonds will be cut when a surface is created, the spacing between
the first two layers of the surface will usually be reduced with respect
to the bulk lattice spacing. This effect is often important for the
surface properties and should not be disregarded. Avoiding this
relaxation on the slab side opposite to the surface of interest,
however, can reduce the total number of layers needed to mimic the
semi-infinite bulk.

|  |
|----|
| **Tip:** For a surface calculation, it is often beneficial to fix several layers at the bottom of the slab to simulate the semi-infinite bulk more efficiently and with fewer total layers. The [Selective Dynamics](../input-files/POSCAR.md) options in the [POSCAR](../input-files/POSCAR.md) file can be used for this purpose. A thin film should be fully relaxed. |

### Surface-energy calculations\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Surface-energy calculations">edit</a> \| (./index.php.md)\]

The surface energy, \$\gamma\$, is an important characteristic of any
surface, determining its stability and influencing its adhesion
properties, catalytic activity, and ability to form thin films and
interfaces.

For a symmetric and stoichiometric surface slab, the surface energy
\$\gamma\$ of the two equivalent surfaces is given by: \begin{equation}
\gamma = \frac{1}{2A}\left\[E\_\mathrm{slab} - N
E\_\mathrm{bulk}\right\] \quad, \end{equation} where
\$E_\mathrm{slab}\$ is the total energy of the slab,
\$E_\mathrm{bulk}\$ is the total energy of the bulk, and \$N\$ is the
number of formula units in the slab relative to those in the bulk cell.

A more general formula, that holds for non-stoichiometric and
non-symmetric slabs for the surface energies \$\gamma_1\$ and
\$\gamma_2\$ on both sides of the slab is \begin{equation} \gamma_1 =
\frac{1}{A}\left\[E\_\mathrm{slab} - \sum_i N_i\mu_i(p, T)\right\] -
\gamma_2 \quad, \label{eqn:gen_surfen} \end{equation} where the bulk
energy is replaced by a term with the chemical potentials \$\mu_i\$,
which influence the surface energies. Thus, the value of the
temperature- and pressure-dependent chemical potential can determine
which surface is energetically most favorable.

|  |
|----|
| **Tip:** The surface energy must be converged with respect to both the number of layers and the vacuum thickness. This can be challenging. To achieve good convergence of the surface energy with respect to slab thickness, it is beneficial to use a bulk cell with the same symmetry as the surface cell to ensure equivalent k-point sampling. Another approach is to infer the bulk energy from the energies of progressively thicker slabs using the Boettger method[^boettger:prb:1994-3]. |

|  |
|----|
| **Mind:** For weakly bound surfaces in large cells, it may be necessary to increase the electrostatic cutoff ([`EWALD_CUTOFF`](../incar-tags/EWALD_CUTOFF.md)` = 6.0`) and use reciprocal-space projectors to achieve meV-level convergence across number of layers and vacuum thickness. As reciprocal-space projectors are inefficient for large cells, first converge with [`LREAL`](../incar-tags/LREAL.md)` = Auto`, then restart from the converged [WAVECAR](../input-files/WAVECAR.md) file with [`LREAL`](../incar-tags/LREAL.md)` = FALSE` for the final total energy. |

Please also consult our
<a href="https://www.vasp.at/tutorials/latest/surface/part1/"
class="external text" rel="nofollow">tutorial on Ni(111)</a> for more
in-depth information about surface-energy calculations.

### Adsorption at a surface\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Adsorption at a surface">edit</a> \| (./index.php.md)\]

When studying the adsorbtion of a molecule on a surface, a lot of
physical and computational options need to be considered:

- **Coverage** - How many molecules are present per unit cell.
- **Adsorption site(s)** – A surface can have several distinct
  high-symmetry positions (e.g., on-top, bridge, hollow) where a
  molecule can adsorb. Most of these correspond to local minima, and it
  is necessary to explore several possibilities to find the most stable
  configuration.
- **Molecular orientation** – Relaxations can help determine the optimal
  geometry, but molecules may become trapped in local minima.
- **Van der Waals interactions** – Adsorption energies are usually
  accurate only if a [dispersion
  correction](../methods/Category-Van_der_Waals_functionals.md)
  or a [nonlocal van der Waals
  functional](../methods/Nonlocal_vdW-DF_functionals.md)
  is used.
- **Dipole corrections** – Adsorption of a molecule breaks the symmetry
  of the system and usually results in the formation of a dipole moment.
  [Dipole
  corrections](../tutorials/Electrostatic_corrections.md)
  should be enabled, at least after relaxation of the system.

Please also consult our tutorial on
<a href="https://www.vasp.at/tutorials/latest/surface/part2/"
class="external text" rel="nofollow">CO adsorption on Ni(111)</a> for
more detailed guidance.

### Computing the work function\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: Computing the work function">edit</a> \| (./index.php.md)\]

The work function is defined as the work needed to move an electron from
a surface to a point in vacuum sufficiently far away from this surface.
Please consult our how-to page on [computing the work
function](../tutorials/Computing_the_work_function.md).

### Simulation of STM pictures\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: Simulation of STM pictures">edit</a> \| (./index.php.md)\]

Scanning-tunneling-microscopy (STM) pictures can be simulated by using a
post-processing method to compute partial charge densities. Please
consult our how-to page on [partial charge densities and STM
simulations](../tutorials/Partial_charge_densities_and_STM_simulations.md).

### Electrostatic corrections\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: Electrostatic corrections">edit</a> \| (./index.php.md)\]

As mentioned, e.g., in the [slab symmetry](#slab-symmetry) or
[adsorption at a surface](#adsorption-at-a-surface) sections,
electrostatic corrections can be important for 2D materials, thin films,
and surfaces. Please consult the
[electrostatics](Category-Electrostatics.md)
and the [electrostatic
corrections](../tutorials/Electrostatic_corrections.md)
pages for more information.

## Tutorials\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorial for <a href="https://vasp.at/tutorials/latest/surface/part1/"
  class="external text" rel="nofollow">surface calculations</a>.
- Tutorial for <a href="https://vasp.at/tutorials/latest/surface/part2/"
  class="external text" rel="nofollow">adsorption on surfaces</a>.
- Tutorial for <a href="https://vasp.at/tutorials/latest/surface/part3/"
  class="external text" rel="nofollow">STM</a>.

## References\[<a
href="/wiki/index.php?title=Category:2D_materials&amp;veaction=edit&amp;section=19"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^ase-1]: [https://wiki.fysik.dtu.dk/ase/ (2025).](https://wiki.fysik.dtu.dk/ase/)
[^pymatgen-2]: [https://pymatgen.org/ (2022).](https://pymatgen.org/)
[^boettger:prb:1994-3]: [J. C. Boettger, Phys. Rev. B **49**, 16798 (1994).](https://doi.org/10.1103/PhysRevB.49.16798)
