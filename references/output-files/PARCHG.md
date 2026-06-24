<!-- Source: https://vasp.at/wiki/index.php/PARCHG | revid: 35866 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PARCHG
PARCHG is an output file created when [partial charge
densities](../redirects/Band-decomposed_charge_densities.md)
are calculated by setting [LPARD](../incar-tags/LPARD.md) = .TRUE.. The
file has the same structure as the [CHG](CHG.md) file,
containing the structure followed by the charge density on the fine FFT
grid, but missing the augmentation occupancies that are written to
[CHGCAR](../input-files/CHGCAR.md). The units are also equivalent to
[CHG](CHG.md) and [CHGCAR](../input-files/CHGCAR.md).

The partial density written to PARCHG is part of the valence electron
density that was converged selfconsistently in a previous run. The bands
and **k** points that contribute to the partial charges are selected by
the [IBAND](../incar-tags/IBAND.md), [NBMOD](../incar-tags/NBMOD.md),
[EINT](../incar-tags/EINT.md) and [KPUSE](../incar-tags/KPUSE.md) tags,
allowing for fine control of the contributions to the partial charge
density.

## Contents

- [1 PARCHG.nb.nk files](#PARCHG.nb.nk_files)
- [2 Format](#Format)
  - [2.1 Spin-polarized calculation](#Spin-polarized_calculation)
- [3 Related tags and articles](#Related_tags_and_articles)

## PARCHG.nb.nk files
If [LSEPB](../incar-tags/LSEPB.md) and/or [LSEPK](../incar-tags/LSEPK.md) are
set to .TRUE. variants of the PARCHG file are written, separating the
contributing bands and **k** points respectively. The units and format
of the files stay the same.

- If [`LSEPB`](../incar-tags/LSEPB.md)` = .TRUE.`, **PARCHG.nb.ALLK** files
  are written, where nb is an index over all bands contributing to the
  partial charge density.

&nbsp;

- If [`LSEPK`](../incar-tags/LSEPK.md)` = .TRUE.`, **PARCHG.ALLB.nk** files
  are created, where nk runs over all **k** points in
  [KPUSE](../incar-tags/KPUSE.md) or all **k** points if
  [KPUSE](../incar-tags/KPUSE.md) is not set.

&nbsp;

- For [`LSEPB`](../incar-tags/LSEPB.md)` = .TRUE.` and
  [`LSEPK`](../incar-tags/LSEPK.md)` = .TRUE.`, all combinations are
  written to **PARCHG.nb.nk** files.

|  |
|----|
| **Mind:** If VASP 6.5.0 or later is used, the code is compiled with [HDF5 support](../misc/Makefile.include.md) "Makefile.include"), and [LPARDH5](../incar-tags/LPARDH5.md) = .TRUE., all output will be redirected to the [vaspout.h5](Vaspout.h5.md) file, where it can be analyzed with [py4vasp](https://vasp.at/py4vasp/latest/index.html). |

## Format
The PARCHG consists of the following blocks:

- Structure in [POSCAR](../input-files/POSCAR.md) format
- FFT-grid dimensions [NGXF](../incar-tags/NGXF.md),
  [NGYF](../incar-tags/NGYF.md), [NGZF](../incar-tags/NGZF.md)
- Partial charge density times FFT-grid volume is written with multiple
  real numbers per line until all
  [NGXF](../incar-tags/NGXF.md)\*[NGYF](../incar-tags/NGYF.md)\*[NGZF](../incar-tags/NGZF.md)
  values of the block are written.

The real-space mesh (NX,NY,NZ) is uniform and is spanned by the lattice
vectors $\vec{a}, \vec{b}, \vec{c}$
defined in the structure block. The coordinates of the mesh points can
be restored via

$(N_x,N_y,N_z) \hat{=}
\frac{N_x-1}{N_{GXF}}\mathbf{a}+\frac{N_y-1}{N_{GYF}}\mathbf{b}+\frac{N_z-1}{N_{GZF}}\mathbf{c}$.

The dimensions can be increased by increasing the cutoff energy
([ENCUT](../incar-tags/ENCUT.md)) or explicitly by setting the fine
FFT-grid dimensions ([NGXF](../incar-tags/NGXF.md),
[NGYF](../incar-tags/NGYF.md), [NGZF](../incar-tags/NGZF.md)).

To arrange the data on the real-space grid in the unit cell, mind that
the data runs fastest over NX and slowest over NZ. To be more explicit,
the density is written using the following command in Fortran

` WRITE(IU,FORM) (((C(NX,NY,NZ),NX=1,`[`NGXF`](../incar-tags/NGXF.md)`),NY=1,`[`NGYF`](../incar-tags/NGYF.md)`),NZ=1,`[`NGZF`](../incar-tags/NGZF.md)`) `.

|  |
|----|
| **Important:** Remember that the values must be divided by the FFT-grid volume and the cell volume to obtain the partial charge density $n(r)$ in units $1/\AA^3$. |

Hence,

$n(r)=data(r)/(V_{grid}\*V_{cell}),$

$V_{grid} = N_{GXF}\*N_{GYF}\*N_{GZF},$

$V_{cell} =
|\mathbf{a}\cdot(\mathbf{b}\times\mathbf{c})|$,

where $n(r)$ is the partial charge
density in units 1/Å$^3$.

### Spin-polarized calculation
In spin-polarized calculations, two data sets are stored in the PARCHG
file. The first set contains the total partial density (spin up + spin
down), and the second is the magnetization density (spin up - spin
down). Each block is separated by a blank line and a line containing the
fine FFT grid dimensions [NGXF](../incar-tags/NGXF.md)
[NGYF](../incar-tags/NGYF.md) [NGZF](../incar-tags/NGZF.md).

- Structure
- FFT-grid dimensions
- Partial charge density times FFT-grid volume (spin up + spin down)
- FFT-grid dimensions
- Partial magnetization density (spin up - spin down)

## Related tags and articles
[LPARD](../incar-tags/LPARD.md), [LPARDH5](../incar-tags/LPARDH5.md),
[IBAND](../incar-tags/IBAND.md), [EINT](../incar-tags/EINT.md),
[NBMOD](../incar-tags/NBMOD.md), [KPUSE](../incar-tags/KPUSE.md),
[LSEPB](../incar-tags/LSEPB.md), [LSEPK](../incar-tags/LSEPK.md),
[Band-decomposed charge
densities](../redirects/Band-decomposed_charge_densities.md)

------------------------------------------------------------------------
