<!-- Source: https://vasp.at/wiki/index.php/Partial_charge_densities_and_STM_simulations | revid: 32861 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Partial charge densities and STM simulations


The partial (band-decomposed) charge density can be used to analyze the
contributions of different orbitals or energy ranges to a specific
region in real space. It helps in gaining insight and visualizing
electronic, magnetic, or transport properties, and is especially
important when simulating scanning-tunneling-microscopy (STM) images. In
VASP, the calculation of partial charges is a quick postprocessing step
that is selected by setting [LPARD](../incar-tags/LPARD.md) = .TRUE. in the
[INCAR](../input-files/INCAR.md) file. It is necessary to provide a
[WAVECAR](../input-files/WAVECAR.md) from a converged ground state
calculation as an input file. To select the contributing **k** points
and bands, various options exist, which can be selected via the
[NBMOD](../incar-tags/NBMOD.md), [IBAND](../incar-tags/IBAND.md),
[EINT](../incar-tags/EINT.md), and [KPUSE](../incar-tags/KPUSE.md) tags.

|  |
|----|
| **Mind:** All charge densities, including the band-decomposed charge densities, are symmetrized using both the space and point group symmetries. However, when calculating partial charge from selected **k** points, this can lead to wrong results due to wrong **k** point weights. In that case, the symmetry must be turned off during the initial ground state calculation from which the WAVECAR is generated, as well as during the subsequent band-decomposed charge density calculation. |

|  |
|----|
| **Warning:** Band-decomposed partial charge density postprocessing is not supported for noncollinear magnetic calculations ([LNONCOLLINEAR](../incar-tags/LNONCOLLINEAR.md) = .TRUE.). |


## Contents


