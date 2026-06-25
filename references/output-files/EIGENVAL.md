<!-- Source: https://vasp.at/wiki/index.php/EIGENVAL | revid: 30963 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# EIGENVAL


The EIGENVAL file contains the
Kohn-Sham-eigenvalues for all k-points, at the end of the simulation.
For dynamic simulations ([IBRION](../incar-tags/IBRION.md)=0) the
eigenvalues on the file are usually the ones predicted for the next
step: i.e. the file is compatible with the
[CONTCAR](CONTCAR.md) file. For static calculations and
relaxations ([IBRION](../incar-tags/IBRION.md)=-1\|1\|2) the eigenvalues
are the solution of the KS-equations for the last step.

Mind: For dynamic simulations ([IBRION](../incar-tags/IBRION.md)=0) the
EIGENVAL file contains
predicted wavefunctions compatible with the
[CONTCAR](CONTCAR.md) file. If you want to use the
eigenvalues for additional calculations, first copy the
[CONTCAR](CONTCAR.md) file to the
[POSCAR](../input-files/POSCAR.md) file and make another static
([ISTART](../incar-tags/ISTART.md)=1, [NSW](../incar-tags/NSW.md)=0)
continuation run with [ICHARG](../incar-tags/ICHARG.md)=1.

  

------------------------------------------------------------------------


