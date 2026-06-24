<!-- Source: https://vasp.at/wiki/index.php/HFRCUT | revid: 21504 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# HFRCUT
HFRCUT = \[real\]  
Default: **HFRCUT** = 0 

Description: HFRCUT specifies how the [Coulomb kernel is approximated at
G=0](../methods/Coulomb_singularity.md) when the Fock
energy and the exchange potential are evaluated.

------------------------------------------------------------------------

In systems with periodic boundary conditions, the Coulomb energy and the
Coulomb potential are usually evaluated under the assumption of a
compensating background by introducing a compensation charge density.
This is well-justified for the Hartree energy, where the compensation
charge density stems from the ions. Yet, this assumption is not valid
for the Fock exchange, which causes an error. For the Fock exchange
potential and energy, one can correct the resulting error by assuming
that the density matrix is local. The leading order correction is given
by the difference between the electrostatic energy of a localized model
charge density in a homogeneous background periodically repeated and the
same model charge density in isolation. For details we refer to J. Paier
*et al.,*^([\[1\]](#cite_note-paier:jcp:05-1)) Section II. D. 4.

- HFRCUT = 0: Ewald summation *or* method of Massida, Posternak, and
  Baldereschi depending on
  k-mesh^([\[2\]](#cite_note-gygi:prb:86-2)[\[3\]](#cite_note-massidda:prb:93-3))

If a regular automatic k-mesh and the standard 1/r Coulomb kernel are
used, the correction is computed using Ewald summations. If the k-mesh
is *not* regular (e.g., if the k-points are explicitly listed in the
[KPOINTS](../input-files/KPOINTS.md) file) or if kernels different from
the bare Coulomb kernel are used (e.g., HSE functional), the method of
Massida, Posternak, and
Baldereschi^([\[2\]](#cite_note-gygi:prb:86-2)[\[3\]](#cite_note-massidda:prb:93-3))
is used. This approach assumes that the model charge density is an
error-function-like charge distribution in real space in order to handle
the long-range nature of the potential in reciprocal space. It requires
setting a decay constant for the error function, see
[HFALPHA](HFALPHA.md). Both methods, the Ewald summation
and the method of Massida, Posternak, and Baldereschi, are strictly
equivalent for regular k-mesh.

- HFRCUT = -1: Automated cutoff
  radius^([\[4\]](#cite_note-spenceralavi:prb:08-4))

An alternative recipe is to replace the 1/r Coulomb kernel with a
truncated Coulomb kernel that is strictly zero beyond a certain cutoff
radius. If HFRCUT is set to -1, the radial cutoff is chosen to be
equivalent to the radius of the sphere with a volume of the unit cell
times the total number of k-points in the full Brillouin zone. For
instance, for a 4x4x4 k-point grid, that yields 64 times the volume of
the unit cell.

- HFRCUT = \[cutoff radius\]: Manually set cutoff radius in Ångström.

In the limit of many k-points, both methods (HFRCUT=-1 and HFRCUT=0)
should yield identical results. In our experience, the HFRCUT=-1
converges more rapidly for systems with a gap, as well as molecules and
atoms, whereas HFRCUT=0 converges faster for metallic systems. It is
expedient to first converge the energies with respect to the number of
k-points for both methods and then select for subsequent calculations
the method that converges more rapidly. A detailed comparison of the
convergence of the different methods for metallic and gapped materials
was made by Sundararaman and
Arias^([\[5\]](#cite_note-sundararamanarias:prb:13-5)).

## Related tags and articles
[AEXX](AEXX.md), [AGGAX](AGGAX.md),
[AGGAC](AGGAC.md), [ALDAC](ALDAC.md),
[HFALPHA](HFALPHA.md), [LTHOMAS](LTHOMAS.md),
[List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md),
[Coulomb singularity](../methods/Coulomb_singularity.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-HFRCUT-_incategory-Examples)

## References
1.  [↑](#cite_ref-paier:jcp:05_1-0) [J. Paier, R. Hirschl, M. Marsman,
    and G. Kresse, J. Chem. Phys. **122**, 234102
    (2005).](https://doi.org/10.1063/1.1926272)
2.  ↑ ^([a](#cite_ref-gygi:prb:86_2-0))
    ^([b](#cite_ref-gygi:prb:86_2-1)) [F. Gygi and A. Baldereschi, Phys.
    Rev. B **34**, 4405(R)
    (1986).](https://doi.org/10.1103/PhysRevB.34.4405)
3.  ↑ ^([a](#cite_ref-massidda:prb:93_3-0))
    ^([b](#cite_ref-massidda:prb:93_3-1)) [S. Massidda, M. Posternak,
    and A. Baldereschi, Phys. Rev. B **48**, 5058
    (1993).](https://doi.org/10.1103/PhysRevB.48.5058)
4.  [↑](#cite_ref-spenceralavi:prb:08_4-0) [J. Spencer and A. Alavi,
    Phys. Phys. Rev. B **77**, 193110
    (2008).](https://doi.org/10.1103/PhysRevB.77.193110)
5.  [↑](#cite_ref-sundararamanarias:prb:13_5-0) [R. Sundararaman
    and T. A. Arias, Phys. Rev. B **87**, 165122
    (2013).](https://doi.org/10.1103/PhysRevB.87.165122)

------------------------------------------------------------------------
