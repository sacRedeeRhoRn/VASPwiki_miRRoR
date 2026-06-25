<!-- Source: https://vasp.at/wiki/index.php/Chester_2019 | revid: 10218 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Chester 2019



## Contents


- [1
  Lectures](#lectures)
- [2 Allocating
  Computing Nodes and Environment
  Setup](#allocating-computing-nodes-and-environment-setup)
- [3 Submitting
  jobs](#submitting-jobs)
- [4
  Tutorials](#tutorials)
- [5 Further
  Examples](#further-examples)
  - [5.1 Nudge
    Elastic Band Method and (constrained) Molecular
    Dynamics](#Nudge_Elastic_Band_Method_and_(constrained)_Molecular_Dynamics)
  - [5.2 Magnetism
    in NiO](#magnetism-in-nio)
  - [5.3 NMR
    calculations](#nmr-calculations)


## Lectures\[<a
href="/wiki/index.php?title=Chester_2019&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Lectures">edit</a> \| (./index.php.md)\]

- <a
  href="http://www.vasp.at/vasp-workshop/lectures/VASP_lecture_Basics1.pdf"
  class="external text" rel="nofollow">DFT, PW, and PAW</a>: "VASP: The
  basics(1). DFT, plane waves, PAW, ...".

<!-- -->

- <a
  href="http://www.vasp.at/vasp-workshop/lectures/VASP_lecture_Basics2.pdf"
  class="external text" rel="nofollow">electronic convergence, BZ
  sampling</a>: "VASP: The basics(2). electronic convergence, BZ
  sampling ...".

<!-- -->

- <a
  href="http://www.vasp.at/vasp-workshop/lectures/VASP_lecture_Hybrids.pdf"
  class="external text" rel="nofollow">Hybrid functionals</a>: "VASP:
  Hybrid functionals".

<!-- -->

- <a
  href="http://www.vasp.at/vasp-workshop/lectures/VASP_lecture_Dielectric.pdf"
  class="external text" rel="nofollow">Dielectric properties</a>: "VASP:
  Dielectric response. Perturbation theory, linear response, and finite
  electric fields".

<!-- -->

- <a
  href="http://www.vasp.at/vasp-workshop/lectures/VASP_lecture_RPA_Kaltak.pdf"
  class="external text" rel="nofollow">Beyond DFT: RPA</a>: "VASP:
  beyond DFT. The Random-Phase-Approximation".

<!-- -->

- <a href="http://www.vasp.at/vasp-workshop/lectures/VASP_lecture_HPC.pdf"
  class="external text" rel="nofollow">Performance</a>: "VASP: running
  on HPC resources".

## Allocating Computing Nodes and Environment Setup\[<a
href="/wiki/index.php?title=Chester_2019&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Allocating Computing Nodes and Environment Setup">edit</a> \| (./index.php.md)\]

An interactive shell should be allocated after login. The following
command allocates an interactive node with 8 CPUs for 4 hours

    qsub -IVl select=1:ncpus=8,walltime=4:0:0,place=scatter:excl -A y15 

After successful allocation, one has to setup the environment as
follows.

To have access to the vasp binaries, the corresponding module has to be
loaded into the environment. Furthermore, the job scripts found in the
tutorial tar files (job.sh, doall.sh, etc) work only if the environment
variables "vasp_std, vasp_gam, vasp_ncl" are defined. Enter following
commands in the terminal window after login, to setup up the
environment.

    module load vasp
    export vasp_std="mpirun -ppn 8 -np 8 /lustre/home/y07/vasp5/5.4.4-intel17-mpt214/bin/vasp_std"
    export vasp_gam="mpirun -ppn 8 -np 8 /lustre/home/y07/vasp5/5.4.4-intel17-mpt214/bin/vasp_gam"
    export vasp_ncl="mpirun -ppn 8 -np 8 /lustre/home/y07/vasp5/5.4.4-intel17-mpt214/bin/vasp_ncl"

## Submitting jobs\[<a
href="/wiki/index.php?title=Chester_2019&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Submitting jobs">edit</a> \| (./index.php.md)\]

Alternative to an interactive shell, one may submit jobs to the cluster
as follows

    qsub vasp.job

where the jobfile "vasp.job" reads

    #!/bin/bash --login

    #PBS -N VASP-Test
    #PBS -l select=1:ncpus=36
    #PBS -l place=scatter:excl
    #PBS -l walltime=00:30:00
    #PBS -A y15 

    cd $PBS_O_WORKDIR 
    module load vasp
    mpiexec_mpt -ppn 36 -n 36 vasp_std | tee vasp.out

## Tutorials\[<a
href="/wiki/index.php?title=Chester_2019&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

For the beginners: [A short introduction to the common Input and Output
files.](Input_and_Output_-_a_short_Intro.md)

- [Atoms and
  Molecules](../tutorials/Atoms_and_Molecules_-_Tutorial.md)
- [Simple Bulk
  Systems](../tutorials/Bulk_Systems_-_Tutorial.md)
- [A bit of Surface
  Science](../tutorials/Surface_Science_-_Tutorial.md)
- [Hybrid
  Functionals](../tutorials/Hybrid_functionals_-_Tutorial.md)
- [Optical Properties and Dielectric
  Response](../tutorials/Optical_properties_and_dielectric_response_-_Tutorial.md)
- [The Random-Phase-Approximation: GW and
  ACFDT](../tutorials/GW_and_ACFDT_-_Tutorial.md)
- [The Bethe-Salpeter equation](../tutorials/BSE_-_Tutorial.md)
- [Magnetism](../tutorials/Magnetism_-_Tutorial.md)

## Further Examples\[<a
href="/wiki/index.php?title=Chester_2019&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Further Examples">edit</a> \| (./index.php.md)\]

#### Nudge Elastic Band Method and (constrained) Molecular Dynamics\[<a
href="/wiki/index.php?title=Chester_2019&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Nudge Elastic Band Method and (constrained) Molecular Dynamics">edit</a> \| (./index.php.md) Molecular Dynamics")\]

- [Liquid Si - Standard
  MD](Liquid_Si_-_Standard_MD.md)

<!-- -->

- [Transition State Search of
  Ammonia](Transition_State_Search_of_Ammonia.md)

<!-- -->

- [Adsorption of H2O on
  TiO2](Adsorption_of_H2O_on_TiO2.md)

#### Magnetism in NiO\[<a
href="/wiki/index.php?title=Chester_2019&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Magnetism in NiO">edit</a> \| (./index.php.md)\]

- [NiO GGA](NiO_GGA.md)

<!-- -->

- [NiO GGA+U](NiO_GGA+U.md)

<!-- -->

- [NiO HSE06](NiO_HSE06.md)

<!-- -->

- [Estimation of J magnetic
  coupling](Estimation_of_J_magnetic_coupling.md)

<!-- -->

- [Including the Spin-Orbit
  Coupling](Including_the_Spin-Orbit_Coupling.md)

<!-- -->

- [Determining the Magnetic
  Anisotropy](Determining_the_Magnetic_Anisotropy.md)

<!-- -->

- [Constraining the local magnetic
  moments](Constraining_the_local_magnetic_moments.md)

#### NMR calculations\[<a
href="/wiki/index.php?title=Chester_2019&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: NMR calculations">edit</a> \| (./index.php.md)\]

- [alpha-SiO2](Alpha-SiO2.md)

<!-- -->

- [alpha-AlF3](Alpha-AlF3.md)


