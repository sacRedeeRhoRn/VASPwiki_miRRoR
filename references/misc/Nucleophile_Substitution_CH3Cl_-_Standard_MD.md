<!-- Source: https://vasp.at/wiki/index.php/Nucleophile_Substitution_CH3Cl_-_Standard_MD | revid: 10364 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Nucleophile Substitution CH3Cl - Standard MD



[Overview](../tutorials/Molecular_dynamics_-_Tutorial.md) \>[Liquid
Si - Standard
MD](Liquid_Si_-_Standard_MD.md) \>
[Liquid Si -
Freezing](Liquid_Si_-_Freezing.md) \>
Nucleophile Substitution CH3Cl -
Standard MD \>
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
  Task](#task)
- [2
  Input](#input)
  - [2.1
    POSCAR](#poscar)
  - [2.2
    KPOINTS](#kpoints)
  - [2.3
    INCAR](#incar)
  - [2.4
    ICONST](#iconst)
- [3
  Calculation](#calculation)
  - [3.1 Running
    the calculation](#running-the-calculation)
  - [3.2 Time
    evolution of distance](#time-evolution-of-distance)
  - [3.3 Higher
    temperature - 1000 K](#higher-temperature---1000-k)
- [4
  Download](#download)


## Task\[<a
href="/wiki/index.php?title=Nucleophile_Substitution_CH3Cl_-_Standard_MD&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

The main task of this example is to learn how to monitor distances on
the example of a nucleophile substitution of a Cl<sup>-</sup> by another
Cl<sup>-</sup> in CH<sub>3</sub>Cl.

## Input\[<a
href="/wiki/index.php?title=Nucleophile_Substitution_CH3Cl_-_Standard_MD&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Nucleophile_Substitution_CH3Cl_-_Standard_MD&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    CH3Cl                                         
       1.00000000000000     
        12.0000000000000000    0.0000000000000000    0.0000000000000000
         0.0000000000000000   12.0000000000000000    0.0000000000000000
         0.0000000000000000    0.0000000000000000   12.0000000000000000 
    C H Cl
       1   3   2
    cart
             5.91331371  7.11364924  5.78037960
             5.81982231  8.15982106  5.46969017
             4.92222130  6.65954232  5.88978969
             6.47810398  7.03808479  6.71586385
             4.32824726  8.75151396  7.80743202
             6.84157897  6.18713289  4.46842049

- The starting [POSCAR](../input-files/POSCAR.md) file for this example can
  be found under POSCAR.init. It will be needed for the script that runs
  the job (run.sh).
- A sufficiently large cell is chosen to minimize the interactions
  between neighbouring cells and hence to simulate an isolated molecular
  reaction.

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Nucleophile_Substitution_CH3Cl_-_Standard_MD&amp;veaction=edit&amp;section=4"
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
href="/wiki/index.php?title=Nucleophile_Substitution_CH3Cl_-_Standard_MD&amp;veaction=edit&amp;section=5"
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
    MDALGO=11                                          # metaDynamics with Andersen thermostat
    ANDERSEN_PROB=0.10                                 # collision probability
    ##############################################################################

- Molecular dynamics are switched on by the tag
  [IBRION](../incar-tags/IBRION.md)=0.
- The metadynamics tag [MDALGO](../incar-tags/MDALGO.md)=11 is only used
  to monitor the two C-Cl distances defined in the
  [ICONST](../input-files/ICONST.md) file.
- Simulations are carried out in the [NVT
  ensemble](NVT_ensemble.md) at approximately room
  temperature ([TEBEG](../incar-tags/TEBEG.md)=300) and the [Andersen
  thermostat](../tutorials/Andersen_thermostat.md) is used
  for the temperature control. The strength of the coupling is
  controlled by the collision probability
  [ANDERSEN_PROB](../incar-tags/ANDERSEN_PROB.md)=0.10.
- The accuracy of this calculation is kept low
  ([PREC](../incar-tags/PREC.md)=Low and
  [ALGO](../incar-tags/ALGO.md)=VeryFast), which is completely sufficient
  for this tutorial. For more quantitative results this tags should be
  investigated (of course at the cost of higher computational demand).
- A charged system (due to the "incoming" Cl<sup>-</sup>) is simulated,
  so the number of electrons is raised by one compared to the neutral
  system ([NELECT](../incar-tags/NELECT.md)=22). To compensate for the
  charge a positive homogeneous background charge is assumed.
- Although very light atoms are present in the structure (hydrogen) a
  time step of 1 fs ([POTIM](../incar-tags/POTIM.md)=1) is safe to use.
  This can be achieved by setting the mass of hydrogen to that of
  tritium (look for the line "POMASS = 3.016" in the
  [POTCAR](../input-files/POTCAR.md) file). This is unproblematic since the
  free energy is independent of the mass of atoms.

### [ICONST](../input-files/ICONST.md)\[<a
href="/wiki/index.php?title=Nucleophile_Substitution_CH3Cl_-_Standard_MD&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: ICONST">edit</a> \| (./index.php.md)\]

For this example an [ICONST](../input-files/ICONST.md) file is used which
looks like:

    R 1 5 0
    R 1 6 0
    S 1 -1 7

- First line: This line selects the interatomic distance (R) between the
  first (C) and the fifth atom (Cl) in the
  [POSCAR](../input-files/POSCAR.md) file. The 0 at the fourth entry would
  usually specify that the distances are constrained but if the
  coordinates are used later for special coordinates the constraining is
  not applied (for further information see
  [ICONST](../input-files/ICONST.md)).
- Second line: Same as the first line but interatomic distance between
  the first (C) and the sixth atom (Cl) in the
  [POSCAR](../input-files/POSCAR.md) file is selected.
- Third line: This line selects a linear combination (option S) of the
  first two coordinates where the second and fourth column specify the
  coefficients of the coordinates. The setting of 1 and -1 corresponds
  to the difference between both. The 7 at the fourth entry specifies
  that difference between these two distances is monitored but no
  constraints are applied.

## Calculation\[<a
href="/wiki/index.php?title=Nucleophile_Substitution_CH3Cl_-_Standard_MD&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

A parameter that approximates the reaction coordinate, the difference
between two C-Cl distances, will be monitored. Expected values for
reactant: $\approx 1 \AA$, for product: $~-1 \AA$, for
transition state: $0 \AA$.

### Running the calculation\[<a
href="/wiki/index.php?title=Nucleophile_Substitution_CH3Cl_-_Standard_MD&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Running the calculation">edit</a> \| (./index.php.md)\]

The mass for hydrogen in this example is set 3.016 a.u. corresponding to
the tritium isotope. This way larger timesteps can be chosen for the MD.
For practical reasons, we split our (pressumably long) molecular
dynamics calculation into shorter runs of lengths of 1000 fs
([NSW](../incar-tags/NSW.md)=1000 and [POTIM](../incar-tags/POTIM.md)=1). At the
end of each run the [CONTCAR](../output-files/CONTCAR.md) file is copied to
the [POSCAR](../input-files/POSCAR.md) so that the simulation continues in
a seamless manner. All of this is done by the script *run* provided with
this example:

    #!/bin/bash

    runvasp="mpirun -np 8 executable_path/vasp_gam"

    # make sure to always start with the same structure
    cp POSCAR.init POSCAR

    i=1

    while [ $i -le 50 ] 
    do
      # start vasp
      $runvasp

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

After the execution we should obtain 50 output files. Each contains a
1000 fs run totalling to a trajectory of 50 ps. It should be mentioned
that this can take several hours on 8 cores so if the user has only
limited time and resources available or is only interested to learn the
execution of this example the number of runs (line "\[ \$i -le 50 \]")
can be changed from 50 to a smaller value. Also the number of timesteps
per run can be lowered ([NSW](../incar-tags/NSW.md)).

### Time evolution of distance\[<a
href="/wiki/index.php?title=Nucleophile_Substitution_CH3Cl_-_Standard_MD&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Time evolution of distance">edit</a> | (./index.php.md)\]

- The monitored value of the distance between the two Cl<sup>-</sup>
  ions defined in the [ICONST](../input-files/ICONST.md) file is written
  for each molecular dynamics run to the [REPORT](../output-files/REPORT.md)
  file written as "mc = ...". The time evolution function of this
  variable is monitored using the script timeEv.sh:

<!-- -->

    #!/bin/bash 

    if test -f "timeEvol.dat"; then
       rm timeEvol.dat
    fi

    i=1
    while [ $i -le 1000 ]
    do
       if test -f REPORT.$i
       then
         grep mc REPORT.$i |awk '{print $3 }' >>timeEvol.dat
       fi
       let i=i+1
    done

To execute this script type:

    bash timeEv.sh

It creates a file "timeEvol.dat" holding the value for the collective
variable at every molecular dynamics step.

  

- After that the task is to get a histogram (or probability
  distribution) of the data. The user should try to write a script for
  itself. Otherwise the script *probability_distribution_function.py*
  can be used:

<!-- -->

    #!/usr/bin/python

    import sys
    import re
    import math

    #setting grid for histogram
    xmin=0.0
    xmax=5.0
    nx=500
    dx=(xmax-xmin)/nx
    histogram=[0.0 for j in range(0,nx)]
    readfile = open("timeEvol.dat","r")
    line=readfile.readline()
    z=0
    ymin=0.0
    ymax=0.0
    #loop over lines in file timeEvol.dat
    while (line):
      z=z+1
      line.strip()
      line=re.sub('^',' ',line)
      y=line.split()
      if (z==1):
         ymin=float(y[0])
         ymax=float(y[0])
      #calculate min max value for normalization
      if (ymin>float(y[0])):
         ymin=float(y[0])
      if (ymax<float(y[0])):
         ymax=float(y[0])
      #calculate index of argument
      ix=int(float(y[0])/float(dx)+0.5)
      #check for segmentation fault
      if (ix>=0 and ix<nx):
         histogram[ix]=histogram[ix]+1.0
      line=readfile.readline()
    readfile.close
    #normalizing and printing histogram
    norm=z*(abs(xmax-xmin))/nx
    for ix in range(0,nx):
       x=xmin+ix*dx
       pair_cor=histogram[ix]/norm
       print x, pair_cor

To execute this script type:

    python probability_distribution_function.py > histogram_600K.dat

To plot the histogram the user should use his favourite program.
Alternatively the histogram is plotted using gnuplot:

    gnuplot -e "set terminal jpeg; set xlabel 'r(Ang)'; set ylabel 'PCF'; set style data lines; plot 'histogram_600K.dat'" > histogram_600K.jpg

The obtained histogram should look like the following:

<a href="/wiki/File:Histogram_600K.jpg" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/4/4d/Histogram_600K.jpg/300px-Histogram_600K.jpg"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/4/4d/Histogram_600K.jpg/450px-Histogram_600K.jpg 1.5x, /wiki/images/thumb/4/4d/Histogram_600K.jpg/600px-Histogram_600K.jpg 2x"
width="300" height="225" /></a>

- The user should also calculate the mean value and variance of the
  Cl<sup>-</sup>-Cl<sup>-</sup> distance. It is recommended to the user
  to try to write an own script/program doing that. Otherwise the script
  *average_and_standard_deviation.py* can be used:

<!-- -->

    #!/usr/bin/python

    import sys
    import re
    import math

    data=[]
    readfile = open("timeEvol.dat","r")
    line=readfile.readline()
    z=0
    mean=0.0
    standard_deviation=0.0
    #loop over lines in file timeEvol.dat
    while (line):
      z=z+1
      line.strip()
      line=re.sub('^',' ',line)
      y=line.split()
      #calculate mean
      mean=mean+float(y[0])
      #save data for later
      data.append(float(y[0]))
      line=readfile.readline()
    readfile.close
    #calculate mean
    mean=mean/z
    #calculate 
    for y in data:
       standard_deviation=standard_deviation+(y-mean)**2.0
    standard_deviation=(standard_deviation/z)**0.5
    print "Mean :",mean
    print "Standard devation :",standard_deviation

To execute this script type:

    python average_and_standard_deviation.py

The calculated mean value and standard deviation should be around 1.5986
$\AA$ and 0.3403 $\AA$.

**Exercise: Did the Cl<sup>-</sup> ever visit the product's region
during this MD?**

### Higher temperature - 1000 K\[<a
href="/wiki/index.php?title=Nucleophile_Substitution_CH3Cl_-_Standard_MD&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Higher temperature - 1000 K">edit</a> | (./index.php.md)\]

After that we rerun the calculation at 1000 K and perform the same
analysis steps as above. We should obtain a histogram at 1000 K that
looks like the following:

<a href="/wiki/File:Histogram_1000K.jpg"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/5/5f/Histogram_1000K.jpg/300px-Histogram_1000K.jpg"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/5/5f/Histogram_1000K.jpg/450px-Histogram_1000K.jpg 1.5x, /wiki/images/thumb/5/5f/Histogram_1000K.jpg/600px-Histogram_1000K.jpg 2x"
width="300" height="225" /></a>

The calculated mean value and standard deviation should be around
2.01023596 $\AA$ and
0.664687047095 $\AA$.

**Exercise: Explain the difference at higher temperature!**

## Download\[<a
href="/wiki/index.php?title=Nucleophile_Substitution_CH3Cl_-_Standard_MD&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/5/56/CH3Cl_standard_Molecular_Dynamics.tgz"
class="internal"
title="CH3Cl standard Molecular Dynamics.tgz">CH3Cl_standard_Molecular_Dynamics.tgz</a>


[Overview](../tutorials/Molecular_dynamics_-_Tutorial.md) \>[Liquid
Si - Standard
MD](Liquid_Si_-_Standard_MD.md) \>
[Liquid Si -
Freezing](Liquid_Si_-_Freezing.md) \>
Nucleophile Substitution CH3Cl -
Standard MD \>
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


