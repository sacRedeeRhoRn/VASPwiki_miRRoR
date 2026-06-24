<!-- Source: https://vasp.at/wiki/index.php/IOP_Chester_2019 | revid: 10257 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IOP Chester 2019
## Contents

- [1 Lectures](#Lectures)
- [2 Allocating Computing Nodes and Environment
  Setup](#Allocating_Computing_Nodes_and_Environment_Setup)
- [3 Submitting jobs](#Submitting_jobs)
- [4 Install sumo for post
  processing](#Install_sumo_for_post_processing)
- [5 Tutorials](#Tutorials)
- [6 Further Examples](#Further_Examples)
  - [6.1 Optimisation in the bulk](#Optimisation_in_the_bulk)
  - [6.2 Nudge Elastic Band Method and (constrained) Molecular
    Dynamics](#Nudge_Elastic_Band_Method_and_(constrained)_Molecular_Dynamics)
  - [6.3 Magnetism in NiO](#Magnetism_in_NiO)
  - [6.4 Surfaces and Interfaces](#Surfaces_and_Interfaces)

## Lectures
- [DFT, PW, and
  PAW](http://www.vasp.at/vasp-workshop/lectures/VASP_lecture_Basics1.pdf):
  "VASP: The basics. DFT, plane waves, PAW, ...".

&nbsp;

- [Hybrid
  functionals](http://www.vasp.at/vasp-workshop/lectures/VASP_lecture_Hybrids.pdf):
  "VASP: Hybrid functionals".

&nbsp;

- [Beyond DFT:
  RPA](http://www.vasp.at/vasp-workshop/lectures/VASP_lecture_RPA.pdf):
  "VASP: beyond DFT. The Random-Phase-Approximation".

&nbsp;

- [Geometry
  optimization](https://github.com/skelton-group/VASP-Workshop-Chester-2019):
  Tutorial on geometry optimisation by Dr. Jonathan Skelton.

&nbsp;

- [Surfaces and
  interfaces](http://www.vasp.at/vasp-workshop/lectures/VASP_lecture_Surfaces_Roldan.pdf)
  by Dr. Alberto Roldan.

&nbsp;

- [Electronic structure of materials surfaces and
  interfaces](http://www.vasp.at/vasp-workshop/lectures/VASP_lecture_Surfaces_Interfaces_Papadopoulos.pdf)
  by Dr. Theodoros Papadopoulos.

&nbsp;

- [Performance](http://www.vasp.at/vasp-workshop/lectures/VASP_lecture_HPC.pdf):
  "VASP: running on HPC resources".

## Allocating Computing Nodes and Environment Setup
An interactive shell should be allocated after login. The following
command allocates an interactive node with 8 CPUs for 90 minutes

    qsub -A y15 -q <queue> -IVl select=1:ncpus=8,walltime=01:30:00,place=scatter:excl

Here `<queue>` is `R1179799` for the 14:00-15:30 and `R1171601` for the
16:00-17:30 session, respectively. After successful allocation, one has
to setup the environment as follows.

To have access to the vasp binaries, the corresponding module has to be
loaded into the environment. Furthermore, the job scripts found in the
tutorial tar files (job.sh, doall.sh, etc) work only if the environment
variables "vasp_std, vasp_gam, vasp_ncl" are defined. Enter following
commands in the terminal window after login, to setup up the
environment.

    module load vasp/5.4.4-intel18-impi18-wannier90_1.2
    export vasp_ncl="mpirun -ppn 8 -np 8 /lustre/home/y07/vasp5/5.4.4-intel18-impi18/bin/vasp_ncl"
    export vasp_gam="mpirun -ppn 8 -np 8 /lustre/home/y07/vasp5/5.4.4-intel18-impi18/bin/vasp_gam"
    export vasp_std="mpirun -ppn 8 -np 8 /lustre/home/y07/vasp5/5.4.4-intel18-impi18/bin/vasp_std"

## Submitting jobs
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

## Install sumo for post processing
Sumo[\[1\]](https://sumo.readthedocs.io) can be used to plot band
structures and density of states. A local installation is possible with
following commands

    module load anaconda/python3
    pip install --user --upgrade pip
    pip3 install --user --upgrade scipy
    pip3 install --user --upgrade numpy
    pip3 install --user sumo

## Tutorials
All tutorial files can be extracted to your home folder as follows

    cd ~ ; mkdir examples 
    cd ~/examples
    cp /lustre/home/shared/VASP_Workshop_Chester/examples.tgz .
    tar -xvf examples.tgz

Electronic structure examples are located on the following folder on
cirrus:

    /lustre/home/shared/VASP_Workshop_Chester/COonNi111.zip

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

## Further Examples
#### Optimisation in the bulk
- [Exercises by Jonathan
  Skelton](https://github.com/skelton-group/VASP-Workshop-Chester-2019)

#### Nudge Elastic Band Method and (constrained) Molecular Dynamics
- [Liquid Si - Standard
  MD](Liquid_Si_-_Standard_MD.md)

&nbsp;

- [Transition State Search of
  Ammonia](Transition_State_Search_of_Ammonia.md)

&nbsp;

- [Adsorption of H2O on
  TiO2](Adsorption_of_H2O_on_TiO2.md)

#### Magnetism in NiO
- [NiO GGA](NiO_GGA.md)

&nbsp;

- [NiO GGA+U](NiO_GGA+U.md)

&nbsp;

- [NiO HSE06](NiO_HSE06.md)

&nbsp;

- [Estimation of J magnetic
  coupling](Estimation_of_J_magnetic_coupling.md)

&nbsp;

- [Including the Spin-Orbit
  Coupling](Including_the_Spin-Orbit_Coupling.md)

&nbsp;

- [Determining the Magnetic
  Anisotropy](Determining_the_Magnetic_Anisotropy.md)

&nbsp;

- [Constraining the local magnetic
  moments](Constraining_the_local_magnetic_moments.md)

### Surfaces and Interfaces
- [Exercises by Alberto Roldan
  Martinez](https://cf-my.sharepoint.com/:f:/g/personal/roldanmartineza_cardiff_ac_uk/EnHWVLFYBlBJnz4Wi6zsr6EB9TqWFsMyknAghU5iTYR8Ng?e=WDqUTz)
