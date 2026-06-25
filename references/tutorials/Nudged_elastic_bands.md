<!-- Source: https://vasp.at/wiki/index.php/Nudged_elastic_bands | revid: 37272 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Nudged elastic bands


The nudged elastic band (NEB)
method<sup>[\[1\]](#cite_note-mills:surf-sci:1995-1)[\[2\]](#cite_note-jonsson:book:1998-2)</sup>
is a computational technique used for studying energy landscapes and
reaction pathways in chemical reactions or phase transitions. It entails
creating an initial path connecting the system's initial and final
states, employing a series of *images* to represent intermediate
configurations. These images are linked by springs, forming an elastic
band. The method then iteratively adjusts the image positions along the
band, minimizing energy until a minimum energy pathway, known as the
'nudged' path, is achieved.


## Contents


- [1 How to set up
  an NEB calculation](#How_to_set_up_an_NEB_calculation)
  - [1.1 Step
    1](#Step_1)
  - [1.2 Step
    2](#Step_2)
  - [1.3 Step
    3](#Step_3)
  - [1.4 Step
    4](#Step_4)
  - [1.5 Step
    5](#Step_5)
- [2 Possible
  issues and advice on how to address
  it](#Possible_issues_and_advice_on_how_to_address_it)
- [3 Related tags
  and articles](#Related_tags_and_articles)
- [4
  References](#References)


## How to set up an NEB calculation\[<a
href="/wiki/index.php?title=Nudged_elastic_bands&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: How to set up an NEB calculation">edit</a> \| (./index.php.md)\]

#### Step 1\[<a
href="/wiki/index.php?title=Nudged_elastic_bands&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Step 1">edit</a> \| (./index.php.md)\]

Carefully [optimize the
structure](Structure_optimization.md) of the
fixed structures of your elastic band, i.e., the initial and the final
state. Remember that in the subsequent steps, the elastic band will be
attached to these fixed structures, so any error will affect the
transition path you obtain.

#### Step 2\[<a
href="/wiki/index.php?title=Nudged_elastic_bands&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Step 2">edit</a> \| (./index.php.md)\]

Create a parent directory with enumerated subdirectories. For
$n$ [IMAGES](../incar-tags/IMAGES.md), create
$(n + 2)$ subdirectories and label them with their index
starting from `0`. The foldername must always have 2 characters, pad
with 0 if necessary. E.g. in case of 3 images

    mycalc -- 00
           |_ 01
           |_ 02
           |_ 03
           |_ 04

Place the [POSCAR](../input-files/POSCAR.md) file of the initial state in
`00` and [POSCAR](../input-files/POSCAR.md) file of the final state in the
last directory (`04` in the example).

#### Step 3\[<a
href="/wiki/index.php?title=Nudged_elastic_bands&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Step 3">edit</a> \| (./index.php.md)\]

Construct an initial guess for the intermediate structures. You may use
a script like in the <a
href="https://vasp.at/tutorials/latest/transition_states/part1/#transition_states-e01"
class="external text" rel="nofollow">tutorial on self-diffusion of a Si
atom to a vacancy site</a> or develop your own method. The intermediate
images should be somewhat close to the real transition path; otherwise,
the optimization of the elastic band may fail. Place the
[POSCAR](../input-files/POSCAR.md) files corresponding to these
intermediate structures in subdirectories `01`, `02`, etc.

|  |
|----|
| **Mind:** Make sure that the [POSCAR](../input-files/POSCAR.md) contains the same ordering of elements for initial, final, and intermediate states. It is highly recommended to minimize the number of images used to an absolute minimum. Convergence to the ground state is faster with fewer images. Starting with a single image between the two endpoints and increasing the number of images after the initial run has converged is often a prudent approach. |

#### Step 4\[<a
href="/wiki/index.php?title=Nudged_elastic_bands&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Step 4">edit</a> \| (./index.php.md)\]

Create an [INCAR](../input-files/INCAR.md) file in the parent directory
(e.g. `mycalc`) and set the tag [IMAGES](../incar-tags/IMAGES.md) to the
number of intermediate structures. This will introduce tangential
springs to maintain equidistance among images during the relaxation
process. Control the strength with the [SPRING](../incar-tags/SPRING.md)
tag, where negative values (like the default of -5) activate the NEB
method. It is important not to use excessively large values for
[SPRING](../incar-tags/SPRING.md), as it can hinder convergence. The
default value generally provides reliable results. You should also set
[IBRION](../incar-tags/IBRION.md), [ISIF](../incar-tags/ISIF.md),
[NSW](../incar-tags/NSW.md), and other .

#### Step 5\[<a
href="/wiki/index.php?title=Nudged_elastic_bands&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Step 5">edit</a> \| (./index.php.md)\]

Create the remaining input files [KPOINTS](../input-files/KPOINTS.md) and
[POTCAR](../input-files/POTCAR.md). For the NEB method, we recommend that
all input files, except the [POSCAR](../input-files/POSCAR.md),
[WAVECAR](../input-files/WAVECAR.md) and [CHGCAR](../input-files/CHGCAR.md)
file, reside in the parent directory. Then, run VASP by executing it in
the parent directory (e.g. `mycalc`) to optimize the reaction path.

## Possible issues and advice on how to address it\[<a
href="/wiki/index.php?title=Nudged_elastic_bands&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Possible issues and advice on how to address it">edit</a> \| (./index.php.md)\]

One challenge with the NEB method arises from its non-linear constraint,
which restricts movements to a hyper-plane perpendicular to the current
tangent. This characteristic can lead to convergence issues with the
conjugate-gradient (CG) algorithm ([IBRION](../incar-tags/IBRION.md)=2).
In such cases, it is advisable to use alternative algorithms like the
RMM-DIIS algorithm ([IBRION](../incar-tags/IBRION.md)=1) or the quick-min
algorithm ([IBRION](../incar-tags/IBRION.md)=3). Additionally, the
equidistant images tend to deviate from this constraint in the initial
steps. To address this, applying a low dimensionality parameter
([IBRION](../incar-tags/IBRION.md)=1, [NFREE](../incar-tags/NFREE.md)=2) in
the initial steps or using steepest descent minimization without line
optimization ([IBRION](../incar-tags/IBRION.md)=3,
[SMASS](../incar-tags/SMASS.md)=2) can help pre-converge the images.

If all degrees of freedom are allowed to relax, (e.g., in isolated
molecules or surfaces), it is crucial to ensure that the sum of all
positions remains consistent across all cells. Failing to do so
introduces artificial forces, causing the images to drift apart. While
this does not affect the VASP calculations, it can complicate result
visualization.

|  |
|----|
| **Warning:** The NEB feature presented here cannot be applied to structural transitions. Changing the lattice would require a different algorithm referred to as variable-cell NEB that is not available within VASP. |

|  |
|----|
| **Tip:** For more advanced calculations, consider using the <a href="https://theory.cm.utexas.edu/vtsttools/index.html"
class="external text" rel="nofollow">Transition State Tools for VASP
(VTST)</a>. |

## Related tags and articles\[<a
href="/wiki/index.php?title=Nudged_elastic_bands&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IMAGES](../incar-tags/IMAGES.md), [IMAGE_1](../incar-tags/IMAGE_1.md),
[SPRING](../incar-tags/SPRING.md), [IBRION](../incar-tags/IBRION.md)

<a
href="https://vasp.at/tutorials/latest/transition_states/part1/#transition_states-e01"
class="external text" rel="nofollow">Tutorial on self-diffusion of a Si
atom to a vacancy site</a>

Lecture on modeling chemical reactions (and transition states) using
<a href="https://youtu.be/mLK7CtDmw0A" class="external text"
rel="nofollow">static approaches</a>

[Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band
Calculation](https://vasp.at/wiki/index.php/Collective_jumps_of_a_Pt_adatom_on_fcc-Pt_(001):_Nudged_Elastic_Band_Calculation "Collective jumps of a Pt adatom on fcc-Pt (001): Nudged Elastic Band Calculation")

[TS search using the NEB
Method](../misc/TS_search_using_the_NEB_Method.md)

## References\[<a
href="/wiki/index.php?title=Nudged_elastic_bands&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-mills:surf-sci:1995_1-0)
    <a href="http://doi.org/10.1016/0039-6028(94)00731-4"
    class="external text" rel="nofollow">G. Mills, H. Jonsson and G. K.
    Schenter, <em>Reversible work transition state theory: application to
    dissociative adsorption of hydrogen</em>, Surf. Sci.,
    <strong>324</strong>, 305 (1995).</a>
2.  [↑](#cite_ref-jonsson:book:1998_2-0)
    <a href="https://doi.org/10.1142/9789812839664_0016"
    class="external text" rel="nofollow">H. Jonsson, G. Mills and K. W.
    Jacobsen, <em>Nudged Elastic Band Method for Finding Minimum Energy
    Paths of Transitions</em>, in <em>Classical and Quantum Dynamics in
    Condensed Phase Simulations</em>, ed. B. J. Berne, G. Ciccotti and D. F.
    Coker (World Scientific, 1998).</a>


