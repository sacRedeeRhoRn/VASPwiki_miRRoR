<!-- Source: https://vasp.at/wiki/index.php/Fcc_Ni_DOS | revid: 10425 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Fcc Ni DOS



[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc
Si](Fcc_Si.md) \>
[fcc Si
DOS](Fcc_Si_DOS.md) \>
[fcc Si
bandstructure](Fcc_Si_bandstructure.md) \>
[cd
Si](Cd_Si.md) \>
[cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si
relaxation](Cd_Si_relaxation.md) \>
[beta-tin
Si](Beta-tin_Si.md) \>
[fcc
Ni](Fcc_Ni.md) \>
[graphite TS binding
energy](Graphite_TS_binding_energy.md) \>
[graphite MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#task)
- [2
  Incar](#incar)
  - [2.1
    POSCAR](#poscar)
  - [2.2
    INCAR](#incar-1)
  - [2.3
    KPOINTS](#kpoints)
- [3
  Calculation](#calculation)
- [4
  Download](#download)


## Task\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

Calculation of the DOS in fcc Ni.

## Incar\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Incar">edit</a> \| (./index.php.md)\]

### [POSCAR](../input-files/POSCAR.md)\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

    fcc:
     3.53 
     0.5 0.5 0.0
     0.0 0.5 0.5
     0.5 0.0 0.5
       1
    cartesian
    0 0 0

  

### [INCAR](../input-files/INCAR.md)\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

     SYSTEM = fcc Ni
     ISTART = 0 ; ICHARG = 2
     ENCUT  = 270
     ISMEAR = -5 
     LORBIT = 11
        
     ISPIN  = 2
     MAGMOM = 1

### [KPOINTS](../input-files/KPOINTS.md)\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

    k-points
     0
    Monkhorst Pack
     11 11 11
     0  0  0

## Calculation\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Calculation">edit</a> \| (./index.php.md)\]

- The bash-script `plotdos` invokes *awk* and *gnuplot* to get the DOS
  from the [vasprun.xml](../output-files/Vasprun.xml.md) file and plot
  it.

<!-- -->

    awk 'BEGIN{i=1} /dos>/,\
                    /\/dos>/ \
                     {a[i]=$2 ; b[i]=$3 ; i=i+1} \
         END{for (j=12;j<i-5;j++) print a[j],b[j]}' vasprun.xml > dos.dat

    ef=`awk '/efermi/ {print $3}' vasprun.xml`

    cat >plotfile<<!
    # set term postscript enhanced eps colour lw 2 "Helvetica" 20
    # set output "optics.eps"
    plot "dos.dat" using (\$1-$ef):(\$2) w lp
    !

    gnuplot -persist plotfile

    rm dos.dat plotfile

## Download\[<a
href="/wiki/index.php?title=Fcc_Ni_DOS&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/2/2c/2_8_fccNi_dos.tgz" class="internal"
title="2 8 fccNi dos.tgz">2_8_fccNi_dos.tgz</a>

------------------------------------------------------------------------


