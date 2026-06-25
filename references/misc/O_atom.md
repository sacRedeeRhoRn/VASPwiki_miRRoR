<!-- Source: https://vasp.at/wiki/index.php/O_atom | revid: 20410 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# O atom



[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
O
atom \> [O atom
spinpolarized](O_atom_spinpolarized.md) \>
[O atom spinpolarized low
symmetry](O_atom_spinpolarized_low_symmetry.md) \>
[O
dimer](O_dimer.md) \>
[CO](../incar-tags/CO.md) \> [CO
vibration](CO_vibration.md) \>
[CO partial
DOS](CO_partial_DOS.md) \>
[H2O](../incar-tags/H2O.md) \> [H2O
vibration](H2O_vibration.md) \>
[H2O molecular
dynamics](H2O_molecular_dynamics.md) \>
[Further things to try](At_and_mol_further.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#task)
- [2
  Input](#input)
  - [2.1
    POSCAR](#poscar)
  - [2.2
    INCAR](#incar)
  - [2.3
    KPOINTS](#kpoints)
- [3
  Calculation](#calculation)
  - [3.1
    stdout](#stdout)
  - [3.2
    OUTCAR](#outcar)
  - [3.3 Restart of
    the calculation](#restart-of-the-calculation)
- [4
  Download](#download)


## Task\[<a href="/wiki/index.php?title=O_atom&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Performing a standard calculation for a single oxygen atom in a box.
Getting to know the main input and output files of VASP.

  

## Input\[<a href="/wiki/index.php?title=O_atom&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a href="/wiki/index.php?title=O_atom&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    O atom in a box
     1.0          ! universal scaling parameters
     8.0 0.0 0.0  ! lattice vector  a(1)
     0.0 8.0 0.0  ! lattice vector  a(2)
     0.0 0.0 8.0  ! lattice vector  a(3)
    1             ! number of atoms
    cart          ! positions in cartesian coordinates
     0 0 0

We are using a POSCAR file with a single atom. Sufficiently large
lattice parameters are selected so that no (significant) interactions
between atoms in neighbouring cells is present.

### [INCAR](../input-files/INCAR.md)\[<a href="/wiki/index.php?title=O_atom&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    SYSTEM = O atom in a box
    ISMEAR = 0  ! Gaussian smearing

### [KPOINTS](../input-files/KPOINTS.md)\[<a href="/wiki/index.php?title=O_atom&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    Gamma-point only
     0
    Monkhorst Pack
     1 1 1
     0 0 0

For atoms or molecules a single k point is sufficient. When more k
points are used only the interaction between atoms (which should be
zero) is described more accurately.

## Calculation\[<a href="/wiki/index.php?title=O_atom&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

### stdout\[<a href="/wiki/index.php?title=O_atom&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: stdout">edit</a> \| (./index.php.md)\]


    running on    8 total cores
    distrk:  each k-point on    8 cores,    1 groups
    distr:  one band on    1 cores,    8 groups
    using from now: INCAR     
    vasp.5.4.1 05Feb16 (build Aug 22 2016 16:46:23) complex                        
    POSCAR found :  1 types and       1 ions
    scaLAPACK will be used
    LDA part: xc-table for Pade appr. of Perdew
    POSCAR, INCAR and KPOINTS ok, starting setup
    WARNING: small aliasing (wrap around) errors must be expected
    FFT: planning ...
    WAVECAR not read
    entering main loop
    N       E                     dE             d eps       ncg     rms          rms(c)
    DAV:   1     0.384469664751E+02    0.38447E+02   -0.96726E+02    16   0.293E+02
    DAV:   2     0.345965628955E+01   -0.34987E+02   -0.34942E+02    32   0.450E+01
    DAV:   3    -0.244485866931E+00   -0.37041E+01   -0.34307E+01    16   0.308E+01
    DAV:   4    -0.312557021227E+00   -0.68071E-01   -0.66914E-01    16   0.508E+00
    DAV:   5    -0.313520305300E+00   -0.96328E-03   -0.96311E-03    32   0.506E-01    0.286E-01
    DAV:   6    -0.314540466589E+00   -0.10202E-02   -0.17853E-03    16   0.332E-01    0.142E-01
    DAV:   7    -0.314637222361E+00   -0.96756E-04   -0.22710E-04    16   0.134E-01
    1 F= -.31463722E+00 E0= -.16037490E+00  d E =-.308525E+00
    writing wavefunctions

The example output (stdout) for the O atom was obtained using VASP
version 5.4.1. The initial charge corresponds to the charge of isolated
overlapping atoms ([POTCAR](../input-files/POTCAR.md) file). For the first
4 steps the charge remains fixed, then the charge is updated (*rms(c)*
column)

Short explanation of the symbols in the
[OSZICAR](../output-files/OSZICAR.md) and stdout file:

|  |  |
|----|----|
| N | iteration count |
| E | total energy |
| dE | change of total energy |
| d eps | change of the eigenvalues (fixed potential) |
| ncg | number of optimisation steps $\mathrm{H} \psi$ |
| rms | total residual vector $\sum_{nk} w_{k} f_{nk} (\mathrm{H} - \epsilon_{nk}) \psi_{nk}$ |
| rms(c) | charge density residual vector |


### [OUTCAR](../output-files/OUTCAR.md)\[<a href="/wiki/index.php?title=O_atom&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: OUTCAR">edit</a> \| (./index.php.md)\]

The individual parts of the [OUTCAR](../output-files/OUTCAR.md) file are
separated by lines.

    ----------------------------------------------------------

The [OUTCAR](../output-files/OUTCAR.md) file is divided into the following
parts:

- Reading [INCAR](../input-files/INCAR.md), [POTCAR](../input-files/POTCAR.md),
  [POSCAR](../input-files/POSCAR.md)

<!-- -->

- Nearest neighbor distances and analysis of symmetry

<!-- -->

- Verbose job information

<!-- -->

- Information on lattice, k points and positions

<!-- -->

- Information on the basis set (number of plane waves)

<!-- -->

- Non-local pseudo potential information

<!-- -->

- Information for each electronic step (one line in
  [OSZICAR](../output-files/OSZICAR.md))

<!-- -->

- Timing and energy information

<!-- -->

       POTLOK:  cpu time    0.0878: real time    0.0877
       SETDIJ:  cpu time    0.0015: real time    0.0014
        EDDAV:  cpu time    0.0267: real time    0.0434
          DOS:  cpu time    0.0001: real time    0.0001
       --------------------------------------------
         LOOP:  cpu time    0.1165: real time    0.1346
       
    eigenvalue-minimisations :    16
    total energy-change (2. order) : 0.3844697E+02  (-0.9672571E+02)
    number of electron       6.0000000 magnetization
    augmentation part        6.0000000 magnetization
        
    Free energy of the ion-electron system (eV)      
     ---------------------------------------------------
     alpha Z        PSCENC =         0.27135287
     Ewald energy   TEWEN  =       -91.92708002
     -Hartree energ DENC   =      -281.84385691
     -exchange      EXHF   =         0.00000000
     -V(xc)+E(xc)   XCENC  =        26.11948841
     PAW double counting   =       245.99840262     -247.84808825
     entropy T*S    EENTRO =        -0.08636665
     eigenvalues    EBANDS =       -44.50008162
     atomic energy  EATOM  =       432.26319604
     Solvation  Ediel_sol  =         0.00000000
     ---------------------------------------------------
     free energy    TOTEN  =        38.44696648 eV
        
     energy without entropy =       38.53333313  energy(sigma->0) =       38.49014980

- Information on the Eigenvalues

<!-- -->

    E-fermi :  -8.8431     XC(G=0):  -0.8043     alpha+bet : -0.1463
    k-point     1 :       0.0000    0.0000    0.0000
    band No.  band energies     occupation
    1     -23.8439      2.00000
    2      -8.9040      1.33333
    3      -8.9040      1.33333
    4      -8.9040      1.33333
    5      -0.4676      0.00000
    6       1.8633      0.00000
    7       1.8633      0.00000
    8       1.8633      0.00000

- Information on stress tensor

<!-- -->

    The O atom (Example: Oatom)
    FORCE on cell =-STRESS in cart. coord.  units (eV):
    Direction    XX          YY          ZZ          XY          YZ          ZX
    --------------------------------------------------------------------------------------
    Alpha Z     0.27135     0.27135     0.27135
    Ewald     -30.64236   -30.64236   -30.64236     0.00000     0.00000     0.00000
    Hartree    93.90244    93.90244    93.90244    -0.00000    -0.00000    -0.00000
    E(xc)     -27.93035   -27.93035   -27.93035    -0.00000    -0.00000    -0.00000
    Local    -147.86211  -147.86211  -147.86211     0.00000     0.00000     0.00000
    n-local   -20.54942   -20.54942   -20.54942    -0.00000    -0.00000    -0.00000
    augment     5.55366     5.55366     5.55366     0.00000    -0.00000     0.00000
    Kinetic   126.50998   126.50998   126.50997    -0.00000     0.00000    -0.00000
    Fock        0.00000     0.00000     0.00000     0.00000     0.00000     0.00000
    -------------------------------------------------------------------------------------
    Total      -0.74681    -0.74681    -0.74681     0.00000    -0.00000    -0.00000
    in kB      -2.33695    -2.33695    -2.33695     0.00000    -0.00000    -0.00000
    external pressure =       -2.34 kB  Pullay stress =        0.00 kB

- Information on the energy

<!-- -->

    FREE ENERGIE OF THE ION-ELECTRON SYSTEM (eV)
    ---------------------------------------------------
    free  energy   TOTEN  =        -0.31463722 eV
    energy  without entropy=       -0.00611258  energy(sigma->0) =       -0.16037490

  
The relevant energy for molecules and atoms is energy without entropy.

    energy  without entropy=     -0.00611258  energy(sigma->0) =     -0.16037490

Three degenerate p orbitals are occupied by 2/3 electrons causing an
unphysical electronic entropy

    entropy T*S    EENTRO =      -0.30852464

A tiny value of [SIGMA](../incar-tags/SIGMA.md)=0.01 would reduce the
entropy but might slow convergence (default is
[SIGMA](../incar-tags/SIGMA.md)=0.2). [SIGMA](../incar-tags/SIGMA.md) controls
the electronic temperature, which is not a very meaningful quantity for
molecules and atoms.

The total energy is found to be essentially zero. VASP subtracts from
any calculated energy the energy of the atom in the configuration for
which the pseudo potential was generated. All pseudo potentials were
generated using non spin-polarized reference atoms.

### Restart of the calculation\[<a href="/wiki/index.php?title=O_atom&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Restart of the calculation">edit</a> \| (./index.php.md)\]

When VASP is restarted the [WAVECAR](../input-files/WAVECAR.md) file is
read and the run is continued from the previous wave functions
(converging rapidly).

    running on    8 total cores
    distrk:  each k-point on    8 cores,    1 groups
    distr:  one band on    1 cores,    8 groups
    using from now: INCAR
    vasp.5.4.1 05Feb16 (build Aug 22 2016 16:46:23) complex
      
    POSCAR found :  1 types and       1 ions
    scaLAPACK will be used
    LDA part: xc-table for Pade appr. of Perdew
    found WAVECAR, reading the header
    POSCAR, INCAR and KPOINTS ok, starting setup
    WARNING: small aliasing (wrap around) errors must be expected
    FFT: planning ...
    reading WAVECAR
    the WAVECAR file was read successfully
    initial charge from wavefunction
    entering main loop
          N       E                     dE             d eps       ncg     rms          rms(c)
    DAV:   1    -0.314680766875E+00   -0.31468E+00   -0.83090E-05    16   0.564E-02    0.107E-02
    DAV:   2    -0.314677281013E+00    0.34859E-05   -0.10030E-05    16   0.198E-02
      1 F= -.31467728E+00 E0= -.16041496E+00 d E =-.308525E+00
    writing wavefunctions

## Download\[<a href="/wiki/index.php?title=O_atom&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/7/7a/Oatom.tgz" class="internal"
title="Oatom.tgz">Oatom.tgz</a>


[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
O
atom \> [O atom
spinpolarized](O_atom_spinpolarized.md) \>
[O atom spinpolarized low
symmetry](O_atom_spinpolarized_low_symmetry.md) \>
[O
dimer](O_dimer.md) \>
[CO](../incar-tags/CO.md) \> [CO
vibration](CO_vibration.md) \>
[CO partial
DOS](CO_partial_DOS.md) \>
[H2O](../incar-tags/H2O.md) \> [H2O
vibration](H2O_vibration.md) \>
[H2O molecular
dynamics](H2O_molecular_dynamics.md) \>
[Further things to try](At_and_mol_further.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


Back to the [main page](The_VASP_Manual.md).


