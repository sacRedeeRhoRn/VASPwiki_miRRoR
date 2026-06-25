<!-- Source: https://vasp.at/wiki/index.php/Category:Pseudopotentials | revid: 26242 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Pseudopotentials


<figure class="mw-halign-right" typeof="mw:File">
<a href="/wiki/File:Sketch_Pseudopotentials.png"
class="mw-file-description"
title="Sketch of a pseudopotential and pseudowavefunction"><img
src="https://vasp.at/wiki/images/thumb/f/fb/Sketch_Pseudopotentials.png/300px-Sketch_Pseudopotentials.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/f/fb/Sketch_Pseudopotentials.png 1.5x" width="300"
height="342"
alt="Sketch of a pseudopotential and pseudowavefunction" /></a>
<figcaption>Sketch of a pseudopotential and
pseudowavefunction</figcaption>
</figure>

**Pseudopotentials**, or effective ionic potentials, are well-behaved
potentials that replace the diverging ionic potentials. As a result, the
pseudopotential approach significantly speeds up
<a href="/wiki/Electronic_minimization" class="mw-redirect"
title="Electronic minimization">electronic structure calculations</a>
and makes the simulation of a wider range of materials feasible.

In a nutshell:

- The pseudopotential and associated information required for a
  calculation must be present in a [POTCAR](../input-files/POTCAR.md) file.

<!-- -->

- Simple instructions to set up a [POTCAR](../input-files/POTCAR.md) file
  with the correct format: [Preparing a
  POTCAR](../tutorials/Preparing_a_POTCAR.md).

<!-- -->

- Recommendations on selecting potentials: [Choosing
  pseudopotentials](../tutorials/Choosing_pseudopotentials.md).

<!-- -->

- Overview of all versions and nomenclature: [Available
  pseudopotentials](../input-files/Available_pseudopotentials.md)

## Theory\[<a
href="/wiki/index.php?title=Category:Pseudopotentials&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Theory">edit</a> \| (./index.php.md)\]

VASP employs the [projector-augmented-wave (PAW)
method](../methods/Projector-augmented-wave_formalism.md)
that uses a plane-wave basis. A plane-wave basis is most convenient for
periodic systems, however without the help of **pseudopotentials** the
description of oscillations near the nuclei (nodal features) would
necessitate an excessively high number of plane waves. The PAW method
introduces a mixed basis where the Kohn-Sham (KS) orbitals are
decomposed in three contributions: The pseudo orbitals, pseudo-onsite
orbitals and all-electron onsite orbitals. The PAW potentials and
resulting pseudo orbitals are identical to the true ionic potentials and
KS orbitals outside a specific radius, as illustrated in the figure.
These pseudo orbitals contain no nodal features and are, thus, given in
a plane-wave basis. Inside the PAW spheres the nodal features are
reintroduced on a radial logarithmic grid by subtracting the
pseudo-onsite orbitals and adding the all-electron onsite orbitals.

An additional approximation taken alongside the pseudopotential method
is the *frozen-core approximation*. Here, the electrons associated with
an ion are separated into valence electrons ([ZVAL](../incar-tags/ZVAL.md))
that are assumed to take part in the physical/chemical property of
interest and core electrons that are included as screening of the ionic
potential. The separation into valence and core states depends on the
property of interest and chemical bonds that occur for a specific
material. For a specific atom type, VASP has a range of [available
pseudopotentials](../input-files/Available_pseudopotentials.md)
that vary in terms of core radius, the number of valence electrons,
their ability to describe excited states, etc.

The plane-wave coefficients of the pseudo orbitals are associated with
reciprocal vectors $\mathbf{G}$
in Fourier space. The number of Fourier components determines the
computational cost and can be controlled by the cutoff energy
([ENCUT](../incar-tags/ENCUT.md)). The appropriate value depends on the
pseudopotential and other factors. A potential is considered
[*soft*](../input-files/Available_pseudopotentials.md)
when few Fourier components are sufficient for an accurate
representation, and
[*hard*](../input-files/Available_pseudopotentials.md)
otherwise. It is advised to perform a convergence study on
[ENCUT](../incar-tags/ENCUT.md) with respect to the quantity of interest.


