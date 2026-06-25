<!-- Source: https://vasp.at/wiki/index.php/Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_%28001%29:_Nudged_Elastic_Band_Calculation | revid: 26241 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band Calculation



[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface
DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
[CO on Ni 111
surface](CO_on_Ni_111_surface.md) \>
[Ni 111 surface high
precision](Ni_111_surface_high_precision.md) \>
[partial DOS of CO on Ni 111
surface](Partial_DOS_of_CO_on_Ni_111_surface.md) \>
[vibrational frequencies of CO on Ni 111
surface](Vibrational_frequencies_of_CO_on_Ni_111_surface.md) \>
[STM of
graphite](STM_of_graphite.md) \>
[STM of
graphene](STM_of_graphene.md) \>
collective jumps of a Pt adatom on
fcc-Pt (001): Nudged Elastic Band Calculation
 \> [List of
tutorials](../categories/Category-Tutorials.md)


  
**Description**: calculate the energy barrier for the self-diffusion (of
a Pt-adatom) on Pt (001): The most stable adsorption site of the adatom
Pt@Pt(001) is the hollow (h) position. Simple models of the diffusion of
the adatom from h to the neighboring h site include two diffusion paths:
hollow-top-hollow (hth, eg along \[1-10\]) or hollow-bridge-hollow (hbh,
eg along \[100\]). A collective jump mechanism involving 2 Pt atoms
diffusing along \[1-10\] is proposed to be the diffusion mechanism with
the lowest energy barrier
[^kellog:prl64:3143-1]

The calculation of the barrier heights involves the following steps:

1\. calculation of the bulk a<sub>0</sub> of Pt for the chosen
functional

2\. a clean Pt (001) surface, with a 2D supercell of -at minimum- (2x2)
reconstruction

3\. the energies of the surface including the Pt-adatom in h, b, and t
position

4\. a [Nudged Elastic
Bands](../tutorials/Nudged_elastic_bands.md) (NEB)
calculation
[^NEB-2]
for the proposed collective jump mechanism

steps 1-3 are straightforward

inputs for a fast, preliminary estimate are given here and in
Pt_NEB_fast.tgz (**mind** this "quick and dirty" setup is only suitable
to learn about principles of the setup of a NEB calculation; the results
of the NEB run with this minimal set of parameters do **not** reproduce
the experimentally found behaviour), for a more time-consuming, but more
accurate setup (larger number of Pt layers, denser k-mesh, higher
[PREC](../incar-tags/PREC.md) and [ENCUT](../incar-tags/ENCUT.md)) please use
the files untarred from Pt_NEB.tgz:

- [INCAR](../input-files/INCAR.md)

System: fcc Pt (001), 3layers

    ISTART = 0
    EDIFF = 1e-6              # electronic convergence
    PREC = Normal
    IBRION = 1                # DIIS algorithm
    POTIM = 0.5
    NSW = 20
    EDIFFG = -0.01            # max forces: 0.1eV/AA
    NELMIN = 5                 # at least 5 el. scf steps  for each ionic step

  

- [KPOINTS](../input-files/KPOINTS.md)

<!-- -->

    K-Points
     0
    Gamma
     3  3  1
     0  0  0

- [POSCAR](../input-files/POSCAR.md) (clean surface)

<!-- -->

    fcc Pt, paw-PBE
    5.62024
      1.0 0.0 0.0
      0.0 1.0 0.0
      0.0 0.0 3.0
      Pt
      12
    Selective
    Direct
    0.25 0.25 0.11785       F  F  F
    0.75 0.25 0.11785       F  F  F
    0.25 0.75 0.11785       F  F  F
    0.75 0.75 0.11785       F  F  F
    0.00 0.00 0.23570       F  F  T
    0.00 0.50 0.23570       F  F  T
    0.50 0.00 0.23570       F  F  T
    0.50 0.50 0.23570       F  F  T
    0.25 0.25 0.35355       F  F  T
    0.75 0.25 0.35355       F  F  T
    0.25 0.75 0.35355       F  F  T
    0.75 0.75 0.35355       F  F  T

- [POSCAR](../input-files/POSCAR.md) (Pt@Pt(001), hollow)

<!-- -->

     fcc Pt, paw-PBE
       5.62024000000000
         1.0000000000000000    0.0000000000000000    0.0000000000000000
         0.0000000000000000    1.0000000000000000    0.0000000000000000
         0.0000000000000000    0.0000000000000000    3.0000000000000000
       Pt 
       13
     Selective dynamics
     Direct
      0.2500000000000000  0.2500000000000000  0.1178499999999971   F   F   F
      0.7500000000000000  0.2500000000000000  0.1178499999999971   F   F   F
      0.2500000000000000  0.7500000000000000  0.1178499999999971   F   F   F
      0.7500000000000000  0.7500000000000000  0.1178499999999971   F   F   F
      0.0000000000000000  0.0000000000000000  0.2341409911878811   T   T   T
      0.0000000000000000  0.5000000000000000  0.2344158754007225   T   T   T
      0.5000000000000000  0.0000000000000000  0.2377721273226986   T   T   T
      0.5000000000000000  0.5000000000000000  0.2341409911878811   T   T   T
      0.2500000000000000  0.2500000000000000  0.3517982322412672   T   T   T
      0.7500000000000000  0.2500000000000000  0.3517982322412672   T   T   T
      0.2500000000000000  0.7500000000000000  0.3517982322412672   T   T   T
      0.7500000000000000  0.7500000000000000  0.3517982322412672   T   T   T
      0.0000000000000000  0.5000000000000000  0.4492270704381683   T   T   T

- [POSCAR](../input-files/POSCAR.md) (Pt@Pt(001), bridge)

<!-- -->

     fcc Pt, paw-PBE
       5.62024000000000
         1.0000000000000000    0.0000000000000000    0.0000000000000000
         0.0000000000000000    1.0000000000000000    0.0000000000000000
         0.0000000000000000    0.0000000000000000    3.0000000000000000
       Pt
       13
     Selective dynamics
     Direct
      0.2500000000000000  0.2500000000000000  0.1178499999999971   F   F   F
      0.7500000000000000  0.2500000000000000  0.1178499999999971   F   F   F
      0.2500000000000000  0.7500000000000000  0.1178499999999971   F   F   F
      0.7500000000000000  0.7500000000000000  0.1178499999999971   F   F   F
      0.0002686432543183  0.0000000000000000  0.2356407813553420   T   T   T
      0.0014220524373488  0.5000000000000000  0.2356795143373628   T   T   T
      0.4997313567456815  0.0000000000000000  0.2356407813553420   T   T   T
      0.4985779475626512  0.5000000000000000  0.2356795143373628   T   T   T
      0.2500000000000000  0.2341977119064422  0.3525947402192897   F   T   T
      0.7500000000000000  0.2518717446753760  0.3518647397661007   T   T   T
      0.2500000000000000  0.7658022880935580  0.3525947402192897   F   T   T
      0.7500000000000000  0.7481282553246233  0.3518647397661007   T   T   T
      0.2500000000000000  0.5000000000000000  0.4716518885541170   F   F   T

- [POSCAR](../input-files/POSCAR.md) (Pt@Pt(001), top)

<!-- -->

     fcc Pt, paw-PBE
       5.62024000000000
         1.0000000000000000    0.0000000000000000    0.0000000000000000
         0.0000000000000000    1.0000000000000000    0.0000000000000000
         0.0000000000000000    0.0000000000000000    3.0000000000000000
       Pt
        13
     Selective dynamics
     Direct
      0.2500000000000000  0.2500000000000000  0.1178499999999971   F   F   F
      0.7500000000000000  0.2500000000000000  0.1178499999999971   F   F   F
      0.2500000000000000  0.7500000000000000  0.1178499999999971   F   F   F
      0.7500000000000000  0.7500000000000000  0.1178499999999971   F   F   F
     -0.0014262288827347 -0.0014262288827347  0.2348121710889565   T   T   T
     -0.0014262288827347  0.5014262288827348  0.2348121710889565   T   T   T
      0.5014262288827348 -0.0014262288827347  0.2348121710889565   T   T   T
      0.5014262288827348  0.5014262288827348  0.2348121710889565   T   T   T
      0.2500000000000000  0.2500000000000000  0.3433443664932221   F   F   T
      0.7500000000000000  0.2500000000000000  0.3546231232810972   T   T   T
      0.2500000000000000  0.7500000000000000  0.3546231232810972   T   T   T
      0.7500000000000000  0.7500000000000000  0.3516055254412989   T   T   T
      0.2500000000000000  0.2500000000000000  0.4861522106341429   F   F   T

the NEB calculation should be done a follows:

1\. run the job from a parent directory containing the files
[INCAR](../input-files/INCAR.md),
[POTCAR](../input-files/POTCAR.md),[KPOINTS](../input-files/KPOINTS.md) and
the run-script of the job

2\. consider how many intermediate geometries (N) should be chosen
between the initial and the final state of the jump in
[INCAR](../input-files/INCAR.md), this corresponds to the parameter
[IMAGES](../incar-tags/IMAGES.md)

3\. generate sub-directories 00 (containing the
[POSCAR](../input-files/POSCAR.md) of the initial geometry i), ... 0(N+1)
(containing the [POSCAR](../input-files/POSCAR.md) of the final geometry f
of the jump). The [POSCAR](../input-files/POSCAR.md) files of the
intermediate steps, to be interpolated between
[POSCAR](../input-files/POSCAR.md)<sub>i</sub> and
[POSCAR](../input-files/POSCAR.md)<sub>f</sub> are stored in the
directories 01 .. 0N. Calculations are **only** done for these
intermediate steps, the optimization of the geometries is done under the
constraint that the relaxing atoms remain on a plane perpendicular to
the hypertangent of the diffusion path. All all output files
[OUTCAR](../output-files/OUTCAR.md), [CONTCAR](../output-files/CONTCAR.md),
[OSZICAR](../output-files/OSZICAR.md) .. of the NEB-steps run are written
to these subdirectories.

in the present excercise, the required precision,... is reduced to a
minimum (the files are found in
<a href="http://www.vasp.at/vasp-workshop/example/Pt_NEB_fast.tgz"
class="external text" rel="nofollow">Pt_NEB_fast.tgz</a>) to save
computing time, a more reliable setup is saved in
<a href="http://www.vasp.at/vasp-workshop/examples/Pt_NEB.tgz"
class="external text" rel="nofollow">Pt_NEB.tgz</a>)

