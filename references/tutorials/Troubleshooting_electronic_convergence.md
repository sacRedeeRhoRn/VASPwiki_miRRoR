<!-- Source: https://vasp.at/wiki/index.php/Troubleshooting_electronic_convergence | revid: 35501 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Troubleshooting electronic convergence


There can be many reasons why convergence to the electronic ground state
fails. Below you find some general strategies to overcome convergence
issues in the [electronic
minimization](../categories/Category-Electronic_minimization.md)
and some recommendations for specific cases, e.g., charged systems or
magnetic systems. This
<a href="https://youtu.be/v7gc98lG6Wo" class="external text"
rel="nofollow">lecture covers electronic convergence in VASP</a>.


## Contents


- [1 Step-by-step
  instructions](#step-by-step-instructions)
- [2
  Method-specific
  recommendations](#method-specific-recommendations)
  - [2.1 Magnetic
    calculation with LDA+U](#magnetic-calculation-with-ldau)
  - [2.2 MBJ
    calculation](#mbj-calculation)
  - [2.3 Dipole
    Correction](#dipole-correction)
  - [2.4 Magnetic
    calculations](#magnetic-calculations)
- [3 Related tags
  and articles](#related-tags-and-articles)


## Step-by-step instructions\[<a
href="/wiki/index.php?title=Troubleshooting_electronic_convergence&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Step-by-step instructions">edit</a> \| (./index.php.md)\]

**Step 1:** Simplify the calculation and reduce time-to-solution. Try to
create a minimal [INCAR](../input-files/INCAR.md) file with as few tags as
possible. If the calculation converges, then gradually add them back
until you find which one was causing the problem. Try to reduce the
time-to-solution as much as possible by lowering the **k**-point
sampling (or using gamma-only calculations if applicable), lower
[ENCUT](../incar-tags/ENCUT.md), use [PREC](../incar-tags/PREC.md)=Normal.

**Step 2:** Check the value of [ISMEAR](../incar-tags/ISMEAR.md). If you
have partially occupied states set [ISMEAR](../incar-tags/ISMEAR.md)=-1 or
1.

**Step 3:** Fixing the charge density (for cases where density mixing is
used)

**Step 4:** Increase [NBANDS](../incar-tags/NBANDS.md). Check if you have
enough bands. You can do this by looking at the
[OUTCAR](../output-files/OUTCAR.md) file and checking that there are enough
empty states, i.e., states with zero occupation. When using an iterative
solver, the last states might not be accurately described, if these are
occupied, then convergence is likely to fail. Often, the VASP default
setting for [NBANDS](../incar-tags/NBANDS.md) is insufficient for systems
with f-orbitals or calculations with meta-GGA's.

**Step 5:** Switch [ALGO](../incar-tags/ALGO.md).

**Step 6:** For [IALGO](../incar-tags/IALGO.md)=5X or 4X change
[TIME](../incar-tags/TIME.md).

|  |
|----|
| **Tip:** You can get information at each electronic step using [`NWRITE`](../incar-tags/NWRITE.md)` = 2,3`. |

## Method-specific recommendations\[<a
href="/wiki/index.php?title=Troubleshooting_electronic_convergence&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Method-specific recommendations">edit</a> \| (./index.php.md)\]

In the following, we will describe a few recipes that work for
particular systems. Some of these recipes might be transferable even to
other methods.

### Magnetic calculation with LDA+U\[<a
href="/wiki/index.php?title=Troubleshooting_electronic_convergence&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Magnetic calculation with LDA+U">edit</a> \| (./index.php.md)\]

Magnetic calculations present a lot of challenges, in particular when
the energy differences between different magnetic configurations are
small. Our recommendation is to split the calculation into multiple
steps:

1.  give initial magnetization only to the magnetic atoms
2.  use spin-polarized calculation
3.  perform the calculation in 3 steps (always starting from the
    previous WAVECAR):
    1.  step 1 with [ICHARG](../incar-tags/ICHARG.md)=12 and
        [ALGO](../incar-tags/ALGO.md)=Normal without any LDA+U tags
    2.  step 2 with [ALGO](../incar-tags/ALGO.md)=All (Conjugate gradient)
        and a small [TIME](../incar-tags/TIME.md) step 0.05 instead of the
        default 0.4 (this is crucial)
    3.  step 3 add LDA+U tags keeping [ALGO](../incar-tags/ALGO.md)=All and
        small [TIME](../incar-tags/TIME.md)

It might be helpful to split step 1. in two by first running with a
smaller [ENCUT](../incar-tags/ENCUT.md) and then restarting the calculation
from the [WAVECAR](../input-files/WAVECAR.md) with the desired
[ENCUT](../incar-tags/ENCUT.md).

### MBJ calculation\[<a
href="/wiki/index.php?title=Troubleshooting_electronic_convergence&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: MBJ calculation">edit</a> \| (./index.php.md)\]

This exchange-correlation functional is not particularly easy to
converge in some systems. For these systems, we recommend that you split
the calculation into multiple steps that successively bring you closer
to the solution (always restarting from the WAVECAR of the previous
step):

1.  Converge with the PBE functional
2.  Converge with the [METAGGA](../incar-tags/METAGGA.md)=MBJ functional
    with the [CMBJ](../incar-tags/CMBJ.md) parameter set to some value and
    [ALGO](../incar-tags/ALGO.md)=All and [TIME](../incar-tags/TIME.md)=0.1
3.  Converge with the [METAGGA](../incar-tags/METAGGA.md)=MBJ functional
    without [CMBJ](../incar-tags/CMBJ.md) parameter set and
    [ALGO](../incar-tags/ALGO.md)=All and [TIME](../incar-tags/TIME.md)=0.1

Similar to the [recipe for magnetic calculation with
LDA+U](#magnetic-calculation-with-ldau), it might be helpful to run
steps 1. to 3. with a low [ENCUT](../incar-tags/ENCUT.md) and then perform
step 3. again with the desired [ENCUT](../incar-tags/ENCUT.md).

### Dipole Correction\[<a
href="/wiki/index.php?title=Troubleshooting_electronic_convergence&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Dipole Correction">edit</a> \| (./index.php.md)\]

1.  First, converge the calculation with
    [LDIPOL](../incar-tags/LDIPOL.md)=.FALSE. Store the
    [WAVECAR](../input-files/WAVECAR.md) in the same folder.
2.  Use the [WAVECAR](../input-files/WAVECAR.md) to restart the
    calculation with [LDIPOL](../incar-tags/LDIPOL.md)=.TRUE.

### Magnetic calculations\[<a
href="/wiki/index.php?title=Troubleshooting_electronic_convergence&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Magnetic calculations">edit</a> \| (./index.php.md)\]

What can one do when convergence is bad:

- Start from charge density of non-spin-polarized calculation using
  [ISTART](../incar-tags/ISTART.md)=0 (or remove the
  [WAVECAR](../input-files/WAVECAR.md) file) and
  [ICHARG](../incar-tags/ICHARG.md)=1.
- Use linear mixing by setting [BMIX](../incar-tags/BMIX.md)=0.0001 and
  [BMIX_MAG](../incar-tags/BMIX_MAG.md)=0.0001.
- Mix slowly, i.e., reduce [AMIX](../incar-tags/AMIX.md) and
  [AMIX_MAG](../incar-tags/AMIX_MAG.md).
- REDUCE [MAXMIX](../incar-tags/MAXMIX.md), the number of steps stored in
  the Broyden mixer (default [MAXMIX](../incar-tags/MAXMIX.md)=45).
- Restart from partially converged results (stop a calculation after say
  20 steps and restart from the [WAVECAR](../input-files/WAVECAR.md)
  file).
- Use constraints to stabilize the magnetic configuration.

## Related tags and articles\[<a
href="/wiki/index.php?title=Troubleshooting_electronic_convergence&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NWRITE](../incar-tags/NWRITE.md)


