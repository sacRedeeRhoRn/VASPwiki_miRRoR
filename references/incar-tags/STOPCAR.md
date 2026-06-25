<!-- Source: https://vasp.at/wiki/index.php/STOPCAR | revid: 22308 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# STOPCAR


Using the STOPCAR file it is
possible to stop VASP during the program execution. If the
STOPCAR file contains the line

    LSTOP = .TRUE.

then VASP stops at the next ionic step. On the other hand, if the
STOPCAR file contains the line

     LABORT = .TRUE.

VASP stops at the next electronic step, i.e.
[WAVECAR](../input-files/WAVECAR.md) and [CHGCAR](../input-files/CHGCAR.md)
might contain non converged results.

If possible use the first option.

------------------------------------------------------------------------


