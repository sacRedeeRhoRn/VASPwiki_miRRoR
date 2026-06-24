<!-- Source: https://vasp.at/wiki/index.php/TMPCAR | revid: 29860 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# TMPCAR
TMPCAR is a binary file which is generated during dynamic simulations
and relaxation jobs using full wave function predication. It contains
the ionic positions and wave function of the previous two steps. Those
are needed for the extrapolation of the wave functions. It is possible
to use the TMPCAR file for MD continuation jobs by setting the flag
[ISTART](../incar-tags/ISTART.md)=3 in the file
[INCAR](../input-files/INCAR.md) file.

Instead of the TMPCAR file VASP.4.X can also use an internal scratch
file. This is faster and more efficient but requires of course more
memory (see [IWAVPR](../incar-tags/IWAVPR.md) for more details).

------------------------------------------------------------------------
