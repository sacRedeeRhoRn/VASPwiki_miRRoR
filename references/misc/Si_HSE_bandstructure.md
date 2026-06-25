<!-- Source: https://vasp.at/wiki/index.php/Si_HSE_bandstructure | revid: 10460 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Si HSE bandstructure


Description: Bandstructure for Si within DFT+HF

Bandstructure in VASP can be obtained following three different
procedures. The standard procedure (procedure 1),

applicable at PBE level, is also described in [Fcc Si bandstructure
example](Fcc_Si_bandstructure.md).

Within Hybrid functional theory it is possible to plot bandstructure
using procedure 2 or 3.


## Contents


- [1 Procedure 1:
  Standard procedure (suitable for DFT
  calculations)](#procedure-1-standard-procedure-suitable-for-dft-calculations))
  - [1.1 Standard
    self-consistent (SC) run](#Standard_self-consistent_(SC)_run)
  - [1.2 Non-SC
    calculation (ICHARG=11)](#non-sc-calculation-icharg11))
  - [1.3 Plot using
    p4v](#plot-using-p4v)
- [2 Procedure 2:
  0-weight (Fake) SC procedure (works DFT & hybrid
  functionals)](#Procedure_2:_0-weight_(Fake)_SC_procedure_(works_DFT_&_hybrid_functionals))
  - [2.1 Standard
    DFT run](#standard-dft-run)
  - [2.2 Hybrid
    calculation using a suitably modified KPOINTS
    file](#hybrid-calculation-using-a-suitably-modified-kpoints-file)
  - [2.3 Plot using
    p4v](#plot-using-p4v-1)
- [3 Procedure 3:
  VASP2WANNIER90 (works for DFT, hybrid functionals, and
  GW)](#procedure-3-vasp2wannier90-works-for-dft-hybrid-functionals-and-gw))
  - [3.1 Standard
    DFT run](#standard-dft-run-1)
  - [3.2 Increase
    the number of states to
    24](#increase-the-number-of-states-to-24)
  - [3.3 HSE +
    LWANNIER90 run](#HSE_+_LWANNIER90_run)
  - [3.4 Plot
    bandstructure (Wannier interpolation) using XMGRACE or
    GNUPLOT](#Plot_bandstructure_(Wannier_interpolation)_using_XMGRACE_or_GNUPLOT)
- [4
  Download](#download)


## Procedure 1: Standard procedure (suitable for DFT calculations)\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Procedure 1: Standard procedure (suitable for DFT calculations)">edit</a> \| (./index.php.md)")\]

Only possible within DFT. Described in [Fcc Si bandstructure
example](Fcc_Si_bandstructure.md):

### Standard self-consistent (SC) run\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=2"
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

- [INCAR](../input-files/INCAR.md) (see INCAR.dft)

<!-- -->

    ISMEAR =  0
    SIGMA  =  0.01
    NBANDS = 8

- [KPOINTS](../input-files/KPOINTS.md) (see KPOINTS.6)

<!-- -->

    6x6x6
     0
    G
     6 6 6
     0 0 0

### Non-SC calculation ([ICHARG](../incar-tags/ICHARG.md)=11)\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Non-SC calculation (ICHARG=11)">edit</a> \| (./index.php.md)")\]

Use preconverged [CHGCAR](../input-files/CHGCAR.md) file and a suitable
[KPOINTS](../input-files/KPOINTS.md) file

- [INCAR](../input-files/INCAR.md)

<!-- -->

    ISMEAR =  0
    SIGMA  =  0.01
    NBANDS = 8
        
    ICHARG = 11 #read charge from CHGCAR and keep fixed
    LORBIT = 11

- [KPOINTS](../input-files/KPOINTS.md) (see KPOINTS_PBE_bands)

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
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Plot using p4v">edit</a> \| (./index.php.md)\]

P4VASP: <a href="http://www.p4vasp.at" class="external text"
rel="nofollow">p4v</a>

## Procedure 2: 0-weight (Fake) SC procedure (works DFT & hybrid functionals)\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Procedure 2: 0-weight (Fake) SC procedure (works DFT &amp; hybrid functionals)">edit</a> \| (./index.php.md) SC procedure (works DFT & hybrid functionals)")\]

This procedure can be applied to compute bandstructure at hybrid
functionals and DFT level (see the `HSE_bandstructure.sh` script).

### Standard DFT run\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Standard DFT run">edit</a> \| (./index.php.md)\]

Just as before

- [INCAR](../input-files/INCAR.md) (see INCAR.dft)

<!-- -->

    ISMEAR =  0
    SIGMA  =  0.01
    NBANDS = 8

- [KPOINTS](../input-files/KPOINTS.md) (see KPOINST.6)

<!-- -->

    6x6x6
     0
    G
     6 6 6
     0 0 0

### Hybrid calculation using a suitably modified KPOINTS file\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Hybrid calculation using a suitably modified KPOINTS file">edit</a> \| (./index.php.md)\]

- [INCAR](../input-files/INCAR.md) (see INCAR.hse)

<!-- -->

    ISMEAR =  0
    SIGMA  =  0.01
        
    LHFCALC = .TRUE. ; HFSCREEN = 0.2 ; AEXX = 0.25
    ALGO = D ; TIME = 0.4 ; LDIAG = .TRUE. 
        
    EDIFF = 1.E-6
        
    NBANDS = 8

- [KPOINTS](../input-files/KPOINTS.md) (see KPOINTS_HSE_bands.6 and
  README.txt)

<!-- -->

    Automatically generated mesh
          26
    Reciprocal lattice
        0.00000000000000    0.00000000000000    0.00000000000000             1
        0.16666666666667    0.00000000000000    0.00000000000000             8
        0.33333333333333    0.00000000000000    0.00000000000000             8
        0.50000000000000    0.00000000000000    0.00000000000000             4
        0.16666666666667    0.16666666666667    0.00000000000000             6
        0.33333333333333    0.16666666666667    0.00000000000000            24
        0.50000000000000    0.16666666666667    0.00000000000000            24
       -0.33333333333333    0.16666666666667    0.00000000000000            24
       -0.16666666666667    0.16666666666667    0.00000000000000            12
        0.33333333333333    0.33333333333333    0.00000000000000             6
        0.50000000000000    0.33333333333333    0.00000000000000            24
       -0.33333333333333    0.33333333333333    0.00000000000000            12
        0.50000000000000    0.50000000000000    0.00000000000000             3
        0.50000000000000    0.33333333333333    0.16666666666667            24
       -0.33333333333333    0.33333333333333    0.16666666666667            24
       -0.33333333333333    0.50000000000000    0.16666666666667            12
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

Please note that step two requires a WAVECAR obtained from a standard
DFT run (not an HSE calculation), otherwise the resulting conduction
bands often have a zig-zag structure.

  

### Plot using p4v\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Plot using p4v">edit</a> \| (./index.php.md)\]

P4VASP: <a href="http://www.p4vasp.at" class="external text"
rel="nofollow">p4v</a>

**Mind**: Zoom in on the right-side part of the bandstructure plot.

## Procedure 3: VASP2WANNIER90 (works for DFT, hybrid functionals, and GW)\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Procedure 3: VASP2WANNIER90 (works for DFT, hybrid functionals, and GW)">edit</a> \| (./index.php.md)")\]

Wannier function interpolation using the VASP2WANNIER90 interface: this
procedure is applicable to DFT, hybrid functionals, and GW bandstructure
calculations. Here we apply it for a hybrid functional. For GW see the
[Bandstructure of Si in GW
(VASP2WANNIER90)](https://vasp.at/wiki/index.php/Bandstructure_of_Si_in_GW_(VASP2WANNIER90) "Bandstructure of Si in GW (VASP2WANNIER90)")
and [bandstructure of SrVO3 in
GW](Bandstructure_of_SrVO3_in_GW.md)
examples.

To see a summary of the workflow below, have a look at the
`HSE_bandstructure_with_wannier90.sh`.

### Standard DFT run\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Standard DFT run">edit</a> \| (./index.php.md)\]

Just as before

- [INCAR](../input-files/INCAR.md) (see INCAR.dft)

<!-- -->

    ISMEAR =  0
    SIGMA  =  0.01
    NBANDS = 8

- [KPOINTS](../input-files/KPOINTS.md) (see KPOINST.6)

<!-- -->

    6x6x6
     0
    G
     6 6 6
     0 0 0

### Increase the number of states to 24\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Increase the number of states to 24">edit</a> \| (./index.php.md)\]

This step is optional.

- [INCAR](../input-files/INCAR.md) (see INCAR.diag)

<!-- -->

    ISMEAR =  0
    SIGMA  =  0.01
         
    ALGO = Exact
    NELM = 1
         
    NBANDS = 24

### HSE + LWANNIER90 run\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: HSE + LWANNIER90 run">edit</a> \| (./index.php.md)\]

Run the hybrid functional calculation and call `wannier90` (see
[LWANNIER90_RUN](../incar-tags/LWANNIER90_RUN.md)). .

- [INCAR](../input-files/INCAR.md) (see INCAR.hse_with_wannier90)

<!-- -->

    ISMEAR =  0
    SIGMA  =  0.01
         
    LHFCALC = .TRUE. ; HFSCREEN = 0.2 ; AEXX = 0.25
    ALGO = D ; TIME = 0.4 ; LDIAG = .TRUE. 
    NKRED = 2
        
    EDIFF = 1.E-6
        
    NBANDS = 24
        
    LWANNIER90_RUN = .TRUE.

You will have to provide some instructions for `wannier90` as well:

- wannier90.win (see wannier90.win_start)

<!-- -->

    num_wann=18
    num_bands=24

    Begin Projections
    Si:s ; p ; d
    End Projections

    #dis_froz_max=9
    dis_num_iter=100

    #guiding_centres=true

    bands_plot      =  true
    begin kpoint_path
    L 0.50000  0.50000 0.5000 G 0.00000  0.00000 0.0000
    G 0.00000  0.00000 0.0000 X 0.50000  0.00000 0.5000
    X 0.50000  0.00000 0.5000 K 0.37500 -0.37500 0.0000
    K 0.37500 -0.37500 0.0000 G 0.00000  0.00000 0.0000
    end kpoint_path
    bands_num_points 40
    bands_plot_format gnuplot xmgrace

  
**Mind**: If the wannier90.win file does not exist VASP will create a
default wannier90.win compatible with the POSCAR and INCAR files, which
needs to be suitably modified by including the proper instruction
required to generate the maximally localized wannier functions (refer to
the <a href="http://www.wannier.org/doc/user_guide.pdf"
class="external text" rel="nofollow">WANNIER90 manual</a>).

### Plot bandstructure (Wannier interpolation) using XMGRACE or GNUPLOT\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Plot bandstructure (Wannier interpolation) using XMGRACE or GNUPLOT">edit</a> \| (./index.php.md) using XMGRACE or GNUPLOT")\]

If all went well, `wannier90` will have generated the following
bandstructure files which can be visualized using xmgrace or gnuplot:

- wannier90_band.agr

<!-- -->

    xmgrace ./wannier90_band.agr

- wannier90_band.dat

<!-- -->

- wannier90_band.gnu

<!-- -->

    gnuplot -persist ./wannier90_band.gnu

**N.B.:** Most modern versions of `gnuplot` will respond with an error
message unless you remove the first line of `wannier90_band.gnu` (some
deprecated syntax issue).

## Download\[<a
href="/wiki/index.php?title=Si_HSE_bandstructure&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/e/e4/Si_HSE_band.tgz" class="internal"
title="Si HSE band.tgz">Si_HSE_band.tgz</a>

------------------------------------------------------------------------


