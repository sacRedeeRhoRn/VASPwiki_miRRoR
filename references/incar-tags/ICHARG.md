<!-- Source: https://vasp.at/wiki/index.php/ICHARG | revid: 37119 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ICHARG
ICHARG = 0 \| 1 \| 2 \| 4 \| 5 

|                     |     |                                      |
|---------------------|-----|--------------------------------------|
| Default: **ICHARG** | = 2 | if [ISTART](ISTART.md)=0 |
|                     | = 0 | else                                 |

Description: ICHARG determines how VASP constructs the *initial* charge
density.

------------------------------------------------------------------------

- ICHARG=0

Calculate the charge density from initial wave functions.

If [ISTART](ISTART.md) is *internally reset* due to an
invalid [WAVECAR](../input-files/WAVECAR.md) file, ICHARG will be set to
ICHARG=2.

|                                                                    |
|--------------------------------------------------------------------|
| **Warning:** This may cause convergence problems for some systems. |

- ICHARG=1

Read the charge density from [CHGCAR](../input-files/CHGCAR.md) file, and
extrapolate from the old positions (on [CHGCAR](../input-files/CHGCAR.md))
to the new positions using a linear combination of atomic charge
densities.

In the [PAW
method](../methods/Projector-augmented-wave_formalism.md),
there is, however, one important point to keep in mind: For the on-site
densities (that is, the densities within the PAW sphere), only
l-decomposed charge densities up to [LMAXMIX](LMAXMIX.md)
are written. Upon restart, the energies might, therefore, differ
slightly from the fully converged energies. The discrepancies can be
large for the DFT+U method. In this case, one might need to increase
[LMAXMIX](LMAXMIX.md) to 4 (d-elements) or even 6
(f-elements).

When [METAGGA](METAGGA.md) is performed VASP also reads the
[TAUCAR](../input-files/TAUCAR.md) file if present. The kinetic energy
density from [TAUCAR](../input-files/TAUCAR.md) is used to initialize
meta-GGA calculations. Warning: if no [TAUCAR](../input-files/TAUCAR.md)
file is present, VASP will start with an empty kinetic energy density
that is updated upon the first charge density update after the
[NELMDL](NELMDL.md) delay phase.

|  |
|----|
| **Tip:** To improve convergence and reduce the number of electronic steps, it is recommended to set ICHARG = 1 when starting calculations repeatedly with small changes in the input parameters. |

- ICHARG=2

Take superposition of atomic charge densities.

- ICHARG=4

Read potential from file [POT](../output-files/POT.md). The local potential on
the file [POT](../output-files/POT.md) is written by the
optimized-effective-potential methods (OEP), if the flag
[LVTOT](LVTOT.md)=.TRUE. is supplied in the
[INCAR](../input-files/INCAR.md) file. Supported as of VASP.5.1.

- ICHARG=5

