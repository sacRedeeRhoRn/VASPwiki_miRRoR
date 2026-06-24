<!-- Source: https://vasp.at/wiki/index.php/Number_of_G-vectors_changed_in_the_star | revid: 19813 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Number of G-vectors changed in the star
This happens because the number of G vectors in the plane-wave basis for
each k-point is determined according to

$\frac{\hbar^2}{2m_e} (\mathbf{G+k})^2 <
\text{ENCUT}$

Using this criterion for different k-points will yield a different
number of G-vectors that fall within the sphere for each k-point.

VASP by default computes the orbitals for k points in the irreducible
Brillouin zone (IBZ) i.e. k-points that cannot be generated from another
in the set by symmetry. For some calculations, VASP needs to generate
the orbitals in the full Brillouin zone (FBZ) and does so by applying
the symmetry operations to the orbitals in the IBZ to get them in the
FBZ. The number of G-vectors within the sphere should be the same for
k-points that are in a star i.e. the set of k-points that are generated
by applying all the symmetry operations to one k-points in the IBZ.
Sometimes the number of G-vectors is different for k-points that are
within a star and you see this error

     -----------------------------------------------------------------------------
    |                                                                             |
    |     EEEEEEE  RRRRRR   RRRRRR   OOOOOOO  RRRRRR      ###     ###     ###     |
    |     E        R     R  R     R  O     O  R     R     ###     ###     ###     |
    |     E        R     R  R     R  O     O  R     R     ###     ###     ###     |
    |     EEEEE    RRRRRR   RRRRRR   O     O  RRRRRR       #       #       #      |
    |     E        R   R    R   R    O     O  R   R                               |
    |     E        R    R   R    R   O     O  R    R      ###     ###     ###     |
    |     EEEEEEE  R     R  R     R  OOOOOOO  R     R     ###     ###     ###     |
    |                                                                             |
    |     internal error in GENERATE_KPOINTS_TRANS: number of G-vector            |
    |     changed in star 570 569                                                 |
    |                                                                             |
    |       ---->  I REFUSE TO CONTINUE WITH THIS SICK JOB ... BYE!!! <----       |
    |                                                                             |
     -----------------------------------------------------------------------------

This should in principle not happen but it can happen because the
symmetry operations are found within the
[SYMPREC](../incar-tags/SYMPREC.md) tolerance.

There are a few things you can try to circumvent this problem:

- Symmetrize your POSCAR file using [this
  script](https://gist.github.com/henriquemiranda/e4a1b616693aac339ef011af6484f890)
  also see more details in
  [POSCAR](../input-files/POSCAR.md))

&nbsp;

- Try and change ENCUT slightly

&nbsp;

- Deactivate symmetries by setting ISYM=0 or ISYM=-1

  

------------------------------------------------------------------------
