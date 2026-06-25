<!-- Source: https://vasp.at/wiki/index.php/Liquid_Si_-_Standard_MD | revid: 32321 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Liquid Si - Standard MD



[Overview](../tutorials/Molecular_dynamics_-_Tutorial.md) \>Liquid
Si - Standard MD \>
[Liquid Si -
Freezing](Liquid_Si_-_Freezing.md) \>
[Nucleophile Substitution CH3Cl - Standard
MD](Nucleophile_Substitution_CH3Cl_-_Standard_MD.md) \>
[Nuclephile Substitution CH3Cl -
mMD1](Nuclephile_Substitution_CH3Cl_-_mMD1.md) \>
[Nuclephile Substitution CH3Cl -
mMD2](Nuclephile_Substitution_CH3Cl_-_mMD2.md) \>
[Nuclephile Substitution CH3Cl -
mMD3](Nuclephile_Substitution_CH3Cl_-_mMD3.md) \>
[Nuclephile Substitution CH3Cl -
SG](Nuclephile_Substitution_CH3Cl_-_SG.md) \>
[Nuclephile Substitution CH3Cl -
BM](Nuclephile_Substitution_CH3Cl_-_BM.md) \>
[List of tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#Task)
- [2
  Input](#Input)
  - [2.1
    POSCAR](#POSCAR)
  - [2.2
    KPOINTS](#KPOINTS)
  - [2.3
    INCAR](#INCAR)
- [3
  Calculation](#Calculation)
  - [3.1 150
    fs](#150_fs)
  - [3.2 300
    fs](#300_fs)
  - [3.3 Further
    continuation](#Further_continuation)
  - [3.4
    Microcanonical
    ensemble](#Microcanonical_ensemble)
  - [3.5 Further
    things to try](#Further_things_to_try)
- [4
  Download](#Download)


## Task\[<a
href="/wiki/index.php?title=Liquid_Si_-_Standard_MD&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Generating liquid Si by melting of the crystalline structure via
molecular dynamics.

## Input\[<a
href="/wiki/index.php?title=Liquid_Si_-_Standard_MD&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Liquid_Si_-_Standard_MD&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

- We start this example by making a [POSCAR](../input-files/POSCAR.md)
  using the conventional unit cell with 8 atoms which should look like
  this:

<!-- -->

    Si cubic diamond conventional cell
      5.43100000000000
     1.00000000 0.00000000 0.00000000
     0.00000000 1.00000000 0.00000000
     0.00000000 0.00000000 1.00000000
      Si
      8
    Direct
      0.00000000 0.00000000 0.00000000
      0.75000000 0.25000000 0.75000000
      0.00000000 0.50000000 0.50000000
      0.75000000 0.75000000 0.25000000
      0.50000000 0.00000000 0.50000000
      0.25000000 0.25000000 0.25000000
      0.50000000 0.50000000 0.00000000
      0.25000000 0.75000000 0.75000000

  

- We obtain a sufficiently large supercell (2x2x2 containing 64 atoms)
  by following the description in: [Preparing a Super
  Cell](../tutorials/Preparing_a_Super_Cell.md).
- The new [POSCAR](../input-files/POSCAR.md) file of the two 2x2x2 super
  cell of the conventional cell should look like this:

<!-- -->

    Si cubic diamond 2x2x2 super cell of conventional cell
         5.43090000000000
        2.00000000   0.00000000   0.00000000
        0.00000000   2.00000000   0.00000000
        0.00000000   0.00000000   2.00000000
       Si
       64
    Direct
       0.00000000   0.00000000   0.00000000
       0.50000000   0.00000000   0.00000000
       0.00000000   0.50000000   0.00000000
       0.50000000   0.50000000   0.00000000
       0.00000000   0.00000000   0.50000000
       0.50000000   0.00000000   0.50000000
       0.00000000   0.50000000   0.50000000
       0.50000000   0.50000000   0.50000000
       0.37500000   0.12500000   0.37500000
       0.87500000   0.12500000   0.37500000
       0.37500000   0.62500000   0.37500000
       0.87500000   0.62500000   0.37500000
       0.37500000   0.12500000   0.87500000
       0.87500000   0.12500000   0.87500000
       0.37500000   0.62500000   0.87500000
       0.87500000   0.62500000   0.87500000
       0.00000000   0.25000000   0.25000000
       0.50000000   0.25000000   0.25000000
       0.00000000   0.75000000   0.25000000
       0.50000000   0.75000000   0.25000000
       0.00000000   0.25000000   0.75000000
       0.50000000   0.25000000   0.75000000
       0.00000000   0.75000000   0.75000000
       0.50000000   0.75000000   0.75000000
       0.37500000   0.37500000   0.12500000
       0.87500000   0.37500000   0.12500000
       0.37500000   0.87500000   0.12500000
       0.87500000   0.87500000   0.12500000
       0.37500000   0.37500000   0.62500000
       0.87500000   0.37500000   0.62500000
       0.37500000   0.87500000   0.62500000
       0.87500000   0.87500000   0.62500000
       0.25000000   0.00000000   0.25000000
       0.75000000   0.00000000   0.25000000
       0.25000000   0.50000000   0.25000000
       0.75000000   0.50000000   0.25000000
       0.25000000   0.00000000   0.75000000
       0.75000000   0.00000000   0.75000000 
       0.25000000   0.50000000   0.75000000
       0.75000000   0.50000000   0.75000000
       0.12500000   0.12500000   0.12500000
       0.62500000   0.12500000   0.12500000
       0.12500000   0.62500000   0.12500000
       0.62500000   0.62500000   0.12500000
       0.12500000   0.12500000   0.62500000
       0.62500000   0.12500000   0.62500000
       0.12500000   0.62500000   0.62500000
       0.62500000   0.62500000   0.62500000
       0.25000000   0.25000000   0.00000000
       0.75000000   0.25000000   0.00000000
       0.25000000   0.75000000   0.00000000
       0.75000000   0.75000000   0.00000000
       0.25000000   0.25000000   0.50000000
       0.75000000   0.25000000   0.50000000
       0.25000000   0.75000000   0.50000000
       0.75000000   0.75000000   0.50000000
       0.12500000   0.37500000   0.37500000
       0.62500000   0.37500000   0.37500000
       0.12500000   0.87500000   0.37500000
       0.62500000   0.87500000   0.37500000
       0.12500000   0.37500000   0.87500000
       0.62500000   0.37500000   0.87500000
       0.12500000   0.87500000   0.87500000
       0.62500000   0.87500000   0.87500000

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Liquid_Si_-_Standard_MD&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    K-Points
     0
    Gamma
     1  1  1
     0  0  0

- Since a sufficiently large super cell is used in this example, it is
  ok in this case to use only a single k-point in the calculations.
  Hence it is also possible to use the $\Gamma$-point only version which is significantly faster
  than the standard version.

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Liquid_Si_-_Standard_MD&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    ISMEAR = 0
    IBRION = 0
    MDALGO = 2
    ISIF = 2
    SMASS = 1.0
    SIGMA = 0.1
    LREAL = Auto
    ALGO = VeryFast
    PREC = Low
    ISYM = 0
    TEBEG = 2000
    NSW = 50
    POTIM = 3.0
    NCORE = 2

- To select a molecular dynamics calculation set
  [IBRION](../incar-tags/IBRION.md)=0.
- By selecting [MDALGO](../incar-tags/MDALGO.md)=2 and
  [ISIF](../incar-tags/ISIF.md)=2 we select the [NVT
  ensemble](NVT_ensemble.md) using the [Nosé-Hoover
  thermostat](../tutorials/Nosé-Hoover_thermostat.md).
- The tag [SMASS](../incar-tags/SMASS.md) specifies the Nosé mass, which is
  a fictitious mass for the fictional coordinate of the heat bath. The
  choice of
  [SMASS](../incar-tags/SMASS.md)=1.0
  should work well for this tutorial.
- Since we are dealing with a super cell, we set
  [LREAL](../incar-tags/LREAL.md)=Auto.
  In this mode the projection operators are evaluated in real space.
  This should speed up the calculation while being slightly less
  accurate then the evaluation of the operators in reciprocal space.
- To significantly speed up the calculations we use
  [ALGO](../incar-tags/ALGO.md)=*VeryFast*
  and
  [PREC](../incar-tags/PREC.md)=*Low*.
  This is ok for this tutorial example but for more precise results
  these flags should be used with caution!
- A time step of 3 femtoseconds
  ([POTIM](../incar-tags/POTIM.md)=3.0)
  is employed in this example, which should be ok for many applications
  of Si.
- The tag [NCORE](../incar-tags/NCORE.md)=2 specifies that the
  parallelization is done such that 2 cores share the work on one
  orbital. This means that for e.g. 8 cores 4 different orbitals would
  be treated simultaneously, where for each orbital two plane-wave
  coefficients would be calculated simultaneously.

## Calculation\[<a
href="/wiki/index.php?title=Liquid_Si_-_Standard_MD&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

The calculation is started from the perfect crystal. Since the chosen
temperature at 2000K is significantly above the known melting
temperature at around 1400 K the melting should be achieved relatively
quickly.

It is suggested to run this calculation using the
$\Gamma$-point only version, since we have only one k
point. Then it should be a very quick calculation on eight nodes:

    mpirun -np 8 vasp_path/vasp_gam

When the solid melts the crystal structure and the distances between the
atoms change. This can be well monitored by looking at the pair
correlation function (or radial distribution function). We will also
monitor the energy conservation to see if we are well equilibrated.

### 150 fs\[<a
href="/wiki/index.php?title=Liquid_Si_-_Standard_MD&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: 150 fs">edit</a> \| (./index.php.md)\]

First we run the calculation for 150 fs.

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:PC_150fs.jpeg" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/e/e5/PC_150fs.jpeg/300px-PC_150fs.jpeg"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/e/e5/PC_150fs.jpeg/450px-PC_150fs.jpeg 1.5x, /wiki/images/thumb/e/e5/PC_150fs.jpeg/600px-PC_150fs.jpeg 2x"
width="300" height="225" /></a>
<figcaption>Fig. 1: Pair correlation function after 150 fs.</figcaption>
</figure>

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Energy_150fs.jpg" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/d/d1/Energy_150fs.jpg/300px-Energy_150fs.jpg"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/d/d1/Energy_150fs.jpg/450px-Energy_150fs.jpg 1.5x, /wiki/images/thumb/d/d1/Energy_150fs.jpg/600px-Energy_150fs.jpg 2x"
width="300" height="225" /></a>
<figcaption>Fig. 2: Total energy vs number of steps in first 150
fs.</figcaption>
</figure>

- Pair correlation function:

The pair correlation function is written out to the
[PCDAT](../output-files/PCDAT.md) file. The abscissa of that file is within
mesh points of a selected grid and need to be converted to
$\AA$. This is done by invoking the following short awk
script on the command line:

    awk <PCDAT >PCDAT.150fs ' NR==8 {pcskal=$1} NR==9 {pcfein=$1} NR>=13 {line=line+1; print (line-0.5)*pcfein/pcskal,$1} '

This produces the file PCDAT.150fs which contains the pair correlation
function against the radius in Angstrom after the first 150 fs (50
timesteps [NSW](../incar-tags/NSW.md)=50 with a stepsize of 3 fs
[POTIM](../incar-tags/POTIM.md)=3). Now we will plot the pair correlation
function in the gnuplot window:

    gnuplot -e "set xlabel 'r(Ang)'; set ylabel 'PCF'; set style data lines; plot 'PCDAT.150fs'; pause -1"

or to a file (in the remainder we just show how to plot to a file):

    gnuplot -e "set terminal jpeg; set xlabel 'r(Ang)'; set ylabel 'PCF'; set style data lines; plot 'PCDAT.150fs'" > PC_150fs.jpg

The obtained pair correlation function should look like in Fig. 1.
Solids usually show sharp peaks in the pair correlation function since
the ions only vibrate around fixed positions in the crystal lattice. In
the liquid or amorphous state the distances are much more diffuse and
one usually would expect no far order (but both can have near order). We
see that many sharp peaks arise in the pair correlation function at
higher distances, so that after 150 fs we have not molten the material.

  

- Energy conservation:

We will also output the total energy for each molecular dynamics step by
invoking the command:

    grep "free  energy" OUTCAR|awk ' {print $5}' > energy.dat

We will now plot the energy using gnuplot (the user can of course use
the plotting program of choice):

    gnuplot -e "set terminal jpeg; set xlabel 'N_{step}'; set ylabel 'Total energy (eV/cell)';set style data lines; plot 'energy.dat'" > energy_150fs.jpg

The progression of the total energy with respect to the length of the
simulation is shown in Fig. 2. We see that the energy changes very
strongly indicating very large changes in the structures. Of course this
is related to the melting and it is fine.

### 300 fs\[<a
href="/wiki/index.php?title=Liquid_Si_-_Standard_MD&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: 300 fs">edit</a> \| (./index.php.md)\]

We repeat the calculation for another 150 fs.

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:PC_300fs.jpg" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/b/b9/PC_300fs.jpg/300px-PC_300fs.jpg"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/b/b9/PC_300fs.jpg/450px-PC_300fs.jpg 1.5x, /wiki/images/thumb/b/b9/PC_300fs.jpg/600px-PC_300fs.jpg 2x"
width="300" height="225" /></a>
<figcaption>Fig. 3: Pair correlation functions after 300 and 150
fs.</figcaption>
</figure>

Before we run the calculation we need to copy the new positions and
velocities in [CONTCAR](../output-files/CONTCAR.md) to
[POSCAR](../input-files/POSCAR.md). Then rerun the calculation using the
same [INCAR](../input-files/INCAR.md) tags and command as above.

- Pair correlation function:

The pair correlation function after 300 fs is written to the file
PCDAT.300fs (it is evaluated only in the interval of the last 150 fs
since we restarted the calculation):

    awk <PCDAT >PCDAT.300fs ' NR==8 {pcskal=$1} NR==9 {pcfein=$1} NR>=13 {line=line+1; print (line-0.5)*pcfein/pcskal,$1} '

To compare it with the pair correlation function after 150 fs we plot
them using the command:

    gnuplot -e "set terminal jpeg; set xlabel 'r(Ang)'; set ylabel 'PCF'; set style data lines; plot 'PCDAT.150fs', 'PCDAT.300fs' " > PC_300fs.jpg

The pair correlation functions should look like Fig. 3. We see that
after 300 fs much less structure is visible at larger distances. This
indicates that the melting is progressing further, but we need to
continue with the monitoring of the pair correlation function until it
is sufficiently converged.

- Total energy:

We don't look at the total energies here but later. Still the energies
from this calculation need to be concatenated to the "energy.dat" file
(mind the ">>" instead of ">" above):

    grep "free  energy" OUTCAR|awk ' {print $5}' >> energy.dat

### Further continuation\[<a
href="/wiki/index.php?title=Liquid_Si_-_Standard_MD&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Further continuation">edit</a> \| (./index.php.md)\]

We continue the calculation for 450 fs.

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:PC_750fs.jpg" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/b/b4/PC_750fs.jpg/300px-PC_750fs.jpg"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/b/b4/PC_750fs.jpg/450px-PC_750fs.jpg 1.5x, /wiki/images/thumb/b/b4/PC_750fs.jpg/600px-PC_750fs.jpg 2x"
width="300" height="225" /></a>
<figcaption>Fig. 4: Pair correlation functions after 750, 300 and 150
fs.</figcaption>
</figure>

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Energy_750fs.jpg" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/7/74/Energy_750fs.jpg/300px-Energy_750fs.jpg"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/7/74/Energy_750fs.jpg/450px-Energy_750fs.jpg 1.5x, /wiki/images/thumb/7/74/Energy_750fs.jpg/600px-Energy_750fs.jpg 2x"
width="300" height="225" /></a>
<figcaption>Fig. 5: Energy vs number of steps in 750 fs.</figcaption>
</figure>

  
To do that we first set [NSW](../incar-tags/NSW.md)=150 in the
[INCAR](../input-files/INCAR.md) file and copy
[CONTCAR](../output-files/CONTCAR.md) to [POSCAR](../input-files/POSCAR.md).

- Pair correlation function:

We obtain the pair correlation function using the command:

    awk <PCDAT >PCDAT.750fs ' NR==8 {pcskal=$1} NR==9 {pcfein=$1} NR>=13 {line=line+1; print (line-0.5)*pcfein/pcskal,$1} '

We compare the pair correlation functions using the command:

    gnuplot -e "set terminal jpeg; set xlabel 'r(Ang)'; set ylabel 'PCF'; set style data lines; plot 'PCDAT.150fs', 'PCDAT.300fs', 'PCDAT.750fs' " > PC_750fs.jpg

The pair correlation functions should look like Fig. 4. We see that for
750 fs the peak at 4 $\AA$ got
smoothened out compared to 300 fs but the rest of the pair correlation
function didn't change much anymore. This is an indication that the
calculation is converging. In principle we want to have a well
equilibrated structure for a given temperature.

- Total energy:

We will further add the energy data to the *energy.dat* file:

    grep "free  energy" OUTCAR|awk ' {print $5}' >> energy.dat

After that we plot the *energy.dat* file:

    gnuplot -e "set terminal jpeg; set xlabel 'N_{step}'; set ylabel 'Total energy (eV/cell)';set style data lines; plot 'energy.dat'" > energy_750fs.jpg

The energy vs number of iteration should look like Fig. 5. We see that
after a few 100 fs the energy is conserved, but of course with some
fluctuations present. This should also indicate that the structure is
not changing drastically anymore and that the melting is achieved. We
should note that the energy conservation can be monitored because we use
the deterministic [Nosé-Hoover
thermostat](../tutorials/Nosé-Hoover_thermostat.md)
which has a kinetic and potential energy term of the heat bath which
provides energy conservation. If we would use e.g. the [Langevin
thermostat](../tutorials/Langevin_thermostat.md) which is a
stochastic thermostat we would obtain large fluctuations in the total
energy.

### Microcanonical ensemble\[<a
href="/wiki/index.php?title=Liquid_Si_-_Standard_MD&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Microcanonical ensemble">edit</a> \| (./index.php.md)\]

Next we want to continue the calculations but instead of the canonical
ensemble ([NVT ensemble](NVT_ensemble.md)) we are
going to carry out the calculations in the microcanonical ensemble ([NVE
ensemble](NVE_ensemble.md)). The microcanonical
ensemble calculations are carried out by setting the following tags in
the [INCAR](../input-files/INCAR.md) file:

    MDALGO = 1
    ANDERSEN_PROB = 0.0

In principle we set here an [Andersen
thermostat](../tutorials/Andersen_thermostat.md) but
effectively without using it since we set the collision probability of
the thermostat [ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md) to
zero.

We will carry out two hundred more molecular dynamics steps (by setting
[NSW](../incar-tags/NSW.md)=200) using the microcanonical ensemble.

First we check the mean temperature by typing the following line

    grep "mean temperature" OUTCAR

The user should get an output like:

    mean temperature <T/S>/<1/S>  :  2566.129

In this example we see that the target temperature is not kept when a
microcanonical ensemble is used.

At this point the user should be able to monitor the energies in the
calculation. If not repeat from scratch!

**Exercise:** Compare the energy conservation of the microcanonical
ensemble and the canonical ensemble. Carry out another 200 molecular
dynamics steps but with a step size that is only the half of the
previous one ([POTIM](../incar-tags/POTIM.md)=1.5). Compare the energy
conservation and check the mean temperature!

### Further things to try\[<a
href="/wiki/index.php?title=Liquid_Si_-_Standard_MD&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Further things to try">edit</a> \| (./index.php.md)\]

To get a better statistics the user should further carry out the
calculation for 400-1000 steps in the [NVT
ensemble](NVT_ensemble.md) but with a much smaller
time step
[POTIM](../incar-tags/POTIM.md)=0.3.
**Repeat the above analysis!**

## Download\[<a
href="/wiki/index.php?title=Liquid_Si_-_Standard_MD&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/1/1e/Si_Liquid_Melting.tgz" class="internal"
title="Si Liquid Melting.tgz">Si_Liquid_Melting.tgz</a>


[Overview](../tutorials/Molecular_dynamics_-_Tutorial.md) \>Liquid
Si - Standard MD \>
[Liquid Si -
Freezing](Liquid_Si_-_Freezing.md) \>
[Nucleophile Substitution CH3Cl - Standard
MD](Nucleophile_Substitution_CH3Cl_-_Standard_MD.md) \>
[Nuclephile Substitution CH3Cl -
mMD1](Nuclephile_Substitution_CH3Cl_-_mMD1.md) \>
[Nuclephile Substitution CH3Cl -
mMD2](Nuclephile_Substitution_CH3Cl_-_mMD2.md) \>
[Nuclephile Substitution CH3Cl -
mMD3](Nuclephile_Substitution_CH3Cl_-_mMD3.md) \>
[Nuclephile Substitution CH3Cl -
SG](Nuclephile_Substitution_CH3Cl_-_SG.md) \>
[Nuclephile Substitution CH3Cl -
BM](Nuclephile_Substitution_CH3Cl_-_BM.md) \>
[List of tutorials](../categories/Category-Tutorials.md)