- [INCAR](../input-files/INCAR.md)

  
System: fcc Pt (001), 3layers

    ISTART = 0
    EDIFF = 1e-6              # electronic convergence
    PREC = Normal
    IBRION = 1                # DIIS algorithm
    NSW = 10
    EDIFFG = -0.01            # max forces: 0.1eV/AA
    NELMIN = 5                 # at least 5 el. scf steps  for each ionic step
    IMAGES = 2                # 2 intermediate geometries for  the NEB
    SPRING = -5               # spring constant

  

- [KPOINTS](../input-files/KPOINTS.md)

<!-- -->

    K-Points
     0
    Gamma
     3  3  1
     0  0  0

- [POSCAR](../input-files/POSCAR.md) (of the initial state, in directory
  00)

<!-- -->

     fcc Pt, paw-PBE
        5.62024000000000 
         1.0000000000000000    0.0000000000000000    0.0000000000000000
         0.0000000000000000    1.0000000000000000    0.0000000000000000
         0.0000000000000000    0.0000000000000000    3.0000000000000000
       13
     Direct
       0.250000    0.250000   0.117850
       0.750000    0.250000   0.117850
       0.250000    0.750000   0.117850
       0.750000    0.750000   0.117850
       0.000000    0.000000   0.230682
       0.000000    0.500000   0.230971
       0.500000    0.000000   0.234757
       0.500000    0.500000   0.230682
       0.256381    0.243619   0.347171
       0.743619    0.243619   0.347171
       0.256381    0.756381   0.347171
       0.743619    0.756381   0.347171
       0.000000    0.500000   0.444316

