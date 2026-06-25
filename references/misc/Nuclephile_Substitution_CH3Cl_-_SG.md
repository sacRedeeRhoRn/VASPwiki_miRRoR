<!-- Source: https://vasp.at/wiki/index.php/Nuclephile_Substitution_CH3Cl_-_SG | revid: 17488 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Nuclephile Substitution CH3Cl - SG



[Overview](../tutorials/Molecular_dynamics_-_Tutorial.md) \>[Liquid
Si - Standard
MD](Liquid_Si_-_Standard_MD.md) \>
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
Nuclephile Substitution CH3Cl -
SG \> [Nuclephile
Substitution CH3Cl -
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
  - [2.4
    ICONST](#ICONST)
- [3
  Calculation](#Calculation)
  - [3.1 Running
    the calculation](#Running_the_calculation)
  - [3.2 Free
    energy profile](#Free_energy_profile)
- [4
  References](#References)
- [5
  Download](#Download)


## Task\[<a
href="/wiki/index.php?title=Nuclephile_Substitution_CH3Cl_-_SG&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

In this example the nucleophile substitution of a Cl<sup>-</sup> by
another Cl<sup>-</sup> in CH<sub>3</sub>Cl is simulated using a slow
growth approach.

## Input\[<a
href="/wiki/index.php?title=Nuclephile_Substitution_CH3Cl_-_SG&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Nuclephile_Substitution_CH3Cl_-_SG&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

       1.00000000000000
         12.0000000000000000    0.0000000000000000    0.0000000000000000
         0.0000000000000000    12.0000000000000000    0.0000000000000000
         0.0000000000000000    0.0000000000000000    12.0000000000000000
    C H Cl
       1   3   2
    direct
    0.53294865 0.56575027 0.49613388
    0.53110276 0.65294003 0.50241434
    0.44611198 0.52863033 0.51450056
    0.58463838 0.52611078 0.55968644
    0.32726066 0.74478226 0.64936301
    0.57915789 0.51894916 0.36275174

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Nuclephile_Substitution_CH3Cl_-_SG&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    Automatic
     0
    Gamma
     1  1  1
     0. 0. 0.

- For isolated atoms and molecules interactions between periodic images
  are negligible (in sufficiently large cells) hence no Brillouin zone
  sampling is necessary.

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Nuclephile_Substitution_CH3Cl_-_SG&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    PREC=Low
    EDIFF=1e-6
    LWAVE=.FALSE.
    LCHARG=.FALSE.
    NELECT=22
    NELMIN=4
    LREAL=.FALSE.
    ALGO=VeryFast
    ISMEAR=-1
    SIGMA=0.0516

    ############################# MD setting #####################################
    IBRION=0                                           # MD simulation
    NSW=1000                                           # number of steps
    POTIM=1                                            # integration step
    TEBEG=600                                          # simulation temperature
    MDALGO=11                                          # md with Andersen thermostat
    ANDERSEN_PROB=0.10                                 # collision probability
    LBLUEOUT=.TRUE.                                    # write the BM stuff on the output
    INCREM=-1e-4                                       # rate at which CV increases each step
    ##############################################################################

- The setting [LBLUEOUT](../incar-tags/LBLUEOUT.md)=*.TRUE.* tells VASP
  to write out the information needed for the computation of free
  energies.

### [ICONST](../input-files/ICONST.md)\[<a
href="/wiki/index.php?title=Nuclephile_Substitution_CH3Cl_-_SG&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: ICONST">edit</a> \| (./index.php.md)\]

    R 1 5 0
    R 1 6 0
    S 1 -1 0

## Calculation\[<a
href="/wiki/index.php?title=Nuclephile_Substitution_CH3Cl_-_SG&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

In a slow growth simulation, an approximation of the collective variable
is increased by the value [INCREM](../incar-tags/INCREM.md) every time
step. In order for the transformation between the initial and final
state to be reversible, the value of [INCREM](../incar-tags/INCREM.md)
must be infinitesimaly small. In practice we are limited by the desired
length of trajectory causing that irreversible rather than reversible
work is computed in a slow-growth simulation.

Slow-growth simulations should be considered as an approximate method of
free energy calculations whose quality depends strongly on the
transformation rate ([INCREM](../incar-tags/INCREM.md)). The quality of
the simulation can be judged from the hysteresis in the free energy
profiles computed for the forward (i.e. reactant -\> product) and
reverse (i.e. product -\> reactant) transformations. Alternatively, free
energies can be computed from a series of slow-growth simulations using
the Jarzyski
identity<sup>[\[1\]](#cite_note-jarzynski:prl:1997-1)</sup>.

**The method is most useful as a quick test of the quality of the
collective variable before launching any more accurate and
time-consuming simulations.**

  

### Running the calculation\[<a
href="/wiki/index.php?title=Nuclephile_Substitution_CH3Cl_-_SG&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Running the calculation">edit</a> \| (./index.php.md)\]

The mass for hydrogen in this example is set 3.016 a.u. corresponding to
the tritium isotope. This way larger timesteps can be chosen for the MD
(note that the free energy is independent of the masses of atoms).

For practical reasons, we split our (presumably long) meta dynamics
calculation into shorter runs of length of 1000 fs (NSW=1000; POTIM=1).
This is done automatically in the script *run* which looks as follows:

    #!/bin/bash 

    runvasp="mpirun -np x executable_path"

    # ensure that this sequence of MD runs is reproducible
    cp POSCAR.init POSCAR
    cp INCAR.init INCAR
    rseed="RANDOM_SEED =         311137787                0                0"
    echo $rseed >> INCAR

    i=1
    while [ $i -le 50 ] 
    do

      # start vasp
      $runvasp

      # ensure that this sequence of MD runs is reproducible
      rseed=$(grep RANDOM_SEED REPORT |tail -1)
      cp INCAR.init INCAR
      echo $rseed >> INCAR

      # use the last configuration generated in the previous
      # run as initial configuration for the next run
      cp CONTCAR POSCAR

      # backup some important files
      cp REPORT REPORT.$i
      cp vasprun.xml vasprun.xml.$i

      let i=i+1
    done

- The user has to adjust the *runvasp* variable, which holds the command
  for the executable command.
- Please run this script by typing:

<!-- -->

    bash ./run

### Free energy profile\[<a
href="/wiki/index.php?title=Nuclephile_Substitution_CH3Cl_-_SG&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Free energy profile">edit</a> | (./index.php.md)\]

The following script *fgradSG.sh* extracts approximate free energy
gradients from *REPORT.\** files obtained in the slow-growth simulation
and stores them along with the collectible variables in the file
*grad.dat*:

    #!/bin/bash

    rm grad.dat

    i=1

    while [ $i -le 1000 ]
    do
      if test -f REPORT.$i
      then
        grep cc REPORT.$i |awk '{print $3}' >xxx
        grep b_m REPORT.$i |awk '{print $2}' >fff
        paste xxx fff >> grad.dat
      fi
      let i=i+1
    done 

    sort -n grad.dat >grad_.dat
    mv grad_.dat grad.dat
    rm xxx
    rm fff

To execute it please type the following:

    bash ./fgradSG.sh

The free energy profile along the collective variable is plotted using
the script *integrateForward.py*:


**Click to show/integrateForward.py**


    #!/usr/bin/python

    import string
    import sys

    f=sys.argv[1]

    f=open(f,'r')

    r=[]
    g=[]

    for line in f.readlines():
      line=string.split(line)
      num=len(line)
      if len(line)==2:
        r.append(float(line[0]))
        g.append(float(line[1]))

    f.close()

    tg=0.0
    print r[0],tg
    for i in range(1,len(r)):
      gg=0.5*(r[i]-r[i-1])*(g[i]+g[i-1])
      tg+=gg
      print r[i],tg


This script obtains the free energy vs. the collective variable via a
simple integration by trapezoid rule. The output is written to standard
out so it has to be redirected to a file (we will arbitrarily choose the
name *free_energy.dat*). To execute the script type the following
command:

    python integrateForward.py grad.dat > free_energy.dat

To plot that script via Gnuplot please use the following:

    gnuplot -e "set terminal jpeg; set xlabel 'Collective variable (Ang)'; set ylabel 'Free energy (eV)'; set style data lines; plot 'free_energy.dat'" > free_energy.jpg

The free energy profile should look like the following:

<a href="/wiki/File:Free_energy_CH3Cl_SG.jpg"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/3/3e/Free_energy_CH3Cl_SG.jpg/500px-Free_energy_CH3Cl_SG.jpg"
class="mw-file-element" decoding="async"
srcset="/wiki/images/3/3e/Free_energy_CH3Cl_SG.jpg 1.5x" width="500"
height="375" /></a>

Again this method is only supposed to give a rough estimate for the free
energy profile of a material.

## References\[<a
href="/wiki/index.php?title=Nuclephile_Substitution_CH3Cl_-_SG&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-jarzynski:prl:1997_1-0)
    <a href="https://doi.org/10.1103/PhysRevLett.78.2690"
    class="external text" rel="nofollow">C. Jarzynski, Phys. Rev. Lett.
    <strong>78</strong>, 2690 (1997).</a>


  

## Download\[<a
href="/wiki/index.php?title=Nuclephile_Substitution_CH3Cl_-_SG&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/e/ed/CH3Cl_SG.tgz" class="internal"
title="CH3Cl SG.tgz">CH3Cl_SG.tgz</a>


[Overview](../tutorials/Molecular_dynamics_-_Tutorial.md) \>[Liquid
Si - Standard
MD](Liquid_Si_-_Standard_MD.md) \>
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
Nuclephile Substitution CH3Cl -
SG \> [Nuclephile
Substitution CH3Cl -
BM](Nuclephile_Substitution_CH3Cl_-_BM.md) \>
[List of tutorials](../categories/Category-Tutorials.md)


