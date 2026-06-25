<!-- Source: https://vasp.at/wiki/index.php/Si_bandstructure | revid: 10458 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Si bandstructure



[Overview](../tutorials/Hybrid_functionals_-_Tutorial.md) \>
[bandgap of Si using different DFT+HF
methods](Bandgap_of_Si_using_different_DFT+HF_methods.md) \>
[MgO optimum
mixing](MgO_optimum_mixing.md) \>
[fcc Ni DOS with hybrid
functional](Fcc_Ni_DOS_with_hybrid_functional.md) \>
Si bandstructure
 \> [List of
tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#Task)
- [2 Procedure 1:
  Standard procedure
  (DFT)](#Procedure_1:_Standard_procedure_(DFT))
  - [2.1 Standard
    self-consistent (SC) run](#Standard_self-consistent_(SC)_run)
  - [2.2 Non-SC
    calculation (ICHARG=11)](#Non-SC_calculation_(ICHARG=11))
  - [2.3 Plot using
    p4v](#Plot_using_p4v)
- [3 Procedure 2:
  0-weight (Fake) SC procedure (PBE &
  Hybrids)](#Procedure_2:_0-weight_(Fake)_SC_procedure_(PBE_&_Hybrids))
  - [3.1 Standard
    DFT run](#Standard_DFT_run)
  - [3.2 Hybrid
    calculation using a suitably modified KPOINTS
    file](#Hybrid_calculation_using_a_suitably_modified_KPOINTS_file)
  - [3.3 Plot using
    p4v](#Plot_using_p4v_2)
- [4 Procedure 3:
  VASP2WANNIER90 (GW, Hybrids,
  PBE)](#Procedure_3:_VASP2WANNIER90_(GW,_Hybrids,_PBE))
  - [4.1 Standard
    DFT run](#Standard_DFT_run_2)
  - [4.2 HSE +
    LWANNIER90 run](#HSE_+_LWANNIER90_run)
  - [4.3 Compute
    Wannier functions](#Compute_Wannier_functions)
  - [4.4 Obtain
    bandstructure (Wannier interpolation) and plot using XMGRACE or
    GNUPLOT](#Obtain_bandstructure_(Wannier_interpolation)_and_plot_using_XMGRACE_or_GNUPLOT)
- [5
  Download](#Download)


## Task\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the bandstructure for Si within DFT+HF.

The bandstructure in VASP can be obtained following three different
procedures. The standard procedure (procedure 1),

applicable at PBE level, is also described in [Fcc Si bandstructure
example](Fcc_Si_bandstructure.md).

Within Hybrid functional theory it is possible to plot bandstructure
using procedure 2 or 3.

## Procedure 1: Standard procedure (DFT)\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Procedure 1: Standard procedure (DFT)">edit</a> \| (./index.php.md)")\]

Only possible within DFT. Described in [Fcc Si bandstructure
example](Fcc_Si_bandstructure.md):

### Standard self-consistent (SC) run\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Standard self-consistent (SC) run">edit</a> \| (./index.php.md) run")\]

- [POSCAR](../input-files/POSCAR.md)

<!-- -->

    system Si
    5.430
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
    2
    cart
    0.00 0.00 0.00
    0.25 0.25 0.25

- [INCAR](../input-files/INCAR.md)

<!-- -->

    System = fcc Si 
    ISMEAR = 0; SIGMA = 0.1;

- [KPOINTS](../input-files/KPOINTS.md)

<!-- -->

    4x4x4
     0
    G
     4 4 4
     0 0 0

### Non-SC calculation ([ICHARG](../incar-tags/ICHARG.md)=11)\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Non-SC calculation (ICHARG=11)">edit</a> \| (./index.php.md)")\]

Use preconverged [CHGCAR](../input-files/CHGCAR.md) file and a suitable
[KPOINTS](../input-files/KPOINTS.md) file (KPOINTS_PBE_bands)

- [INCAR](../input-files/INCAR.md)

<!-- -->

    System = fcc Si 
    ICHARG = 11 #charge read file
    ISMEAR = 0; SIGMA = 0.1;
    LORBIT = 11

- [KPOINTS](../input-files/KPOINTS.md)

<!-- -->

    k-points for bandstructure L-G-X-U K-G
     10
    line
    reciprocal
      0.50000  0.50000  0.50000    1
      0.00000  0.00000  0.00000    1

      0.00000  0.00000  0.00000    1
      0.00000  0.50000  0.50000    1

      0.00000  0.50000  0.50000    1
      0.25000  0.62500  0.62500    1

      0.37500  0.7500   0.37500    1
      0.00000  0.00000  0.00000    1

### Plot using p4v\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Plot using p4v">edit</a> \| (./index.php.md)\]

P4VASP: <a href="http://www.p4vasp.at" class="external text"
rel="nofollow">p4v</a>

## Procedure 2: 0-weight (Fake) SC procedure (PBE & Hybrids)\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Procedure 2: 0-weight (Fake) SC procedure (PBE &amp; Hybrids)">edit</a> \| (./index.php.md) SC procedure (PBE & Hybrids)")\]

This procedure can be applied to compute bandstructure at Hybrid
functionals and DFT level.

### Standard DFT run\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Standard DFT run">edit</a> \| (./index.php.md)\]

- [INCAR](../input-files/INCAR.md)

<!-- -->

    ## Default       
    ISMEAR =  0
    SIGMA  =  0.01
    GGA    = PE
        
    ## HSE
    #LHFCALC = .TRUE. ; HFSCREEN = 0.2 ; AEXX = 0.25
    #ALGO = D ; TIME = 0.4 ; LDIAG = .TRUE.

- [KPOINTS](../input-files/KPOINTS.md)

<!-- -->

    Automatically generated mesh
     0
    G
     4 4 4
     0 0 0

### Hybrid calculation using a suitably modified [KPOINTS](../input-files/KPOINTS.md) file\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Hybrid calculation using a suitably modified KPOINTS file">edit</a> \| (./index.php.md)\]

- [INCAR](../input-files/INCAR.md)

<!-- -->

    ## Default       
    ISMEAR =  0
    SIGMA  =  0.01
    GGA    = PE
        
    ## HSE
    LHFCALC = .TRUE. ; HFSCREEN = 0.2 ; AEXX = 0.25
    ALGO = D ; TIME = 0.4 ; LDIAG = .TRUE.

- KPOINTS_HSE_bands (see README.txt)

<!-- -->

    Explicit k-points list
          18
    Reciprocal lattice
        0.00000000000000    0.00000000000000    0.00000000000000             1
        0.25000000000000    0.00000000000000    0.00000000000000             8
        0.50000000000000    0.00000000000000    0.00000000000000             4
        0.25000000000000    0.25000000000000    0.00000000000000             6
        0.50000000000000    0.25000000000000    0.00000000000000            24
       -0.25000000000000    0.25000000000000    0.00000000000000            12
        0.50000000000000    0.50000000000000    0.00000000000000             3
       -0.25000000000000    0.50000000000000    0.25000000000000             6
    0.00000000 0.00000000 0.00000000 0.000
    0.00000000 0.05555556 0.05555556 0.000
    0.00000000 0.11111111 0.11111111 0.000
    0.00000000 0.16666667 0.16666667 0.000
    0.00000000 0.22222222 0.22222222 0.000
    0.00000000 0.27777778 0.27777778 0.000
    0.00000000 0.33333333 0.33333333 0.000
    0.00000000 0.38888889 0.38888889 0.000
    0.00000000 0.44444444 0.44444444 0.000
    0.00000000 0.50000000 0.50000000 0.000

### Plot using p4v\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Plot using p4v">edit</a> \| (./index.php.md)\]

P4VASP: <a href="http://www.p4vasp.at" class="external text"
rel="nofollow">p4v</a>

**Mind**: Remove from the bandstructure plot the eigenvalues
corresponding to the the regular k-points mesh.

## Procedure 3: VASP2WANNIER90 (GW, Hybrids, PBE)\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Procedure 3: VASP2WANNIER90 (GW, Hybrids, PBE)">edit</a> \| (./index.php.md)")\]

Wannier function interpolation using the VASP2WANNIER90 interface.
Applicable in all cases (here applied for hybrids; for GW see
[Bandstructure_of_Si_in_GW\_(VASP2WANNIER90)
example](https://vasp.at/wiki/index.php/Bandstructure_of_Si_in_GW_(VASP2WANNIER90) "Bandstructure of Si in GW (VASP2WANNIER90)")).

### Standard DFT run\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Standard DFT run">edit</a> \| (./index.php.md)\]

- [INCAR](../input-files/INCAR.md)

<!-- -->

    ## Default       
    ISMEAR =  0
    SIGMA  =  0.01
    GGA    = PE
         
    ## HSE
    #LHFCALC = .TRUE. ; HFSCREEN = 0.2 ; AEXX = 0.25
    #ALGO = D ; TIME = 0.4 ; LDIAG = .TRUE.
        
    ##VASP2WANNIER
    #LWANNIER90=.TRUE.

- [KPOINTS](../input-files/KPOINTS.md)

<!-- -->

    Automatically generated mesh
     0
    G
     4 4 4
     0 0 0

### HSE + LWANNIER90 run\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: HSE + LWANNIER90 run">edit</a> \| (./index.php.md)\]

- [INCAR](../input-files/INCAR.md)

<!-- -->

    ## Default       
    ISMEAR =  0
    SIGMA  =  0.01
    GGA    = PE
        
    ## HSE
    LHFCALC = .TRUE. ; HFSCREEN = 0.2 ; AEXX = 0.25
    ALGO = D ; TIME = 0.4 ; LDIAG = .TRUE.
        
    ##VASP2WANNIER
    LWANNIER90=.TRUE.

Use the wannier90.win file given below which contains all instructions
needed to generate the necessary input files for the WANNIER90 runs
(wannier90.amn, wannier90.mmn, wannier90.eig).

**Mind**: If the wannier90.win file does not exist VASP will create a
default wannier90.win compatible with the POSCAR and INCAR files, which
needs to be suitably modified by including the proper instruction
required to generate the maximally localized wannier functions (refer to
the <a href="http://www.wannier.org/doc/user_guide.pdf"
class="external text" rel="nofollow">WANNIER90 manual</a>).

- wannier90.win

<!-- -->

    num_wann=8
    num_bands=8

    Begin Projections
    Si:sp3
    End Projections

    dis_froz_max=9
    dis_num_iter=1000

    guiding_centres=true

    #restart         =  plot
    #bands_plot      =  true
    #begin kpoint_path
    #L 0.50000  0.50000 0.5000 G 0.00000  0.00000 0.0000
    #G 0.00000  0.00000 0.0000 X 0.50000  0.00000 0.5000
    #X 0.50000  0.00000 0.5000 K 0.37500 -0.37500 0.0000
    #K 0.37500 -0.37500 0.0000 G 0.00000  0.00000 0.0000
    #end kpoint_path
    #bands_num_points 40
    #bands_plot_format gnuplot xmgrace

    begin unit_cell_cart
         2.7150000     2.7150000     0.0000000
         0.0000000     2.7150000     2.7150000
         2.7150000     0.0000000     2.7150000
    end unit_cell_cart

    begin atoms_cart
    Si       0.0000000     0.0000000     0.0000000
    Si       1.3575000     1.3575000     1.3575000
    end atoms_cart

    mp_grid =     4     4     4

    begin kpoints
         0.0000000     0.0000000     0.0000000
         0.2500000     0.0000000     0.0000000
         0.5000000     0.0000000     0.0000000
         0.2500000     0.2500000     0.0000000
         0.5000000     0.2500000     0.0000000
        -0.2500000     0.2500000     0.0000000
         0.5000000     0.5000000     0.0000000
        -0.2500000     0.5000000     0.2500000
         0.0000000     0.2500000     0.0000000
         0.0000000     0.0000000     0.2500000
        -0.2500000    -0.2500000    -0.2500000
        -0.2500000     0.0000000     0.0000000
         0.0000000    -0.2500000     0.0000000
         0.0000000     0.0000000    -0.2500000
         0.2500000     0.2500000     0.2500000
         0.0000000     0.5000000     0.0000000
         0.0000000     0.0000000     0.5000000
        -0.5000000    -0.5000000    -0.5000000
         0.0000000     0.2500000     0.2500000
         0.2500000     0.0000000     0.2500000
        -0.2500000    -0.2500000     0.0000000
        -0.2500000     0.0000000    -0.2500000
         0.0000000    -0.2500000    -0.2500000
         0.0000000     0.5000000     0.2500000
         0.2500000     0.0000000     0.5000000
        -0.2500000    -0.2500000     0.2500000
        -0.5000000    -0.2500000    -0.5000000
         0.2500000     0.5000000     0.0000000
         0.2500000    -0.2500000    -0.2500000
        -0.5000000    -0.5000000    -0.2500000
         0.0000000     0.2500000     0.5000000
        -0.2500000     0.2500000    -0.2500000
        -0.2500000    -0.5000000    -0.5000000
         0.5000000     0.0000000     0.2500000
        -0.5000000    -0.2500000     0.0000000
         0.0000000    -0.5000000    -0.2500000
        -0.2500000     0.0000000    -0.5000000
         0.2500000     0.2500000    -0.2500000
         0.5000000     0.2500000     0.5000000
        -0.2500000    -0.5000000     0.0000000
        -0.2500000     0.2500000     0.2500000
         0.5000000     0.5000000     0.2500000
         0.0000000    -0.2500000    -0.5000000
         0.2500000    -0.2500000     0.2500000
         0.2500000     0.5000000     0.5000000
        -0.5000000     0.0000000    -0.2500000
         0.0000000    -0.2500000     0.2500000
         0.2500000     0.0000000    -0.2500000
        -0.2500000    -0.2500000    -0.5000000
         0.2500000     0.5000000     0.2500000
         0.2500000    -0.2500000     0.0000000
        -0.5000000    -0.2500000    -0.2500000
         0.2500000     0.2500000     0.5000000
         0.0000000     0.2500000    -0.2500000
        -0.2500000    -0.5000000    -0.2500000
         0.5000000     0.2500000     0.2500000
        -0.2500000     0.0000000     0.2500000
         0.0000000     0.5000000     0.5000000
         0.5000000     0.0000000     0.5000000
         0.2500000    -0.2500000     0.5000000
         0.5000000     0.2500000    -0.2500000
        -0.5000000    -0.2500000    -0.7500000
         0.2500000    -0.5000000    -0.2500000
        -0.2500000     0.2500000    -0.5000000
    end kpoints

### Compute Wannier functions\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Compute Wannier functions">edit</a> \| (./index.php.md)\]

run wannier90:

wannier90.x wannier90

This run generates the wannier90 standard output (wannier90.wout) and
the file wannier90.chk needed for the wannier interpolation (next step)

### Obtain bandstructure (Wannier interpolation) and plot using XMGRACE or GNUPLOT\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Obtain bandstructure (Wannier interpolation) and plot using XMGRACE or GNUPLOT">edit</a> \| (./index.php.md) and plot using XMGRACE or GNUPLOT")\]

Uncomment the bandstructure plot flags in wannier90.win and rerun
(restart) wannier90:

wannier90.x wannier90

This run generates the following bandstructure files which can be
visualized using xmgrace or gnuplot:

wannier90_band.agr

wannier90_band.dat

wannier90_band.gnu

  

- README.txt

<!-- -->

    Bandstructure plot in VASP (Three different ways)

    1) Standard way: PBE (Fcc Si bandstructure example).
       1.1  Standard self-consistent (SC) run
       1.2  non-SC calculation (ICHARG=11) using preconverged CHGCAR file and KPOINTS_PBE_bands
       1.3  Plot using p4v

    2) Fake SC procedure: PBE & HSE
       2.1 Standard self-consistent (SC) run
       2.2 Additional SC-run using KPOINTS_HSE_bands
       2.3 Plot using p4v 

    ----
    The file KPOINTS_HSE_bands is constructed by copying the IBZKPT file from run 2.1 to the KPOINTS file:

    IBZKPT
    Automatically generated mesh
           8
    Reciprocal lattice
        0.00000000000000    0.00000000000000    0.00000000000000             1
        0.25000000000000    0.00000000000000    0.00000000000000             8
        0.50000000000000    0.00000000000000    0.00000000000000             4
        0.25000000000000    0.25000000000000    0.00000000000000             6
        0.50000000000000    0.25000000000000    0.00000000000000            24
       -0.25000000000000    0.25000000000000    0.00000000000000            12
        0.50000000000000    0.50000000000000    0.00000000000000             3
       -0.25000000000000    0.50000000000000    0.25000000000000             6

    Then add the desired additional k-points with zero weight and change the total number of k-points

    Explicit k-points list
          18 <--- CHANGE TOTAL NUMBER OF K-POINTS !!
    Reciprocal lattice
        0.00000000000000    0.00000000000000    0.00000000000000             1
        0.25000000000000    0.00000000000000    0.00000000000000             8
        0.50000000000000    0.00000000000000    0.00000000000000             4
        0.25000000000000    0.25000000000000    0.00000000000000             6
        0.50000000000000    0.25000000000000    0.00000000000000            24
       -0.25000000000000    0.25000000000000    0.00000000000000            12
        0.50000000000000    0.50000000000000    0.00000000000000             3
       -0.25000000000000    0.50000000000000    0.25000000000000             6
    0.00000000 0.00000000 0.00000000 0.000 <--- ZERO WEIGHT !!
    0.00000000 0.05555556 0.05555556 0.000
    0.00000000 0.11111111 0.11111111 0.000
    0.00000000 0.16666667 0.16666667 0.000
    0.00000000 0.22222222 0.22222222 0.000
    0.00000000 0.27777778 0.27777778 0.000
    0.00000000 0.33333333 0.33333333 0.000
    0.00000000 0.38888889 0.38888889 0.000
    0.00000000 0.44444444 0.44444444 0.000
    0.00000000 0.50000000 0.50000000 0.000
    ----

    3) VASP2WANNIER90: PBE, HSE & GW 
       3.1 Standard SC run using the existing wannier.win file  
       3.2 run wannier90 (wannier90.x wannier90) to generate MLWFs
       3.3 uncomment bandstructure plot flags in wannier90.win and restart wannier90

    ----
    If the wannier90.win file does not exist VASP will create a default wannier90.win compatible with
    the POSCAR and INCAR, which need to be suitably modify by including the proper instruction required 
    to generate the MLWFs (refer to the wannier90 manual):

    default wannier90.win
     num_wann =     8  ! set to NBANDS by VASP

    use_bloch_phases = .T.

    begin unit_cell_cart
         2.7150000     2.7150000     0.0000000
         0.0000000     2.7150000     2.7150000
         2.7150000     0.0000000     2.7150000
    end unit_cell_cart

    begin atoms_cart
    Si       0.0000000     0.0000000     0.0000000
    Si       1.3575000     1.3575000     1.3575000
    end atoms_cart

    mp_grid =     4     4     4

    begin kpoints
         0.0000000     0.0000000     0.0000000
         0.2500000     0.0000000     0.0000000
         0.5000000     0.0000000     0.0000000
         0.2500000     0.2500000     0.0000000
         0.5000000     0.2500000     0.0000000
        -0.2500000     0.2500000     0.0000000
         0.5000000     0.5000000     0.0000000
        -0.2500000     0.5000000     0.2500000
         0.0000000     0.2500000     0.0000000
         0.0000000     0.0000000     0.2500000
        -0.2500000    -0.2500000    -0.2500000
        -0.2500000     0.0000000     0.0000000
         0.0000000    -0.2500000     0.0000000
         0.0000000     0.0000000    -0.2500000
         0.2500000     0.2500000     0.2500000
         0.0000000     0.5000000     0.0000000
         0.0000000     0.0000000     0.5000000
        -0.5000000    -0.5000000    -0.5000000
         0.0000000     0.2500000     0.2500000
         0.2500000     0.0000000     0.2500000
        -0.2500000    -0.2500000     0.0000000
        -0.2500000     0.0000000    -0.2500000
         0.0000000    -0.2500000    -0.2500000
         0.0000000     0.5000000     0.2500000
         0.2500000     0.0000000     0.5000000
        -0.2500000    -0.2500000     0.2500000
        -0.5000000    -0.2500000    -0.5000000
         0.2500000     0.5000000     0.0000000
         0.2500000    -0.2500000    -0.2500000
        -0.5000000    -0.5000000    -0.2500000
         0.0000000     0.2500000     0.5000000
        -0.2500000     0.2500000    -0.2500000
        -0.2500000    -0.5000000    -0.5000000
         0.5000000     0.0000000     0.2500000
        -0.5000000    -0.2500000     0.0000000
         0.0000000    -0.5000000    -0.2500000
        -0.2500000     0.0000000    -0.5000000
         0.2500000     0.2500000    -0.2500000
         0.5000000     0.2500000     0.5000000
        -0.2500000    -0.5000000     0.0000000
        -0.2500000     0.2500000     0.2500000
         0.5000000     0.5000000     0.2500000
         0.0000000    -0.2500000    -0.5000000
         0.2500000    -0.2500000     0.2500000
         0.2500000     0.5000000     0.5000000
        -0.5000000     0.0000000    -0.2500000
         0.0000000    -0.2500000     0.2500000
         0.2500000     0.0000000    -0.2500000
        -0.2500000    -0.2500000    -0.5000000
         0.2500000     0.5000000     0.2500000
         0.2500000    -0.2500000     0.0000000
        -0.5000000    -0.2500000    -0.2500000
         0.2500000     0.2500000     0.5000000
         0.0000000     0.2500000    -0.2500000
        -0.2500000    -0.5000000    -0.2500000
         0.5000000     0.2500000     0.2500000
        -0.2500000     0.0000000     0.2500000
         0.0000000     0.5000000     0.5000000
         0.5000000     0.0000000     0.5000000
         0.2500000    -0.2500000     0.5000000
         0.5000000     0.2500000    -0.2500000
        -0.5000000    -0.2500000    -0.7500000
         0.2500000    -0.5000000    -0.2500000
        -0.2500000     0.2500000    -0.5000000
    end kpoints
    ----

Wannier90 Manual: <a href="http://www.wannier.org/doc/user_guide.pdf"
class="external text" rel="nofollow">WANNIER90 manual</a>

LWANNIER90 in the VASP Manual:
[LWANNIER90](../incar-tags/LWANNIER90.md).

## Download\[<a
href="/wiki/index.php?title=Si_bandstructure&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/d/d1/5_4_Si_bandstructure.tgz" class="internal"
title="5 4 Si bandstructure.tgz">5_4_Si_bandstructure.tgz</a>


[Overview](../tutorials/Hybrid_functionals_-_Tutorial.md) \>
[bandgap of Si using different DFT+HF
methods](Bandgap_of_Si_using_different_DFT+HF_methods.md) \>
[MgO optimum
mixing](MgO_optimum_mixing.md) \>
[fcc Ni DOS with hybrid
functional](Fcc_Ni_DOS_with_hybrid_functional.md) \>
Si bandstructure
 \> [List of
tutorials](../categories/Category-Tutorials.md)


