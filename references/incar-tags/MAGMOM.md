<!-- Source: https://vasp.at/wiki/index.php/MAGMOM | revid: 36612 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# MAGMOM
MAGMOM = \[real array\] 

|  |  |  |
|----|----|----|
| Default: **MAGMOM** | = NIONS \* 1.0 | for [ISPIN](ISPIN.md)=2 |
|  | = 3 \* NIONS \* 1.0 | for noncollinear magnetic systems ([LNONCOLLINEAR](LNONCOLLINEAR.md)=.TRUE.) |

Description: Initial magnetic moment for each atom if no magnetization
density is present. Considered when symmetry is determined.

------------------------------------------------------------------------

- For a **magnetic calculation from scratch**
  ([ISTART](ISTART.md)=0), MAGMOM specifies (i) the initial
  on-site magnetic moment for each atom, and (ii) lowers the symmetry of
  the system (as of VASP.4.4.4). A magnetic calculation could be either
  a spin-polarized calculation ([ISPIN](ISPIN.md)=2) or
  noncollinear calculation
  ([LNONCOLLINEAR](LNONCOLLINEAR.md)=T). If the
  MAGMOM line breaks a symmetry of the crystal, the corresponding
  symmetry operation is removed and not applied during the
  symmetrization of, e.g., charges and forces.

&nbsp;

- When **restarting a magnetic calculation**, MAGMOM is only used to
  determine the symmetry of the system and not to set the on-site
  magnetic moment. Therefore, if you remove the MAGMOM tag before
  restarting from a converged [WAVECAR](../input-files/WAVECAR.md) or
  [CHGCAR](../input-files/CHGCAR.md), the magnetization is likely to be
  symmetrized away.

&nbsp;

- MAGMOM also specifies the initial on-site magnetic moments when a
  **magnetic calculation** ([ISPIN](ISPIN.md)=2 or
  [LNONCOLLINEAR](LNONCOLLINEAR.md)=T) is **started
  from a non-spin-polarized calculation**
  ([ISPIN](ISPIN.md)=1 and
  [LNONCOLLINEAR](LNONCOLLINEAR.md)=F). This implies
  restarting with [ICHARG](ICHARG.md)=1 while the
  [CHGCAR](../input-files/CHGCAR.md) file contains no magnetization
  density. Starting magnetic calculations from a non-spin-polarized
  calculation can improve convergence.

The [I_CONSTRAINED_M](I_CONSTRAINED_M.md) tag can
constrain the on-site magnetic moments.

