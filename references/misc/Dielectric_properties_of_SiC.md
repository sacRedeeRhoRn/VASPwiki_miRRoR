<!-- Source: https://vasp.at/wiki/index.php/Dielectric_properties_of_SiC | revid: 10418 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Dielectric properties of SiC



[Overview](../tutorials/Optical_properties_and_dielectric_response_-_Tutorial.md) \>
dielectric properties of
SiC \> [dielectric
properties of
Si](Dielectric_properties_of_Si.md)
 \> [Ionic contributions to
the frequency dependent dielectric function of
NaCl](Ionic_contributions_to_the_frequency_dependent_dielectric_function_of_NaCl.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#task)
- [2 Static
  dielectric properties](#static-dielectric-properties)
  - [2.1 Density
    functional perturbation
    theory](#density-functional-perturbation-theory)
  - [2.2 Response
    to finite electric
    fields](#response-to-finite-electric-fields)
  - [2.3 Ionic
    contributions to the static dielectric
    properties](#ionic-contributions-to-the-static-dielectric-properties)
- [3 Frequency
  dependent dielectric
  response](#frequency-dependent-dielectric-response)
  - [3.1 The
    independent-particle
    picture](#the-independent-particle-picture)
  - [3.2 Including
    local field effects](#including-local-field-effects)
- [4
  References](#references)
- [5
  Download](#download)


## Task\[<a
href="/wiki/index.php?title=Dielectric_properties_of_SiC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the static and frequency dependent dielectric properties
of SiC.

## Static dielectric properties\[<a
href="/wiki/index.php?title=Dielectric_properties_of_SiC&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Static dielectric properties">edit</a> \| (./index.php.md)\]

### Density functional perturbation theory\[<a
href="/wiki/index.php?title=Dielectric_properties_of_SiC&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Density functional perturbation theory">edit</a> \| (./index.php.md)\]

Let us start with the calculation of the static dielectric properties.
The most convenient way to determine the Born effective charges,
dielectric-, piezoelectric tensors is by means of density functional
perturbation theory ([LEPSILON](../incar-tags/LEPSILON.md)=*.TRUE.*).

- [INCAR](../input-files/INCAR.md) (see INCAR.LEPSILON)

<!-- -->

    ISMEAR =  0
    SIGMA  =  0.01
    EDIFF  = 1.E-8
       
    ## to get the Born effective charges
    ## and the macroscopic dielectric tensor
    LEPSILON = .TRUE.
        
    #LRPA = .TRUE.
    #LPEAD = .TRUE.
       
    ## to get the ionic contribution
    ## to the macroscopic dielectric tensor
    #IBRION = 8
       
    ## As an alternative to LEPSILON = .TRUE.
    ## you might try the following:
    #LCALCEPS = .TRUE.
       
    ## and:
    #IBRION = 6
    #NFREE = 2

- [KPOINTS](../input-files/KPOINTS.md) (see KPOINTS.8)

<!-- -->

    8x8x8
     0
    G
     8 8 8
     0 0 0

- [POSCAR](../input-files/POSCAR.md)

<!-- -->

    system SiC
    4.35
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
    1 1
    cart
    0.00 0.00 0.00 
    0.25 0.25 0.25

<a href="/wiki/File:Fig_dielectric_properties_SiC_1.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/f/f2/Fig_dielectric_properties_SiC_1.png/300px-Fig_dielectric_properties_SiC_1.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/f/f2/Fig_dielectric_properties_SiC_1.png/450px-Fig_dielectric_properties_SiC_1.png 1.5x, /wiki/images/f/f2/Fig_dielectric_properties_SiC_1.png 2x"
width="300" height="328" /></a>

- The [LRPA](../incar-tags/LRPA.md)-tag

By default the dielectric tensor is calculated in the
independent-particle (IP) approximation, you should see the following
lines in the [OUTCAR](../output-files/OUTCAR.md) file:

    HEAD OF MICROSCOPIC STATIC DIELECTRIC TENSOR (independent particle, excluding Hartree and local field effects)

and

    MACROSCOPIC STATIC DIELECTRIC TENSOR (including local field effects in DFT)

which comes later in the [OUTCAR](../output-files/OUTCAR.md) file.

If one adds

    LRPA=.TRUE.

to the [INCAR](../input-files/INCAR.md) above, the second instance will
include local field effect only with respect to the response in the
Hartree part of the potential, i.e., in the *random-phase-approximation*
(RPA). Search for

    MACROSCOPIC STATIC DIELECTRIC TENSOR (including local field effects in RPA (Hartree))

in the [OUTCAR](../output-files/OUTCAR.md).

- The Born effective charge tensors ($Z^{\*}_{ij}$)

Roughly speaking, the Born effective tensors provide a measure of how
much charge effectively moves with an atom when you displace it. For a
definition see the article on [Berry phases and finite electric
fields](../theory/Berry_phases_and_finite_electric_fields.md).
For [LEPSILON](../incar-tags/LEPSILON.md)=.TRUE., the Born effective
charge tensors are written near the end of the
[OUTCAR](../output-files/OUTCAR.md) file.

Look for

    BORN EFFECTIVE CHARGES (in e, cummulative output)

**Mind**: you will find this entry only if
[LRPA](../incar-tags/LRPA.md)=.FALSE. (default), since the Born-effective
charges in the RPA tend to be nonsensical.

- The [LPEAD](../incar-tags/LPEAD.md)-tag

As an alternative to solving a linear Sternheimer equation (Eq. 32 of
<sup>[\[1\]](#cite_note-gajdos:prb:06-1)</sup>),
one may compute $| \nabla_{\mathbf{k}}
\tilde{u}_{n\mathbf{k}} \rangle$ from finite
differences by specifying

    LPEAD=.TRUE.

  
in the [INCAR](../input-files/INCAR.md) file. The derivative of the
cell-periodic part of the wave function w.r.t. the Bloch vector is then
computed by means of a fourth-order finite difference stencil, in the
spirit of Eqs. 96 and 97 of
<sup>[\[2\]](#cite_note-nunes:prb:01-2)</sup>.
The results of the calculation of static dielectric properties by means
of [LEPSILON](../incar-tags/LEPSILON.md)=.TRUE. tend to converge more
rapidly w.r.t. **k**-point sampling with
[LPEAD](../incar-tags/LPEAD.md)=.TRUE.

Rerun the example with

    ISMEAR =  0
    SIGMA  =  0.01
    EDIFF  = 1.E-8
       
    ## to get the Born effective charges
    ## and the macroscopic dielectric tensor
    LEPSILON = .TRUE.
    LPEAD = .TRUE.

This will allow for a clean comparison with the next topic.

### Response to finite electric fields\[<a
href="/wiki/index.php?title=Dielectric_properties_of_SiC&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Response to finite electric fields">edit</a> \| (./index.php.md)\]

The second way one may compute the static dielectric properties is from
[self-consistent response of the system to a finite electric
field](../theory/Berry_phases_and_finite_electric_fields.md).<sup>[\[3\]](#cite_note-souza:prl:02-3)</sup>

- [INCAR](../input-files/INCAR.md)

<!-- -->

    ISMEAR =  0
    SIGMA  =  0.01
    EDIFF  = 1.E-8
        
    LCALCEPS = .TRUE.

### Ionic contributions to the static dielectric properties\[<a
href="/wiki/index.php?title=Dielectric_properties_of_SiC&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Ionic contributions to the static dielectric properties">edit</a> \| (./index.php.md)\]

To obtain the ionic contributions to the static dielectric properties
one needs to compute the force-constant matrices (Hessian of the total
energy w.r.t. the ionic positions) and internal strain tensors (second
derivative of the total energy w.r.t. strain fields and ionic postions).
These properties may be obtained from finite differences
([IBRION](../incar-tags/IBRION.md)=5 or 6) or from perturbation theory
([IBRION](../incar-tags/IBRION.md)=7 or 8). Try the following

- [INCAR](../input-files/INCAR.md)

<!-- -->

    ISMEAR =  0
    SIGMA  =  0.01
    EDIFF  = 1.E-8
       
    ## to get the Born effective charges
    ## and the macroscopic dielectric tensor
    LEPSILON = .TRUE.
    LPEAD = .TRUE.
        
    ## to get the ionic contribution
    ## to the macroscopic dielectric tensor
    IBRION = 8

and search for

    MACROSCOPIC STATIC DIELECTRIC TENSOR IONIC CONTRIBUTION

    ELASTIC MODULI IONIC CONTR (kBar)

    PIEZOELECTRIC TENSOR IONIC CONTR  for field in x, y, z        (C/m^2)

in the [OUTCAR](../output-files/OUTCAR.md) file.

## Frequency dependent dielectric response\[<a
href="/wiki/index.php?title=Dielectric_properties_of_SiC&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Frequency dependent dielectric response">edit</a> \| (./index.php.md)\]

Frequency dependent dielectric functions may be computed at various
levels of approximation:

1.  In the independent-particle approximation.
2.  Including local field effects in the random-phase-approximation.
3.  Including local field effects in DFT.

Whatever we may choose to do afterwards in terms of dielectric response
calculations, we have to start with a standard DFT (or hybrid
functional) calculation

- [INCAR](../input-files/INCAR.md) (see INCAR.DFT)

<!-- -->

    ISMEAR =  0
    SIGMA  =  0.01
    EDIFF  = 1.E-8

- [KPOINTS](../input-files/KPOINTS.md) (see KPOINTS.6)

<!-- -->

    6x6x6
     0
    G
     6 6 6
     0 0 0

**Mind**: keep the [WAVECAR](../input-files/WAVECAR.md) file, you're going
to need it in the following.

### The independent-particle picture\[<a
href="/wiki/index.php?title=Dielectric_properties_of_SiC&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: The independent-particle picture">edit</a> \| (./index.php.md)\]

To compute the frequency dependent dielectric function in the
independent-particle (IP) picture we restart from the
[WAVECAR](../input-files/WAVECAR.md) of the previous run, with the
following [INCAR](../input-files/INCAR.md)

- [INCAR](../input-files/INCAR.md) (see INCAR.LOPTICS)

<!-- -->

    ALGO = Exact
    NBANDS  = 64
    LOPTICS = .TRUE. ; CSHIFT = 0.100
    NEDOS = 2000
       
    ## and you might try with the following
    #LPEAD = .TRUE.
       
    ISMEAR =  0
    SIGMA  =  0.01
    EDIFF  = 1.E-8

The frequency dependent dielectric functions is written to the
[OUTCAR](../output-files/OUTCAR.md) file. Search for

     frequency dependent IMAGINARY DIELECTRIC FUNCTION (independent particle, no local field effects)

and

     frequency dependent      REAL DIELECTRIC FUNCTION (independent particle, no local field effects)

To visualize the real and imaginary parts of the frequency dependent
dielectric function you may use `p4vasp`

    p4v vasprun.xml

or run the following bash-script (`plotoptics2`)

    awk 'BEGIN{i=1} /imag/,\
                    /\/imag/ \
                     {a[i]=$2 ; b[i]=$3 ; i=i+1} \
         END{for (j=12;j<i-3;j++) print a[j],b[j]}' vasprun.xml > imag.dat

    awk 'BEGIN{i=1} /real/,\
                    /\/real/ \
                     {a[i]=$2 ; b[i]=$3 ; i=i+1} \
         END{for (j=12;j<i-3;j++) print a[j],b[j]}' vasprun.xml > real.dat

    cat >plotfile<<!
    # set term postscript enhanced eps colour lw 2 "Helvetica" 20
    # set output "optics.eps"
    plot [0:25] "imag.dat" using (\$1):(\$2) w lp, "real.dat" using (\$1):(\$2) w lp
    !

    gnuplot -persist plotfile

- [LPEAD](../incar-tags/LPEAD.md)-tag

As an alternative to the perturbative expression (Eq. 31 of
<sup>[\[1\]](#cite_note-gajdos:prb:06-1)</sup>),
one may compute $| \nabla_{\mathbf{k}}
\tilde{u}_{n\mathbf{k}} \rangle$ from finite
differences by specifying

    LPEAD=.TRUE.

in the [INCAR](../input-files/INCAR.md) file. The derivative of the
cell-periodic part of the wave function w.r.t. the Bloch vector is then
computed by means of a fourth-order finite difference stencil, in the
spirit of Eqs. 96 and 97 of
<sup>[\[2\]](#cite_note-nunes:prb:01-2)</sup>.

**Mind**: keep the [WAVECAR](../input-files/WAVECAR.md) and
[WAVEDER](../input-files/WAVEDER.md) files, you're going to need them in
the following. You might also want to keep a copy of the
[vasprun.xml](../output-files/Vasprun.xml.md).

    cp vasprun.xml vasprun_loptics.xml

### Including local field effects\[<a
href="/wiki/index.php?title=Dielectric_properties_of_SiC&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Including local field effects">edit</a> \| (./index.php.md)\]

To determine the frequency dependent dielectric function including local
field effects one needs the [WAVECAR](../input-files/WAVECAR.md) and
[WAVEDER](../input-files/WAVEDER.md) files from the previous calculation
([ALGO](../incar-tags/ALGO.md)=Exact and
[LOPTICS](../incar-tags/LOPTICS.md)=.TRUE., and sufficient virtual
orbitals), and

- [INCAR](../input-files/INCAR.md) (see INCAR.CHI)

<!-- -->

    # Frequency dependent dielectric tensor with and
    # without local field effects in RPA
    # N.B.: beware one first has to have done a
    # calculation with ALGO=Exact, LOPTICS=.TRUE.
    # and a reasonable number of virtual states (see above)
    ALGO = CHI
           
    # be sure to take the same number of bands as for
    # the LOPTICS=.TRUE. calculation, otherwise the
    # WAVEDER file is not read correctly
    NBANDS = 64
       
    ISMEAR =  0
    SIGMA  =  0.01
    EDIFF  = 1.E-8
         
    LWAVE = .FALSE.
    LCHARG= .FALSE.

  
Information concerning the dielectric function in the
independent-particle picture is written after the line

    HEAD OF MICROSCOPIC DIELECTRIC TENSOR (INDEPENDENT PARTICLE)

in the [OUTCAR](../output-files/OUTCAR.md) file.

Per default, for [ALGO](../incar-tags/ALGO.md)=*CHI*, local field effects
are included at the level of the RPA
([LRPA](../incar-tags/LRPA.md)=*.TRUE.*), i.e., limited to Hartree
contributions only.

See the information after

    INVERSE MACROSCOPIC DIELECTRIC TENSOR (including local field effects in RPA (Hartree))

in the [OUTCAR](../output-files/OUTCAR.md) file.

To include local field effects beyond the RPA, i.e., contributions from
DFT exchange and correlation, one has to specify

    LRPA=.FALSE.

in the [INCAR](../input-files/INCAR.md) file.

In this case look at the output after

    INVERSE MACROSCOPIC DIELECTRIC TENSOR (test charge-test charge, local field effects in DFT)

in the [OUTCAR](../output-files/OUTCAR.md) file.

The following bash-script (`plotchi`) uses *awk* to extract the
frequency dependent dielectric constant, both in the
independent-particle picture as well as including local field effects
(either in DFT or in the RPA) and plots the real and imaginary
components using *gnuplot*:

    awk 'BEGIN{i=1} /HEAD OF MICRO/,\
                    /XI_LOCAL/ \
                     {if ($4=="dielectric") {a[i]=$1 ; b[i]=$2 ; c[i]=$3 ; i=i+1}} \
         END{for (j=1;j<i;j++) print a[j],b[j],c[j]}' OUTCAR > chi0.dat

    awk 'BEGIN{i=1} /INVERSE MACRO/,\
                    /XI_TO_W/ \
                     {if ($4=="dielectric") {a[i]=$1 ; b[i]=$2 ; c[i]=$3 ; i=i+1}} \
         END{for (j=1;j<i;j++) print a[j],b[j],c[j]}' OUTCAR > chi.dat
    cat >plotfile<<!
    # set term postscript enhanced eps colour lw 2 "Helvetica" 20
    # set output "optics.eps"

    plot "chi0.dat" using (\$1):(\$2)  w lp lt -1 lw 2 pt 4 title "chi0 real", \
         "chi0.dat" using (\$1):(-\$3) w lp lt  0 lw 2 pt 4 title "chi0 imag", \
         "chi.dat"  using (\$1):(\$2)  w lp lt  1 lw 2 pt 2 title "chi  real", \
         "chi.dat"  using (\$1):(-\$3) w lp lt  0 lw 2 pt 2 lc 1 title "chi  imag"
    !

    gnuplot -persist plotfile

If you have kept a copy of the
[vasprun.xml](../output-files/Vasprun.xml.md) of the
[LOPTICS](../incar-tags/LOPTICS.md)=*.TRUE.* run (e.g.,
`vasprun_loptics.xml`), you might execute `plotall` to compare the
dielectric functions computed with
[LOPTICS](../incar-tags/LOPTICS.md)=*.TRUE.* and
[ALGO](../incar-tags/ALGO.md)=*CHI*.

    vasprun_LOPTICS=vasprun_loptics.xml
    OUTCAR_CHI=OUTCAR

    awk 'BEGIN{i=1} /imag/,\
                    /\/imag/ \
                     {a[i]=$2 ; b[i]=$3 ; i=i+1} \
         END{for (j=12;j<i-3;j++) print a[j],b[j]}' $vasprun_LOPTICS > imag.dat

    awk 'BEGIN{i=1} /real/,\
                    /\/real/ \
                     {a[i]=$2 ; b[i]=$3 ; i=i+1} \
         END{for (j=12;j<i-3;j++) print a[j],b[j]}' $vasprun_LOPTICS > real.dat

    awk 'BEGIN{i=1} /HEAD OF MICRO/,\
                    /XI_LOCAL/ \
                     {if ($4=="dielectric") {a[i]=$1 ; b[i]=$2 ; c[i]=$3 ; i=i+1}} \
         END{for (j=1;j<i;j++) print a[j],b[j],c[j]}' $OUTCAR_CHI > chi0.dat

    awk 'BEGIN{i=1} /INVERSE MACRO/,\
                    /XI_TO_W/ \
                     {if ($4=="dielectric") {a[i]=$1 ; b[i]=$2 ; c[i]=$3 ; i=i+1}} \
         END{for (j=1;j<i;j++) print a[j],b[j],c[j]}' $OUTCAR_CHI > chi.dat

    cat >plotfile<<!
    # set term postscript enhanced eps colour lw 2 "Helvetica" 20
    # set output "optics.eps"

    plot "chi0.dat" using (\$1):(\$2)  w lp lt -1 lw 2 pt 4 title "chi0 real", \
         "chi0.dat" using (\$1):(-\$3) w lp lt  0 lw 2 pt 4 title "chi0 imag", \
         "chi.dat"  using (\$1):(\$2)  w lp lt  1 lw 2 pt 2 title "chi  real", \
         "chi.dat"  using (\$1):(-\$3) w lp lt  0 lw 2 pt 2 lc 1 title "chi  imag", \
         "real.dat"  using (\$1):(\$2) w l lt -1  title "optics  real", \
         "imag.dat"  using (\$1):(-\$2) w l lt  0 lc -1 title "optics  imag"
    !

    gnuplot -persist plotfile

Why are the dielectric functions in independent-particle picture from
the [LOPTICS](../incar-tags/LOPTICS.md)=*.TRUE.* and the
[ALGO](../incar-tags/ALGO.md)=*CHI* calculations different?

Hints:

- What [CSHIFT](../incar-tags/CSHIFT.md) is used in the
  [ALGO](../incar-tags/ALGO.md)=*CHI* calculation?

Try redoing the [LOPTICS](../incar-tags/LOPTICS.md)=*.TRUE.* calculation
with the same [CSHIFT](../incar-tags/CSHIFT.md) as VASP chose for the
[ALGO](../incar-tags/ALGO.md)=*CHI* calculation (see INCAR.LOPTICS2):

    CSHIFT=0.466

- Redo the [ALGO](../incar-tags/ALGO.md)=*CHI* calculation with
  [LSPECTRAL](../incar-tags/LSPECTRAL.md)=*.FALSE.* in the
  [ALGO](../incar-tags/ALGO.md)=*CHI* calculation (see INCAR.CHI2).

and compare the dielectric functions again.

- The sample output (using a $6\times6\times6$ mesh for the k points) should look like the
  following:

<a href="/wiki/File:Fig_dielectric_properties_SiC_2.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/1/11/Fig_dielectric_properties_SiC_2.png/600px-Fig_dielectric_properties_SiC_2.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/1/11/Fig_dielectric_properties_SiC_2.png/900px-Fig_dielectric_properties_SiC_2.png 1.5x, /wiki/images/1/11/Fig_dielectric_properties_SiC_2.png 2x"
width="600" height="367" /></a>

## References\[<a
href="/wiki/index.php?title=Dielectric_properties_of_SiC&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-gajdos:prb:06_1-0)</sup>
    <sup>[b](#cite_ref-gajdos:prb:06_1-1)</sup>
    <a href="http://link.aps.org/doi/10.1103/PhysRevB.73.045112"
    class="external text" rel="nofollow">M. Gajdoš, K. Hummer, G. Kresse, J.
    Furthmüller, and F. Bechstedt, Phys. Rev. B 73, 045112 (2006).</a>
2.  ↑
    <sup>[a](#cite_ref-nunes:prb:01_2-0)</sup>
    <sup>[b](#cite_ref-nunes:prb:01_2-1)</sup>
    <a href="http://link.aps.org/doi/10.1103/PhysRevB.63.155107"
    class="external text" rel="nofollow">R. W. Nunes and X. Gonze, Phys.
    Rev. B 63, 155107 (2001).</a>
3.  [↑](#cite_ref-souza:prl:02_3-0)
    <a href="http://link.aps.org/doi/10.1103/PhysRevLett.89.117602"
    class="external text" rel="nofollow">I. Souza, J. Íñiguez, and D.
    Vanderbilt, Phys. Rev. Lett. 89, 117602 (2002).</a>


## Download\[<a
href="/wiki/index.php?title=Dielectric_properties_of_SiC&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/f/f0/SiC_dielectric.tgz" class="internal"
title="SiC dielectric.tgz">SiC_dielectric.tgz</a>


[Overview](../tutorials/Optical_properties_and_dielectric_response_-_Tutorial.md) \>
dielectric properties of
SiC \> [dielectric
properties of
Si](Dielectric_properties_of_Si.md)
 \> [Ionic contributions to
the frequency dependent dielectric function of
NaCl](Ionic_contributions_to_the_frequency_dependent_dielectric_function_of_NaCl.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


