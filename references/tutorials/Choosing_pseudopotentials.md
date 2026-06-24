<!-- Source: https://vasp.at/wiki/index.php/Choosing_pseudopotentials | revid: 34876 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Choosing pseudopotentials
Several [pseudopotential variants labeled by
suffixes](../input-files/Available_pseudopotentials.md)
exist for many elements. When making a choice, it is necessary to
balance computational cost, accuracy, and transferability.

- To set up a minimal working example of your calculation, follow
  [prepare a POTCAR](../redirects/Prepare_a_POTCAR.md).
- Try to create a smaller test calculation and perform your own tests to
  confirm if the quantity of interest is sensitive to the choice of the
  pseudopotential. It might be possible to opt for a computationally
  cheaper [POTCAR](../input-files/POTCAR.md) and gain performance. On the
  other hand, it could be necessary to opt for a computationally
  demanding setup to obtain correct results.
- With the [aspects described in the next
  section](#Aspects_to_refine_the_choice_of_pseudopotentials) in mind,
  carefully look over the [recommendations for each group in the
  periodic table](#Recommendations_and_advice).

## Contents

- [1 Aspects to refine the choice of
  pseudopotentials](#Aspects_to_refine_the_choice_of_pseudopotentials)
- [2 Recommendations and advice](#Recommendations_and_advice)
  - [2.1 Recommended PAW potentials](#Recommended_PAW_potentials)
    - [2.1.1 Standard DFT without the need for many unoccupied
      states](#Standard_DFT_without_the_need_for_many_unoccupied_states)
    - [2.1.2 Calculation requiring a large number of unoccupied
      states](#Calculation_requiring_a_large_number_of_unoccupied_states)
    - [2.1.3 Reference calculation; extremely high
      accuracy](#Reference_calculation;_extremely_high_accuracy)
  - [2.2 Selecting the release version](#Selecting_the_release_version)
  - [2.3 Element-specific
    recommendation](#Element-specific_recommendation)
    - [2.3.1 Hydrogen-like atoms with fractional
      valence](#Hydrogen-like_atoms_with_fractional_valence)
    - [2.3.2 First-row elements](#First-row_elements)
    - [2.3.3 Alkali and alkali-earth elements (simple
      metals)](#Alkali_and_alkali-earth_elements_(simple_metals))
    - [2.3.4 p-elements](#p-elements)
    - [2.3.5 d-elements](#d-elements)
    - [2.3.6 f-elements](#f-elements)
      - [2.3.6.1 Lanthanides with fixed
        valence](#Lanthanides_with_fixed_valence)
- [3 Example: NiO equilibrium volume](#Example:_NiO_equilibrium_volume)
- [4 Related tags and sections](#Related_tags_and_sections)
- [5 References](#References)

## Aspects to refine the choice of pseudopotentials
**Aspect 1:** The bond lengths and the valency of the ions.

Short bonds will require harder potentials, and semicore states might
have to be treated as valence for certain chemical bonding. For some
elements, variants for specific valency exist; for example, the suffix
[\_2 or
\_3](../input-files/Available_pseudopotentials.md)
can be used to describe [fixed divalent or trivalent
Lanthanides](#Lanthanides_with_fixed_valence).

**Aspect 2:** The physical or chemical property of interest.

If you are only interested in a rough [structure
optimization](../redirects/Ionic_minimization.md), soft
potentials
([\_s](../input-files/Available_pseudopotentials.md))
with minimal valency may suffice. This approach might also work for
[phonon calculations](../redirects/Phonons.md) that rely on large
supercells.

On the other hand, when optimizing a magnetic structure, it may be
necessary to include semicore states in the valence ([\_pv and
\_sv](../input-files/Available_pseudopotentials.md)).

For the computation of [optical
properties](../redirects/Optical_properties.md), it is
crucial to use [GW
potentials](../input-files/Available_pseudopotentials.md).

**Aspect 3:** The method or algorithm used in your calculation.

For any calculation involving unoccupied states significantly above the
Fermi energy, the [\_GW
variants](../input-files/Available_pseudopotentials.md)
of potentials are superior and should be used. Particularly, all kinds
of [calculations within many-body perturbation
theory](../redirects/Many-body_perturbation_theory.md)
need a high number of [empty
bands](../incar-tags/NBANDS.md).
Therefore, when GW, BSE, etc. is performed, the [GW
potentials](../input-files/Available_pseudopotentials.md)
should be used throughout the workflow.

[Hartree-Fock and hybrid
caluclations](../redirects/Hybrid_functionals.md) should
*not* be performed with soft potentials
([\_s](../input-files/Available_pseudopotentials.md)).
Moreover, any calculations where you switch the [exchange-correlation
functional](../redirects/Exchange-correlation_functional.md)
should *not* be performed with soft potentials
([\_s](../input-files/Available_pseudopotentials.md)).

For standard DFT-ground-state calculations, using [\_GW or
\_h](../input-files/Available_pseudopotentials.md)
potentials is usually unnecessary unless, e.g., the property of interest
or geometry of the structure demands it.

## Recommendations and advice
### Recommended PAW potentials
#### Standard DFT without the need for many unoccupied states
The table directly below highlights recommended PAW potentials in
**bold**.

These potentials are *not ideal* for calculations involving a large
number of excited states as needed, e.g., for [optical
properties](../redirects/Optical_properties.md) or [many-body
perturbation
theory](../redirects/Many-body_perturbation_theory.md).

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| Standard PBE potentials (potpaw.64) |  |  |  |
| Potential name | Number of valence electrons | Valence electron configuration | ENAMX \[eV\] |
| **H** | **1** | **1*s*¹** | **250.0** |
| H.25 | 0.25 | 1*s*^(0.25) | 250.0 |
| H.33 | 0.33 | 1*s*^(0.33) | 250.0 |
| H.42 | 0.42 | 1*s*^(0.42) | 250.0 |
| H.5 | 0.5 | 1*s*^(0.5) | 250.0 |
| H.58 | 0.58 | 1*s*^(0.58) | 250.0 |
| H.66 | 0.66 | 1*s*^(0.66) | 250.0 |
| H.75 | 0.75 | 1*s*^(0.75) | 250.0 |
| H1.25 | 1.25 | 1*s*^(1.25) | 250.0 |
| H1.33 | 1.33 | 1*s*^(1.33) | 250.0 |
| H1.5 | 1.5 | 1*s*^(1.5) | 250.0 |
| H1.66 | 1.66 | 1*s*^(1.66) | 250.0 |
| H1.75 | 1.75 | 1*s*^(1.75) | 250.0 |
| H_AE | 1 | 1*s*¹ | 1000.0 |
| H_h | 1 | 1*s*¹ | 700.0 |
| H_s | 1 | 1*s*¹ | 200.0 |
| **He** | **2** | **1*s*²** | **478.896** |
| He_AE | 2 | 1*s*² | 2135.871 |
| Li | 1 | 2*s*¹ | 140.0 |
| **Li_sv** | **3** | **1*s*² 2*s*¹** | **499.034** |
| **Be** | **2** | **2*s*^(1.99) 2*p*^(0.01)** | **247.543** |
| Be_sv | 4 | 1*s*² 2*s*^(1.99) 2*p*^(0.01) | 308.768 |
| **B** | **3** | **2*s*² 2*p*¹** | **318.614** |
| B_h | 3 | 2*s*² 2*p*¹ | 700.0 |
| B_s | 3 | 2*s*² 2*p*¹ | 269.245 |
| **C** | **4** | **2*s*² 2*p*²** | **400.0** |
| C_h | 4 | 2*s*² 2*p*² | 741.689 |
| C_s | 4 | 2*s*² 2*p*² | 273.911 |
| **N** | **5** | **2*s*² 2*p*³** | **400.0** |
| N_h | 5 | 2*s*² 2*p*³ | 755.582 |
| N_s | 5 | 2*s*² 2*p*³ | 279.692 |
| **O** | **6** | **2*s*² 2*p*⁴** | **400.0** |
| O_h | 6 | 2*s*² 2*p*⁴ | 765.519 |
| O_s | 6 | 2*s*² 2*p*⁴ | 282.853 |
| **F** | **7** | **2*s*² 2*p*⁵** | **400.0** |
| F_h | 7 | 2*s*² 2*p*⁵ | 772.626 |
| F_s | 7 | 2*s*² 2*p*⁵ | 289.837 |
| **Ne** | **8** | **2*s*² 2*p*⁶** | **343.606** |
| Na | 1 | 3*s*¹ | 101.968 |
| **Na_pv** | **7** | **2*p*⁶ 3*s*¹** | **259.561** |
| Na_sv | 9 | 2*s*² 2*p*⁶ 3*s*¹ | 645.64 |
| **Mg** | **2** | **3*s*²** | **200.0** |
| Mg_pv | 8 | 2*p*⁶ 3*s*² | 403.929 |
| Mg_sv | 10 | 2*s*² 2*p*⁶ 3*s*² | 495.223 |
| **Al** | **3** | **3*s*² 3*p*¹** | **240.3** |
| **Si** | **4** | **3*s*² 3*p*²** | **245.345** |
| **P** | **5** | **3*s*² 3*p*³** | **255.04** |
| P_h | 5 | 3*s*² 3*p*³ | 390.202 |
| **S** | **6** | **3*s*² 3*p*⁴** | **258.689** |
| S_h | 6 | 3*s*² 3*p*⁴ | 402.436 |
| **Cl** | **7** | **3*s*² 3*p*⁵** | **262.472** |
| Cl_h | 7 | 3*s*² 3*p*⁵ | 409.136 |
| **Ar** | **8** | **3*s*² 3*p*⁶** | **266.408** |
| K_pv | 7 | 3*p*⁶ 4*s*¹ | 116.731 |
| **K_sv** | **9** | **3*s*² 3*p*⁶ 4*s*¹** | **259.264** |
| Ca_pv | 8 | 3*p*⁶ 4*s*² | 119.559 |
| **Ca_sv** | **10** | **3*s*² 3*p*⁶ 4*s*²** | **266.622** |
| Sc | 3 | 3*d*² 4*s*¹ | 154.763 |
| **Sc_sv** | **11** | **3*s*² 3*p*⁶ 3*d*² 4*s*¹** | **222.66** |
| Ti | 4 | 3*d*³ 4*s*¹ | 178.33 |
| Ti_pv | 10 | 3*p*⁶ 3*d*³ 4*s*¹ | 222.335 |
| **Ti_sv** | **12** | **3*s*² 3*p*⁶ 3*d*³ 4*s*¹** | **274.61** |
| V | 5 | 3*d*⁴ 4*s*¹ | 192.543 |
| V_pv | 11 | 3*p*⁶ 3*d*⁴ 4*s*¹ | 263.673 |
| **V_sv** | **13** | **3*s*² 3*p*⁶ 3*d*⁴ 4*s*¹** | **263.673** |
| Cr | 6 | 3*d*⁵ 4*s*¹ | 227.08 |
| **Cr_pv** | **12** | **3*p*⁶ 3*d*⁵ 4*s*¹** | **265.681** |
| Cr_sv | 14 | 3*s*² 3*p*⁶ 3*d*⁵ 4*s*¹ | 395.471 |
| Mn | 7 | 3*d*⁶ 4*s*¹ | 269.864 |
| **Mn_pv** | **13** | **3*p*⁶ 3*d*⁶ 4*s*¹** | **269.864** |
| Mn_sv | 15 | 3*s*² 3*p*⁶ 3*d*⁶ 4*s*¹ | 387.187 |
| **Fe** | **8** | **3*d*⁷ 4*s*¹** | **267.882** |
| Fe_pv | 14 | 3*p*⁶ 3*d*⁷ 4*s*¹ | 293.238 |
| Fe_sv | 16 | 3*s*² 3*p*⁶ 3*d*⁷ 4*s*¹ | 390.558 |
| **Co** | **9** | **3*d*⁸ 4*s*¹** | **267.968** |
| Co_pv | 15 | 3*p*⁶ 3*d*⁸ 4*s*¹ | 271.042 |
| Co_sv | 17 | 3*s*² 3*p*⁶ 3*d*⁸ 4*s*¹ | 390.362 |
| **Ni** | **10** | **3*d*⁹ 4*s*¹** | **269.532** |
| Ni_pv | 16 | 3*p*⁶ 3*d*⁹ 4*s*¹ | 367.986 |
| **Cu** | **11** | **3*d*¹⁰ 4*s*¹** | **295.446** |
| Cu_pv | 17 | 3*p*⁶ 3*d*¹⁰ 4*s*¹ | 368.648 |
| **Zn** | **12** | **3*d*¹⁰ 4*s*²** | **276.723** |
| Ga | 3 | 4*s*² 4*p*¹ | 134.678 |
| **Ga_d** | **13** | **3*d*¹⁰ 4*s*² 4*p*¹** | **282.691** |
| Ga_h | 13 | 3*d*¹⁰ 4*s*² 4*p*¹ | 404.601 |
| Ge | 4 | 4*s*² 4*p*² | 173.807 |
| **Ge_d** | **14** | **3*d*¹⁰ 4*s*² 4*p*²** | **310.294** |
| Ge_h | 14 | 3*d*¹⁰ 4*s*² 4*p*² | 410.425 |
| **As** | **5** | **4*s*² 4*p*³** | **208.702** |
| As_d | 15 | 3*d*¹⁰ 4*s*² 4*p*³ | 288.651 |
| **Se** | **6** | **4*s*² 4*p*⁴** | **211.555** |
| **Br** | **7** | **4*s*² 4*p*⁵** | **216.285** |
| **Kr** | **8** | **4*s*² 4*p*⁶** | **185.331** |
| Rb_pv | 7 | 4*p*⁶ 4*d*^(0.001) 5*s*^(0.999) | 121.882 |
| **Rb_sv** | **9** | **4*s*² 4*p*⁶ 4*d*^(0.001) 5*s*^(0.999)** | **220.112** |
| **Sr_sv** | **10** | **4*s*² 4*p*⁶ 4*d*^(0.001) 5*s*^(1.999)** | **229.353** |
| **Y_sv** | **11** | **4*s*² 4*p*⁶ 4*d*² 5*s*¹** | **202.626** |
| **Zr_sv** | **12** | **4*s*² 4*p*⁶ 4*d*³ 5*s*¹** | **229.898** |
| Nb_pv | 11 | 4*p*⁶ 4*d*⁴ 5*s*¹ | 208.608 |
| **Nb_sv** | **13** | **4*s*² 4*p*⁶ 4*d*⁴ 5*s*¹** | **293.235** |
| Mo | 6 | 4*d*⁵ 5*s*¹ | 224.584 |
| Mo_pv | 12 | 4*p*⁶ 4*d*⁵ 5*s*¹ | 224.584 |
| **Mo_sv** | **14** | **4*s*² 4*p*⁶ 4*d*⁵ 5*s*¹** | **242.676** |
| Tc | 7 | 4*d*⁶ 5*s*¹ | 228.694 |
| **Tc_pv** | **13** | **4*p*⁶ 4*d*⁶ 5*s*¹** | **263.523** |
| Tc_sv | 15 | 4*s*² 4*p*⁶ 4*d*⁶ 5*s*¹ | 318.703 |
| Ru | 8 | 4*d*⁷ 5*s*¹ | 213.271 |
| **Ru_pv** | **14** | **4*p*⁶ 4*d*⁷ 5*s*¹** | **240.049** |
| Ru_sv | 16 | 4*s*² 4*p*⁶ 4*d*⁷ 5*s*¹ | 318.855 |
| Rh | 9 | 4*d*⁸ 5*s*¹ | 228.996 |
| **Rh_pv** | **15** | **4*p*⁶ 4*d*⁸ 5*s*¹** | **247.408** |
| **Pd** | **10** | **4*d*⁹ 5*s*¹** | **250.925** |
| Pd_pv | 16 | 4*p*⁶ 4*d*⁹ 5*s*¹ | 250.925 |
| **Ag** | **11** | **4*d*¹⁰ 5*s*¹** | **249.844** |
| Ag_pv | 17 | 4*p*⁶ 4*d*¹⁰ 5*s*¹ | 297.865 |
| **Cd** | **12** | **4*d*¹⁰ 5*s*²** | **274.336** |
| In | 3 | 5*s*² 5*p*¹ | 95.934 |
| **In_d** | **13** | **4*d*¹⁰ 5*s*² 5*p*¹** | **239.211** |
| Sn | 4 | 5*s*² 5*p*² | 103.236 |
| **Sn_d** | **14** | **4*d*¹⁰ 5*s*² 5*p*²** | **241.083** |
| **Sb** | **5** | **5*s*² 5*p*³** | **172.069** |
| **Te** | **6** | **5*s*² 5*p*⁴** | **174.982** |
| **I** | **7** | **5*s*² 5*p*⁵** | **175.647** |
| **Xe** | **8** | **5*s*² 5*p*⁶** | **153.118** |
| **Cs_sv** | **9** | **5*s*² 5*p*⁶ 6*s*¹** | **220.318** |
| **Ba_sv** | **10** | **5*s*² 5*p*⁶ 5*d*^(0.01) 6*s*^(1.99)** | **187.181** |
| **La** | **11** | **4*f*^(0.0001) 5*s*² 5*p*⁶ 5*d*^(0.9999) 6*s*²** | **219.292** |
| La_s | 9 | 5*p*⁶ 5*d*¹ 6*s*² | 136.53 |
| **Ce** | **12** | **4*f*¹ 5*s*² 5*p*⁶ 5*d*¹ 6*s*²** | **273.042** |
| Ce_3 | 11 | 5*s*² 5*p*⁶ 5*d*¹ 6*s*² | 176.506 |
| Ce_h | 12 | 4*f*¹ 5*s*² 5*p*⁶ 5*d*¹ 6*s*² | 299.9 |
| Pr | 13 | 4*f*^(2.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 337.25 |
| **Pr_3** | **11** | **5*s*² 5*p*⁶ 5*d*¹ 6*s*²** | **181.719** |
| Pr_h | 13 | 4*f*^(2.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 400.742 |
| Nd | 14 | 4*f*^(3.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 338.34 |
| **Nd_3** | **11** | **5*s*² 5*p*⁶ 5*d*¹ 6*s*²** | **182.619** |
| Nd_h | 14 | 4*f*^(3.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 402.016 |
| Pm | 15 | 4*f*^(4.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 340.358 |
| **Pm_3** | **11** | **5*s*² 5*p*⁶ 5*d*¹ 6*s*²** | **176.959** |
| Pm_h | 15 | 4*f*^(4.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 404.406 |
| Sm | 16 | 4*f*^(5.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 341.177 |
| **Sm_3** | **11** | **5*s*² 5*p*⁶ 5*d*¹ 6*s*²** | **177.087** |
| Sm_h | 16 | 4*f*^(5.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 405.382 |
| Eu | 17 | 4*f*^(6.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 344.705 |
| **Eu_2** | **8** | **5*p*⁶ 6*s*²** | **99.328** |
| Eu_3 | 9 | 5*p*⁶ 5*d*¹ 6*s*² | 129.057 |
| Eu_h | 17 | 4*f*^(6.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 403.212 |
| Gd | 18 | 4*f*^(7.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 342.859 |
| **Gd_3** | **9** | **5*p*⁶ 5*d*¹ 6*s*²** | **154.332** |
| Gd_h | 18 | 4*f*^(7.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 407.403 |
| Tb | 19 | 4*f*^(8.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 340.855 |
| **Tb_3** | **9** | **5*p*⁶ 5*d*¹ 6*s*²** | **155.613** |
| Tb_h | 19 | 4*f*^(8.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 405.043 |
| Dy | 20 | 4*f*^(9.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 341.547 |
| **Dy_3** | **9** | **5*p*⁶ 5*d*¹ 6*s*²** | **155.713** |
| Dy_h | 20 | 4*f*^(9.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 405.886 |
| Ho | 21 | 4*f*^(10.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 343.845 |
| **Ho_3** | **9** | **5*p*⁶ 5*d*¹ 6*s*²** | **154.137** |
| Ho_h | 21 | 4*f*^(10.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 415.91 |
| Er | 22 | 4*f*^(11.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 346.295 |
| Er_2 | 8 | 5*p*⁶ 6*s*² | 119.75 |
| **Er_3** | **9** | **5*p*⁶ 5*d*¹ 6*s*²** | **155.037** |
| Er_h | 22 | 4*f*^(11.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 429.583 |
| Tm | 23 | 4*f*^(12.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 344.206 |
| **Tm_3** | **9** | **5*p*⁶ 5*d*¹ 6*s*²** | **149.221** |
| Tm_h | 23 | 4*f*^(12.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 419.812 |
| Yb | 24 | 4*f*^(13.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 344.312 |
| **Yb_2** | **8** | **5*p*⁶ 6*s*²** | **112.578** |
| Yb_3 | 9 | 5*p*⁶ 5*d*¹ 6*s*² | 188.359 |
| Yb_h | 24 | 4*f*^(13.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 409.285 |
| Lu | 25 | 4*f*¹⁴ 5*s*² 5*p*⁶ 5*d*¹ 6*s*² | 255.695 |
| **Lu_3** | **9** | **5*p*⁶ 5*d*¹ 6*s*²** | **154.992** |
| Hf | 4 | 5*d*³ 6*s*¹ | 220.334 |
| **Hf_pv** | **10** | **5*p*⁶ 5*d*³ 6*s*¹** | **220.334** |
| Hf_sv | 12 | 5*s*² 5*p*⁶ 5*d*⁴ | 237.444 |
| Ta | 5 | 5*d*⁴ 6*s*¹ | 223.667 |
| **Ta_pv** | **11** | **5*p*⁶ 5*d*⁴ 6*s*¹** | **223.667** |
| W | 6 | 5*d*⁵ 6*s*¹ | 223.057 |
| **W_sv** | **14** | **5*s*² 5*p*⁶ 5*d*⁵ 6*s*¹** | **223.057** |
| **Re** | **7** | **5*d*⁶ 6*s*¹** | **226.216** |
| Re_pv | 13 | 5*p*⁶ 5*d*⁶ 6*s*¹ | 226.216 |
| **Os** | **8** | **5*d*⁷ 6*s*¹** | **228.022** |
| Os_pv | 14 | 5*p*⁶ 5*d*⁷ 6*s*¹ | 228.022 |
| **Ir** | **9** | **5*d*⁸ 6*s*¹** | **210.864** |
| **Pt** | **10** | **5*d*⁹ 6*s*¹** | **230.283** |
| Pt_pv | 16 | 5*p*⁶ 5*d*⁹ 6*s*¹ | 294.607 |
| **Au** | **11** | **5*d*¹⁰ 6*s*¹** | **229.943** |
| **Hg** | **12** | **5*d*¹⁰ 6*s*²** | **233.204** |
| Tl | 3 | 6*s*² 6*p*¹ | 90.14 |
| **Tl_d** | **13** | **5*d*¹⁰ 6*s*² 6*p*¹** | **237.053** |
| Pb | 4 | 6*s*² 6*p*² | 97.973 |
| **Pb_d** | **14** | **5*d*¹⁰ 6*s*² 6*p*²** | **237.835** |
| Bi | 5 | 6*s*² 6*p*³ | 105.037 |
| **Bi_d** | **15** | **5*d*¹⁰ 6*s*² 6*p*³** | **242.839** |
| Po | 6 | 6*s*² 6*p*⁴ | 159.707 |
| **Po_d** | **16** | **5*d*¹⁰ 6*s*² 6*p*⁴** | **264.565** |
| **At** | **7** | **6*s*² 6*p*⁵** | **161.43** |
| **Rn** | **8** | **6*s*² 6*p*⁶** | **151.497** |
| **Fr_sv** | **9** | **6*s*² 6*p*⁶ 7*s*¹** | **214.54** |
| **Ra_sv** | **10** | **6*s*² 6*p*⁶ 7*s*²** | **237.367** |
| **Ac** | **11** | **6*s*² 6*p*⁶ 6*d*¹ 7*s*²** | **172.351** |
| **Th** | **12** | **5*f*¹ 6*s*² 6*p*⁶ 6*d*¹ 7*s*²** | **247.306** |
| Th_s | 10 | 5*f*¹ 6*p*⁶ 6*d*¹ 7*s*² | 169.363 |
| **Pa** | **13** | **5*f*¹ 6*s*² 6*p*⁶ 6*d*² 7*s*²** | **252.193** |
| Pa_s | 11 | 5*f*¹ 6*p*⁶ 6*d*² 7*s*² | 193.466 |
| **U** | **14** | **5*f*² 6*s*² 6*p*⁶ 6*d*² 7*s*²** | **252.502** |
| U_s | 14 | 5*f*² 6*s*² 6*p*⁶ 6*d*² 7*s*² | 209.23 |
| **Np** | **15** | **5*f*³ 6*s*² 6*p*⁶ 6*d*² 7*s*²** | **254.26** |
| Np_s | 15 | 5*f*³ 6*s*² 6*p*⁶ 6*d*² 7*s*² | 207.713 |
| **Pu** | **16** | **5*f*⁴ 6*s*² 6*p*⁶ 6*d*² 7*s*²** | **254.353** |
| Pu_s | 16 | 5*f*⁴ 6*s*² 6*p*⁶ 6*d*² 7*s*² | 207.83 |
| **Am** | **17** | **5*f*⁵ 6*s*² 6*p*⁶ 6*d*² 7*s*²** | **255.875** |
| **Cm** | **18** | **5*f*⁶ 6*s*² 6*p*⁶ 6*d*² 7*s*²** | **257.953** |
| Cf | 20 | 5*f*⁸ 6*s*² 6*p*⁶ 6*d*² 7*s*² | 414.614 |

#### Calculation requiring a large number of unoccupied states
The following table highlights recommended PAW potentials for
calculations involving many states above the Fermi energy in **bold**.

They are optimized for scattering properties high above the Fermi level
and thus have advantages if many unoccupied states are involved, as for
[optical properties](../redirects/Optical_properties.md) or
[many-body perturbation
theory](../redirects/Many-body_perturbation_theory.md).

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| GW potentials (potpaw.64) |  |  |  |
| Potential name | Number of valence electrons | Valence electron configuration | ENAMX \[eV\] |
| **H_GW** | **1** | **1*s*¹** | **300.0** |
| H_GW_new | 1 | 1*s*¹ | 536.615 |
| H_h_GW | 1 | 1*s*¹ | 700.0 |
| **He_GW** | **2** | **1*s*²** | **405.78** |
| Li_AE_GW | 3 | 1*s*² 2*p*¹ | 433.699 |
| Li_GW | 1 | 2*s*¹ | 112.104 |
| **Li_sv_GW** | **3** | **1*s*² 2*p*¹** | **433.699** |
| Be_GW | 2 | 2*s*^(1.9999) 2*p*^(0.001) | 247.543 |
| **Be_sv_GW** | **4** | **1*s*² 2*p*²** | **537.454** |
| **B_GW** | **3** | **2*s*² 2*p*¹** | **318.614** |
| B_GW_new | 3 | 2*s*² 2*p*¹ | 318.614 |
| B_h_GW | 3 | 2*s*² 2*p*¹ | 731.373 |
| **C_GW** | **4** | **2*s*² 2*p*²** | **413.992** |
| C_GW_new | 4 | 2*s*² 2*p*² | 433.983 |
| C_h_GW | 4 | 2*s*² 2*p*² | 741.689 |
| C_s_GW | 4 | 2*s*² 2*p*² | 304.843 |
| **N_GW** | **5** | **2*s*² 2*p*³** | **420.902** |
| N_GW_new | 5 | 2*s*² 2*p*³ | 452.633 |
| N_h_GW | 5 | 2*s*² 2*p*³ | 755.582 |
| N_s_GW | 5 | 2*s*² 2*p*³ | 312.986 |
| **O_GW** | **6** | **2*s*² 2*p*⁴** | **414.635** |
| O_GW_new | 6 | 2*s*² 2*p*⁴ | 466.797 |
| O_h_GW | 6 | 2*s*² 2*p*⁴ | 765.519 |
| O_s_GW | 6 | 2*s*² 2*p*⁴ | 334.664 |
| **F_GW** | **7** | **2*s*² 2*p*⁵** | **487.698** |
| F_GW_new | 7 | 2*s*² 2*p*⁵ | 480.281 |
| F_h_GW | 7 | 2*s*² 2*p*⁵ | 848.626 |
| **Ne_GW** | **8** | **2*s*² 2*p*⁶** | **432.275** |
| Ne_s_GW | 8 | 2*s*² 2*p*⁶ | 318.26 |
| **Na_sv_GW** | **9** | **2*s*² 2*p*⁶ 3*p*¹** | **372.853** |
| Mg_GW | 2 | 3*s*² | 126.143 |
| Mg_pv_GW | 8 | 2*p*⁶ 3*s*² | 403.929 |
| **Mg_sv_GW** | **10** | **2*s*² 2*p*⁶ 3*d*²** | **429.893** |
| **Al_GW** | **3** | **3*s*² 3*p*¹** | **240.3** |
| Al_sv_GW | 11 | 2*s*² 2*p*⁶ 3*s*² 3*p*¹ | 411.109 |
| **Si_GW** | **4** | **3*s*² 3*p*²** | **245.345** |
| Si_sv_GW | 12 | 2*s*² 2*p*⁶ 3*s*² 3*p*² | 547.578 |
| **P_GW** | **5** | **3*s*² 3*p*³** | **255.04** |
| **S_GW** | **6** | **3*s*² 3*p*⁴** | **258.689** |
| **Cl_GW** | **7** | **3*s*² 3*p*⁵** | **262.472** |
| **Ar_GW** | **8** | **3*s*² 3*p*⁶** | **290.599** |
| **K_sv_GW** | **9** | **3*s*² 3*p*⁶ 3*d*¹** | **248.998** |
| **Ca_sv_GW** | **10** | **3*s*² 3*p*⁶ 3*d*²** | **281.43** |
| **Sc_sv_GW** | **11** | **3*s*² 3*p*⁶ 3*d*³** | **378.961** |
| **Ti_sv_GW** | **12** | **3*s*² 3*p*⁶ 3*d*⁴** | **383.774** |
| **V_sv_GW** | **13** | **3*s*² 3*p*⁶ 3*d*⁵** | **382.321** |
| **Cr_sv_GW** | **14** | **3*s*² 3*p*⁶ 3*d*⁶** | **384.932** |
| Mn_GW | 7 | 3*d*⁶ 4*s*¹ | 278.466 |
| **Mn_sv_GW** | **15** | **3*s*² 3*p*⁶ 3*d*⁷** | **384.627** |
| Fe_GW | 8 | 3*d*⁷ 4*s*¹ | 321.007 |
| **Fe_sv_GW** | **16** | **3*s*² 3*p*⁶ 3*d*⁸** | **387.837** |
| Co_GW | 9 | 3*d*⁸ 4*s*¹ | 323.4 |
| **Co_sv_GW** | **17** | **3*s*² 3*p*⁶ 3*d*⁹** | **387.491** |
| Ni_GW | 10 | 3*d*⁹ 4*s*¹ | 357.323 |
| **Ni_sv_GW** | **18** | **3*s*² 3*p*⁶ 3*d*¹⁰** | **389.645** |
| Cu_GW | 11 | 3*d*¹⁰ 4*s*¹ | 417.039 |
| **Cu_sv_GW** | **19** | **3*s*² 3*p*⁶ 3*d*¹⁰ 4*s*¹** | **467.331** |
| Zn_GW | 12 | 3*d*¹⁰ 4*s*² | 328.191 |
| **Zn_sv_GW** | **20** | **3*s*² 3*p*⁶ 3*d*¹⁰ 4*s*²** | **401.665** |
| Ga_GW | 3 | 4*s*² 4*p*¹ | 134.678 |
| **Ga_d_GW** | **13** | **3*d*¹⁰ 4*s*² 4*p*¹** | **404.602** |
| Ga_sv_GW | 21 | 3*s*² 3*p*⁶ 3*d*¹⁰ 4*s*² 4*p*¹ | 404.602 |
| Ge_GW | 4 | 4*s*² 4*p*² | 173.807 |
| **Ge_d_GW** | **14** | **3*d*¹⁰ 4*s*² 4*p*²** | **375.434** |
| Ge_sv_GW | 22 | 3*s*² 3*p*⁶ 3*d*¹⁰ 4*s*² 4*p*² | 410.425 |
| **As_GW** | **5** | **4*s*² 4*p*³** | **208.702** |
| As_sv_GW | 23 | 3*s*² 3*p*⁶ 3*d*¹⁰ 4*s*² 4*p*³ | 415.313 |
| **Se_GW** | **6** | **4*s*² 4*p*⁴** | **211.555** |
| Se_sv_GW | 24 | 3*s*² 3*p*⁶ 3*d*¹⁰ 4*s*² 4*p*⁴ | 469.344 |
| **Br_GW** | **7** | **4*s*² 4*p*⁵** | **216.285** |
| Br_sv_GW | 25 | 3*s*² 3*p*⁶ 3*d*¹⁰ 4*s*² 4*p*⁵ | 475.692 |
| **Kr_GW** | **8** | **4*s*² 4*p*⁶** | **252.232** |
| **Rb_sv_GW** | **9** | **4*s*² 4*p*⁶ 4*d*¹** | **221.197** |
| **Sr_sv_GW** | **10** | **4*s*² 4*p*⁶ 4*d*²** | **224.817** |
| **Y_sv_GW** | **11** | **4*s*² 4*p*⁶ 4*d*³** | **339.758** |
| **Zr_sv_GW** | **12** | **4*s*² 4*p*⁶ 4*d*⁴** | **346.364** |
| **Nb_sv_GW** | **13** | **4*s*² 4*p*⁶ 4*d*⁵** | **353.872** |
| **Mo_sv_GW** | **14** | **4*s*² 4*p*⁶ 4*d*⁶** | **344.914** |
| **Tc_sv_GW** | **15** | **4*s*² 4*p*⁶ 4*d*⁷** | **351.044** |
| **Ru_sv_GW** | **16** | **4*s*² 4*p*⁶ 4*d*⁸** | **348.106** |
| Rh_GW | 9 | 4*d*⁸ 5*s*¹ | 247.408 |
| **Rh_sv_GW** | **17** | **4*s*² 4*p*⁶ 4*d*⁹** | **351.206** |
| Pd_GW | 10 | 4*d*⁹ 5*s*¹ | 250.925 |
| **Pd_sv_GW** | **18** | **4*s*² 4*p*⁶ 4*d*¹⁰** | **356.093** |
| Ag_GW | 11 | 4*d*¹⁰ 5*s*¹ | 249.844 |
| **Ag_sv_GW** | **19** | **4*s*² 4*p*⁶ 4*d*¹¹** | **354.43** |
| Cd_GW | 12 | 4*d*¹⁰ 5*s*² | 254.045 |
| **Cd_sv_GW** | **20** | **4*s*² 4*p*⁶ 4*d*¹⁰ 5*s*²** | **361.806** |
| **In_d_GW** | **13** | **4*d*¹⁰ 5*s*² 5*p*¹** | **278.624** |
| In_sv_GW | 21 | 4*s*² 4*p*⁶ 4*d*¹⁰ 5*s*² 5*p*¹ | 366.771 |
| **Sn_d_GW** | **14** | **4*d*¹⁰ 5*s*² 5*p*²** | **260.066** |
| Sn_sv_GW | 22 | 4*s*² 4*p*⁶ 4*d*¹⁰ 5*s*² 5*p*² | 368.778 |
| Sb_GW | 5 | 5*s*² 5*p*³ | 172.069 |
| **Sb_d_GW** | **15** | **4*d*¹⁰ 5*s*² 5*p*³** | **263.1** |
| Sb_sv_GW | 23 | 4*s*² 4*p*⁶ 4*d*¹⁰ 5*s*² 5*p*³ | 372.491 |
| **Te_GW** | **6** | **5*s*² 5*p*⁴** | **174.982** |
| Te_sv_GW | 24 | 4*s*² 4*p*⁶ 4*d*¹⁰ 5*s*² 5*p*⁴ | 376.618 |
| **I_GW** | **7** | **5*s*² 5*p*⁵** | **175.647** |
| I_sv_GW | 25 | 4*s*² 4*p*⁶ 4*d*¹⁰ 5*s*² 5*p*⁵ | 381.674 |
| **Xe_GW** | **8** | **5*s*² 5*p*⁶** | **179.547** |
| Xe_sv_GW | 26 | 4*s*² 4*p*⁶ 4*d*¹⁰ 5*s*² 5*p*⁶ | 400.476 |
| **Cs_sv_GW** | **9** | **5*s*² 5*p*⁶ 5*d*¹** | **198.101** |
| **Ba_sv_GW** | **10** | **5*s*² 5*p*⁶ 5*d*¹ 6*s*¹** | **267.02** |
| **La_GW** | **11** | **4*f*^(0.2) 5*s*² 5*p*⁶ 5*d*^(0.8) 6*s*²** | **313.688** |
| **Ce_GW** | **12** | **4*f*¹ 5*s*² 5*p*⁶ 5*d*¹ 6*s*²** | **304.625** |
| **Hf_sv_GW** | **12** | **5*s*² 5*p*⁶ 5*d*⁴** | **309.037** |
| **Ta_sv_GW** | **13** | **5*s*² 5*p*⁶ 5*d*⁵** | **286.008** |
| **W_sv_GW** | **14** | **5*s*² 5*p*⁶ 5*d*⁶** | **317.132** |
| **Re_sv_GW** | **15** | **5*s*² 5*p*⁶ 5*d*⁷** | **317.012** |
| **Os_sv_GW** | **16** | **5*s*² 5*p*⁶ 5*d*⁸** | **319.773** |
| **Ir_sv_GW** | **17** | **5*s*² 5*p*⁶ 5*d*⁹** | **319.843** |
| Pt_GW | 10 | 5*d*⁹ 6*s*¹ | 248.716 |
| **Pt_sv_GW** | **18** | **5*s*² 5*p*⁶ 5*d*¹⁰** | **323.669** |
| Au_GW | 11 | 5*d*¹⁰ 6*s*¹ | 248.344 |
| **Au_sv_GW** | **19** | **5*s*² 5*p*⁶ 5*d*¹¹** | **306.658** |
| **Hg_sv_GW** | **20** | **5*s*² 5*p*⁶ 5*d*¹⁰ 6*s*²** | **312.028** |
| **Tl_d_GW** | **15** | **5*s*² 5*d*¹⁰ 6*s*² 6*p*¹** | **237.053** |
| Tl_sv_GW | 21 | 5*s*² 5*p*⁶ 5*d*¹⁰ 6*s*² 6*p*¹ | 316.583 |
| **Pb_d_GW** | **16** | **5*s*² 5*d*¹⁰ 6*s*² 6*p*²** | **237.809** |
| Pb_sv_GW | 22 | 5*s*² 5*p*⁶ 5*d*¹⁰ 6*s*² 6*p*² | 317.193 |
| Bi_GW | 5 | 6*s*² 6*p*³ | 146.53 |
| **Bi_d_GW** | **17** | **5*s*² 5*d*¹⁰ 6*s*² 6*p*³** | **261.876** |
| Bi_sv_GW | 23 | 5*s*² 5*p*⁶ 5*d*¹⁰ 6*s*² 6*p*³ | 323.513 |
| **Po_d_GW** | **18** | **5*s*² 5*d*¹⁰ 6*s*² 6*p*⁴** | **267.847** |
| Po_sv_GW | 24 | 5*s*² 5*p*⁶ 5*d*¹⁰ 6*s*² 6*p*⁴ | 326.618 |
| **At_d_GW** | **17** | **5*d*¹⁰ 6*s*² 6*p*⁵** | **266.251** |
| At_sv_GW | 25 | 5*s*² 5*p*⁶ 5*d*¹⁰ 6*s*² 6*p*⁵ | 328.529 |
| **Rn_d_GW** | **18** | **5*d*¹⁰ 6*s*² 6*p*⁶** | **267.347** |
| Rn_sv_GW | 26 | 5*s*² 5*p*⁶ 5*d*¹⁰ 6*s*² 6*p*⁶ | 329.758 |

#### Reference calculation; extremely high accuracy
For reference calculations, i.e., calculations where the utmost accuracy
is needed, and computational effort is of no concern, we recommend the
following set of potentials. These are mostly [hard pseudopotentials
(\_h)](../input-files/Available_pseudopotentials.md)
of the GW variant, which were used with a 1000 eV plane-wave cutoff in a
recent comparison study of DFT codes to reproduce all-electron results
as accurately as
possible^([\[1\]](#cite_note-bosoni:natphysrev:2023-1)). However, in
most cases, the results should be comparable with the standard
potentials, while the computational effort will increase
significantly^([\[2\]](#cite_note-2)).

|  |
|----|
| **Mind:** Unless the utmost accuracy is required, it is usually not worth paying the extra computational cost required for the hard GW potentials recommended in the following list, compared to their standard counterparts at the beginning of this section for DFT calculations. |

|  |  |  |  |  |
|:--:|:--:|:--:|:--:|:--:|
| Reference potentials (potpaw.64) |  |  |  |  |
| Element | Potential name | Number of valence electrons | Valence electron configuration | ENAMX \[eV\] |
| H | H_GW | 1 | 1*s*¹ | 300.0 |
| He | He_GW | 2 | 1*s*² | 405.78 |
| Li | Li_sv_GW | 3 | 1*s*² 2*p*¹ | 433.699 |
| Be | Be_sv_GW | 4 | 1*s*² 2*p*² | 537.454 |
| B | B_GW | 3 | 2*s*² 2*p*¹ | 318.614 |
| C | C_GW | 4 | 2*s*² 2*p*² | 413.992 |
| N | N_GW | 5 | 2*s*² 2*p*³ | 420.902 |
| O | O_h_GW | 6 | 2*s*² 2*p*⁴ | 765.519 |
| F | F_GW | 7 | 2*s*² 2*p*⁵ | 487.698 |
| Ne | Ne_GW | 8 | 2*s*² 2*p*⁶ | 432.275 |
| Na | Na_sv_GW | 9 | 2*s*² 2*p*⁶ 3*p*¹ | 372.853 |
| Mg | Mg_sv_GW | 10 | 2*s*² 2*p*⁶ 3*d*² | 429.893 |
| Al | Al_GW | 3 | 3*s*² 3*p*¹ | 240.3 |
| Si | Si_GW | 4 | 3*s*² 3*p*² | 245.345 |
| P | P_GW | 5 | 3*s*² 3*p*³ | 255.04 |
| S | S_GW | 6 | 3*s*² 3*p*⁴ | 258.689 |
| Cl | Cl_GW | 7 | 3*s*² 3*p*⁵ | 262.472 |
| Ar | Ar_GW | 8 | 3*s*² 3*p*⁶ | 290.599 |
| K | K_sv_GW | 9 | 3*s*² 3*p*⁶ 3*d*¹ | 248.998 |
| Ca | Ca_sv_GW | 10 | 3*s*² 3*p*⁶ 3*d*² | 281.43 |
| Sc | Sc_sv_GW | 11 | 3*s*² 3*p*⁶ 3*d*³ | 378.961 |
| Ti | Ti_sv_GW | 12 | 3*s*² 3*p*⁶ 3*d*⁴ | 383.774 |
| V | V_sv_GW | 13 | 3*s*² 3*p*⁶ 3*d*⁵ | 382.321 |
| Cr | Cr_sv_GW | 14 | 3*s*² 3*p*⁶ 3*d*⁶ | 384.932 |
| Mn | Mn_sv_GW | 15 | 3*s*² 3*p*⁶ 3*d*⁷ | 384.627 |
| Fe | Fe_sv_GW | 16 | 3*s*² 3*p*⁶ 3*d*⁸ | 387.837 |
| Co | Co_sv_GW | 17 | 3*s*² 3*p*⁶ 3*d*⁹ | 387.491 |
| Ni | Ni_sv_GW | 18 | 3*s*² 3*p*⁶ 3*d*¹⁰ | 389.645 |
| Cu | Cu_sv_GW | 19 | 3*s*² 3*p*⁶ 3*d*¹⁰ 4*s*¹ | 467.331 |
| Zn | Zn_sv_GW | 20 | 3*s*² 3*p*⁶ 3*d*¹⁰ 4*s*² | 401.665 |
| Ga | Ga_d_GW | 13 | 3*d*¹⁰ 4*s*² 4*p*¹ | 404.602 |
| Ge | Ge_d_GW | 14 | 3*d*¹⁰ 4*s*² 4*p*² | 375.434 |
| As | As_GW | 5 | 4*s*² 4*p*³ | 208.702 |
| Se | Se_GW | 6 | 4*s*² 4*p*⁴ | 211.555 |
| Br | Br_GW | 7 | 4*s*² 4*p*⁵ | 216.285 |
| Kr | Kr_GW | 8 | 4*s*² 4*p*⁶ | 252.232 |
| Rb | Rb_sv_GW | 9 | 4*s*² 4*p*⁶ 4*d*¹ | 221.197 |
| Sr | Sr_sv_GW | 10 | 4*s*² 4*p*⁶ 4*d*² | 224.817 |
| Y | Y_sv_GW | 11 | 4*s*² 4*p*⁶ 4*d*³ | 339.758 |
| Zr | Zr_sv_GW | 12 | 4*s*² 4*p*⁶ 4*d*⁴ | 346.364 |
| Nb | Nb_sv_GW | 13 | 4*s*² 4*p*⁶ 4*d*⁵ | 353.872 |
| Mo | Mo_sv_GW | 14 | 4*s*² 4*p*⁶ 4*d*⁶ | 344.914 |
| Tc | Tc_sv_GW | 15 | 4*s*² 4*p*⁶ 4*d*⁷ | 351.044 |
| Ru | Ru_sv_GW | 16 | 4*s*² 4*p*⁶ 4*d*⁸ | 348.106 |
| Rh | Rh_sv_GW | 17 | 4*s*² 4*p*⁶ 4*d*⁹ | 351.206 |
| Pd | Pd_sv_GW | 18 | 4*s*² 4*p*⁶ 4*d*¹⁰ | 356.093 |
| Ag | Ag_sv_GW | 19 | 4*s*² 4*p*⁶ 4*d*¹¹ | 354.43 |
| Cd | Cd_sv_GW | 20 | 4*s*² 4*p*⁶ 4*d*¹⁰ 5*s*² | 361.806 |
| In | In_d_GW | 13 | 4*d*¹⁰ 5*s*² 5*p*¹ | 278.624 |
| Sn | Sn_d_GW | 14 | 4*d*¹⁰ 5*s*² 5*p*² | 260.066 |
| Sb | Sb_d_GW | 15 | 4*d*¹⁰ 5*s*² 5*p*³ | 263.1 |
| Te | Te_GW | 6 | 5*s*² 5*p*⁴ | 174.982 |
| I | I_GW | 7 | 5*s*² 5*p*⁵ | 175.647 |
| Xe | Xe_GW | 8 | 5*s*² 5*p*⁶ | 179.547 |
| Cs | Cs_sv_GW | 9 | 5*s*² 5*p*⁶ 5*d*¹ | 198.101 |
| Ba | Ba_sv_GW | 10 | 5*s*² 5*p*⁶ 5*d*¹ 6*s*¹ | 267.02 |
| La | La_GW | 11 | 4*f*^(0.2) 5*s*² 5*p*⁶ 5*d*^(0.8) 6*s*² | 313.688 |
| Ce | Ce_GW | 12 | 4*f*¹ 5*s*² 5*p*⁶ 5*d*¹ 6*s*² | 304.625 |
| Pr | Pr_h | 13 | 4*f*^(2.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 400.742 |
| Nd | Nd_h | 14 | 4*f*^(3.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 402.016 |
| Pm | Pm_h | 15 | 4*f*^(4.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 404.406 |
| Sm | Sm_h | 16 | 4*f*^(5.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 405.382 |
| Eu | Eu_h | 17 | 4*f*^(6.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 403.212 |
| Gd | Gd_h | 18 | 4*f*^(7.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 407.403 |
| Tb | Tb_h | 19 | 4*f*^(8.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 405.043 |
| Dy | Dy_h | 20 | 4*f*^(9.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 405.886 |
| Ho | Ho_h | 21 | 4*f*^(10.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 415.91 |
| Er | Er_h | 22 | 4*f*^(11.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 429.583 |
| Tm | Tm_h | 23 | 4*f*^(12.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 419.812 |
| Yb | Yb_h | 24 | 4*f*^(13.5) 5*s*² 5*p*⁶ 5*d*^(0.5) 6*s*² | 409.285 |
| Lu | Lu | 25 | 4*f*¹⁴ 5*s*² 5*p*⁶ 5*d*¹ 6*s*² | 255.695 |
| Hf | Hf_sv_GW | 12 | 5*s*² 5*p*⁶ 5*d*⁴ | 309.037 |
| Ta | Ta_sv_GW | 13 | 5*s*² 5*p*⁶ 5*d*⁵ | 286.008 |
| W | W_sv_GW | 14 | 5*s*² 5*p*⁶ 5*d*⁶ | 317.132 |
| Re | Re_sv_GW | 15 | 5*s*² 5*p*⁶ 5*d*⁷ | 317.012 |
| Os | Os_sv_GW | 16 | 5*s*² 5*p*⁶ 5*d*⁸ | 319.773 |
| Ir | Ir_sv_GW | 17 | 5*s*² 5*p*⁶ 5*d*⁹ | 319.843 |
| Pt | Pt_sv_GW | 18 | 5*s*² 5*p*⁶ 5*d*¹⁰ | 323.669 |
| Au | Au_sv_GW | 19 | 5*s*² 5*p*⁶ 5*d*¹¹ | 306.658 |
| Hg | Hg_sv_GW | 20 | 5*s*² 5*p*⁶ 5*d*¹⁰ 6*s*² | 312.028 |
| Tl | Tl_d_GW | 15 | 5*s*² 5*d*¹⁰ 6*s*² 6*p*¹ | 237.053 |
| Pb | Pb_d_GW | 16 | 5*s*² 5*d*¹⁰ 6*s*² 6*p*² | 237.809 |
| Bi | Bi_d_GW | 17 | 5*s*² 5*d*¹⁰ 6*s*² 6*p*³ | 261.876 |
| Po | Po_d_GW | 18 | 5*s*² 5*d*¹⁰ 6*s*² 6*p*⁴ | 267.847 |
| At | At_d_GW | 17 | 5*d*¹⁰ 6*s*² 6*p*⁵ | 266.251 |
| Rn | Rn_d_GW | 18 | 5*d*¹⁰ 6*s*² 6*p*⁶ | 267.347 |
| Fr | Fr_sv | 9 | 6*s*² 6*p*⁶ 7*s*¹ | 214.54 |
| Ra | Ra_sv | 10 | 6*s*² 6*p*⁶ 7*s*² | 237.367 |
| Ac | Ac | 11 | 6*s*² 6*p*⁶ 6*d*¹ 7*s*² | 172.351 |
| Th | Th | 12 | 5*f*¹ 6*s*² 6*p*⁶ 6*d*¹ 7*s*² | 247.306 |
| Pa | Pa | 13 | 5*f*¹ 6*s*² 6*p*⁶ 6*d*² 7*s*² | 252.193 |
| U | U | 14 | 5*f*² 6*s*² 6*p*⁶ 6*d*² 7*s*² | 252.502 |
| Np | Np | 15 | 5*f*³ 6*s*² 6*p*⁶ 6*d*² 7*s*² | 254.26 |
| Pu | Pu | 16 | 5*f*⁴ 6*s*² 6*p*⁶ 6*d*² 7*s*² | 254.353 |
| Am | Am | 17 | 5*f*⁵ 6*s*² 6*p*⁶ 6*d*² 7*s*² | 255.875 |
| Cm | Cm | 18 | 5*f*⁶ 6*s*² 6*p*⁶ 6*d*² 7*s*² | 257.953 |

### Selecting the release version
Generally, we recommend using the latest release of pseudopotentials.

|  |
|----|
| **Tip:** For compatibility reasons or to accurately reproduce another calculation, you might need to use another (older) pseudopotential release. Consult the list of [available pseudopotentials](../input-files/Available_pseudopotentials.md). |

### Element-specific recommendation
#### Hydrogen-like atoms with fractional valence
Twelve hydrogen-like potentials are supplied for a valency between 0.25
and 1.75. Further potentials might become available, c.f. [available
pseudopotentials](../input-files/Available_pseudopotentials.md).
These are useful, e.g., to passivate dangling surface bonds.

|  |
|----|
| **Mind:** The [POTCAR](../input-files/POTCAR.md) files restrict the number of digits for the valency (typically 2, at most 3 digits). Therefor, using three H.33 potentials does yield 0.99 electrons and not 1.00 electron. This can cause undesirable hole- or electron-like states. Set the [NELECT](../incar-tags/NELECT.md) tag in the [INCAR](../input-files/INCAR.md) file to correct the total number of electrons. |

#### First-row elements
For the 1st row elements B, C, N, O, and F, three potential versions
exist, the plain one, a hard version, and a soft version. For most
purposes, the standard version of PAW potentials is most appropriate.
They yield reliable results for energy cutoffs between 325 and 400 eV,
where 370-400 eV are required to predict vibrational properties
accurately. Binding geometries and energy differences are already well
reproduced at 325 eV. The typical bond-length errors for first row
dimers (N₂, CO, O₂) are about 1% compared to more accurate DFT
calculations. The [hard pseudopotentials
(\_h)](../input-files/Available_pseudopotentials.md)
give results that are essentially identical to the best DFT calculations
presently available (FLAPW, or Gaussian with very large basis sets). The
[soft potentials
(\_s)](../input-files/Available_pseudopotentials.md)
are optimized to work around 250-280 eV. They yield reliable description
for most oxides, such as V_(x)O_(y), TiO₂, CeO₂, but fail to describe
some structural details in zeolites, i.e., cell parameters, and volume.

For Hartree-Fock (HF) and hybrid-functional calculations, we strictly
recommend using the standard, standard GW, or hard potentials. For
instance, the O_s potential can cause unacceptably large errors even in
transition metal oxides. Generally, the soft potentials are less
transferable from one exchange-correlation functional to another and
often fail when the exact exchange needs to be calculated.

|  |
|----|
| **Tip:** If dimers with short bonds are present in the system (H₂O, O₂, CO, N₂, F₂, P₂, S₂, Cl₂), we recommend using the \_h potentials. Specifically, C_h, O_h, N_h, F_h, P_h, S_h, Cl_h, or their \_GW counterparts. Otherwise, the standard version is often the best choice for first-row elements. |

#### Alkali and alkali-earth elements (simple metals)
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

#### p-elements
For Ga, Ge, In, Sn, Tl-At, the lower-lying *d* states should be treated
as valence states (\_d potential). For these elements, alternative
potentials that treat the *d* states as core states are also available
but should be used with great care.

#### d-elements
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

#### f-elements
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

##### Lanthanides with fixed valence
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

## Example: NiO equilibrium volume
Antiferromagnetic NiO in the rocksalt structure is a prototype system
for a correlated material. It is a Mott insulator and not well described
with standard DFT. To get correct material properties, methods beyond
DFT are required. [DFT+DMFT
calculations](DFT+DMFT_calculations.md) are
an option, but the much cheaper [DFT+U](../redirects/DFT+U.md) approach
is often used with satisfactory results.

[![](https://vasp.at/wiki/images/thumb/4/46/NiO_diff_pots_energy_vs_volume.png/450px-NiO_diff_pots_energy_vs_volume.png)](https://vasp.at/wiki/File:NiO_diff_pots_energy_vs_volume.png)

Fig 1. LSDA+U Energy vs. volume plot for AFM NiO. Different Ni
potentials were used to create the data. All other inputs are
equivalent. The all-electron (AE) reference was calculated with Wien2K.

The computational setup and how to interpret the results of a DFT+U
calculation for NiO are given in the section on [NiO
LSDA+U](../misc/NiO_LSDA+U.md). Here, we will focus on the
effect of the choice of the Ni pseudopotential on the equation of state
(EOS). We compare the results to reference Wien2K
calculations^([\[3\]](#cite_note-tran:prb:2006-3)), which do not use
pseudopotentials, as Wien2K is an all-electron (AE)
code^([\[4\]](#cite_note-blaha:2020-4)).

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

## Related tags and sections
[POTCAR](../input-files/POTCAR.md), [Prepare a
POTCAR](../redirects/Prepare_a_POTCAR.md), [Available
pseudopotentials](../input-files/Available_pseudopotentials.md)

Theoretical background:
[Pseudopotentials](../redirects/Pseudopotentials.md),
[Projector-augmented-wave
formalism](../methods/Projector-augmented-wave_formalism.md)

## References
1.  [↑](#cite_ref-bosoni:natphysrev:2023_1-0) [Emanuele Bosoni, Louis
    Beal, Marnik Bercx, Peter Blaha, Stefan Blügel, Jens Bröder, Martin
    Callsen, Stefaan Cottenier, Augustin Degomme, Vladimir Dikan,
    Kristjan Eimre, Espen Flage-Larsen, Marco Fornari, Alberto Garcia,
    Luigi Genovese, Matteo Giantomassi, Sebastiaan P. Huber, Henning
    Janssen, Georg Kastlunger, Matthias Krack, Georg Kresse, Thomas D.
    Kühne, Kurt Lejaeghere, Georg K. H. Madsen, Martijn Marsman, Nicola
    Marzari, Gregor Michalicek, Hossein Mirhosseini, Tiziano M. A.
    Müller, Guido Petretto, Chris J. Pickard, Samuel Poncé, Gian-Marco
    Rignanese, Oleg Rubel, Thomas Ruh, Michael Sluydts, Danny E. P.
    Vanpoucke, Sudarshan Vijay, Michael Wolloch, Daniel Wortmann,
    Aliaksandr V. Yakutovich, Jusong Yu, Austin Zadoks, Bonan Zhu,
    Giovanni Pizzi, *How to verify the precision of
    density-functional-theory implementations via reproducible and
    universal workflows*, Nat Rev Phys 6, 45–58
    (2024).](https://doi.org/10.1038/s42254-023-00655-3)
2.  [↑](#cite_ref-2) For the potpaw_PBE.64 potential set,
    [ENMAX](../redirects/ENMAX.md) is on average ~26 eV (~11%) and
    [EAUG](../incar-tags/EAUG.md) ~210 eV (~42%) larger for the GW
    potentials compared to their standard counterparts with the same
    valency.
3.  [↑](#cite_ref-tran:prb:2006_3-0) [F. Tran, P. Blaha, and K. Schwarz,
    *Hybrid exchange-correlation energy functionals for strongly
    correlated electrons: Applications to transition-metal monoxides*,
    Phys. Rev. B **74**, 155108
    (2006).](https://doi.org/10.1103/PhysRevB.74.155108)
4.  [↑](#cite_ref-blaha:2020_4-0) [P. Blaha, K. Schwarz. F. Tran, R.
    Laskowski, G. K. H. Madsen, and L. D. Marks, *WIEN2k: An APW+lo
    program for calculating the properties of solids*, J. Chem. Phys.
    **152**, 074101 (2020).](https://doi.org/10.1063/1.5143061)