- [POSCAR](../input-files/POSCAR.md) (of the final state, in directory 03)

<!-- -->


     fcc Pt, paw-PBE
       5.62024000000000
         1.0000000000000000    0.0000000000000000    0.0000000000000000
         0.0000000000000000    1.0000000000000000    0.0000000000000000
         0.0000000000000000    0.0000000000000000    3.0000000000000000
       13
     Direct
       0.250000    0.250000   0.117850
       0.750000    0.250000   0.117850
       0.250000    0.750000   0.117850
       0.750000    0.750000   0.117850
       0.000000    0.000000   0.230682
       0.000000    0.500000   0.230971
       0.500000    0.000000   0.234757
       0.500000    0.500000   0.230682
       0.500000    0.000000   0.444316
       0.756381    0.256381   0.347171
       0.243619    0.743619   0.347171
       0.756381    0.743619   0.347171
       0.243619    0.256381   0.347171

4\. concatenate the [POSCAR](../input-files/POSCAR.md) files of i and f to
the file <a
href="/wiki/index.php?title=POSCAR1_POSCAR2&amp;action=edit&amp;redlink=1"
class="new"
title="POSCAR1 POSCAR2 (page does not exist)">POSCAR1_POSCAR2</a> MIND:

-- these files must not include the lines with the names of the atoms
(vasp.5.2 only) and 'Selective Dynamics',

