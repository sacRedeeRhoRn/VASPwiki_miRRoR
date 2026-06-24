<!-- Source: https://vasp.at/wiki/index.php/ELFCAR | revid: 29877 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ELFCAR
The ELFCAR file is created when the [LELF](../incar-tags/LELF.md)=*.TRUE.*
in the [INCAR](../input-files/INCAR.md) file is set and contains the
electron localization function denoted by $ELF$ in Ref. ^([\[1\]](#cite_note-silvi:nature:371-1)).

The same file format is used as for the [CHGCAR](../input-files/CHGCAR.md)
file. That is, lattice vectors, atomic coordinates and number of
cartesian sampling points $N_x, N_y, N_z$ are written, followed by $ELF(x,y,z)$ with $x$ being the fastest
and $z$ the slowest index.

For [ISPIN](../incar-tags/ISPIN.md)=2, $ELF_{\uparrow}$ is written first followed by
$ELF_{\downarrow}$.

It is recommended to avoid wrap around errors, when evaluating the
ELFCAR file. This can be done by specifying
[PREC](../incar-tags/PREC.md)=*High* in the [INCAR](../input-files/INCAR.md)
file.

- N.B. The electronic localization function is not implemented for
  non-collinear calculations.

## References
1.  [↑](#cite_ref-silvi:nature:371_1-0) [B. Silvi and A. Savin, Nature
    371, 683-686
    (1994).](http://www.nature.com/nature/journal/v371/n6499/pdf/371683a0.pdf)

------------------------------------------------------------------------
