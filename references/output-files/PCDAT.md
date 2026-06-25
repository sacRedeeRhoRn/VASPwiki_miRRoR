<!-- Source: https://vasp.at/wiki/index.php/PCDAT | revid: 24214 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PCDAT


The PCDAT file contains the
pair correlation function. For dynamic simulations
([IBRION](../incar-tags/IBRION.md)$\ge$0) an
averaged pair correlation is written to the file (see also
[NBLOCK](../incar-tags/NBLOCK.md), [KBLOCK](../incar-tags/KBLOCK.md),
[NPACO](../incar-tags/NPACO.md) and [APACO](../incar-tags/APACO.md)).

A sample output of the PCDAT
file for a system containing two element types looks as follows:

      1   8   1   0  0.8163705E+01  0.1000000E+04
     CAR
     structure name
       0   0   0
       1   1
     350 350 350
     350
      0.1000000E-09
      0.2857143E-11
       1
      0.1000000E-14  0.4027100E-09  0.4027100E-09  0.4027100E-09
      0.2410163E+04  0.2410163E+04
      0.000  0.000  0.000  0.000
      0.000  0.000  0.000  0.000
      0.000  0.000  0.000  0.000
      0.000  0.000  0.000  0.000
      0.000  0.000  0.000  0.000
      0.000  0.000  0.000  0.000
      0.000  0.000  0.000  0.000
      0.000  0.000  0.000  0.000
      0.000  0.000  0.000  0.000
      0.000  0.000  0.000  0.000
      0.000  0.000  0.000  0.000
      0.000  0.000  0.000  0.000
      0.000  0.000  0.000  0.000
      ...
      0.000  0.000  0.000  0.000
      0.165  0.000  0.331  0.000
      0.000  0.000  0.000  0.000
      0.152  0.000  0.304  0.000
      0.293  0.000  0.585  0.000
      0.844  0.000  1.688  0.000
      1.218  0.000  2.436  0.000
      1.173  0.000  2.346  0.000
      1.256  0.000  2.512  0.000
      1.453  0.000  2.906  0.000
      1.168  0.000  2.337  0.000
      1.918  0.000  3.836  0.000
      0.981  0.000  1.962  0.000
      1.580  0.000  3.161  0.000
      0.917  0.000  1.834  0.000
      0.986  0.000  1.972  0.000
      1.528  0.000  3.056  0.000
      1.203  0.000  2.405  0.000
      0.538  0.000  1.076  0.000
      0.869  0.000  1.739  0.000
      0.759  0.000  1.518  0.000 
      ...

Here is the description of each line:

- Line 1: 1 (fixed output), number of ions, 1 (fixed output), 0 (fixed
  output), unit cell volume divided by number of atoms, temperature.
- Line 2: CAR (fixed output).
- Line 3: Header of [INCAR](../input-files/INCAR.md) file (the tag
  [SYSTEM](../incar-tags/SYSTEM.md)).
- Line 4: 0, 0, 0 (all fixed output).
- Line 5: 1 (fixed output), [NBLOCK](../incar-tags/NBLOCK.md).
- Line 6: [NPACO](../incar-tags/NPACO.md), [NPACO](../incar-tags/NPACO.md),
  [NPACO](../incar-tags/NPACO.md).
- Line 7: [NPACO](../incar-tags/NPACO.md).
- Line 8: 0.1\*10<sup>-9</sup> (fixed output).
- Line 9: [APACO](../incar-tags/APACO.md)$\times$10<sup>-10</sup>/[NPACO](../incar-tags/NPACO.md).
- Line 10:
  [NSW](../incar-tags/NSW.md)/[NBLOCK](../incar-tags/NBLOCK.md)/[KBLOCK](../incar-tags/KBLOCK.md).
- Line 11: [POTIM](../incar-tags/POTIM.md)$\times$10<sup>-15</sup>, norm of lattice vector 1 times
  10<sup>-10</sup>, norm of lattice vector 2 times 10<sup>-10</sup>,
  norm of lattice vector 3 times 10<sup>-10</sup>.
- Line 12-(12+[NPACO](../incar-tags/NPACO.md)): Input mean
  temperature/([NBLOCK](../incar-tags/NBLOCK.md)$\times$[KBLOCK](../incar-tags/KBLOCK.md)), actual mean
  temperature.
- Following that the next [NPACO](../incar-tags/NPACO.md) lines show the
  pair correlation function for each species combination.
- Optional ([KBLOCK](../incar-tags/KBLOCK.md)$\times$[NBLOCK](../incar-tags/NBLOCK.md)/[NSW](../incar-tags/NSW.md))$\times$[NPACO](../incar-tags/NPACO.md)+1 lines: The above is
  repeated [KBLOCK](../incar-tags/KBLOCK.md)$\times$[NBLOCK](../incar-tags/NBLOCK.md)/[NSW](../incar-tags/NSW.md)
  times.

The order of species combinations (columns of the pair correlation
function) follows column-wise the lower triangle of the species
correlation matrix. That means for 3 species the order is the following:

    total 1-1  1-2  1-3  2-2  2-3  3-3

The numbers listed above corresponds to the species as encountered in
the [POSCAR](../input-files/POSCAR.md)/[POTCAR](../input-files/POTCAR.md)
file. The first column (total) reports the total pair correlation
function.

The PCDAT file contains no abscissa. To obtain the pair correlation
functions with the corresponding abscissa the following 'bash/awk'
script can be used:


**Click to show/*pair_correlation_xny.sh***


    file=PCDAT
    awk <$file >PCDAT.xy '
    NR==8 { pcskal=$1}
    NR==9 { pcfein=$1}
    NR==7 { npaco=$1}
    NR>=13 {  
      line=line+1
      if (line==1) s=s+1
      if (line==(npaco+1))  {
         print " "
         line=0
      }
      else  {
         a1[line]=  a1[line] + $1
         a2[line]=  a2[line] + $2
         a3[line]=  a3[line] + $3
         a4[line]=  a4[line] + $4
         print (line-0.5)*pcfein/pcskal,$1,$2, $3, $4, $5
      }
    }
    END {
     print "final sets=", s
     for (line=1 ; line<=npaco ; line++)
         print (line-0.5)*pcfein/pcskal,a1[line]/s,a2[line]/s,a3[line]/s,a4[line]/s
    }
    '


To use this script, in your folder with the
PCDAT file, please copy the
content to *pair_correlation_xny.sh* and type the following:

    bash pair_correlation_xny.sh 

The resulting pair correlation function is written to

    PCDAT.xy

## Related tags and articles\[<a href="/wiki/index.php?title=PCDAT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IBRION](../incar-tags/IBRION.md), [MDALGO](../incar-tags/MDALGO.md),
[NBLOCK](../incar-tags/NBLOCK.md), [KBLOCK](../incar-tags/KBLOCK.md),
[NSW](../incar-tags/NSW.md), [NPACO](../incar-tags/NPACO.md),
[APACO](../incar-tags/APACO.md)

------------------------------------------------------------------------