-- there must be no blank line between the POSCARS

-- the block with the velocities of the atoms must be deleted

-- be careful to check that in
[POSCAR](../input-files/POSCAR.md)<sub>i</sub> and
[POSCAR](../input-files/POSCAR.md)<sub>j</sub> all atoms are on the same
side of the supercell to avoid that an atom that actually jumps across
the origin of the cell is dragged through the cell by the interpolation
of the positions.

5\. interpolate the starting geometries of the
[IMAGES](../incar-tags/IMAGES.md), this can be done by using the following
script

interpolatePOSCAR <a
href="/wiki/index.php?title=POSCAR1_POSCAR2&amp;action=edit&amp;redlink=1"
class="new"
title="POSCAR1 POSCAR2 (page does not exist)">POSCAR1_POSCAR2</a>, the
interpolated files are written into the respective subdirectories 00 ...
0(N+1)

  

- interpolatePOSCAR

<!-- -->

    file=$1
    if [ ! -x $file ]
    then
      usage: interpolatePOS POSCAR1_POSCAR2
    fi

    awk <$file '
    BEGIN { rep=4; center=0 }
    /center/ { center=1}
    /rep/ { rep=$2 }
     { line=line+1
       if ( second != 1 ) {
           if ( line == 6 )  {
              lines = $1 + $2 + $3 + 7
              print "found ",lines," ions"
              head[line] = $0
           } else if ( line < 8 )
              head[line] = $0
           else
              {
                 x[line-7] = $1 ; y[line-7] = $2 ; z[line-7] = $3
                 if (line==lines) {
                       line=0; second=1;
                       print "first set read"
                 }
              }
        } else {
           if ( line >= 8 )
              {
                  x2[line-7] = $1; y2[line-7] = $2 ; z2[line-7] = $3  }
                 if (line==lines) {
                       print "second set read"
                 }
        }
    }
    END  {
       lines=lines-7
       for ( line=1; line<=lines ; line ++ )  {
            cx1=cx1+ x[line] ; cy1=cy1+ y[line] ; cz1=cz1+ z[line]
            cx2=cx2+ x2[line]; cy2=cy2+ y2[line]; cz2=cz2+ z2[line]
       }
       if (center) {
         cx=(cx2-cx1)/lines
         cy=(cy2-cy1)/lines
         cz=(cz2-cz1)/lines
         print "center of mass for second cell will be shifted by",cx,cy,cz
       }

       for ( i=0; i<rep ; i++ ) {
           file="0" i "/POSCAR"
           print "writing to " file
           for (line=1; line<=7 ; line++ )
              print head[line]  >file
           for ( line=1; line<=lines ; line ++ )  {
              b=i/(rep-1)
              a=(rep-1-i)/(rep-1)
              dx=a*x[line] + b*(x2[line]-cx)
              dy=a*y[line] + b*(y2[line]-cy)
              dz=a*z[line] + b*(z2[line]-cz)

              printf " %10.6f  %10.6f %10.6f\n",dx,dy,dz >file
           }
       }
    }'