|  |
|----|
| **Tip:** To converge to the magnetic ground state, we recommend setting the magnetic moments slightly larger than the expected values, e.g., using the experimental magnetic moment multiplied by 1.2-1.5. A growing collection of experimental data is available at the Bilbao crystallographic server.^([\[1\]](#cite_note-bilbao.crystal.server-1)) If no experimental data is available, MAGMOM can be defined according to the procedure outlined in the Huebsch et al. 2021.^([\[2\]](#cite_note-huebsch:prx:11-2)) |

|  |
|----|
| **Important:** The final magnetic state strongly depends on the initial values for MAGMOM.^([\[2\]](#cite_note-huebsch:prx:11-2)) This is true even if no symmetry is used ([ISYM](ISYM.md)=-1), because of the many local minima that most exchange-correlation functionals have within spin-density-functional theory. |

## Format and basis
- For a spin-polarized calculation ([ISPIN](ISPIN.md)=2),
  MAGMOM is a list of NIONS positive or negative values that specify the
  magnitude and relative orientation of the magnetization on each ion.
  The on-site magnetic moments have no direction in real space, i.e., no
  orientation in the lattice.

&nbsp;

- For noncollinear calculation
  ([LNONCOLLINEAR](LNONCOLLINEAR.md)=T), the on-site
  magnetic moment is specified by three components for each ion. Without
  spin-orbit coupling ([LSORBIT](LSORBIT.md)=False), the
  total energy depends only on the relative direction of the on-site
  magnetic moments. Hence, you can give the desired magnetic structure
  in Cartesian coordinates without considering how the lattice matrix or
  [SAXIS](SAXIS.md) is defined.

&nbsp;

- With spin-orbit coupling ([LSORBIT](LSORBIT.md)=True),
  the three components must be specified in the basis of spinor space
  that is defined by [SAXIS](SAXIS.md). The default is
  $\sigma_1=\hat x$,
  $\sigma_2 =\hat y$,
  $\sigma_3 = \hat z$, such that MAGMOM
  can be given in Cartesian coordinates. The orientation of MAGMOM with
  respect to the lattice only matters if spin-orbit coupling is included
  ([LSORBIT](LSORBIT.md)).

## Examples
- The most simple input for a bcc cell with antiferromagnetic (AFM) spin
  alignment would be the following.

[POSCAR](../input-files/POSCAR.md) file:

    AFM
     2.80000
     1.00000   .00000   .00000
      .00000  1.00000   .00000
      .00000   .00000  1.00000
     1 1
    Cartesian
      .00000   .00000   .00000
      .50000   .50000   .50000

with

     ISPIN = 2
     MAGMOM = 1.0 -1.0

specified in [INCAR](../input-files/INCAR.md). In a perfectly AFM ordered
cell, the total net magnetisation is zero, but the local magnetic
moments can be written to the [OUTCAR](../output-files/OUTCAR.md) file by
setting [LORBIT](LORBIT.md) tag (and if
[LORBIT](LORBIT.md)\<10 , the [RWIGS](RWIGS.md)
tag in addition) in the [INCAR](../input-files/INCAR.md) file.

- If you have problems converging to a desired magnetic solution, try to
  calculate first the non-magnetic ground state and continue from the
  generated [WAVECAR](../input-files/WAVECAR.md) and
  [CHGCAR](../input-files/CHGCAR.md). To restart, e.g., a calculation with
  two atoms that have equally large and antiferromagnetically coupled
  on-site magnetic moments, you need to set the following in the
  [INCAR](../input-files/INCAR.md) file:

&nbsp;

    ICHARG = 1 
    ISPIN = 2 
    MAGMOM = m -m

or for a noncollinear

    ICHARG = 1
    LNONCOLLINEAR = T
    MAGMOM = 0 0 m  0 0 -m

- For systems containing many atoms, MAGMOM input on a single line can
  be hard to read, especially in the noncollinear case. It is possible
  to provide [INCAR](../input-files/INCAR.md) input on [multiple
  lines](../input-files/INCAR.md) using backslashes (**\\**) as
  linebreaks. E.g. for a noncollinear system with AFM alignment and 16
  atoms (the first 8 of them magnetic), the multi-line input could look
  like this:

&nbsp;

    MAGMOM =  3.0  2.0  1.0 \
             -3.0 -2.0 -1.0 \
              3.0  2.0  1.0 \
             -3.0 -2.0 -1.0 \
              3.0  2.0  1.0 \
             -3.0 -2.0 -1.0 \
              3.0  2.0  1.0 \
             -3.0 -2.0 -1.0 \
              24*0.0

## Related Tags and Sections
[ISPIN](ISPIN.md),
[LNONCOLLINEAR](LNONCOLLINEAR.md),
[LSORBIT](LSORBIT.md), [SAXIS](SAXIS.md),
[LORBIT](LORBIT.md),
[I_CONSTRAINED_M](I_CONSTRAINED_M.md),
[NUPDOWN](NUPDOWN.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-MAGMOM-_incategory-Examples)

------------------------------------------------------------------------

1.  [↑](#cite_ref-bilbao.crystal.server_1-0) [MAGNDATA, Bilbao
    crystallographic
    server](https://www.cryst.ehu.es/magndata/search.php?show_db=1)
2.  ↑ ^([a](#cite_ref-huebsch:prx:11_2-0))
    ^([b](#cite_ref-huebsch:prx:11_2-1)) [Huebsch, M-T and Nomoto, T and
    Suzuki, M-T and Arita, R,*Benchmark for ab initio prediction of
    magnetic structures based on cluster-multipole theory*, Phys. Rev. X
    **11**, 011031 (2021).](http://doi.org/10.1103/PhysRevX.11.011031)
