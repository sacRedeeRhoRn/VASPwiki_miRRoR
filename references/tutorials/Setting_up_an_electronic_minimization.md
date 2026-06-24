<!-- Source: https://vasp.at/wiki/index.php/Setting_up_an_electronic_minimization | revid: 37300 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Setting up an electronic minimization
Setting up an [electronic
minimization](../categories/Category-Electronic_minimization.md)
calculation using density-functional theory requires a few steps. The
[input files](../categories/Category-Input_files.md) must be
created or copied into the execution folder. This includes making a few
choices for the [**k**-point](../input-files/KPOINTS.md) sampling and
[electronic smearing](../incar-tags/ISMEAR.md), [minimization
algorithm](../incar-tags/ALGO.md), and [exchange-correlation
functionals](../categories/Category-Exchange-correlation_functionals.md).
A
[dry-run](../misc/Command-line_arguments.md)
can be used to review settings and select appropriate
[parallelization](../categories/Category-Parallelization.md)
tags. After running the calculation, the output can be analyzed.

## Contents

- [1 Step-by-step instructions](#Step-by-step_instructions)
  - [1.1 Create the input files](#Create_the_input_files)
  - [1.2 Optimize your settings](#Optimize_your_settings)
  - [1.3 Run the calculation](#Run_the_calculation)
- [2 Recommendations and advice](#Recommendations_and_advice)
- [3 Example](#Example)
  - [3.1 Setting up the POSCAR file](#Setting_up_the_POSCAR_file)
  - [3.2 Creating the POTCAR file](#Creating_the_POTCAR_file)
  - [3.3 Creating the KPOINTS file](#Creating_the_KPOINTS_file)
  - [3.4 Creating the INCAR file](#Creating_the_INCAR_file)
  - [3.5 Performing a dryrun](#Performing_a_dryrun)
  - [3.6 Running the calculation](#Running_the_calculation)
- [4 Related tags and articles](#Related_tags_and_articles)
- [5 References](#References)

## Step-by-step instructions
### Create the input files
**Step 1**: Create a [POSCAR](../input-files/POSCAR.md) file containing the
structure for which you want to compute the electronic groundstate.
External tools like VESTA^([\[1\]](#cite_note-vesta-1)), or Python
packages like the Atomic Simulation Environment
(ASE)^([\[2\]](#cite_note-ase-2)) or
pymatgen^([\[3\]](#cite_note-pymatgen-3)) can help with this step.

**Step 2**: [Choose an exchange-correlation (XC)
functional](../categories/Category-Exchange-correlation_functionals.md)
appropriate for your material and quantity of interest.

**Step 3**: Create a suitable [POTCAR](../input-files/POTCAR.md) file by
following the instructions on our [preparing a
POTCAR](Preparing_a_POTCAR.md) page.

**Step 4**: Create a [KPOINTS](../input-files/KPOINTS.md) file to define
the [integration mesh in reciprocal
space](../theory/Integrating_over_all_orbitals.md).
Including a single k point at the origin, i.e. the Gamma point, neglects
all interactions beyond the unit cell. This is appropriate for isolates
systems like a single molecule or in large supercells. For bulk systems,
start with a [regular
mesh](../input-files/KPOINTS.md). For shorter lattice
vectors, more k points are required to achieve the same sampling
density. Consult the [symmetry reduction
section](../input-files/KPOINTS.md) of the
[KPOINTS](../input-files/KPOINTS.md) page to select the appropriate mesh
type. Alternatively to a [KPOINTS](../input-files/KPOINTS.md) file, the
[KSPACING](../incar-tags/KSPACING.md) can be used.

**Step 5**: Write an [INCAR](../input-files/INCAR.md) file. It is
recommended to start from a rather minimal file, and only specify the
most important tags:

- [XC](../incar-tags/XC.md) to specify the [exchange-correlation
  functional](../categories/Category-Exchange-correlation_functionals.md).
- [ALGO](../incar-tags/ALGO.md) to select the algorithm for [electronic
  minimization](../categories/Category-Electronic_minimization.md).
- [ISMEAR](../incar-tags/ISMEAR.md) to select the type of [electronic
  smearing technique](Smearing_technique.md).
- [SIGMA](../incar-tags/SIGMA.md) to choose an appropriate smearing width
  of the [electronic
  smearing](Smearing_technique.md).
- [ENCUT](../incar-tags/ENCUT.md) to set the [plane-wave energy
  cutoff](../redirects/Energy_cut_off_and_FFT_mesh.md).
- [EDIFF](../incar-tags/EDIFF.md) to specify the global break condition for
  the electronic self-consistent loop

### Optimize your settings
**Step 6** (optional): Select the appropriate version of the VASP
executable. I.e. `vasp_gam` if you only want to use the Gamma point for
reciprocal space integration, `vasp_ncl` for [noncollinear
magnetic](../categories/Category-Noncollinear_magnetism.md)
calculations, or `vasp_std` for anything else. Then Run a
[dry-run](../misc/Command-line_arguments.md)
calculation to validate settings and uncover possible errors. Open a
terminal, go to the calculation directory that contains all input files
and run

     /path/to/your/vasp_std --dry-run

**Step 7** (optional): Inspect the [OUTCAR](../output-files/OUTCAR.md) file
of your
[dry-run](../misc/Command-line_arguments.md).
Take note of the number of bands, [NBANDS](../incar-tags/NBANDS.md), and
the number of **k**-points, NKPTS, especially. Follow the guidelines on
the [optimizing the
parallelization](Optimizing_the_parallelization.md)
page to set [NCORE](../incar-tags/NCORE.md) and/or
[KPAR](../incar-tags/KPAR.md) in the [INCAR](../input-files/INCAR.md) file.

### Run the calculation
**Step 8**: Run the calculation. If you are new to VASP, or unsure about
the calculation setup, run a small calculation and monitor the [screen
output](../redirects/Stdout.md). For parallel execution on 4 MPI ranks,
the command reads

     mpirun -np 4 /path/to/your/vasp_std

At an HPC center, submit your job with a submission script. Ask your
system administrator for help.

Once the calculation is finished, you have access to the [electronic
ground-state
properties](../categories/Category-Electronic_ground-state_properties.md)
via the [output
files](https://vasp.at/wiki/index.php/Category:Output_files) for the
selected parameters. Check the [OUTCAR](../output-files/OUTCAR.md) file for
warnings or advice. For help, consult the page about [troubleshooting
electronic
convergence](Troubleshooting_electronic_convergence.md)
and search our [Forum](https://www.vasp.at/forum/%7C) for similar
issues.

**Step 9** (convergence study): Repeat Steps 4 - 8 with increasingly
accurate parameter settings, e.g. higher cutoff energy and denser
k-points mesh, and monitor your quantity of interest. Stop if the
quantity of interest reaches the desired accuracy.

## Recommendations and advice
|  |
|----|
| **Mind:** Make sure to specify the lattice vectors and ionic positions in the [POSCAR](../input-files/POSCAR.md) with at least 7 digits of precision to ensure the [symmetry analysis](../input-files/POSCAR.md) can function accurately. |

[TABLE]

## Example
We will do a small DFT calculation of GaAs in the zincblende structure,
using the local-density approximation (LDA) with the Perdew-Zunger
parametrization of Ceperley-Alder Monte Carlo correlation
data.^([\[4\]](#cite_note-ceperley1980-4)[\[5\]](#cite_note-perdewzunger1981-5)).
Thus, our [XC
functional](../categories/Category-Exchange-correlation_functionals.md)
will be set to [`XC`](../incar-tags/XC.md)` = CA`.

### Setting up the [POSCAR](../input-files/POSCAR.md) file
The [POSCAR](../input-files/POSCAR.md) file starts with a comment line and
a scaling factor, which in our case corresponds to the lattice parameter
of GaAs, around 5.65 Angstrom.

    Zincblende GaAs
      5.65000000000

Next we need to define the lattice vectors. Zincblende is a
face-centered cubic (fcc) structure with two different elements in the
unit cell. We can describe the fcc lattice with three vectors, pointing
from the origin to the face-centers of the cube:

         0.0000000000000000  0.5000000000000000  0.5000000000000000
         0.5000000000000000  0.0000000000000000  0.5000000000000000
         0.5000000000000000  0.5000000000000000  0.0000000000000000

Now, we define the ion types, and in the line below the number of ions
in the structure for each type:

     Ga  As
      1   1

Specify the positions of the atoms in direct coordinates, with Ga at the
origin and As a quarter along the diagonal of the cube:

    Direct
      0.0000000000000000  0.0000000000000000  0.0000000000000000
      0.2500000000000000  0.2500000000000000  0.2500000000000000

This is the complete [POSCAR](../input-files/POSCAR.md) file:

    Zincblende GaAs
      5.65000000000
         0.0000000000000000  0.5000000000000000  0.5000000000000000
         0.5000000000000000  0.0000000000000000  0.5000000000000000
         0.5000000000000000  0.5000000000000000  0.0000000000000000
     Ga  As
      1   1
    Direct
      0.0000000000000000  0.0000000000000000  0.0000000000000000
      0.2500000000000000  0.2500000000000000  0.2500000000000000

If you have access to
[py4vasp](https://vasp.at/py4vasp/latest/index.html), the structure can
be visualized with two lines of Python code in a Jupyter notebook.

[![](https://vasp.at/wiki/images/thumb/1/16/GaAs_zincblende_py4vasp_2SC.png/400px-GaAs_zincblende_py4vasp_2SC.png)](https://vasp.at/wiki/File:GaAs_zincblende_py4vasp_2SC.png)

Visualization of the [POSCAR](../input-files/POSCAR.md) file of GaAs with
[py4vasp](https://vasp.at/py4vasp/latest/index.html).

    from py4vasp import calculation

    calculation.structure.plot(supercell=2,selection="POSCAR")

If ASE^([\[2\]](#cite_note-ase-2)) is installed, an equivalent
[POSCAR](../input-files/POSCAR.md) file can be created as follows:

    from ase.build import bulk
    from ase.io.vasp import write_vasp

    atoms = bulk("GaAs", crystalstructure="zincblende", a=5.65)
    write_vasp("POSCAR", atoms, direct=True, sort=False)

### Creating the [POTCAR](../input-files/POTCAR.md) file
We have already decided to use [`XC`](../incar-tags/XC.md)` = CA`, and can
create the [POTCAR](../input-files/POTCAR.md) file as discussed on the
[preparing a POTCAR](Preparing_a_POTCAR.md)
page.

### Creating the [KPOINTS](../input-files/KPOINTS.md) file
Since our structure is face-centered cubic, we create a [regular
Gamma-centered](../input-files/KPOINTS.md)
**k**-point mesh according to the [symmetry
considerations](../input-files/KPOINTS.md)
for [KPOINTS](../input-files/KPOINTS.md) files.

     Regular k-point mesh
       0
     Gamma
      7 7 7

### Creating the [INCAR](../input-files/INCAR.md) file
We chose the efficient combination of a [blocked-Davidson
algorithm](../theory/Blocked-Davidson_algorithm.md)
and the [RMM-DIIS](../theory/RMM-DIIS.md) algorithm which can be
selected with [`ALGO`](../incar-tags/ALGO.md)` = Fast`.

    ALGO = Fast

GaAs is a semiconductor, so we could use the tetrahedron method
[`ISMEAR`](../incar-tags/ISMEAR.md)` = -5`, but bandgaps are
underestimated systematically by DFT and XC functional or lattice
parameter may fail to reproduce experimental results. Thus, following
the recommendation on [electronic smearing
techniques](Smearing_technique.md),
it is safer to select Gaussian smearing and a small smearing width:

    ISMEAR = 0
    SIGMA = 0.1
    EFERMI = MIDGAP

For an initial guess of the plane-wave cutoff energy
[ENCUT](../incar-tags/ENCUT.md), we can search for
[ENMAX](../redirects/ENMAX.md) in the [POTCAR](../input-files/POTCAR.md),
e.g. by `grep ENMAX POTCAR`, and set the largest as a starting point. In
preceding calculations this value should be increased, e.g. by
increments of approximately 20%. Accordingly, in the first run we set:

    ENCUT = 285

For the break condition of the self-consistent loop, we select
$1\times10^{-6}$ eV:

    EDIFF = 1.0E-06

The complete [INCAR](../input-files/INCAR.md) file is:

    XC = CA
    ALGO = Fast
    ISMEAR = 0
    EFERMI = MIDGAP
    SIGMA = 0.1
    ENCUT = 285
    EDIFF = 1.0E-06

### Performing a dryrun
We are not doing a
[noncollinear](../categories/Category-Noncollinear_magnetism.md),
nor a Gamma-only calculation, thus we execute a VASP
[dry-run](../misc/Command-line_arguments.md)
with the standard executable:

    /your/vasp_dir/bin/vasp_std --dry-run

Which will print a warning about the
[dry-run](../misc/Command-line_arguments.md)
and some information about the MPI-ranks, OMP-threads, the VASP version,
and the input structure. Mistakes in the setup, e.g. if the order of
elements in the [POSCAR](../input-files/POSCAR.md) and
[POTCAR](../input-files/POTCAR.md) do not match, warnings are printed.

We can now check the [OUTCAR](../output-files/OUTCAR.md) file and find the
total number of **k**-points, 20, and number of bands
([NBANDS](../incar-tags/NBANDS.md)), 13. This means a relatively low
number of bands and a decent number of **k** points. If we want to run
our calculation on 4 MPI ranks, setting
[`KPAR`](../incar-tags/KPAR.md)` = 4` is an excellent choice for
parallelization. Mind that the [parallelization changes number of
bands](../incar-tags/NBANDS.md).

### Running the calculation
After adding [`KPAR`](../incar-tags/KPAR.md)` = 4` to the
[INCAR](../input-files/INCAR.md) file, we run the calculation on 4 MPI
ranks:

    mpirun -np 4 /your/vasp_dir/bin/vasp_std

Consult the page on [screen output](../redirects/Screen_output.md)
for details about the information VASP prints out. For this example it
should be similar to this:

     running    4 mpi-ranks, with    1 threads/rank, on    1 nodes
     distrk:  each k-point on    1 cores,    4 groups
     distr:  one band on    1 cores,    1 groups
     vasp.6.5.0 16Dec24 (build Dec 18 2024 11:18:52) complex                        
     
     POSCAR found type information on POSCAR GaAs
     POSCAR found :  2 types and       2 ions
     Reading from existing POTCAR
     scaLAPACK will be used
     Reading from existing POTCAR
     LDA part: xc-table for (Slater(with rela. corr.)+CA(PZ))
     , standard interpolation
     POSCAR, INCAR and KPOINTS ok, starting setup
     FFT: planning ... GRIDC
     FFT: planning ... GRID_SOFT
     FFT: planning ... GRID
     WAVECAR not read
     entering main loop
           N       E                     dE             d eps       ncg     rms          rms(c)
    DAV:   1     0.623500523606E+02    0.62350E+02   -0.70852E+03   528   0.135E+03
    DAV:   2    -0.533903918847E+01   -0.67689E+02   -0.65331E+02   580   0.246E+02
    DAV:   3    -0.978648308483E+01   -0.44474E+01   -0.44252E+01   635   0.613E+01
    DAV:   4    -0.985351010991E+01   -0.67027E-01   -0.67012E-01   614   0.819E+00
    DAV:   5    -0.985490478939E+01   -0.13947E-02   -0.13947E-02   641   0.931E-01    0.301E+00
    RMM:   6    -0.966994813504E+01    0.18496E+00   -0.21049E-01   715   0.453E+00    0.175E+00
    RMM:   7    -0.962995486843E+01    0.39993E-01   -0.10315E-01   701   0.182E+00    0.574E-01
    RMM:   8    -0.962647867206E+01    0.34762E-02   -0.12692E-02   740   0.127E+00    0.937E-02
    RMM:   9    -0.962642442346E+01    0.54249E-04   -0.21087E-03   757   0.536E-01    0.594E-02
    RMM:  10    -0.962647797834E+01   -0.53555E-04   -0.39237E-04   794   0.212E-01    0.167E-02
    RMM:  11    -0.962646653288E+01    0.11445E-04   -0.91747E-05   785   0.105E-01    0.529E-03
    RMM:  12    -0.962646808711E+01   -0.15542E-05   -0.17691E-05   735   0.426E-02    0.300E-03
    RMM:  13    -0.962646810096E+01   -0.13852E-07   -0.27033E-06   491   0.223E-02
       1 F= -.96264681E+01 E0= -.96264536E+01  d E =-.289650E-04
     writing wavefunctions

You can now use the [output
files](https://vasp.at/wiki/index.php/Category:Output_files) to analyze
the [electronic ground-state
properties](../categories/Category-Electronic_ground-state_properties.md).
Do not forget to perform a convergence study before reporting a value,
see [Step 9](#Step_9).

## Related tags and articles
[Input files](../categories/Category-Input_files.md):
[INCAR](../input-files/INCAR.md), [POSCAR](../input-files/POSCAR.md),
[KPOINTS](../input-files/KPOINTS.md), [POTCAR](../input-files/POTCAR.md),

[Parallelization](../categories/Category-Parallelization.md)

[Output files](https://vasp.at/wiki/index.php/Category:Output_files) and
[Electronic ground-state
properties](../categories/Category-Electronic_ground-state_properties.md)

## References
1.  [↑](#cite_ref-vesta_1-0) [https://jp-minerals.org/vesta/en/
    (2025).](https://jp-minerals.org/vesta/en/)
2.  ↑ ^([a](#cite_ref-ase_2-0)) ^([b](#cite_ref-ase_2-1))
    [https://wiki.fysik.dtu.dk/ase/
    (2025).](https://wiki.fysik.dtu.dk/ase/)
3.  [↑](#cite_ref-pymatgen_3-0) [https://pymatgen.org/
    (2022).](https://pymatgen.org/)
4.  [↑](#cite_ref-ceperley1980_4-0) [D. M. Ceperley and B. J. Alder,
    Phys. Rev. Lett. **45**, 566
    (1980).](https://doi.org/10.1103/PhysRevLett.45.566)
5.  [↑](#cite_ref-perdewzunger1981_5-0) [J. P. Perdew and A. Zunger,
    Phys. Rev. B **23**, 5048
    (1981).](https://doi.org/10.1103/PhysRevB.23.5048)
