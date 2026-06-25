<!-- Source: https://vasp.at/wiki/index.php/CRPA_of_SrVO3 | revid: 36492 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CRPA of SrVO3



[Overview](../tutorials/GW_and_ACFDT_-_Tutorial.md) \>
[bandgap of Si in
GW](Bandgap_of_Si_in_GW.md) \>
[bandstructure of Si in GW
(VASP2WANNIER90)](https://vasp.at/wiki/index.php/Bandstructure_of_Si_in_GW_(VASP2WANNIER90) "Bandstructure of Si in GW (VASP2WANNIER90)") \>
[bandstructure of SrVO3 in
GW](Bandstructure_of_SrVO3_in_GW.md)
 \>
CRPA of SrVO3
 \> [Equilibrium volume of Si
in the
RPA](Equilibrium_volume_of_Si_in_the_RPA.md) \>
[List of tutorials](../categories/Category-Tutorials.md)


The following tutorial describes how to perform [cRPA
calculations](../theory/Constrained–random-phase–approximation_formalism.md),
which is available as of VASP 6.


## Contents


- [1
  Task](#task)
- [2 DFT
  groundstate calculation](#dft-groundstate-calculation)
- [3 Obtain DFT
  virtual orbitals and long-wave
  limit](#obtain-dft-virtual-orbitals-and-long-wave-limit)
- [4 cRPA
  Calculation](#crpa-calculation)
  - [4.1 cRPA
    calculation on Matsubara
    axis](#crpa-calculation-on-matsubara-axis)
    - [4.1.1
      Optional: Analytic
      continuation](#optional-analytic-continuation)
- [5 Off-centre
  Coulomb integrals](#off-centre-coulomb-integrals)
- [6
  Downloads](#downloads)
- [7
  References](#references)


## Task\[<a
href="/wiki/index.php?title=CRPA_of_SrVO3&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the Coulomb matrix elements $U_{ijkl}(\omega=0)$ in the constrained Random Phase Approximation
(<a href="/wiki/Constrained-random-phase_approximation"
class="mw-redirect"
title="Constrained-random-phase approximation">cRPA</a>) of
SrVO<sub>3</sub> between the Vanadium t<sub>2g</sub> states.

------------------------------------------------------------------------

Performing a cRPA calculation with VASP is a 3-step procedure: a DFT
groundstate calculation, a calculation to obtain a number of virtual
orbitals, and the actual cRPA calculation itself.

**N.B.:** This example involves quite a number of individual
calculations. The easiest way to run this example is to execute:

    ./doall.sh

In any case, one can consider the `doall.sh` script to be an overview of
the steps described below.

## DFT groundstate calculation\[<a
href="/wiki/index.php?title=CRPA_of_SrVO3&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: DFT groundstate calculation">edit</a> \| (./index.php.md)\]

The first step is a conventional DFT (in this case PBE) groundstate
calculation.

- [INCAR](../input-files/INCAR.md) (see INCAR.DFT)

<!-- -->

    SYSTEM  = SrVO3    # system name
    NBANDS = 36        # small number of bands
    ISMEAR = -1        # Fermi smearing
    SIGMA = 0.1        # electronic temperature in eV (1eV ~ 11604K)
    EDIFF = 1E-8       # high precision for groundstate calculation
    KPAR = 2           # parallelization of k-points in two groups

Copy the aforementioned file to [INCAR](../input-files/INCAR.md):

    cp INCAR.DFT INCAR

The [POSCAR](../input-files/POSCAR.md) file describes the structure of the
system:

- [POSCAR](../input-files/POSCAR.md)

<!-- -->

    SrVO3
    3.84652  #cubic fit for 6x6x6 k-points
     +1.0000000000  +0.0000000000  +0.0000000000 
     +0.0000000000  +1.0000000000  +0.0000000000 
     +0.0000000000  +0.0000000000  +1.0000000000 
    Sr V O
     1 1 3
    Direct
     +0.0000000000  +0.0000000000  +0.0000000000 
     +0.5000000000  +0.5000000000  +0.5000000000 
     +0.5000000000  +0.5000000000  +0.0000000000 
     +0.5000000000  +0.0000000000  +0.5000000000 
     +0.0000000000  +0.5000000000  +0.5000000000

This file remains unchanged in the following.

The [KPOINTS](../input-files/KPOINTS.md) file describes how the first
Brillouin zone is sampled. In the first step we use a uniform k-point
sampling:

- [KPOINTS](../input-files/KPOINTS.md)

<!-- -->

    Automatically generated mesh
     0
    Gamma
     4 4 4
     0 0 0

**Mind**: this is definitely not dense enough for a high-quality
description of SrVO<sub>3</sub>, but in the interest of speed we will
live with it.

Run VASP. If all went well, one should obtain a
[WAVECAR](../input-files/WAVECAR.md) file containing the PBE wavefunction.

## Obtain DFT virtual orbitals and long-wave limit\[<a
href="/wiki/index.php?title=CRPA_of_SrVO3&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Obtain DFT virtual orbitals and long-wave limit">edit</a> \| (./index.php.md)\]

Use following [INCAR](../input-files/INCAR.md) file to increase the number
of virtual states and to determine the long-wave limit of the
polarizability (stored in [WAVEDER](../input-files/WAVEDER.md)):

- [INCAR](../input-files/INCAR.md) (see INCAR.PBE)

<!-- -->

    SYSTEM = SrVO3          # system name
    ISMEAR = -1             # Fermi smearing
    SIGMA = 0.1             # electronic temperature in eV (1eV ~ 11604K)
    KPAR = 2                # parallelization of k-points in two groups
    ALGO = Exact            # exact diagonalization
    NELM = 1                # one electronic step suffices, since WAVECAR from previous step is present
    NBANDS = 96             # need for a lot of bands in GW
    LOPTICS = .TRUE.        # we need d phi/ d k  for GW calculations for long-wave limit
    LFINITE_TEMPERATURE = T # compute all optical matrix elements (only required for CRPAR)

Restart VASP. At this stage it is a good idea to make a safety copy of
the [WAVECAR](../input-files/WAVECAR.md) and
[WAVEDER](../input-files/WAVEDER.md) files since we will repeatedly need
them in the calculations that follow:

    cp WAVECAR WAVECAR.PBE
    cp WAVEDER WAVEDER.PBE

## cRPA Calculation\[<a
href="/wiki/index.php?title=CRPA_of_SrVO3&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: cRPA Calculation">edit</a> \| (./index.php.md)\]

Calculate the cRPA interaction parameters for the t2g states by using
the PBE wavefunction as input

    cp WAVECAR.PBE WAVECAR
    cp WAVEDER.PBE WAVEDER

And use following input file as

- [INCAR](../input-files/INCAR.md) (see INCAR.CRPA) and run vasp

<!-- -->

    SYSTEM = SrVO3            # system name
    ISMEAR = -1               # Fermi smearing
    SIGMA = 0.1               # electronic temperature in eV (1eV ~ 11604K)
    NCSHMEM = 1               # switch off shared memory for chi
    ALGO = CRPA               # Switch on CRPA
    NBANDS = 96               # CRPA needs many empty states
    PRECFOCK = Fast           # fast mode for FFTs
    NTARGET_STATES = 1 2 3    # exclude wannier states 1 - 3 in screening
    LWRITE_WANPROJ = .TRUE.   # write wannier projection file
    #LFINITE_TEMPERATURE = T  # T>0 formalism can be avoided here, because U computed only at omega=0

|  |
|----|
| **Warning:** As of version 6.2.0 run this tutorial successfully by adding following lines to INCAR. For older version copy wannier90.win.CRPA to wannier90.win and omit following lines in INCAR. |

    NUM_WANN = 3 
    WANNIER90_WIN = "
    num_bands=   96

    # because bands 21, 22, 23 do not cross with other bands
    # one can exclude all other bands in wannierization
    # and omit the definition of an energy window like so
    exclude_bands = 1-20, 24-96

    begin projections
     V:dxy;dxz;dyz
    end projections
    "

The cRPA interaction values for $\omega=0$ can
be found in the [OUTCAR](../output-files/OUTCAR.md):

    spin components:  1  1, frequency:    0.0000    0.0000

    screened Coulomb repulsion U_iijj between MLWFs:
            1         2         3
       1    3.3459    2.3455    2.3455
       2    2.3455    3.3459    2.3455
       3    2.3455    2.3455    3.3459

    screened Coulomb repulsion U_ijji between MLWFs:
            1         2         3
       1    3.3459    0.4281    0.4281
       2    0.4281    3.3459    0.4281
       3    0.4281    0.4281    3.3459

    screened Coulomb repulsion U_ijij between MLWFs:
            1         2         3
       1    3.3459    0.4281    0.4281
       2    0.4281    3.3459    0.4281
       3    0.4281    0.4281    3.3459

    averaged interaction parameter
    screened Hubbard U =    3.3459    0.0000
    screened Hubbard u =    2.3455    0.0000
    screened Hubbard J =    0.4281   -0.0000

The full interaction matrix is written to [UIJKL](../output-files/UIJKL.md).

|  |
|----|
| **Mind:** The frequency point $\omega$ can be set by [OMEGAMAX](../incar-tags/OMEGAMAX.md) in the INCAR. |

For instance to evaluate the cRPA interaction matrix at
$\omega=10$ eV, add

     OMEGAMAX = 10

to the INCAR and restart VASP. In contrast, adding following two lines
to the [INCAR](../input-files/INCAR.md)

     OMEGAMAX = 10 
     NOMEGAR = 0 

tells VASP to calculate the interaction on the imaginary frequency axis
at $\omega=i 10$. This can be used to evaluate
$U$ at a specific Matsubara frequency point.

In addition, the bare Coulomb interaction matrix is calculated for a
high [VCUTOFF](../incar-tags/VCUTOFF.md) and low energy cutoff
[ENCUTGW](../incar-tags/ENCUTGW.md) and written in that order to the
[OUTCAR](../output-files/OUTCAR.md) file. Look for the lines similar to:

    spin components:  1  1
     
    bare Coulomb repulsion V_iijj between MLWFs:
            1         2         3
       1   16.3485   15.0984   15.0984
       2   15.0984   16.3485   15.0984
       3   15.0984   15.0984   16.3485
     
    bare Coulomb repulsion V_ijji between MLWFs:
            1         2         3
       1   16.3485    0.5351    0.5351
       2    0.5351   16.3485    0.5351
       3    0.5351    0.5351   16.3485
     
    bare Coulomb repulsion V_ijij between MLWFs:
            1         2         3
       1   16.3485    0.5351    0.5351
       2    0.5351   16.3485    0.5351
       3    0.5351    0.5351   16.3485

    averaged bare interaction
    bare Hubbard U =   16.3485   -0.0000
    bare Hubbard u =   15.0984   -0.0000
    bare Hubbard J =    0.5351    0.0000

Similar to the effectively screened interaction the full output is
written to [VIJKL](../output-files/VIJKL.md).

### cRPA calculation on Matsubara axis\[<a
href="/wiki/index.php?title=CRPA_of_SrVO3&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: cRPA calculation on Matsubara axis">edit</a> \| (./index.php.md)\]

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

Note that the same frequency grid is used as for
[ALGO](../incar-tags/ALGO.md)=RPA (RPA correlation energy calculation) and
can not be changed directly. To calculate the cRPA interaction for a set
of automatically chosen imaginary frequency points use once again the
PBE wavefunction as input

    cp WAVECAR.PBE WAVECAR
    cp WAVEDER.PBE WAVEDER

Currently, this step requires the [WANPROJ](../input-files/WANPROJ.md)
file from previous step, no wannier90.win file is necessary. You can
also, delete [WANPROJ](../input-files/WANPROJ.md) and define a wannier
projection as in the previous step in the [INCAR](../input-files/INCAR.md).

Select the space-time cRPA algorithm with following file:

- [INCAR](../input-files/INCAR.md) (see INCAR.CRPAR)

<!-- -->

    SYSTEM = SrVO3             # system name
    LFINITE_TEMPERATURE = T    # use finite temperature formalism 
    ISMEAR = -1                # required for finite temperature algorithm
    SIGMA = 0.1                # electron temperature in eV (1 eV ~ 11000 K)
    ALGO = CRPAR               # Switch on CRPA on imaginary axis
    NBANDS = 96                # CRPA needs many empty states
    PRECFOCK = Fast            # fast mode for FFTs
    NTARGET_STATES = 1 2 3     # exclude wannier states 1 - 3 in screening
    NCRPA_BANDS = 21 22 23     # remove bands 21-23 in screening, currently required for space-time algo
    NOMEGA = 8                 # use 8 imaginary frequency points
    NOMEGA_DUMP = 0            # write WFULLxxxx.tmp files at omega=0, used for off-centre Coulomb integrals in next step

  
Run VASP and make a copy of the output file

    cp OUTCAR OUTCAR.CRPAR

After a successful run, the interaction values at
[NOMEGA](../incar-tags/NOMEGA.md)+1
frequencies are written to the [OUTCAR](../output-files/OUTCAR.md) file,
where the first point is always $\omega=0$:

     spin components:  1  1, frequency:    0.0000    0.0000

    screened Coulomb repulsion U_iijj between MLWFs:
            1         2         3
       1    3.3450    2.3447    2.3447
       2    2.3447    3.3450    2.3447
       3    2.3447    2.3447    3.3450

    ...

     spin components:  1  1, frequency:    0.0000  109.6955

    screened Coulomb repulsion U_iijj between MLWFs:
            1         2         3
       1   15.2510   14.0759   14.0759
       2   14.0759   15.2510   14.0759
       3   14.0759   14.0759   15.2510

The complete matrix at zero frequency is also written to
[UIJKL](../output-files/UIJKL.md), while the result at the first frequency
point of the minimax
grid[^Kaltak:PRB:2020-1]
is found in [UIJKL](../output-files/UIJKL.md).1 and so on.

#### Optional: Analytic continuation\[<a
href="/wiki/index.php?title=CRPA_of_SrVO3&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Optional: Analytic continuation">edit</a> \| (./index.php.md)\]

To obtain the effective interaction on the real frequency axis from the
imaginary axis (stored in [UIJKL](../output-files/UIJKL.md).\*) following
python code can be used in a
<a href="https://jupyter.org/" class="external text"
rel="nofollow">jupyter notebook</a>:


    import numpy as np 
    from scipy.interpolate import AAA
    import matplotlib.pyplot as plt
    # results stored in NOMEGA dimensional array 
    nomega=24
    u = np.zeros( nomega, dtype='complex' )  
    # one-site indices 
    idx=[0,40,80 ]
    # store one-site bare interaction
    v = np.sum( np.loadtxt('VIJKL').T[4][idx] )/len(idx)
    for i in range(nomega):
        raw = np.loadtxt( 'UIJKL.{omega:d}'.format(omega=i+1) ) 
        u[i] = np.sum( raw.T[4][idx] + 1j * raw.T[5][idx] ) / len(idx)
    # extract omega points 
    !grep "omega =" UIJKL.{?,??} | awk '{print $5}' > omegas.dat
    omegas=np.loadtxt( 'omegas.dat' )*1j
    # use AAA algorithm for analytic continuation 
    u_cont = AAA(omegas,u )
    # plot real part of U and bare interaction V 
    z = np.linspace( 0, 200, num=1000)
    fig, ax = plt.subplots()
    ax.plot( z, u_cont(z).real, '-', color='r', label='U')
    ax.axhline(y=v, color='b', linestyle='-', label='V')
    ax.legend()
    # add low-frequency regime as an inset 
    zlow=np.linspace( 0, 20, num=1000)
    inset_ax = ax.inset_axes([0.35, 0.1, 0.6, 0.6])  # [left, bottom, width, height]
    inset_ax.plot(zlow, u_cont(zlow), color='red')
    plt.xlabel('$\omega$ [eV]')
    plt.show()


<a href="/wiki/File:SrVO3_U_omega_acont.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/2/24/SrVO3_U_omega_acont.png/480px-SrVO3_U_omega_acont.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/2/24/SrVO3_U_omega_acont.png/720px-SrVO3_U_omega_acont.png 1.5x, /wiki/images/2/24/SrVO3_U_omega_acont.png 2x"
width="480" height="374" /></a>

|  |
|----|
| **Tip:** Increase [NOMEGA](../incar-tags/NOMEGA.md) points to resolve more details on the real frequency axis. |

In the above plot, there are 24 [NOMEGA](../incar-tags/NOMEGA.md) points
in the calculation to resolve more detail, rather than 8 used in the
rest of the exercise. The exact features of the graph will change
depending on how you fit it using the <a
href="https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.AAA.html"
class="external text" rel="nofollow">AAA algorithm</a> (a rational
approximation algorithm). The tolerance parameter `rtol` can lead to
Froissart doublets
[^gilewicz:kryakin:2003-2],
i.e., non-physical poles, if `rtol` is set too tight, e.g., the pole at
$\omega \approx 13$ eV. The parameter should be changed
in order to ensure that the poles do not disappear when it is modified.
The key parts of the graph are the value of the Coulomb potential at
$\omega = 0$ eV, the first plasmon peak at
$\omega \approx 4$ eV, and that the screened Coulomb
potential U approaches the bare Coulomb potential V at high frequencies.
Note that the first plasmon peak is approximately the distance between
the centers of mass of the p and d states around the Fermi energy, shown
in the DOS in the previous exercise.

## Off-centre Coulomb integrals\[<a
href="/wiki/index.php?title=CRPA_of_SrVO3&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Off-centre Coulomb integrals">edit</a> \| (./index.php.md)\]

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

Every cRPA job writes the effectively screened Coulomb kernel (in
reciprocal space) at zero frequency to
[WFULLxxxx.tmp](../input-files/WFULLxxxx.tmp.md) files. These files
can be read in and off-centre Coulomb integrals can be evaluated using
following input:

    ALGO = 2E4WA                           # Compute off-centre Coulomb integrals
    ISMEAR = -1                            # Fermi smearing             
    SIGMA = 0.1                            # electronic temperature
    NBANDS = 96                            # use same number of bands as stored in WAVECAR
    PRECFOCK = Fast                        # fast mode for FFTs
    NTARGET_STATES = 1 2 3                 # Wannier states for which Coulomb integrals are evaluated

The bare off-centre Coulomb integrals are written to
[VRijkl](../output-files/VRijkl.md), while the effectively screened ones are
found in [URijkl](../output-files/URijkl.md):

    # File generated by VASP contains Coulomb matrix elements
    # U_ijkl = [ij|kl] 
    #  I   J   K   L          RE(U_IJKL)          IM(U_IJKL)
    # R:    1  0.000000  0.000000  0.000000
       1   1   1   1        3.3450226866        0.0000000000
       2   1   1   1        0.0000058776        0.0000006717
       3   1   1   1        0.0000026927       -0.0000003292
    ...
       3   3   3   3        3.3450230976        0.0000000000
    # R:    2  0.000000  0.000000  1.000000
       1   1   1   1        0.7321605022       -0.0001554484
       2   1   1   1        0.0000021144        0.0000002295
    ...

## Downloads\[<a
href="/wiki/index.php?title=CRPA_of_SrVO3&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Downloads">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/e/ee/CRPA_of_SrVO3.zip" class="internal"
title="CRPA of SrVO3.zip">CRPA_of_SrVO3.zip</a>


[Overview](../tutorials/GW_and_ACFDT_-_Tutorial.md) \>
[bandgap of Si in
GW](Bandgap_of_Si_in_GW.md) \>
[bandstructure of Si in GW
(VASP2WANNIER90)](https://vasp.at/wiki/index.php/Bandstructure_of_Si_in_GW_(VASP2WANNIER90) "Bandstructure of Si in GW (VASP2WANNIER90)") \>
[bandstructure of SrVO3 in
GW](Bandstructure_of_SrVO3_in_GW.md)
 \>
CRPA of SrVO3
 \> [Equilibrium volume of Si
in the
RPA](Equilibrium_volume_of_Si_in_the_RPA.md) \>
[List of tutorials](../categories/Category-Tutorials.md)


Back to the [main page](The_VASP_Manual.md).

## References\[<a
href="/wiki/index.php?title=CRPA_of_SrVO3&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^Kaltak:PRB:2020-1]: [M. Kaltak and G. Kresse, Phys. Rev. B. **101**, 205145 (2020).](https://doi.org/10.1103/PhysRevB.101.205145)
[^gilewicz:kryakin:2003-2]: [J. Gilewicz, Y. Kryakin, *Froissart doublets in Padé approximation in the case of polynomial noise*, J. Comput. Appl. Math. **153**, 235 (2003).](https://doi.org/10.1016/S0377-0427(02)00674-X)
