<!-- Source: https://vasp.at/wiki/index.php/Supercell_core-hole_calculations | revid: 30742 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Supercell core-hole calculations
The SCH
approach^([\[1\]](#cite_note-karsai:prb:2018-1)[\[2\]](#cite_note-unzog:prb:2022-2))
is explained in detail on the following [theory
page](../theory/Supercell_core-hole_theory.md).
When the core hole is explicitly introduced in one of the atoms, i.e., a
core electron is removed, it is necessary to eliminate the effective
interaction of the core hole with its image across the periodic
boundary. That requires using a large supercell so that this interaction
is negligible. After the self-consistent electronic minimization is
converged in the presence of the core hole, the dielectric function is
calculated using Fermi's golden rule.

Two different approaches can be used to treat the excited electron. The
excited electron can be placed into the lowest conduction band in the
**excited electron and core-hole
(XCH)**^([\[3\]](#cite_note-hetenyi:jcp:2004-3)) approach, alternatively
the excited electron can be accounted for by a negative background
charge in the **full core-hole (FCH)**
^([\[4\]](#cite_note-Prendergasst:prl:2006-4)) method.

## Contents

- [1 Pre-calculation](#Pre-calculation)
- [2 Calculation](#Calculation)
- [3 INCAR tags](#INCAR_tags)
  - [3.1 Example INCAR](#Example_INCAR)
  - [3.2 Core hole tags](#Core_hole_tags)
  - [3.3 XAS tags](#XAS_tags)
  - [3.4 Other important tags](#Other_important_tags)
- [4 Output](#Output)
  - [4.1 OUTCAR](#OUTCAR)
  - [4.2 vaspout.h5](#vaspout.h5)
  - [4.3 vasprun.xml](#vasprun.xml)
- [5 References](#References)

## Pre-calculation
To run a successful calculation you have to make the following
preliminary steps:

**Step 1.** Make a super cell for structure

To minimize the interaction between core holes from neighboring cells
the supercell size has to be converged. The convergence is very material
dependent and has to be in principle done every time for a new material.
It is best to do a bottom-up approach, beginning with the from the small
cell.

|  |
|----|
| **Mind:** Although by increasing the cell size the k mesh is implicitly also increased it still has to be also converged since the spectrum can depend also very strongly on the k points. |

**Step 2.** Select one atom in the file that will carry the core-hole
and provide a POTCAR file for that atom After making the super cell, one
atom has to be made to a new species with a single atom in it that will
carry the core-hole. The initial line for the number of atoms and atoms
for example can look like this

    Mg O
    32 32

If we are for example interested in the K-edge spectrum of Mg, we would
have to change the [POSCAR](../input-files/POSCAR.md) file as follows

    Mg Mg O
    1 31 32

Since we create a new species this way we need the
[POTCAR](../input-files/POTCAR.md) information for it. This is very easily
done by taking the [POTCAR](../input-files/POTCAR.md) file for the same
species and concatenating it to the [POTCAR](../input-files/POTCAR.md)
carrying all species: i.e. *cat POTCAR_Mg POTCAR*.

The procedure for oxygen would be very similar:

    Mg O O
    32 31 1

and *cat POTCAR POTCAR_O*.

|  |
|----|
| **Mind:** One typical source of error is that the additional [POTCAR](../input-files/POTCAR.md) is not added to the main [POTCAR](../input-files/POTCAR.md) file or that the order of species is not the same in the [POSCAR](../input-files/POSCAR.md) and [POTCAR](../input-files/POTCAR.md) files. |

|  |
|----|
| **Warning:** It is strongly recommended to use the available GW PAW potentials for the [POTCAR](../input-files/POTCAR.md) files, since many standard potentials don't have projectors with quantum numbers 2 or larger and the GW potentials are more exact for excited states than the standard potentials. |

## Calculation
The supercell core-hole calculations (SCH) consist in principle of two
steps:

- Self-consistent electronic cycle with a core hole.
- Calculation of the dielectric function of the core electron with the
  band structure from the SCF run.

In VASP these two steps are all done in a single calculation.

**Step 3. (optional)** Checking calculational parameters in advance

To check calculational paramaters such as e.g. number of bands, number
of irreducible k-points, number of electrons, etc. VASP can be run in a
dry mode which doesn't do any "actual" calculations but only does the
setup up steps:

    vasp_executable --dry-run 

This is often needed in SCH calculations, so whenever in the following
one is instructed to increase or decrease a parameter it is useful to
run VASP in dry mode before to get the reference value,
`e.g. grep NELECT OUTCAR` to find the number of electrons
[NELECT](../incar-tags/NELECT.md) to be specified in the
[INCAR](../input-files/INCAR.md) file.

**Step 4.** Calculate the XAS spectrum for varying cell sizes

Run a SCH calculation using for several different super cells,
increasing until convergence is achieved.

[TABLE]

**Step 5.** Compare to experiment

If experimental data is available, try comparing to it. The peak maxima
are unlikely to align, so you will need to shift the calculated spectra
to compare with experiment.

## INCAR tags
There are several tags that are required to run an SCH calculation.

### Example INCAR
An example input for the 2s K-edge of Mg in MgO would look like the
following:

     CH_LSPEC=.TRUE
     CH_NEDOS=1000
     CH_SIGMA=0.3
     ICORELEVEL=2
     CLNT=1
     CLN=2
     CLL=0
     CLZ=1.0
     CH_AMPLIFICATION=32.0
     NBANDS=600
     SIMGA=0.1
     ISMEAR=0

### Core hole tags
- [ICORELEVEL](../incar-tags/ICORELEVEL.md): To enable core-hole
  calculations in the final-state approximation with self-consistent
  field cycles (SCF) one has to set
  [ICORELEVEL](../incar-tags/ICORELEVEL.md)=2. Core-hole calculations
  in the initial-state approximation
  ([ICORELEVEL](../incar-tags/ICORELEVEL.md)=1) are also available,
  but they are physically less relevant and should be only used if
  especially needed.
- [CLNT](../incar-tags/CLNT.md): This tag selects the species holding the
  core hole. This number corresponds to the species defined in the
  [POSCAR](../input-files/POSCAR.md) and [POTCAR](../input-files/POTCAR.md)
  files.
- [CLN](../incar-tags/CLN.md): Specifies the $n$ quantum number of the excited electron.
- [CLL](../incar-tags/CLL.md): Specifies the $l$ quantum number of the excited electron.
- [CLZ](../incar-tags/CLZ.md): Specifies how much of a fraction of the chosen
  electron should be excited. Usually one always sets
  [CLZ](../incar-tags/CLZ.md)=1.0, but in some cases values lesser than 1 can
  lead to better agreement with experiment. However, this should be
  handled with caution since the physics behind is very dubious.

### XAS tags
- [CH_LSPEC](../incar-tags/CH_LSPEC.md): To obtain X-ray absorption
  spectra (XAS) the following flag has to be set
  [CH_LSPEC](../incar-tags/CH_LSPEC.md)=*.TRUE.*.
- [CH_SIGMA](../incar-tags/CH_SIGMA.md): The broadening of the spectrum
  is by default of Gaussian form and the broadening width in eV is set
  by [CH_SIGMA](../incar-tags/CH_SIGMA.md). We recommend using a very
  small broadening
  [CH_SIGMA](../incar-tags/CH_SIGMA.md)$\le$0.001 in the calculations and to broaden the spectrum in
  post-processing. Also, the spectrum can be recalculated with different
  parameters without the need to redo the electronic self-consistent
  field cycle. For that one can use the converged
  [WAVECAR](../input-files/WAVECAR.md) from the previous calculation and
  set [ALGO](../incar-tags/ALGO.md)=*None* together with the new parameters
  for the spectrum "CH\_\*" in the [INCAR](../input-files/INCAR.md) file.
- [CH_NEDOS](../incar-tags/CH_NEDOS.md): Sets the number of grid points
  on the energy axis of the spectrum.
- [CH_AMPLIFICATION](../incar-tags/CH_AMPLIFICATION.md): Scaling
  of the spectrum by the specified value. This tag is not important but
  can be useful sometimes if one needs to scale the spectrum a priori.
  Otherwise, it is recommended to scale the spectrum a posteriori.

### Other important tags
- [NBANDS](../incar-tags/NBANDS.md): Number of bands in the calculation.
  This parameter usually needs to be significantly increased compared to
  standard DFT calculations, since it sets the number of bands available
  in the calculation into which the core electron can be excited.
- [ISMEAR](../incar-tags/ISMEAR.md): This sets the type of smearing
  (broadening) in the electronic calculation. Mind that there is also a
  second broadening when calculating the spectrum, which is currently
  always of Gaussian form. Both broadenings affect the form of the
  spectrum.
- [SIGMA](../incar-tags/SIGMA.md): Sets the smearing (broadening) width in
  eV within the electronic calculation.

## Output
The dielectric function is written to the following files:

- [OUTCAR](../output-files/OUTCAR.md)
- [vaspout.h5](../output-files/Vaspout.h5.md)
- [vasprun.xml](../output-files/Vasprun.xml.md)

  
Usually for an absorption spectrum all six components of the dielectric
tensor are summed up. In most cases the obtained spectrum needs further
processing via an energy dependent broadening.

### OUTCAR
The frequency dependent dielectric tensor, which is directly
proportional to the absorption spectrum, is written to the
[OUTCAR](../output-files/OUTCAR.md) file. It starts with the following
lines:

      frequency dependent IMAGINARY DIELECTRIC FUNCTION (independent particle, no local field effects) density-density
        E(ev)      X         Y         Z        XY        YZ        ZX
     --------------------------------------------------------------------------------------------------------------

The energies of the excitations are with respect to the energy levels of
the core electron of interest. The start of the output of the dielectric
function with respect to excitation energy is set slightly below the
first peak to avoid many zeros over a large energy range, since core
states have very large binding energies.

### vaspout.h5
The energies of the excitations are with respect to the energy levels of
the core electron of interest.

### vasprun.xml
The energies of the excitations are with respect to the highest occupied
bands (without the core hole).

## References
1.  [↑](#cite_ref-karsai:prb:2018_1-0) [F. Karsai, M. Humer, E.
    Flage-Larsen, P. Blaha, and G. Kresse, Phys. Rev. B **98**, 235205
    (2018).](https://doi.org/10.1103/PhysRevB.98.235205)
2.  [↑](#cite_ref-unzog:prb:2022_2-0) [M. Unzog, A. Tal, G. Kresse,
    *X-ray absorption using the projector augmented-wave method and the
    Bethe-Salpeter equation*, Phys. Rev. B **106**, 155133
    (2022).](http://doi.org/10.1103/PhysRevB.106.155133)
3.  [↑](#cite_ref-hetenyi:jcp:2004_3-0) [B. Hetényi, F. De Angelis, P.
    Giannozzi, and R. Car, *Calculation of near-edge x-ray-absorption
    fine structure at finite temperatures: spectral signatures of
    hydrogen bond breaking in liquid water* , J. Chem. Phys. **120**,
    8632 (2004).](https://doi.org/10.1063/1.1703526)
4.  [↑](#cite_ref-Prendergasst:prl:2006_4-0) [D. Prendergasst and G.
    Galli, *X-Ray Absorption Spectra of Water from First Principles
    Calculations*, Phys. Rev. Lett. **96**, 215502
    (2006).](https://doi.org/10.1103/PhysRevLett.96.215502)
