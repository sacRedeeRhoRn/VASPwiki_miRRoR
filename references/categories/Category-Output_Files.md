<!-- Source: https://vasp.at/wiki/index.php/Category:Output_Files | revid: 14942 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Output Files
The main output file of VASP is the [OUTCAR](../output-files/OUTCAR.md). The
[vasprun.xml](../output-files/Vasprun.xml.md) contains similar
information but in an xml format. The [OSZICAR](../output-files/OSZICAR.md)
file contains the total energies of the electronic and ionic SCF steps,
and it is useful for the monitoring of the calculation.

When [HDF5 support](Category-HDF5_support.md)
is enabled, a [vaspout.h5](../output-files/Vaspout.h5.md) file is
produced containing the main results of the VASP calculation.

Here is a comprehensive list of all important output files:

|  |  |
|----|----|
| [BSEFATBAND](../output-files/BSEFATBAND.md) | BSE eigenvalues used for "fatband" plots. |
| [CHG](../output-files/CHG.md) | Contains charge density, lattice vectors and atomic coordinates. Should be used for visualization. |
| [CHGCAR](../input-files/CHGCAR.md) | Same as CHG but it contains also one-center occupancies. Should be used to restart VASP from existing charge density. |
| [CONTCAR](../output-files/CONTCAR.md) | Is the updated [POSCAR](../input-files/POSCAR.md) file after each calculation, whether ionic movement was performed or not. |
| [DOSCAR](../output-files/DOSCAR.md) | Contains DOS and integrated DOS. |
| [EIGENVAL](../output-files/EIGENVAL.md) | Contains Kohn-Sham eigenvalues for each k point after the end of the calculation. |
| [ELFCAR](../output-files/ELFCAR.md) | Contains electron localization function. |
| [IBZKPT](../output-files/IBZKPT.md) | Contains k-point coordinates and weights. |
| [LOCPOT](../output-files/LOCPOT.md) | Contains total local potential in eV. |
| [OSZICAR](../output-files/OSZICAR.md) | Information on each electronic and ionic SCF step. |
| [OUTCAR](../output-files/OUTCAR.md) | Main output file. |
| [PARCHG](../output-files/PARCHG.md) | Contains partial charge densities. |
| [PCDAT](../output-files/PCDAT.md) | Contains the pair correlation function. |
| [PROCAR](../output-files/PROCAR.md) | Contains spd and site-projected wave function character. |
| [PROOUT](../output-files/PROOUT.md) | Contains projection of wavefunction onto spherical harmonics. |
| [REPORT](../output-files/REPORT.md) | Contains output of various molecular dynamics caculations (umbrella integration, etc.). |
| [TMPCAR](../output-files/TMPCAR.md) | Contains wavefunction and ionic positions of previous ionic step. |
| [vasprun.xml](../output-files/Vasprun.xml.md) | Main output file in xml format. |
| [vaspout.h5](../output-files/Vaspout.h5.md) | Main output file in hdf5 format. Required for the postprocessing with [py4vasp](https://vasp.at/py4vasp/latest/index.html). |
| [vaspwave.h5](../output-files/Vaspwave.h5.md) | Contains charge density and wave functions when output is directed to hdf5. |
| [Wxxxx.tmp](../input-files/Wxxxx.tmp.md) | Contains diagonal elements of screened exchange in BSE calculations. |
| [WAVECAR](../input-files/WAVECAR.md) | Binary file containing information such as wave function coefficients, eigenvalues, Fermi weights, etc. |
| [WAVEDER](../input-files/WAVEDER.md) | Contains derivative of wave functions with respect to k point. |
| [WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md) | Store full screened exchange in BSE calculations. |
| [XDATCAR](../output-files/XDATCAR.md) | Contains ionic configuration for each output step of molecular dynamics simulations. |
