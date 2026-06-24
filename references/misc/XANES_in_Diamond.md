<!-- Source: https://vasp.at/wiki/index.php/XANES_in_Diamond | revid: 17498 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# XANES in Diamond
Important: This feature will be only available from VASP 6.0.

[Overview](../tutorials/XAS_-_Tutorial.md) \> XANES in Diamond \>
[List of tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 Input](#Input)
  - [2.1 POSCAR](#POSCAR)
  - [2.2 INCAR](#INCAR)
- [3 Calculation](#Calculation)
  - [3.1 Step 1 build a supercell](#Step_1_build_a_supercell)
  - [3.2 Step 2 Prepare input files](#Step_2_Prepare_input_files)
  - [3.3 Step 3 Running Calculation](#Step_3_Running_Calculation)
  - [3.4 Step 4 Extraction of XAS
    Spectrum](#Step_4_Extraction_of_XAS_Spectrum)
- [4 Download](#Download)
- [5 References](#References)

## Task
Calculation of the XANES K-edge in diamond using the supercell core-hole
method.

## Input
### [POSCAR](../input-files/POSCAR.md)
    cubic diamond
     3.567
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
     2
    direct
    0.0 0.0 0.0
    0.25 0.25 0.25

Above, we show the [POSCAR](../input-files/POSCAR.md) file for the
primitive unit cell of diamond. Note that we will not use this structure
as input for the calculation. Instead, we use it to construct a
[POSCAR](../input-files/POSCAR.md) file for a $3
\times 3 \times 3$ super cell actually used in the
calculation.

### [INCAR](../input-files/INCAR.md)
    System = DIAMOND
    ALGO = FAST
    ISMEAR = 0; SIGMA = 0.1;
    ICORELEVEL = 2
    CLNT = 1
    CLN = 1
    CLL = 0
    CLZ = 1.0
    CH_LSPEC = .TRUE.
    CH_SIGMA = 0.5
    NBANDS = 300
    LREAL = A

- To promote a core electron into the conduction bands and hence create
  the core-hole [ICORELEVEL](../incar-tags/ICORELEVEL.md)=2 has to be
  set. This corresponds to the final state approximation.
- [CLNT](../incar-tags/CLNT.md)=1 selects the first atom species in the
  [POSCAR](../input-files/POSCAR.md) file.
- [CLN](../incar-tags/CLN.md)=1 selects main quantum number 1 (hence K-edge).
- [CLL](../incar-tags/CLL.md)=0 selects angular quantum number 0 (s).
- [CLZ](../incar-tags/CLZ.md)=1.0 selects the charge of the core hole. By
  setting this number to a fractional value we can mimic different
  screenings of the electrons. These non-integer values should only be
  used with caution, since this purely exploits error cancellation and
  does not correspond to a physically correct description of the
  screening.
- By setting [CH_LSPEC](../incar-tags/CH_LSPEC.md)=*.TRUE.*, we enable
  the calculation of matrix elements between core and conduction states
  and the calculation of the core electron absorption spectrum.
- The broadening of the core electron absorption spectrum is controlled
  by the tag [CH_SIGMA](../incar-tags/CH_SIGMA.md). Usually it is good
  practice to set this value low and broaden the spectrum in post
  processing.
- We have to set [NBANDS](../incar-tags/NBANDS.md) to a larger value to
  consider enough conduction band states in the calculation.
- Since super cells are used the calculation of the projection operators
  in real space ([LREAL](../incar-tags/LREAL.md)=*A*) is much faster.

## Calculation
### Step 1 build a supercell
In the periodic boundary conditions of VASP, the core-hole interacts
with its periodic replica so that we need sufficiently large super cells
to reduce this spurious interaction. To this end, we employ successively
large cells until the spectrum shows no significant changes. For this
tutorial, we illustrate the calculation of a core-hole using a
$3\times3\times3$ cell to allow for a
reasonably fast calculation. However, for converged values one should
use at least $4\times4\times4$ super
cell.

The super cell can be obtained by either taking the file POSCAR.3x3x3
provided with this tutorial or constructing the
[POSCAR](../input-files/POSCAR.md) file from the primitive cell using
p4vasp, which is demonstrated below:

- Open p4vasp by typing *p4v* on the terminal.
- Load the primitive cell by clicking on **File**→**Load system**:

[![](https://vasp.at/wiki/images/thumb/7/75/Fig_XAS_1.png/200px-Fig_XAS_1.png)](https://vasp.at/wiki/File:Fig_XAS_1.png)

- Multiply cell in each direction (enter 3 for each direction) by
  clicking on **Edit**→**Multiply Cell**:

[![](https://vasp.at/wiki/images/thumb/6/67/Fig_XAS_2.png/250px-Fig_XAS_2.png)](https://vasp.at/wiki/File:Fig_XAS_2.png)

- Save new system by clicking on **File**→**Save system as**:

[![](https://vasp.at/wiki/images/thumb/d/df/Fig_XAS_3.png/250px-Fig_XAS_3.png)](https://vasp.at/wiki/File:Fig_XAS_3.png)

### Step 2 Prepare input files
The first few lines of the generated [POSCAR](../input-files/POSCAR.md)
file for the super cell should look like the following

    cubic diamond
    3.567
     +1.5000000000  +1.5000000000  +0.0000000000
     +0.0000000000  +1.5000000000  +1.5000000000
     +1.5000000000  +0.0000000000  +1.5000000000
     54
    Cartesian
     +0.0000000000  +0.0000000000  +0.0000000000
     +0.2500000000  +0.2500000000  +0.2500000000
     +0.5000000000  +0.0000000000  +0.5000000000
     ...

Here, all the 54 atoms are of the same species (line 6). To distinguish
between the atom with the core-hole and the rest, we treat one atom as a
different species. Choosing the first atom, we replace the 54 in the 6th
line with 1 and 53 and obtain the following
[POSCAR](../input-files/POSCAR.md) file

    cubic diamond
    3.567
     +1.5000000000  +1.5000000000  +0.0000000000
     +0.0000000000  +1.5000000000  +1.5000000000
     +1.5000000000  +0.0000000000  +1.5000000000
     1 53
    Cartesian
     +0.0000000000  +0.0000000000  +0.0000000000
     +0.2500000000  +0.2500000000  +0.2500000000
     +0.5000000000  +0.0000000000  +0.5000000000
     ...

In the [INCAR](../input-files/INCAR.md) file, we specify that the first
species carries the core-hole by setting [CLNT](../incar-tags/CLNT.md)=1. We
create a [POTCAR](../input-files/POTCAR.md) file with the PAW/PS
information for both species. Since both species are carbon this amounts
simply to the concatenation of the [POTCAR](../input-files/POTCAR.md) file
for carbon

     cat POT_C POT_C > POTCAR

We provide the resulting [POTCAR](../input-files/POTCAR.md) file for this
core-hole calculation in the tar file of this tutorial.

To calculate accurate spectra, we need to include a sufficient number of
conduction states. The required number of bands depends on the number of
electrons in the system and the energy range of the spectrum. We can
manually adjust the number of bands with the
[NBANDS](../incar-tags/NBANDS.md) variable. However, since the computation
time increases drastically with the number of bands, selecting initially
very large numbers is also not advisable. Hence, one has to increase the
number of bands to find the optimum of computational effort and
accuracy. In this tutorial, we use [NBANDS](../incar-tags/NBANDS.md)=300.

The other input variables in the [INCAR](../input-files/INCAR.md) file are
described above.

**Mind**: The multiplicity of the species carrying the core-hole has to
be 1 otherwise the code will not work. Also mind that the selected
species ([CLNT](../incar-tags/CLNT.md) in the [INCAR](../input-files/INCAR.md)
file) is consistent with the order of the species specified in the
[POSCAR](../input-files/POSCAR.md) and [POTCAR](../input-files/POTCAR.md)
files.

  

### Step 3 Running Calculation
Both the SCF calculation with the core-hole and the subsequent
calculation of the dielectric matrix (spectrum) are done in a run of
VASP. To minimize the spurious interaction between core-holes in
neighboring cells requires large super cells and to reduce the
computational time it is advisable to run a parallel VASP calculation

     mpirun -np $np vasp_version

Here, *\$np* corresponds to the number of processes and the *\_version*
in the executable stands for *std*, *gam*, and *ncl*: the standard,
$\Gamma$-point only, and non-collinear
version, respectively. The $3\times3\times3$ cell used in this tutorial gives qualitatively correct
results and can be completed even with a small number of processes. You
can verify the spectrum on the larger $4\times4\times4$ cell, which we provide in the tar file of
this tutorial.

### Step 4 Extraction of XAS Spectrum
The XAS spectrum is proportional to the imaginary part of the
frequency-dependent dielectric function, which is written in the
[OUTCAR](../output-files/OUTCAR.md) file

      frequency dependent IMAGINARY DIELECTRIC FUNCTION (independent particle, no local field effects) density-density
         E(ev)      X         Y         Z        XY        YZ        ZX
      --------------------------------------------------------------------------------------------------------------
      243.589609    0.000000    0.000000    0.000000    0.000000    0.000000    0.000000
      243.677325    0.000000    0.000000    0.000000    0.000000    0.000000    0.000000
      243.765042    0.000000    0.000000    0.000000    0.000000    0.000000    0.000000
      ...

Usually we are interested in the sum of all components of the dielectric
matrix. You can obtain this by the script provided in this tutorial
*plot_core_imdiel.sh*

**Click to show/*plot_core_imdiel.sh***

    #!/bin/bash

    parallel=-1
    normal=-1
    all=-1
    tauc=-1
    trace=-1
    while [[ $# -gt 0 ]]
    do
       key="$1"
       case $key in
          -parallel) parallel=0
          ;;
          -normal) normal=0
          ;;
          -trace) trace=0
          ;;
          -tauc) tauc=0
          ;;
       esac
       shift
    done


    cat > helpscript.perl  <<EOF
    #!/bin/perl

    use strict;
    use warnings;
    my \$mode=shift;

    while(<>)
    {
       chomp;
       if(\$_ =~ /frequency dependent IMAGINARY DIELECTRIC FUNCTION/)
       {
          \$_=<>;
          \$_=<>;
          while (<>)
          {
             my \$sum=0;
             if (\$_ !~ /[0-9]/) {last;}
             chomp;
             \$_=~s/^/ /;
             my @help=split(/[\t,\s]+/);
             if (\$help[2]=~/NaN/||\$help[3]=~/NaN/||\$help[4]=~/NaN/) {next;}
             if (\$help[5]=~/NaN/||\$help[6]=~/NaN/||\$help[4]=~/NaN/) {next;}
             if (\$mode==0) {\$sum=\$help[2]+\$help[3]+\$help[4]+\$help[5]+\$help[6]+\$help[7];}
             if (\$mode==1) {\$sum=\$help[4];}
             if (\$mode==2) {\$sum=\$help[2]+\$help[3];}
             if (\$mode==3) {\$sum=\$help[2]+\$help[3]+\$help[4];}
             if (\$mode==4) {\$sum=(\$help[1]*\$help[1]*(\$help[2]+\$help[3]+\$help[4]+\$help[5]+\$help[6]+\$help[7]))**0.5;}
             if (\$mode==5) {\$sum=(\$help[1]*\$help[1]*(\$help[4]))**0.5;}
             if (\$mode==6) {\$sum=(\$help[1]*\$help[1]*(\$help[2]+\$help[3]))**0.5;}
             if (\$mode==7) {\$sum=(\$help[1]*\$help[1]*(\$help[2]+\$help[3]+\$help[4]))**0.5;}
             print \$help[1]," ",\$sum,"\n";
          }
       }
       last if eof;
    }
    EOF

    if [[ $normal -eq 0 ]]; then
       if [[ $tauc -eq 0 ]]; then
          perl helpscript.perl 4 OUTCAR > CORE_DIELECTRIC_IMAG.dat
       else
          perl helpscript.perl 1 OUTCAR > CORE_DIELECTRIC_IMAG.dat
       fi
    else
       if [[ $parallel -eq 0 ]]; then
          if [[ $tauc -eq 0 ]]; then
             perl helpscript.perl 5 OUTCAR > CORE_DIELECTRIC_IMAG.dat
          else
             perl helpscript.perl 2 OUTCAR > CORE_DIELECTRIC_IMAG.dat
          fi
       else
          if [[ $trace -eq 0 ]]; then
             if [[ $tauc -eq 0 ]]; then
                perl helpscript.perl 6 OUTCAR > CORE_DIELECTRIC_IMAG.dat
             else
                perl helpscript.perl 3 OUTCAR > CORE_DIELECTRIC_IMAG.dat
             fi
          else
             if [[ $tauc -eq 0 ]]; then
                perl helpscript.perl 7 OUTCAR > CORE_DIELECTRIC_IMAG.dat
             else
                perl helpscript.perl 0 OUTCAR > CORE_DIELECTRIC_IMAG.dat
             fi
          fi
       fi
    fi
    rm helpscript.perl

To use it type:

    bash ./plot_core_imdiel.sh

This will create the file CORE_DIELECTRIC_IMAG.dat containing the sum of
the imaginary part of the dielectric matrix. Note that the absolute
values of the experimental peak positions is not captured due to
fundamental limitations of local DFT to describe the core level
energies. Usually, there is even a noticeable deviation between
calculations using different codes. Therefore, it is accepted in
literature to look at the relative peak positions in the spectra and
their relative intensity.

We compare the results obtained with VASP to
experimental^([\[1\]](#cite_note-Ma.PRL-1)) and
theoretical^([\[2\]](#cite_note-Tallefumier.PRB-2)) XAS spectra from
literature provided in the files *C_XAS_aligned_to_VASP.dat* and
*C_PARATEC_aligned_to_VASP.dat*, respectively. The theoretical reference
calculation was obtained using the PARATEC code and relies on
PAW/Pseudopotential similar to VASP. We provide a script with this
tutorial to compare these literature results to the spectrum obtained
with VASP:

**Click to show/*gnuplot_XANES_C.script***

    unset ytics
    set xrange [280:310]
    set xlabel "Energy (eV)"
    set ylabel "Absorption (arbitrary units)"
    plot "CORE_DIELECTRIC_IMAG.dat" using 1:2 with lines lw 2 ti "VASP",\
         "C_PARATEC_aligned_to_VASP.dat" using 1:2 with lines ti "PAW lit",\
         "C_XAS_aligned_to_VASP.dat" using 1:2 with lines ti "Exp"
     pause -1

To use that script type:

     gnuplot gnuplot_XANES_C.script

The file *plot.sh* constitutes a convenient wrapper around these post
processing steps. The resulting spectra should look like this:  
[![](https://vasp.at/wiki/images/thumb/a/a2/Fig_XAS_4.png/600px-Fig_XAS_4.png)](https://vasp.at/wiki/File:Fig_XAS_4.png)

Because DFT cannot reproduce the absolute position (see above), we have
shifted both spectra so that the position of the first peak coincides
with the VASP. In this example, we scaled the experiment to VASP, since
in this way the obtained results can be very easily compared using a
script. Usually one would either scale the first peak to 0 or would
scale the calculated value to the experiment. Additionally the intensity
of the spectrum can be scaled arbitrarily. So in this example, we align
the position and the height of the first peak for the calculations. The
experiment is a little bit more tricky. It's a matter of taste what to
consider as the first peak, but we decided that most likely the second
peak corresponds to the first peak in the calculations and the first
peak in experiment is a shoulder that is simply not pronounced in the
calculations.

Another important issue is the broadening. Because the observed
broadening is driven by many factors depending on the particular
experimental setup, it is not possible to reproduce the broadening
exactly. Therefore, we arbitrarily choose a broadening that gives
approximately the same width as experiment. For simplicity in this
tutorial, we choose to use a 0.5 eV constant Gaussian broadening (the
broadening is determined by the [ISMEAR](../incar-tags/ISMEAR.md) tag and
we used [ISMEAR](../incar-tags/ISMEAR.md)=0 which corresponds to a
Gaussian broadening). For more elaborate spectra we strongly advise
users to choose a 0.05 eV broadening and apply the desired broadening as
post-processing.

Apart from the lower broadening width, we get a quite reasonable
agreement with the theoretical literature calculation. We stress again
that the $3\times3\times3$ super cell in
this example are not fully converged. The interested user can repeat the
calculations for a larger $4\times4\times4$ super cell. The files for this example are also given in the
tar file. Be aware that the larger number of atoms in the bigger super
cell requires an adjustment of the [NBANDS](../incar-tags/NBANDS.md)
variable..

## Download
[XANES_Diamond.tgz](https://vasp.at/wiki/images/1/19/XANES_Diamond.tgz "XANES Diamond.tgz")

## References
1.  [↑](#cite_ref-Ma.PRL_1-0) [Y.Ma et al., Phys. Rev. Lett 69, 2598
    (1992).](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.69.2598)
2.  [↑](#cite_ref-Tallefumier.PRB_2-0) [M.Tallefumier et al., Phys. Rev.
    B 66, 195107
    (2002).](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.66.195107)

[Overview](../tutorials/XAS_-_Tutorial.md) \> XANES in Diamond \>
[List of tutorials](../categories/Category-Tutorials.md)
