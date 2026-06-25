<!-- Source: https://vasp.at/wiki/index.php/CHG | revid: 29880 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CHG


This file contains the lattice vectors, atomic coordinates and the total
charge multiplied by the grid volume $n(r)\times V_{\mathrm{grid}}$ on the fine FFT-grid
(<a href="/wiki/index.php?title=NG(X,Y,Z)F&amp;action=edit&amp;redlink=1"
class="new" title="NG(X,Y,Z)F (page does not exist)">NG(X,Y,Z)F</a>,
with $V_\mathrm{grid}$ = [NGXF](../incar-tags/NGXF.md)$\times$[NGYF](../incar-tags/NGYF.md)$\times$[NGZF](../incar-tags/NGZF.md)) at every tenth MD step i.e.

    MOD(NSTEP,10)==1,

where
<a href="/wiki/index.php?title=NSTEP&amp;action=edit&amp;redlink=1"
class="new" title="NSTEP (page does not exist)">NSTEP</a> starts from 1.
To save disc space less digits are written to the
CHG file than to the
[CHGCAR](../input-files/CHGCAR.md). The file can be used to provide data
for visualization programs, for instance IBM data explorer (for the IBM
data explorer, a tool exists to convert the
CHG file to a valid data
explorer file). It is possible to avoid that the
CHG file is written out by
setting

    LCHARG  =  .FALSE. 

in the [INCAR](../input-files/INCAR.md) file. The data arrangement of the
CHG file is similar to that of
the [CHGCAR](../input-files/CHGCAR.md) file, with the exception of the PAW
one centre occupancies, which are missing on the
CHG file.

------------------------------------------------------------------------


