<!-- Source: https://vasp.at/wiki/index.php/WAVECAR | revid: 22293 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# WAVECAR


The WAVECAR file is a binary file containing the following data:

         NBAND       number of bands
         ENCUTI      'initial' cut-off energy
         AX          'initial' basis vectors defining the supercell
         CELEN       ('initial') eigenvalues
         FERWE       ('initial') Fermi-weights
         CPTWFP      ('initial') wavefunctions

Usually WAVECAR provides
excellent starting wavefunctions for a continuation job. For dynamic
simulation ([IBRION](../incar-tags/IBRION.md)=0) the wavefunctions in the
file are usually those predicted for the next step: i.e. the file is
compatible with [CONTCAR](../output-files/CONTCAR.md). The
WAVECAR,
[CHGCAR](CHGCAR.md) and the
[CONTCAR](../output-files/CONTCAR.md) file can be used consistently for a
molecular dynamics continuation job. For static calculations and
relaxations ([IBRION](../incar-tags/IBRION.md)=-1,1,2) the written
wavefunctions are the solution of the KS-equations for the last step. It
is possible to avoid, that the
WAVECAR is written out by
setting

    LWAVE  =  .FALSE.

in the [INCAR](INCAR.md) file.

Mind: For dynamic simulations ([IBRION](../incar-tags/IBRION.md)=0) the
WAVECAR file contains
predicted wavefunctions compatible with
[CONTCAR](../output-files/CONTCAR.md). If you want to use the wavefunctions
for additional calculations, first copy
[CONTCAR](../output-files/CONTCAR.md) to [POSCAR](POSCAR.md)
and make another static ([ISTART](../incar-tags/ISTART.md)=1;
[NSW](../incar-tags/NSW.md)=0) continuation run with
[ICHARG](../incar-tags/ICHARG.md)=1.

------------------------------------------------------------------------


