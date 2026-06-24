<!-- Source: https://vasp.at/wiki/index.php/Tkatchenko-Scheffler_method_with_iterative_Hirshfeld_partitioning | revid: 29766 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Tkatchenko-Scheffler method with iterative Hirshfeld partitioning
The [Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md),
which uses fixed neutral atoms as a reference to estimate the effective
volumes of atoms-in-molecule (AIM) and to calibrate their
polarizabilities and dispersion coefficients, fails to describe the
structure and the energetics of ionic solids. As shown in references
^([\[1\]](#cite_note-bucko:jctc:13-1)) and
^([\[2\]](#cite_note-bucko:jcp:14-2)), this problem can be solved by
replacing the conventional Hirshfeld partitioning used to compute
properties of interacting atoms by the iterative scheme proposed by
Bultinck^([\[3\]](#cite_note-bultinck:jcp:07-3)). In this iterative
Hirshfeld algorithm (HI), the neutral reference atoms are replaced with
ions with fractional charges determined together with the AIM charge
densities in a single iterative procedure. The algorithm is initialized
with a promolecular density defined by non-interacting neutral atoms.
The iterative procedure then runs in the following steps:

- The Hirshfeld weight function for the step $i$ is computed as

$w_A^{i}({\mathbf{r}}) =
{n^{i}_A({\mathbf{r}})}/\left({\sum_B n^{i}_B({\mathbf{r}})}\right)$

where the sum extends over all atoms in the system.

- The number of electrons per atom is determined using

$N_{A}^{i+1} = N_{A}^{i} + \int \left\[
n_{A}^{i}(\mathbf{r}) - w_{A}^i(\mathbf{r})\\n(\mathbf{r})
\right\]\\d^{3}\mathbf{r}.$

- New reference charge densities are computed using

$n^{i+1}_A(\mathbf{r}) =
n^{\text{lint}(N^i_A)}(\mathbf{r})\left \[
\text{uint}(N^i_A)-N^i_A\right \] +
n^{\text{uint}(N_A^i)}({\mathbf{r}})\left \[ N^i_A -
\text{lint}(N^i_A)\right \]$

where $\text{lint}(x)$ expresses the
integer part of $x$ and
$\text{uint}(x)=\text{lint}(x)+1$.

Steps (1) to (3) are iterated until the difference in the electronic
populations between two subsequent steps ($\Delta_{A}^{i} = \vert N_{A}^{i}-N_{A}^{i+1}\vert$) is less
than a predefined threshold for all atoms. The converged iterative
Hirshfeld weights ($w_{A}^{i}$) are
then used to define the AIM properties needed to evaluate the dispersion
energy (see [Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md)).

The TS-HI method is described in detail in reference
^([\[1\]](#cite_note-bucko:jctc:13-1)) and its performance in
optimization of various crystalline systems is examined in reference
^([\[2\]](#cite_note-bucko:jcp:14-2)).

## Usage
The Tkatchenko-Scheffler method with iterative Hirshfeld partitioning
(TS-HI) is invoked by setting [IVDW](../incar-tags/IVDW.md)=21. The
convergence criterion for iterative Hirshfeld partitioning (in e) can
optionally be defined via the parameter
[HITOLER](../incar-tags/HITOLER.md) (the default value is 5e-5). Other
optional parameters controlling the input for the calculation are as in
the conventional [Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md).
The default value of the adjustable parameter
[VDW_SR](../incar-tags/VDW_SR.md) is 0.95 and corresponds to the PBE
functional.

[TABLE]

## Related tags and articles
[HITOLER](../incar-tags/HITOLER.md), [VDW_SR](../incar-tags/VDW_SR.md),
[VDW_ALPHA](../incar-tags/VDW_ALPHA.md),
[VDW_C6](../incar-tags/VDW_C6.md), [VDW_R0](../incar-tags/VDW_R0.md),
[VDW_S6](../incar-tags/VDW_S6.md), [VDW_D](../incar-tags/VDW_D.md),
[LVDW_EWALD](../incar-tags/LVDW_EWALD.md), [IVDW](../incar-tags/IVDW.md),
[Tkatchenko-Scheffler
method](Tkatchenko-Scheffler_method.md),
[Self-consistent screening in Tkatchenko-Scheffler
method](Self-consistent_screening_in_Tkatchenko-Scheffler_method.md),
[Many-body dispersion
energy](Many-body_dispersion_energy.md),
[Many-body dispersion energy with fractionally ionic model for
polarizability](Many-body_dispersion_energy_with_fractionally_ionic_model_for_polarizability.md)

## References
1.  ↑ ^([a](#cite_ref-bucko:jctc:13_1-0))
    ^([b](#cite_ref-bucko:jctc:13_1-1)) [T. Bučko, S. Lebègue, J.
    Hafner, and J. G. Ángyán, J. Chem. Theory Comput. **9**, 4293
    (2013)](https://doi.org/10.1021/ct400694h)
2.  ↑ ^([a](#cite_ref-bucko:jcp:14_2-0))
    ^([b](#cite_ref-bucko:jcp:14_2-1)) [T. Bučko, S. Lebègue, J. G.
    Ángyán, and J. Hafner, J. Chem. Phys. **141**, 034114
    (2014).](https://doi.org/10.1063/1.4890003)
3.  [↑](#cite_ref-bultinck:jcp:07_3-0) [P. Bultinck, C. Van
    Alsenoy, P. W. Ayers, and R. Carbó Dorca, J. Chem. Phys. **126**,
    144111 (2007).](https://doi.org/10.1063/1.2715563)
4.  [↑](#cite_ref-kerber:jcc:08_4-0) [T. Kerber, M. Sierka, and J.
    Sauer, J. Comput. Chem. **29**, 2088
    (2008).](https://doi.org/10.1002/jcc.21069)

------------------------------------------------------------------------