NOTE: the total number of steps is explicitely given in line 8 of the
script (rep=, rep = [IMAGES](../incar-tags/IMAGES.md)+2). If a dfferent
number of [IMAGES](../incar-tags/IMAGES.md) is chosen, this parameter has
to be changed.

**alternatively** the name of the input file and the number of images
can be passed as options to interpolatePOSCAR: interpolatePOSCAR \<fn\>
\<[IMAGES](../incar-tags/IMAGES.md)+2\>

6\. run vasp:

**MIND**: the number of CPUs to be used has to be an integer multiple of
[IMAGES](../incar-tags/IMAGES.md)

7\. if convergence is not reached within [NSW](../incar-tags/NSW.md) steps,
the calculation can be continued by a continuation run, just like for a
standard ionic relaxation.

8\. HINT: better convergence is usually achieved if the number of
[IMAGES](../incar-tags/IMAGES.md) is rather low (up to 4). If the region
close to the transition state is to be refined, one can do another
NEB-calculation, using the ionic configurations of the IMAGES adjacent
to the transition state as the new initial and final states for the
follow-up run.

9: obtain the barrier along diffusion path 00-03 by interpolation
(spline)

## Downloads\[<a
href="/wiki/index.php?title=Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Downloads">edit</a> \| (./index.php.md):_Nudged_Elastic_Band_Calculation&action=edit&section=1 "Edit section's source code: Downloads")\]

<a href="/wiki/images/a/ad/Pt_NEB.tgz" class="internal"
title="Pt NEB.tgz">Pt_NEB.tgz</a>,
<a href="/wiki/images/1/1c/Pt_NEB_fast.tgz" class="internal"
title="Pt NEB fast.tgz">Pt_NEB_fast.tgz</a>

## References\[<a
href="/wiki/index.php?title=Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md):_Nudged_Elastic_Band_Calculation&action=edit&section=2 "Edit section's source code: References")\]
[Overview](../tutorials/Surface_Science_-_Tutorial.md) \>
[Ni 100 surface
relaxation](Ni_100_surface_relaxation.md) \>
[Ni 100 surface
DOS](Ni_100_surface_DOS.md) \>
[Ni 100 surface
bandstructure](Ni_100_surface_bandstructure.md) \>
[Ni 111 surface
relaxation](Ni_111_surface_relaxation.md) \>
[CO on Ni 111
surface](CO_on_Ni_111_surface.md) \>
[Ni 111 surface high
precision](Ni_111_surface_high_precision.md) \>
[partial DOS of CO on Ni 111
surface](Partial_DOS_of_CO_on_Ni_111_surface.md) \>
[vibrational frequencies of CO on Ni 111
surface](Vibrational_frequencies_of_CO_on_Ni_111_surface.md) \>
[STM of
graphite](STM_of_graphite.md) \>
[STM of
graphene](STM_of_graphene.md) \>
collective jumps of a Pt adatom on
fcc-Pt (001): Nudged Elastic Band Calculation
 \> [List of
tutorials](../categories/Category-Tutorials.md)


Back to the [main page](The_VASP_Manual.md).

[^kellog:prl64:3143-1]: G.L.Kellogg and Peter J.Feibelman, Phys. Rev. Lett. **64** (26), 3143 (1990)
[^NEB-2]: G. Mills, H. Jonsson and G. K. Schenter, Surface Science, **324**, 305 (1995); H. Jonsson, G. Mills and K. W. Jacobsen, \`Nudged Elastic Band Method for Finding Minimum Energy Paths of Transitions', in \`Classical and Quantum Dynamics in Condensed Phase Simulations', ed. B. J. Berne, G. Ciccotti and D. F. Coker (World Scientific, 1998)
