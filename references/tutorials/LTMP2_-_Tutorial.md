<!-- Source: https://vasp.at/wiki/index.php/LTMP2_-_Tutorial | revid: 18020 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LTMP2 - Tutorial



[Overview](MP2_ground_state_calculation_-_Tutorial.md) \>
[MP2](../incar-tags/MP2.md) \>
LTMP2 \>
[stochastic LTMP2](../theory/Stochastic_LTMP2.md)
 \> <a
href="/wiki/index.php?title=High_energy_contributions_using_stochastic_LTMP2&amp;action=edit&amp;redlink=1"
class="new"
title="High energy contributions using stochastic LTMP2 (page does not exist)">High
energy contributions using stochastic LTMP2</a> \>
[List of tutorials](../categories/Category-Tutorials.md)


On this page, we explain how to perform a calculation using the
**LTMP2**<sup>[\[1\]](#cite_note-schaefer2017-1)</sup>
algorithm. Make sure you successfully completed the preparation steps <a
href="/wiki/MP2_ground_state_calculation#Preparation:_the_Hartree-Fock_ground_state"
class="mw-redirect" title="MP2 ground state calculation">Hartree-Fock
ground state</a> and <a
href="/wiki/MP2_ground_state_calculation#Calculating_the_unoccupied_Hartree-Fock_orbitals"
class="mw-redirect" title="MP2 ground state calculation">Hartree-Fock
virtuals</a>.

**NOTE:** *If you use this algorithm, please cite reference
<sup>[\[1\]](#cite_note-schaefer2017-1)</sup>
in your publication in addition to the standard VASP reference.*


## Contents


- [1 The INCAR
  file](#the-incar-file)
  - [1.1 NOMEGA
    flag](#nomega-flag)
- [2
  Parallelization](#parallelization)
  - [2.1 Example
    for 512 CPUs](#example-for-512-cpus)
- [3
  References](#references)


## The INCAR file\[<a
href="/wiki/index.php?title=LTMP2_-_Tutorial&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: The INCAR file">edit</a> \| (./index.php.md)\]

The LTMP2 calculation can simply be performed using the following
[INCAR](../input-files/INCAR.md) file

    ALGO = ACFDTRK 
    LMP2LT = .TRUE.
    NOMEGA = # number of tau points (see below)
    NBANDS = # same value as in the Hartree-Fock unoccupied step ( = number of plane-waves)
    ENCUT = # same value as in the Hartree-Fock step
    LORBITALREAL = .TRUE.
    PRECFOCK = Fast
    KPAR = # parallelization (see below)

Make sure that VASP reads the WAVECAR file from the <a
href="/wiki/MP2_ground_state_calculation#Calculating_the_unoccupied_Hartree-Fock_orbitals"
class="mw-redirect" title="MP2 ground state calculation">Hartree-Fock
virtuals</a> step. The setting for [PRECFOCK](../incar-tags/PRECFOCK.md)
is strongly recommended, since the code heavily relies on real space
grid FFTs.

#### NOMEGA flag\[<a
href="/wiki/index.php?title=LTMP2_-_Tutorial&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: NOMEGA flag">edit</a> \| (./index.php.md)\]

The number of $\tau$-points
is controlled by the NOMEGA flag. This is necessary to calculate the
Laplace transformed energy denominator (see Ref
<sup>[\[1\]](#cite_note-schaefer2017-1)</sup>
for details),

$\frac{1}{\varepsilon_i + \varepsilon_j - \varepsilon_a -\varepsilon_b}
= - \int_0^\infty \textrm e^{-(\varepsilon_i + \varepsilon_j -
\varepsilon_a -\varepsilon_b)\tau} \\ \textrm d \tau \\.$

Usually it is sufficient to set [NOMEGA](../incar-tags/NOMEGA.md)=6. For
materials with a small bandgap it is worth checking if the MP2 energy
changes with increasing [NOMEGA](../incar-tags/NOMEGA.md) (e.g. 8 or 10).
Note, that the MP2 energy diverges with 1/bandgap, independent of
[NOMEGA](../incar-tags/NOMEGA.md).

## Parallelization\[<a
href="/wiki/index.php?title=LTMP2_-_Tutorial&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Parallelization">edit</a> \| (./index.php.md)\]

The LTMP2 algorithm is a high-performance code and can easily be used on
many CPUs. Both OpenMP and MPI is supported. We recommend to use MPI for
parallelization since the code possesses an almost ideal parallelization
efficiency. OpenMP should only be used to increase the shared memory, if
necessary.

In order to activate the efficient MPI parallelization use the KPAR flag
in the following way (note that the usual meaning of the KPAR flag
becomes obsolete in the LTMP2 algorithm). KPAR specifies the number of
plane-waves treated in parallel. Ideally, set KPAR to half of the used
MPI ranks. If this results in memory issues, further decrease KPAR (such
that KPAR is alway a divisor of the used MPI ranks) or increase the
number of OpenMP threads.

#### Example for 512 CPUs\[<a
href="/wiki/index.php?title=LTMP2_-_Tutorial&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Example for 512 CPUs">edit</a> \| (./index.php.md)\]

MPI ranks: 512  
OpenMP threads per rank: 1  

    KPAR = 256

To decrease the memory requirement you can alternatively set KPAR to 128
or 64 and so on. Or also try  
MPI ranks: 256  
OpenMP threads per rank: 2  

    KPAR = 128

## References\[<a
href="/wiki/index.php?title=LTMP2_-_Tutorial&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-schaefer2017_1-0)</sup>
    <sup>[b](#cite_ref-schaefer2017_1-1)</sup>
    <sup>[c](#cite_ref-schaefer2017_1-2)</sup>
    <a href="http://dx.doi.org/10.1063/1.4976937" class="external text"
    rel="nofollow">T. Schäfer, B. Ramberger, and G. Kresse, J. Chem. Phys.
    146, 104101 (2017).</a>


------------------------------------------------------------------------


