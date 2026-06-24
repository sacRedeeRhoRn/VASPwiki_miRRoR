<!-- Source: https://vasp.at/wiki/index.php/Category:Biased_molecular_dynamics | revid: 35861 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Biased molecular dynamics
*Biased molecular dynamics'* (MD) refers to advanced [MD-simulation
methods](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
that introduce a *bias potential*. One of the most important purposes of
using bias potentials is to enhance the sampling of phase space with low
probability density (e.g., transition regions of chemical reactions).
Depending on the type of sampling and in combination with the
corresponding statistical methods one then has access to important
thermodynamic quantities like, e.g., free energies. Biased molecular
dynamics comes in very different flavors such as, e.g., umbrella
sampling^([\[1\]](#cite_note-torrie:jcp:1977-1)) and umbrella
integration^([\[2\]](#cite_note-kaestner:jcp:2005-2)), to name a few.
For a comprehensive description (especially about umbrella sampling), we
refer the interested user to Ref.
^([\[3\]](#cite_note-frenkel:ap-book:2002-3)) written by D. Frenkel and
B. Smit.

The probability density for a geometric parameter ξ of the system driven
by a Hamiltonian

$H(q,p) = T(p) + V(q), \\$

with *T*(*p*), and *V*(*q*) being kinetic, and potential energies,
respectively, can be written as

$P(\xi_i)=\frac{\int\delta\Big(\xi(q)-\xi_i\Big)
\exp\left\\-H(q,p)/k_B\\T\right\\ dq\\dp}{\int
\exp\left\\-H(q,p)/k_B\\T\right\\dq\\dp} =
\langle\delta\Big(\xi(q)-\xi_i\Big)\rangle_{H}.$

The term $\langle X \rangle_H$ stands
for a thermal average of quantity *X* evaluated for the system driven by
the Hamiltonian *H*.

If the system is modified by adding a bias potential
$\tilde{V}(\xi)$ acting on one or
multiple selected internal coordinates of the system ξ=ξ(*q*), the
Hamiltonian takes the form

$\tilde{H}(q,p) = H(q,p) + \tilde{V}(\xi),$

and the probability density of ξ in the biased ensemble is

$\tilde{P}(\xi_i)= \frac{\int
\delta\Big(\xi(q)-\xi_i\Big) \exp\left\\-\tilde{H}(q,p)/k_B\\T\right\\
dq\\dp}{\int \exp\left\\-\tilde{H}(q,p)/k_B\\T\right\\dq\\dp} =
\langle\delta\Big(\xi(q)-\xi_i\Big)\rangle_{\tilde{H}}.$

It can be shown that the biased and unbiased averages are related via

$P(\xi_i)=\tilde{P}(\xi_i)
\frac{\exp\left\\\tilde{V}(\xi)/k_B\\T\right\}{\langle
\exp\left\\\tilde{V}(\xi)/k_B\\T\right\\ \rangle_{\tilde{H}}}.$

More generally, an observable

$\langle A \rangle_{H} = \frac{\int A(q)
\exp\left\\-H(q,p)/k_B\\T\right\\ dq\\dp}{\int
\exp\left\\-H(q,p)/k_B\\T\right\\dq\\dp}$

can be expressed in terms of thermal averages within the biased ensemble
as

$\langle A \rangle_{H} =\frac{\langle A(q)
\\\exp\left\\\tilde{V}(\xi)/k_B\\T\right\\ \rangle_{\tilde{H}}}{\langle
\exp\left\\\tilde{V}(\xi)/k_B\\T\right\\ \rangle_{\tilde{H}}}.$

One of the most popular methods using bias potentials is umbrella
sampling^([\[1\]](#cite_note-torrie:jcp:1977-1)). This method uses a
bias potential to enhance sampling of ξ in regions with low
*P*(ξ_(*i*)), e.g., transition regions of chemical reactions. The
correct distributions are recovered afterward using the equation for
$\langle A \rangle_{H}$ above.

## Contents

- [1 How to](#How_to)
  - [1.1 Available potentials](#Available_potentials)
    - [1.1.1 Harmonic potentials](#Harmonic_potentials)
    - [1.1.2 Step function](#Step_function)
    - [1.1.3 Gaussian potential](#Gaussian_potential)
  - [1.2 Output](#Output)
- [2 Examples of usage](#Examples_of_usage)
- [3 Related methods in VASP](#Related_methods_in_VASP)
- [4 References](#References)

## How to
- First one needs to setup a [standard molecular
  dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
  run. The bias potentials are supported in both the
  [NVT](../misc/NVT_ensemble.md) and
  [NpT](../misc/NpT_ensemble.md) MD simulations, regardless of
  the particular
  [thermostat](Category-Thermostats.md) and/or
  [barostat](../incar-tags/PSTRESS.md) setting.

|  |
|----|
| **Mind:** Mind that for VASP 5.x the biased molecular dynamics runs have to be chosen by adding 10 to the chosen value of [MDALGO](../incar-tags/MDALGO.md). E.g. [MDALGO](../incar-tags/MDALGO.md)=12 instead of [MDALGO](../incar-tags/MDALGO.md)=2 has to be chosen for [Nosé-Hoover thermostat](../tutorials/Nosé-Hoover_thermostat.md). |

- Then one needs to set the geometric parameters and bias potential
  types. The geometric parameters ξ, also called collective variables,
  that are controlled via the potentials are defined in the
  [ICONST](../input-files/ICONST.md) file. The type of bias potential is
  also set in this file. The format of this file follows this layout:

&nbsp;

    flag item(1) ... item(N) status

Here `flag` specifies the type of geometric parameters (bond lengths,
angles, etc.), `item(1) ... item(N)` the actual geometric items (atom
numbers, etc.) and the `status` sets the type of used bias potential.
[Here](../input-files/ICONST.md) we advise the user to also look into the
description of the full capabilities of the geometric parameters.

- To avoid the update of the bias potential
  [HILLS_BIN](../incar-tags/HILLS_BIN.md)=[NSW](../incar-tags/NSW.md) is set
  by default.
- Next one needs to set the parameters of the potential in the
  [INCAR](../input-files/INCAR.md) (harmonic and step function) file or in
  the [PENALTYPOT](../input-files/PENALTYPOT.md) file (Gaussian). The
  following table summarizes the available potentials with their
  corresponding parameters:

|  |  |  |
|:--:|:--:|:--:|
| Potential type | `status` in [ICONST](../input-files/ICONST.md) | [INCAR](../input-files/INCAR.md) parameters |
| Harmonic potential | 8 | [SPRING_K](../incar-tags/SPRING_K.md), [SPRING_R0](../incar-tags/SPRING_R0.md), optional [SPRING_V0](../incar-tags/SPRING_V0.md) |
| Step function | 4 | [FBIAS_A](../incar-tags/FBIAS_A.md), [FBIAS_D](../incar-tags/FBIAS_D.md), and [FBIAS_R0](../incar-tags/FBIAS_R0.md) |
| Gaussian potential | 5 | parameters set in [PENALTYPOT](../input-files/PENALTYPOT.md) file |

### Available potentials
[![](https://vasp.at/wiki/images/thumb/4/43/Bias_potentials.png/300px-Bias_potentials.png)](https://vasp.at/wiki/File:Bias_potentials.png)

Fig.1) Graphical representation of (a) harmonic, (b) Fermi
function-shaped, and (c) and Gauss function-shaped bias potentials.

In the following details are given on how to control the available bias
potentials in VASP that are plotted in Fig.1.

#### Harmonic potentials
A sum of Harmonic potentials (curve (a) in Fig.1)

$\tilde{V}(\xi_1,\dots,\xi_{M_8}) =
\sum_{\mu=1}^{M}\frac{1}{2}\kappa_{\mu} (\xi_{\mu}(q)-\xi_{0\mu})^2
\\$

where the sum runs over all ($M_8$)
coordinates the potential acts upon. The potential is chosen in the
[ICONST](../input-files/ICONST.md) file by setting the `status` to 8. The
parameters of the potential are the force constant
$\kappa_{\mu}$
([SPRING_K](../incar-tags/SPRING_K.md)) and the minimum or the potential
$\xi_{0\mu}$
[SPRING_R0](../incar-tags/SPRING_R0.md). These must be set in the
[INCAR](../input-files/INCAR.md) file. Optionally, it is possible to change
the value of $\xi_{0\mu}$ every MD step
at a constant rate defined via the [INCAR](../input-files/INCAR.md) tag
[SPRING_V0](../incar-tags/SPRING_V0.md).

|  |
|----|
| **Mind:** The number of items defined via [SPRING_K](../incar-tags/SPRING_K.md), [SPRING_R0](../incar-tags/SPRING_R0.md), and [SPRING_V0](../incar-tags/SPRING_V0.md) must be equal to $M_8$. Otherwise, the calculation terminates with an error message. |

This form of bias potential is employed in several simulation protocols,
such as the umbrella sampling^([\[1\]](#cite_note-torrie:jcp:1977-1)),
umbrella integration, or steered MD, and is useful also in cases where
the $\xi_{\mu}$ values need to be
restrained.

#### Step function
A sum of Fermi-like step functions (curve (b) in Fig.1)

$\tilde{V}(\xi_1,\dots,\xi_{M_4}) =
\sum_{\mu=1}^{M_4}\frac{A_{\mu}}{1+\text{exp}\left
\[-D_{\mu}(\frac{\xi(q)}{\xi_{0\mu}} -1) \right \]} \\$

where the sum runs over all ($M_4$)
coordinates the potential acts upon. The potential is chosen in the
[ICONST](../input-files/ICONST.md) file by setting the `status` to 4. The
parameters of the potential are the height of the step
($A_{\mu}$ set by
[FBIAS_A](../incar-tags/FBIAS_A.md)), the slope around the point
$\xi_{0\mu}$ ($D_{\mu}$ set by [FBIAS_D](../incar-tags/FBIAS_D.md)), and the
position of the step ($\xi_{0\mu}$ set
by [FBIAS_R0](../incar-tags/FBIAS_R0.md)). These must be set in the
[INCAR](../input-files/INCAR.md) file.

|  |
|----|
| **Mind:** The number of items defined via [FBIAS_A](../incar-tags/FBIAS_A.md), [FBIAS_D](../incar-tags/FBIAS_D.md), and [FBIAS_R0](../incar-tags/FBIAS_R0.md) must be equal to $M_4$. Otherwise, the calculation terminates with an error message. |

This form of potential is suitable especially for imposing restrictions
on the upper (or lower) limit of the value of $\xi$.

#### Gaussian potential
A sum of Gauss functions (curve (b) in Fig.1)

$\tilde{V}(\xi_1,\dots,\xi_{M}) =
\sum_{\nu=1}^{N_5}h_{\nu}\text{exp}\left
\[-\frac{\sum_{\mu=1}^{M_5}(\xi_{\mu}(q)-\xi_{0\nu,\mu})^2}{2w_{\nu}^2}
\right \], \\$

where $N_5$ is the number of Gaussian
functions and $M_5$ is the number of
coordinates the potential acts upon. The potential is chosen in the
[ICONST](../input-files/ICONST.md) file by setting the `status` to 5. The
parameters of the potentials, $h_{\nu}$, $w_{\nu}$, and
$\xi_{0\nu,\mu}$ are defined in the
[PENALTYPOT](../input-files/PENALTYPOT.md) file.

This type of bias potential is primarily intended for use in
metadynamics, but since Gaussians can be used as basis functions for
more general shapes, they can also be used to prepare various atypically
shaped bias potentials.

### Output
The values of all collective variables defined in the
[ICONST](../input-files/ICONST.md) file for each MD step are listed in the
[REPORT](../output-files/REPORT.md) file. Check the lines after the string
`Metadynamics`.

## Examples of usage
Let us consider the nucleophile substitution reaction of
CH$_3$Cl with Cl$^-$. The reactant is a weak van-der-Waals complex. The
corresponding [POSCAR](../input-files/POSCAR.md) file reads

    vdW complex CH3Cl...Cl 
    1.00000000000000
    12.0000000000000000    0.0000000000000000    0.0000000000000000
    0.0000000000000000    12.0000000000000000    0.0000000000000000
    0.0000000000000000    0.0000000000000000    12.0000000000000000
    C H Cl
    1 3 2
    cart
    5.91331371  7.11364924  5.78037960
    5.81982231  8.15982106  5.46969017
    4.92222130  6.65954232  5.88978969
    6.47810398  7.03808479  6.71586385
    4.32824726  8.75151396  7.80743202
    6.84157897  6.18713289  4.46842049

Due to the weak interactions between CH$_3$Cl and Cl$^-$, the complex can
collapse at high temperatures. This can be avoided by setting an upper
bound for the length of the non-bonding Cl...C interactions. This can be
conveniently achieved by using a Fermi-like step-shaped bias potential.
To this end, we need to define the Cl...C distance, i.e., the distance
between the atoms 1 and 5, as a coordinate with status 4 in the
[ICONST](../input-files/ICONST.md) file:

    R 1 5 4   

Next, we need to set the molecular dynamics parameters and specify the
bias potential parameters [FBIAS_A](../incar-tags/FBIAS_A.md),
[FBIAS_D](../incar-tags/FBIAS_D.md), and
[FBIAS_R0](../incar-tags/FBIAS_R0.md) in the
[INCAR](../input-files/INCAR.md) file:

    # Molecular dynamics part
    IBRION = 0
    TEBEG = 300
    TEEND = 300
    MDALGO = 2
    POTIM = 2.0
    NSW = 10000
    # Bias potential part
    FBIAS_A  = 1
    FBIAS_D  = 50
    FBIAS_R0 = 3.5

Since the bias potential acts only on one internal coordinate
($M_4=1$), we need to provide only one
number for each of the tags. The chosen bias potential parameters ensure
that repulsive bias forces steeply increase when the C...Cl distance is
increased beyond about $3.2 \AA$. This
causes a shortening of the distance in the next MD step. Notice that the
bias force is essentially negligible for distances below
$3 \AA$. A careful adjustment of
[FBIAS_A](../incar-tags/FBIAS_A.md) and
[FBIAS_D](../incar-tags/FBIAS_D.md) is needed to ensure that (i) the bias
force is large enough to effectively limit the value of
$\xi$, and (ii) the interval of
$\xi$ values for which the bias forces
are significant is broad enough to avoid overcoming via random
fluctuations. A suitable setting can be found by noting that the maximal
bias force of $\frac{D\\A}{4\xi_0}$ is
exerted on the system at the point $\xi = \xi_{0}$. This can be seen by inspecting the analytical expression for
the potential.

## Related methods in VASP
- [Metadynamics](../theory/Metadynamics.md): In contrast to the
  methods discussed on this page metadynamics continuously updates the
  bias potential of the system to push it into unvisited parts of phase
  space.

&nbsp;

- [Interface
  pinning](Category-Interface_pinning.md):
  This employs a bias potential to pin the state of an interface between
  a solid and a liquid. This method uses entirely different
  [INCAR](../input-files/INCAR.md) tags than the bias potentials presented
  on this page.

## References
1.  ↑ ^([a](#cite_ref-torrie:jcp:1977_1-0))
    ^([b](#cite_ref-torrie:jcp:1977_1-1))
    ^([c](#cite_ref-torrie:jcp:1977_1-2)) [G. M. Torrie and J. P.
    Valleau, J. Comp. Phys. **23**, 187
    (1977).](http://doi.org/10.1016/0021-9991(77)90121-8)
2.  [↑](#cite_ref-kaestner:jcp:2005_2-0) [J. Kästner, and W. Thiel,
    *Bridging the gap between thermodynamic integration and umbrella
    sampling provides a novel analysis method: “Umbrella
    integration”*, J. Chem. Phys. **123**, 144104
    (2005).](https://doi.org/10.1063/1.2052648)
3.  [↑](#cite_ref-frenkel:ap-book:2002_3-0) [D. Frenkel and B. Smit,
    *Understanding molecular simulations: from algorithms to
    applications*, Academic Press: San Diego,
    2002.](http://doi.org/10.1016/0021-9991(77)90121-8)
