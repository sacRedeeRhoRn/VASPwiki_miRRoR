<!-- Source: https://vasp.at/wiki/index.php/MP2_ground_state_calculation_-_Tutorial | revid: 35758 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# MP2 ground state calculation - Tutorial



Overview \>
[MP2](../incar-tags/MP2.md) \>
[LTMP2](LTMP2_-_Tutorial.md) \>
[stochastic LTMP2](../theory/Stochastic_LTMP2.md)
 \> <a
href="/wiki/index.php?title=High_energy_contributions_using_stochastic_LTMP2&amp;action=edit&amp;redlink=1"
class="new"
title="High energy contributions using stochastic LTMP2 (page does not exist)">High
energy contributions using stochastic LTMP2</a> \>
[List of tutorials](../categories/Category-Tutorials.md)


This tutorial introduces how to calculate the ground state energy using
second order Møller-Plesset perturbation theory (MP2) with VASP.
Currently there are three implementations available:

- **MP2**<sup>[\[1\]](#cite_note-marsman-1)</sup>:
  this implementation is recommended for very small unit cells, very few
  k-points and very low plane-wave cuttofs. The system size scaling of
  this algorithm is N⁵.
- **LTMP2**<sup>[\[2\]](#cite_note-schaefer2017-2)</sup>:
  for all larger systems this Laplace transformed MP2 (LTMP)
  implementation is recommended. Larger cutoffs and denser k-point
  meshes can be used. It possesses a lower system size scaling (N⁴) and
  a more efficient k-point sampling.
- **stochastic
  LTMP2**<sup>[\[3\]](#cite_note-schaefer2018-3)</sup>:
  even faster calculations at the price of statistical noise can be
  achieved with the stochastic MP2 algorithm. It is an optimal choice
  for very large systems where only relative errors per valence electron
  are relevant. Keeping the absolute error fixed, the algorithm exhibits
  a cubic scaling with the system size, N³, whereas for a fixed relative
  error, a linear scaling, N¹, can be achieved. Note that there is no
  k-point sampling and no spin polarization implemented for this
  algorithm.

**NOTE:** *If you use one of these algorithms, please cite the
corresponding reference in your publication in addition to the standard
VASP reference.*

Both LTMP2 as well as stochastic LTMP2 are high performance algorithms
that can parallelize the MP2 calculation over thousands of CPUs.

At first, one should select the best algorithm according to the
considered system size. In the following, a step by step instruction for
each algorithm is presented.


## Contents


- [1 Preparation:
  the Hartree-Fock ground
  state](#Preparation:_the_Hartree-Fock_ground_state)
- [2 Calculating
  the unoccupied Hartree-Fock
  orbitals](#Calculating_the_unoccupied_Hartree-Fock_orbitals)
- [3 Actual MP2
  calculations](#Actual_MP2_calculations)
- [4
  References](#References)


## Preparation: the Hartree-Fock ground state\[<a
href="/wiki/index.php?title=MP2_ground_state_calculation_-_Tutorial&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Preparation: the Hartree-Fock ground state">edit</a> \| (./index.php.md)\]

In order to calculate the Hartree-Fock ground state, use the following
[INCAR](../input-files/INCAR.md) file

    ISMEAR = 0 ; SIGMA = 0.01
    ALGO = A
    LHFCALC = .TRUE. ; AEXX = 1.0
    EDIFF = 1E-6
    ENCUT = # 10-20% larger than ENMAX in the POTCAR file
    LORBITALREAL = .TRUE. # only necessary for LTMP2 and stochastic LTMP2

Keep the [OUTCAR](../output-files/OUTCAR.md) file to read-out the
Hartree-Fock ground state energy later.

## Calculating the unoccupied Hartree-Fock orbitals\[<a
href="/wiki/index.php?title=MP2_ground_state_calculation_-_Tutorial&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Calculating the unoccupied Hartree-Fock orbitals">edit</a> \| (./index.php.md)\]

We also need the unoccupied/virtual Hartree-Fock orbitals to perform MP2
calculations. The number of necessary orbitals should be equal to the
number of plane-waves, that can be found via

    nplw=`awk '/number of plane-waves:/ {print $5} ' < OUTCAR_HARTREE_FOCK_GROUND_STATE

For the Gamma-only version of VASP, twice the number of plane-waves have
to be used.

Set the INCAR file to

    ISMEAR = 0 ; SIGMA = 0.01
    ALGO = Exact
    LHFCALC = .TRUE. ; AEXX = 1.0
    NELM = 1
    NBANDS = # number of plane-waves (favorably a multiple of the used mpi-ranks)
    ENCUT = # same value as in the Hartree-Fock step
    LORBITALREAL = .TRUE. # only necessary for LTMP2 and stochastic LTMP2

Make sure that VASP reads the [WAVECAR](../input-files/WAVECAR.md) file
from the previous Hartree-Fock step.

## Actual MP2 calculations\[<a
href="/wiki/index.php?title=MP2_ground_state_calculation_-_Tutorial&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Actual MP2 calculations">edit</a> \| (./index.php.md)\]

Depending on your choice, please switch to the corresponding page.


1.  [MP2](../incar-tags/MP2.md)
2.  <a href="/wiki/LTMP2" class="mw-redirect" title="LTMP2">LTMP2</a>
3.  [stochastic LTMP2](../theory/Stochastic_LTMP2.md)


## References\[<a
href="/wiki/index.php?title=MP2_ground_state_calculation_-_Tutorial&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-marsman_1-0)
    <a href="http://dx.doi.org/10.1063/1.3126249" class="external text"
    rel="nofollow">M. Marsman, A. Grüneis, J. Paier, and G. Kresse, J. Chem.
    Phys. 130, 184103 (2009).</a>
2.  [↑](#cite_ref-schaefer2017_2-0)
    <a href="http://dx.doi.org/10.1063/1.4976937" class="external text"
    rel="nofollow">T. Schäfer, B. Ramberger, and G. Kresse, J. Chem. Phys.
    146, 104101 (2017).</a>
3.  [↑](#cite_ref-schaefer2018_3-0)
    <a href="https://doi.org/10.1063/1.5016100" class="external text"
    rel="nofollow">T. Schäfer, B. Ramberger, and G. Kresse, J. Chem. Phys.
    148, 064103 (2018).</a>


------------------------------------------------------------------------


