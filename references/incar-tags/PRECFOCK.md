<!-- Source: https://vasp.at/wiki/index.php/PRECFOCK | revid: 34420 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PRECFOCK
PRECFOCK = Normal \| Accurate \| Fast \| Medium \| Single \| Low 

|  |  |  |
|----|----|----|
| Default: **PRECFOCK** | = Fast | for RPAR calculations |
|  | = Single | if [PREC](PREC.md)=Single or SingleN |
|  | = Normal | else |

Description: PRECFOCK controls the FFT grids used in the exact exchange
routines (Hartree-Fock and hybrid functionals).

------------------------------------------------------------------------

The FFT grid used for the exact exchange contributions can be chose to
be different from the one used for the Hartree and DFT potentials.
Information on the FFT grid that is used in the exact Fock exchange
routines is written to the [OUTCAR](../output-files/OUTCAR.md) file after
the lines

    FFT grid for exact exchange (Hartree Fock)

We recommend to set PRECFOCK=Normal for routine calculations. If speed
is an issue, you can also use PRECFOCK=Fast (e.g. use this to
pre-converge the orbitals). For very high precision, in particular for
phonon calculations, PRECFOCK=Accurate is recommended. The two setting,
PRECFOCK=Medium and PRECFOCK=Low are not recommended, but have been kept
to maintain compatibility with older VASP versions.

Generally, as opposed to gradient corrected density functionals, the
exact exchange energy is rather insensitive to the FFT grids, and in
many cases a rather coarse grid can be used to calculate the overlap
densities and the exact exchange (Fock) potential. [Exact
exchange](../redirects/Hybrid_functionals.md) requires one to
evaluation the overlap density

$\psi_{\mathbf{k}n}^{\*}(\mathbf{r})\psi_{\mathbf{q}m}(\mathbf{r})$

between two orbitals. Strictly speaking, errors in the convolution
(aliasing errors) are only avoided, if the FFT grid contains all Fourier
components up to twice the plane wave with the largest wave vector,
2\|G_(cut)\|. As usual, \|G_(cut)\| is determined by the plane wave
cutoff ([ENCUT](ENCUT.md)). A grid avoiding aliasing errors
is chosen by setting PRECFOCK=Accurate. In this case, the FFT grid for
the exact exchange is identical to the FFT grid used for the orbitals
for [PREC](PREC.md)=Accurate in the DFT part.
PRECFOCK=Accurate is the recommended setting for very accurate
calculations.

For PRECFOCK=Low and Fast, the smallest possible FFT grid that just
encloses the cutoff sphere (G_(cut)\|) is used. This accelerates the
calculations by roughly a factor two to three, but causes slight errors
in the total energies and some noise in the calculated forces. To reduce
the noise, the augmentation charges are made very soft for PRECFOCK=Fast
(whereas PRECFOCK=Low uses the standard augmentation charges also used
for DFT).

For PRECFOCK=Normal, the FFT grid for the exact exchange is identical to
the FFT grid used for the orbitals for [PREC](PREC.md)=Normal
in the DFT part. In this case, the grid density is between the ones for
PRECFOCK=Accurate and PRECFOCK=Fast. This is often a very reasonable
comprise and hence recommended for most routine calculations.

For PRECFOCK=Fast, Normal and Accurate, the augmentation charges
(required to restore the norm and dipoles of the overlap density on the
plane wave grid) are softened, such that an accurate presentation on the
plane wave grid is possible even for relatively coarse FFT grids. The
sphere size is printed out after

    Radii for the augmentation spheres in the nonlocal exchange

Since VASP always uses one-center terms to correct for the difference
between all-electron and pseudo orbitals, the precise shape of the
augmentation charges matters little for exchange energies. Still it is
recommended to keep PRECFOCK and PREC the same if relative energies are
calculated (for instance adsorption energies, energies differences
between different phases, etc.).

The following table summarizes the possible setting:

[TABLE]

Medium and Single are synonyms. They are useful the select the same
treatment for the Hartree and exchange term. This can be advantageously
for correlated wave function calculations to obtain a numerically exact
balance and compensation between Hartree and exchange (for instance for
the upcoming auxiliary field Monte-Carlo module in VASP). For
conventional Hartree-Fock or hybrid functional calculations, Normal or
Accurate should be used.

In this table, G_(cut) is determined by the relation

$E_{\rm cut}=\frac{\hbar^2}{2m_e}G_{\rm cut}^2$

with E_(cut)=[ENCUT](ENCUT.md).

Even PRECFOCK=Fast yields fairly low noise in the forces and virtually
no egg-box effects (aliasing errors). In the forces, the noise is
usually below 0.01 eV/Å. For PRECFOCK=N and PRECFOCK=A, noise is usually
not an issue, and the accuracy is sufficient even for phonon
calculations in large supercells.

Any combination of [PREC](PREC.md) and PRECFOCK is allowed by
the code. Useful settings of increasing precision are however:

    PREC = Normal ; PRECFOCK = Fast       ! if your are in need for speed
    PREC = Normal ; PRECFOCK = Normal     ! the default
    PREC = Accurate ; PRECFOCK = Normal   ! increase the precision for DFT part; since exchange dominates the compute time, only slightly slower
    PREC = Accurate ; PRECFOCK = Accurate ! highest accuracy, suggested for phonons

## Related tags and articles
[PREC](PREC.md), [ENCUT](ENCUT.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PRECFOCK-_incategory-Examples)

------------------------------------------------------------------------
