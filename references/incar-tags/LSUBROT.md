<!-- Source: https://vasp.at/wiki/index.php/LSUBROT | revid: 16896 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSUBROT
LSUBROT = .FALSE. \| .TRUE. 

|                     |           |     |
|---------------------|-----------|-----|
| Default: **SUBROT** | = .FALSE. |     |

Description: This flag can be set for [hybrid
functionals](../methods/Category-Hybrid_functionals.md)
(HF-type calculations). LSUBROT determines whether an optimal rotation
matrix between the occupied and unoccupied block is sought, when a
direct optimization of the energy functional is performed (i.e.
[ALGO](ALGO.md)=All \| Damped). The corresponding algorithm is
unpublished. LSUBROT =.FALSE. is the standard algorithm, in which the
rotation matrix between occupied and unoccupied orbitals is determined
essentially using Loewdin perturbation theory, as for instance explained
in Ref. ^([\[1\]](#cite_note-kresse:prb:96-1)). For LSUBROT =.TRUE. the
rotation matrix is instead optimized by performing a few standard SCF
steps, in which the orbitals are kept fixed, but rotations between the
occupied and unoccupied manifold are allowed. Once satisfactory
convergence has been reached, the optimized density matrix (rotation
matrix between occupied and unoccupied block) is passed back to the
direct optimization routine and a rotation along the suggested direction
is performed alongside an update of the orbitals. This generally speeds
up calculations for small gap systems as well as metals. However, in
rare cases, we have observed instabilities, so be careful when selecting
LSUBROT =.TRUE.

Although the flag can be set for standard functionals, it is only
efficient for hybrid functionals (HF-type calculations).

## References
1.  [↑](#cite_ref-kresse:prb:96_1-0) [G. Kresse and J. Furthmüller,
    Phys. Rev. B 54, 11169
    (1996).](http://link.aps.org/doi/10.1103/PhysRevB.54.11169)

------------------------------------------------------------------------
