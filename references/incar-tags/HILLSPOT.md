<!-- Source: https://vasp.at/wiki/index.php/HILLSPOT | revid: 26682 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# HILLSPOT


During the metadynamics simulation, the time-dependent bias potential
(see [MDALGO](MDALGO.md)) is written in file
HILLSPOT using the same format
as for the [PENALTYPOT](../input-files/PENALTYPOT.md) file. If the
metadynamics is performed as a sequence of shorter runs (which is
recommended), the HILLSPOT
file should be copied into [PENALTYPOT](../input-files/PENALTYPOT.md)
at the end of each run. The following is an example of script running
the sequence of 100 simulations:

    #!/bin/bash
    i=1
    while [ $i -le 100 ]
    do
      cp POSCAR POSCAR.$i
      ./vasp
      cp CONTCAR POSCAR
      cp REPORT REPORT.$i
      cp HILLSPOT PENALTYPOT
      let i=i+1
    done

## Related Tags and Sections\[<a href="/wiki/index.php?title=HILLSPOT&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related Tags and Sections">edit</a> \| (./index.php.md)\]

[HILLS_BIN](HILLS_BIN.md),
[HILLS_H](HILLS_H.md), [HILLS_W](HILLS_W.md),
[MDALGO](MDALGO.md)

------------------------------------------------------------------------


