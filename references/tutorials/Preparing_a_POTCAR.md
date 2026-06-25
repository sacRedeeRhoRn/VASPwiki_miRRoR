<!-- Source: https://vasp.at/wiki/index.php/Preparing_a_POTCAR | revid: 25377 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Preparing a POTCAR


The [POTCAR](../input-files/POTCAR.md) file is a mandatory
<a href="/wiki/Input_files" class="mw-redirect"
title="Input files">input file</a> that holds the
[pseudopotential](../categories/Category-Pseudopotentials.md)
for each element in the structure. The templates for each element can be
downloaded from the
<a href="https://www.vasp.at/sign_in/portal/" class="external text"
rel="nofollow">VASP Portal</a>. There are sometimes multiple templates
for one element with subtle differences.


## Contents


- [1 Step-by-step
  instructions](#Step-by-step_instructions)
- [2
  Recommendations and
  advice](#Recommendations_and_advice)
- [3 Example for
  preparing a POTCAR for the Heusler alloy
  TiCo<sub>2</sub>Si](#Example_for_preparing_a_POTCAR_for_the_Heusler_alloy_TiCo2Si)
- [4 Related tags
  and sections](#Related_tags_and_sections)


## Step-by-step instructions\[<a
href="/wiki/index.php?title=Preparing_a_POTCAR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Step-by-step instructions">edit</a> \| (./index.php.md)\]

**Step 1:** Select the [latest
version](../input-files/Available_pseudopotentials.md)
of [POTCAR](../input-files/POTCAR.md) files unless you need to use an older
one to reproduce a result.

**Step 2:** Choose

- [standard
  potentials](../input-files/Available_pseudopotentials.md)
  for calculations depending mainly on occupied states, e.g., within
  density-functional theory, using
  <a href="/wiki/Hybrid_functionals" class="mw-redirect"
  title="Hybrid functionals">hybrid functionals</a>, or
- [GW
  variants](../input-files/Available_pseudopotentials.md)
  if the calculation requires high accuracy for unoccupied states, i.e.,
  for <a href="/wiki/Optical_properties" class="mw-redirect"
  title="Optical properties">optical response</a> and
  <a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
  title="Many-body perturbation theory">many-body perturbation theory</a>.

**Step 3:** Select a [POTCAR](../input-files/POTCAR.md) for a certain
family of
<a href="/wiki/Exchange-correlation_functionals" class="mw-redirect"
title="Exchange-correlation functionals">exchange-correlation (XC)
functionals</a>.

|  |
|----|
| **Tip:** The standard choice is to use the [PBE version](../input-files/Available_pseudopotentials.md) based on [LEXCH](../incar-tags/LEXCH.md)=PE which has a high transferability to other <a href="/wiki/XC_functionals" class="mw-redirect"
title="XC functionals">XC functionals</a>. |

All potentials are constructed based on solving the scalar relativistic
Schrödinger equation for a reference system with a certain
<a href="/wiki/Exchange-correlation_functionals" class="mw-redirect"
title="Exchange-correlation functionals">XC functional</a>. In most
versions, one set is available for the LDA, and one for the GGA. The
transferability to other
<a href="/wiki/Exchange-correlation_functionals" class="mw-redirect"
title="Exchange-correlation functionals">XC functionals</a> is seamless
by specifying the [XC](../incar-tags/XC.md) tag in the
[INCAR](../input-files/INCAR.md).

**Step 4 (optional):** Choose a [different variant (reference atomic
valence configuration, etc.) specified by the
suffix](../input-files/Available_pseudopotentials.md).

|  |
|----|
| **Tip:** The standard choice is to use the bold version in the [list of PAW potentials](../input-files/Available_pseudopotentials.md). |

See [choosing
pseudopotentials](Choosing_pseudopotentials.md).

|  |
|----|
| **Important:** Generally opt for the recommended [POTCAR](../input-files/POTCAR.md) files, but test if the property of interest is sensitive to the choice of the pseudopotential. It may be possible to choose a computationally cheaper version or necessary to select a more demanding one. |

**Step 5:** For a single element in the structure, you can copy the
[POTCAR](../input-files/POTCAR.md) to the working directory, e.g,

     cp /path/to/pot/Al/POTCAR .

For structures with multiple elements, the selected
[POTCAR](../input-files/POTCAR.md) files must be concatenated to create one
[POTCAR](../input-files/POTCAR.md) file containing all species present in
the structure. Combine the potentials by entering, for instance,

     cat /path/to/pot/Al/POTCAR /path/to/pot/C/POTCAR /path/to/pot/H/POTCAR > POTCAR 

The order of the potentials must correspond to the order of the species
in the [POSCAR](../input-files/POSCAR.md) file.

|  |
|----|
| **Tip:** If species names are given in the [POSCAR](../input-files/POSCAR.md), and the order does not match the order in the [POTCAR](../input-files/POTCAR.md), a warning is printed, but VASP will still run. |

## Recommendations and advice\[<a
href="/wiki/index.php?title=Preparing_a_POTCAR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Recommendations and advice">edit</a> \| (./index.php.md)\]

|  |
|----|
| **Important:** Except for the 1st-row elements, all PAW potentials are designed to work at an energy cutoff (<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> tag in the [POTCAR](../input-files/POTCAR.md)) of roughly 250 eV. This is a key aspect of making the calculation computationally cheap. We recommend performing a convergence study of the quantity of interest with respect to the energy cutoff ([ENCUT](../incar-tags/ENCUT.md) tag in the [INCAR](../input-files/INCAR.md)). |

|  |
|----|
| **Mind:** Mismatched order of species in the [POSCAR](../input-files/POSCAR.md) and [POTCAR](../input-files/POTCAR.md) files is a common mistake! Add species names to your [POSCAR](../input-files/POSCAR.md) to receive a warning if this happens. |

|  |
|----|
| **Mind:** You can mix and match [POTCAR](../input-files/POTCAR.md) families. Even combining pseudopotentials generated with different <a href="/wiki/XC_functionals" class="mw-redirect"
title="XC functionals">XC functionals</a> is possible, however make sure to specify the <a href="/wiki/XC_functional" class="mw-redirect"
title="XC functional">XC functional</a> in the [INCAR](../input-files/INCAR.md), see [XC](../incar-tags/XC.md). |

## Example for preparing a [POTCAR](../input-files/POTCAR.md) for the Heusler alloy TiCo<sub>2</sub>Si\[<a
href="/wiki/index.php?title=Preparing_a_POTCAR&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Example for preparing a POTCAR for the Heusler alloy TiCo2Si">edit</a> \| (./index.php.md)\]

In this example, we want to prepare a [POTCAR](../input-files/POTCAR.md)
for a PBE calculation of ferromagnetic TiCo<sub>2</sub>Si. We are
interested in the energy difference between the ferromagnetic and the
nonmagnetic solutions.

The structure is defined by the following
[POSCAR](../input-files/POSCAR.md):

    TiCo2Si
     1.0
      0.0000000000000000    2.8580789844367893    2.8580789844367893
      2.8580789844367893    0.0000000000000000    2.8580789844367893
      2.8580789844367893    2.8580789844367893    0.0000000000000000
    Co Si Ti
     2  1  1
    direct
      0.7500000000000000    0.7500000000000000    0.7500000000000000 Co
      0.2500000000000000    0.2500000000000000    0.2500000000000000 Co
      0.0000000000000000    0.0000000000000000    0.0000000000000000 Si
      0.5000000000000000    0.5000000000000000    0.5000000000000000 Ti

We will use the potpaw_PBE.64 potential set, and since we are interested
in small energy differences caused by different magnetic solutions, we
should use potentials with additional semicore-states in the valence for
the 3d metals. The Co_pv and Ti_sv potentials seem appropriate for the
transition metals. We do not expect Si to become magnetic and are not
interested in unoccupied states, so the Si potential is a good choice
compared to the harder, computationally more demanding Si_GW or even
Si_sv_GW.

On a UNIX machine, one can use the `cat` command to concatenate files
together. One can redirect the output from `stdout` to a file using the
`>` operator. The order in the [POSCAR](../input-files/POSCAR.md) dictates
the order in the [POTCAR](../input-files/POTCAR.md):

    cat ~/potpaw_PBE.64/Co_pv/POTCAR ~/potpaw_PBE.64/Si/POTCAR ~/potpaw_PBE.64/Ti_sv/POTCAR > ~/scratch/TiCo2Si/POTCAR

## Related tags and sections\[<a
href="/wiki/index.php?title=Preparing_a_POTCAR&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

<a href="/wiki/Available_potentials" class="mw-redirect"
title="Available potentials">Available potentials</a>,
[POTCAR](../input-files/POTCAR.md), [Choosing
pseudopotentials](Choosing_pseudopotentials.md),
[Projector-augmented-wave
formalism](../methods/Projector-augmented-wave_formalism.md)


