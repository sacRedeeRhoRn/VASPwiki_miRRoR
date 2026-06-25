<!-- Source: https://vasp.at/wiki/index.php/Category:Electrostatics | revid: 27554 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Electrostatics


Computing the properties of charged and dipolar systems requires proper
treatment of the **electrostatics**. Without appropriate corrections,
the energies, forces, and potentials will not correspond to the expected
boundary conditions. This page provides a summary of the corrections
that are implemented and the relevant [INCAR](../input-files/INCAR.md) tags
to activate these corrections. Practical details regarding convergence,
setting up, and running relevant calculations can be found in the how-to
section.

## Summary of relevant INCAR tags\[<a
href="/wiki/index.php?title=Category:Electrostatics&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Summary of relevant INCAR tags">edit</a> \| (./index.php.md)\]

The table contains a summary of [INCAR](../input-files/INCAR.md) tags for
performing monopole, dipole, and quadrupole corrections. Please see the
relevant pages of the respective tags for more detailed information. In
general, we refer to a 3D system as a system with periodicity in all
three dimensions of a cell, a 2D system as having requirements of
periodicity only along two out of the three dimensions (eg. a slab or a
2D-material such as graphene), a 1D system as having requirements of
periodicity along only one out of the three dimensions (eg. a nano-rod)
and a 0D system as having no requirements of periodicity (such as an
atom or a molecule).

|  |  |  |  |
|----|----|----|----|
| Dimensionality of the system | Does the system have net charge? | Does the system have a net dipole moment? | Relevant INCAR tags for monopole/dipole corrections |
| Any | No | No | None |
| 3D | Yes | No | [NELECT](../incar-tags/NELECT.md), [LMONO](../incar-tags/LMONO.md), [EPSILON](../incar-tags/EPSILON.md) |
| 3D | No | Yes | [DIPOL](../incar-tags/DIPOL.md), [IDIPOL](../incar-tags/IDIPOL.md), [EPSILON](../incar-tags/EPSILON.md) |
| 3D | Yes | Yes | [NELECT](../incar-tags/NELECT.md), [DIPOL](../incar-tags/DIPOL.md), [IDIPOL](../incar-tags/IDIPOL.md), [EPSILON](../incar-tags/EPSILON.md) |
| 2D | Yes | No | [NELECT](../incar-tags/NELECT.md), [KERNEL_TRUNCATION/LTRUNCATE](../incar-tags/KERNEL_TRUNCATION__LTRUNCATE.md) |
| 2D | No | Yes | [IDIPOL](../incar-tags/IDIPOL.md), [LDIPOL](../incar-tags/LDIPOL.md), [DIPOL](../incar-tags/DIPOL.md), [KERNEL_TRUNCATION/LTRUNCATE](../incar-tags/KERNEL_TRUNCATION__LTRUNCATE.md) |
| 2D | Yes | Yes | [NELECT](../incar-tags/NELECT.md), [KERNEL_TRUNCATION/LTRUNCATE](../incar-tags/KERNEL_TRUNCATION__LTRUNCATE.md) |
| 1D | Yes | No | [NELECT](../incar-tags/NELECT.md) |
| 1D | No | Yes | Not implemented |
| 1D | Yes | Yes | Not implemented |
| 0D | Yes | No | [NELECT](../incar-tags/NELECT.md), [LMONO](../incar-tags/LMONO.md), [LDIPOL](../incar-tags/LDIPOL.md), [KERNEL_TRUNCATION/LTRUNCATE](../incar-tags/KERNEL_TRUNCATION__LTRUNCATE.md) |
| 0D | No | Yes | [LDIPOL](../incar-tags/LDIPOL.md), [KERNEL_TRUNCATION/LTRUNCATE](../incar-tags/KERNEL_TRUNCATION__LTRUNCATE.md) |
| 0D | Yes | Yes | [NELECT](../incar-tags/NELECT.md), [LMONO](../incar-tags/LMONO.md), [LDIPOL](../incar-tags/LDIPOL.md), [KERNEL_TRUNCATION/LTRUNCATE](../incar-tags/KERNEL_TRUNCATION__LTRUNCATE.md) |

|  |
|----|
| **Tip:** If an external electrostatic field is desired for slab or molecular calculations, see [EFIELD](../incar-tags/EFIELD.md). |

## How to\[<a
href="/wiki/index.php?title=Category:Electrostatics&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

Practical guides to electrostatic corrections implemented in VASP:

- [Electrostatic
  corrections](../tutorials/Electrostatic_corrections.md)
- [Computing the work
  function](../tutorials/Computing_the_work_function.md)
- [Dipole correction for defects in
  solids](../tutorials/Dipole_corrections_for_defects_in_solids.md)