External charge-density-update mode to read in and add an external
correction to the Kohn-Sham (KS) occupations in every SCF step of the
[electronic
minimization](../redirects/Electronic_minimization.md).
The initialization of the charge density is done as in ICHARG=1, and
after [NELMDL](NELMDL.md) steps VASP reads the occupations
from a user-supplied text file [GAMMA](../input-files/GAMMA.md) (or
[vaspgamma.h5](../input-files/Vaspgamma.h5.md) if compiled with [HDF5
support](../categories/Category-HDF5_support.md)) for each
k point in each SCF step. The procedure described in
Ref.^([\[1\]](#cite_note-schueler:jpcm:30-1)) Eq. (30)-(32) is then used
to construct a new charge density from the combined occupations (KS
occupations + [GAMMA](../input-files/GAMMA.md) file), from which the next KS
potential is constructed. The [DFT
workflow](../redirects/Electronic_minimization.md)
continues after a user-supplied [vasp.lock](../input-files/Vasp.lock.md)
file is read. Additionally, with ICHARG=5 after each SCF step VASP
writes out all with [LOCPROJ](LOCPROJ.md) defined wave
function projections. The ICHARG=5 mode can be used with an external
code that modifies the occupations, and requires extra output after each
SCF step. The TRIQS software
package^([\[2\]](#cite_note-parcollet:cpc:196-2)) makes use of it to
perform charge self-consistent DFT plus dynamical mean field theory
(DMFT)
calculations^([\[3\]](#cite_note-merkel:joss:7-3)[\[4\]](#cite_note-aichhorn:cpc:204-4)).
See the
[DFT+DMFT](../tutorials/DFT+DMFT_calculations.md) howto
page for a tutorial.

- ICHARG=10

non-selfconsistent calculations: Adding 10 to the value of ICHARG, e.g.,
ICHARG=11 or 12 (or the less convenient value 10) means that the charge
density will be kept constant during the *entire electronic
minimization*.

There are several reasons why to keep the charge density constant:

- ICHARG=11

To obtain the eigenvalues (for band-structure plots) or the density of
states (DOS) of a given charge density read from
[CHGCAR](../input-files/CHGCAR.md). The self-consistent
[CHGCAR](../input-files/CHGCAR.md) file must be determined beforehand by a
fully self-consistent calculation with a k-point grid spanning the
entire Brillouin zone.

- ICHARG=12

Non-self-consistent calculations for a superposition of atomic charge
densities. This is in the spirit of the non-self-consistent
[Harris-Foulkes
functional](../methods/Harris-Foulkes_functional.md).
The stress and the forces calculated by VASP are correct, and it is
possible to perform an ab-initio MD for the non-selfconsistent
[Harris-Foulkes
functional](../methods/Harris-Foulkes_functional.md).

|  |
|----|
| **Tip:** If ICHARG is set to 11 or 12, it is strongly recommended to set [LMAXMIX](LMAXMIX.md) to twice the maximum l-quantum number in the pseudopotentials. Thus, for s and p elements [LMAXMIX](LMAXMIX.md) should be set to 2, for d elements [LMAXMIX](LMAXMIX.md) should be set to 4, and for f elements [LMAXMIX](LMAXMIX.md) should be set to 6. |

The initial charge density is of importance in the following cases:

- If ICHARG≥10 the charge density remains constant during the run.

&nbsp;

- For all algorithms except [IALGO](IALGO.md)=5X the initial
  charge density is used to set up the initial Hamiltonian that is used
  in the first few non-selfconsistent steps, c.f.,
  [NELMDL](NELMDL.md) tag.

## Related tags and articles
[Restart and output files cheat
sheet](../tutorials/Restart_and_output_files_cheat_sheet.md)

[CHGCAR](../input-files/CHGCAR.md), [TAUCAR](../input-files/TAUCAR.md),
[ISTART](ISTART.md), [LCHARG](LCHARG.md),
[LMAXMIX](LMAXMIX.md), [NELMDL](NELMDL.md),
[INIWAV](INIWAV.md), [GAMMA](../input-files/GAMMA.md),
[vaspgamma.h5](../input-files/Vaspgamma.h5.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ICHARG-_incategory-Examples)

------------------------------------------------------------------------

1.  [↑](#cite_ref-schueler:jpcm:30_1-0) [M. Schüler, O. E. Peil, G. J.
    Kraberger, R. Pordzik, M. Marsman, G. Kresse, T. O. Wehling, and M.
    Aichhorn, Journal of Physics: Condensed Matter **30**, 475901
    (2018).](https://doi.org/10.1088/1361-648X/aae80a)
2.  [↑](#cite_ref-parcollet:cpc:196_2-0) [O. Parcollet, M. Ferrero, T.
    Ayral, H. Hafermann, I. Krivenko, L. Messio and P. Seth, Computer
    Physics Communications **196**, 398
    (2015).](http://dx.doi.org/10.1016/j.cpc.2015.04.023)
3.  [↑](#cite_ref-merkel:joss:7_3-0) [M. E. Merkel, A. Carta, S. Beck
    and Alexander Hampel, Journal of Open Source Software **7**, 77
    (2022).](https://doi.org/10.21105/joss.04623)
4.  [↑](#cite_ref-aichhorn:cpc:204_4-0) [M. Aichhorn, L. Pourovskii, P.
    Seth, V. Vildosola, M. Zingl, O. E. Peil, X. Deng, J. Mravlje, G. J.
    Kraberger, C. Martins, M. Ferrero, O. Parcollet, Computer Physics
    Communications **204**, 200
    (2016).](https://doi.org/10.1016/j.cpc.2016.03.014)
