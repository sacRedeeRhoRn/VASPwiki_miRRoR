<!-- Source: https://vasp.at/wiki/index.php/Machine_learning_force_field:_Theory | revid: 36061 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Machine learning force field: Theory


Here we present the theory for on-the-fly machine learning force fields.
The theory will be presented in a very condensed manner and for a more
detailed description of the methods, we refer the readers to Refs.
[^jinnouchi:prl:2019-1],
[^jinnouchi2:arx:2019-2]
and
[^jinnouchi:jcm:20-3].


## Contents


- [1
  Introduction](#introduction)
- [2
  Algorithms](#algorithms)
  - [2.1 On-the-fly
    machine-learning
    algorithm](#on-the-fly-machine-learning-algorithm)
  - [2.2 Sampling
    of training data and local reference
    configurations](#sampling-of-training-data-and-local-reference-configurations)
  - [2.3 Threshold
    for uncertainty of
    forces](#threshold-for-uncertainty-of-forces)
- [3 Local
  energies](#local-energies)
- [4
  Descriptors](#descriptors)
  - [4.1 Radial
    descriptor](#radial-descriptor)
  - [4.2 Angular
    descriptor](#angular-descriptor)
  - [4.3 Basis set
    expansion and
    descriptors](#basis-set-expansion-and-descriptors)
    - [4.3.1
      Angular
      filtering](#angular-filtering)
    - [4.3.2
      Reduced
      descriptors](#reduced-descriptors)
- [5 Potential
  energy fitting](#potential-energy-fitting)
  - [5.1
    Normalization](#normalization)
  - [5.2 Matrix
    vector form of linear
    equations](#matrix-vector-form-of-linear-equations)
- [6 Bayesian
  linear regression](#bayesian-linear-regression)
  - [6.1
    Regression](#regression)
    - [6.1.1
      Solution via
      Inversion](#solution-via-inversion)
    - [6.1.2
      Solution via LU
      factorization](#solution-via-lu-factorization)
    - [6.1.3
      Solution via regularized
      SVD](#solution-via-regularized-svd)
    - [6.1.4
      Evidence
      approximation](#evidence-approximation)
- [7 Uncertainty
  estimation](#uncertainty-estimation)
  - [7.1
    Uncertainty estimates from Bayesian linear
    regression](#uncertainty-estimates-from-bayesian-linear-regression)
  - [7.2 Spilling
    factor](#spilling-factor)
- [8
  Sparsification](#sparsification)
  - [8.1
    Sparsification of local reference
    configurations](#sparsification-of-local-reference-configurations)
  - [8.2
    Sparsification of angular
    descriptors](#sparsification-of-angular-descriptors)
- [9
  References](#references)


## Introduction\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Introduction">edit</a> \| (./index.php.md)\]

Molecular dynamics is one of the most important methods for the
determination of dynamic properties. The quality of the molecular
dynamics simulation depends very strongly on the accuracy of the
calculational method, but higher accuracy usually comes at the cost of
increased computational demand. A very accurate method is ab initio
molecular dynamics, where the interactions of atoms and electrons are
calculated fully quantum mechanically from ab initio calculations (such
as e.g. DFT). Unfortunately, this method is very often limited to small
simulation cells and simulation times. One way to hugely speed up these
calculations is by using force fields, which are parametrizations of the
potential energy. These parametrizations can range from very simple
functions with only empirical parameters, to very complex functions
parametrized using thousands of ab initio calculations. Usually making
accurate force fields manually is a very time-consuming task that needs
tremendous expertise and know-how.

Another way to greatly reduce computational cost and required human
intervention is by machine learning. Here, in the prediction of the
target property, the method automatically interpolates between known
training systems that were previously calculated ab initio. This way the
generation of force fields is already significantly simplified compared
to a classical force field which needs manual (or even empirical)
adjustment of the parameters. Nevertheless, there is still the problem
of how to choose the proper (minimal) training data. One very efficient
and automatic way to solve that is to adapt on-the-fly learning. Here an
MD calculation is used for the learning. During the run of the MD
calculation, ab initio data is picked out and added to the training
data. From the existing data, a force field is continuously built up. At
each step, it is judged whether to make an ab initio calculation and
possibly add the data to the force field or to use the force field for
that step and actually skip learning for that step. Hence the name "on
the fly" learning. The crucial point here is the probability model for
the estimation of uncertainties. This model is built up from newly
sampled data. Hence, the more accurate the force field gets the less
sampling is needed and the more expensive ab initio steps are skipped.
This way not only the convergence of the force field can be controlled
but also a very widespread scan through phase space for the training
structures can be performed. The crucial point for on-the-fly machine
learning which will be explained with the rest of the methodology in the
following subsections is to be able to predict uncertainties of the
force field on a newly sampled structure without the necessity to
perform an ab initio calculation on that structure.

## Algorithms\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Algorithms">edit</a> \| (./index.php.md)\]

### On-the-fly machine-learning algorithm\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: On-the-fly machine-learning algorithm">edit</a> \| (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:MLFF_main_algorithm.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/a/a0/MLFF_main_algorithm.png/300px-MLFF_main_algorithm.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/a/a0/MLFF_main_algorithm.png/450px-MLFF_main_algorithm.png 1.5x, /wiki/images/thumb/a/a0/MLFF_main_algorithm.png/600px-MLFF_main_algorithm.png 2x"
width="300" height="431" /></a>
<figcaption>Fig. 1: On-the-fly machine learning force field generation
scheme.</figcaption>
</figure>

To obtain the machine-learning force field several **structure
datasets** are required. A structure dataset defines the Bravais lattice
and the atomic positions of the system and contains the total energy,
the forces, and the stress tensor calculated by first principles. Given
these structure datasets, the machine identifies **local
configurations** around an atom to learn what force field is
appropriate. The local configuration measures the radial and angular
distribution of neighboring atoms around this given site and is captured
in the so-called [**descriptors**](#descriptors).

The on-the-fly force field generation scheme is given by the following
steps (a flowchart of the algorithm is shown in Fig. 1):

1.  The machine predicts the energy, the forces, and the stress tensor
    and their uncertainties for a given structure using the existing
    force field.
2.  The machine decides whether to perform a first-principles
    calculation (proceed with step 3); otherwise we skip to step 5.
3.  Performing the first principles calculation, we obtain a new
    structure dataset that may improve the force field.
4.  If the number of newly collected structures reaches a certain
    threshold or if the predicted uncertainty becomes too large, the
    machine learns an improved force field by including the new
    structure datasets and local configurations.
5.  Atomic positions and velocities are updated by using the force field
    (if accurate enough) or the first principles calculation.
6.  If the desired total number of ionic steps ([NSW](../incar-tags/NSW.md))
    is reached we are done; otherwise proceed with step 1.

### Sampling of training data and local reference configurations\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Sampling of training data and local reference configurations">edit</a> \| (./index.php.md)\]

We employ a learning scheme where structures are only added to the list
of training structures when local reference configurations are picked
for atoms that have an uncertainty in the force higher than a given
threshold. So in the following, it is implied that whenever a new
training structure is obtained, also local reference configurations from
this structure are obtained.

Usually one can employ that the force field doesn't necessarily need to
be retrained immediately at every step when a training structure with
corresponding local configurations is added. Instead, one can also
collect candidates and do the learning in a later step for all
structures simultaneously (blocking). This way saving significant
computational costs. Of course learning after every new configuration or
after every block can have different results, but with not too large
block sizes the difference should be small. The tag
[ML_MCONF_NEW](../incar-tags/ML_MCONF_NEW.md) sets the block size
for learning. The force field is usually not updated at every
molecular-dynamics step. The update happens under the following
conditions:

- If there is no force field present, all atoms of a structure are
  sampled as local reference configurations and a force field is
  constructed.
- If the Bayesian uncertainty of the force for any atom is above the
  strict threshold set by
  [ML_CDOUB](../incar-tags/ML_CDOUB.md)$\times$[ML_CTIFOR](../incar-tags/ML_CTIFOR.md), the local
  reference configurations are sampled and a new force field is
  constructed.
- If the Bayesian uncertainty of the force for any atom is above the
  threshold [ML_CTIFOR](../incar-tags/ML_CTIFOR.md) but below
  [ML_CDOUB](../incar-tags/ML_CDOUB.md)$\times$[ML_CTIFOR](../incar-tags/ML_CTIFOR.md), the
  structure is added to the list of new training structure candidates.
  Whenever the number of candidates is equal to
  [ML_MCONF_NEW](../incar-tags/ML_MCONF_NEW.md) they are added to
  the entire set of training structures and the force field is updated.
  To avoid sampling too similar structures, the next step, from which
  training structures are allowed to be taken as candidates, is set by
  [ML_NMDINT](../incar-tags/ML_NMDINT.md). All ab initio calculations
  within this distance are skipped if the Bayesian uncertainty for the
  force on all atoms is below
  [ML_CDOUB](../incar-tags/ML_CDOUB.md)$\times$[ML_CTIFOR](../incar-tags/ML_CTIFOR.md).

### Threshold for uncertainty of forces\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Threshold for uncertainty of forces">edit</a> \| (./index.php.md)\]

Training structures and their corresponding local configurations are
only chosen if the uncertainty in the forces of any atom exceeds a
chosen threshold. The initial threshold is set to the value provided by
[ML_CTIFOR](../incar-tags/ML_CTIFOR.md) (the unit is eV/Angstrom). The
behavior of how the threshold is further controlled is given by
[ML_ICRITERIA](../incar-tags/ML_ICRITERIA.md). The following options
are available:

- [ML_ICRITERIA](../incar-tags/ML_ICRITERIA.md) = 0: No update of
  initial value of [ML_CTIFOR](../incar-tags/ML_CTIFOR.md) is done.
- [ML_ICRITERIA](../incar-tags/ML_ICRITERIA.md) = 1: Update of
  criteria using an average of the Bayesian uncertainties of the forces
  from history (see description of the method below).
- [ML_ICRITERIA](../incar-tags/ML_ICRITERIA.md) = 2: Update of
  criteria using gliding average of Bayesian uncertainties (probably
  more robust but **not well tested**).

Generally, it is recommended to automatically update the threshold
[ML_CTIFOR](../incar-tags/ML_CTIFOR.md) during machine learning.
Details on how and when the update is performed are controlled by
[ML_CSLOPE](../incar-tags/ML_CSLOPE.md),
[ML_CSIG](../incar-tags/ML_CSIG.md) and
[ML_MHIS](../incar-tags/ML_MHIS.md).

Description of [ML_ICRITERIA](../incar-tags/ML_ICRITERIA.md)=1:

[ML_CTIFOR](../incar-tags/ML_CTIFOR.md) is updated using the average
Bayesian uncertainty in the previous steps. Specifically, it is set to

[ML_CTIFOR](../incar-tags/ML_CTIFOR.md) = (average of the stored
Bayesian uncertainties) \*(1.0 + [ML_CX](../incar-tags/ML_CX.md)).

The number of entries in the history of the Bayesian uncertainties is
controlled by [ML_MHIS](../incar-tags/ML_MHIS.md). To avoid noisy data or
an abrupt jump of the Bayesian uncertainty causing issues, the standard
error of the history must be below the threshold
[ML_CSIG](../incar-tags/ML_CSIG.md), for the update to take place.
Furthermore, the slope of the stored data must be below the threshold
[ML_CSLOPE](../incar-tags/ML_CSLOPE.md). In practice, the slope and the
standard errors are at least to some extent correlated: often the
standard error is proportional to [ML_MHIS](../incar-tags/ML_MHIS.md)/3
times the slope or somewhat larger. We recommend to vary only
[ML_CSIG](../incar-tags/ML_CSIG.md) and keep
[ML_CSLOPE](../incar-tags/ML_CSLOPE.md) fixed to its default value.

## Local energies\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Local energies">edit</a> \| (./index.php.md)\]

The potential energy $U$ of a
structure with $N_{a}$ atoms
is approximated as

$U
= \sum\limits_{i=1}^{N_{\mathrm{a}}} U_{i}.$

The local energies $U_{i}$ are
functionals $U_{i}=F\[\rho_{i}(\mathbf{r})\]$ of the probability
density $\rho_{i}$ to
find another atom $j$ at the
position $\mathbf{r}$
around the atom $i$ within a
cut-off radius $R_{\mathrm{cut}}$ defined as

$\rho_{i}\left(\mathbf{r}\right) = \sum\limits_{j=1}^{N_{\mathrm{a}}}
f_{\mathrm{cut}}\left(r_{ij}\right)
g\left(\mathbf{r}-\mathbf{r}_{ij}\right), \qquad \qquad \qquad \qquad
r_{ij}=|\mathbf{r}_{ij}|=|\mathbf{r}_{j}-\mathbf{r}_{i}|.$

Here $f_{\mathrm{cut}}$ is a cut-off function that goes to zero for
$r_{ij}>R_{\mathrm{cut}}$ and
$g\left(\mathbf{r}-\mathbf{r}_{ij}\right)$ is a delta
function.

The atom distribution can also be written as a sum of individual
distributions:

$\rho_{i}\left(\mathbf{r}\right) = \sum\limits_{j \ne
i}^{N_{\mathrm{a}}} \rho_{ij}\left(\mathbf{r}\right).$

Here $\rho_{ij}\left(\mathbf{r}\right)$ describes the
probability of find an atom $j$ at a
position $\mathbf{r}$
with respect to atom $i$.

## Descriptors\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Descriptors">edit</a> \| (./index.php.md)\]

Similar to the Smooth Overlap of Atomic
Positions[^bartok:prb:2013-4]
(SOAP) method the delta function $g(\mathbf{r})$ is approximated as

$g\left(\mathbf{r}\right)=\frac{1}{\sigma_{\mathrm{atom}}\sqrt{2\pi}}\mathrm{exp}\left(-\frac{|\mathbf{r}|^{2}}{2\sigma_{\mathrm{atom}}^{2}}\right).$

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:MLFF_rad_and_ang_descriptor.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/b/b5/MLFF_rad_and_ang_descriptor.png/300px-MLFF_rad_and_ang_descriptor.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/b/b5/MLFF_rad_and_ang_descriptor.png/450px-MLFF_rad_and_ang_descriptor.png 1.5x, /wiki/images/thumb/b/b5/MLFF_rad_and_ang_descriptor.png/600px-MLFF_rad_and_ang_descriptor.png 2x"
width="300" height="133" /></a>
<figcaption>Fig. 2: Radial and angular descriptors.</figcaption>
</figure>

  
Unfortunately $\rho_{i}\left(\mathbf{r}\right)$ is not rotationally
invariant. To deal with this problem intermediate functions or
*descriptors* depending on $\rho_{i}\left(\mathbf{r}\right)$ possessing rotational
invariance are introduced:

### Radial descriptor\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Radial descriptor">edit</a> \| (./index.php.md)\]

This is the simplest descriptor which relies on the radial distribution
function

$\rho_{i}^{(2)}\left(r\right) = \frac{1}{4\pi} \int
\rho_{i}\left(r\hat{\mathbf{r}}\right) d\hat{\mathbf{r}},$

where $\hat{\mathbf{r}}$ denotes the unit vector of the vector
$\mathbf{r}$ between atoms $i$ and
$j$ \[see Fig. 2 (a)\]. The Radial descriptor can also be
regarded as a two-body descriptor.

### Angular descriptor\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Angular descriptor">edit</a> \| (./index.php.md)\]

In most cases the radial descriptor is not enough to distinguish
different probability densities $\rho_{i}$,
since two different $\rho_{i}$
can yield the same $\rho_{i}^{(2)}$. To improve on this angular information between two
radial descriptors is also incorporated within an angular descriptor

$\rho_{i}^{(3)}\left(r,s,\theta\right) = \iint d\hat{\mathbf{r}}
d\hat{\mathbf{s}} \delta\left(\hat{\mathbf{r}}\cdot\hat{\mathbf{s}} -
\mathrm{cos}\theta\right) \sum\limits_{j=1}^{N_{a}} \sum\limits_{k
\ne j}^{N_{a}} \rho_{ik} \left(r\hat{\mathbf{r}}\right) \rho_{ij}
\left(s\hat{\mathbf{s}}\right)$

where $\theta$
denotes the angle between two vectors $\mathbf{r}_{ij}$ and $\mathbf{r}_{ik}$ \[see Fig. 2 (b)\]. The important difference of the
function $\rho_{i}^{(3)}$ compared to the angular distribution function (also
called power spectrum within the Gaussian Approximation Potential) used
in reference
[^bartok:prl:2010-5]
is that no self interaction is included, where
$j$ and $k$ have the
same distance from $i$ and the
angle between the two is zero. It can be shown
[^jinnouchi:jcm:20-3]
that the self-interaction component is equivalent to the two body
descriptors. This means that our angular descriptor is a pure angular
descriptor, containing no two-body components and it cannot be expressed
as linear combinations of the power spectrum. The advantage of this
descriptor is that it enables us to separately control the effects of
two- and three-body descriptors.

### Basis set expansion and descriptors\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Basis set expansion and descriptors">edit</a> \| (./index.php.md)\]

The atomic probability density can be also expanded in terms of basis
functions

$\rho_{i} \left( \mathbf{r} \right) =
\sum\limits_{l=1}^{L_{\mathrm{max}}} \sum\limits_{m=-l}^{l}
\sum\limits_{n=1}^{N^{l}_{ \mathrm{R}}} c_{nlm}^{i}\chi_{nl} \left(
r \right) Y_{lm} \left( \hat{\mathbf{r}} \right),$

where $c_{nlm}^{i}$, $\chi_{nl}$
and $Y_{lm}$
denote expansion coefficients, radial basis functions and spherical
harmonics, respectively. The indices $n$,
$l$ and $m$ denote
radial numbers, angular and magnetic quantum numbers, respectively.

By using the above equation the radial descriptor and angular descriptor
can be written as

$\rho_{i}^{(2)}\left(r\right) = \frac{1}{\sqrt{4\pi}}
\sum\limits_{n=1}^{N^{0}_{\mathrm{R}}} c_{n00}^{i}
\chi_{n0}\left(r\right),$

and

$\rho_{i}^{(3)}\left(r,s,\theta\right) =
\sum\limits_{l=1}^{L_{\mathrm{max}}}
\sum\limits_{n=1}^{N^{l}_{\mathrm{R}}}\sum\limits_{\nu=1}^{N^{l}_{\mathrm{R}}}
\sqrt{\frac{2l+1}{2}} p_{n\nu l}^{i}\chi_{nl}\left(r\right)\chi_{\nu
l}\left(s\right)P_{l}\left(\mathrm{cos}\theta\right),$

where $\chi_{\nu l}$ and $P_{l}$
represent normalized spherical Bessel functions and Legendre polynomials
of order $l$,
respectively.

The expansion coefficients for the angular descriptor can be converted
to

$p_{n\nu l}^{i}=\sqrt{\frac{8\pi^{2}}{2l+1}} \sum\limits_{m=-l}^{l}
\left\[ c_{nlm}^{i} c_{\nu lm}^{i\*} - \sum\limits_{j}^{N_{a}}
c_{nlm}^{ij} c_{\nu lm}^{ij\*}\right\] ,$

where $c_{nlm}^{ij}$ denotes expansion coefficients of the distribution
$\rho_{ij}(\mathbf{r})$ with respect to
$\chi_{\nu l}$ and $P_{l}$

$\rho_{ij}(\mathbf{r}) = \sum\limits_{l=1}^{L_{\mathrm{max}}}
\sum\limits_{m=-l}^{l} \sum\limits_{n=1}^{N^{l}_{ \mathrm{R}}}
c_{nlm}^{ij}\chi_{nl} \left( r \right) Y_{lm} \left( \hat{\mathbf{r}}
\right)$

and

$c_{nlm}^{i} = \sum\limits_{j}^{N_{a}} c_{nlm}^{ij}.$

#### Angular filtering\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Angular filtering">edit</a> \| (./index.php.md)\]

In many cases $\chi_{nl}$
is multiplied with an angular filtering
function[^boyd:book:2000-6]
$\eta$ ([ML_IAFILT2](../incar-tags/ML_IAFILT2.md)),
which can noticably reduce the necessary basis set size without losing
accuracy in the calculations

$\eta_{l,a_{\mathrm{FILT}}}=\frac{1}{1+a_{\mathrm{FILT}} \[l
(l+1)\]^{2}}$

where $a_{\mathrm{FILT}}$ ([ML_AFILT2](../incar-tags/ML_AFILT2.md)) is a
parameter controlling the extent of the filtering. A larger value for
the parameter should provide more filtering.

#### Reduced descriptors\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Reduced descriptors">edit</a> \| (./index.php.md)\]

A descriptor that reduces the number of descriptors with respect to the
number of
elements[^csanyi:npj:2022-7]
is written as

$p_{n\nu l}^{iJ}=\sqrt{\frac{8\pi^{2}}{2l+1}} \sum\limits_{m=-l}^{l}
c_{nlm}^{iJ} \sum\limits_{J'}c_{\nu lm}^{iJ'}.$

For more details on the effects of this descriptor please see following
site: [ML_DESC_TYPE](../incar-tags/ML_DESC_TYPE.md).

## Potential energy fitting\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Potential energy fitting">edit</a> \| (./index.php.md)\]

It is convenient to express the local potential energy of atom
$i$ in structure $\alpha$ in
terms of linear coefficients $w_{i_\mathrm{B}}$ and a kernel $K
\left(\mathbf{X}_{i},\mathbf{X}_{i_\mathrm{B}} \right)$ as follows

$U_{i}^{\alpha} = \sum\limits_{i_\mathrm{B}=1}^{N_\mathrm{B}}
w_{i_\mathrm{B}} K \left(
\mathbf{X}_{i}^{\alpha},\mathbf{X}_{i_\mathrm{B}} \right)$

where $N_\mathrm{B}$ is the basis set size. The kernel
$K
\left( \mathbf{X}_{i},\mathbf{X}_{i_\mathrm{B}}\right)$ measures the similarity between a *local*
configuration from the training set $\rho_{i}(\mathbf{r})$ and basis set $\rho_{i_\mathrm{B}}(\mathbf{r})$. Using the radial
and angular descriptors it is written as

$K
\left(\mathbf{\hat{X}}_{i},\mathbf{\hat{X}}_{i_\mathrm{B}}\right) =
\left\[ \beta \mathbf{\hat{X}}_{i}^{(2)} \cdot
\mathbf{\hat{X}}_{i_{\mathrm{B}}}^{(2)} + (1-\beta)
\mathbf{\hat{X}}_{i}^{(3)} \cdot
\mathbf{\hat{X}}_{i_{\mathrm{B}}}^{(3)} \right\]^{\zeta}.$

Here the vectors $\mathbf{\hat{X}}_{i}^{(2)}$ and $\mathbf{\hat{X}}_{i}^{(3)}$ contain all coefficients $c_{n00}^{i}$
and $p_{n\nu l}^{i}$, respectively. The notation
$\mathbf{\hat{X}}$ indicates that it is a normalized
vector. The parameter $\beta$
([ML_W1](../incar-tags/ML_W1.md)) controls the weighting of the radial and
angular terms, respectively. The parameter $\zeta$
([ML_NHYP](../incar-tags/ML_NHYP.md)) controls the sharpness of the
kernel and the order of the many-body interactions.

### Normalization\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Normalization">edit</a> \| (./index.php.md)\]

The two and three body descriptors are combined to form a feature
concatenated vector

$\mathbf{X}_{\mathrm{c}} = \begin{bmatrix} \sqrt{\beta} \mathbf{X}^{(2)}
\\ \sqrt{(1-\beta)} \mathbf{X}^{(3)} \end{bmatrix}.$

$||\mathbf{X}_{\mathrm{c}}||$ is used in the
normalization of $\mathbf{X}^{(2)}$ and $\mathbf{X}^{(3)}$.

### Matrix vector form of linear equations\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: Matrix vector form of linear equations">edit</a> \| (./index.php.md)\]

Similarly to the energy $U_{i}^{\alpha}$the forces and the stress tensor are also described as
linear functions of the coefficients $w_{i_\mathrm{B}}$. All three are fitted simultaneously which leads to
the following matrix-vector form

$\mathbf{Y} = \mathbf{\Phi} \mathbf{w}$

where $\mathbf{Y}$
is a super vector consisting of the sub vectors
$\\\mathbf{y}^{\alpha}|\alpha=1,...,N_{\mathrm{st}}\\$. Here each $\mathbf{y}^{\alpha}$ contains the first principle energies per atom, forces
and stress tensors for each structure $\alpha$.
$N_\mathrm{st}$ denotes the total number of structures.
The size of $\mathbf{Y}$
is $N_{\mathrm{st}} \times (1+3N^{\alpha}_{a}+6)$.

The matrix $\mathbf{\Phi}$ is also called as *design*
matrix[^bishop:book:2006-8].
The rows of this matrix are blocked for each structure
$\alpha$, where the first line of each block consists of
the kernel used to calculate the energy. The subsequent
$3
N^{\alpha}_{a}$ lines consist of the derivatives of
the kernel with respect to the atomic coordinates used to calculate the
forces. The final 6 lines within each structure consist of the
derivatives of the kernel with respect to the unit cell coordinates used
to calculate the stress tensor components. The overall size of
$\mathbf{Y}$ is $N_{\mathrm{st}} \times (1+3
N^{\alpha}_{a}+6)\times N_\mathrm{B}$ looking like as
follows

$\mathbf{\Phi} = \begin{bmatrix} \sum_{i}
\frac{1}{N^{\alpha=1}_{\mathrm{a}}}K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \frac{1}{N^{\alpha=1}_{\mathrm{a}}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots \\ \sum_{i} \nabla_{x_{1}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \nabla_{x_{1}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots\\ \sum_{i} \nabla_{y_{1}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \nabla_{y_{1}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots\\ \sum_{i} \nabla_{z_{1}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \nabla_{z_{1}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots\\ \sum_{i} \nabla_{x_{2}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \nabla_{x_{2}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots\\ \sum_{i} \nabla_{y_{2}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \nabla_{y_{2}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots\\ \sum_{i} \nabla_{z_{2}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \nabla_{z_{2}}
K\left(\mathbf{X}^{\alpha=1}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots\\ \ldots &\ldots &\dots &\dots &\dots\\ \ldots
&\ldots &\dots &\dots &\dots\\ \ldots &\ldots &\dots &\dots &\dots\\
\sum_{i}
\frac{1}{N^{\alpha=2}_{\mathrm{a}}}K\left(\mathbf{X}^{\alpha=2}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \frac{1}{N^{\alpha=2}_{\mathrm{a}}}
K\left(\mathbf{X}^{\alpha=2}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots \\ \sum_{i} \nabla_{x_{1}}
K\left(\mathbf{X}^{\alpha=2}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \nabla_{x_{1}}
K\left(\mathbf{X}^{\alpha=2}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots\\ \sum_{i} \nabla_{y_{1}}
K\left(\mathbf{X}^{\alpha=2}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \nabla_{y_{1}}
K\left(\mathbf{X}^{\alpha=2}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots\\ \sum_{i} \nabla_{z_{1}}
K\left(\mathbf{X}^{\alpha=2}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \nabla_{z_{1}}
K\left(\mathbf{X}^{\alpha=2}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots\\ \sum_{i} \nabla_{x_{2}}
K\left(\mathbf{X}^{\alpha=2}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \nabla_{x_{2}}
K\left(\mathbf{X}^{\alpha=2}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots\\ \sum_{i} \nabla_{y_{2}}
K\left(\mathbf{X}^{\alpha=2}_{i},\mathbf{X}_{i_{\mathrm{B}}=1}\right)
&\sum_{i} \nabla_{y_{2}}
K\left(\mathbf{X}^{\alpha=2}_{i},\mathbf{X}_{i_{\mathrm{B}}=2}\right)
&\dots &\dots &\dots\\ \sum_{i} \nabla_{z_{2}} K\left(\dots\right)
&\sum_{i} \nabla_{z_{2}} K\left(\dots\right) &\dots &\dots &\dots\\
\ldots &\ldots &\dots &\dots &\dots\end{bmatrix}.$

## Bayesian linear regression\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: Bayesian linear regression">edit</a> \| (./index.php.md)\]

Ultimately for uncertainty prediction we want to get the maximized
probability of observing a new structure $\mathbf{y}$
on basis of the training set $\mathbf{Y}$,
which is denoted as $p \left( \mathbf{y} |
\mathbf{Y} \right)$. For this we need to get from the
error of the linear fitting coefficients $\mathbf{w}$
in the reproduction of the training data $p\left( \mathbf{w} |
\mathbf{Y} \right)$ to $p \left( \mathbf{y} |
\mathbf{Y} \right)$ which is explained in the
following.

First we obtain $p\left( \mathbf{w} |
\mathbf{Y} \right)$ from the Bayesian theorem

$p\left( \mathbf{w} | \mathbf{Y} \right) = \frac{p\left( \mathbf{Y} |
\mathbf{w} \right) p\left( \mathbf{w} \right)}{p\left( \mathbf{Y}
\right)}$,

where we assume multivariate Gaussian distributions
$\mathcal{N}$ for the likelihood function

$p\left( \mathbf{Y} | \mathbf{w} \right) = \mathcal{N}
\left(\mathbf{Y}| \mathbf{\Phi} \mathbf{w},
\sigma_{\mathrm{v}}^{2}\mathbf{I} \right)$

and the (conjugate) prior

$p\left( \mathbf{w} \right) = \mathcal{N} \left(\mathbf{w}|
\mathbf{0},\sigma_{\mathrm{w}}^{2}\mathbf{I} \right).$

The parameters $\sigma_{\mathrm{w}}^{2}$ and $\sigma_{\mathrm{v}}^{2}$ need to be optimized to balance the accuracy and
robustness of the force field (see below). The normalization is obtained
by

$p\left( \mathbf{Y} \right) = \int p\left( \mathbf{Y} | \mathbf{w}
\right) p\left( \mathbf{w} \right) d\mathbf{w}.$

Using the equations from above and the completing square
method[^bishop:book:2006-8]
$p\left( \mathbf{w} | \mathbf{Y} \right)$ is obtained
as follows

$p\left( \mathbf{w} | \mathbf{Y} \right) = \mathcal{N}
\left(\mathbf{w}| \mathbf{\bar w},\mathbf{\Sigma} \right).$

Since the prior and the likelood function are described by multivariate
Gaussian distributions the posterior $\mathcal{N} \left(\mathbf{w}|
\mathbf{\bar w},\mathbf{\Sigma} \right)$ describes a
multivariate Gaussian written as

$\mathcal{N} \left(\mathbf{w}| \mathbf{\bar w},\mathbf{\Sigma} \right) =
\frac{1}{\sqrt{ \left( 2 \pi \right)^{N_{\mathrm{B}}}
\mathrm{det}\mathbf{\Sigma} }} \mathrm{exp} \left\[ -\frac{ \left(
\mathbf{w} - \mathbf{\bar w} \right)^{\mathrm{T}} \mathbf{\Sigma}^{-1}
\left( \mathbf{w} - \mathbf{ \bar w} \right)}{2} \right\]$

where we use the following definitions for the center of the Guassian
distribution $\mathbf{\bar w}$ and the covariance matrix $\mathbf{\Sigma}$

$\mathbf{\bar w} = s_{\mathrm{v}} \mathbf{\Sigma}
\mathbf{\Phi}^{\mathrm{T}} \mathbf{Y},$

$\mathbf{\Sigma}^{-1} =s_{\mathrm{w}} \mathbf{I} + s_{\mathrm{v}}
\mathbf{\Phi}^{\mathrm{T}}\mathbf{\Phi}.$

Here we have used the following definitions

$s_{\mathrm{v}} = \frac{1}{\sigma_{\mathrm{v}}^{2}}$

and

$s_{\mathrm{w}} = \frac{1}{\sigma_{\mathrm{w}}^{2}}.$

### Regression\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: Regression">edit</a> \| (./index.php.md)\]

We want to obtain the weights $\mathbf{\bar w}$ for the linear equations

$\mathbf{Y} = \mathbf{\Phi} \mathbf{\bar w}.$

  

#### Solution via Inversion\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: Solution via Inversion">edit</a> \| (./index.php.md)\]

By using directly the covariance matrix $\mathbf{\Sigma}$ the equation from above

$\mathbf{\bar w} = s_{\mathrm{v}} \mathbf{\Sigma}
\mathbf{\Phi}^{\mathrm{T}} \mathbf{Y},$

can be solved straightforwardly. However, only
$\mathbf{\Sigma}^{-1}$ is directly accesible and
$\mathbf{\Sigma}$ must be obtained from
$\mathbf{\Sigma}^{-1}$ via inversion. This inversion is
numerically unstable and leads to lower accuracy. **Hence we don't use
this method.**

  

#### Solution via LU factorization\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=19"
class="mw-editsection-visualeditor"
title="Edit section: Solution via LU factorization">edit</a> \| (./index.php.md)\]

Here we directly use the invers of the covariance matrix
$\mathbf{\Sigma}^{-1}$ by solving the following equation
for the weights $\mathbf{\bar w}$

$\mathbf{\Sigma}^{-1} \mathbf{\bar w} = s_{\mathrm{v}}
\mathbf{\Phi}^{\mathrm{T}} \mathbf{Y}.$

For that $\mathbf{\Sigma}^{-1}$ is decomposed into it's LU factorized components
$\mathbf{P} \* \mathbf{L} \* \mathbf{U}$. After that the
$\mathbf{L} \* \mathbf{U}$ factors are used to solve the
previous linear equation for the weights $\mathbf{\bar w}$. This method is noticeably more accurate than the
method via inversion of $\mathbf{\Sigma}^{-1}$ while being on the same order of magnitude in terms of
computational cost. **Hence it is the method used in on-the-fly
learning.**

  

#### Solution via regularized SVD\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=20"
class="mw-editsection-visualeditor"
title="Edit section: Solution via regularized SVD">edit</a> \| (./index.php.md)\]

The regression problem can also be solved by using the singular value
decomposition to factorize $\mathbf{\Phi}$ as

$\mathbf{\Phi}=\mathbf{U}\mathbf{\Lambda}\mathbf{V}^{T}.$

To add the regularization the diagonal matrix
$\mathbf{\Lambda}$ containing the singular values is
rewritten as

$\tilde{\mathbf{\Lambda}}=\mathbf{\Lambda}+\frac{s_{\mathrm{w}}}{s_{\mathrm{v}}}\mathbf{\Lambda}^{-1}.$

By using the orthogonality of the left and right eigenvector matrices
$\mathbf{U}^{T}\mathbf{U}=\mathbf{I}_{n}$ and
$\mathbf{V}\mathbf{V}^{T}=\mathbf{I}_{n}$ the
regression problem has the following solution

$\tilde{\mathbf{w}} =
\mathbf{V}\tilde{\mathbf{\Lambda}}^{-1}\mathbf{U}^{T}\mathbf{Y}.$

  

#### Evidence approximation\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=21"
class="mw-editsection-visualeditor"
title="Edit section: Evidence approximation">edit</a> \| (./index.php.md)\]

Finally to get the best results and to prevent overfitting the
parameters $s_{\mathrm{v}}$ and $s_{\mathrm{w}}$ have to be optimized. To achieve this, we use the
evidence
approximation[^gull:book:1989-9][^mackay:neu:2012-10][^jinnouchi:pcl:2017-11]
(also called as empirical bayes, 2 maximum likelihood or generalized
maximum likelihood), which maximizes the evidence function (also called
model evidence) defined as

$p\left(\mathbf{Y}|s_{\mathrm{v}}^{-1},s_{\mathrm{w}}^{-1}\right)
=\left(\frac{1}{\sqrt{2\pi s_{\mathrm{v}}^{-1}}}\right)^{M}
\left(\frac{1}{\sqrt{2\pi
s_{\mathrm{w}}^{-1}}}\right)^{N_{\mathrm{B}}} \int
\mathrm{exp}\left\[-E\left( \mathbf{w} \right) \right\] d\mathbf{w},$

$E\left( \mathbf{w} \right) = \frac{s_{\mathrm{v}}}{2} ||
\mathbf{\Phi}\mathbf{w}-\mathbf{Y}||^{2} + \frac{s_{\mathrm{w}}}{
2}||\mathbf{w}||^{2}.$

The function $p\left(\mathbf{Y}|s_{\mathrm{v}}^{-1},s_{\mathrm{w}}^{-1}\right)$ corresponds to the probability that the regression
model with parameters $s_{\mathrm{v}}$ and $s_{\mathrm{w}}$ provides the reference data
$\mathbf{Y}$. Hence the best fit is optimized by
maximizing this probability. The maximization is carried out by
simultaneously solving the following equations

$s_{\mathrm{w}}=\frac{\gamma}{|\mathbf{\bar{w}}|^{2}},$

$s_{\mathrm{v}}=\frac{M-\gamma}{|\mathbf{T}-\mathbf{\phi}\mathbf{\bar{w}}|^{2}},$

$\gamma=\sum\limits_{k=1}^{N_{\mathrm{B}}}
\frac{\lambda_{k}}{\lambda_{k}+s_{\mathrm{w}}}$

where $\lambda_{k}$
are the eigenvalues of the matrix $s_{\mathrm{v}}\mathbf{\Phi}^{\mathrm{T}}\mathbf{\Phi}$.

The evidence approximation can be done for any of the above-described
regression methods, but we combine it only with the solutions from LU
factorization since solutions via SVD are calculationally too expensive
to be carried out multiple times.

## Uncertainty estimation\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=22"
class="mw-editsection-visualeditor"
title="Edit section: Uncertainty estimation">edit</a> \| (./index.php.md)\]

### Uncertainty estimates from Bayesian linear regression\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=23"
class="mw-editsection-visualeditor"
title="Edit section: Uncertainty estimates from Bayesian linear regression">edit</a> \| (./index.php.md)\]

By using the relation

$p
\left( \mathbf{y} | \mathbf{Y} \right) = \int p \left( \mathbf{y} |
\mathbf{w} \right) p \left( \mathbf{w} | \mathbf{Y} \right) d\mathbf{w}$

and the completing square
method[^bishop:book:2006-8]
the distribution of $p \left( \mathbf{y} |
\mathbf{Y} \right)$ is written as

$p
\left( \mathbf{y} | \mathbf{Y} \right) = \mathcal{N} \left(
\mathbf{\phi}\mathbf{\bar w}, \mathbf{\sigma} \right),$

$\mathbf{\sigma}=\frac{1}{s_{\mathrm{v}}}\mathbf{I}+\mathbf{\phi}^{\mathrm{T}}\mathbf{\Sigma}\mathbf{\phi}.$

Here $\mathbf{\phi}$ is similar to $\mathbf{\Phi}$ but only for the new structure
$\mathbf{y}$.

The mean vector $\mathbf{\phi}\mathbf{\bar w}$ contains the predicted results on the dimensionless
total energy, forces, and stress tensor. The diagonal elements of
$\mathbf{\sigma}$ correspond to the variances in the
predicted results. These variances are a measure of the uncertainty of
the predicted (dimensionless) total energies, forces, and stress
tensors. VASP outputs the square root of these variances, i.e. the
standard deviations of the predicted means, to the
[ML_LOGFILE](../output-files/ML_LOGFILE.md) ("`grep BEEF ML_LOGFILE`").
The output is scaled to the appropriate units (eV/atom and eV/A). During
on-the-fly training, a first-principles calculation is performed if the
standard deviations are above a certain threshold.

Please note that the uncertainty estimate can only account for epistemic
uncertainty, which arises from a lack of knowledge or data. Systematic
errors caused by the model's approximation can not be measured or
determined from the Bayesian uncertainty. In kernel-based methods, model
errors usually dominate the total error after few hundred training
steps; thus the predicted uncertainty is usually significantly smaller
than the true error. This does not indicate any deficiency in the
Bayesian regression!

### Spilling factor\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=24"
class="mw-editsection-visualeditor"
title="Edit section: Spilling factor">edit</a> \| (./index.php.md)\]

The spilling
factor[^jinnouchi2:arx:2019-2][^miwa:prb:2016-12]
$s_{i}$ is a measure of the overlap (or similarity) of
a given structural environment on an atom $\mathbf{X}_{i}$ with the local reference configurations
$\mathbf{X}_{i_{\mathrm{B}}}$ written as

$s_{i}= 1 - \frac{ \sum\limits_{i_{\mathrm{B}}=1}^{N_{\mathrm{B}}}
\sum\limits_{i'_{\mathrm{B}}=1}^{N_{\mathrm{B}}}
K(\mathbf{X}_{i},\mathbf{X}_{i_{\mathrm{B}}})
K^{-1}(\mathbf{X}_{i_{\mathrm{B}}}, \mathbf{X}_{i'_{\mathrm{B}}})
K(\mathbf{X}_{i'_{\mathrm{B}}},\mathbf{X}_{i}) } {
K(\mathbf{X}_{i},\mathbf{X}_{i}) }.$

If $\mathbf{X}_{i}$ is fully overlapping with any of the
local reference configurations then the second term on the right hand
side of the above equation becomes 1 and $s = 0$. If
$\mathbf{X}_{i}$ has no similarities with any of the
local reference configurations the second term on the right hand side of
the above equations becomes 0 and $s = 1$.

## Sparsification\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=25"
class="mw-editsection-visualeditor"
title="Edit section: Sparsification">edit</a> \| (./index.php.md)\]

Within the machine learning force field methods the sparsification of
local reference configurations and the angular descriptors is supported.
The sparsification of local reference configurations is by default used
and the extent is mainly controlled by
[ML_EPS_LOW](../incar-tags/ML_EPS_LOW.md). This is procedure is
important to avoid overcompleteness and to dampen the acquisition of new
configurations in special cases. The sparsification of angular
descriptors is by default not used and should be used very cautiously
and only if it's necessary. The description of the usage of this feature
is given in [ML_LSPARSDES](../incar-tags/ML_LSPARSDES.md).

### Sparsification of local reference configurations\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=26"
class="mw-editsection-visualeditor"
title="Edit section: Sparsification of local reference configurations">edit</a> \| (./index.php.md)\]

We start by defining the similarity kernel (or Gram matrix) for the
local configurations with each other

$\mathbf{K}_{i_{B},j_{B}}=\mathbf{K}
\left(\mathbf{X}_{i_B},\mathbf{X}_{j_B}\right).$

The CUR algorithm starts out from the diagonalization of this matrix

$\mathbf{U}^{T}\mathbf{K} \mathbf{U}= \mathbf{L} =
\textrm{diag}(l_{1},l_{2},...,l_{N_{B}}),$

where $\mathbf{U}$
is the matrix of the eigenvectors $\mathbf{u_j}$

$\mathbf{U} = (\mathbf{u}_{1},\mathbf{u}_{2},...,\mathbf{u}_{N_{B}}),
\qquad \mathbf{u}_{j} = \left( \begin{array}{c} u_{1j} \\ u_{2j}
\\... \\ u_{N_{B}j} \end{array} \right)$

In contrast to the original CUR
algorithm[^mahoney:pnas:2009-13]
that was developed to efficiently select a few significant columns of
the matrix $\mathbf{K}$,
we search for (few) insignificant local configurations and remove them.
We dispose of the columns of $\mathbf{K}$
that are correlated with the $N_{\mathrm{low}}$ eigenvectors $u_{\chi}$
with the smallest eigenvalues $l_{\chi}$.
The correlation is measured by the statistical leverage scoring measured
for each column $j$ of
$\mathbf{K}$ as

$\omega_{j}= \frac{1}{N_{\mathrm{low}}} \sum\limits_{\chi=1}^{N_{B}}
\gamma_{\chi,j},$

$\gamma_{\chi,j} = \left\\ \begin{array}{cl} u_{j\chi}^{2} &\mathrm{if}
\\\\ l_{\chi} > \epsilon_{\mathrm{low}} \\ 0 &\mathrm{otherwise}
\end{array} \right. ,$

where $\epsilon_{\mathrm{low}}$ (see also [ML_EPS_LOW](../incar-tags/ML_EPS_LOW.md))
is the threshold for the lowest eigenvalues. One can prove (using the
orthogonality of the eigenvectors and their completeness relation) that
this is equivalent to the usual CUR leverage scoring algorithm, i.e.
removing the least significant columns will result in those columns that
are most strongly "correlated" to the largest eigenvalues.

### Sparsification of angular descriptors\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=27"
class="mw-editsection-visualeditor"
title="Edit section: Sparsification of angular descriptors">edit</a> \| (./index.php.md)\]

The sparsification of the angular descriptors is done in a similar
manner as for the local reference configurations. We start by defining
the $N_{D} \times N_{D}$ square matrix

$\mathbf{A}=\mathbf{X}\mathbf{X}^{T}.$

Here $N_{D}$
denotes the number of angular descriptors given by

$N_{D} = \sum\limits_{l=1}^{L_{\mathrm{max}}} \frac{1}{2} N_{R}^{l}
\left( N_{R}^{l} + 1 \right) \left( L_{\mathrm{max}} + 1 \right).$

In this equation the symmetry of the descriptors
$\rho_{n \nu l}= \rho_{\nu n l}$ is already taken into
account. The matrix $\mathbf{X}$
is constructed from the vectors of the angular descriptors
$\left(\mathbf{x}_{1}^{(3)},\mathbf{x}_{2}^{(3)},...,\mathbf{x}_{N_{B}}^{(3)}
\right)$. The matrix $\mathbf{X}$
has dimension $N_{D} \times N_{B}$ and the matrix product is done over the
$N_{B}$ elements of the local configurations.

In analogy to the local configurations the $j$th element
of the matrix $\mathbf{A}$
is written as

$\mathbf{a}_{j} = \sum\limits_{\chi=1}^{N_{D}}
(u_{j\chi}l_{\chi})\mathbf{u_{\chi}}.$

In contrast to the sparsification of the local configuration and more in
line with the original CUR method, the columns of matrix
$\mathbf{A}$ are kept when they are strongly correlated
to the $k$ (see also
[ML_NRANK_SPARSDES](../incar-tags/ML_NRANK_SPARSDES.md))
eigenvectors $u_{\chi}$
which have the largest eigenvalues $l_{\chi}$.
The correlation of the eigenvalues is then measured via a leverage
scoring

$\omega_{j} = \frac{1}{k} \sum\limits_{\chi=1}^{k} u_{j\chi}^{2}.$

From the leverage scorings, the ones with the highest values are
selected until the ratio of the selected descriptors to the total number
of descriptors becomes a previously selected value
$x_{\mathrm{spars}}$ (see also
[ML_RDES_SPARSDES](../incar-tags/ML_RDES_SPARSDES.md)).

## References\[<a
href="/wiki/index.php?title=Machine_learning_force_field:_Theory&amp;veaction=edit&amp;section=28"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^jinnouchi:prl:2019-1]: [R. Jinnouchi, J. Lahnsteiner, F. Karsai, G. Kresse, and M. Bokdam, Phys. Rev. Lett. **122**, 225701 (2019).](https://doi.org/10.1103/PhysRevLett.122.225701)
[^jinnouchi2:arx:2019-2]: [R. Jinnouchi, F. Karsai, and G. Kresse, Phys. Rev. B **100**, 014105 (2019).](https://doi.org/10.1103/PhysRevB.100.014105)
[^jinnouchi:jcm:20-3]: [R. Jinnouchi, F. Karsai, C. Verdi, R. Asahi, and G. Kresse, J. Chem. Phys. **152**, 234102 (2020).](https://doi.org/10.1063/5.0009491)
[^bartok:prb:2013-4]: [A. P. Bartók, R. Kondor, and G. Csányi, Phys. Rev. B **87**, 184115 (2013).](https://doi.org/10.1103/PhysRevB.87.184115)
[^bartok:prl:2010-5]: [A. P. Bartók, M.C. Payne, R. Kondor, and G. Csányi, Phys. Rev. Lett **104**, 136403 (2010).](https://doi.org/10.1103/PhysRevLett.104.136403)
[^boyd:book:2000-6]: [J. P. Boyd, Chebyshev and Fourier Spectral Methods (Dover Publications, New York, 2000).](https://link.springer.com/gp/book/9783540514879)
[^csanyi:npj:2022-7]: [J. P. Darby, J. R. Kermode, and G. Csanyi, *Compressing local atomic neighbourhood descriptors*, New Phys. J. **8**, 166 (2022).](https://doi.org/10.1038/s41524-022-00847-y)
[^bishop:book:2006-8]: [C. M. Bishop, Pattern Recognition and Machine Learning, (New York: Springer), (2006).](https://www.springer.com/gp/book/9780387310732)
[^gull:book:1989-9]: [S.F. Gull and J. Skilling, Maximum Entropy Bayesian Methods, Fundam. Theor. Phys., 28th ed. (Springer, Dordrecht, 1989).](https://doi.org/10.1007/978-94-015-7860-8)
[^mackay:neu:2012-10]: [D. J. C. Mackay, Neural Computation **4**, 415 (1992).](https://doi.org/10.1162/neco.1992.4.3.415)
[^jinnouchi:pcl:2017-11]: [R. Jinnouchi and R. Asahi, J. Phys. Chem. Lett. **8**, 4279 (2017).](https://doi.org/10.1021/acs.jpclett.7b02010)
[^miwa:prb:2016-12]: [K. Miwa and H. Ohno, Phys. Rev. B **94**, 184109 (2016).](https://doi.org/10.1103/PhysRevB.94.184109)
[^mahoney:pnas:2009-13]: [M. W. Mahoney and P. Drineas, Proc. Natl. Acad. Sci. USA **106**, 697 (2009).](https://doi.org/10.1063/5.0009491)
