<!-- Source: https://vasp.at/wiki/index.php/VCAIMAGES | revid: 36724 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VCAIMAGES


VCAIMAGES = \[real\]  
Default: **VCAIMAGES** = -1 

Description: The tag VCAIMAGES
allows to perform thermodynamic integrations (TI); it defines the
coupling parameter λ.

------------------------------------------------------------------------

VCAIMAGES allows two molecular
dynamics (MD) simulations to be performed with e.g. different
[POTCAR](../input-files/POTCAR.md) or [KPOINTS](../input-files/KPOINTS.md)
files or different exchange-correlation functionals, and averages the
energies and forces between the two calculations. This is known as
thermodynamic integration (TI)
<sup>[\[1\]](#cite_note-dorner:PRL:2018-1)</sup>.

The tag VCAIMAGES internally
splits the available nodes into two groups, and each group then performs
an independent VASP calculation (this implies
VCAIMAGES only works in the
MPI version). This behavior is implemented in the same way as the
[nudged elastic band
method](../tutorials/Nudged_elastic_bands.md) (NEB)
described under the tag [IMAGES](IMAGES.md). As opposed to
NEB, only two images are created ([IMAGES](IMAGES.md)=2 is
set internally). The two calculations are performed in subdirectories
`01` and `02` (`00` and `03` are not required, in contrast to NEB).


## Contents


- [1 Description of
  reading a writing during the
  calculation](#description-of-reading-a-writing-during-the-calculation)
- [2 Finding the
  energies](#finding-the-energies)
- [3 Related tags
  and articles](#related-tags-and-articles)
- [4
  References](#references)


### Description of reading a writing during the calculation\[<a
href="/wiki/index.php?title=VCAIMAGES&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Description of reading a writing during the calculation">edit</a> \| (./index.php.md)\]

The two calculations are performed essentially independently in
subdirectories `01` and `02`. The forces, energies, and the stress
tensor of the two calculations are averaged according to the coupling
parameter supplied by
VCAIMAGES. Specifically, the
value supplied in the tag
VCAIMAGES determines the
weight of the calculations performed in subdirectory `01`. The weight of
the second image is
1-VCAIMAGES. After
self-consistency has been reach for both calculations, the energies and
forces are averaged, affecting the final total energy as well as the
forces. This ensures that the trajectories for the two MD simulations
are identical.

|  |
|----|
| **Important:** Make sure that the initial [POSCAR](../input-files/POSCAR.md) is identical in both subdirectories. |

### Finding the energies\[<a
href="/wiki/index.php?title=VCAIMAGES&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Finding the energies">edit</a> \| (./index.php.md)\]

The averaged energies can be found in the
[OUTCAR](../output-files/OUTCAR.md) file after the lines
`ENERGY OF THE ELECTRON-ION-THERMOSTAT SYSTEM (eV)`, as well as in the
file [OSZICAR](../output-files/OSZICAR.md) (in the lines writing the free
energy `F=`). This can make looking for the energies of the individual
calculation awkward. You can find these under
`FREE ENERGIE OF THE ION-ELECTRON SYSTEM (eV)` in the
[OUTCAR](../output-files/OUTCAR.md) file for a DFT calculation (They are
under `ML FREE ENERGIE OF THE ION-ELECTRON SYSTEM (eV)` for a
machine-learned force field (MLFF)).

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vpurple); --box-emph-color: var(--vpurple); padding: 5px; color: var(--vdefault-text-nb); background: var(--vpurple-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span
style="color: var(--vpurple);">Important:</span></strong> In some cases
it might be desirable to use a different number of cores for
<p>the first image and the second image. E.g., when the thermodynamic
integration is performed from a coarse to a dense k-point grid, or from
a cheap to an expensive exchange-correlation functional. To set the
number of cores in the first image the tag <a
href="/wiki/NCORE_IN_IMAGE1" title="NCORE IN IMAGE1">NCORE_IN_IMAGE1</a>
has to be set. The second image then contains the remaining
cores.</p></td>
</tr>
</tbody>
</table>

The usage of this tag is also explained in the supplementary information
of reference
<sup>[\[1\]](#cite_note-dorner:PRL:2018-1)</sup>.

## Related tags and articles\[<a
href="/wiki/index.php?title=VCAIMAGES&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NCORE_IN_IMAGE1](NCORE_IN_IMAGE1.md),
[SCALEE](SCALEE.md), [IMAGES](IMAGES.md),
[Thermodynamic integration
calculations](../tutorials/Thermodynamic_integration_calculations.md)

## References\[<a
href="/wiki/index.php?title=VCAIMAGES&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-dorner:PRL:2018_1-0)</sup>
    <sup>[b](#cite_ref-dorner:PRL:2018_1-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevLett.121.195701"
    class="external text" rel="nofollow">F. Dorner, Z. Sukurma, C. Dellago,
    and G. Kresse, Phys. Rev. Lett. <strong>121</strong>, 195701 (2018).</a>


