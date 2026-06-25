<!-- Source: https://vasp.at/wiki/index.php/Electron-phonon_interactions_from_Monte-Carlo_sampling | revid: 35881 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Electron-phonon interactions from Monte-Carlo sampling


|  |
|----|
| **Mind:** This feature is only available from VASP 6.0 or higher. |

For the theory on electron-phonon interactions from Monte-Carlo (MC)
sampling, see the [theory
page](../theory/Electron-phonon_interactions_theory.md).

First of all this method needs a sufficiently large supercell. It also
involves phonon calculations for the $\Gamma$ point
(see [Phonons from finite
differences](Phonons_from_finite_differences.md)).
So many tags in the [INCAR](../input-files/INCAR.md) will be used from the
phonon calculations.

The first implementation of electron-phonon interactions from MC
sampling in VASP is found in Ref.
[^karsai:njp:2018-1].

The original publication of the ZG configuration (one-shot method) is
found in Ref.
[^zacharias:prb:2016-2].


## Contents


- [1 Step-by-step
  instructions](#step-by-step-instructions)
- [2 ZG
  configuration (one-shot
  sampling)](#zg-configuration-one-shot-sampling))
- [3 Full MC
  sampling](#full-mc-sampling)
- [4 Related tags
  and articles](#related-tags-and-articles)
- [5
  References](#references)


## Step-by-step instructions\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_from_Monte-Carlo_sampling&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Step-by-step instructions">edit</a> \| (./index.php.md)\]

**Step 1**: Run a single calculation to create the
[POSCAR](../input-files/POSCAR.md) file(s) with special positions either
belonging to the ZG configuration method or MC sampling. To enable
electron-phonon interactions from MC methods
[PHON_LMC](../incar-tags/PHON_LMC.md)=*.TRUE.* has to be set in the
[INCAR](../input-files/INCAR.md) file. Also,
[IBRION](../incar-tags/IBRION.md)=6 has to be selected (the sampling
methods are currently only implemented for
[IBRION](../incar-tags/IBRION.md)=6). The description of the remaining
required [INCAR](../input-files/INCAR.md) tags for each method is given
below. Both methods produce [POSCAR](../input-files/POSCAR.md) files with
different distorted Wycoff positions but unchanged Brillouin matrix. The
ZG configuration method produces one structure for each temperature
defined in [PHON_TLIST](../incar-tags/PHON_TLIST.md). The files are
labeled as

    POSCAR.T=TEMP.

The MC sampling code produces many [POSCAR](../input-files/POSCAR.md) files
at a given temperature defined by [TEBEG](../incar-tags/TEBEG.md). The
files are labeled as

    POSCAR.T=TEBEG.NUMBER

where NUMBER runs from 1 to
[PHON_NSTRUCT](../incar-tags/PHON_NSTRUCT.md).

**Step 2**: Run calculation for the previously created
[POSCAR](../input-files/POSCAR.md) files on the desired observable. These
calculations can be anything that is suitable for an MC sum
$\langle O(T)\rangle = \frac{1}{n} \sum\limits_{i=1}^{n}
O(x_{T}^{\textrm{MC,i}})$, for example, band gap
calculations, absorption spectra calculations, etc.

**Step 3 (optional)**: Calculate the desired observable for the original
"pristine" supercell. This step can be necessary when changes to an
observable due to electron-phonon interactions are required. An example
of such a calculation is the calculation of the band-gap renormalization
due to electron-phonon interactions.

**Step 4 (optional)**: If MC sampling was used, average the results over
the number of structures created in step 1
([PHON_NSTRUCT](../incar-tags/PHON_NSTRUCT.md)).

## ZG configuration (one-shot sampling)\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_from_Monte-Carlo_sampling&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: ZG configuration (one-shot sampling)">edit</a> \| (./index.php.md)")\]

M. Zacharias and F.
Giustino[^zacharias:prb:2016-2]
introduced a one-shot method (named ZG configuration after the authors).
This method is an approximation to full MC sampling. It only uses a
single distorted structure and hence it is computationally much cheaper
than the full MC sampling. It retains an accuracy very close to the full
MC sampling for converged supercell sizes. For example, we showed that
for the zero-point renormalization of the band gap, the accuracy is
within 5 meV between the ZG configurations and the full MC
sampling[^karsai:njp:2018-1].
Hence we suggest using this method preferably, when convergence of the
supercell size is hard to achieve or the 5 meV accuracy is enough.

To select the ZG configuration
[PHON_NSTRUCT](../incar-tags/PHON_NSTRUCT.md)=0 has to be set in the
[INCAR](../input-files/INCAR.md) file.

The list of temperatures (in K) has to be provided using the tag
[PHON_TLIST](../incar-tags/PHON_TLIST.md), respectively, in the
[INCAR](../input-files/INCAR.md) file. An example would look like:

    PHON_TLIST = 0.0 100.0 200.0 350.0

This makes the simultaneous calculation of the ZG configuration at
several temperatures possible.

An example [INCAR](../input-files/INCAR.md) file for a temperature range
from 0-700 K (with step size of 100 K) is given as:

    System = DEFAULT
    PREC = Accurate
    ISMEAR = 0; SIGMA = 0.1;
    IBRION = 6
    PHON_TLIST = 0.0 100.0 200.0 300.0 400.0 500.0 600.0 700.0
    PHON_NSTRUCT = 0
    PHON_LMC = .TRUE.

## Full MC sampling\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_from_Monte-Carlo_sampling&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Full MC sampling">edit</a> \| (./index.php.md)\]

The tag [PHON_NSTRUCT](../incar-tags/PHON_NSTRUCT.md) sets the
number of structures generated due to the MC sampling. Convergence of
the observable with respect to this number should be monitored.

The tag [TEBEG](../incar-tags/TEBEG.md)=0 is also needed to choose the
temperature at which the sampling is run.

Additionally, the [PHON_LBOSE](../incar-tags/PHON_LBOSE.md) can be set
*.TRUE.* or *.FALSE.* (default
[PHON_LBOSE](../incar-tags/PHON_LBOSE.md)=*.TRUE.*), which selects
Bose-Einstein or Maxwell-Boltzmann statistics, respectively.

A sample [INCAR](../input-files/INCAR.md) file for 0 K looks like the
following:

    System = DEFAULT
    PREC = Accurate
    ISMEAR = 0; SIGMA = 0.1;
    IBRION = 6

    PHON_LMC = .TRUE.
    PHON_NSTRUCT = 100
    TEBEG = 0.0

## Related tags and articles\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_from_Monte-Carlo_sampling&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [PHON_LBOSE](../incar-tags/PHON_LBOSE.md)
- [PHON_LMC](../incar-tags/PHON_LMC.md)
- [PHON_NSTRUCT](../incar-tags/PHON_NSTRUCT.md)
- [PHON_TLIST](../incar-tags/PHON_TLIST.md)
- [Electron-phonon interactions from statistical
  sampling](../theory/Electron-phonon_interactions_theory.md)
- [Band-structure
  renormalization](Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Transport
  calculations](Transport_coefficients_including_electron-phonon_scattering.md)

## References\[<a
href="/wiki/index.php?title=Electron-phonon_interactions_from_Monte-Carlo_sampling&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^karsai:njp:2018-1]: [F. Karsai, M. Engel, E. Flage-Larssen, and G. Kresse, New J. of Phys. **20**, 123008 (2018).](https://doi.org/10.1088/1367-2630/aaf53f)
[^zacharias:prb:2016-2]: [M. Zacharias and F. Giustino, Phys. Rev. B **94**, 075125 (2016).](https://doi.org/10.1103/PhysRevB.94.075125)
