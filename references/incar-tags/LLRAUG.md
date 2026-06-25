<!-- Source: https://vasp.at/wiki/index.php/LLRAUG | revid: 29602 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LLRAUG


LLRAUG = .TRUE. \| .FALSE.  
Default: **LLRAUG** = .FALSE. 

Description: LLRAUG calculates
the two-center contributions to the chemical shift tensor.

------------------------------------------------------------------------

LLRAUG switches on two-center
contributions to the NMR chemical shift tensor. These are contributions
due to the augmentation currents in other PAW spheres than the sphere
with the atom for which the shift tensor is calculated. Typically these
contributions are safely neglected. It makes sense to include them for
accurate calculations with hard potentials (`*_h`) on systems containing
also (non-hydrogen) atoms from the top rows of the periodic table (B, C,
N, O, F), typically with short bonds, e.g. C<sub>2</sub>H<sub>2</sub>,
where effects up to a few ppm are possible. Effects are most significant
for the H shift. For such systems using standard potentials typically
introduces larger inaccuracies. The two-center contributions are
calculated using a multipole expansion of the current density that is
represented on the plane wave grid; as in Sec. III.A.3 of. Ref.
<sup>[\[1\]](#cite_note-dewijs:jcp:2013-1)</sup>.
The relevance of LLRAUG to
achieve basis-set completeness for shieldings is discussed in Ref.
<sup>[\[2\]](#cite_note-dewijs:jcp:2021-2)</sup>
that compares to basis-set converged quantum chemical calculations
<sup>[\[3\]](#cite_note-jenssen:pccp:2016-3)</sup>.

## Related tags and articles\[<a href="/wiki/index.php?title=LLRAUG&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md)

## References\[<a href="/wiki/index.php?title=LLRAUG&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-dewijs:jcp:2013_1-0)
    <a href="https://doi.org/10.1063/1.4810799" class="external text"
    rel="nofollow">F. Vasconcelos, G.A. de Wijs, R. W. A. Havenith, M.
    Marsman, and G. Kresse, <em>Finite-field implementation of NMR chemical
    shieldings for molecules: Direct and converse gauge-including
    projector-augmented-wave methods</em>, J. Chem. Phys.
    <strong>139</strong>, 014109 (2013).</a>
2.  [↑](#cite_ref-dewijs:jcp:2021_2-0)
    <a href="https://doi.org/10.1063/5.0069637" class="external text"
    rel="nofollow">G.A. de Wijs, G. Kresse, R. W. A. Havenith, and M.
    Marsman, <em>Comparing GIPAW with numerically exact chemical shieldings:
    The role of two-center contributions to the induced current</em>, J.
    Chem. Phys. <strong>155</strong>, 234101 (2021).</a>
3.  [↑](#cite_ref-jenssen:pccp:2016_3-0)
    <a href="https://doi.org/10.1039/C6CP01294A" class="external text"
    rel="nofollow">S.R. Jensen, T. Flå, D. Jonsson, R.S. Monstad, K. Ruud,
    and L. Frediani, <em>Magnetic properties with multiwavelets and DFT: the
    complete basis set limit achieved</em>, Phys. Chem. Chem. Phys.
    <strong>18</strong>, 21145 (2016).</a>


