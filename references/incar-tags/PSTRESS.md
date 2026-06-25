<!-- Source: https://vasp.at/wiki/index.php/PSTRESS | revid: 25988 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PSTRESS


PSTRESS = \[real\]  
Default: **PSTRESS** = 0 

Description: Sets the external pressure in kB or adds corrections to the
stress tensor.

------------------------------------------------------------------------

The unit of PSTRESS is kB.

During <a href="/wiki/Ionic_minimization" class="mw-redirect"
title="Ionic minimization">ionic minimization</a>, an energy term
$E=
V \times \mathrm{PSTRESS}$ is added to the total energy
and the value of PSTRESS is
subtracted from the diagonals of the stress tensor. This allows to
perform structure optimization at a specific external pressure.

In <a href="/wiki/Molecular_dynamics" class="mw-redirect"
title="Molecular dynamics">molecular-dynamics calculations</a> within
the [NpT ensemble](../misc/NpT_ensemble.md),
PSTRESS controls the target
pressure for the
Parinello-Rahman<sup>[\[1\]](#cite_note-parrinello:prl:1980-1)[\[2\]](#cite_note-parrinello:jap:1981-2)</sup>
barostat.

Generally, if a negative value is supplied, the system is under
effective tensile strain and during relaxations (or molecular dynamics
simulations) the volume will increase. If a positive value is supplied,
the system is under compressive strain; this will decrease the volume
during relaxations and molecular dynamics simulations.

PSTRESS can also be used to
correct errors caused by the Pulay stress, i.e., errors in the
calculated stress tensor caused by the incomplete plane wave basis set.
To correct for Pulay-stress errors, set
PSTRESS to the negative value
of the Pulay stress. The Pulay stress is computed by taking the
difference between the external pressure at the desired cutoff and a
very large energy cutoff (check the lines 'external pressure' in the
[OUTCAR](../output-files/OUTCAR.md) file and calculate pressure at cutoff
you want to use $-$ pressure
at large cutoff; this must be a negative value). Before using this tag
in this manner, please read the following section carefully: [Volume
relaxation](../methods/Volume_relaxation.md).

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PSTRESS-_incategory-Examples)

------------------------------------------------------------------------


1.  [↑](#cite_ref-parrinello:prl:1980_1-0)
    <a href="https://doi.org/10.1103/PhysRevLett.45.1196"
    class="external text" rel="nofollow">M. Parrinello and A. Rahman, Phys.
    Rev. Lett. <strong>45</strong>, 1196 (1980).</a>
2.  [↑](#cite_ref-parrinello:jap:1981_2-0)
    <a href="https://doi.org/10.1063/1.328693" class="external text"
    rel="nofollow">M. Parrinello and A. Rahman, J. Appl. Phys.
    <strong>52</strong>, 7182 (1981).</a>


