<!-- Source: https://vasp.at/wiki/index.php/Category:Bethe-Salpeter_equations | revid: 35510 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Bethe-Salpeter equations


The formalism of the Bethe-Salpeter equation (BSE) allows for
calculating the polarizability with the electron-hole interaction and
constitutes the state of the art for calculating absorption spectra in
solids.


## Contents


- [1
  Theory](#theory)
- [2
  Scaling](#scaling)
  - [2.1 Building
    matrix](#building-matrix)
  - [2.2 Solving
    equation](#solving-equation)
    - [2.2.1 Exact
      diagonalization](#exact-diagonalization)
    - [2.2.2
      Iterative
      solution](#iterative-solution)
- [3 Exact
  diagonalization](#exact-diagonalization-1)
- [4 Time
  evolution](#time-evolution)
- [5 Lanczos
  algorithm](#lanczos-algorithm)
- [6 X-ray
  absorption spectra](#x-ray-absorption-spectra)
- [7 Performing BSE
  calculations on GPU](#performing-bse-calculations-on-gpu)
- [8 Additional
  resources](#additional-resources)
  - [8.1
    Lectures](#lectures)
  - [8.2
    Tutorials](#tutorials)
  - [8.3 How
    to](#how-to)
- [9
  References](#references)


## Theory\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Theory">edit</a> \| (./index.php.md)\]

As discussed in detail in the [theory
page](Bethe-Salpeter_equation.md), the
Bethe-Salpeter equation is a non-hermitian eigenvalue problem

$\left(\begin{array}{cc} \mathbf{A} & \mathbf{B} \\ \mathbf{B}^\* &
\mathbf{A}^\* \end{array}\right)\left(\begin{array}{l}
\mathbf{X}_\lambda \\ \mathbf{Y}_\lambda
\end{array}\right)=\omega_\lambda\left(\begin{array}{cc} \mathbf{1} &
\mathbf{0} \\ \mathbf{0} & -\mathbf{1}
\end{array}\right)\left(\begin{array}{l} \mathbf{X}_\lambda \\
\mathbf{Y}_\lambda \end{array}\right)~.$

Using the eigenvectors $\mathbf{X}_\lambda,
\mathbf{Y}_\lambda$ and eigenvalues
$\omega_\lambda$ of this equation we can find the
dielectric function including the excitonic effects.

## Scaling\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Scaling">edit</a> \| (./index.php.md)\]

The steep scaling of BSE with the system size can be a limiting factor
for its application in large systems. This should be considered when
performing BSE calculations.

### Building matrix\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Building matrix">edit</a> \| (./index.php.md)\]

The [`ALGO`](../incar-tags/ALGO.md)` = BSE/TDHF` algorithm as a first step,
requires building the Hamiltonian of rank

$N_{\rm rank} = N_k\times N_c\times N_v$,

where $N_k$ is the
number of k-points in the full Brillouin zone and
$N_c$ and $N_v$ are the
number of conduction and valence bands, respectively. This computation
scales as

$N_k\times N_q\times (N_v\times N_v\times N_G\times N_c\times N_c)$,

where $N_q$ is the
number of q-points and $N_G$ number
of G-vectors. To simplify it, we can estimate this computation as
$N^4-N^5$ with the system size.

### Solving equation\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Solving equation">edit</a> \| (./index.php.md)\]

In the second step, the equation has to be solved. VASP provides
different methods for doing that.

#### Exact diagonalization\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Exact diagonalization">edit</a> \| (./index.php.md)\]

The exact diagonalization algorithm ([`IBSE`](../incar-tags/IBSE.md)` = 2`)
scales cubically with the matrix rank $N_{\rm rank}^3$ or as $N^6$ with the
system size.

#### Iterative solution\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Iterative solution">edit</a> \| (./index.php.md)\]

The iterative solution, as in the time-evolution
([`IBSE`](../incar-tags/IBSE.md)` = 1`) or Lanczos
([`IBSE`](../incar-tags/IBSE.md)` = 3`) algorithms, do not require
diagonalizaing the full matrix but instead, require computing the
matrix-vector multiplication for a number of steps or iterations
$m$. Thus, solving the equation via the time-evolution or
Lanczos algorithms scales as $N_{\rm rank}^2\times m$ or $N^4$ with the
system size. The number of iterations depends on the algorithm and the
required precision, which can be selected via
[BSEPREC](../incar-tags/BSEPREC.md) .

## Exact diagonalization\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Exact diagonalization">edit</a> \| (./index.php.md)\]

The diagonalization of the BSE Hamiltonian can be perform using various
eigensolvers provided in ScaLAPACK, ELPA, and cuSolver libraries. The
advantage of this approach is that the eigenvectors can be directly
obtained and used for the analysis of the excitons. Using the
eigenvalues $\omega_\lambda$ and eigenvectors $X_\lambda$
of the BSE Hamiltonian, the macroscopic dielectric which accounts for
the excitonic effects can be found

$\epsilon_M(\mathbf{q},\omega)= 1+2\lim_{\mathbf{q}\rightarrow
0}v(q)\sum_{\lambda} \left|\sum_{c,v,k}\langle
c\mathbf{k}|e^{i\mathbf{qr}}|v\mathbf{k}\rangle
X_\lambda^{cv\mathbf{k}}\right|^2 \times
\left(\frac{1}{\omega_\lambda - \omega - i\delta}\right)~.$

The following features are currently supported:

- <a href="/wiki/BSE_calculations#Bethe-Salpeter_equation_calculation"
  class="mw-redirect" title="BSE calculations">Calculating the dielectric
  function and eigenvectors</a>
- <a
  href="/wiki/BSE_calculations#Calculations_beyond_Tamm-Dancoff_approximation"
  class="mw-redirect" title="BSE calculations">Calculations beyond
  Tamm-Dancoff approximation</a>
- <a href="/wiki/BSE_calculations#Calculations_at_finite_wavevectors"
  class="mw-redirect" title="BSE calculations">Calculations of $\varepsilon(\mathbf{q},\omega)$ for $\mathbf{q}\neq0$</a>
- [Fatband plot](Plot_BSE_fatbands.md)

## Time evolution\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Time evolution">edit</a> \| (./index.php.md)\]

Alternatively, it is possible to use the time-evolution algorithm which
applies a short Dirac delta pulse of electric field and then follows the
evolution of the dipole moments. The dielectric function is found via a
Fourier transform
[^sander:jcp:2017-1]

$\epsilon_M(\omega)=1-\frac{4\pi}{\Omega}\int_0^{\infty} \mathrm{d} t
\sum_{c,v,\mathbf{k}}\left(\langle\mu_{cv\mathbf{k}}|
\xi_{cv\mathbf{k}}(t)\rangle+c . c .\right) e^{-i(\omega-i \delta) t}$,

where $\mu$ and
$\xi(t)$ are the dipole moments.

The solution found this way is strictly equivalent to the same solution
as the exact diagonalization and can be used for obtaining the
absorption spectrum, but does not yield the eigenvectors, which can be
limiting for the analysis of the excitons. The advantage of this
approach is the quadratic scaling with the size of the BSE Hamiltonian
$N_{rank}^2$.

The time-evolution algorithm can be selected by setting
[IBSE](../incar-tags/IBSE.md) = 1 in a BSE calculation. The required number
of steps in the time-evolution calculation depends on the broadening
[CSHIFT](../incar-tags/CSHIFT.md) and the maximum energy
[OMEGAMAX](../incar-tags/OMEGAMAX.md). The precision can be selected via
tag [BSEPREC](../incar-tags/BSEPREC.md).

|  |
|----|
| **Mind:** The required number of steps does not depend on the size of the Hamiltonian |

The following features are currently supported:

- Calculating the dielectric function
- Calculations beyond the Tamm-Dancoff approximation

## Lanczos algorithm\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Lanczos algorithm">edit</a> \| (./index.php.md)\]

The expression for the dielectric function can be re-written as a
continued fraction

$\epsilon_{\alpha\beta}(\omega) = \delta_{\alpha\beta} -
\frac{4\pi}{\Omega}\cfrac{|u_0|^2}{(\omega - a_1 + \mathrm i\eta) -
\cfrac{b_1^2}{(\omega -a_2 + \mathrm i\eta) - \cfrac{b_2^2}{...}}},$

where $|u_0\rangle$
is an initial guess vector computed from the dipole moments,
$|u_0\rangle = \sum_{cv\mathbf{k}} \langle
c\mathbf{k}|r_\alpha|v\mathbf{k}\rangle \langle
v\mathbf{k}|r_\beta|c\mathbf{k}\rangle$. The
$a$ and $b$
coefficients are evaluated iteratively, with the iterative algorithm
stopping once the difference between $\epsilon(\omega)$ from two consecutive iterations is below a certain
threshold selected by [BSEPREC](../incar-tags/BSEPREC.md).

Using the dipole moments as the starting point means that the iterative
algorithm is sensitive only to optically active transitions, i.e.
$v\to c$ transitions with non-zero dipole moment. As
such, the algorithm will ignore optically inactive transitions and can
reach convergence faster than other methods for larger matrices.

The following features are currently supported:

- Calculating the dielectric function

## X-ray absorption spectra\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: X-ray absorption spectra">edit</a> \| (./index.php.md)\]

The BSE/TDHF algorithm can also be used to model the X-ray absorption
spectra (XAS), i.e., excitations from the core states into conduction
bands. The detailed documentation of this method can be found in
[Category:XAS](../categories/Category-XAS.md).

## Performing BSE calculations on GPU\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Performing BSE calculations on GPU">edit</a> \| (./index.php.md)\]

As of VASP 6.5, the BSE/TDHF calculations with
[`IBSE`](../incar-tags/IBSE.md)` = 1` or [`IBSE`](../incar-tags/IBSE.md)` = 2`
can be fully run on NVIDIA GPUs. To be able to offload the BSE
calculations to GPUs one has to compile VASP with the
<a href="https://docs.nvidia.com/cuda/cusolvermp" class="external text"
rel="nofollow">cuSOLVERMp</a> and
<a href="https://docs.nvidia.com/cuda/cublasmp" class="external text"
rel="nofollow">cuBLASMp</a> libraries provided with NVHPC-SDK 24.7 or
newer. To be able to use these libraries VASP has to be compiled with
HPC-X (MPI shipped with NVHPC-SDK), which can be loaded via

    module load nvhpc-hpcx-cuda12/24.7

To enable these libraries in VASP, make sure to include the following
lines in your `makefile.include`

    CPP_OPTIONS+= -DCUSOLVERMP -DCUBLASMP
    LLIBS      += -cudalib=cusolvermp,cublasmp -lnvhpcwrapcal

To be able to perform the BSE calculation on GPUs, VASP needs to store
the full BSE Hamiltonian in the GPU memory, which is often the limiting
factor. The memory required to store the BSE Hamiltonian can be
estimated as $N_{\rm rank}^2\times 16\cdot
10^{-9}$ in Gb for
[`ANTIRES`](../incar-tags/ANTIRES.md)` = 0`. In the case of exact
diagonalization [`IBSE`](../incar-tags/IBSE.md)` = 2`, the eigensolver
requires an additional scratch space.

|  |
|----|
| **Mind:** When running BSE calculations on GPUs, we recommend not setting [OMEGAMAX](../incar-tags/OMEGAMAX.md) or setting it to a larger value so that all the bands selected in [NBANDSV](../incar-tags/NBANDSV.md) and [NBANDSO](../incar-tags/NBANDSO.md) are included in the kernel. Otherwise, additional data transfers between CPU and GPU might be required, which leads to a serious performance degradation on GPUs. |

## Additional resources\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Additional resources">edit</a> \| (./index.php.md)\]

### Lectures\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Lectures">edit</a> \| (./index.php.md)\]

- Lecture on the
  <a href="https://youtu.be/arTPHW28qNM" class="external text"
  rel="nofollow">Bethe-Salpeter equation and optical excitations</a>.

### Tutorials\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Tutorials">edit</a> \| (./index.php.md)\]

- Tutorial calculating optical absorption of C diamond using
  <a href="https://www.vasp.at/tutorials/latest/bse/part1/#BSE-e01"
  class="external text" rel="nofollow">G0W0</a>,
  <a href="https://www.vasp.at/tutorials/latest/bse/part1/#BSE-e02"
  class="external text" rel="nofollow">BSE</a>, and
  <a href="https://www.vasp.at/tutorials/latest/bse/part1/#BSE-e03"
  class="external text" rel="nofollow">TDDDH</a>.
- Tutorial calculating optical absorption of LiF using
  <a href="https://www.vasp.at/tutorials/latest/bse/part2/#BSE-e04"
  class="external text" rel="nofollow">G0W0</a>, the
  <a href="https://www.vasp.at/tutorials/latest/bse/part2/#BSE-e05"
  class="external text" rel="nofollow">independent particle approximation
  (IPA)</a>, the
  <a href="https://www.vasp.at/tutorials/latest/bse/part2/#BSE-e06"
  class="external text" rel="nofollow">random phase approximation
  (RPA)</a>, the
  <a href="https://www.vasp.at/tutorials/latest/bse/part2/#BSE-e07"
  class="external text" rel="nofollow">Tamm-Dancoff approximation</a>
  (TDA)\], and
  <a href="https://www.vasp.at/tutorials/latest/bse/part2/#BSE-e08"
  class="external text" rel="nofollow">beyond TDA</a>.
- Tutorial on the
  <a href="https://www.vasp.at/tutorials/latest/bse/part3/#BSE-e09"
  class="external text" rel="nofollow">efficient Brillouin zone
  sampling</a> and
  <a href="https://www.vasp.at/tutorials/latest/bse/part3/#BSE-e10"
  class="external text" rel="nofollow">exciton analysis</a>.
- Tutorial for calculating x-ray adsorption spectroscopy
  <a href="https://www.vasp.at/tutorials/latest/bse/part2"
  class="external text" rel="nofollow">XAS calculations</a> using the
  BSE.

### How to\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

- Practical guide for solving the Bethe-Salpeter equation via
  diagonalization <a href="/wiki/BSE_calculations" class="mw-redirect"
  title="BSE calculations">BSE calculations</a>.
- Practical guide for solving the Casida equation via diagonalization
  <a href="/wiki/TDDFT_calculations" class="mw-redirect"
  title="TDDFT calculations">TDDFT calculations</a>.
- Practical guide for using the [Bethe-Salpeter equation for core
  excitations](../tutorials/Bethe-Salpeter_equation_for_core_excitations.md).
- Practical guide for optimizing the [BSE
  calculations](../tutorials/Best_practices_for_Bethe-Salpeter_calculations.md).

## References\[<a
href="/wiki/index.php?title=Category:Bethe-Salpeter_equations&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^sander:jcp:2017-1]: [T. Sander, G. Kresse, *Macroscopic dielectric function within time-dependent density functional theory—Real time evolution versus the Casida approach* , J. Chem. Phys. *146*, 064110 (2017)](http://doi.org/10.1063/1.4975193)
