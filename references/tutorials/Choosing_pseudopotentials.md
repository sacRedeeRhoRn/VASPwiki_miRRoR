<!-- Source: https://vasp.at/wiki/index.php/Choosing_pseudopotentials | revid: 34876 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Choosing pseudopotentials


Several [pseudopotential variants labeled by
suffixes](../input-files/Available_pseudopotentials.md)
exist for many elements. When making a choice, it is necessary to
balance computational cost, accuracy, and transferability.

- To set up a minimal working example of your calculation, follow
  <a href="/wiki/Prepare_a_POTCAR" class="mw-redirect"
  title="Prepare a POTCAR">prepare a POTCAR</a>.
- Try to create a smaller test calculation and perform your own tests to
  confirm if the quantity of interest is sensitive to the choice of the
  pseudopotential. It might be possible to opt for a computationally
  cheaper [POTCAR](../input-files/POTCAR.md) and gain performance. On the
  other hand, it could be necessary to opt for a computationally
  demanding setup to obtain correct results.
- With the [aspects described in the next
  section](#aspects-to-refine-the-choice-of-pseudopotentials) in mind,
  carefully look over the [recommendations for each group in the
  periodic table](#recommendations-and-advice).


## Contents


- [1 Aspects to
  refine the choice of
  pseudopotentials](#aspects-to-refine-the-choice-of-pseudopotentials)
- [2
  Recommendations and
  advice](#recommendations-and-advice)
  - [2.1
    Recommended PAW
    potentials](#recommended-paw-potentials)
    - [2.1.1
      Standard DFT without the need for many
      unoccupied
      states](#standard-dft-without-the-need-for-many-unoccupied-states)
    - [2.1.2
      Calculation requiring a large number of
      unoccupied
      states](#calculation-requiring-a-large-number-of-unoccupied-states)
    - [2.1.3
      Reference calculation; extremely high
      accuracy](#reference-calculation-extremely-high-accuracy)
  - [2.2 Selecting
    the release version](#selecting-the-release-version)
  - [2.3
    Element-specific
    recommendation](#element-specific-recommendation)
    - [2.3.1
      Hydrogen-like atoms with fractional
      valence](#hydrogen-like-atoms-with-fractional-valence)
    - [2.3.2
      First-row
      elements](#first-row-elements)
    - [2.3.3 Alkali
      and alkali-earth elements (simple
      metals)](#alkali-and-alkali-earth-elements-simple-metals))
    - [2.3.4
      p-elements](#p-elements)
    - [2.3.5
      d-elements](#d-elements)
    - [2.3.6
      f-elements](#f-elements)
      - [2.3.6.1
        Lanthanides with fixed
        valence](#lanthanides-with-fixed-valence)
- [3 Example: NiO
  equilibrium volume](#example-nio-equilibrium-volume)
- [4 Related tags
  and sections](#related-tags-and-sections)
- [5
  References](#references)


## Aspects to refine the choice of pseudopotentials\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Aspects to refine the choice of pseudopotentials">edit</a> \| (./index.php.md)\]

**Aspect 1:** The bond lengths and the valency of the ions.

Short bonds will require harder potentials, and semicore states might
have to be treated as valence for certain chemical bonding. For some
elements, variants for specific valency exist; for example, the suffix
[\_2 or
\_3](../input-files/Available_pseudopotentials.md)
can be used to describe [fixed divalent or trivalent
Lanthanides](#lanthanides-with-fixed-valence).

**Aspect 2:** The physical or chemical property of interest.

If you are only interested in a rough
<a href="/wiki/Ionic_minimization" class="mw-redirect"
title="Ionic minimization">structure optimization</a>, soft potentials
([\_s](../input-files/Available_pseudopotentials.md))
with minimal valency may suffice. This approach might also work for
<a href="/wiki/Phonons" class="mw-redirect" title="Phonons">phonon
calculations</a> that rely on large supercells.

On the other hand, when optimizing a magnetic structure, it may be
necessary to include semicore states in the valence ([\_pv and
\_sv](../input-files/Available_pseudopotentials.md)).

For the computation of
<a href="/wiki/Optical_properties" class="mw-redirect"
title="Optical properties">optical properties</a>, it is crucial to use
[GW
potentials](../input-files/Available_pseudopotentials.md).

**Aspect 3:** The method or algorithm used in your calculation.

For any calculation involving unoccupied states significantly above the
Fermi energy, the [\_GW
variants](../input-files/Available_pseudopotentials.md)
of potentials are superior and should be used. Particularly, all kinds
of <a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">calculations within many-body
perturbation theory</a> need a high number of [empty
bands](../incar-tags/NBANDS.md).
Therefore, when GW, BSE, etc. is performed, the [GW
potentials](../input-files/Available_pseudopotentials.md)
should be used throughout the workflow.

<a href="/wiki/Hybrid_functionals" class="mw-redirect"
title="Hybrid functionals">Hartree-Fock and hybrid caluclations</a>
should *not* be performed with soft potentials
([\_s](../input-files/Available_pseudopotentials.md)).
Moreover, any calculations where you switch the
<a href="/wiki/Exchange-correlation_functional" class="mw-redirect"
title="Exchange-correlation functional">exchange-correlation
functional</a> should *not* be performed with soft potentials
([\_s](../input-files/Available_pseudopotentials.md)).

For standard DFT-ground-state calculations, using [\_GW or
\_h](../input-files/Available_pseudopotentials.md)
potentials is usually unnecessary unless, e.g., the property of interest
or geometry of the structure demands it.

## Recommendations and advice\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Recommendations and advice">edit</a> \| (./index.php.md)\]

### Recommended PAW potentials\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Recommended PAW potentials">edit</a> \| (./index.php.md)\]

#### Standard DFT without the need for many unoccupied states\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Standard DFT without the need for many unoccupied states">edit</a> \| (./index.php.md)\]

The table directly below highlights recommended PAW potentials in
**bold**.

These potentials are *not ideal* for calculations involving a large
number of excited states as needed, e.g., for
<a href="/wiki/Optical_properties" class="mw-redirect"
title="Optical properties">optical properties</a> or
<a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">many-body perturbation theory</a>.

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| Standard PBE potentials (potpaw.64) |  |  |  |
| Potential name | Number of valence electrons | Valence electron configuration | ENAMX \[eV\] |
| **H** | **1** | **1*s*<sup>1</sup>** | **250.0** |
| H.25 | 0.25 | 1*s*<sup>0.25</sup> | 250.0 |
| H.33 | 0.33 | 1*s*<sup>0.33</sup> | 250.0 |
| H.42 | 0.42 | 1*s*<sup>0.42</sup> | 250.0 |
| H.5 | 0.5 | 1*s*<sup>0.5</sup> | 250.0 |
| H.58 | 0.58 | 1*s*<sup>0.58</sup> | 250.0 |
| H.66 | 0.66 | 1*s*<sup>0.66</sup> | 250.0 |
| H.75 | 0.75 | 1*s*<sup>0.75</sup> | 250.0 |
| H1.25 | 1.25 | 1*s*<sup>1.25</sup> | 250.0 |
| H1.33 | 1.33 | 1*s*<sup>1.33</sup> | 250.0 |
| H1.5 | 1.5 | 1*s*<sup>1.5</sup> | 250.0 |
| H1.66 | 1.66 | 1*s*<sup>1.66</sup> | 250.0 |
| H1.75 | 1.75 | 1*s*<sup>1.75</sup> | 250.0 |
| H_AE | 1 | 1*s*<sup>1</sup> | 1000.0 |
| H_h | 1 | 1*s*<sup>1</sup> | 700.0 |
| H_s | 1 | 1*s*<sup>1</sup> | 200.0 |
| **He** | **2** | **1*s*<sup>2</sup>** | **478.896** |
| He_AE | 2 | 1*s*<sup>2</sup> | 2135.871 |
| Li | 1 | 2*s*<sup>1</sup> | 140.0 |
| **Li_sv** | **3** | **1*s*<sup>2</sup> 2*s*<sup>1</sup>** | **499.034** |
| **Be** | **2** | **2*s*<sup>1.99</sup> 2*p*<sup>0.01</sup>** | **247.543** |
| Be_sv | 4 | 1*s*<sup>2</sup> 2*s*<sup>1.99</sup> 2*p*<sup>0.01</sup> | 308.768 |
| **B** | **3** | **2*s*<sup>2</sup> 2*p*<sup>1</sup>** | **318.614** |
| B_h | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 700.0 |
| B_s | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 269.245 |
| **C** | **4** | **2*s*<sup>2</sup> 2*p*<sup>2</sup>** | **400.0** |
| C_h | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 741.689 |
| C_s | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 273.911 |
| **N** | **5** | **2*s*<sup>2</sup> 2*p*<sup>3</sup>** | **400.0** |
| N_h | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 755.582 |
| N_s | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 279.692 |
| **O** | **6** | **2*s*<sup>2</sup> 2*p*<sup>4</sup>** | **400.0** |
| O_h | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 765.519 |
| O_s | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 282.853 |
| **F** | **7** | **2*s*<sup>2</sup> 2*p*<sup>5</sup>** | **400.0** |
| F_h | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 772.626 |
| F_s | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 289.837 |
| **Ne** | **8** | **2*s*<sup>2</sup> 2*p*<sup>6</sup>** | **343.606** |
| Na | 1 | 3*s*<sup>1</sup> | 101.968 |
| **Na_pv** | **7** | **2*p*<sup>6</sup> 3*s*<sup>1</sup>** | **259.561** |
| Na_sv | 9 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>1</sup> | 645.64 |
| **Mg** | **2** | **3*s*<sup>2</sup>** | **200.0** |
| Mg_pv | 8 | 2*p*<sup>6</sup> 3*s*<sup>2</sup> | 403.929 |
| Mg_sv | 10 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>2</sup> | 495.223 |
| **Al** | **3** | **3*s*<sup>2</sup> 3*p*<sup>1</sup>** | **240.3** |
| **Si** | **4** | **3*s*<sup>2</sup> 3*p*<sup>2</sup>** | **245.345** |
| **P** | **5** | **3*s*<sup>2</sup> 3*p*<sup>3</sup>** | **255.04** |
| P_h | 5 | 3*s*<sup>2</sup> 3*p*<sup>3</sup> | 390.202 |
| **S** | **6** | **3*s*<sup>2</sup> 3*p*<sup>4</sup>** | **258.689** |
| S_h | 6 | 3*s*<sup>2</sup> 3*p*<sup>4</sup> | 402.436 |
| **Cl** | **7** | **3*s*<sup>2</sup> 3*p*<sup>5</sup>** | **262.472** |
| Cl_h | 7 | 3*s*<sup>2</sup> 3*p*<sup>5</sup> | 409.136 |
| **Ar** | **8** | **3*s*<sup>2</sup> 3*p*<sup>6</sup>** | **266.408** |
| K_pv | 7 | 3*p*<sup>6</sup> 4*s*<sup>1</sup> | 116.731 |
| **K_sv** | **9** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 4*s*<sup>1</sup>** | **259.264** |
| Ca_pv | 8 | 3*p*<sup>6</sup> 4*s*<sup>2</sup> | 119.559 |
| **Ca_sv** | **10** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 4*s*<sup>2</sup>** | **266.622** |
| Sc | 3 | 3*d*<sup>2</sup> 4*s*<sup>1</sup> | 154.763 |
| **Sc_sv** | **11** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>2</sup> 4*s*<sup>1</sup>** | **222.66** |
| Ti | 4 | 3*d*<sup>3</sup> 4*s*<sup>1</sup> | 178.33 |
| Ti_pv | 10 | 3*p*<sup>6</sup> 3*d*<sup>3</sup> 4*s*<sup>1</sup> | 222.335 |
| **Ti_sv** | **12** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>3</sup> 4*s*<sup>1</sup>** | **274.61** |
| V | 5 | 3*d*<sup>4</sup> 4*s*<sup>1</sup> | 192.543 |
| V_pv | 11 | 3*p*<sup>6</sup> 3*d*<sup>4</sup> 4*s*<sup>1</sup> | 263.673 |
| **V_sv** | **13** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>4</sup> 4*s*<sup>1</sup>** | **263.673** |
| Cr | 6 | 3*d*<sup>5</sup> 4*s*<sup>1</sup> | 227.08 |
| **Cr_pv** | **12** | **3*p*<sup>6</sup> 3*d*<sup>5</sup> 4*s*<sup>1</sup>** | **265.681** |
| Cr_sv | 14 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>5</sup> 4*s*<sup>1</sup> | 395.471 |
| Mn | 7 | 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 269.864 |
| **Mn_pv** | **13** | **3*p*<sup>6</sup> 3*d*<sup>6</sup> 4*s*<sup>1</sup>** | **269.864** |
| Mn_sv | 15 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 387.187 |
| **Fe** | **8** | **3*d*<sup>7</sup> 4*s*<sup>1</sup>** | **267.882** |
| Fe_pv | 14 | 3*p*<sup>6</sup> 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 293.238 |
| Fe_sv | 16 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 390.558 |
| **Co** | **9** | **3*d*<sup>8</sup> 4*s*<sup>1</sup>** | **267.968** |
| Co_pv | 15 | 3*p*<sup>6</sup> 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 271.042 |
| Co_sv | 17 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 390.362 |
| **Ni** | **10** | **3*d*<sup>9</sup> 4*s*<sup>1</sup>** | **269.532** |
| Ni_pv | 16 | 3*p*<sup>6</sup> 3*d*<sup>9</sup> 4*s*<sup>1</sup> | 367.986 |
| **Cu** | **11** | **3*d*<sup>10</sup> 4*s*<sup>1</sup>** | **295.446** |
| Cu_pv | 17 | 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>1</sup> | 368.648 |
| **Zn** | **12** | **3*d*<sup>10</sup> 4*s*<sup>2</sup>** | **276.723** |
| Ga | 3 | 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 134.678 |
| **Ga_d** | **13** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup>** | **282.691** |
| Ga_h | 13 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 404.601 |
| Ge | 4 | 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 173.807 |
| **Ge_d** | **14** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup>** | **310.294** |
| Ge_h | 14 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 410.425 |
| **As** | **5** | **4*s*<sup>2</sup> 4*p*<sup>3</sup>** | **208.702** |
| As_d | 15 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>3</sup> | 288.651 |
| **Se** | **6** | **4*s*<sup>2</sup> 4*p*<sup>4</sup>** | **211.555** |
| **Br** | **7** | **4*s*<sup>2</sup> 4*p*<sup>5</sup>** | **216.285** |
| **Kr** | **8** | **4*s*<sup>2</sup> 4*p*<sup>6</sup>** | **185.331** |
| Rb_pv | 7 | 4*p*<sup>6</sup> 4*d*<sup>0.001</sup> 5*s*<sup>0.999</sup> | 121.882 |
| **Rb_sv** | **9** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>0.001</sup> 5*s*<sup>0.999</sup>** | **220.112** |
| **Sr_sv** | **10** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>0.001</sup> 5*s*<sup>1.999</sup>** | **229.353** |
| **Y_sv** | **11** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>2</sup> 5*s*<sup>1</sup>** | **202.626** |
| **Zr_sv** | **12** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>3</sup> 5*s*<sup>1</sup>** | **229.898** |
| Nb_pv | 11 | 4*p*<sup>6</sup> 4*d*<sup>4</sup> 5*s*<sup>1</sup> | 208.608 |
| **Nb_sv** | **13** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>4</sup> 5*s*<sup>1</sup>** | **293.235** |
| Mo | 6 | 4*d*<sup>5</sup> 5*s*<sup>1</sup> | 224.584 |
| Mo_pv | 12 | 4*p*<sup>6</sup> 4*d*<sup>5</sup> 5*s*<sup>1</sup> | 224.584 |
| **Mo_sv** | **14** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>5</sup> 5*s*<sup>1</sup>** | **242.676** |
| Tc | 7 | 4*d*<sup>6</sup> 5*s*<sup>1</sup> | 228.694 |
| **Tc_pv** | **13** | **4*p*<sup>6</sup> 4*d*<sup>6</sup> 5*s*<sup>1</sup>** | **263.523** |
| Tc_sv | 15 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>6</sup> 5*s*<sup>1</sup> | 318.703 |
| Ru | 8 | 4*d*<sup>7</sup> 5*s*<sup>1</sup> | 213.271 |
| **Ru_pv** | **14** | **4*p*<sup>6</sup> 4*d*<sup>7</sup> 5*s*<sup>1</sup>** | **240.049** |
| Ru_sv | 16 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>7</sup> 5*s*<sup>1</sup> | 318.855 |
| Rh | 9 | 4*d*<sup>8</sup> 5*s*<sup>1</sup> | 228.996 |
| **Rh_pv** | **15** | **4*p*<sup>6</sup> 4*d*<sup>8</sup> 5*s*<sup>1</sup>** | **247.408** |
| **Pd** | **10** | **4*d*<sup>9</sup> 5*s*<sup>1</sup>** | **250.925** |
| Pd_pv | 16 | 4*p*<sup>6</sup> 4*d*<sup>9</sup> 5*s*<sup>1</sup> | 250.925 |
| **Ag** | **11** | **4*d*<sup>10</sup> 5*s*<sup>1</sup>** | **249.844** |
| Ag_pv | 17 | 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>1</sup> | 297.865 |
| **Cd** | **12** | **4*d*<sup>10</sup> 5*s*<sup>2</sup>** | **274.336** |
| In | 3 | 5*s*<sup>2</sup> 5*p*<sup>1</sup> | 95.934 |
| **In_d** | **13** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup>** | **239.211** |
| Sn | 4 | 5*s*<sup>2</sup> 5*p*<sup>2</sup> | 103.236 |
| **Sn_d** | **14** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup>** | **241.083** |
| **Sb** | **5** | **5*s*<sup>2</sup> 5*p*<sup>3</sup>** | **172.069** |
| **Te** | **6** | **5*s*<sup>2</sup> 5*p*<sup>4</sup>** | **174.982** |
| **I** | **7** | **5*s*<sup>2</sup> 5*p*<sup>5</sup>** | **175.647** |
| **Xe** | **8** | **5*s*<sup>2</sup> 5*p*<sup>6</sup>** | **153.118** |
| **Cs_sv** | **9** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 6*s*<sup>1</sup>** | **220.318** |
| **Ba_sv** | **10** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.01</sup> 6*s*<sup>1.99</sup>** | **187.181** |
| **La** | **11** | **4*f*<sup>0.0001</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.9999</sup> 6*s*<sup>2</sup>** | **219.292** |
| La_s | 9 | 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 136.53 |
| **Ce** | **12** | **4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **273.042** |
| Ce_3 | 11 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 176.506 |
| Ce_h | 12 | 4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 299.9 |
| Pr | 13 | 4*f*<sup>2.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 337.25 |
| **Pr_3** | **11** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **181.719** |
| Pr_h | 13 | 4*f*<sup>2.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 400.742 |
| Nd | 14 | 4*f*<sup>3.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 338.34 |
| **Nd_3** | **11** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **182.619** |
| Nd_h | 14 | 4*f*<sup>3.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 402.016 |
| Pm | 15 | 4*f*<sup>4.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 340.358 |
| **Pm_3** | **11** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **176.959** |
| Pm_h | 15 | 4*f*<sup>4.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 404.406 |
| Sm | 16 | 4*f*<sup>5.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 341.177 |
| **Sm_3** | **11** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **177.087** |
| Sm_h | 16 | 4*f*<sup>5.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 405.382 |
| Eu | 17 | 4*f*<sup>6.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 344.705 |
| **Eu_2** | **8** | **5*p*<sup>6</sup> 6*s*<sup>2</sup>** | **99.328** |
| Eu_3 | 9 | 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 129.057 |
| Eu_h | 17 | 4*f*<sup>6.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 403.212 |
| Gd | 18 | 4*f*<sup>7.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 342.859 |
| **Gd_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **154.332** |
| Gd_h | 18 | 4*f*<sup>7.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 407.403 |
| Tb | 19 | 4*f*<sup>8.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 340.855 |
| **Tb_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **155.613** |
| Tb_h | 19 | 4*f*<sup>8.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 405.043 |
| Dy | 20 | 4*f*<sup>9.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 341.547 |
| **Dy_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **155.713** |
| Dy_h | 20 | 4*f*<sup>9.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 405.886 |
| Ho | 21 | 4*f*<sup>10.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 343.845 |
| **Ho_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **154.137** |
| Ho_h | 21 | 4*f*<sup>10.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 415.91 |
| Er | 22 | 4*f*<sup>11.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 346.295 |
| Er_2 | 8 | 5*p*<sup>6</sup> 6*s*<sup>2</sup> | 119.75 |
| **Er_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **155.037** |
| Er_h | 22 | 4*f*<sup>11.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 429.583 |
| Tm | 23 | 4*f*<sup>12.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 344.206 |
| **Tm_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **149.221** |
| Tm_h | 23 | 4*f*<sup>12.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 419.812 |
| Yb | 24 | 4*f*<sup>13.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 344.312 |
| **Yb_2** | **8** | **5*p*<sup>6</sup> 6*s*<sup>2</sup>** | **112.578** |
| Yb_3 | 9 | 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 188.359 |
| Yb_h | 24 | 4*f*<sup>13.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 409.285 |
| Lu | 25 | 4*f*<sup>14</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 255.695 |
| **Lu_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **154.992** |
| Hf | 4 | 5*d*<sup>3</sup> 6*s*<sup>1</sup> | 220.334 |
| **Hf_pv** | **10** | **5*p*<sup>6</sup> 5*d*<sup>3</sup> 6*s*<sup>1</sup>** | **220.334** |
| Hf_sv | 12 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>4</sup> | 237.444 |
| Ta | 5 | 5*d*<sup>4</sup> 6*s*<sup>1</sup> | 223.667 |
| **Ta_pv** | **11** | **5*p*<sup>6</sup> 5*d*<sup>4</sup> 6*s*<sup>1</sup>** | **223.667** |
| W | 6 | 5*d*<sup>5</sup> 6*s*<sup>1</sup> | 223.057 |
| **W_sv** | **14** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>5</sup> 6*s*<sup>1</sup>** | **223.057** |
| **Re** | **7** | **5*d*<sup>6</sup> 6*s*<sup>1</sup>** | **226.216** |
| Re_pv | 13 | 5*p*<sup>6</sup> 5*d*<sup>6</sup> 6*s*<sup>1</sup> | 226.216 |
| **Os** | **8** | **5*d*<sup>7</sup> 6*s*<sup>1</sup>** | **228.022** |
| Os_pv | 14 | 5*p*<sup>6</sup> 5*d*<sup>7</sup> 6*s*<sup>1</sup> | 228.022 |
| **Ir** | **9** | **5*d*<sup>8</sup> 6*s*<sup>1</sup>** | **210.864** |
| **Pt** | **10** | **5*d*<sup>9</sup> 6*s*<sup>1</sup>** | **230.283** |
| Pt_pv | 16 | 5*p*<sup>6</sup> 5*d*<sup>9</sup> 6*s*<sup>1</sup> | 294.607 |
| **Au** | **11** | **5*d*<sup>10</sup> 6*s*<sup>1</sup>** | **229.943** |
| **Hg** | **12** | **5*d*<sup>10</sup> 6*s*<sup>2</sup>** | **233.204** |
| Tl | 3 | 6*s*<sup>2</sup> 6*p*<sup>1</sup> | 90.14 |
| **Tl_d** | **13** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>1</sup>** | **237.053** |
| Pb | 4 | 6*s*<sup>2</sup> 6*p*<sup>2</sup> | 97.973 |
| **Pb_d** | **14** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup>** | **237.835** |
| Bi | 5 | 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 105.037 |
| **Bi_d** | **15** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup>** | **242.839** |
| Po | 6 | 6*s*<sup>2</sup> 6*p*<sup>4</sup> | 159.707 |
| **Po_d** | **16** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>4</sup>** | **264.565** |
| **At** | **7** | **6*s*<sup>2</sup> 6*p*<sup>5</sup>** | **161.43** |
| **Rn** | **8** | **6*s*<sup>2</sup> 6*p*<sup>6</sup>** | **151.497** |
| **Fr_sv** | **9** | **6*s*<sup>2</sup> 6*p*<sup>6</sup> 7*s*<sup>1</sup>** | **214.54** |
| **Ra_sv** | **10** | **6*s*<sup>2</sup> 6*p*<sup>6</sup> 7*s*<sup>2</sup>** | **237.367** |
| **Ac** | **11** | **6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>1</sup> 7*s*<sup>2</sup>** | **172.351** |
| **Th** | **12** | **5*f*<sup>1</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>1</sup> 7*s*<sup>2</sup>** | **247.306** |
| Th_s | 10 | 5*f*<sup>1</sup> 6*p*<sup>6</sup> 6*d*<sup>1</sup> 7*s*<sup>2</sup> | 169.363 |
| **Pa** | **13** | **5*f*<sup>1</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **252.193** |
| Pa_s | 11 | 5*f*<sup>1</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 193.466 |
| **U** | **14** | **5*f*<sup>2</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **252.502** |
| U_s | 14 | 5*f*<sup>2</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 209.23 |
| **Np** | **15** | **5*f*<sup>3</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **254.26** |
| Np_s | 15 | 5*f*<sup>3</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 207.713 |
| **Pu** | **16** | **5*f*<sup>4</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **254.353** |
| Pu_s | 16 | 5*f*<sup>4</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 207.83 |
| **Am** | **17** | **5*f*<sup>5</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **255.875** |
| **Cm** | **18** | **5*f*<sup>6</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **257.953** |
| Cf | 20 | 5*f*<sup>8</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 414.614 |

#### Calculation requiring a large number of unoccupied states\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Calculation requiring a large number of unoccupied states">edit</a> \| (./index.php.md)\]

The following table highlights recommended PAW potentials for
calculations involving many states above the Fermi energy in **bold**.

They are optimized for scattering properties high above the Fermi level
and thus have advantages if many unoccupied states are involved, as for
<a href="/wiki/Optical_properties" class="mw-redirect"
title="Optical properties">optical properties</a> or
<a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">many-body perturbation theory</a>.

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| GW potentials (potpaw.64) |  |  |  |
| Potential name | Number of valence electrons | Valence electron configuration | ENAMX \[eV\] |
| **H_GW** | **1** | **1*s*<sup>1</sup>** | **300.0** |
| H_GW_new | 1 | 1*s*<sup>1</sup> | 536.615 |
| H_h_GW | 1 | 1*s*<sup>1</sup> | 700.0 |
| **He_GW** | **2** | **1*s*<sup>2</sup>** | **405.78** |
| Li_AE_GW | 3 | 1*s*<sup>2</sup> 2*p*<sup>1</sup> | 433.699 |
| Li_GW | 1 | 2*s*<sup>1</sup> | 112.104 |
| **Li_sv_GW** | **3** | **1*s*<sup>2</sup> 2*p*<sup>1</sup>** | **433.699** |
| Be_GW | 2 | 2*s*<sup>1.9999</sup> 2*p*<sup>0.001</sup> | 247.543 |
| **Be_sv_GW** | **4** | **1*s*<sup>2</sup> 2*p*<sup>2</sup>** | **537.454** |
| **B_GW** | **3** | **2*s*<sup>2</sup> 2*p*<sup>1</sup>** | **318.614** |
| B_GW_new | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 318.614 |
| B_h_GW | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 731.373 |
| **C_GW** | **4** | **2*s*<sup>2</sup> 2*p*<sup>2</sup>** | **413.992** |
| C_GW_new | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 433.983 |
| C_h_GW | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 741.689 |
| C_s_GW | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 304.843 |
| **N_GW** | **5** | **2*s*<sup>2</sup> 2*p*<sup>3</sup>** | **420.902** |
| N_GW_new | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 452.633 |
| N_h_GW | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 755.582 |
| N_s_GW | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 312.986 |
| **O_GW** | **6** | **2*s*<sup>2</sup> 2*p*<sup>4</sup>** | **414.635** |
| O_GW_new | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 466.797 |
| O_h_GW | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 765.519 |
| O_s_GW | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 334.664 |
| **F_GW** | **7** | **2*s*<sup>2</sup> 2*p*<sup>5</sup>** | **487.698** |
| F_GW_new | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 480.281 |
| F_h_GW | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 848.626 |
| **Ne_GW** | **8** | **2*s*<sup>2</sup> 2*p*<sup>6</sup>** | **432.275** |
| Ne_s_GW | 8 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> | 318.26 |
| **Na_sv_GW** | **9** | **2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*p*<sup>1</sup>** | **372.853** |
| Mg_GW | 2 | 3*s*<sup>2</sup> | 126.143 |
| Mg_pv_GW | 8 | 2*p*<sup>6</sup> 3*s*<sup>2</sup> | 403.929 |
| **Mg_sv_GW** | **10** | **2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*d*<sup>2</sup>** | **429.893** |
| **Al_GW** | **3** | **3*s*<sup>2</sup> 3*p*<sup>1</sup>** | **240.3** |
| Al_sv_GW | 11 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>2</sup> 3*p*<sup>1</sup> | 411.109 |
| **Si_GW** | **4** | **3*s*<sup>2</sup> 3*p*<sup>2</sup>** | **245.345** |
| Si_sv_GW | 12 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>2</sup> 3*p*<sup>2</sup> | 547.578 |
| **P_GW** | **5** | **3*s*<sup>2</sup> 3*p*<sup>3</sup>** | **255.04** |
| **S_GW** | **6** | **3*s*<sup>2</sup> 3*p*<sup>4</sup>** | **258.689** |
| **Cl_GW** | **7** | **3*s*<sup>2</sup> 3*p*<sup>5</sup>** | **262.472** |
| **Ar_GW** | **8** | **3*s*<sup>2</sup> 3*p*<sup>6</sup>** | **290.599** |
| **K_sv_GW** | **9** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>1</sup>** | **248.998** |
| **Ca_sv_GW** | **10** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>2</sup>** | **281.43** |
| **Sc_sv_GW** | **11** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>3</sup>** | **378.961** |
| **Ti_sv_GW** | **12** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>4</sup>** | **383.774** |
| **V_sv_GW** | **13** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>5</sup>** | **382.321** |
| **Cr_sv_GW** | **14** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>6</sup>** | **384.932** |
| Mn_GW | 7 | 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 278.466 |
| **Mn_sv_GW** | **15** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>7</sup>** | **384.627** |
| Fe_GW | 8 | 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 321.007 |
| **Fe_sv_GW** | **16** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>8</sup>** | **387.837** |
| Co_GW | 9 | 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 323.4 |
| **Co_sv_GW** | **17** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>9</sup>** | **387.491** |
| Ni_GW | 10 | 3*d*<sup>9</sup> 4*s*<sup>1</sup> | 357.323 |
| **Ni_sv_GW** | **18** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup>** | **389.645** |
| Cu_GW | 11 | 3*d*<sup>10</sup> 4*s*<sup>1</sup> | 417.039 |
| **Cu_sv_GW** | **19** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>1</sup>** | **467.331** |
| Zn_GW | 12 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> | 328.191 |
| **Zn_sv_GW** | **20** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup>** | **401.665** |
| Ga_GW | 3 | 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 134.678 |
| **Ga_d_GW** | **13** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup>** | **404.602** |
| Ga_sv_GW | 21 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 404.602 |
| Ge_GW | 4 | 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 173.807 |
| **Ge_d_GW** | **14** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup>** | **375.434** |
| Ge_sv_GW | 22 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 410.425 |
| **As_GW** | **5** | **4*s*<sup>2</sup> 4*p*<sup>3</sup>** | **208.702** |
| As_sv_GW | 23 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>3</sup> | 415.313 |
| **Se_GW** | **6** | **4*s*<sup>2</sup> 4*p*<sup>4</sup>** | **211.555** |
| Se_sv_GW | 24 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>4</sup> | 469.344 |
| **Br_GW** | **7** | **4*s*<sup>2</sup> 4*p*<sup>5</sup>** | **216.285** |
| Br_sv_GW | 25 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>5</sup> | 475.692 |
| **Kr_GW** | **8** | **4*s*<sup>2</sup> 4*p*<sup>6</sup>** | **252.232** |
| **Rb_sv_GW** | **9** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>1</sup>** | **221.197** |
| **Sr_sv_GW** | **10** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>2</sup>** | **224.817** |
| **Y_sv_GW** | **11** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>3</sup>** | **339.758** |
| **Zr_sv_GW** | **12** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>4</sup>** | **346.364** |
| **Nb_sv_GW** | **13** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>5</sup>** | **353.872** |
| **Mo_sv_GW** | **14** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>6</sup>** | **344.914** |
| **Tc_sv_GW** | **15** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>7</sup>** | **351.044** |
| **Ru_sv_GW** | **16** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>8</sup>** | **348.106** |
| Rh_GW | 9 | 4*d*<sup>8</sup> 5*s*<sup>1</sup> | 247.408 |
| **Rh_sv_GW** | **17** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>9</sup>** | **351.206** |
| Pd_GW | 10 | 4*d*<sup>9</sup> 5*s*<sup>1</sup> | 250.925 |
| **Pd_sv_GW** | **18** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup>** | **356.093** |
| Ag_GW | 11 | 4*d*<sup>10</sup> 5*s*<sup>1</sup> | 249.844 |
| **Ag_sv_GW** | **19** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>11</sup>** | **354.43** |
| Cd_GW | 12 | 4*d*<sup>10</sup> 5*s*<sup>2</sup> | 254.045 |
| **Cd_sv_GW** | **20** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup>** | **361.806** |
| **In_d_GW** | **13** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup>** | **278.624** |
| In_sv_GW | 21 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup> | 366.771 |
| **Sn_d_GW** | **14** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup>** | **260.066** |
| Sn_sv_GW | 22 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup> | 368.778 |
| Sb_GW | 5 | 5*s*<sup>2</sup> 5*p*<sup>3</sup> | 172.069 |
| **Sb_d_GW** | **15** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>3</sup>** | **263.1** |
| Sb_sv_GW | 23 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>3</sup> | 372.491 |
| **Te_GW** | **6** | **5*s*<sup>2</sup> 5*p*<sup>4</sup>** | **174.982** |
| Te_sv_GW | 24 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>4</sup> | 376.618 |
| **I_GW** | **7** | **5*s*<sup>2</sup> 5*p*<sup>5</sup>** | **175.647** |
| I_sv_GW | 25 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>5</sup> | 381.674 |
| **Xe_GW** | **8** | **5*s*<sup>2</sup> 5*p*<sup>6</sup>** | **179.547** |
| Xe_sv_GW | 26 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> | 400.476 |
| **Cs_sv_GW** | **9** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup>** | **198.101** |
| **Ba_sv_GW** | **10** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>1</sup>** | **267.02** |
| **La_GW** | **11** | **4*f*<sup>0.2</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.8</sup> 6*s*<sup>2</sup>** | **313.688** |
| **Ce_GW** | **12** | **4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **304.625** |
| **Hf_sv_GW** | **12** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>4</sup>** | **309.037** |
| **Ta_sv_GW** | **13** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>5</sup>** | **286.008** |
| **W_sv_GW** | **14** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>6</sup>** | **317.132** |
| **Re_sv_GW** | **15** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>7</sup>** | **317.012** |
| **Os_sv_GW** | **16** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>8</sup>** | **319.773** |
| **Ir_sv_GW** | **17** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>9</sup>** | **319.843** |
| Pt_GW | 10 | 5*d*<sup>9</sup> 6*s*<sup>1</sup> | 248.716 |
| **Pt_sv_GW** | **18** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup>** | **323.669** |
| Au_GW | 11 | 5*d*<sup>10</sup> 6*s*<sup>1</sup> | 248.344 |
| **Au_sv_GW** | **19** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>11</sup>** | **306.658** |
| **Hg_sv_GW** | **20** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup>** | **312.028** |
| **Tl_d_GW** | **15** | **5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>1</sup>** | **237.053** |
| Tl_sv_GW | 21 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>1</sup> | 316.583 |
| **Pb_d_GW** | **16** | **5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup>** | **237.809** |
| Pb_sv_GW | 22 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup> | 317.193 |
| Bi_GW | 5 | 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 146.53 |
| **Bi_d_GW** | **17** | **5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup>** | **261.876** |
| Bi_sv_GW | 23 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 323.513 |
| **Po_d_GW** | **18** | **5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>4</sup>** | **267.847** |
| Po_sv_GW | 24 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>4</sup> | 326.618 |
| **At_d_GW** | **17** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>5</sup>** | **266.251** |
| At_sv_GW | 25 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>5</sup> | 328.529 |
| **Rn_d_GW** | **18** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup>** | **267.347** |
| Rn_sv_GW | 26 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> | 329.758 |

#### Reference calculation; extremely high accuracy\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Reference calculation; extremely high accuracy">edit</a> \| (./index.php.md)\]

For reference calculations, i.e., calculations where the utmost accuracy
is needed, and computational effort is of no concern, we recommend the
following set of potentials. These are mostly [hard pseudopotentials
(\_h)](../input-files/Available_pseudopotentials.md)
of the GW variant, which were used with a 1000 eV plane-wave cutoff in a
recent comparison study of DFT codes to reproduce all-electron results
as accurately as
possible<sup>[\[1\]](#cite_note-bosoni:natphysrev:2023-1)</sup>.
However, in most cases, the results should be comparable with the
standard potentials, while the computational effort will increase
significantly<sup>[\[2\]](#cite_note-2)</sup>.

|  |
|----|
| **Mind:** Unless the utmost accuracy is required, it is usually not worth paying the extra computational cost required for the hard GW potentials recommended in the following list, compared to their standard counterparts at the beginning of this section for DFT calculations. |

|  |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|
| Reference potentials (potpaw.64) |  |  |  |  |
| Element | Potential name | Number of valence electrons | Valence electron configuration | ENAMX \[eV\] |
| H | H_GW | 1 | 1*s*<sup>1</sup> | 300.0 |
| He | He_GW | 2 | 1*s*<sup>2</sup> | 405.78 |
| Li | Li_sv_GW | 3 | 1*s*<sup>2</sup> 2*p*<sup>1</sup> | 433.699 |
| Be | Be_sv_GW | 4 | 1*s*<sup>2</sup> 2*p*<sup>2</sup> | 537.454 |
| B | B_GW | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 318.614 |
| C | C_GW | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 413.992 |
| N | N_GW | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 420.902 |
| O | O_h_GW | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 765.519 |
| F | F_GW | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 487.698 |
| Ne | Ne_GW | 8 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> | 432.275 |
| Na | Na_sv_GW | 9 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*p*<sup>1</sup> | 372.853 |
| Mg | Mg_sv_GW | 10 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*d*<sup>2</sup> | 429.893 |
| Al | Al_GW | 3 | 3*s*<sup>2</sup> 3*p*<sup>1</sup> | 240.3 |
| Si | Si_GW | 4 | 3*s*<sup>2</sup> 3*p*<sup>2</sup> | 245.345 |
| P | P_GW | 5 | 3*s*<sup>2</sup> 3*p*<sup>3</sup> | 255.04 |
| S | S_GW | 6 | 3*s*<sup>2</sup> 3*p*<sup>4</sup> | 258.689 |
| Cl | Cl_GW | 7 | 3*s*<sup>2</sup> 3*p*<sup>5</sup> | 262.472 |
| Ar | Ar_GW | 8 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> | 290.599 |
| K | K_sv_GW | 9 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>1</sup> | 248.998 |
| Ca | Ca_sv_GW | 10 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>2</sup> | 281.43 |
| Sc | Sc_sv_GW | 11 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>3</sup> | 378.961 |
| Ti | Ti_sv_GW | 12 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>4</sup> | 383.774 |
| V | V_sv_GW | 13 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>5</sup> | 382.321 |
| Cr | Cr_sv_GW | 14 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>6</sup> | 384.932 |
| Mn | Mn_sv_GW | 15 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>7</sup> | 384.627 |
| Fe | Fe_sv_GW | 16 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>8</sup> | 387.837 |
| Co | Co_sv_GW | 17 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>9</sup> | 387.491 |
| Ni | Ni_sv_GW | 18 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> | 389.645 |
| Cu | Cu_sv_GW | 19 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>1</sup> | 467.331 |
| Zn | Zn_sv_GW | 20 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> | 401.665 |
| Ga | Ga_d_GW | 13 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 404.602 |
| Ge | Ge_d_GW | 14 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 375.434 |
| As | As_GW | 5 | 4*s*<sup>2</sup> 4*p*<sup>3</sup> | 208.702 |
| Se | Se_GW | 6 | 4*s*<sup>2</sup> 4*p*<sup>4</sup> | 211.555 |
| Br | Br_GW | 7 | 4*s*<sup>2</sup> 4*p*<sup>5</sup> | 216.285 |
| Kr | Kr_GW | 8 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> | 252.232 |
| Rb | Rb_sv_GW | 9 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>1</sup> | 221.197 |
| Sr | Sr_sv_GW | 10 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>2</sup> | 224.817 |
| Y | Y_sv_GW | 11 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>3</sup> | 339.758 |
| Zr | Zr_sv_GW | 12 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>4</sup> | 346.364 |
| Nb | Nb_sv_GW | 13 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>5</sup> | 353.872 |
| Mo | Mo_sv_GW | 14 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>6</sup> | 344.914 |
| Tc | Tc_sv_GW | 15 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>7</sup> | 351.044 |
| Ru | Ru_sv_GW | 16 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>8</sup> | 348.106 |
| Rh | Rh_sv_GW | 17 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>9</sup> | 351.206 |
| Pd | Pd_sv_GW | 18 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> | 356.093 |
| Ag | Ag_sv_GW | 19 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>11</sup> | 354.43 |
| Cd | Cd_sv_GW | 20 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> | 361.806 |
| In | In_d_GW | 13 | 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup> | 278.624 |
| Sn | Sn_d_GW | 14 | 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup> | 260.066 |
| Sb | Sb_d_GW | 15 | 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>3</sup> | 263.1 |
| Te | Te_GW | 6 | 5*s*<sup>2</sup> 5*p*<sup>4</sup> | 174.982 |
| I | I_GW | 7 | 5*s*<sup>2</sup> 5*p*<sup>5</sup> | 175.647 |
| Xe | Xe_GW | 8 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> | 179.547 |
| Cs | Cs_sv_GW | 9 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> | 198.101 |
| Ba | Ba_sv_GW | 10 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>1</sup> | 267.02 |
| La | La_GW | 11 | 4*f*<sup>0.2</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.8</sup> 6*s*<sup>2</sup> | 313.688 |
| Ce | Ce_GW | 12 | 4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 304.625 |
| Pr | Pr_h | 13 | 4*f*<sup>2.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 400.742 |
| Nd | Nd_h | 14 | 4*f*<sup>3.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 402.016 |
| Pm | Pm_h | 15 | 4*f*<sup>4.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 404.406 |
| Sm | Sm_h | 16 | 4*f*<sup>5.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 405.382 |
| Eu | Eu_h | 17 | 4*f*<sup>6.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 403.212 |
| Gd | Gd_h | 18 | 4*f*<sup>7.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 407.403 |
| Tb | Tb_h | 19 | 4*f*<sup>8.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 405.043 |
| Dy | Dy_h | 20 | 4*f*<sup>9.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 405.886 |
| Ho | Ho_h | 21 | 4*f*<sup>10.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 415.91 |
| Er | Er_h | 22 | 4*f*<sup>11.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 429.583 |
| Tm | Tm_h | 23 | 4*f*<sup>12.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 419.812 |
| Yb | Yb_h | 24 | 4*f*<sup>13.5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.5</sup> 6*s*<sup>2</sup> | 409.285 |
| Lu | Lu | 25 | 4*f*<sup>14</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 255.695 |
| Hf | Hf_sv_GW | 12 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>4</sup> | 309.037 |
| Ta | Ta_sv_GW | 13 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>5</sup> | 286.008 |
| W | W_sv_GW | 14 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>6</sup> | 317.132 |
| Re | Re_sv_GW | 15 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>7</sup> | 317.012 |
| Os | Os_sv_GW | 16 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>8</sup> | 319.773 |
| Ir | Ir_sv_GW | 17 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>9</sup> | 319.843 |
| Pt | Pt_sv_GW | 18 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> | 323.669 |
| Au | Au_sv_GW | 19 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>11</sup> | 306.658 |
| Hg | Hg_sv_GW | 20 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> | 312.028 |
| Tl | Tl_d_GW | 15 | 5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>1</sup> | 237.053 |
| Pb | Pb_d_GW | 16 | 5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup> | 237.809 |
| Bi | Bi_d_GW | 17 | 5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 261.876 |
| Po | Po_d_GW | 18 | 5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>4</sup> | 267.847 |
| At | At_d_GW | 17 | 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>5</sup> | 266.251 |
| Rn | Rn_d_GW | 18 | 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> | 267.347 |
| Fr | Fr_sv | 9 | 6*s*<sup>2</sup> 6*p*<sup>6</sup> 7*s*<sup>1</sup> | 214.54 |
| Ra | Ra_sv | 10 | 6*s*<sup>2</sup> 6*p*<sup>6</sup> 7*s*<sup>2</sup> | 237.367 |
| Ac | Ac | 11 | 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>1</sup> 7*s*<sup>2</sup> | 172.351 |
| Th | Th | 12 | 5*f*<sup>1</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>1</sup> 7*s*<sup>2</sup> | 247.306 |
| Pa | Pa | 13 | 5*f*<sup>1</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 252.193 |
| U | U | 14 | 5*f*<sup>2</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 252.502 |
| Np | Np | 15 | 5*f*<sup>3</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 254.26 |
| Pu | Pu | 16 | 5*f*<sup>4</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 254.353 |
| Am | Am | 17 | 5*f*<sup>5</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 255.875 |
| Cm | Cm | 18 | 5*f*<sup>6</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 257.953 |

### Selecting the release version\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Selecting the release version">edit</a> \| (./index.php.md)\]

Generally, we recommend using the latest release of pseudopotentials.

|  |
|----|
| **Tip:** For compatibility reasons or to accurately reproduce another calculation, you might need to use another (older) pseudopotential release. Consult the list of [available pseudopotentials](../input-files/Available_pseudopotentials.md). |

### Element-specific recommendation\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Element-specific recommendation">edit</a> \| (./index.php.md)\]

#### Hydrogen-like atoms with fractional valence\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Hydrogen-like atoms with fractional valence">edit</a> \| (./index.php.md)\]

Twelve hydrogen-like potentials are supplied for a valency between 0.25
and 1.75. Further potentials might become available, c.f. [available
pseudopotentials](../input-files/Available_pseudopotentials.md).
These are useful, e.g., to passivate dangling surface bonds.

|  |
|----|
| **Mind:** The [POTCAR](../input-files/POTCAR.md) files restrict the number of digits for the valency (typically 2, at most 3 digits). Therefor, using three H.33 potentials does yield 0.99 electrons and not 1.00 electron. This can cause undesirable hole- or electron-like states. Set the [NELECT](../incar-tags/NELECT.md) tag in the [INCAR](../input-files/INCAR.md) file to correct the total number of electrons. |

#### First-row elements\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: First-row elements">edit</a> \| (./index.php.md)\]

For the 1st row elements B, C, N, O, and F, three potential versions
exist, the plain one, a hard version, and a soft version. For most
purposes, the standard version of PAW potentials is most appropriate.
They yield reliable results for energy cutoffs between 325 and 400 eV,
where 370-400 eV are required to predict vibrational properties
accurately. Binding geometries and energy differences are already well
reproduced at 325 eV. The typical bond-length errors for first row
dimers (N<sub>2</sub>, CO, O<sub>2</sub>) are about 1% compared to more
accurate DFT calculations. The [hard pseudopotentials
(\_h)](../input-files/Available_pseudopotentials.md)
give results that are essentially identical to the best DFT calculations
presently available (FLAPW, or Gaussian with very large basis sets). The
[soft potentials
(\_s)](../input-files/Available_pseudopotentials.md)
are optimized to work around 250-280 eV. They yield reliable description
for most oxides, such as V<sub>x</sub>O<sub>y</sub>, TiO<sub>2</sub>,
CeO<sub>2</sub>, but fail to describe some structural details in
zeolites, i.e., cell parameters, and volume.

For Hartree-Fock (HF) and hybrid-functional calculations, we strictly
recommend using the standard, standard GW, or hard potentials. For
instance, the O_s potential can cause unacceptably large errors even in
transition metal oxides. Generally, the soft potentials are less
transferable from one exchange-correlation functional to another and
often fail when the exact exchange needs to be calculated.

|  |
|----|
| **Tip:** If dimers with short bonds are present in the system (H<sub>2</sub>O, O<sub>2</sub>, CO, N<sub>2</sub>, F<sub>2</sub>, P<sub>2</sub>, S<sub>2</sub>, Cl<sub>2</sub>), we recommend using the \_h potentials. Specifically, C_h, O_h, N_h, F_h, P_h, S_h, Cl_h, or their \_GW counterparts. Otherwise, the standard version is often the best choice for first-row elements. |

#### Alkali and alkali-earth elements (simple metals)\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Alkali and alkali-earth elements (simple metals)">edit</a> \| (./index.php.md)")\]

For Li (and Be), a standard potential and a potential that treats the
1*s* shell as valence states are available (Li_sv, Be_sv). One should
use the \_sv potentials for many applications since their
transferability is much higher than the standard potentials.

For the other alkali and alkali-earth elements, the semi-core *s* and
*p* states should be treated as valence states as well. For lighter
elements (Na-Ca), it is usually sufficient to treat the 2*p* and 3*p*
states as valence states (\_pv), respectively. For Rb-Sr, the 4*s*,
4*p*, and 5*s*, 5*p* states, must be treated as valence states (\_sv).

|  |
|----|
| **Tip:** For alkali and alkali-earth metals, the \_sv variants should be chosen, other than for very light elements Na, Mg, K, and Ca, where \_pv is usually sufficient. |

#### p-elements\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: p-elements">edit</a> \| (./index.php.md)\]

For Ga, Ge, In, Sn, Tl-At, the lower-lying *d* states should be treated
as valence states (\_d potential). For these elements, alternative
potentials that treat the *d* states as core states are also available
but should be used with great care.

#### d-elements\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: d-elements">edit</a> \| (./index.php.md)\]

For the *d* elements, applies the same as for the alkali and
earth-alkali metals: the semi-core *p* states and possibly the semi-core
*s* states should be treated as valence states. In most cases, however,
reliable results can be obtained even if the semi-core states are kept
frozen.

When to switch from X_pv potentials to the X potentials depends on the
required accuracy and the row for the 3*d* elements, even the Ti, V, and
Cr potentials give reasonable results but should be used with uttermost
care. 4*d* elements are the most problematic, and we advise using the
X_pv potentials up to Tc_pv. For 5*d* elements the 5*p* states are
rather strongly localized (below 3 Ry), since the 4*f* shell becomes
filled. One can use the standard potentials starting from Hf, but we
recommend performing test calculations. For some elements, X_sv
potentials are available (,e.g., Nb_sv, Mo_sv, Hf_sv). These potentials
usually have very similar energy cutoffs as the \_pv potentials and can
also be used. For HF-type and hybrid-functional calculations, we
strongly recommend using the [\_sv and
\_pv](../input-files/Available_pseudopotentials.md)
potentials whenever possible.

|  |
|----|
| **Tip:** As a rule of thumb the *p* states should be treated as valence states for d-elements, if their eigenenergy $\epsilon$ lies above 3 Ry. |

#### f-elements\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: f-elements">edit</a> \| (./index.php.md)\]

Due to self-interaction errors, *f* electrons are not handled well by
the presently available density functionals. In particular, partially
filled *f* states are often incorrectly described. For instance, all *f*
states are pinned at the Fermi-level, leading to large overbinding for
Pr-Eu and Tb-Yb. The errors are largest at quarter and three-quarter
filling, e.g., Gd is handled reasonably well since 7 electrons occupy
the majority *f* shell. These errors are DFT and not VASP related.

Particularly problematic is the description of the transition from an
itinerant (band-like) behavior observed at the beginning of each period
to localized states towards the end of the period. For the 4*f*
elements, this transition occurs already in La and Ce, whereas the
transition sets in for Pu and Am for the 5*f* elements. A routine way to
cope with the inabilities of present DFT functionals to describe the
localized 4*f* electrons is to place the 4*f* electrons in the core.
Such potentials are available and described below; however, they are
expected to fail to describe magnetic properties arising *f* orbitals.
Furthermore, PAW potentials in which the *f* states are treated as
valence states are available, but these potentials are expected to fail
to describe electronic properties when *f* electrons are localized. In
this case, one might treat electronic correlation effects more
carefully, e.g., by employing hybrid functionals or introducing on-site
Coulomb interaction.

For some elements, [soft versions
(\_s)](../input-files/Available_pseudopotentials.md)
are available as well. The semi-core *p* states are always treated as
valence states, whereas the semi-core *s* states are treated as valence
states only in the standard potentials. For most applications (oxides,
sulfides), the standard version should be used since the soft versions
might result in *s* ghost-states close to the Fermi-level (,e.g., Ce_s
in ceria). The soft versions are, however, expected to be sufficiently
accurate for calculations on intermetallic compounds.

##### Lanthanides with fixed valence\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: Lanthanides with fixed valence">edit</a> \| (./index.php.md)\]

In addition, special GGA potentials are supplied for Ce-Lu, in which *f*
electrons are kept frozen in the core, which is an attempt to treat the
localized nature of *f* electrons. The number of f electrons in the core
equals the total number of valence electrons minus the formal valency.
For instance, according to the periodic table, Sm has a total of 8
valence electrons, i.e., 6 *f* electrons and 2 *s* electrons. In most
compounds, Sm adopts a valency of 3; hence 5 *f* electrons are placed in
the core when the pseudopotential is generated. The corresponding
potential can be found in the directory Sm_3. The formal valency n is
indicted by \_n, where n is either 3 or 2. Ce_3 is, for instance, a Ce
potential for trivalent Ce (for tetravalent Ce, the standard potential
should be used).

|  |
|----|
| **Warning:** *f*-elements are notoriously hard to describe with DFT due to self-interaction errors in the strongly localized orbitals. Placing some, or all, 4*f* electrons in the core can rectify this issue, but then the description of magnetism will fail and transferability will suffer. |

|  |
|----|
| **Tip:** If you are not interested in 4*f*-magnetism, and know the valency of your lanthanide, use the \_2 or \_3 potentials. |

  

|  |
|----|
| **Important:** Even if you have taken a lot of care to optimize your pseudopotential choice, it is always good to perform some test calculations with other potentials, if necessary, on a small prototype system. You might realize that you need extra accuracy, or that you are leaving performance on the table by using unnecessarily hard [POTCARs](../input-files/POTCAR.md) for your problem. |

## Example: NiO equilibrium volume\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: Example: NiO equilibrium volume">edit</a> \| (./index.php.md)\]

Antiferromagnetic NiO in the rocksalt structure is a prototype system
for a correlated material. It is a Mott insulator and not well described
with standard DFT. To get correct material properties, methods beyond
DFT are required. [DFT+DMFT
calculations](DFT+DMFT_calculations.md) are
an option, but the much cheaper
<a href="/wiki/DFT%2BU" class="mw-redirect" title="DFT+U">DFT+U</a>
approach is often used with satisfactory results.

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:NiO_diff_pots_energy_vs_volume.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/4/46/NiO_diff_pots_energy_vs_volume.png/450px-NiO_diff_pots_energy_vs_volume.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/4/46/NiO_diff_pots_energy_vs_volume.png/675px-NiO_diff_pots_energy_vs_volume.png 1.5x, /wiki/images/thumb/4/46/NiO_diff_pots_energy_vs_volume.png/900px-NiO_diff_pots_energy_vs_volume.png 2x"
width="450" height="338" /></a>
<figcaption>Fig 1. LSDA+U Energy vs. volume plot for AFM NiO. Different
Ni potentials were used to create the data. All other inputs are
equivalent. The all-electron (AE) reference was calculated with
Wien2K.</figcaption>
</figure>

The computational setup and how to interpret the results of a DFT+U
calculation for NiO are given in the section on [NiO
LSDA+U](../misc/NiO_LSDA+U.md). Here, we will focus on the
effect of the choice of the Ni pseudopotential on the equation of state
(EOS). We compare the results to reference Wien2K
calculations<sup>[\[3\]](#cite_note-tran:prb:2006-3)</sup>,
which do not use pseudopotentials, as Wien2K is an all-electron (AE)
code<sup>[\[4\]](#cite_note-blaha:2020-4)</sup>.

The Ni, Ni_pv, and Ni_sv_GW pseudopotentials of the
[potpaw_PBE.64](../input-files/Available_pseudopotentials.md) "Available pseudopotentials")
set were combined with the O pseudopotential for all calculations. The
plane-wave cutoff energy [ENCUT](../incar-tags/ENCUT.md) was set to 1000 eV
to avoid any influence of basis set convergence.

Fig. 1 shows the data for all three Ni POTCAR options and the AE
reference as a black line. The standard Ni potential, which is the one
usually recommended for calculations that do not need a high number of
unoccupied bands, is underestimating the equilibrium volume by 6%, which
translates to a lattice parameter of 4.04 Å. Taking the semi-core
3*p*-states into account with the Ni_pv potential improves the results
significantly, with the volume underestimation reduced to 1.7% and
increasing the lattice parameter to 4.10 Å. If we want to also take the
semicore 3*s*-states into account, we need to choose a
[\_GW](../input-files/Available_pseudopotentials.md)
potential, Ni_sv_GW. The inclusion of the *s*-states improves the EOS
further, with the underestimation of the volume now being only 0.2% and
the lattice parameter matching the AE reference to two significant
digits at 4.12 Å.

It is worth noting that the semicore 3*p*-, and the 3*s*-states, are
only important for the equilibrium volume if the L(S)DA+U method is
used. If no Hubbard corrections are used, all three tested Ni
pseudopotentials give a lattice parameter of 4.06 Å, which is very close
to the 4.07 Å of the AE reference.

However, the large value of U=8 eV applied to the Ni 4*d*-states in our
calculations pushes the *d*-states away from the Fermi level and
compresses them. If the *p* (or, better, the *sp*) orbitals are in the
valence, they can hybridize with the *d*-states and expand, increasing
the lattice parameter. (This process happens equivalently in a [DFT+DMFT
calculation](DFT+DMFT_calculations.md) of
NiO.) In fact, the expected linear increase of the lattice parameter
with increasing U value is only observed correctly if the Ni_sv_GW
potential is used. Note that the lattice parameter predicted by the Ni
PAW potential for U=8 eV, at 4.04 Å, is actually lower than the 4.06 Å
predicted without the U, because the *d*-states are still compressed,
but the frozen *s*- and *p*-states cannot expand accordingly.

## Related tags and sections\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[POTCAR](../input-files/POTCAR.md),
<a href="/wiki/Prepare_a_POTCAR" class="mw-redirect"
title="Prepare a POTCAR">Prepare a POTCAR</a>, [Available
pseudopotentials](../input-files/Available_pseudopotentials.md)

Theoretical background:
<a href="/wiki/Pseudopotentials" class="mw-redirect"
title="Pseudopotentials">Pseudopotentials</a>, [Projector-augmented-wave
formalism](../methods/Projector-augmented-wave_formalism.md)

## References\[<a
href="/wiki/index.php?title=Choosing_pseudopotentials&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-bosoni:natphysrev:2023_1-0)
    <a href="https://doi.org/10.1038/s42254-023-00655-3"
    class="external text" rel="nofollow">Emanuele Bosoni, Louis Beal, Marnik
    Bercx, Peter Blaha, Stefan Blügel, Jens Bröder, Martin Callsen, Stefaan
    Cottenier, Augustin Degomme, Vladimir Dikan, Kristjan Eimre, Espen
    Flage-Larsen, Marco Fornari, Alberto Garcia, Luigi Genovese, Matteo
    Giantomassi, Sebastiaan P. Huber, Henning Janssen, Georg Kastlunger,
    Matthias Krack, Georg Kresse, Thomas D. Kühne, Kurt Lejaeghere, Georg K.
    H. Madsen, Martijn Marsman, Nicola Marzari, Gregor Michalicek, Hossein
    Mirhosseini, Tiziano M. A. Müller, Guido Petretto, Chris J. Pickard,
    Samuel Poncé, Gian-Marco Rignanese, Oleg Rubel, Thomas Ruh, Michael
    Sluydts, Danny E. P. Vanpoucke, Sudarshan Vijay, Michael Wolloch, Daniel
    Wortmann, Aliaksandr V. Yakutovich, Jusong Yu, Austin Zadoks, Bonan Zhu,
    Giovanni Pizzi, <em>How to verify the precision of
    density-functional-theory implementations via reproducible and universal
    workflows</em>, Nat Rev Phys 6, 45–58 (2024).</a>
2.  [↑](#cite_ref-2)
    For the potpaw_PBE.64 potential set,
    <a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> is
    on average ~26 eV (~11%) and [EAUG](../incar-tags/EAUG.md) ~210 eV
    (~42%) larger for the GW potentials compared to their standard
    counterparts with the same valency.
3.  [↑](#cite_ref-tran:prb:2006_3-0)
    <a href="https://doi.org/10.1103/PhysRevB.74.155108"
    class="external text" rel="nofollow">F. Tran, P. Blaha, and K. Schwarz,
    <em>Hybrid exchange-correlation energy functionals for strongly
    correlated electrons: Applications to transition-metal monoxides</em>,
    Phys. Rev. B <strong>74</strong>, 155108 (2006).</a>
4.  [↑](#cite_ref-blaha:2020_4-0)
    <a href="https://doi.org/10.1063/1.5143061" class="external text"
    rel="nofollow">P. Blaha, K. Schwarz. F. Tran, R. Laskowski, G. K. H.
    Madsen, and L. D. Marks, <em>WIEN2k: An APW+lo program for calculating
    the properties of solids</em>, J. Chem. Phys. <strong>152</strong>,
    074101 (2020).</a>


