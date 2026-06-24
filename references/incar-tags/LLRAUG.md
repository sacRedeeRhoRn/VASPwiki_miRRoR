<!-- Source: https://vasp.at/wiki/index.php/LLRAUG | revid: 29602 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LLRAUG
LLRAUG = .TRUE. \| .FALSE.  
Default: **LLRAUG** = .FALSE. 

Description: LLRAUG calculates the two-center contributions to the
chemical shift tensor.

------------------------------------------------------------------------

LLRAUG switches on two-center contributions to the NMR chemical shift
tensor. These are contributions due to the augmentation currents in
other PAW spheres than the sphere with the atom for which the shift
tensor is calculated. Typically these contributions are safely
neglected. It makes sense to include them for accurate calculations with
hard potentials (`*_h`) on systems containing also (non-hydrogen) atoms
from the top rows of the periodic table (B, C, N, O, F), typically with
short bonds, e.g. C₂H₂, where effects up to a few ppm are possible.
Effects are most significant for the H shift. For such systems using
standard potentials typically introduces larger inaccuracies. The
two-center contributions are calculated using a multipole expansion of
the current density that is represented on the plane wave grid; as in
Sec. III.A.3 of. Ref. ^([\[1\]](#cite_note-dewijs:jcp:2013-1)). The
relevance of LLRAUG to achieve basis-set completeness for shieldings is
discussed in Ref. ^([\[2\]](#cite_note-dewijs:jcp:2021-2)) that compares
to basis-set converged quantum chemical calculations
^([\[3\]](#cite_note-jenssen:pccp:2016-3)).

## Related tags and articles
[LCHIMAG](LCHIMAG.md)

## References
1.  [↑](#cite_ref-dewijs:jcp:2013_1-0) [F. Vasconcelos, G.A. de
    Wijs, R. W. A. Havenith, M. Marsman, and G. Kresse, *Finite-field
    implementation of NMR chemical shieldings for molecules: Direct and
    converse gauge-including projector-augmented-wave methods*, J. Chem.
    Phys. **139**, 014109 (2013).](https://doi.org/10.1063/1.4810799)
2.  [↑](#cite_ref-dewijs:jcp:2021_2-0) [G.A. de Wijs, G.
    Kresse, R. W. A. Havenith, and M. Marsman, *Comparing GIPAW with
    numerically exact chemical shieldings: The role of two-center
    contributions to the induced current*, J. Chem. Phys. **155**,
    234101 (2021).](https://doi.org/10.1063/5.0069637)
3.  [↑](#cite_ref-jenssen:pccp:2016_3-0) [S.R. Jensen, T. Flå, D.
    Jonsson, R.S. Monstad, K. Ruud, and L. Frediani, *Magnetic
    properties with multiwavelets and DFT: the complete basis set limit
    achieved*, Phys. Chem. Chem. Phys. **18**, 21145
    (2016).](https://doi.org/10.1039/C6CP01294A)
