<!-- Source: https://vasp.at/wiki/index.php/LVGVCALC | revid: 29604 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LVGVCALC
LVGVCALC = .TRUE. \| .FALSE.  
Default: **LVGVCALC** = .TRUE. 

Description: LVGVCALC switches on calculation of the *vGv* expression
for the orbital magnetic susceptibility.

LVGVCALC is available as of VASP.6.4.0.

------------------------------------------------------------------------

When performing a chemical shift calculation the standard *pGv*
susceptibility is calculated and used in the calculation of the CSA
tensor ^([\[1\]](#cite_note-yates:prb:2007-1)). When LVGVCALC is true,
the magnetic susceptibility is also calculated with the *vGv*
approximation. [LVGVAPPL](LVGVAPPL.md) determines whether
the *vGv* or *pGv* result is applied in the calculation of the
$\mathbf{G=0}$ contribution to the CSA
tensor.

The *vGv* expression for the orbital susceptibility was introduced by
d'Avezac *et al.* ^([\[2\]](#cite_note-avezac:prb:2007-2)). In VASP its
ultra-soft generalization is used
^([\[3\]](#cite_note-dewijs:havenith:jcp:2021-3)).

## Related tags and articles
[LCHIMAG](LCHIMAG.md),
[LVGVAPPL](LVGVAPPL.md)

## References
1.  [↑](#cite_ref-yates:prb:2007_1-0) [J. R. Yates, C. J. Pickard,
    and F. Mauri, *Calculation of NMR chemical shifts for extended
    systems using ultrasoft pseudopotentials*, Phys. Rev. B **76**,
    024401 (2007).](https://doi.org/10.1103/PhysRevB.76.024401)
2.  [↑](#cite_ref-avezac:prb:2007_2-0) [M. d'Avezac, N. Marzari, and F.
    Mauri, *Spin and orbital magnetic response in metals: Susceptibility
    and NMR shifts*, Phys. Rev. B **76**, 165122
    (2007).](https://doi.org/10.1103/PhysRevB.76.165122)
3.  [↑](#cite_ref-dewijs:havenith:jcp:2021_3-0) [G.A. de Wijs, G.
    Kresse, R. W. A. Havenith, and M. Marsman, *Spin and orbital
    magnetic response in metals: Susceptibility and NMR shifts*, J.
    Chem. Phys. **155**, 234101
    (2021).](https://doi.org/10.1063/5.0069637)
