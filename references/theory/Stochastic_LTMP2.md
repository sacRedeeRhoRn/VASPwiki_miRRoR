<!-- Source: https://vasp.at/wiki/index.php/Stochastic_LTMP2 | revid: 35863 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Stochastic LTMP2



[Overview](../tutorials/MP2_ground_state_calculation_-_Tutorial.md) \>
[MP2](../incar-tags/MP2.md) \>
[LTMP2](../tutorials/LTMP2_-_Tutorial.md) \>
stochastic LTMP2
 \> <a
href="/wiki/index.php?title=High_energy_contributions_using_stochastic_LTMP2&amp;action=edit&amp;redlink=1"
class="new"
title="High energy contributions using stochastic LTMP2 (page does not exist)">High
energy contributions using stochastic LTMP2</a> \>
[List of tutorials](../categories/Category-Tutorials.md)


On this page, we explain how to perform a calculation using the
**stochastic
LTMP2**[^schaefer2018-1]
algorithm. Make sure you successfully completed the preparation steps <a
href="/wiki/MP2_ground_state_calculation#Preparation:_the_Hartree-Fock_ground_state"
class="mw-redirect" title="MP2 ground state calculation">Hartree-Fock
ground state</a> and <a
href="/wiki/MP2_ground_state_calculation#Calculating_the_unoccupied_Hartree-Fock_orbitals"
class="mw-redirect" title="MP2 ground state calculation">Hartree-Fock
virtuals</a>.

**NOTE:** *If you use this algorithm, please cite reference
[^schaefer2018-1]
in your publication in addition to the standard VASP reference.*


## Contents


- [1 The INCAR
  file](#the-incar-file)
  - [1.1 NOMEGA
    flag](#nomega-flag)
  - [1.2 ESTOP
    flag](#estop-flag)
  - [1.3 NSTORB
    flag](#nstorb-flag)
- [2
  Parallelization](#parallelization)
- [3
  References](#references)


## The INCAR file\[<a
href="/wiki/index.php?title=Stochastic_LTMP2&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: The INCAR file">edit</a> \| (./index.php.md)\]

The LTMP2 calculation can simply be performed using the following
[INCAR](../input-files/INCAR.md) file

    ALGO = ACFDTRK 
    LSMP2LT = .TRUE.
    ESTOP = # accuracy of energy per tau-point
    NSTORB = # number of stochastic orbitals per cycle
    NOMEGA = # number of tau-points (see below)
    NBANDS = # same valule as in the Hartree-Fock unoccupieds step ( = number of plane-waves)
    ENCUT = # same value as in the Hartree-Fock step
    LORBITALREAL = .TRUE.
    PRECFOCK = Fast

Make sure that VASP reads the WAVECAR file from the <a
href="/wiki/MP2_ground_state_calculation#Calculating_the_unoccupied_Hartree-Fock_orbitals"
class="mw-redirect" title="MP2 ground state calculation">Hartree-Fock
virtuals</a> step. The setting for [PRECFOCK](../incar-tags/PRECFOCK.md)
is strongly recommended, since the code heavily relies on real space
grid FFTs.

#### NOMEGA flag\[<a
href="/wiki/index.php?title=Stochastic_LTMP2&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: NOMEGA flag">edit</a> \| (./index.php.md)\]

The number of $\tau$-points
is controlled by the NOMEGA flag. This is necessary to calculate the
Laplace transformed energy denominator (see Ref
[^schaefer2018-1]
for details),

$\frac{1}{\varepsilon_i + \varepsilon_j - \varepsilon_a -\varepsilon_b}
= - \int_0^\infty \textrm e^{-(\varepsilon_i + \varepsilon_j -
\varepsilon_a -\varepsilon_b)\tau} \\ \textrm d \tau \\.$

Usually it is sufficient to set NOMEGA to 6. For materials with a small
bandgap it is worth checking if the MP2 energy changes with increasing
NOMEGA (e.g. 8 or 10). Note, that the MP2 energy diverges with
1/bandgap, independent of NOMEGA.

#### ESTOP flag\[<a
href="/wiki/index.php?title=Stochastic_LTMP2&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: ESTOP flag">edit</a> \| (./index.php.md)\]

This flag defines the stop condition for the stochastic algorithm. It
defines the energy accuracy in units of eV for each individual tau-point
of the two individual MP2 energy contributions (direct MP2 term +
exchange MP2 term). Since the statistical errors of each contribution is
independent, the standard deviation of the MP2 energy can be estimated
as

$\sigma = \texttt{ESTOP} \* \sqrt{2 \cdot \texttt{NOMEGA}} \\.$

According to our experience, the error of the resulting MP2 energy can
then be safely estimated by $\pm 2 \sigma$.

Thus, if you require an MP2 energy with a maximum error of
$\Delta$, you should set

$\texttt{ESTOP} = \frac{\Delta}{2 \cdot \sqrt{2 \cdot \texttt{NOMEGA}}}
\\.$

#### NSTORB flag\[<a
href="/wiki/index.php?title=Stochastic_LTMP2&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: NSTORB flag">edit</a> \| (./index.php.md)\]

This flag defines the number of stochastic orbitals per cycle, i.e. the
number of stochastic orbitals that define one stochastic sample. If the
sample is not large enough, the calculations is repeated until the
accuracy, defined by ESTOP, is reached.

As a rule of thumb we recommend to set

$\texttt{NSTORB} = \sqrt{\texttt{NBANDS}} \\.$

## Parallelization\[<a
href="/wiki/index.php?title=Stochastic_LTMP2&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Parallelization">edit</a> \| (./index.php.md)\]

The stochastic LTMP2 algorithm supports parallelization with MPI and
OpenMP (OMP). The optimal setting is to set the number of MPI ranks as
well as the **KPAR** flag to the number of cores (#cores), i.e. start
VASP using

    mpirun -np #cores vasp

and write

    KPAR = #cores

in the [INCAR](../input-files/INCAR.md) file. With this setting the entire
set of Hartree-Fock orbitals (WAVECAR) is available on each MPI rank,
which is necessary to calculate stochastic samples independently. Note,
that **KPAR** is only used to control the distribution of the orbitals
and has nothing to do with **k**-point parallelization here.

However, for very large systems (large WAVECAR files) the available
storage per MPI rank could be insufficient to store the entire set of
orbitals. In this case, simply decrease the **KPAR**. Note that the
available memory for the orbitals can be calculated by (memory per MPI
rank) \* (number of MPI ranks) / KPAR. For example, if your WAVECAR file
has 17 GB you need 2\*17 GB = 34 GB of memory to distribute the orbitals
(the factor 2 is due to double precision). If want to use 64 cores with
4 GB per core and 64 MPI ranks, you have to set **KPAR** = 4. In this
case the orbitals are distributed over 64/4 = 16 MPI ranks. Each MPI
rank will still be able to perform independent stochastic calculations,
however, a bit more MPI communication is necessary.

It is also possible to increase the memory per MPI rank using shared
memory with OMP. This is a viable option if your available memory per
core is too small, decreasing **KPAR** does not help or you don't want
to set too small **KPAR** values. However, in general, it is recommended
to solve memory issues with the **KPAR** flag first.

## References\[<a
href="/wiki/index.php?title=Stochastic_LTMP2&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^schaefer2018-1]: [T. Schäfer, B. Ramberger, and G. Kresse, J. Chem. Phys. 148, 064103 (2018).](https://doi.org/10.1063/1.5016100)
