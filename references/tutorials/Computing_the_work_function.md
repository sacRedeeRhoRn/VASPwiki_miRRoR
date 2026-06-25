<!-- Source: https://vasp.at/wiki/index.php/Computing_the_work_function | revid: 25067 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Computing the work function


The work function is defined as the work needed to move an electron from
a surface to a point in vacuum sufficiently far away from this surface.
It is a central quantity in surface science, vacuum science, catalysis,
and other related fields as it characterizes a given surface;
illustrating the presence of impurities, adsorbates, and possible
surface reconstruction. It is typically measured using surface science
techniques such as thermionic emission, the Kelvin probe method, etc. It
has also served as an important measure in various theoretical models
about metallic surfaces. On this page, we describe how to compute the
work function using outputs from a DFT calculation performed using VASP.
We detail best practices, required [INCAR](../input-files/INCAR.md) tags,
and possible pitfalls.

|  |
|----|
| **Mind:** The work function is a property of a surface, not a bulk property. Hence, the content of this page only applies to systems with reduced dimensionality (such as surfaces), i.e., systems where there is expected to be a charge-density-free region in at least one direction of the cell. |


## Contents


- [1 Required
  quantities](#Required_quantities)
- [2 Step-by-step
  instructions](#Step-by-step_instructions)
- [3
  Example](#Example)
- [4 Related tags
  and articles](#Related_tags_and_articles)


## Required quantities\[<a
href="/wiki/index.php?title=Computing_the_work_function&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Required quantities">edit</a> \| (./index.php.md)\]

The work function, $\Phi$, is
computed using the expression, $\Phi =
e\phi_{\mathrm{vacuum}} - \varepsilon_{\mathrm{F}}$
where $\phi_{\mathrm{vacuum}}$ is the vacuum potential, i.e., the potential
sufficiently far away from a surface, such that if an electron were to
be placed at this position, it would not feel the presence of the
surface. $\varepsilon_{F}$ is the Fermi level of the surface, and
$e$ is the charge on the electron (equal to 1 in atomic
units). In the next section, we describe how $\phi_{\mathrm{vacuum}}$ and $\varepsilon_{F}$ are determined from the
[LOCPOT](../output-files/LOCPOT.md) and [OUTCAR](../output-files/OUTCAR.md)
files, respectively.

## Step-by-step instructions\[<a
href="/wiki/index.php?title=Computing_the_work_function&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Step-by-step instructions">edit</a> \| (./index.php.md)\]

**Step 1**: Ensure that the chosen structure has a large enough
atom-free, i.e., charge-density-free, and field-free region in the
direction normal to the surface. A good rule of thumb is to center the
atoms in your cell and have anywhere between 8–12 Å of vacuum on either
side in this direction.

|  |
|----|
| **Warning:** An insufficiently large vacuum region causes a field within the vacuum region and, thus, leads to inaccurate values of the vacuum potential (see point 3). |

**Step 2**: Perform a ground-state-DFT calculation. We suggest setting
[PREC](../incar-tags/PREC.md)=Accurate. If your cell has a net dipole
moment, (i.e., it is not symmetric along the direction of the surface
normal), we suggest switching on the dipole correction by using the
following INCAR tags: [LDIPOL](../incar-tags/LDIPOL.md),
[IDIPOL](../incar-tags/IDIPOL.md), [DIPOL](../incar-tags/DIPOL.md). The use
of the dipole correction is crucial to obtaining a flat field-free
region in the potential (*c.f*. next point). In addition to these tags,
set the [LVHAR](../incar-tags/LVHAR.md)=T to output only the Hartree and
ionic potentials to the [LOCPOT](../output-files/LOCPOT.md) file or set
[`WRT_POTENTIAL`](../incar-tags/WRT_POTENTIAL.md)`=hartree ionic`
to store the potentials in the
[vaspout.h5](../output-files/Vaspout.h5.md) file.

|  |
|----|
| **Tip:** We recommend using only the Hartree and ionic potentials as the exchange-correlation potential decays very slowly in the vacuum region. Using the sum of the Hartree and ionic potentials allows for determining the work function with significantly less vacuum requirements (and hence lower computational cost). |

**Step 3**: Compute the vacuum potential. Average the contents of the
[LOCPOT](../output-files/LOCPOT.md) or the /results/potential/hartree and
/results/potential/ionic datasets of the
[vaspout.h5](../output-files/Vaspout.h5.md) file along the lattice
vectors of the surface, (i.e., both directions perpendicular to the
surface normal). Find the field-free region by determining the region of
space where the potential remains constant. This value of the potential
is the vacuum potential.

|  |
|----|
| **Tip:** There exist two vacuum potential regions, one for either direction of the surface normal. Depending on your system, one of the directions may be more relevant than another. |

**Step 3b**: Alternatively, VASP can compute the vacuum potential when
you set [LVACPOTAV](../incar-tags/LVACPOTAV.md)=T in the INCAR file.
You can then `grep` for the output in the
[OUTCAR](../output-files/OUTCAR.md) file

       grep upper OUTCAR

which gives the following example output:

      vacuum level on the upper side and lower side of the slab         8.049         7.778

**Step 4**: Determine the Fermi energy. The Fermi energy is written
directly to the [OUTCAR](../output-files/OUTCAR.md) file. `grep` for the
following lines in the [OUTCAR](../output-files/OUTCAR.md) to get the Fermi
energy in eV.

      grep "Fermi energy" OUTCAR

## Example\[<a
href="/wiki/index.php?title=Computing_the_work_function&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Example">edit</a> \| (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Workfunction_potentials.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/7/70/Workfunction_potentials.png/400px-Workfunction_potentials.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/7/70/Workfunction_potentials.png/600px-Workfunction_potentials.png 1.5x, /wiki/images/thumb/7/70/Workfunction_potentials.png/800px-Workfunction_potentials.png 2x"
width="400" height="300" /></a>
<figcaption>Vacuum potential referenced to the Fermi energy plotted
against the distance along the surface normal. Insets to the figure show
the work function for (red) a clean Pt(111) surface (blue) Pt(111) with
a carbon atom adsorbed on only one surface termination (atom center ~15
Å on the <em>x</em> axis).</figcaption>
</figure>

Consider an example of a carbon atom adsorbed on an *fcc*-Pt(111)
surface. The structure of such a system is

    Pt16C
    1.0000000000000000
       5.5437171645025325    0.0000000000000000    0.0000000000000000
       0.0000000000000000    4.8009998958550284    0.0000000000000000
       0.0000000000000000    0.0000000000000000   20.0000000000000000
    Pt C
    16 1
    Direct
       0.1250000000000000    0.0833333333333334    0.3302590208582500
       0.6250000000000000    0.0833333333333334    0.3302590208582500
       0.3749999999999999    0.5833333333333334    0.3302590208582500
       0.8750000000000001    0.5833333333333334    0.3302590208582500
       0.3749999999999999    0.2500000000000000    0.4434196736194167
       0.8750000000000001    0.2500000000000000    0.4434196736194167
       0.1250000000000000    0.7500000000000000    0.4434196736194167
       0.6250000000000000    0.7500000000000000    0.4434196736194167
       0.1250000000000000    0.4166666666666667    0.5565803263805833
       0.6250000000000000    0.4166666666666667    0.5565803263805833
       0.3749999999999999    0.9166666666666666    0.5565803263805833
       0.8750000000000001    0.9166666666666666    0.5565803263805833
       0.1250000000000000    0.0833333333333334    0.6697409791417500
       0.6250000000000000    0.0833333333333334    0.6697409791417500
       0.3749999999999999    0.5833333333333334    0.6697409791417500
       0.8750000000000001    0.5833333333333334    0.6697409791417500
       0.0000000000000000    0.0000000000000000    0.7597409791417501

The bottom and top surfaces are not identical: one is clean, and the
other has carbon adsorbed on it. Since the system has a net dipole
moment, we need to use the dipole correction in our calculation. An
example [INCAR](../input-files/INCAR.md) file for this system is,

    LDIPOL  = T
    IDIPOL  = 3
    DIPOL   = 0.5 0.5 0.5
    LVHAR   = T
    PREC    = Accurate

The Figure to the right shows a representative example of the vacuum
potential obtained by averaging the contents of
[LOCPOT](../output-files/LOCPOT.md). This potential is referenced to the
Fermi energy and is plotted against the distance along the surface
normal (*x* axis) for two systems, *fcc* Pt(111) surface (in blue) and
Pt(111) surface with a carbon atom adsorbed on one surface termination
(Pt(111)-C\*). The vacuum potentials are flat, (i.e., constant), on
either side (magnified in insets). The work function on either side of
the slab is annotated in the insets as $\Phi$. It is
equal for both sides of the clean slab but slightly higher for the case
of Pt(111)-C\*.

## Related tags and articles\[<a
href="/wiki/index.php?title=Computing_the_work_function&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LOCPOT](../output-files/LOCPOT.md), [LDIPOL](../incar-tags/LDIPOL.md),
[IDIPOL](../incar-tags/IDIPOL.md), [DIPOL](../incar-tags/DIPOL.md),
[LVHAR](../incar-tags/LVHAR.md),
[WRT_POTENTIAL](../incar-tags/WRT_POTENTIAL.md)


