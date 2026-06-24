<!-- Source: https://vasp.at/wiki/index.php/Vaspelph.h5 | revid: 33077 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# vaspelph.h5
  
The vaspelph.h5 file contains electron-phonon matrix elements and
related quantities. It is created when
[`ELPH_DRIVER`](../incar-tags/ELPH_DRIVER.md)` = mels`.

|  |
|----|
| **Important:** Within the [projector-augmented-wave method](../methods/Projector-augmented-wave_formalism.md), different definitions of the electron-phonon matrix element exist. In order to choose which one is used and written to vaspelph.h5, please use the [ELPH_DECOMPOSE](../incar-tags/ELPH_DECOMPOSE.md) tag. |

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.5.0 |

It is usually best to avoid writing the electron-phonon matrix elements
to disk. There are several reasons for this:

- The total number of matrix elements required for a particular
  electron-phonon calculation can be very large, thus requiring a lot of
  disk space.
- Writing to or reading from the hard drive is usually much slower than
  keeping data in memory. This can cause a performance bottleneck in
  your calculation. This is especially true on distributed clusters
  where additional communication is required.
- When running electron-phonon calculations directly inside VASP, it is
  possible to avoid calculating some matrix elements. For example,
  during [transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md),
  only the matrix elements close to the chemical potential have sizeable
  contributions. The ones further away are not calculated by default,
  which can give a significant performance boost. This advantage is lost
  when choosing to write the matrix elements to disk.

However, the information in the vaspelph.h5 file is still useful in some
situations. For example,
[`ELPH_DRIVER`](../incar-tags/ELPH_DRIVER.md)` = mels` can be used to
plot the electron-phonon matrix along high-symmetry lines or for
specific combinations of bands, modes and k/q-points.

## Contents

- [1 File Layout](#File_Layout)
  - [1.1 Group: /kpoints](#Group:_/kpoints)
    - [1.1.1 Datasets](#Datasets)
  - [1.2 Group: /matrix_elements](#Group:_/matrix_elements)
    - [1.2.1 Datasets](#Datasets_2)
- [2 Related tags and articles](#Related_tags_and_articles)

## File Layout
This section describes the structure of the HDF5 file used to store
electron-phonon matrix elements, electronic eigenvalues, phonon
frequencies, and associated metadata (e.g., array sizes, k-point
information). The file is organized into two main groups: **kpoints**
and **matrix_elements**.

- **/kpoints**: Contains data related to the k-point grids, symmetry
  operations, and mapping between the full Brillouin zone (FBZ) and the
  irreducible Brillouin zone (IBZ).
- **/matrix_elements**: Contains information on the electron-phonon
  interaction, including electron eigenvalues, phonon frequencies,
  matrix elements, and system dimensions (number of atoms, bands,
  k-points, spins).

Each group is described in detail below.

### Group: /kpoints
This group contains datasets related to the k-point grid and symmetry
mapping.

#### Datasets
nrotk  
*Shape:* Scalar

*Description:* Total number of symmetry operations in **igrpop**.

igrpop  
*Shape:* {nrotk, 3, 3}

*Description:* Stores symmetry operation matrices. Each
$3 \times 3$ matrix is associated with
one symmetry operation.

indx_fbz2ibz  
*Shape:* {nkpts_kp}

*Description:* Maps k-points from the FBZ to the IBZ.

irot_fbz2ibz  
*Shape:* {nkpts_kp}

*Description:* Stores the index to the symmetry operation in **igrpop**
associated with each FBZ k-point that maps to its corresponding IBZ
k-point.

vkpt_k  
*Shape:* {nkpts_k, 3}

*Description:* k-points in direct coordinates for the IBZ.

vkpt_kp  
*Shape:* {nkpts_kp, 3}

*Description:* k-points in direct coordinates for the FBZ.

wtkpt_k  
*Shape:* {nkpts_k}

*Description:* Weights corresponding to each IBZ k-point. These are used
for Brillouin zone integrations.

### Group: /matrix_elements
This group contains datasets for the electron–phonon coupling as well as
related electronic and phononic properties.

#### Datasets
nspin  
*Shape:* Scalar

*Description:* Number of spin channels used in the simulation. A value
of 1 indicates non-spin-polarized calculations, while 2 indicates
spin-polarized.

natoms  
*Shape:* Scalar

*Description:* Total number of atoms in the simulation cell.

nkpts_k  
*Shape:* Scalar

*Description:* Total number of k-points in the IBZ.

nkpts_kp  
*Shape:* Scalar

*Description:* Total number of k-points in the FBZ.

nbands_k  
*Shape:* Scalar

*Description:* Number of electronic bands associated with the IBZ.

nbands_kp  
*Shape:* Scalar

*Description:* Number of electronic bands associated with the FBZ.

band_start_k  
*Shape*: Scalar

*Description*: Starting index for the electronic bands associated with
the IBZ k-points.

band_start_kp  
*Shape:* Scalar

*Description:* Starting index for the electronic bands associated with
the FBZ k-points.

eigenvalues_k  
*Shape:* {nspin, nkpts_k, nbands_k}

*Description:* Electronic eigenvalues in eV for the IBZ k-points.

eigenvalues_kp  
*Shape:* {nspin, nkpts_kp, nbands_kp}

*Description:* Electronic eigenvalues in eV for the FBZ k-points.

elph  
*Shape:* {nspin, nkpts_kp, nkpts_k, 3\*natoms, nbands_kp, nbands_k, 2}

*Description:* Electron–phonon matrix elements in eV.

The last (fastest) dimension is due to complex numbers being stored as
two real numbers (real and imaginary parts).

**nkpts_kp** and **nbands_kp** refer to the initial (Ket) state.

**nkpts_k** and **nbands_k** refer to the final (Bra) state.

phonon_eigenvalues  
*Shape:* {nkpts_kp, nkpts_k, 3\*natoms}

*Description:* Phonon eigenvalues (frequencies) computed at each
k-point.

## Related tags and articles
[ELPH_DRIVER](../incar-tags/ELPH_DRIVER.md),
[ELPH_RUN](../incar-tags/ELPH_RUN.md), [Electron-phonon potential from
supercells](../tutorials/Electron-phonon_potential_from_supercells.md)