- [1 Input tags for
  selecting and writing the partial
  charges](#input-tags-for-selecting-and-writing-the-partial-charges)
- [2 Output
  files](#output-files)
- [3 Step-by-step
  instructions for simulating an STM
  picture](#step-by-step-instructions-for-simulating-an-stm-picture)
- [4
  Example](#example)
- [5 Related tags
  and articles](#related-tags-and-articles)


## Input tags for selecting and writing the partial charges\[<a
href="/wiki/index.php?title=Partial_charge_densities_and_STM_simulations&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Input tags for selecting and writing the partial charges">edit</a> \| (./index.php.md)\]

The following list briefly explains the various
[INCAR](../input-files/INCAR.md) tags that control the behavior of the
band-decomposed charge density decomposition. Please refer to the
documentation of each tag for further details.

- [LPARD](../incar-tags/LPARD.md): Toggles the partial charge
  postprocessing on or off. If only this tag is set, the valence charge
  density is computed for all occupied bands and written to the
  [CHGCAR](../input-files/CHGCAR.md) file (without the augmentation
  occupancies usually written to that file).
- [LPARDH5](../incar-tags/LPARDH5.md) Switches the output to the
  [vaspout.h5](../output-files/Vaspout.h5.md) file. This tag is only
  available as of VASP.6.5.0.
- [IBAND](../incar-tags/IBAND.md): An integer array specifying the bands to
  include in the partial charge density. If [IBAND](../incar-tags/IBAND.md)
  is specified, [NBMOD](../incar-tags/NBMOD.md) is automatically set to the
  number of selected bands.
- [EINT](../incar-tags/EINT.md): Specifies an energy interval. Any energy
  bands with eigenvalues within this range will contribute to the
  calculation of the partial charge density. If the value of the
  [NBMOD](../incar-tags/NBMOD.md) tag is set to -3, the energy values are
  interpreted as relative to the Fermi energy
  $\epsilon_f$. If the [NBMOD](../incar-tags/NBMOD.md) tag
  is not set or is set to -2, the provided energy values will be
  considered as absolute total energies.
- [NBMOD](../incar-tags/NBMOD.md): This tag controls the mode of selecting
  bands that should contribute to the calculation of partial charges.
  - [NBMOD](../incar-tags/NBMOD.md) = n: Use n bands (set automatically if
    [IBAND](../incar-tags/IBAND.md) is used).
  - [NBMOD](../incar-tags/NBMOD.md) = 0: Use all bands (occupied and
    empty).
  - [NBMOD](../incar-tags/NBMOD.md) = -1: Use all occupied bands (and write
    to [CHGCAR](../input-files/CHGCAR.md) instead of
    [PARCHG](../output-files/PARCHG.md) if
    <a href="/wiki/index.php?title=PARCHGH5&amp;action=edit&amp;redlink=1"
    class="new" title="PARCHGH5 (page does not exist)">PARCHGH5</a> =
    .FALSE.)
  - [NBMOD](../incar-tags/NBMOD.md) = -2: To choose the bands that
    contribute, you can utilize an energy interval defined by the tag
    [EINT](../incar-tags/EINT.md).
  - [NBMOD](../incar-tags/NBMOD.md) = -3: Use an energy interval relative
    to the Fermi energy $\epsilon_f$ to select contributing bands (defined by
    [EINT](../incar-tags/EINT.md)).
- [KPUSE](../incar-tags/KPUSE.md): Specifies which **k** points are used in
  the evaluation of the partial charge density.
- [LSEPB](../incar-tags/LSEPB.md): Specifies whether to write the partial
  charge density for selected bands individually or merge them.
- [LSEPK](../incar-tags/LSEPK.md): Specifies whether to write the partial
  charge density for selected **k** points individually or merge them.

## Output files\[<a
href="/wiki/index.php?title=Partial_charge_densities_and_STM_simulations&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Output files">edit</a> \| (./index.php.md)\]

The partial valence charge density is written in the
[PARCHG](../output-files/PARCHG.md) file. If you want to separate the output
by **k** points or bands, setting [LSEPB](../incar-tags/LSEPB.md) and/or
[LSEPK](../incar-tags/LSEPK.md) allows you to write it to multiple
PARCHG.\*.\* files. If the code is compiled with [HDF5
support](../misc/Makefile.include.md) "Makefile.include"),
[`LPARDH5`](../incar-tags/LPARDH5.md)` = .TRUE.` redirects all output to
the [vaspout.h5](../output-files/Vaspout.h5.md) file. In that case
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> can be used to analyze
the output and plot [simulated STM
pictures](#step-by-step-instructions-for-simulating-an-stm-picture).

|  |
|----|
| **Mind:** For spin-polarized calculations, the [PARCHG](../output-files/PARCHG.md) and its variants hold the total density and the magnetization density. For instance, if the 4th band is selected ([IBAND](../incar-tags/IBAND.md) = 4) the first data set in the [PARCHG](../output-files/PARCHG.md) file corresponds to the summed density of the 4th spin up and 4th spin down orbital, whereas the second data set holds the difference between the 4th spin-up and 4th spin-down orbital (magnetization density). Hence, to obtain the charge density corresponding to a specific orbital of a specific spin channel some post-processing of the [PARCHG](../output-files/PARCHG.md) file might be required (building differences or sums). A simple workaround is to use [EINT](../incar-tags/EINT.md) and specify sufficient digits to select only one orbital from either the spin-up or spin-down channel. |

## Step-by-step instructions for simulating an STM picture\[<a
href="/wiki/index.php?title=Partial_charge_densities_and_STM_simulations&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Step-by-step instructions for simulating an STM picture">edit</a> \| (./index.php.md)\]

In this example, we will produce a partial charge density useful for STM
picture simulation. Note that the bias voltage and tip distance from an
experiment do not always translate one-to-one to the simulation.

**Step 1**: Ensure that the ground-state calculation has a
well-converged charge density (low rms(c) in the standard output or the
[OSZICAR](../output-files/OSZICAR.md)). The **k** point mesh should be well
converged to get good results for STM simulations.

**Step 2**: Copy [POSCAR](../input-files/POSCAR.md),
[KPOINTS](../input-files/KPOINTS.md), and
[WAVECAR](../input-files/WAVECAR.md) to a new directory.

**Step 3**: Prepare an appropriate [INCAR](../input-files/INCAR.md) file in
the new directory, making sure you specify the same settings for
[ENCUT](../incar-tags/ENCUT.md), [ISYM](../incar-tags/ISYM.md), and
[ISPIN](../incar-tags/ISPIN.md) as in the ground-state calculation. This
could be a possible [INCAR](../input-files/INCAR.md):

    SYSTEM = STM simulation
    ENCUT = 520
    ISPIN = 2
    LPARD = .TRUE.
    LPARDH5 = .TRUE.
    NBMOD = -3
    EINT = -0.2 0.05
    LSEPB = .FALSE.
    LSEPK = .FALSE.

[LPARD](../incar-tags/LPARD.md) = .TRUE. activates the partial charge mode
and assures that the [WAVECAR](../input-files/WAVECAR.md) file is read.
[LPARDH5](../incar-tags/LPARDH5.md) = .TRUE. redirect the output to the
[vaspout.h5](../output-files/Vaspout.h5.md) file allowing the use of
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> for plotting the
simulated STM picture. [ENCUT](../incar-tags/ENCUT.md) and
[ISPIN](../incar-tags/ISPIN.md) settings are copied over from the
ground-state calculation. [NBMOD](../incar-tags/NBMOD.md) = -3 and
[EINT](../incar-tags/EINT.md) = -0.2 0.05 ensure that the bands from
$\epsilon_f-0.2$ to $\epsilon_f+0.05$ eV are included (corresponding to a negative bias
voltage of about 0.2 Volt). The two remaining tags,
[LSEPB](../incar-tags/LSEPB.md) and [LSEPK](../incar-tags/LSEPK.md) are set to
their default values (.FALSE.) and are there for clarity only. We want
to sum up the contributions of all bands in the energy range at all
**k** points without separating any of this information.

**Step 4**: Run VASP. No electronic (or ionic) minimization is
performed, so the calculation is rapid and does not require
parallelization.

**Step 5**: (optional, requires
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a>): execute the following
Python script in a Python environment where
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> is installed:

    from py4vasp import Calculation
    calc = Calculation.from_file('/path/to/your/vaspout.h5')
    calc.partial_density.to_stm(selection='constant_height(total)', tip_height=4, supercell=[7,7])

This will plot the simulation of an STM image in constant height mode,
with the tip 4Å above the surface. A 7 by 7 supercell is plotted. Under
the hood, the data is pre-processed with Gaussian smoothening for the
STM plot. More convenient methods are provided in
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> to work with the
partial charge data.

**Alternative Step 5** (optional, if VASP is compiled without HDF5
support): Load the resulting [PARCHG](../output-files/PARCHG.md) file with
your favorite visualization program to view constant-height images by
looking at slices through the data or constant current images by using
isosurfaces.

## Example\[<a
href="/wiki/index.php?title=Partial_charge_densities_and_STM_simulations&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Example">edit</a> \| (./index.php.md)\]

The images below show an experimental (on the left) and a simulated (on
the right) scanning tunneling image of Graphene. The experimental image
was measured at room temperature in air at the Department for Earth and
Environmental Sciences, LMU, and Center for NanoScience (CeNS), Munich.
The simulated image was created with
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> at very similar
settings as described in the
[section](#step-by-step-instructions-for-simulating-an-stm-picture)
above.

<a href="/wiki/File:STM_Graphite_exp_sim.png"
class="mw-file-description"
title="Fig 1. Experimental (left) and simulated (right) STM image of Graphene."><img
src="https://vasp.at/wiki/images/thumb/7/70/STM_Graphite_exp_sim.png/800px-STM_Graphite_exp_sim.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/7/70/STM_Graphite_exp_sim.png 1.5x" width="800"
height="266"
alt="Fig 1. Experimental (left) and simulated (right) STM image of Graphene." /></a>

There are tutorials to calcualte the constant height STM and constant
current STM in
<a href="https://www.vasp.at/tutorials/latest/surface/part3/"
class="external text" rel="nofollow">part 3 of the surface tutorials</a>
on our website.

## Related tags and articles\[<a
href="/wiki/index.php?title=Partial_charge_densities_and_STM_simulations&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LPARD](../incar-tags/LPARD.md), [IBAND](../incar-tags/IBAND.md),
[EINT](../incar-tags/EINT.md), [NBMOD](../incar-tags/NBMOD.md),
[KPUSE](../incar-tags/KPUSE.md), [LSEPB](../incar-tags/LSEPB.md),
[LSEPK](../incar-tags/LSEPK.md), [PARCHG](../output-files/PARCHG.md),
[CHGCAR](../input-files/CHGCAR.md), [WAVECAR](../input-files/WAVECAR.md)


