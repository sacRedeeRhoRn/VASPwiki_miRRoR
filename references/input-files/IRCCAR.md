<!-- Source: https://vasp.at/wiki/index.php/IRCCAR | revid: 37278 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IRCCAR
The IRCCAR file defines a discretized transformation path. Usually this
is taken from an [intrinsic reaction
coordinate](../tutorials/Intrinsic-reaction-coordinate_calculations.md)
(IRC) - using [IBRION](../incar-tags/IBRION.md)=40, projected onto a small
set of internal coordinates. It is required to define the path-based
coordinates `IS` and `IZ` in
[ICONST](ICONST.md)
^([\[1\]](#cite_note-branduari:parrinello:2007-1)).

However, this path is followed during a biased molecular dynamics (MD)
simulation, similar to the [Blue moon
ensemble](../theory/Blue_moon_ensemble.md) method,
[metadynamics](../theory/Metadynamics.md), and other [advanced
MD
aproaches](../categories/Category-Advanced_molecular-dynamics_sampling.md)
^([\[2\]](#cite_note-bucko:book:2025-2)). The structure of the file is:

    M
    chi_1(1) chi_2(1) ... chi(r)(1)
    chi_1(2) chi_2(2) ... chi(r)(2)
    ...
    chi_1(M) chi_2(M) ... chi(r)(M)

where `M` is the number of points in the file and `chi_j(i)` is
$\tilde{\chi}_k(i)$, the discretized
transformation path in terms of internal coordinates, taking values
between 0 and 1.

|  |
|----|
| **Mind:** Contact [Tomáš Bučko](https://fns.uniba.sk/en/tomas-bucko/) for necessary Python scripts to prepare this file. |

## Related tags and articles
[ICONST](ICONST.md)

## References
1.  [↑](#cite_ref-branduari:parrinello:2007_1-0) [D. Branduardi, F.
    Gervasio, and M. Parrinello, *From A to B in free energy space*, J.
    Chem. Phys. **126**, 054103
    (2007).](https://doi.org/10.1063/1.2432340)
2.  [↑](#cite_ref-bucko:book:2025_2-0) [T. Bučko, *Investigating
    chemical reactions with VASP - A practical guide*, Comenius
    University Bratislava (2025),
    p.50-51.](https://stella.uniba.sk/texty/PRIF_TB_investigating_chemical_reactions_vasp.pdf)
