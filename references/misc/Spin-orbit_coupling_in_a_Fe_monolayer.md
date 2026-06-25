<!-- Source: https://vasp.at/wiki/index.php/Spin-orbit_coupling_in_a_Fe_monolayer | revid: 36614 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Spin-orbit coupling in a Fe monolayer



[Overview](../tutorials/Magnetism_-_Tutorial.md) \>
[fcc Ni
(revisited)](https://vasp.at/wiki/index.php/Fcc_Ni_(revisited) "Fcc Ni (revisited)") \>
[NiO](NiO.md) \> [NiO
LSDA+U](NiO_LSDA+U.md) \>
[Spin-orbit coupling in a Ni
monolayer](Spin-orbit_coupling_in_a_Ni_monolayer.md) \>
Spin-orbit coupling in a Fe
monolayer \>[constraining
local magnetic
moments](Constraining_local_magnetic_moments.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#Task)
- [2
  Input](#Input)
  - [2.1
    POSCAR](#POSCAR)
  - [2.2
    INCAR](#INCAR)
  - [2.3
    KPOINTS](#KPOINTS)
- [3
  Calculation](#Calculation)
- [4
  Download](#Download)


## Task\[<a
href="/wiki/index.php?title=Spin-orbit_coupling_in_a_Fe_monolayer&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Spin-orbit coupling (SOC) in a freestanding Fe monolayer. This example
is carried out in total analogy to [Spin-orbit coupling in a Ni
monolayer](Spin-orbit_coupling_in_a_Ni_monolayer.md).

## Input\[<a
href="/wiki/index.php?title=Spin-orbit_coupling_in_a_Fe_monolayer&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Spin-orbit_coupling_in_a_Fe_monolayer&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    fcc Fe 100 surface
     3.45
       .50000   .50000   .00000
      -.50000   .50000   .00000
       .00000   .00000  5.00000
      1
    Cartesian
       .00000   .00000   .00000

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Spin-orbit_coupling_in_a_Fe_monolayer&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    SYSTEM        = Fe (100) monolayer
    ISTART        = 0
    ENCUT         = 270.00
    LNONCOLLINEAR = .TRUE.
    MAGMOM        = 0.0 0.0 3.0
    VOSKOWN       = 1
    LSORBIT       = .TRUE.
         
    LMAXMIX       = 4

- For the second calculation, switch to in-plane magnetiztion by setting
  [MAGMOM](../incar-tags/MAGMOM.md)= 3.0 0.0 0.0.

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Spin-orbit_coupling_in_a_Fe_monolayer&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
     0
    Monkhorst-Pack
    9 9 1
    0 0 0

## Calculation\[<a
href="/wiki/index.php?title=Spin-orbit_coupling_in_a_Fe_monolayer&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- From the energy differences of the calculations using in plane and out
  of plane magnetization we see that the easy axis lies (in contrast to
  Ni) out of plane:

$E_{\textrm{MAE}}=E(m_{\perp})-E(m_{\parallel})=-0.2 \\ \textrm{meV}$

## Download\[<a
href="/wiki/index.php?title=Spin-orbit_coupling_in_a_Fe_monolayer&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/d/d9/4_4_SOI_Fe.tgz" class="internal"
title="4 4 SOI Fe.tgz">4_4_SOI_Fe.tgz</a>


[Overview](../tutorials/Magnetism_-_Tutorial.md) \>
[fcc Ni
(revisited)](https://vasp.at/wiki/index.php/Fcc_Ni_(revisited) "Fcc Ni (revisited)") \>
[NiO](NiO.md) \> [NiO
LSDA+U](NiO_LSDA+U.md) \>
[Spin-orbit coupling in a Ni
monolayer](Spin-orbit_coupling_in_a_Ni_monolayer.md) \>
Spin-orbit coupling in a Fe
monolayer \>[constraining
local magnetic
moments](Constraining_local_magnetic_moments.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


