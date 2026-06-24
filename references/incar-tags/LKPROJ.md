<!-- Source: https://vasp.at/wiki/index.php/LKPROJ | revid: 27288 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LKPROJ
LKPROJ = .TRUE. \| .FALSE.  
Default: **LKPROJ** = .FALSE. 

Description: switches on the **k**-point projection scheme.

------------------------------------------------------------------------

For LKPROJ=.TRUE., VASP will project the orbitals onto the reciprocal
space of an alternative unit cell. This unit cell has to be supplied in
the file [POSCAR.prim](../misc/POSCAR.prim.md), in the usual
[POSCAR](../input-files/POSCAR.md) format.

As a first step, the **k**-projection scheme determines the set
{**k′**}, of **k**-points in the irreducible part of the first Brillouin
zone of the structure given in
[POSCAR.prim](../misc/POSCAR.prim.md), for which

$\langle \mathbf{k}'+\mathbf{G}' |
\mathbf{k}+\mathbf{G}\rangle \neq 0$

where **G** and **G′** are reciprocal space vectors in the reciprocal
spaces of the structures specified in [POSCAR](../input-files/POSCAR.md)
and [POSCAR.prim](../misc/POSCAR.prim.md), respectively. As
usual, the set of points {**k**} is specified in the
[KPOINTS](../input-files/KPOINTS.md) file. The set {**k′**} is written to
the [OUTCAR](../output-files/OUTCAR.md) file. Look at the part of the
[OUTCAR](../output-files/OUTCAR.md) following `NKPTS_PRIM`.

Once the set {**k′**} has been determined VASP will compute the
following

$\Kappa_{n\mathbf{k}\sigma\mathbf{k}'}=\sum_{\mathbf{GG}'} |\langle
\mathbf{k}'+\mathbf{G}'| \mathbf{k}+\mathbf{G}\rangle \langle
\mathbf{k}+\mathbf{G} | \psi_{n\mathbf{k}\sigma}\rangle |^2$

and writes this information onto the [PRJCAR](../output-files/PRJCAR.md) and
[vasprun.xml](../output-files/Vasprun.xml.md) files.

K_(n**k**σ**k′**) provides a measure of how strongly the orbital
$\Psi$_(n**k**σ) contributes at the
point **k′** in the reciprocal space of structure
[POSCAR.prim](../misc/POSCAR.prim.md).

One may, for instance, use this scheme to project the orbitals of a
supercell onto the reciprocal space of a generating primitive cell.

|  |
|----|
| **Warning:** At the moment the **k**-point projection only works with [NPAR](NPAR.md)=1. |

|                                               |
|-----------------------------------------------|
| **Mind:** Available as of VASP version 6.0.0. |

## Related tags and articles
[PRJCAR](../output-files/PRJCAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LKPROJ-_incategory-Examples)
