<!-- Source: https://vasp.at/wiki/index.php/Delta_Self-Consistent_Field | revid: 31982 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Delta Self-Consistent Field
$\Delta$SCF is a method that allows to
calculate energies of neutral excitation within DFT by constraining
occupations. Within the Franck-Condon approximation, the electronic
excitation is much faster than the nuclear motion. Thus,
$\Delta$SCF can be used for calculating
excited-state properties such as vertical absorption (VAE) and vertical
emission energy (VEE). Furthermore, this method can be used to calculate
the zero-phonon lines (ZPL) by performing a full atomic relaxation in
the excited-state configuration and thus account for the Stockes shifts.
This method is commonly used for calculating the [optical
properties](../categories/Category-Dielectric_properties.md)
of point defects in semiconductors and insulators
^([\[1\]](#cite_note-Freysoldt2014-1)).

## Contents

- [1 Vertical absorption energies
  (VAE)](#Vertical_absorption_energies_(VAE))
- [2 Zero-phonon lines (ZPL)](#Zero-phonon_lines_(ZPL))
- [3 Vertical emission energies
  (VEE)](#Vertical_emission_energies_(VEE))
- [4 Electronic minimization with constrained electronic
  occupation](#Electronic_minimization_with_constrained_electronic_occupation)
- [5 Example: ZPL of $\mathrm{NV}^-$
  center in
  diamond](#Example:_ZPL_of_%5Bmath%5D\displaystyle%7B_\mathrm%7BNV%7D%5E-_%7D%5B/math%5D_center_in_diamond)
  - [5.1 Step 1](#Step_1)
  - [5.2 Step 2](#Step_2)
  - [5.3 Step 3](#Step_3)
- [6 Related tags and articles](#Related_tags_and_articles)
- [7 References](#References)

## Vertical absorption energies (VAE)
[![](https://vasp.at/wiki/images/thumb/b/b8/Drawing.png/300px-Drawing.png)](https://vasp.at/wiki/File:Drawing.png)

Schematic representation of the excitation energies.

The VAE can be calculated by performing a full SCF calculation of the
system in its excited-state configuration following three steps:

1.  Perform a [ground-state
    calculation](../tutorials/Setting_up_an_electronic_minimization.md)
    to obtain the total energy of the system in its ground-state
    configuration, $E_{gs}$.
2.  Perform a full [SCF calculation with constrained electronic
    occupancies](#Electronic_minimization_with_constrained_electronic_occupation)
    to obtain the total energy of the system in its excited-state
    configuration, $E_{ex}$.
3.  The VAE is then given by the difference between the total energies
    of the excited and ground states: $\mathrm{VAE} = E_{ex} - E_{gs}.$

## Zero-phonon lines (ZPL)
The ZPL calculation requires performing a full atomic relaxation in the
excited state configuration. The ZPL calculation can be performed in
three steps:

1.  Perform a [ground-state
    calculation](../tutorials/Setting_up_an_electronic_minimization.md)
    to obtain the total energy of the system in its ground-state
    configuration, $E_{gs}$.
2.  Set up a [constrained occupation
    calculation](#Electronic_minimization_with_constrained_electronic_occupation)
    and perform a full [atomic
    relaxation](../tutorials/Structure_optimization.md)
    to obtain the total energy of the system in its excited-state
    configuration at relaxed atomic positions, $E_{ex}^\*$
3.  The ZPL is then given by the difference between the total energies
    of the relaxed excited and ground states: $\mathrm{ZPL} = E_{ex}^\* - E_{gs}$

## Vertical emission energies (VEE)
The VEE calculation can be performed in three steps:

1.  Set up a [constrained occupation
    calculation](#Electronic_minimization_with_constrained_electronic_occupation)
    to represent the excited state and perform a full [atomic
    relaxation](../tutorials/Structure_optimization.md)
    of the excited state to obtain the total energy
    $E_{ex}^\*$.
2.  Remove the occupation constraints and perform a full [SCF
    calculation](../tutorials/Setting_up_an_electronic_minimization.md)
    to obtain the total energy of the system in this atomic
    configuration, $E_{gs}^\*$.
3.  The VEE is then given by the difference between the total energies
    of the excited state and the ground state: $\mathrm{VEE} = E_{ex}^\* - E_{gs}^\*.$

## Electronic minimization with constrained electronic occupation
[![](https://vasp.at/wiki/images/thumb/1/1a/Diagram_delta_scf.png/200px-Diagram_delta_scf.png)](https://vasp.at/wiki/File:Diagram_delta_scf.png)

Scheme of how states order might change upon SCF calculation of the
excited state.

Identify the band index of the states involved in the excitation based
on a ground-state calculation. Then, set the [occupations of the
Kohn-Sham
states](../categories/Category-Electronic_occupancy.md)
to represent the excited state via [FERWE](../incar-tags/FERWE.md) and
[FERDO](../incar-tags/FERDO.md) tags.

When constraining the electronic occupancies, it is important to ensure
that the order of the states is preserved throughout the calculation.
This can be achieved by setting [LDIAG](../incar-tags/LDIAG.md)=.FALSE. in
[ALGO](../incar-tags/ALGO.md)=Damped or [ALGO](../incar-tags/ALGO.md)=All.

To improve convergence, it is recommended to restart the calculation
from the converged [WAVECAR](../input-files/WAVECAR.md) file of a
preceding calculation without constraints.

|  |
|----|
| **Mind:** [ALGO](../incar-tags/ALGO.md)=Normal, Fast, VeryFast are not recommended for constrained occupation calculations as they may lead to state reordering. |

|  |
|----|
| **Warning:** In versions of VASP between VASP 5.4.1 and VASP 6.4, the [LDIAG](../incar-tags/LDIAG.md)=.FALSE. was broken and did not preserve the order of states between ionic iterations. |

## Example: ZPL of $\mathrm{NV}^-$ center in diamond
[![](https://vasp.at/wiki/images/thumb/7/71/Diamond_nv.png/200px-Diamond_nv.png)](https://vasp.at/wiki/File:Diamond_nv.png)

$\mathrm{NV}^-$ center in 64-atom
diamond supercell.

We consider a negatively charged point defect in diamond, so-called
$\mathrm{NV}^-$, which consists of an N
substitution and a vacancy. This is a well-studied point defect in
diamond, which can be used here for illustrating the principle of the
ZPL calculations ^([\[2\]](#cite_note-Lofgren2018-2)). In this example,
we consider a single $\mathrm{NV}^-$ in
a 64-atom supercell.

### Step 1
Perform a full [atomic
relaxation](../tutorials/Structure_optimization.md) of
the $\mathrm{NV}^-$ center in its ground
state. Identify the band index of the states involved in the excitation.

                Spin up                             Spin down
       ...
       124       8.8280      1.00000         124       8.9642      1.00000
       125       8.8280      1.00000         125       8.9642      1.00000
       126      10.1514      1.00000         126      10.5683      1.00000
       127      11.1936      1.00000         127      12.4369      0.00000
       128      11.1936      1.00000         128      12.4369      0.00000
       129      13.6991      0.00000         129      13.7261      0.00000
       ...

To simulate the excitation, we promote an electron from the highest
occupied state in the spin-down channel (126) to the lowest unoccupied
state in the same channel (127). Thus, we need to provide the following
occupations:

    FERWE = 128*1 64*0
    FERDO = 125*1 1*0 1*1 65*0

Here, the first number is a multiplicity and the second number is the
occupation, e.g., 128\*1 means that the first 128 states are fully
occupied. The occupations must be provided for all
[NBANDS](../incar-tags/NBANDS.md) and all k-points. Thus, for a 4x4x4
k-point mesh with 13 k-points in IBZ, we have:

    FERWE = 128*1 64*0 128*1 64*0 128*1 64*0 128*1 64*0  \
            128*1 64*0 128*1 64*0 128*1 64*0 128*1 64*0  \
            128*1 64*0 128*1 64*0 128*1 64*0 128*1 64*0  \
            128*1 64*0
    FERDO = 125*1 1*0 1*1 65*0 125*1 1*0 1*1 65*0 125*1 1*0 1*1 65*0 125*1 1*0 1*1 65*0  \
            125*1 1*0 1*1 65*0 125*1 1*0 1*1 65*0 125*1 1*0 1*1 65*0 125*1 1*0 1*1 65*0  \
            125*1 1*0 1*1 65*0 125*1 1*0 1*1 65*0 125*1 1*0 1*1 65*0 125*1 1*0 1*1 65*0  \
            125*1 1*0 1*1 65*0

### Step 2
Perform a full SCF calculation with the above occupations to obtain the
total energy of the system in its excited-state configuration,
$E_{ex}$. Make sure that the correct
excited state is preserved throughout the calculation.

                 Spin up                             Spin down
        ...
        124       8.8622      1.00000         124       8.9647      1.00000
        125       8.8622      1.00000         125       8.9647      1.00000
        126       9.9201      1.00000         126      10.4995      0.00000
        127      11.4574      1.00000         127      12.4388      1.00000
        128      11.4574      1.00000         128      12.4388      0.00000
        129      13.6252      0.00000         129      13.6705      0.00000
        ...

By subtracting the ground-state energy from the excited state, we find
the VAE of 1.77 eV.

### Step 3
To calculate ZPL, perform a full [atomic
relaxation](../tutorials/Structure_optimization.md) of
this excited state. After the convergence was achieved, make sure that
the excited state was preserved and the converged configuration is
correct.

                 Spin up                             Spin down
        ...
        124       8.8276      1.00000         124       8.9334      1.00000
        125       8.8276      1.00000         125       8.9334      1.00000
        126      10.0760      1.00000         126      10.7072      0.00000
        127      11.3836      1.00000         127      12.3573      1.00000
        128      11.3836      1.00000         128      12.3573      0.00000
        129      13.5935      0.00000         129      13.6348      0.00000
        ...

The total energy difference between the ground state and the excited
state after the ionic relaxation, i.e., ZPL is 1.59 eV.

## Related tags and articles
- [FERWE](../incar-tags/FERWE.md),[FERDO](../incar-tags/FERDO.md)
- [Setting up an electronic
  minimization](../tutorials/Setting_up_an_electronic_minimization.md)
- [Troubleshooting electronic
  convergence](../tutorials/Troubleshooting_electronic_convergence.md)

## References
1.  [↑](#cite_ref-Freysoldt2014_1-0) [Christoph Freysoldt, Blazej
    Grabowski, Tilmann Hickel, Jörg Neugebauer, Georg Kresse, and
    Anderson Janotti, Rev. Mod. Phys.
    (2014).](http://dx.doi.org/10.1103/RevModPhys.86.253)
2.  [↑](#cite_ref-Lofgren2018_2-0) [R. Löfgren, R. Pawar, and S. Öberg,
    New J. Phys. (2018).](http://dx.doi.org/10.1088/1367-2630/aaa382)
