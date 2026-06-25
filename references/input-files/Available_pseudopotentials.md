<!-- Source: https://vasp.at/wiki/index.php/Available_pseudopotentials | revid: 25069 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Available pseudopotentials


[Pseudopotentials](../categories/Category-Pseudopotentials.md)
are stored in [POTCAR](POTCAR.md) files and are available
for all elements in the periodic table from the
<a href="https://www.vasp.at/sign_in/portal/" class="external text"
rel="nofollow">VASP Portal</a>. The
available pseudopotentials are
mostly so-called PAW potentials that are based on the
[projector-augmented-wave (PAW)
method](../methods/Projector-augmented-wave_formalism.md)<sup>[\[1\]](#cite_note-bloechl:prb:94b-1)</sup>.
The PAW potentials have been created following the recipes discussed in
Ref.
<sup>[\[2\]](#cite_note-kresse:prb:99-2)</sup>.
Cite Ref.
<sup>[\[1\]](#cite_note-bloechl:prb:94b-1)</sup>
and Ref.
<sup>[\[2\]](#cite_note-kresse:prb:99-2)</sup>
when using any PAW potential.

Also see:

- Simple instructions to set up a [POTCAR](POTCAR.md) file
  with the correct format:
  <a href="/wiki/Prepare_a_POTCAR" class="mw-redirect"
  title="Prepare a POTCAR">Prepare a POTCAR</a>.

<!-- -->

- Guide on **recommendations** and checks to decide which
  pseudopotential flavor to use for a specific calculation: [Choosing
  pseudopotentials](../tutorials/Choosing_pseudopotentials.md).


## Contents


- [1 Available
  pseudopotential sets](#Available_pseudopotential_sets)
  - [1.1 potpaw.64
    (latest, recommended)](#potpaw.64_(latest,_recommended))
    - [1.1.1
      Standard
      potentials](#Standard_potentials)
    - [1.1.2 GW
      potentials](#GW_potentials)
  - [1.2
    potpaw.54](#potpaw.54)
    - [1.2.1
      Standard
      potentials](#Standard_potentials_2)
    - [1.2.2 GW
      potentials](#GW_potentials_2)
  - [1.3
    potpaw.52](#potpaw.52)
    - [1.3.1
      Standard
      potentials](#Standard_potentials_3)
    - [1.3.2 GW
      potentials](#GW_potentials_3)
  - [1.4 LDA
    (2010), PW91 (2006) and PBE (2010) PAW
    potentials](#LDA_(2010),_PW91_(2006)_and_PBE_(2010)_PAW_potentials)
    - [1.4.1
      Standard
      potentials](#Standard_potentials_4)
    - [1.4.2 GW
      potentials](#GW_potentials_4)
  - [1.5 Ultrasoft
    pseudopotentials for LDA and PW91
    (2002)](#Ultrasoft_pseudopotentials_for_LDA_and_PW91_(2002))
  - [1.6 LDA & PBE,
    5.2 & 5.4 (original univie release
    version)](#LDA_&_PBE,_5.2_&_5.4_(original_univie_release_version))
- [2 Different
  variants specified by the
  suffix](#Different_variants_specified_by_the_suffix)
- [3 Related tags
  and sections](#Related_tags_and_sections)
- [4
  References](#References)


## Available pseudopotential sets\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Available pseudopotential sets">edit</a> \| (./index.php.md)\]

The tables list all available pseudopotentials split between

- *standard potentials*: these are intended for treating mostly occupied
  states and are appropriate for calculations within density-functional
  theory, and

<!-- -->

- *GW potentials*: these are optimized for treating unoccupied states
  far above the Fermi level and have an [\_GW
  suffix](#Different_variants_specified_by_the_suffix). GW potentials
  are recommended for computing
  <a href="/wiki/Optical_properties" class="mw-redirect"
  title="Optical properties">optical properties</a> and calculations
  within
  <a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
  title="Many-body perturbation theory">many-body perturbation theory</a>.

The tables comprise the name of the potential, number of valence
electrons, valence electron configuration for the reference system, and
the cutoff energy
(<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>).

The **bold-highlighted entries are the default recommendations**, but
depending on the specific calculation, it might be preferable or
necessary to [choose a different
pseudopotential](../tutorials/Choosing_pseudopotentials.md).

|  |
|----|
| **Important:** Refer to the explanation of [different variants](#Different_variants_specified_by_the_suffix) to understand the suffix in the name of the potential. |

### potpaw.64 (latest, recommended)\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: potpaw.64 (latest, recommended)">edit</a> \| (./index.php.md)")\]

Updated potentials with respect to the potpaw.54 set:

- Li_GW, He_GW: improved accuracy
- C_GW_new, N_GW_new, O_GW_new, F_GW_new: more balanced overall
- C_h, N_h O_h, F_h: improved accuracy for HF calculation (errors below
  0.5 kcal)
- N_s_GW: improved accuracy
- Rn Rn_d_GW, Rn_sv_GW: mass updated to 220
- Ba_sv_GW, Cs_sv, Cs_sv_GW, Cu_sv_GW, Hf_sv_GW: improved accuracy/
  ghost-state issues
- Dy, Er, Eu, Gd, Ho, Nd, Pm, Pr, Sm, Tb, Tm, Yb: lanthanides updated

Newly added potentials:

- H_GW_new, B_GW_new, B_h_GW, C_s_GW
- Dy_h, Er_h, Eu_h, Gd_h, Ho_h, Nd_h, Pm_h, Pr_h, Sm_h, Tb_h, Tm_h, Yb_h

#### Standard potentials\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Standard potentials">edit</a> \| (./index.php.md)\]

Standard PAW potentials are appropriate for calculations that mainly
involve occupied states, e.g., calculations within density-functional
theory *without* computing optical properties.

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| List of LDA potentials |  |  |  |
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
| H_AE | 1 |  | 1000.0 |
| H_h | 1 | 1*s*<sup>1</sup> | 700.0 |
| H_s | 1 | 1*s*<sup>1</sup> | 200.0 |
| **He** | **2** | **1*s*<sup>2</sup>** | **477.779** |
| Li | 1 | 2*s*<sup>1</sup> | 140.0 |
| **Li_sv** | **3** | **1*s*<sup>2</sup> 2*s*<sup>1</sup>** | **498.387** |
| **Be** | **2** | **2*s*<sup>1.9999</sup> 2*p*<sup>0.001</sup>** | **247.951** |
| Be_sv | 4 | 1*s*<sup>2</sup> 2*s*<sup>1.9999</sup> 2*p*<sup>0.001</sup> | 308.45 |
| **B** | **3** | **2*s*<sup>2</sup> 2*p*<sup>1</sup>** | **318.762** |
| B_h | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 700.0 |
| B_s | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 269.251 |
| **C** | **4** | **2*s*<sup>2</sup> 2*p*<sup>2</sup>** | **400.0** |
| C_h | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 742.464 |
| C_s | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 273.704 |
| **N** | **5** | **2*s*<sup>2</sup> 2*p*<sup>3</sup>** | **400.0** |
| N_h | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 755.833 |
| N_s | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 279.424 |
| **O** | **6** | **2*s*<sup>2</sup> 2*p*<sup>4</sup>** | **400.0** |
| O_h | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 765.442 |
| O_s | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 282.604 |
| **F** | **7** | **2*s*<sup>2</sup> 2*p*<sup>5</sup>** | **400.0** |
| F_h | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 772.351 |
| F_s | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 289.647 |
| **Ne** | **8** | **2*s*<sup>2</sup> 2*p*<sup>6</sup>** | **343.403** |
| Na | 1 | 3*s*<sup>1</sup> | 101.956 |
| **Na_pv** | **7** | **2*p*<sup>6</sup> 3*s*<sup>1</sup>** | **259.494** |
| Na_sv | 9 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>1</sup> | 644.874 |
| **Mg** | **2** | **3*s*<sup>1.999</sup> 3*p*<sup>0.001</sup>** | **200.0** |
| Mg_pv | 8 | 2*p*<sup>6</sup> 3*s*<sup>2</sup> | 403.538 |
| Mg_sv | 10 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>2</sup> | 473.54 |
| **Al** | **3** | **3*s*<sup>2</sup> 3*p*<sup>1</sup>** | **240.957** |
| **Si** | **4** | **3*s*<sup>2</sup> 3*p*<sup>2</sup>** | **245.704** |
| **P** | **5** | **3*s*<sup>2</sup> 3*p*<sup>3</sup>** | **255.155** |
| P_h | 5 | 3*s*<sup>2</sup> 3*p*<sup>3</sup> | 390.903 |
| **S** | **6** | **3*s*<sup>2</sup> 3*p*<sup>4</sup>** | **258.602** |
| S_h | 6 | 3*s*<sup>2</sup> 3*p*<sup>4</sup> | 402.84 |
| **Cl** | **7** | **3*s*<sup>2</sup> 3*p*<sup>5</sup>** | **262.25** |
| Cl_h | 7 | 3*s*<sup>2</sup> 3*p*<sup>5</sup> | 409.272 |
| **Ar** | **8** | **3*s*<sup>2</sup> 3*p*<sup>6</sup>** | **266.101** |
| K_pv | 7 | 3*p*<sup>6</sup> 4*s*<sup>1</sup> | 116.596 |
| **K_sv** | **9** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 4*s*<sup>1</sup>** | **259.279** |
| Ca_pv | 8 | 3*p*<sup>6</sup> 4*s*<sup>2</sup> | 119.552 |
| **Ca_sv** | **10** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 4*s*<sup>2</sup>** | **266.727** |
| Sc | 3 | 3*d*<sup>2</sup> 4*s*<sup>1</sup> | 155.006 |
| **Sc_sv** | **11** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>2</sup> 4*s*<sup>1</sup>** | **222.7** |
| Ti | 4 | 3*d*<sup>3</sup> 4*s*<sup>1</sup> | 178.52 |
| Ti_pv | 10 | 3*p*<sup>6</sup> 3*d*<sup>3</sup> 4*s*<sup>1</sup> | 222.435 |
| **Ti_sv** | **12** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>3</sup> 4*s*<sup>1</sup>** | **274.719** |
| V | 5 | 3*d*<sup>4</sup> 4*s*<sup>1</sup> | 192.706 |
| V_pv | 11 | 3*p*<sup>6</sup> 3*d*<sup>4</sup> 4*s*<sup>1</sup> | 263.722 |
| **V_sv** | **13** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>4</sup> 4*s*<sup>1</sup>** | **263.722** |
| Cr | 6 | 3*d*<sup>5</sup> 4*s*<sup>1</sup> | 227.202 |
| **Cr_pv** | **12** | **3*p*<sup>6</sup> 3*d*<sup>5</sup> 4*s*<sup>1</sup>** | **265.753** |
| Cr_sv | 14 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>5</sup> 4*s*<sup>1</sup> | 395.443 |
| Mn | 7 | 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 269.944 |
| **Mn_pv** | **13** | **3*p*<sup>6</sup> 3*d*<sup>6</sup> 4*s*<sup>1</sup>** | **269.944** |
| Mn_sv | 15 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 387.112 |
| **Fe** | **8** | **3*d*<sup>7</sup> 4*s*<sup>1</sup>** | **267.969** |
| Fe_pv | 14 | 3*p*<sup>6</sup> 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 293.303 |
| Fe_sv | 16 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 390.513 |
| **Co** | **9** | **3*d*<sup>8</sup> 4*s*<sup>1</sup>** | **268.056** |
| Co_pv | 15 | 3*p*<sup>6</sup> 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 270.871 |
| Co_sv | 17 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 390.343 |
| **Ni** | **10** | **3*d*<sup>9</sup> 4*s*<sup>1</sup>** | **269.618** |
| Ni_pv | 16 | 3*p*<sup>6</sup> 3*d*<sup>9</sup> 4*s*<sup>1</sup> | 367.726 |
| **Cu** | **11** | **3*d*<sup>10</sup> 4*s*<sup>1</sup>** | **295.521** |
| Cu_pv | 17 | 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>1</sup> | 368.406 |
| **Zn** | **12** | **3*d*<sup>10</sup> 4*s*<sup>2</sup>** | **276.847** |
| Ga | 3 | 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 134.8 |
| **Ga_d** | **13** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup>** | **282.829** |
| Ga_h | 13 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 404.723 |
| Ge | 4 | 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 173.969 |
| **Ge_d** | **14** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup>** | **310.448** |
| Ge_h | 14 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 410.604 |
| **As** | **5** | **4*s*<sup>2</sup> 4*p*<sup>3</sup>** | **208.87** |
| As_d | 15 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>3</sup> | 288.762 |
| **Se** | **6** | **4*s*<sup>2</sup> 4*p*<sup>4</sup>** | **211.602** |
| **Br** | **7** | **4*s*<sup>2</sup> 4*p*<sup>5</sup>** | **216.224** |
| **Kr** | **8** | **4*s*<sup>2</sup> 4*p*<sup>6</sup>** | **185.392** |
| Rb_pv | 7 | 4*p*<sup>6</sup> 4*d*<sup>0.001</sup> 5*s*<sup>0.999</sup> | 122.21 |
| **Rb_sv** | **9** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>0.001</sup> 5*s*<sup>0.999</sup>** | **220.215** |
| **Sr_sv** | **10** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>0.001</sup> 5*s*<sup>1.999</sup>** | **226.327** |
| **Y_sv** | **11** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>2</sup> 5*s*<sup>1</sup>** | **202.554** |
| **Zr_sv** | **12** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>3</sup> 5*s*<sup>1</sup>** | **230.037** |
| Nb_pv | 11 | 4*p*<sup>6</sup> 4*d*<sup>4</sup> 5*s*<sup>1</sup> | 207.263 |
| **Nb_sv** | **13** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>4</sup> 5*s*<sup>1</sup>** | **293.304** |
| Mo | 6 | 4*d*<sup>5</sup> 5*s*<sup>1</sup> | 224.535 |
| Mo_pv | 12 | 4*p*<sup>6</sup> 4*d*<sup>5</sup> 5*s*<sup>1</sup> | 224.535 |
| **Mo_sv** | **14** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>5</sup> 5*s*<sup>1</sup>** | **236.514** |
| Tc | 7 | 4*d*<sup>6</sup> 5*s*<sup>1</sup> | 228.636 |
| **Tc_pv** | **13** | **4*p*<sup>6</sup> 4*d*<sup>6</sup> 5*s*<sup>1</sup>** | **263.345** |
| Tc_sv | 15 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>6</sup> 5*s*<sup>1</sup> | 318.479 |
| Ru | 8 | 4*d*<sup>7</sup> 5*s*<sup>1</sup> | 213.221 |
| **Ru_pv** | **14** | **4*p*<sup>6</sup> 4*d*<sup>7</sup> 5*s*<sup>1</sup>** | **239.907** |
| Ru_sv | 16 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>7</sup> 5*s*<sup>1</sup> | 318.687 |
| Rh | 9 | 4*d*<sup>8</sup> 5*s*<sup>1</sup> | 228.926 |
| **Rh_pv** | **15** | **4*p*<sup>6</sup> 4*d*<sup>8</sup> 5*s*<sup>1</sup>** | **247.321** |
| **Pd** | **10** | **4*d*<sup>9</sup> 5*s*<sup>1</sup>** | **250.832** |
| Pd_pv | 16 | 4*p*<sup>6</sup> 4*d*<sup>9</sup> 5*s*<sup>1</sup> | 250.832 |
| **Ag** | **11** | **4*d*<sup>10</sup> 5*s*<sup>1</sup>** | **249.752** |
| Ag_pv | 17 | 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>1</sup> | 297.68 |
| **Cd** | **12** | **4*d*<sup>10</sup> 5*s*<sup>2</sup>** | **274.265** |
| In | 3 | 5*s*<sup>2</sup> 5*p*<sup>1</sup> | 96.062 |
| **In_d** | **13** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup>** | **239.196** |
| Sn | 4 | 5*s*<sup>2</sup> 5*p*<sup>2</sup> | 103.318 |
| **Sn_d** | **14** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup>** | **241.107** |
| **Sb** | **5** | **5*s*<sup>2</sup> 5*p*<sup>3</sup>** | **172.301** |
| **Te** | **6** | **5*s*<sup>2</sup> 5*p*<sup>4</sup>** | **175.144** |
| **I** | **7** | **5*s*<sup>2</sup> 5*p*<sup>5</sup>** | **175.712** |
| **Xe** | **8** | **5*s*<sup>2</sup> 5*p*<sup>6</sup>** | **153.021** |
| **Cs_sv** | **9** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 6*s*<sup>1</sup>** | **220.727** |
| **Ba_sv** | **10** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.001</sup> 6*s*<sup>1.999</sup>** | **186.981** |
| **La** | **11** | **4*f*<sup>0.0001</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.9999</sup> 6*s*<sup>2</sup>** | **219.044** |
| La_s | 9 | 4*f*<sup>0.0001</sup> 5*p*<sup>6</sup> 5*d*<sup>0.9999</sup> 6*s*<sup>2</sup> | 136.594 |
| **Ce** | **12** | **4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **273.088** |
| Ce_h | 12 | 4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 299.927 |
| Hf | 4 | 5*d*<sup>3</sup> 6*s*<sup>1</sup> | 220.431 |
| **Hf_pv** | **10** | **5*p*<sup>6</sup> 5*d*<sup>3</sup> 6*s*<sup>1</sup>** | **220.431** |
| Hf_sv | 12 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>4</sup> | 237.414 |
| Ta | 5 | 5*d*<sup>4</sup> 6*s*<sup>1</sup> | 223.759 |
| **Ta_pv** | **11** | **5*p*<sup>6</sup> 5*d*<sup>4</sup> 6*s*<sup>1</sup>** | **223.759** |
| W | 6 | 5*d*<sup>5</sup> 6*s*<sup>1</sup> | 223.126 |
| **W_sv** | **14** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>5</sup> 6*s*<sup>1</sup>** | **223.126** |
| **Re** | **7** | **5*d*<sup>6</sup> 6*s*<sup>1</sup>** | **226.25** |
| Re_pv | 13 | 5*p*<sup>6</sup> 5*d*<sup>6</sup> 6*s*<sup>1</sup> | 226.25 |
| **Os** | **8** | **5*d*<sup>7</sup> 6*s*<sup>1</sup>** | **228.023** |
| Os_pv | 14 | 5*p*<sup>6</sup> 5*d*<sup>7</sup> 6*s*<sup>1</sup> | 228.023 |
| **Ir** | **9** | **5*d*<sup>8</sup> 6*s*<sup>1</sup>** | **210.837** |
| **Pt** | **10** | **5*d*<sup>9</sup> 6*s*<sup>1</sup>** | **230.228** |
| Pt_pv | 16 | 5*p*<sup>6</sup> 5*d*<sup>9</sup> 6*s*<sup>1</sup> | 294.53 |
| **Au** | **11** | **5*d*<sup>10</sup> 6*s*<sup>1</sup>** | **229.869** |
| **Hg** | **12** | **5*d*<sup>10</sup> 6*s*<sup>2</sup>** | **233.142** |
| Tl | 3 | 6*s*<sup>2</sup> 6*p*<sup>1</sup> | 90.239 |
| **Tl_d** | **13** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>1</sup>** | **237.001** |
| Pb | 4 | 6*s*<sup>2</sup> 6*p*<sup>2</sup> | 98.039 |
| **Pb_d** | **14** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup>** | **237.817** |
| Bi | 5 | 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 105.071 |
| **Bi_d** | **15** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup>** | **242.856** |
| Po | 6 | 6*s*<sup>2</sup> 6*p*<sup>4</sup> | 159.801 |
| **Po_d** | **16** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>4</sup>** | **264.606** |
| **At** | **7** | **6*s*<sup>2</sup> 6*p*<sup>5</sup>** | **161.481** |
| **Rn** | **8** | **6*s*<sup>2</sup> 6*p*<sup>6</sup>** | **151.461** |
| **Fr_sv** | **9** | **6*s*<sup>2</sup> 6*p*<sup>6</sup> 7*s*<sup>1</sup>** | **214.489** |
| **Ra_sv** | **10** | **6*s*<sup>2</sup> 6*p*<sup>6</sup> 7*s*<sup>2</sup>** | **237.216** |
| **Ac** | **11** | **5*f*<sup>0.0001</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>0.9999</sup> 7*s*<sup>2</sup>** | **170.048** |
| **Th** | **12** | **5*f*<sup>1</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>1</sup> 7*s*<sup>2</sup>** | **247.389** |
| Th_s | 10 | 5*f*<sup>1</sup> 6*p*<sup>6</sup> 6*d*<sup>1</sup> 7*s*<sup>2</sup> | 169.575 |
| **Pa** | **13** | **5*f*<sup>1</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **252.31** |
| Pa_s | 11 | 5*f*<sup>1</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 193.642 |
| **U** | **14** | **5*f*<sup>2</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **252.603** |
| U_s | 14 | 5*f*<sup>2</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 209.218 |
| **Np** | **15** | **5*f*<sup>3</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **254.349** |
| Np_s | 15 | 5*f*<sup>3</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 213.932 |
| **Pu** | **16** | **5*f*<sup>4</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **254.436** |
| Pu_s | 16 | 5*f*<sup>4</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 211.493 |
| **Am** | **17** | **5*f*<sup>5</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **255.953** |
| **Cm** | **18** | **5*f*<sup>6</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **258.027** |

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| List of PBE potentials |  |  |  |
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
| H_AE | 1 |  | 1000.0 |
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

#### GW potentials\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: GW potentials">edit</a> \| (./index.php.md)\]

GW potentials are recommended for calculations involving unoccupied
states, e.g., computing
<a href="/wiki/Optical_properties" class="mw-redirect"
title="Optical properties">optical properties</a> or using
<a href="/wiki/Many-body_perturbation_theory" class="mw-redirect"
title="Many-body perturbation theory">many-body perturbation theory</a>.

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| List of LDA potentials |  |  |  |
| Potential name | Number of valence electrons | Valence electron configuration | ENAMX \[eV\] |
| **H_GW** | **1** | **1*s*<sup>1</sup>** | **300.0** |
| H_h_GW | 1 | 1*s*<sup>1</sup> | 700.0 |
| **He_GW** | **2** | **1*s*<sup>2</sup>** | **404.806** |
| Li_AE_GW | 3 | 1*s*<sup>2</sup> 2*p*<sup>1</sup> | 433.253 |
| Li_GW | 1 | 2*s*<sup>1</sup> | 112.417 |
| **Li_sv_GW** | **3** | **1*s*<sup>2</sup> 2*p*<sup>1</sup>** | **433.253** |
| Be_GW | 2 | 2*s*<sup>1.9999</sup> 2*p*<sup>0.001</sup> | 247.951 |
| **Be_sv_GW** | **4** | **1*s*<sup>2</sup> 2*p*<sup>2</sup>** | **536.216** |
| **B_GW** | **3** | **2*s*<sup>2</sup> 2*p*<sup>1</sup>** | **318.762** |
| B_GW_new | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 318.762 |
| **C_GW** | **4** | **2*s*<sup>2</sup> 2*p*<sup>2</sup>** | **413.992** |
| C_GW_new | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 433.894 |
| C_h_GW | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 742.464 |
| C_s_GW | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 304.668 |
| **N_GW** | **5** | **2*s*<sup>2</sup> 2*p*<sup>3</sup>** | **420.681** |
| N_GW_new | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 452.165 |
| N_h_GW | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 755.833 |
| N_s_GW | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 312.431 |
| **O_GW** | **6** | **2*s*<sup>2</sup> 2*p*<sup>4</sup>** | **414.315** |
| O_GW_new | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 466.114 |
| O_h_GW | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 765.442 |
| O_s_GW | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 334.366 |
| **F_GW** | **7** | **2*s*<sup>2</sup> 2*p*<sup>5</sup>** | **487.335** |
| F_GW_new | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 479.919 |
| F_h_GW | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 847.822 |
| **Ne_GW** | **8** | **2*s*<sup>2</sup> 2*p*<sup>6</sup>** | **431.952** |
| Ne_s_GW | 8 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> | 317.594 |
| **Na_sv_GW** | **9** | **2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*p*<sup>1</sup>** | **372.86** |
| Mg_GW | 2 | 3*s*<sup>2</sup> | 126.671 |
| Mg_pv_GW | 8 | 2*p*<sup>6</sup> 3*s*<sup>2</sup> | 403.538 |
| **Mg_sv_GW** | **10** | **2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*d*<sup>2</sup>** | **430.099** |
| **Al_GW** | **3** | **3*s*<sup>2</sup> 3*p*<sup>1</sup>** | **240.957** |
| Al_sv_GW | 11 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>2</sup> 3*p*<sup>1</sup> | 411.007 |
| **Si_GW** | **4** | **3*s*<sup>2</sup> 3*p*<sup>2</sup>** | **245.704** |
| Si_sv_GW | 12 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>2</sup> 3*p*<sup>2</sup> | 546.548 |
| **P_GW** | **5** | **3*s*<sup>2</sup> 3*p*<sup>3</sup>** | **255.155** |
| **S_GW** | **6** | **3*s*<sup>2</sup> 3*p*<sup>4</sup>** | **258.602** |
| **Cl_GW** | **7** | **3*s*<sup>2</sup> 3*p*<sup>5</sup>** | **262.25** |
| **Ar_GW** | **8** | **3*s*<sup>2</sup> 3*p*<sup>6</sup>** | **290.518** |
| **K_sv_GW** | **9** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>1</sup>** | **248.606** |
| **Ca_sv_GW** | **10** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>2</sup>** | **281.209** |
| **Sc_sv_GW** | **11** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>3</sup>** | **378.598** |
| **Ti_sv_GW** | **12** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>4</sup>** | **383.48** |
| **V_sv_GW** | **13** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>5</sup>** | **382.093** |
| **Cr_sv_GW** | **14** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>6</sup>** | **384.753** |
| Mn_GW | 7 | 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 278.537 |
| **Mn_sv_GW** | **15** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>7</sup>** | **384.488** |
| Fe_GW | 8 | 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 321.044 |
| **Fe_sv_GW** | **16** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>8</sup>** | **387.727** |
| Co_GW | 9 | 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 323.447 |
| **Co_sv_GW** | **17** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>9</sup>** | **387.407** |
| Ni_GW | 10 | 3*d*<sup>9</sup> 4*s*<sup>1</sup> | 357.352 |
| **Ni_sv_GW** | **18** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup>** | **389.485** |
| Cu_GW | 11 | 3*d*<sup>10</sup> 4*s*<sup>1</sup> | 417.032 |
| **Cu_sv_GW** | **19** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>1</sup>** | **466.991** |
| Zn_GW | 12 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> | 328.312 |
| **Zn_sv_GW** | **20** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup>** | **401.745** |
| Ga_GW | 3 | 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 134.8 |
| **Ga_d_GW** | **13** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup>** | **404.723** |
| Ga_sv_GW | 21 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 404.723 |
| Ge_GW | 4 | 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 173.969 |
| **Ge_d_GW** | **14** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup>** | **375.614** |
| Ge_sv_GW | 22 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 410.604 |
| **As_GW** | **5** | **4*s*<sup>2</sup> 4*p*<sup>3</sup>** | **208.87** |
| As_sv_GW | 23 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>3</sup> | 415.514 |
| **Se_GW** | **6** | **4*s*<sup>2</sup> 4*p*<sup>4</sup>** | **211.602** |
| Se_sv_GW | 24 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>4</sup> | 469.258 |
| **Br_GW** | **7** | **4*s*<sup>2</sup> 4*p*<sup>5</sup>** | **216.224** |
| Br_sv_GW | 25 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>5</sup> | 475.88 |
| **Kr_GW** | **8** | **4*s*<sup>2</sup> 4*p*<sup>6</sup>** | **252.563** |
| **Rb_sv_GW** | **9** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>1</sup>** | **220.92** |
| **Sr_sv_GW** | **10** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>2</sup>** | **224.532** |
| **Y_sv_GW** | **11** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>3</sup>** | **339.94** |
| **Zr_sv_GW** | **12** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>4</sup>** | **346.437** |
| **Nb_sv_GW** | **13** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>5</sup>** | **353.857** |
| **Mo_sv_GW** | **14** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>6</sup>** | **344.65** |
| **Tc_sv_GW** | **15** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>7</sup>** | **350.798** |
| **Ru_sv_GW** | **16** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>8</sup>** | **347.881** |
| Rh_GW | 9 | 4*d*<sup>8</sup> 5*s*<sup>1</sup> | 247.321 |
| **Rh_sv_GW** | **17** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>9</sup>** | **350.989** |
| Pd_GW | 10 | 4*d*<sup>9</sup> 5*s*<sup>1</sup> | 250.832 |
| **Pd_sv_GW** | **18** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup>** | **355.88** |
| Ag_GW | 11 | 4*d*<sup>10</sup> 5*s*<sup>1</sup> | 249.752 |
| **Ag_sv_GW** | **19** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>11</sup>** | **354.226** |
| Cd_GW | 12 | 4*d*<sup>10</sup> 5*s*<sup>2</sup> | 253.99 |
| **Cd_sv_GW** | **20** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup>** | **361.653** |
| **In_d_GW** | **13** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup>** | **278.582** |
| In_sv_GW | 21 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup> | 366.636 |
| **Sn_d_GW** | **14** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup>** | **260.086** |
| Sn_sv_GW | 22 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup> | 368.704 |
| Sb_GW | 5 | 5*s*<sup>2</sup> 5*p*<sup>3</sup> | 172.301 |
| **Sb_d_GW** | **15** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>3</sup>** | **263.147** |
| Sb_sv_GW | 23 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>3</sup> | 372.498 |
| **Te_GW** | **6** | **5*s*<sup>2</sup> 5*p*<sup>4</sup>** | **175.144** |
| Te_sv_GW | 24 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>4</sup> | 376.686 |
| **I_GW** | **7** | **5*s*<sup>2</sup> 5*p*<sup>5</sup>** | **175.712** |
| I_sv_GW | 25 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>5</sup> | 381.757 |
| **Xe_GW** | **8** | **5*s*<sup>2</sup> 5*p*<sup>6</sup>** | **179.528** |
| Xe_sv_GW | 26 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> | 400.581 |
| **Cs_sv_GW** | **9** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup>** | **198.012** |
| **Ba_sv_GW** | **10** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>2</sup>** | **237.484** |
| **La_GW** | **11** | **4*f*<sup>0.2</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.8</sup> 6*s*<sup>2</sup>** | **313.728** |
| **Ce_GW** | **12** | **4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **304.649** |
| **Hf_sv_GW** | **12** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>4</sup>** | **308.829** |
| **Ta_sv_GW** | **13** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>5</sup>** | **285.798** |
| **W_sv_GW** | **14** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>6</sup>** | **316.943** |
| **Re_sv_GW** | **15** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>7</sup>** | **316.85** |
| **Os_sv_GW** | **16** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>8</sup>** | **319.628** |
| **Ir_sv_GW** | **17** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>9</sup>** | **319.708** |
| Pt_GW | 10 | 5*d*<sup>9</sup> 6*s*<sup>1</sup> | 248.657 |
| **Pt_sv_GW** | **18** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup>** | **323.536** |
| Au_GW | 11 | 5*d*<sup>10</sup> 6*s*<sup>1</sup> | 248.263 |
| **Au_sv_GW** | **19** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>11</sup>** | **306.52** |
| **Hg_sv_GW** | **20** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup>** | **311.949** |
| **Tl_d_GW** | **15** | **5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>1</sup>** | **237.001** |
| Tl_sv_GW | 21 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>1</sup> | 316.502 |
| **Pb_d_GW** | **16** | **5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup>** | **237.793** |
| Pb_sv_GW | 22 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup> | 317.138 |
| Bi_GW | 5 | 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 146.628 |
| **Bi_d_GW** | **17** | **5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup>** | **261.89** |
| Bi_sv_GW | 23 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 323.502 |
| **Po_d_GW** | **18** | **5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>4</sup>** | **267.666** |
| Po_sv_GW | 24 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>4</sup> | 326.653 |
| **At_d_GW** | **17** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>5</sup>** | **266.303** |
| At_sv_GW | 25 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>5</sup> | 328.597 |
| **Rn_d_GW** | **18** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup>** | **267.397** |
| Rn_sv_GW | 26 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> | 329.841 |

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| List of PBE potentials |  |  |  |
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

### potpaw.54\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: potpaw.54">edit</a> \| (./index.php.md)\]

LDA and PBE PAW datasets version 54, including the GW variety (original
release 2015-09-04). When read by VASP these files yield identical
results as the files distributed before. The POTCAR files, however,
differ from previous versions:

1.  the TITLE string is set to the directory in which the POTCAR file
    reside for: O_GW_new, Ge_GW, G_GW_new, Cd_GW, Br_GW, B_GW.
2.  HASH key added to all POTCAR files.

#### Standard potentials\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Standard potentials">edit</a> \| (./index.php.md)\]

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| List of LDA potentials |  |  |  |
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
| H_AE | 1 |  | 1000.0 |
| H_h | 1 | 1*s*<sup>1</sup> | 700.0 |
| H_s | 1 | 1*s*<sup>1</sup> | 200.0 |
| **He** | **2** | **1*s*<sup>2</sup>** | **477.779** |
| Li | 1 | 2*s*<sup>1</sup> | 140.0 |
| **Li_sv** | **3** | **1*s*<sup>2</sup> 2*s*<sup>1</sup>** | **498.387** |
| **Be** | **2** | **2*s*<sup>1.9999</sup> 2*p*<sup>0.001</sup>** | **247.951** |
| Be_sv | 4 | 1*s*<sup>2</sup> 2*s*<sup>1.9999</sup> 2*p*<sup>0.001</sup> | 308.45 |
| **B** | **3** | **2*s*<sup>2</sup> 2*p*<sup>1</sup>** | **318.762** |
| B_h | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 700.0 |
| B_s | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 269.251 |
| **C** | **4** | **2*s*<sup>2</sup> 2*p*<sup>2</sup>** | **400.0** |
| C_h | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 700.0 |
| C_s | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 273.704 |
| **N** | **5** | **2*s*<sup>2</sup> 2*p*<sup>3</sup>** | **400.0** |
| N_h | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 700.0 |
| N_s | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 279.424 |
| **O** | **6** | **2*s*<sup>2</sup> 2*p*<sup>4</sup>** | **400.0** |
| O_h | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 700.0 |
| O_s | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 282.604 |
| **F** | **7** | **2*s*<sup>2</sup> 2*p*<sup>5</sup>** | **400.0** |
| F_h | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 772.351 |
| F_s | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 289.647 |
| **Ne** | **8** | **2*s*<sup>2</sup> 2*p*<sup>6</sup>** | **343.403** |
| Na | 1 | 3*s*<sup>1</sup> | 101.956 |
| **Na_pv** | **7** | **2*p*<sup>6</sup> 3*s*<sup>1</sup>** | **259.494** |
| Na_sv | 9 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>1</sup> | 644.874 |
| **Mg** | **2** | **3*s*<sup>1.999</sup> 3*p*<sup>0.001</sup>** | **200.0** |
| Mg_pv | 8 | 2*p*<sup>6</sup> 3*s*<sup>2</sup> | 403.538 |
| Mg_sv | 10 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>2</sup> | 473.54 |
| **Al** | **3** | **3*s*<sup>2</sup> 3*p*<sup>1</sup>** | **240.957** |
| **Si** | **4** | **3*s*<sup>2</sup> 3*p*<sup>2</sup>** | **245.704** |
| **P** | **5** | **3*s*<sup>2</sup> 3*p*<sup>3</sup>** | **255.155** |
| P_h | 5 | 3*s*<sup>2</sup> 3*p*<sup>3</sup> | 390.903 |
| **S** | **6** | **3*s*<sup>2</sup> 3*p*<sup>4</sup>** | **258.602** |
| S_h | 6 | 3*s*<sup>2</sup> 3*p*<sup>4</sup> | 402.84 |
| **Cl** | **7** | **3*s*<sup>2</sup> 3*p*<sup>5</sup>** | **262.25** |
| Cl_h | 7 | 3*s*<sup>2</sup> 3*p*<sup>5</sup> | 409.272 |
| **Ar** | **8** | **3*s*<sup>2</sup> 3*p*<sup>6</sup>** | **266.101** |
| K_pv | 7 | 3*p*<sup>6</sup> 4*s*<sup>1</sup> | 116.596 |
| **K_sv** | **9** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 4*s*<sup>1</sup>** | **259.279** |
| Ca_pv | 8 | 3*p*<sup>6</sup> 4*s*<sup>2</sup> | 119.552 |
| **Ca_sv** | **10** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 4*s*<sup>2</sup>** | **266.727** |
| Sc | 3 | 3*d*<sup>2</sup> 4*s*<sup>1</sup> | 155.006 |
| **Sc_sv** | **11** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>2</sup> 4*s*<sup>1</sup>** | **222.7** |
| Ti | 4 | 3*d*<sup>3</sup> 4*s*<sup>1</sup> | 178.52 |
| Ti_pv | 10 | 3*p*<sup>6</sup> 3*d*<sup>3</sup> 4*s*<sup>1</sup> | 222.435 |
| **Ti_sv** | **12** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>3</sup> 4*s*<sup>1</sup>** | **274.719** |
| V | 5 | 3*d*<sup>4</sup> 4*s*<sup>1</sup> | 192.706 |
| V_pv | 11 | 3*p*<sup>6</sup> 3*d*<sup>4</sup> 4*s*<sup>1</sup> | 263.722 |
| **V_sv** | **13** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>4</sup> 4*s*<sup>1</sup>** | **263.722** |
| Cr | 6 | 3*d*<sup>5</sup> 4*s*<sup>1</sup> | 227.202 |
| **Cr_pv** | **12** | **3*p*<sup>6</sup> 3*d*<sup>5</sup> 4*s*<sup>1</sup>** | **265.753** |
| Cr_sv | 14 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>5</sup> 4*s*<sup>1</sup> | 395.443 |
| Mn | 7 | 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 269.944 |
| **Mn_pv** | **13** | **3*p*<sup>6</sup> 3*d*<sup>6</sup> 4*s*<sup>1</sup>** | **269.944** |
| Mn_sv | 15 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 387.112 |
| **Fe** | **8** | **3*d*<sup>7</sup> 4*s*<sup>1</sup>** | **267.969** |
| Fe_pv | 14 | 3*p*<sup>6</sup> 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 293.303 |
| Fe_sv | 16 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 390.513 |
| **Co** | **9** | **3*d*<sup>8</sup> 4*s*<sup>1</sup>** | **268.056** |
| Co_pv | 15 | 3*p*<sup>6</sup> 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 270.871 |
| Co_sv | 17 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 390.343 |
| **Ni** | **10** | **3*d*<sup>9</sup> 4*s*<sup>1</sup>** | **269.618** |
| Ni_pv | 16 | 3*p*<sup>6</sup> 3*d*<sup>9</sup> 4*s*<sup>1</sup> | 367.726 |
| **Cu** | **11** | **3*d*<sup>10</sup> 4*s*<sup>1</sup>** | **295.521** |
| Cu_pv | 17 | 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>1</sup> | 368.406 |
| **Zn** | **12** | **3*d*<sup>10</sup> 4*s*<sup>2</sup>** | **276.847** |
| Ga | 3 | 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 134.8 |
| **Ga_d** | **13** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup>** | **282.829** |
| Ga_h | 13 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 404.723 |
| Ge | 4 | 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 173.969 |
| **Ge_d** | **14** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup>** | **310.448** |
| Ge_h | 14 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 410.604 |
| **As** | **5** | **4*s*<sup>2</sup> 4*p*<sup>3</sup>** | **208.87** |
| As_d | 15 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>3</sup> | 288.762 |
| **Se** | **6** | **4*s*<sup>2</sup> 4*p*<sup>4</sup>** | **211.602** |
| **Br** | **7** | **4*s*<sup>2</sup> 4*p*<sup>5</sup>** | **216.224** |
| **Kr** | **8** | **4*s*<sup>2</sup> 4*p*<sup>6</sup>** | **185.392** |
| Rb_pv | 7 | 4*p*<sup>6</sup> 4*d*<sup>0.001</sup> 5*s*<sup>0.999</sup> | 122.21 |
| **Rb_sv** | **9** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>0.001</sup> 5*s*<sup>0.999</sup>** | **220.215** |
| **Sr_sv** | **10** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>0.001</sup> 5*s*<sup>1.999</sup>** | **226.327** |
| **Y_sv** | **11** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>2</sup> 5*s*<sup>1</sup>** | **202.554** |
| **Zr_sv** | **12** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>3</sup> 5*s*<sup>1</sup>** | **230.037** |
| Nb_pv | 11 | 4*p*<sup>6</sup> 4*d*<sup>4</sup> 5*s*<sup>1</sup> | 207.263 |
| **Nb_sv** | **13** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>4</sup> 5*s*<sup>1</sup>** | **293.304** |
| Mo | 6 | 4*d*<sup>5</sup> 5*s*<sup>1</sup> | 224.535 |
| Mo_pv | 12 | 4*p*<sup>6</sup> 4*d*<sup>5</sup> 5*s*<sup>1</sup> | 224.535 |
| **Mo_sv** | **14** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>5</sup> 5*s*<sup>1</sup>** | **236.514** |
| Tc | 7 | 4*d*<sup>6</sup> 5*s*<sup>1</sup> | 228.636 |
| **Tc_pv** | **13** | **4*p*<sup>6</sup> 4*d*<sup>6</sup> 5*s*<sup>1</sup>** | **263.345** |
| Tc_sv | 15 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>6</sup> 5*s*<sup>1</sup> | 318.479 |
| Ru | 8 | 4*d*<sup>7</sup> 5*s*<sup>1</sup> | 213.221 |
| **Ru_pv** | **14** | **4*p*<sup>6</sup> 4*d*<sup>7</sup> 5*s*<sup>1</sup>** | **239.907** |
| Ru_sv | 16 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>7</sup> 5*s*<sup>1</sup> | 318.687 |
| Rh | 9 | 4*d*<sup>8</sup> 5*s*<sup>1</sup> | 228.926 |
| **Rh_pv** | **15** | **4*p*<sup>6</sup> 4*d*<sup>8</sup> 5*s*<sup>1</sup>** | **247.321** |
| **Pd** | **10** | **4*d*<sup>9</sup> 5*s*<sup>1</sup>** | **250.832** |
| Pd_pv | 16 | 4*p*<sup>6</sup> 4*d*<sup>9</sup> 5*s*<sup>1</sup> | 250.832 |
| **Ag** | **11** | **4*d*<sup>10</sup> 5*s*<sup>1</sup>** | **249.752** |
| Ag_pv | 17 | 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>1</sup> | 297.68 |
| **Cd** | **12** | **4*d*<sup>10</sup> 5*s*<sup>2</sup>** | **274.265** |
| In | 3 | 5*s*<sup>2</sup> 5*p*<sup>1</sup> | 96.062 |
| **In_d** | **13** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup>** | **239.196** |
| Sn | 4 | 5*s*<sup>2</sup> 5*p*<sup>2</sup> | 103.318 |
| **Sn_d** | **14** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup>** | **241.107** |
| **Sb** | **5** | **5*s*<sup>2</sup> 5*p*<sup>3</sup>** | **172.301** |
| **Te** | **6** | **5*s*<sup>2</sup> 5*p*<sup>4</sup>** | **175.144** |
| **I** | **7** | **5*s*<sup>2</sup> 5*p*<sup>5</sup>** | **175.712** |
| **Xe** | **8** | **5*s*<sup>2</sup> 5*p*<sup>6</sup>** | **153.021** |
| **Cs_sv** | **9** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 6*s*<sup>1</sup>** | **220.727** |
| **Ba_sv** | **10** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.001</sup> 6*s*<sup>1.999</sup>** | **186.981** |
| **La** | **11** | **4*f*<sup>0.0001</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.9999</sup> 6*s*<sup>2</sup>** | **219.044** |
| La_s | 9 | 4*f*<sup>0.0001</sup> 5*p*<sup>6</sup> 5*d*<sup>0.9999</sup> 6*s*<sup>2</sup> | 136.594 |
| **Ce** | **12** | **4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **273.088** |
| Ce_h | 12 | 4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 299.927 |
| Hf | 4 | 5*d*<sup>3</sup> 6*s*<sup>1</sup> | 220.431 |
| **Hf_pv** | **10** | **5*p*<sup>6</sup> 5*d*<sup>3</sup> 6*s*<sup>1</sup>** | **220.431** |
| Hf_sv | 12 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>4</sup> | 237.414 |
| Ta | 5 | 5*d*<sup>4</sup> 6*s*<sup>1</sup> | 223.759 |
| **Ta_pv** | **11** | **5*p*<sup>6</sup> 5*d*<sup>4</sup> 6*s*<sup>1</sup>** | **223.759** |
| W | 6 | 5*d*<sup>5</sup> 6*s*<sup>1</sup> | 223.126 |
| **W_sv** | **14** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>5</sup> 6*s*<sup>1</sup>** | **223.126** |
| **Re** | **7** | **5*d*<sup>6</sup> 6*s*<sup>1</sup>** | **226.25** |
| Re_pv | 13 | 5*p*<sup>6</sup> 5*d*<sup>6</sup> 6*s*<sup>1</sup> | 226.25 |
| **Os** | **8** | **5*d*<sup>7</sup> 6*s*<sup>1</sup>** | **228.023** |
| Os_pv | 14 | 5*p*<sup>6</sup> 5*d*<sup>7</sup> 6*s*<sup>1</sup> | 228.023 |
| **Ir** | **9** | **5*d*<sup>8</sup> 6*s*<sup>1</sup>** | **210.837** |
| **Pt** | **10** | **5*d*<sup>9</sup> 6*s*<sup>1</sup>** | **230.228** |
| Pt_pv | 16 | 5*p*<sup>6</sup> 5*d*<sup>9</sup> 6*s*<sup>1</sup> | 294.53 |
| **Au** | **11** | **5*d*<sup>10</sup> 6*s*<sup>1</sup>** | **229.869** |
| **Hg** | **12** | **5*d*<sup>10</sup> 6*s*<sup>2</sup>** | **233.142** |
| Tl | 3 | 6*s*<sup>2</sup> 6*p*<sup>1</sup> | 90.239 |
| **Tl_d** | **13** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>1</sup>** | **237.001** |
| Pb | 4 | 6*s*<sup>2</sup> 6*p*<sup>2</sup> | 98.039 |
| **Pb_d** | **14** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup>** | **237.817** |
| Bi | 5 | 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 105.071 |
| **Bi_d** | **15** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup>** | **242.856** |
| Po | 6 | 6*s*<sup>2</sup> 6*p*<sup>4</sup> | 159.801 |
| **Po_d** | **16** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>4</sup>** | **264.606** |
| **At** | **7** | **6*s*<sup>2</sup> 6*p*<sup>5</sup>** | **161.481** |
| **Rn** | **8** | **6*s*<sup>2</sup> 6*p*<sup>6</sup>** | **152.086** |
| **Fr_sv** | **9** | **6*s*<sup>2</sup> 6*p*<sup>6</sup> 7*s*<sup>1</sup>** | **214.489** |
| **Ra_sv** | **10** | **6*s*<sup>2</sup> 6*p*<sup>6</sup> 7*s*<sup>2</sup>** | **237.216** |
| **Ac** | **11** | **5*f*<sup>0.0001</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>0.9999</sup> 7*s*<sup>2</sup>** | **170.048** |
| **Th** | **12** | **5*f*<sup>1</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>1</sup> 7*s*<sup>2</sup>** | **247.389** |
| Th_s | 10 | 5*f*<sup>1</sup> 6*p*<sup>6</sup> 6*d*<sup>1</sup> 7*s*<sup>2</sup> | 169.575 |
| **Pa** | **13** | **5*f*<sup>1</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **252.31** |
| Pa_s | 11 | 5*f*<sup>1</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 193.642 |
| **U** | **14** | **5*f*<sup>2</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **252.603** |
| U_s | 14 | 5*f*<sup>2</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 209.218 |
| **Np** | **15** | **5*f*<sup>3</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **254.349** |
| Np_s | 15 | 5*f*<sup>3</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 213.932 |
| **Pu** | **16** | **5*f*<sup>4</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **254.436** |
| Pu_s | 16 | 5*f*<sup>4</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 211.493 |
| **Am** | **17** | **5*f*<sup>5</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **255.953** |
| **Cm** | **18** | **5*f*<sup>6</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **258.027** |

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| List of PBE potentials |  |  |  |
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
| H_AE | 1 |  | 1000.0 |
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
| C_h | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 700.0 |
| C_s | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 273.911 |
| **N** | **5** | **2*s*<sup>2</sup> 2*p*<sup>3</sup>** | **400.0** |
| N_h | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 700.0 |
| N_s | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 279.692 |
| **O** | **6** | **2*s*<sup>2</sup> 2*p*<sup>4</sup>** | **400.0** |
| O_h | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 700.0 |
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
| Pr | 13 | 4*f*<sup>2</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 272.941 |
| **Pr_3** | **11** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **181.719** |
| Nd | 14 | 4*f*<sup>3</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 253.189 |
| **Nd_3** | **11** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **182.619** |
| Pm | 15 | 4*f*<sup>4</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 258.627 |
| **Pm_3** | **11** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **176.959** |
| Sm | 16 | 4*f*<sup>5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 257.515 |
| **Sm_3** | **11** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **177.087** |
| Eu | 17 | 4*f*<sup>7</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 6*s*<sup>2</sup> | 249.668 |
| **Eu_2** | **8** | **5*p*<sup>6</sup> 6*s*<sup>2</sup>** | **99.328** |
| Eu_3 | 9 | 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 129.057 |
| Gd | 18 | 4*f*<sup>7</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 256.472 |
| **Gd_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **154.332** |
| Tb | 19 | 4*f*<sup>8</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 264.824 |
| **Tb_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **155.613** |
| Dy | 20 | 4*f*<sup>9</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 255.467 |
| **Dy_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **155.713** |
| Ho | 21 | 4*f*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 257.168 |
| **Ho_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **154.137** |
| Er | 22 | 4*f*<sup>11</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 298.116 |
| Er_2 | 8 | 5*p*<sup>6</sup> 6*s*<sup>2</sup> | 119.75 |
| **Er_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **155.037** |
| Tm | 23 | 4*f*<sup>12</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 257.42 |
| **Tm_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **149.221** |
| Yb | 24 | 4*f*<sup>14</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 6*s*<sup>2</sup> | 253.028 |
| **Yb_2** | **8** | **5*p*<sup>6</sup> 6*s*<sup>2</sup>** | **112.578** |
| Yb_3 | 9 | 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 188.359 |
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
| **Rn** | **8** | **6*s*<sup>2</sup> 6*p*<sup>6</sup>** | **152.121** |
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

#### GW potentials\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: GW potentials">edit</a> \| (./index.php.md)\]

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| List of LDA potentials |  |  |  |
| Potential name | Number of valence electrons | Valence electron configuration | ENAMX \[eV\] |
| **H_GW** | **1** | **1*s*<sup>1</sup>** | **300.0** |
| H_h_GW | 1 | 1*s*<sup>1</sup> | 700.0 |
| **He_GW** | **2** | **1*s*<sup>2</sup>** | **404.806** |
| Li_AE_GW | 3 | 1*s*<sup>2</sup> 2*p*<sup>1</sup> | 433.253 |
| Li_GW | 1 | 2*s*<sup>1</sup> | 112.417 |
| **Li_sv_GW** | **3** | **1*s*<sup>2</sup> 2*p*<sup>1</sup>** | **433.253** |
| Be_GW | 2 | 2*s*<sup>1.9999</sup> 2*p*<sup>0.001</sup> | 247.951 |
| **Be_sv_GW** | **4** | **1*s*<sup>2</sup> 2*p*<sup>2</sup>** | **536.216** |
| **B_GW** | **3** | **2*s*<sup>2</sup> 2*p*<sup>1</sup>** | **318.762** |
| **C_GW** | **4** | **2*s*<sup>2</sup> 2*p*<sup>2</sup>** | **413.992** |
| C_GW_new | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 413.992 |
| C_h_GW | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 742.464 |
| **N_GW** | **5** | **2*s*<sup>2</sup> 2*p*<sup>3</sup>** | **420.681** |
| N_GW_new | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 420.681 |
| N_h_GW | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 755.833 |
| N_s_GW | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 296.222 |
| **O_GW** | **6** | **2*s*<sup>2</sup> 2*p*<sup>4</sup>** | **414.315** |
| O_GW_new | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 433.745 |
| O_h_GW | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 765.442 |
| O_s_GW | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 334.366 |
| **F_GW** | **7** | **2*s*<sup>2</sup> 2*p*<sup>5</sup>** | **487.335** |
| F_GW_new | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 487.335 |
| F_h_GW | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 847.822 |
| **Ne_GW** | **8** | **2*s*<sup>2</sup> 2*p*<sup>6</sup>** | **431.952** |
| Ne_s_GW | 8 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> | 317.594 |
| **Na_sv_GW** | **9** | **2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*p*<sup>1</sup>** | **372.86** |
| Mg_GW | 2 | 3*s*<sup>2</sup> | 126.671 |
| Mg_pv_GW | 8 | 2*p*<sup>6</sup> 3*s*<sup>2</sup> | 403.538 |
| **Mg_sv_GW** | **10** | **2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*d*<sup>2</sup>** | **430.099** |
| **Al_GW** | **3** | **3*s*<sup>2</sup> 3*p*<sup>1</sup>** | **240.957** |
| Al_sv_GW | 11 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>2</sup> 3*p*<sup>1</sup> | 411.007 |
| **Si_GW** | **4** | **3*s*<sup>2</sup> 3*p*<sup>2</sup>** | **245.704** |
| Si_sv_GW | 12 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>2</sup> 3*p*<sup>2</sup> | 546.548 |
| **P_GW** | **5** | **3*s*<sup>2</sup> 3*p*<sup>3</sup>** | **255.155** |
| **S_GW** | **6** | **3*s*<sup>2</sup> 3*p*<sup>4</sup>** | **258.602** |
| **Cl_GW** | **7** | **3*s*<sup>2</sup> 3*p*<sup>5</sup>** | **262.25** |
| **Ar_GW** | **8** | **3*s*<sup>2</sup> 3*p*<sup>6</sup>** | **290.518** |
| **K_sv_GW** | **9** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>1</sup>** | **248.606** |
| **Ca_sv_GW** | **10** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>2</sup>** | **281.209** |
| **Sc_sv_GW** | **11** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>3</sup>** | **378.598** |
| **Ti_sv_GW** | **12** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>4</sup>** | **383.48** |
| **V_sv_GW** | **13** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>5</sup>** | **382.093** |
| **Cr_sv_GW** | **14** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>6</sup>** | **384.753** |
| Mn_GW | 7 | 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 278.537 |
| **Mn_sv_GW** | **15** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>7</sup>** | **384.488** |
| Fe_GW | 8 | 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 321.044 |
| **Fe_sv_GW** | **16** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>8</sup>** | **387.727** |
| Co_GW | 9 | 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 323.447 |
| **Co_sv_GW** | **17** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>9</sup>** | **387.407** |
| Ni_GW | 10 | 3*d*<sup>9</sup> 4*s*<sup>1</sup> | 357.352 |
| **Ni_sv_GW** | **18** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup>** | **389.485** |
| Cu_GW | 11 | 3*d*<sup>10</sup> 4*s*<sup>1</sup> | 417.032 |
| **Cu_sv_GW** | **19** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>1</sup>** | **391.702** |
| Zn_GW | 12 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> | 328.312 |
| **Zn_sv_GW** | **20** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup>** | **401.745** |
| Ga_GW | 3 | 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 134.8 |
| **Ga_d_GW** | **13** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup>** | **404.723** |
| Ga_sv_GW | 21 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 404.723 |
| Ge_GW | 4 | 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 173.969 |
| **Ge_d_GW** | **14** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup>** | **375.614** |
| Ge_sv_GW | 22 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 410.604 |
| **As_GW** | **5** | **4*s*<sup>2</sup> 4*p*<sup>3</sup>** | **208.87** |
| As_sv_GW | 23 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>3</sup> | 415.514 |
| **Se_GW** | **6** | **4*s*<sup>2</sup> 4*p*<sup>4</sup>** | **211.602** |
| Se_sv_GW | 24 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>4</sup> | 469.258 |
| **Br_GW** | **7** | **4*s*<sup>2</sup> 4*p*<sup>5</sup>** | **216.224** |
| Br_sv_GW | 25 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>5</sup> | 475.88 |
| **Kr_GW** | **8** | **4*s*<sup>2</sup> 4*p*<sup>6</sup>** | **252.563** |
| **Rb_sv_GW** | **9** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>1</sup>** | **220.92** |
| **Sr_sv_GW** | **10** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>2</sup>** | **224.532** |
| **Y_sv_GW** | **11** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>3</sup>** | **339.94** |
| **Zr_sv_GW** | **12** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>4</sup>** | **346.437** |
| **Nb_sv_GW** | **13** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>5</sup>** | **353.857** |
| **Mo_sv_GW** | **14** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>6</sup>** | **344.65** |
| **Tc_sv_GW** | **15** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>7</sup>** | **350.798** |
| **Ru_sv_GW** | **16** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>8</sup>** | **347.881** |
| Rh_GW | 9 | 4*d*<sup>8</sup> 5*s*<sup>1</sup> | 247.321 |
| **Rh_sv_GW** | **17** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>9</sup>** | **350.989** |
| Pd_GW | 10 | 4*d*<sup>9</sup> 5*s*<sup>1</sup> | 250.832 |
| **Pd_sv_GW** | **18** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup>** | **355.88** |
| Ag_GW | 11 | 4*d*<sup>10</sup> 5*s*<sup>1</sup> | 249.752 |
| **Ag_sv_GW** | **19** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>11</sup>** | **354.226** |
| Cd_GW | 12 | 4*d*<sup>10</sup> 5*s*<sup>2</sup> | 253.99 |
| **Cd_sv_GW** | **20** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup>** | **361.653** |
| **In_d_GW** | **13** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup>** | **278.582** |
| In_sv_GW | 21 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup> | 366.636 |
| **Sn_d_GW** | **14** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup>** | **260.086** |
| Sn_sv_GW | 22 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup> | 368.704 |
| Sb_GW | 5 | 5*s*<sup>2</sup> 5*p*<sup>3</sup> | 172.301 |
| **Sb_d_GW** | **15** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>3</sup>** | **263.147** |
| Sb_sv_GW | 23 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>3</sup> | 372.498 |
| **Te_GW** | **6** | **5*s*<sup>2</sup> 5*p*<sup>4</sup>** | **175.144** |
| Te_sv_GW | 24 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>4</sup> | 376.686 |
| **I_GW** | **7** | **5*s*<sup>2</sup> 5*p*<sup>5</sup>** | **175.712** |
| I_sv_GW | 25 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>5</sup> | 381.757 |
| **Xe_GW** | **8** | **5*s*<sup>2</sup> 5*p*<sup>6</sup>** | **179.528** |
| Xe_sv_GW | 26 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> | 400.581 |
| **Cs_sv_GW** | **9** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup>** | **198.012** |
| **Ba_sv_GW** | **10** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>2</sup>** | **237.484** |
| **La_GW** | **11** | **4*f*<sup>0.2</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.8</sup> 6*s*<sup>2</sup>** | **313.728** |
| **Ce_GW** | **12** | **4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **304.649** |
| **Hf_sv_GW** | **12** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>4</sup>** | **282.716** |
| **Ta_sv_GW** | **13** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>5</sup>** | **285.798** |
| **W_sv_GW** | **14** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>6</sup>** | **316.943** |
| **Re_sv_GW** | **15** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>7</sup>** | **316.85** |
| **Os_sv_GW** | **16** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>8</sup>** | **319.628** |
| **Ir_sv_GW** | **17** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>9</sup>** | **319.708** |
| Pt_GW | 10 | 5*d*<sup>9</sup> 6*s*<sup>1</sup> | 248.657 |
| **Pt_sv_GW** | **18** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup>** | **323.536** |
| Au_GW | 11 | 5*d*<sup>10</sup> 6*s*<sup>1</sup> | 248.263 |
| **Au_sv_GW** | **19** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>11</sup>** | **306.52** |
| **Hg_sv_GW** | **20** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup>** | **311.949** |
| **Tl_d_GW** | **15** | **5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>1</sup>** | **237.001** |
| Tl_sv_GW | 21 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>1</sup> | 316.502 |
| **Pb_d_GW** | **16** | **5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup>** | **237.793** |
| Pb_sv_GW | 22 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup> | 317.138 |
| Bi_GW | 5 | 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 146.628 |
| **Bi_d_GW** | **17** | **5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup>** | **261.89** |
| Bi_sv_GW | 23 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 323.502 |
| **Po_d_GW** | **18** | **5*s*<sup>2</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>4</sup>** | **267.666** |
| Po_sv_GW | 24 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>4</sup> | 326.653 |
| **At_d_GW** | **17** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>5</sup>** | **266.303** |
| At_sv_GW | 25 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>5</sup> | 328.597 |
| **Rn_d_GW** | **18** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup>** | **268.546** |
| Rn_sv_GW | 26 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> | 331.257 |

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| List of PBE potentials |  |  |  |
| Potential name | Number of valence electrons | Valence electron configuration | ENAMX \[eV\] |
| **H_GW** | **1** | **1*s*<sup>1</sup>** | **300.0** |
| H_h_GW | 1 | 1*s*<sup>1</sup> | 700.0 |
| **He_GW** | **2** | **1*s*<sup>2</sup>** | **405.78** |
| Li_AE_GW | 3 | 1*s*<sup>2</sup> 2*p*<sup>1</sup> | 433.699 |
| Li_GW | 1 | 2*s*<sup>1</sup> | 112.104 |
| **Li_sv_GW** | **3** | **1*s*<sup>2</sup> 2*p*<sup>1</sup>** | **433.699** |
| Be_GW | 2 | 2*s*<sup>1.9999</sup> 2*p*<sup>0.001</sup> | 247.543 |
| **Be_sv_GW** | **4** | **1*s*<sup>2</sup> 2*p*<sup>2</sup>** | **537.454** |
| **B_GW** | **3** | **2*s*<sup>2</sup> 2*p*<sup>1</sup>** | **318.614** |
| **C_GW** | **4** | **2*s*<sup>2</sup> 2*p*<sup>2</sup>** | **413.992** |
| C_GW_new | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 413.992 |
| C_h_GW | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 741.689 |
| **N_GW** | **5** | **2*s*<sup>2</sup> 2*p*<sup>3</sup>** | **420.902** |
| N_GW_new | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 420.902 |
| N_h_GW | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 755.582 |
| N_s_GW | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 296.495 |
| **O_GW** | **6** | **2*s*<sup>2</sup> 2*p*<sup>4</sup>** | **414.635** |
| O_GW_new | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 434.431 |
| O_h_GW | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 765.519 |
| O_s_GW | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 334.664 |
| **F_GW** | **7** | **2*s*<sup>2</sup> 2*p*<sup>5</sup>** | **487.698** |
| F_GW_new | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 487.698 |
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
| **Cu_sv_GW** | **19** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>1</sup>** | **391.688** |
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
| **Ba_sv_GW** | **10** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>2</sup>** | **237.515** |
| **La_GW** | **11** | **4*f*<sup>0.2</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.8</sup> 6*s*<sup>2</sup>** | **313.688** |
| **Ce_GW** | **12** | **4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **304.625** |
| **Hf_sv_GW** | **12** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>4</sup>** | **282.964** |
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
| **Rn_d_GW** | **18** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup>** | **268.495** |
| Rn_sv_GW | 26 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> | 331.173 |

### potpaw.52\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: potpaw.52">edit</a> \| (./index.php.md)\]

PBE and LDA PAW datasets version 52, including early GW variety
(snapshot 19-04-2012). When read by VASP these files yield identical
results as the files distributed in 2012. The POTCAR files, however,
differ from previous versions:

1.  the TITLE string is set to the directory in which the POTCAR file
    reside for: B_GW Br_GW Cd_GW Cd_pv_GW Cd_sv_GW F_GW_new Ge_GW H_AE
    Ne_GW_soft O_GW_new Pb_d_GW.
2.  For PBE GW the TITLE string has been updated from PAW to PAW_PBE.
3.  HASH key added to all POTCAR files.

|  |
|----|
| **Mind:** The C_GW_new, N_GW_new, O_GW_new, and F_GW_new [POTCAR](POTCAR.md) files, use the f-pseudopotential as local potential and possess d-projectors. In contrast, the C_GW, N_GW, O_GW, and F_GW [POTCAR](POTCAR.md) files use the d-pseudopotential as local potential and possess no d-projectors. Calculations usually converge faster with respect to the energy cutoff <a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> using the C_GW, N_GW, O_GW, and G_GW potentials. Whether the new potentials possess a precision advantage over the old potentials is not entirely clear. In theory, they should be more precise for correlated wavefunction calculations. However, in practice, the improvements seem modest and often do not justify the greater computational load. |

#### Standard potentials\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Standard potentials">edit</a> \| (./index.php.md)\]

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| List of LDA potentials |  |  |  |
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
| H_AE | 1 |  | 1000.0 |
| H_h | 1 | 1*s*<sup>1</sup> | 700.0 |
| H_s | 1 | 1*s*<sup>1</sup> | 200.0 |
| **He** | **2** | **1*s*<sup>2</sup>** | **477.779** |
| Li | 1 | 2*s*<sup>1</sup> | 140.0 |
| **Li_sv** | **3** | **1*s*<sup>2</sup> 2*s*<sup>1</sup>** | **498.387** |
| **Be** | **2** | **2*s*<sup>1.9999</sup> 2*p*<sup>0.001</sup>** | **247.951** |
| Be_sv | 4 | 1*s*<sup>2</sup> 2*s*<sup>1.9999</sup> 2*p*<sup>0.001</sup> | 308.45 |
| **B** | **3** | **2*s*<sup>2</sup> 2*p*<sup>1</sup>** | **318.762** |
| B_h | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 700.0 |
| B_s | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 269.251 |
| **C** | **4** | **2*s*<sup>2</sup> 2*p*<sup>2</sup>** | **400.0** |
| C_h | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 700.0 |
| C_s | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 273.704 |
| **N** | **5** | **2*s*<sup>2</sup> 2*p*<sup>3</sup>** | **400.0** |
| N_h | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 700.0 |
| N_s | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 279.424 |
| **O** | **6** | **2*s*<sup>2</sup> 2*p*<sup>4</sup>** | **400.0** |
| O_h | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 700.0 |
| O_s | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 282.604 |
| **F** | **7** | **2*s*<sup>2</sup> 2*p*<sup>5</sup>** | **400.0** |
| F_h | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 700.0 |
| F_s | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 289.647 |
| **Ne** | **8** | **2*s*<sup>2</sup> 2*p*<sup>6</sup>** | **343.403** |
| Na | 1 | 3*s*<sup>1</sup> | 101.956 |
| **Na_pv** | **7** | **2*p*<sup>6</sup> 3*s*<sup>1</sup>** | **259.494** |
| Na_sv | 9 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>1</sup> | 644.874 |
| **Mg** | **2** | **3*s*<sup>1.999</sup> 3*p*<sup>0.001</sup>** | **213.415** |
| Mg_pv | 8 | 2*p*<sup>6</sup> 3*s*<sup>2</sup> | 403.538 |
| Mg_sv | 10 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>2</sup> | 473.54 |
| **Al** | **3** | **3*s*<sup>2</sup> 3*p*<sup>1</sup>** | **240.957** |
| **Si** | **4** | **3*s*<sup>2</sup> 3*p*<sup>2</sup>** | **245.704** |
| **P** | **5** | **3*s*<sup>2</sup> 3*p*<sup>3</sup>** | **255.155** |
| P_h | 5 | 3*s*<sup>2</sup> 3*p*<sup>3</sup> | 390.903 |
| **S** | **6** | **3*s*<sup>2</sup> 3*p*<sup>4</sup>** | **258.602** |
| S_h | 6 | 3*s*<sup>2</sup> 3*p*<sup>4</sup> | 402.84 |
| **Cl** | **7** | **3*s*<sup>2</sup> 3*p*<sup>5</sup>** | **262.25** |
| Cl_h | 7 | 3*s*<sup>2</sup> 3*p*<sup>5</sup> | 409.272 |
| **Ar** | **8** | **3*s*<sup>2</sup> 3*p*<sup>6</sup>** | **266.101** |
| K_pv | 7 | 3*p*<sup>6</sup> 4*s*<sup>1</sup> | 116.596 |
| **K_sv** | **9** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 4*s*<sup>1</sup>** | **259.279** |
| Ca_pv | 8 | 3*p*<sup>6</sup> 4*s*<sup>2</sup> | 119.552 |
| **Ca_sv** | **10** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 4*s*<sup>2</sup>** | **266.727** |
| Sc | 3 | 3*d*<sup>2</sup> 4*s*<sup>1</sup> | 155.006 |
| **Sc_sv** | **11** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>2</sup> 4*s*<sup>1</sup>** | **222.7** |
| Ti | 4 | 3*d*<sup>3</sup> 4*s*<sup>1</sup> | 178.52 |
| Ti_pv | 10 | 3*p*<sup>6</sup> 3*d*<sup>3</sup> 4*s*<sup>1</sup> | 222.435 |
| **Ti_sv** | **12** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>3</sup> 4*s*<sup>1</sup>** | **274.719** |
| V | 5 | 3*d*<sup>4</sup> 4*s*<sup>1</sup> | 192.706 |
| V_pv | 11 | 3*p*<sup>6</sup> 3*d*<sup>4</sup> 4*s*<sup>1</sup> | 263.722 |
| **V_sv** | **13** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>4</sup> 4*s*<sup>1</sup>** | **263.722** |
| Cr | 6 | 3*d*<sup>5</sup> 4*s*<sup>1</sup> | 227.202 |
| **Cr_pv** | **12** | **3*p*<sup>6</sup> 3*d*<sup>5</sup> 4*s*<sup>1</sup>** | **265.753** |
| Cr_sv | 14 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>5</sup> 4*s*<sup>1</sup> | 395.443 |
| Mn | 7 | 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 269.944 |
| **Mn_pv** | **13** | **3*p*<sup>6</sup> 3*d*<sup>6</sup> 4*s*<sup>1</sup>** | **269.944** |
| Mn_sv | 15 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 387.112 |
| **Fe** | **8** | **3*d*<sup>7</sup> 4*s*<sup>1</sup>** | **267.969** |
| Fe_pv | 14 | 3*p*<sup>6</sup> 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 293.303 |
| Fe_sv | 16 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 390.513 |
| **Co** | **9** | **3*d*<sup>8</sup> 4*s*<sup>1</sup>** | **268.056** |
| Co_pv | 15 | 3*p*<sup>6</sup> 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 270.871 |
| Co_sv | 17 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 390.343 |
| **Ni** | **10** | **3*d*<sup>9</sup> 4*s*<sup>1</sup>** | **269.618** |
| Ni_pv | 16 | 3*p*<sup>6</sup> 3*d*<sup>9</sup> 4*s*<sup>1</sup> | 367.726 |
| **Cu** | **11** | **3*d*<sup>10</sup> 4*s*<sup>1</sup>** | **295.521** |
| Cu_pv | 17 | 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>1</sup> | 368.406 |
| **Zn** | **12** | **3*d*<sup>10</sup> 4*s*<sup>2</sup>** | **276.847** |
| Ga | 3 | 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 134.8 |
| **Ga_d** | **13** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup>** | **282.829** |
| Ga_h | 13 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 404.723 |
| Ge | 4 | 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 173.969 |
| **Ge_d** | **14** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup>** | **310.448** |
| Ge_h | 14 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 410.604 |
| **As** | **5** | **4*s*<sup>2</sup> 4*p*<sup>3</sup>** | **208.87** |
| As_d | 15 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>3</sup> | 288.762 |
| **Se** | **6** | **4*s*<sup>2</sup> 4*p*<sup>4</sup>** | **211.602** |
| **Br** | **7** | **4*s*<sup>2</sup> 4*p*<sup>5</sup>** | **216.224** |
| **Kr** | **8** | **4*s*<sup>2</sup> 4*p*<sup>6</sup>** | **185.392** |
| Rb_pv | 7 | 4*p*<sup>6</sup> 4*d*<sup>0.001</sup> 5*s*<sup>0.999</sup> | 122.21 |
| **Rb_sv** | **9** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>0.001</sup> 5*s*<sup>0.999</sup>** | **220.215** |
| **Sr_sv** | **10** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>0.001</sup> 5*s*<sup>1.999</sup>** | **226.327** |
| **Y_sv** | **11** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>2</sup> 5*s*<sup>1</sup>** | **202.554** |
| **Zr_sv** | **12** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>3</sup> 5*s*<sup>1</sup>** | **230.037** |
| Nb_pv | 11 | 4*p*<sup>6</sup> 4*d*<sup>4</sup> 5*s*<sup>1</sup> | 207.263 |
| **Nb_sv** | **13** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>4</sup> 5*s*<sup>1</sup>** | **293.304** |
| Mo | 6 | 4*d*<sup>5</sup> 5*s*<sup>1</sup> | 224.535 |
| Mo_pv | 12 | 4*p*<sup>6</sup> 4*d*<sup>5</sup> 5*s*<sup>1</sup> | 224.535 |
| **Mo_sv** | **14** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>5</sup> 5*s*<sup>1</sup>** | **236.514** |
| Tc | 7 | 4*d*<sup>6</sup> 5*s*<sup>1</sup> | 228.636 |
| **Tc_pv** | **13** | **4*p*<sup>6</sup> 4*d*<sup>6</sup> 5*s*<sup>1</sup>** | **263.345** |
| Tc_sv | 15 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>6</sup> 5*s*<sup>1</sup> | 318.479 |
| Ru | 8 | 4*d*<sup>7</sup> 5*s*<sup>1</sup> | 213.221 |
| **Ru_pv** | **14** | **4*p*<sup>6</sup> 4*d*<sup>7</sup> 5*s*<sup>1</sup>** | **239.907** |
| Ru_sv | 16 | 4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>7</sup> 5*s*<sup>1</sup> | 318.687 |
| Rh | 9 | 4*d*<sup>8</sup> 5*s*<sup>1</sup> | 228.926 |
| **Rh_pv** | **15** | **4*p*<sup>6</sup> 4*d*<sup>8</sup> 5*s*<sup>1</sup>** | **247.321** |
| **Pd** | **10** | **4*d*<sup>9</sup> 5*s*<sup>1</sup>** | **250.832** |
| Pd_pv | 16 | 4*p*<sup>6</sup> 4*d*<sup>9</sup> 5*s*<sup>1</sup> | 250.832 |
| **Ag** | **11** | **4*d*<sup>10</sup> 5*s*<sup>1</sup>** | **249.752** |
| Ag_pv | 17 | 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>1</sup> | 297.68 |
| **Cd** | **12** | **4*d*<sup>10</sup> 5*s*<sup>2</sup>** | **274.265** |
| In | 3 | 5*s*<sup>2</sup> 5*p*<sup>1</sup> | 96.062 |
| **In_d** | **13** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup>** | **239.196** |
| Sn | 4 | 5*s*<sup>2</sup> 5*p*<sup>2</sup> | 103.318 |
| **Sn_d** | **14** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup>** | **241.107** |
| **Sb** | **5** | **5*s*<sup>2</sup> 5*p*<sup>3</sup>** | **172.301** |
| **Te** | **6** | **5*s*<sup>2</sup> 5*p*<sup>4</sup>** | **175.144** |
| **I** | **7** | **5*s*<sup>2</sup> 5*p*<sup>5</sup>** | **175.712** |
| **Xe** | **8** | **5*s*<sup>2</sup> 5*p*<sup>6</sup>** | **153.021** |
| **Cs_sv** | **9** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 6*s*<sup>1</sup>** | **220.727** |
| **Ba_sv** | **10** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.001</sup> 6*s*<sup>1.999</sup>** | **186.981** |
| **La** | **11** | **4*f*<sup>0.0001</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>0.9999</sup> 6*s*<sup>2</sup>** | **219.044** |
| La_s | 9 | 4*f*<sup>0.0001</sup> 5*p*<sup>6</sup> 5*d*<sup>0.9999</sup> 6*s*<sup>2</sup> | 136.594 |
| **Ce** | **12** | **4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **273.088** |
| Ce_h | 12 | 4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 299.927 |
| Hf | 4 | 5*d*<sup>3</sup> 6*s*<sup>1</sup> | 220.431 |
| **Hf_pv** | **10** | **5*p*<sup>6</sup> 5*d*<sup>3</sup> 6*s*<sup>1</sup>** | **220.431** |
| Hf_sv | 12 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>4</sup> | 237.414 |
| Ta | 5 | 5*d*<sup>4</sup> 6*s*<sup>1</sup> | 223.759 |
| **Ta_pv** | **11** | **5*p*<sup>6</sup> 5*d*<sup>4</sup> 6*s*<sup>1</sup>** | **223.759** |
| W | 6 | 5*d*<sup>5</sup> 6*s*<sup>1</sup> | 223.126 |
| W_pv | 12 | 5*p*<sup>6</sup> 5*d*<sup>5</sup> 6*s*<sup>1</sup> | 223.126 |
| **Re** | **7** | **5*d*<sup>6</sup> 6*s*<sup>1</sup>** | **226.25** |
| Re_pv | 13 | 5*p*<sup>6</sup> 5*d*<sup>6</sup> 6*s*<sup>1</sup> | 226.25 |
| **Os** | **8** | **5*d*<sup>7</sup> 6*s*<sup>1</sup>** | **228.023** |
| Os_pv | 14 | 5*p*<sup>6</sup> 5*d*<sup>7</sup> 6*s*<sup>1</sup> | 228.023 |
| **Ir** | **9** | **5*d*<sup>8</sup> 6*s*<sup>1</sup>** | **210.837** |
| **Pt** | **10** | **5*d*<sup>9</sup> 6*s*<sup>1</sup>** | **230.228** |
| Pt_pv | 16 | 5*p*<sup>6</sup> 5*d*<sup>9</sup> 6*s*<sup>1</sup> | 294.53 |
| **Au** | **11** | **5*d*<sup>10</sup> 6*s*<sup>1</sup>** | **229.869** |
| **Hg** | **12** | **5*d*<sup>10</sup> 6*s*<sup>2</sup>** | **233.142** |
| Tl | 3 | 6*s*<sup>2</sup> 6*p*<sup>1</sup> | 90.239 |
| **Tl_d** | **13** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>1</sup>** | **237.001** |
| Pb | 4 | 6*s*<sup>2</sup> 6*p*<sup>2</sup> | 98.039 |
| **Pb_d** | **14** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup>** | **237.817** |
| Bi | 5 | 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 105.071 |
| **Bi_d** | **15** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup>** | **242.856** |
| Po | 6 | 6*s*<sup>2</sup> 6*p*<sup>4</sup> | 159.801 |
| **Po_d** | **16** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>4</sup>** | **264.606** |
| **At** | **7** | **6*s*<sup>2</sup> 6*p*<sup>5</sup>** | **161.481** |
| At_d | 17 | 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>5</sup> | 266.303 |
| **Rn** | **8** | **6*s*<sup>2</sup> 6*p*<sup>6</sup>** | **152.086** |
| **Fr_sv** | **9** | **6*s*<sup>2</sup> 6*p*<sup>6</sup> 7*s*<sup>1</sup>** | **214.489** |
| **Ra_sv** | **10** | **6*s*<sup>2</sup> 6*p*<sup>6</sup> 7*s*<sup>2</sup>** | **237.216** |
| **Ac** | **11** | **5*f*<sup>0.0001</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>0.9999</sup> 7*s*<sup>2</sup>** | **170.048** |
| **Th** | **12** | **5*f*<sup>1</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>1</sup> 7*s*<sup>2</sup>** | **247.389** |
| Th_s | 10 | 5*f*<sup>1</sup> 6*p*<sup>6</sup> 6*d*<sup>1</sup> 7*s*<sup>2</sup> | 169.575 |
| **Pa** | **13** | **5*f*<sup>1</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **252.31** |
| Pa_s | 11 | 5*f*<sup>1</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 193.642 |
| **U** | **14** | **5*f*<sup>2</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **252.603** |
| U_s | 14 | 5*f*<sup>2</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 209.218 |
| **Np** | **15** | **5*f*<sup>3</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **254.349** |
| Np_s | 15 | 5*f*<sup>3</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 213.932 |
| **Pu** | **16** | **5*f*<sup>4</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **254.436** |
| Pu_s | 16 | 5*f*<sup>4</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup> | 211.493 |
| **Am** | **17** | **5*f*<sup>5</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **255.953** |
| **Cm** | **18** | **5*f*<sup>6</sup> 6*s*<sup>2</sup> 6*p*<sup>6</sup> 6*d*<sup>2</sup> 7*s*<sup>2</sup>** | **258.027** |

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| List of PBE potentials |  |  |  |
| Potential name | Number of valence electrons | Valence electron configuration | ENAMX \[eV\] |
| **H** | **1** | **1*s*<sup>1</sup>** | **250.0** |
| H.25 | 0.25 | 1*s*<sup>0.25</sup> | 250.0 |
| H.33 | 0.33 | 1*s*<sup>0.33</sup> | 250.0 |
| H.42 | 0.42 | 1*s*<sup>0.42</sup> | 250.0 |
| H.5 | 0.5 | 1*s*<sup>0.5</sup> | 250.0 |
| H.58 | 0.58 | 1*s*<sup>0.58</sup> | 250.0 |
| H.66 | 0.66 | 1*s*<sup>0.66</sup> | 250.0 |
| H.75 | 0.75 | 1*s*<sup>0.75</sup> | 250.0 |
| H1.25 | 1.25 | 1*s*<sup>1.25</sup> | 457.521 |
| H1.33 | 1.33 | 1*s*<sup>1.33</sup> | 250.0 |
| H1.5 | 1.5 | 1*s*<sup>1.5</sup> | 250.0 |
| H1.66 | 1.66 | 1*s*<sup>1.66</sup> | 250.0 |
| H1.75 | 1.75 | 1*s*<sup>1.75</sup> | 250.0 |
| H_AE | 1 |  | 1000.0 |
| H_h | 1 | 1*s*<sup>1</sup> | 700.0 |
| H_s | 1 | 1*s*<sup>1</sup> | 200.0 |
| **He** | **2** | **1*s*<sup>2</sup>** | **478.896** |
| Li | 1 | 2*s*<sup>1</sup> | 140.0 |
| **Li_sv** | **3** | **1*s*<sup>2</sup> 2*s*<sup>1</sup>** | **499.034** |
| **Be** | **2** | **2*s*<sup>1.99</sup> 2*p*<sup>0.01</sup>** | **247.543** |
| Be_sv | 4 | 1*s*<sup>2</sup> 2*s*<sup>1.99</sup> 2*p*<sup>0.01</sup> | 308.768 |
| **B** | **3** | **2*s*<sup>2</sup> 2*p*<sup>1</sup>** | **318.614** |
| B_h | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 700.0 |
| B_s | 3 | 2*s*<sup>2</sup> 2*p*<sup>1</sup> | 269.245 |
| **C** | **4** | **2*s*<sup>2</sup> 2*p*<sup>2</sup>** | **400.0** |
| C_h | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 700.0 |
| C_s | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 273.911 |
| **N** | **5** | **2*s*<sup>2</sup> 2*p*<sup>3</sup>** | **400.0** |
| N_h | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 700.0 |
| N_s | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 279.692 |
| **O** | **6** | **2*s*<sup>2</sup> 2*p*<sup>4</sup>** | **400.0** |
| O_h | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 700.0 |
| O_s | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 282.853 |
| **F** | **7** | **2*s*<sup>2</sup> 2*p*<sup>5</sup>** | **400.0** |
| F_h | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 700.0 |
| F_s | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 289.837 |
| **Ne** | **8** | **2*s*<sup>2</sup> 2*p*<sup>6</sup>** | **343.606** |
| Na | 1 | 3*s*<sup>1</sup> | 101.968 |
| **Na_pv** | **7** | **2*p*<sup>6</sup> 3*s*<sup>1</sup>** | **259.561** |
| Na_sv | 9 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>1</sup> | 645.64 |
| **Mg** | **2** | **3*s*<sup>2</sup>** | **126.143** |
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
| Pr | 13 | 4*f*<sup>2</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 272.941 |
| **Pr_3** | **11** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **181.719** |
| Nd | 14 | 4*f*<sup>3</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 253.189 |
| **Nd_3** | **11** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **182.619** |
| Pm | 15 | 4*f*<sup>4</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 258.627 |
| **Pm_3** | **11** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **176.959** |
| Sm | 16 | 4*f*<sup>5</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 257.515 |
| **Sm_3** | **11** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **177.087** |
| Eu | 17 | 4*f*<sup>7</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 6*s*<sup>2</sup> | 249.668 |
| **Eu_2** | **8** | **5*p*<sup>6</sup> 6*s*<sup>2</sup>** | **99.328** |
| Eu_3 | 9 | 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 129.057 |
| Gd | 18 | 4*f*<sup>7</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 256.472 |
| **Gd_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **154.332** |
| Tb | 19 | 4*f*<sup>8</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 264.824 |
| **Tb_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **155.613** |
| Dy | 20 | 4*f*<sup>9</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 255.467 |
| **Dy_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **155.713** |
| Ho | 21 | 4*f*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 257.168 |
| **Ho_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **154.137** |
| Er | 22 | 4*f*<sup>11</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 298.116 |
| Er_2 | 8 | 5*p*<sup>6</sup> 6*s*<sup>2</sup> | 119.75 |
| **Er_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **155.037** |
| Tm | 23 | 4*f*<sup>12</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 257.42 |
| **Tm_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **149.221** |
| Yb | 24 | 4*f*<sup>14</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 6*s*<sup>2</sup> | 253.028 |
| **Yb_2** | **8** | **5*p*<sup>6</sup> 6*s*<sup>2</sup>** | **112.578** |
| Lu | 25 | 4*f*<sup>14</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup> | 255.695 |
| **Lu_3** | **9** | **5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **154.992** |
| Hf | 4 | 5*d*<sup>3</sup> 6*s*<sup>1</sup> | 220.334 |
| **Hf_pv** | **10** | **5*p*<sup>6</sup> 5*d*<sup>3</sup> 6*s*<sup>1</sup>** | **220.334** |
| Hf_sv | 12 | 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>4</sup> | 237.444 |
| Ta | 5 | 5*d*<sup>4</sup> 6*s*<sup>1</sup> | 223.667 |
| **Ta_pv** | **11** | **5*p*<sup>6</sup> 5*d*<sup>4</sup> 6*s*<sup>1</sup>** | **223.667** |
| W | 6 | 5*d*<sup>5</sup> 6*s*<sup>1</sup> | 223.057 |
| W_pv | 12 | 5*p*<sup>6</sup> 5*d*<sup>5</sup> 6*s*<sup>1</sup> | 223.057 |
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
| At_d | 17 | 5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>5</sup> | 266.251 |
| **Rn** | **8** | **6*s*<sup>2</sup> 6*p*<sup>6</sup>** | **152.121** |
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

#### GW potentials\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: GW potentials">edit</a> \| (./index.php.md)\]

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| List of LDA potentials |  |  |  |
| Potential name | Number of valence electrons | Valence electron configuration | ENAMX \[eV\] |
| **H_GW** | **1** | **1*s*<sup>1</sup>** | **300.0** |
| H_h_GW | 1 | 1*s*<sup>1</sup> | 700.0 |
| **He_GW** | **2** | **1*s*<sup>2</sup>** | **404.806** |
| Li_AE_GW | 3 | 1*s*<sup>2</sup> 2*p*<sup>1</sup> | 433.253 |
| Li_GW | 1 | 2*s*<sup>1</sup> | 112.417 |
| **Li_sv_GW** | **3** | **1*s*<sup>2</sup> 2*p*<sup>1</sup>** | **433.253** |
| Be_GW | 2 | 2*s*<sup>1.9999</sup> 2*p*<sup>0.001</sup> | 247.951 |
| **Be_sv_GW** | **4** | **1*s*<sup>2</sup> 2*p*<sup>2</sup>** | **536.216** |
| **B_GW** | **3** | **2*s*<sup>2</sup> 2*p*<sup>1</sup>** | **318.762** |
| **C_GW** | **4** | **2*s*<sup>2</sup> 2*p*<sup>2</sup>** | **413.992** |
| C_GW_new | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 413.992 |
| **N_GW** | **5** | **2*s*<sup>2</sup> 2*p*<sup>3</sup>** | **420.681** |
| N_GW_new | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 420.681 |
| N_s_GW | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 296.222 |
| **O_GW** | **6** | **2*s*<sup>2</sup> 2*p*<sup>4</sup>** | **414.315** |
| O_GW_new | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 433.745 |
| O_s_GW | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 334.366 |
| **F_GW** | **7** | **2*s*<sup>2</sup> 2*p*<sup>5</sup>** | **487.335** |
| F_GW_new | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 487.335 |
| **Ne_GW** | **8** | **2*s*<sup>2</sup> 2*p*<sup>6</sup>** | **317.594** |
| Ne_GW_soft | 8 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> | 317.594 |
| **Na_sv_GW** | **9** | **2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*d*<sup>1</sup>** | **260.372** |
| Mg_GW | 2 | 3*s*<sup>2</sup> | 126.671 |
| Mg_pv_GW | 8 | 2*p*<sup>6</sup> 3*s*<sup>2</sup> | 403.538 |
| **Mg_sv_GW** | **10** | **2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*d*<sup>2</sup>** | **430.099** |
| **Al_GW** | **3** | **3*s*<sup>2</sup> 3*p*<sup>1</sup>** | **240.957** |
| Al_sv_GW | 11 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>2</sup> 3*p*<sup>1</sup> | 411.007 |
| **Si_GW** | **4** | **3*s*<sup>2</sup> 3*p*<sup>2</sup>** | **245.704** |
| Si_sv_GW | 12 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*s*<sup>2</sup> 3*p*<sup>2</sup> | 546.548 |
| **P_GW** | **5** | **3*s*<sup>2</sup> 3*p*<sup>3</sup>** | **255.155** |
| **S_GW** | **6** | **3*s*<sup>2</sup> 3*p*<sup>4</sup>** | **258.602** |
| **Cl_GW** | **7** | **3*s*<sup>2</sup> 3*p*<sup>5</sup>** | **262.25** |
| **Ar_GW** | **8** | **3*s*<sup>2</sup> 3*p*<sup>6</sup>** | **266.101** |
| **K_sv_GW** | **9** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>1</sup>** | **248.606** |
| **Ca_sv_GW** | **10** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>2</sup>** | **281.209** |
| **Sc_sv_GW** | **11** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>3</sup>** | **284.878** |
| **Ti_sv_GW** | **12** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>4</sup>** | **285.665** |
| **V_sv_GW** | **13** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>5</sup>** | **322.537** |
| **Cr_sv_GW** | **14** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>6</sup>** | **327.752** |
| Mn_GW | 7 | 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 278.537 |
| **Mn_sv_GW** | **15** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>7</sup>** | **357.618** |
| Fe_GW | 8 | 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 321.044 |
| **Fe_sv_GW** | **16** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>8</sup>** | **364.41** |
| Co_GW | 9 | 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 323.447 |
| **Co_sv_GW** | **17** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>9</sup>** | **363.483** |
| Ni_GW | 10 | 3*d*<sup>9</sup> 4*s*<sup>1</sup> | 357.352 |
| **Ni_sv_GW** | **18** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup>** | **413.158** |
| Cu_GW | 11 | 3*d*<sup>10</sup> 4*s*<sup>1</sup> | 417.032 |
| Cu_pv_GW | 17 | 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>1</sup> | 466.991 |
| Zn_GW | 12 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> | 328.312 |
| Zn_pv_GW | 18 | 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> | 360.353 |
| **Zn_sv_GW** | **20** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>12</sup>** | **496.249** |
| Ga_GW | 3 | 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 134.8 |
| **Ga_d_GW** | **13** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup>** | **404.723** |
| Ga_pv_GW | 19 | 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 422.753 |
| Ga_sv_GW | 21 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 503.451 |
| Ge_GW | 4 | 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 173.969 |
| **Ge_d_GW** | **14** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup>** | **310.448** |
| Ge_sv_GW | 22 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 454.654 |
| **As_GW** | **5** | **4*s*<sup>2</sup> 4*p*<sup>3</sup>** | **208.87** |
| **Se_GW** | **6** | **4*s*<sup>2</sup> 4*p*<sup>4</sup>** | **211.602** |
| **Br_GW** | **7** | **4*s*<sup>2</sup> 4*p*<sup>5</sup>** | **216.224** |
| **Kr_GW** | **8** | **4*s*<sup>2</sup> 4*p*<sup>6</sup>** | **185.392** |
| **Rb_sv_GW** | **9** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>1</sup>** | **220.92** |
| **Sr_sv_GW** | **10** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>2</sup>** | **224.532** |
| **Y_sv_GW** | **11** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>3</sup>** | **229.027** |
| **Zr_sv_GW** | **12** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>4</sup>** | **282.169** |
| **Nb_sv_GW** | **13** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>5</sup>** | **285.574** |
| **Mo_sv_GW** | **14** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>6</sup>** | **311.692** |
| **Tc_sv_GW** | **15** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>7</sup>** | **317.903** |
| Ru_pv_GW | 14 | 4*p*<sup>6</sup> 4*d*<sup>7</sup> 5*s*<sup>1</sup> | 239.907 |
| **Ru_sv_GW** | **16** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>8</sup>** | **320.997** |
| Rh_GW | 9 | 4*d*<sup>8</sup> 5*s*<sup>1</sup> | 247.321 |
| Rh_pv_GW | 15 | 4*p*<sup>6</sup> 4*d*<sup>8</sup> 5*s*<sup>1</sup> | 247.321 |
| **Rh_sv_GW** | **17** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>9</sup>** | **319.891** |
| Pd_GW | 10 | 4*d*<sup>9</sup> 5*s*<sup>1</sup> | 250.832 |
| Ag_GW | 11 | 4*d*<sup>10</sup> 5*s*<sup>1</sup> | 249.752 |
| Cd_GW | 12 | 4*d*<sup>10</sup> 5*s*<sup>2</sup> | 253.99 |
| Cd_pv_GW | 18 | 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> | 396.576 |
| **Cd_sv_GW** | **20** | **4*s*<sup>4</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup>** | **650.91** |
| **In_d_GW** | **13** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup>** | **278.582** |
| **Sn_d_GW** | **14** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup>** | **260.086** |
| Sb_GW | 5 | 5*s*<sup>2</sup> 5*p*<sup>3</sup> | 172.301 |
| **Sb_d_GW** | **15** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>3</sup>** | **263.147** |
| **Te_GW** | **6** | **5*s*<sup>2</sup> 5*p*<sup>4</sup>** | **175.144** |
| **I_GW** | **7** | **5*s*<sup>2</sup> 5*p*<sup>5</sup>** | **175.712** |
| **Xe_GW** | **8** | **5*s*<sup>2</sup> 5*p*<sup>6</sup>** | **179.528** |
| **Cs_sv_GW** | **9** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup>** | **198.012** |
| **Ba_sv_GW** | **10** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>2</sup>** | **237.484** |
| **Ce_GW** | **12** | **4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **304.649** |
| **Hf_sv_GW** | **12** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>4</sup>** | **282.716** |
| **Ta_sv_GW** | **13** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>5</sup>** | **285.798** |
| **W_sv_GW** | **14** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>6</sup>** | **316.943** |
| **Re_sv_GW** | **15** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>7</sup>** | **316.85** |
| **Os_sv_GW** | **16** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>8</sup>** | **319.628** |
| **Ir_sv_GW** | **17** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>9</sup>** | **319.708** |
| Pt_GW | 10 | 5*d*<sup>9</sup> 6*s*<sup>1</sup> | 248.657 |
| Pt_pv_GW | 16 | 5*p*<sup>6</sup> 5*d*<sup>9</sup> 6*s*<sup>1</sup> | 248.657 |
| **Pt_sv_GW** | **18** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup>** | **323.536** |
| Au_GW | 11 | 5*d*<sup>10</sup> 6*s*<sup>1</sup> | 248.263 |
| Au_pv_GW | 17 | 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>1</sup> | 248.263 |
| **Pb_d_GW** | **14** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup>** | **237.793** |
| Bi_GW | 5 | 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 146.628 |
| **Bi_d_GW** | **15** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup>** | **242.856** |

|  |  |  |  |
|:--:|:--:|:--:|:--:|
| List of PBE potentials |  |  |  |
| Potential name | Number of valence electrons | Valence electron configuration | ENAMX \[eV\] |
| **H_GW** | **1** | **1*s*<sup>1</sup>** | **300.0** |
| H_h_GW | 1 | 1*s*<sup>1</sup> | 700.0 |
| **He_GW** | **2** | **1*s*<sup>2</sup>** | **405.78** |
| Li_AE_GW | 3 | 1*s*<sup>2</sup> 2*p*<sup>1</sup> | 433.699 |
| Li_GW | 1 | 2*s*<sup>1</sup> | 112.104 |
| **Li_sv_GW** | **3** | **1*s*<sup>2</sup> 2*p*<sup>1</sup>** | **433.699** |
| Be_GW | 2 | 2*s*<sup>1.9999</sup> 2*p*<sup>0.001</sup> | 247.543 |
| **Be_sv_GW** | **4** | **1*s*<sup>2</sup> 2*p*<sup>2</sup>** | **537.454** |
| **B_GW** | **3** | **2*s*<sup>2</sup> 2*p*<sup>1</sup>** | **318.614** |
| **C_GW** | **4** | **2*s*<sup>2</sup> 2*p*<sup>2</sup>** | **413.992** |
| C_GW_new | 4 | 2*s*<sup>2</sup> 2*p*<sup>2</sup> | 413.992 |
| **N_GW** | **5** | **2*s*<sup>2</sup> 2*p*<sup>3</sup>** | **420.902** |
| N_GW_new | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 420.902 |
| N_s_GW | 5 | 2*s*<sup>2</sup> 2*p*<sup>3</sup> | 296.495 |
| **O_GW** | **6** | **2*s*<sup>2</sup> 2*p*<sup>4</sup>** | **414.635** |
| O_GW_new | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 434.431 |
| O_s_GW | 6 | 2*s*<sup>2</sup> 2*p*<sup>4</sup> | 334.664 |
| **F_GW** | **7** | **2*s*<sup>2</sup> 2*p*<sup>5</sup>** | **487.698** |
| F_GW_new | 7 | 2*s*<sup>2</sup> 2*p*<sup>5</sup> | 487.698 |
| **Ne_GW** | **8** | **2*s*<sup>2</sup> 2*p*<sup>6</sup>** | **318.26** |
| Ne_GW_soft | 8 | 2*s*<sup>2</sup> 2*p*<sup>6</sup> | 318.26 |
| **Na_sv_GW** | **9** | **2*s*<sup>2</sup> 2*p*<sup>6</sup> 3*d*<sup>1</sup>** | **260.065** |
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
| **Ar_GW** | **8** | **3*s*<sup>2</sup> 3*p*<sup>6</sup>** | **266.408** |
| **K_sv_GW** | **9** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>1</sup>** | **248.998** |
| **Ca_sv_GW** | **10** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>2</sup>** | **281.43** |
| **Sc_sv_GW** | **11** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>3</sup>** | **285.066** |
| **Ti_sv_GW** | **12** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>4</sup>** | **285.998** |
| **V_sv_GW** | **13** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>5</sup>** | **323.07** |
| **Cr_sv_GW** | **14** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>6</sup>** | **328.282** |
| Mn_GW | 7 | 3*d*<sup>6</sup> 4*s*<sup>1</sup> | 278.466 |
| **Mn_sv_GW** | **15** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>7</sup>** | **357.944** |
| Fe_GW | 8 | 3*d*<sup>7</sup> 4*s*<sup>1</sup> | 321.007 |
| **Fe_sv_GW** | **16** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>8</sup>** | **364.719** |
| Co_GW | 9 | 3*d*<sup>8</sup> 4*s*<sup>1</sup> | 323.4 |
| **Co_sv_GW** | **17** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>9</sup>** | **363.77** |
| Ni_GW | 10 | 3*d*<sup>9</sup> 4*s*<sup>1</sup> | 357.323 |
| **Ni_sv_GW** | **18** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup>** | **413.475** |
| Cu_GW | 11 | 3*d*<sup>10</sup> 4*s*<sup>1</sup> | 417.039 |
| Cu_pv_GW | 17 | 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>1</sup> | 467.331 |
| Zn_GW | 12 | 3*d*<sup>10</sup> 4*s*<sup>2</sup> | 328.191 |
| Zn_pv_GW | 18 | 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> | 360.246 |
| **Zn_sv_GW** | **20** | **3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>12</sup>** | **496.604** |
| Ga_GW | 3 | 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 134.678 |
| **Ga_d_GW** | **13** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup>** | **404.602** |
| Ga_pv_GW | 19 | 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 423.002 |
| Ga_sv_GW | 21 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>1</sup> | 503.418 |
| Ge_GW | 4 | 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 173.807 |
| **Ge_d_GW** | **14** | **3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup>** | **310.294** |
| Ge_sv_GW | 22 | 3*s*<sup>2</sup> 3*p*<sup>6</sup> 3*d*<sup>10</sup> 4*s*<sup>2</sup> 4*p*<sup>2</sup> | 454.489 |
| **As_GW** | **5** | **4*s*<sup>2</sup> 4*p*<sup>3</sup>** | **208.702** |
| **Se_GW** | **6** | **4*s*<sup>2</sup> 4*p*<sup>4</sup>** | **211.555** |
| **Br_GW** | **7** | **4*s*<sup>2</sup> 4*p*<sup>5</sup>** | **216.285** |
| **Kr_GW** | **8** | **4*s*<sup>2</sup> 4*p*<sup>6</sup>** | **185.331** |
| **Rb_sv_GW** | **9** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>1</sup>** | **221.197** |
| **Sr_sv_GW** | **10** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>2</sup>** | **224.817** |
| **Y_sv_GW** | **11** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>3</sup>** | **229.276** |
| **Zr_sv_GW** | **12** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>4</sup>** | **282.431** |
| **Nb_sv_GW** | **13** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>5</sup>** | **285.792** |
| **Mo_sv_GW** | **14** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>6</sup>** | **311.905** |
| **Tc_sv_GW** | **15** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>7</sup>** | **318.11** |
| Ru_pv_GW | 14 | 4*p*<sup>6</sup> 4*d*<sup>7</sup> 5*s*<sup>1</sup> | 240.049 |
| **Ru_sv_GW** | **16** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>8</sup>** | **321.2** |
| Rh_GW | 9 | 4*d*<sup>8</sup> 5*s*<sup>1</sup> | 247.408 |
| Rh_pv_GW | 15 | 4*p*<sup>6</sup> 4*d*<sup>8</sup> 5*s*<sup>1</sup> | 247.408 |
| **Rh_sv_GW** | **17** | **4*s*<sup>2</sup> 4*p*<sup>6</sup> 4*d*<sup>9</sup>** | **320.091** |
| Pd_GW | 10 | 4*d*<sup>9</sup> 5*s*<sup>1</sup> | 250.925 |
| Ag_GW | 11 | 4*d*<sup>10</sup> 5*s*<sup>1</sup> | 249.844 |
| Cd_GW | 12 | 4*d*<sup>10</sup> 5*s*<sup>2</sup> | 254.045 |
| Cd_pv_GW | 18 | 4*p*<sup>6</sup> 4*d*<sup>10</sup> 5*s*<sup>2</sup> | 396.766 |
| **Cd_sv_GW** | **20** | **4*s*<sup>4</sup> 4*p*<sup>6</sup> 4*d*<sup>10</sup>** | **651.254** |
| **In_d_GW** | **13** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>1</sup>** | **278.624** |
| **Sn_d_GW** | **14** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>2</sup>** | **260.066** |
| Sb_GW | 5 | 5*s*<sup>2</sup> 5*p*<sup>3</sup> | 172.069 |
| **Sb_d_GW** | **15** | **4*d*<sup>10</sup> 5*s*<sup>2</sup> 5*p*<sup>3</sup>** | **263.1** |
| **Te_GW** | **6** | **5*s*<sup>2</sup> 5*p*<sup>4</sup>** | **174.982** |
| **I_GW** | **7** | **5*s*<sup>2</sup> 5*p*<sup>5</sup>** | **175.647** |
| **Xe_GW** | **8** | **5*s*<sup>2</sup> 5*p*<sup>6</sup>** | **179.547** |
| **Cs_sv_GW** | **9** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup>** | **198.101** |
| **Ba_sv_GW** | **10** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>2</sup>** | **237.515** |
| **Ce_GW** | **12** | **4*f*<sup>1</sup> 5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>1</sup> 6*s*<sup>2</sup>** | **304.625** |
| **Hf_sv_GW** | **12** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>4</sup>** | **282.964** |
| **Ta_sv_GW** | **13** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>5</sup>** | **286.008** |
| **W_sv_GW** | **14** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>6</sup>** | **317.132** |
| **Re_sv_GW** | **15** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>7</sup>** | **317.012** |
| **Os_sv_GW** | **16** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>8</sup>** | **319.773** |
| **Ir_sv_GW** | **17** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>9</sup>** | **319.843** |
| Pt_GW | 10 | 5*d*<sup>9</sup> 6*s*<sup>1</sup> | 248.716 |
| Pt_pv_GW | 16 | 5*p*<sup>6</sup> 5*d*<sup>9</sup> 6*s*<sup>1</sup> | 248.716 |
| **Pt_sv_GW** | **18** | **5*s*<sup>2</sup> 5*p*<sup>6</sup> 5*d*<sup>10</sup>** | **323.669** |
| Au_GW | 11 | 5*d*<sup>10</sup> 6*s*<sup>1</sup> | 248.344 |
| Au_pv_GW | 17 | 5*p*<sup>6</sup> 5*d*<sup>10</sup> 6*s*<sup>1</sup> | 248.344 |
| **Pb_d_GW** | **14** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>2</sup>** | **237.809** |
| Bi_GW | 5 | 6*s*<sup>2</sup> 6*p*<sup>3</sup> | 146.53 |
| **Bi_d_GW** | **15** | **5*d*<sup>10</sup> 6*s*<sup>2</sup> 6*p*<sup>3</sup>** | **242.839** |

### LDA (2010), PW91 (2006) and PBE (2010) PAW potentials\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: LDA (2010), PW91 (2006) and PBE (2010) PAW potentials">edit</a> \| (./index.php.md), PW91 (2006) and PBE (2010) PAW potentials")\]

The LDA, PW91 and PBE PAW datasets (snapshot: 05-05-2010, 19-09-2006 and
06-05-2010, respectively). These files are outdated, not supported and
only distributed as is. Some VASP feature might yield undesired results
with these files (e.g. [METAGGA](../incar-tags/METAGGA.md)).

#### Standard potentials\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Standard potentials">edit</a> \| (./index.php.md)\]

|                        |                             |              |
|:----------------------:|:---------------------------:|:------------:|
| List of LDA potentials |                             |              |
|     Potential name     | Number of valence electrons | ENAMX \[eV\] |
|          Free          |              0              |    250.0     |
|         **H**          |            **1**            |  **250.0**   |
|          H.25          |            0.25             |   419.126    |
|          H.33          |            0.33             |    250.0     |
|          H.5           |             0.5             |    250.0     |
|          H.66          |            0.66             |   250.477    |
|          H.75          |            0.75             |    250.0     |
|         H1.25          |            1.25             |    250.0     |
|         H1.33          |            1.33             |   458.665    |
|          H1.5          |             1.5             |    250.0     |
|         H1.66          |            1.66             |   467.584    |
|         H1.75          |            1.75             |   469.843    |
|          H_AE          |              1              |    1000.0    |
|          H_h           |              1              |    700.0     |
|         **He**         |            **2**            | **477.779**  |
|           Li           |              1              |    140.0     |
|       **Li_sv**        |            **3**            | **498.387**  |
|       Li_sv_old        |              3              |    270.99    |
|         **Be**         |            **2**            | **247.951**  |
|         Be_sv          |              4              |    308.45    |
|         **B**          |            **3**            | **318.762**  |
|          B_h           |              3              |    700.0     |
|          B_s           |              3              |    250.0     |
|         **C**          |            **4**            |  **400.0**   |
|          C_d           |              4              |   413.992    |
|         C_f_AE         |              6              |   840.525    |
|          C_h           |              4              |    700.0     |
|        C_local         |              4              |   1047.306   |
|          C_s           |              4              |    250.0     |
|         **N**          |            **5**            |  **400.0**   |
|          N_h           |              5              |    700.0     |
|          N_s           |              5              |    250.0     |
|         **O**          |            **6**            |  **400.0**   |
|          O_h           |              6              |    700.0     |
|          O_s           |              6              |   282.604    |
|         **F**          |            **7**            |  **400.0**   |
|          F_h           |              7              |    700.0     |
|          F_s           |              7              |    250.0     |
|         **Ne**         |            **8**            | **343.403**  |
|         Ne_AE          |             10              |   2744.212   |
|           Na           |              1              |   101.956    |
|       **Na_pv**        |            **7**            | **259.494**  |
|         Na_sv          |              9              |    700.0     |
|         **Mg**         |            **2**            | **210.674**  |
|         Mg_pv          |              8              |   403.538    |
|       Mg_pv.old        |              8              |   265.566    |
|         Mg_sv          |             10              |    473.54    |
|         **Al**         |            **3**            | **240.957**  |
|         Al_pv          |              9              |   370.394    |
|          Al_s          |              3              |   135.119    |
|         **Si**         |            **4**            | **245.704**  |
|          Si_h          |              4              |   339.353    |
|        Si_nopc         |              4              |   245.704    |
|         **P**          |            **5**            |  **270.0**   |
|          P_h           |              5              |   390.903    |
|         **S**          |            **6**            |  **280.0**   |
|          S_h           |              6              |    402.84    |
|         **Cl**         |            **7**            |  **280.0**   |
|          Cl_h          |              7              |   409.272    |
|        Cl_h_new        |              7              |   409.272    |
|         **Ar**         |            **8**            | **266.101**  |
|           K            |              7              |   116.596    |
|          K_pv          |              7              |   116.596    |
|        **K_sv**        |            **9**            | **259.279**  |
|         Ca_pv          |              8              |    150.0     |
|       **Ca_sv**        |           **10**            | **266.727**  |
|           Sc           |              3              |   155.006    |
|       **Sc_sv**        |           **11**            |  **222.7**   |
|           Ti           |              4              |    178.52    |
|         Ti_pv          |             10              |   222.435    |
|          Ti_s          |              2              |   141.437    |
|       **Ti_sv**        |           **12**            | **274.719**  |
|       Ti_sv_new        |             12              |   274.719    |
|           V            |              5              |   192.706    |
|          V_pv          |             11              |   263.722    |
|        **V_sv**        |           **13**            | **263.722**  |
|           Cr           |              6              |   227.202    |
|       **Cr_pv**        |           **12**            | **265.753**  |
|           Mn           |              7              |   269.944    |
|       **Mn_pv**        |           **13**            | **269.944**  |
|         **Fe**         |            **8**            | **267.969**  |
|         Fe_pv          |             14              |   293.303    |
|         Fe_sv          |             16              |   390.513    |
|         **Co**         |            **9**            | **268.056**  |
|         Co_pv          |             15              |   415.593    |
|         **Ni**         |           **10**            | **269.618**  |
|          Ni_h          |             10              |   357.352    |
|         Ni_pv          |             16              |   367.726    |
|         **Cu**         |           **11**            | **273.298**  |
|         Cu_new         |             11              |   295.521    |
|         Cu_pv          |             17              |   368.406    |
|         **Zn**         |           **12**            | **276.847**  |
|         Zn_pv          |             18              |   376.385    |
|      Zn_sv_LDApU       |             20              |   725.781    |
|           Ga           |              3              |    134.8     |
|         Ga_NC2         |              3              |   513.106    |
|        **Ga_d**        |           **13**            | **282.829**  |
|          Ga_h          |             13              |   404.723    |
|          Ga_s          |              3              |    87.077    |
|           Ge           |              4              |   173.969    |
|        **Ge_d**        |           **14**            | **310.448**  |
|          Ge_h          |             14              |   410.604    |
|         **As**         |            **5**            |  **208.87**  |
|         As_NC2         |              5              |   342.549    |
|          As_d          |             15              |   288.762    |
|         **Se**         |            **6**            | **211.602**  |
|         **Br**         |            **7**            | **216.224**  |
|         **Kr**         |            **8**            | **185.392**  |
|         Rb_pv          |              7              |    122.21    |
|       **Rb_sv**        |            **9**            | **220.215**  |
|       **Sr_sv**        |           **10**            | **226.327**  |
|        **Y_sv**        |           **11**            | **211.836**  |
|           Zr           |              4              |    145.4     |
|       **Zr_sv**        |           **12**            | **230.037**  |
|       Zr_sv_new        |             12              |   230.037    |
|         Nb_pv          |             11              |   207.263    |
|       **Nb_sv**        |           **13**            | **293.304**  |
|           Mo           |              6              |   224.535    |
|         Mo_pv          |             12              |   224.535    |
|       Mo_pv_new        |             12              |   224.535    |
|       **Mo_sv**        |           **14**            | **236.514**  |
|           Tc           |              7              |   228.636    |
|         Tc_new         |              7              |   228.636    |
|       **Tc_pv**        |           **13**            | **228.636**  |
|       Tc_pv_new        |             13              |   263.345    |
|           Ru           |              8              |   213.221    |
|         Ru_new         |              8              |   213.221    |
|       **Ru_pv**        |           **14**            | **230.359**  |
|       Ru_pv_new        |             14              |   239.907    |
|           Rh           |              9              |   228.926    |
|         Rh_new         |              9              |   228.926    |
|       **Rh_pv**        |           **15**            | **271.355**  |
|       Rh_pv_new        |             15              |   247.321    |
|         **Pd**         |           **10**            | **250.832**  |
|         Pd_new         |             10              |   250.832    |
|         Pd_pv          |             16              |   270.984    |
|       Pd_pv_new        |             16              |   250.832    |
|         **Ag**         |           **11**            | **249.752**  |
|         Ag_new         |             11              |   249.752    |
|         **Cd**         |           **12**            | **274.265**  |
|           In           |              3              |    96.062    |
|        **In_d**        |           **13**            | **239.196**  |
|         In_pv          |             19              |   241.124    |
|           Sn           |              4              |   103.318    |
|        **Sn_d**        |           **14**            | **241.107**  |
|         **Sb**         |            **5**            | **172.301**  |
|          Sb\_          |              5              |   172.301    |
|         **Te**         |            **6**            | **175.144**  |
|         Te_rel         |              6              |   175.141    |
|         **I**          |            **7**            | **175.712**  |
|         **Xe**         |            **8**            | **153.021**  |
|       **Cs_sv**        |            **9**            | **220.727**  |
|       **Ba_sv**        |           **10**            | **186.981**  |
|         **La**         |           **11**            | **219.044**  |
|          La_s          |              9              |   136.594    |
|         **Ce**         |           **12**            | **299.927**  |
|          Ce_h          |             12              |   299.927    |
|          Ce_s          |             10              |   173.613    |
|           Hf           |              4              |   220.431    |
|       **Hf_pv**        |           **10**            | **220.431**  |
|         Hf_sv          |             12              |   237.414    |
|           Ta           |              5              |   223.759    |
|       **Ta_pv**        |           **11**            | **223.759**  |
|           W            |              6              |   223.126    |
|          W_pv          |             12              |   223.126    |
|         **Re**         |            **7**            |  **226.25**  |
|         Re_pv          |             13              |    226.25    |
|         **Os**         |            **8**            | **228.023**  |
|         Os_pv          |             14              |   228.023    |
|         **Ir**         |            **9**            | **210.837**  |
|         **Pt**         |           **10**            | **230.228**  |
|         Pt_new         |             10              |   230.228    |
|         **Au**         |           **11**            | **229.869**  |
|         Au_new         |             11              |   229.869    |
|         **Hg**         |           **12**            | **233.142**  |
|           Tl           |              3              |    90.239    |
|        **Tl_d**        |           **13**            | **237.001**  |
|           Pb           |              4              |    98.039    |
|        **Pb_d**        |           **14**            | **237.817**  |
|         Pb_dr          |              4              |    98.041    |
|           Bi           |              5              |   105.071    |
|        **Bi_d**        |           **15**            | **242.856**  |
|         Bi_pv          |             21              |   309.184    |
|           Po           |              6              |   159.801    |
|        **Po_d**        |           **16**            | **264.606**  |
|         **At**         |            **7**            | **161.481**  |
|          At_d          |             17              |   266.303    |
|         **Rn**         |            **8**            | **152.086**  |
|       **Fr_sv**        |            **9**            | **214.489**  |
|       **Ra_sv**        |           **10**            | **237.216**  |
|         **Ac**         |           **11**            | **170.048**  |
|          Ac_s          |              9              |   119.996    |
|         **Th**         |           **12**            | **247.389**  |
|          Th_s          |             10              |   169.575    |
|         **Pa**         |           **13**            |  **252.31**  |
|          Pa_s          |             11              |   193.642    |
|         **U**          |           **14**            | **252.603**  |
|          U_s           |             14              |   209.218    |
|         **Np**         |           **15**            | **254.349**  |
|          Np_s          |             15              |   213.932    |
|         **Pu**         |           **16**            | **254.436**  |
|          Pu_s          |             16              |   211.493    |

|                         |                             |              |
|:-----------------------:|:---------------------------:|:------------:|
| List of PW91 potentials |                             |              |
|     Potential name      | Number of valence electrons | ENAMX \[eV\] |
|          **H**          |            **1**            |  **250.0**   |
|           H.5           |             0.5             |    250.0     |
|          H.75           |            0.75             |    250.0     |
|          H1.25          |            1.25             |    250.0     |
|          H1.5           |             1.5             |    250.0     |
|           H_h           |              1              |    700.0     |
|         **He**          |            **2**            |  **400.0**   |
|           Li            |              1              |    140.0     |
|        **Li_sv**        |            **3**            | **271.798**  |
|         **Be**          |            **2**            |  **300.0**   |
|          Be_sv          |              4              |   308.815    |
|          **B**          |            **3**            | **318.644**  |
|           B_h           |              3              |    700.0     |
|           B_s           |              3              |    250.0     |
|          **C**          |            **4**            |  **400.0**   |
|           C_h           |              4              |    700.0     |
|           C_s           |              4              |   273.894    |
|          **N**          |            **5**            |  **400.0**   |
|           N_h           |              5              |    700.0     |
|           N_s           |              5              |    250.0     |
|          **O**          |            **6**            |  **400.0**   |
|           O_h           |              6              |    700.0     |
|           O_s           |              6              |    250.0     |
|          **F**          |            **7**            |  **400.0**   |
|           F_h           |              7              |    700.0     |
|           F_s           |              7              |    250.0     |
|         **Ne**          |            **8**            | **343.681**  |
|           Na            |              1              |    81.389    |
|        **Na_pv**        |            **7**            |  **300.0**   |
|          Na_sv          |              9              |    700.0     |
|         **Mg**          |            **2**            | **210.083**  |
|          Mg_pv          |              8              |   265.602    |
|         **Al**          |            **3**            | **240.437**  |
|          Al_h           |              3              |   295.008    |
|         **Si**          |            **4**            | **245.435**  |
|          Si_h           |              4              |   380.358    |
|          **P**          |            **5**            |  **270.0**   |
|           P_h           |              5              |   390.361    |
|          **S**          |            **6**            |  **280.0**   |
|           S_h           |              6              |   402.548    |
|         **Cl**          |            **7**            |  **280.0**   |
|          Cl_h           |              7              |    409.2     |
|         **Ar**          |            **8**            | **266.356**  |
|          K_pv           |              7              |    150.0     |
|        **K_sv**         |            **9**            | **259.333**  |
|           Ca            |              2              |   102.811    |
|          Ca_pv          |              8              |    150.0     |
|        **Ca_sv**        |           **10**            | **290.424**  |
|           Sc            |              3              |   154.804    |
|        **Sc_sv**        |           **11**            | **222.696**  |
|           Ti            |              4              |   178.367    |
|          Ti_pv          |             10              |   222.364    |
|        **Ti_sv**        |           **12**            | **274.616**  |
|            V            |              5              |   192.578    |
|          V_pv           |             11              |   263.695    |
|        **V_sv**         |           **13**            | **263.695**  |
|           Cr            |              6              |   227.109    |
|        **Cr_pv**        |           **12**            | **265.704**  |
|           Mn            |              7              |   269.887    |
|        **Mn_pv**        |           **13**            | **269.887**  |
|         **Fe**          |            **8**            | **267.907**  |
|          Fe_pv          |             14              |   293.258    |
|          Fe_sv          |             16              |   390.561    |
|         **Co**          |            **9**            | **267.995**  |
|         **Ni**          |           **10**            | **269.561**  |
|          Ni_pv          |             16              |   367.921    |
|         **Cu**          |           **11**            | **273.246**  |
|          Cu_pv          |             17              |   368.583    |
|         **Zn**          |           **12**            | **276.749**  |
|           Ga            |              3              |   134.733    |
|        **Ga_d**         |           **13**            | **282.718**  |
|          Ga_h           |             13              |   404.633    |
|           Ge            |              4              |   173.845    |
|        **Ge_d**         |           **14**            | **287.594**  |
|          Ge_h           |             14              |   410.475    |
|         **As**          |            **5**            | **208.733**  |
|         **Se**          |            **6**            | **211.557**  |
|         **Br**          |            **7**            | **216.262**  |
|         **Kr**          |            **8**            | **185.301**  |
|          Rb_pv          |              7              |   121.969    |
|        **Rb_sv**        |            **9**            | **220.155**  |
|        **Sr_sv**        |           **10**            | **226.196**  |
|        **Y_sv**         |           **11**            | **211.698**  |
|           Zr            |              4              |   154.655    |
|        **Zr_sv**        |           **12**            | **229.898**  |
|          Nb_pv          |             11              |   207.286    |
|        **Nb_sv**        |           **13**            | **293.199**  |
|           Mo            |              6              |    224.58    |
|          Mo_pv          |             12              |    224.58    |
|           Tc            |              7              |   228.688    |
|        **Tc_pv**        |           **13**            | **228.688**  |
|           Ru            |              8              |   213.271    |
|        **Ru_pv**        |           **14**            | **230.419**  |
|          Ru_sv          |             16              |   325.765    |
|           Rh            |              9              |   228.993    |
|        **Rh_pv**        |           **15**            | **271.449**  |
|         **Pd**          |           **10**            | **250.918**  |
|          Pd_pv          |             16              |    350.0     |
|         **Ag**          |           **11**            | **249.842**  |
|         **Cd**          |           **12**            | **274.325**  |
|           In            |              3              |    95.997    |
|        **In_d**         |           **13**            | **239.209**  |
|           Sn            |              4              |   103.267    |
|        **Sn_d**         |           **14**            |  **241.09**  |
|         **Sb**          |            **5**            |  **172.1**   |
|         **Te**          |            **6**            | **174.996**  |
|          **I**          |            **7**            | **175.639**  |
|         **Xe**          |            **8**            | **153.081**  |
|        **Cs_sv**        |            **9**            | **220.143**  |
|        **Ba_sv**        |           **10**            | **187.204**  |
|         **La**          |           **11**            | **219.271**  |
|          La_s           |              9              |   136.553    |
|         **Ce**          |           **12**            | **300.014**  |
|          Ce_3           |             11              |   181.336    |
|          Ce_s           |             10              |   169.178    |
|           Pr            |             13              |   252.521    |
|        **Pr_3**         |           **11**            | **181.693**  |
|           Nd            |             14              |   253.289    |
|        **Nd_3**         |           **11**            | **182.593**  |
|           Pm            |             15              |   258.471    |
|        **Pm_3**         |           **11**            | **183.955**  |
|           Sm            |             16              |   255.347    |
|          Sm_2           |             10              |    183.22    |
|        **Sm_3**         |           **11**            | **184.729**  |
|           Eu            |             17              |   249.776    |
|        **Eu_2**         |            **8**            |  **99.303**  |
|           Gd            |             18              |   256.563    |
|        **Gd_3**         |            **9**            | **154.375**  |
|        **Tb_3**         |            **9**            | **155.659**  |
|        **Dy_3**         |            **9**            | **155.765**  |
|        **Ho_3**         |            **9**            | **154.194**  |
|        **Er_3**         |            **9**            | **155.099**  |
|           Tm            |             23              |   257.516    |
|        **Tm_3**         |            **9**            | **154.002**  |
|           Yb            |             24              |   291.902    |
|        **Yb_2**         |            **8**            | **112.547**  |
|        **Lu_3**         |            **9**            | **155.066**  |
|           Hf            |              4              |   220.361    |
|        **Hf_pv**        |           **10**            | **220.361**  |
|           Ta            |              5              |   223.688    |
|        **Ta_pv**        |           **11**            | **223.688**  |
|            W            |              6              |   223.072    |
|          W_pv           |             12              |   223.072    |
|         **Re**          |            **7**            | **226.223**  |
|          Re_pv          |             13              |   226.223    |
|         **Os**          |            **8**            | **228.022**  |
|          Os_pv          |             14              |   228.022    |
|         **Ir**          |            **9**            | **210.865**  |
|         **Pt**          |           **10**            | **230.277**  |
|         **Au**          |           **11**            | **229.938**  |
|         **Hg**          |           **12**            | **233.196**  |
|           Tl            |              3              |    90.216    |
|        **Tl_d**         |           **13**            |  **237.04**  |
|           Pb            |              4              |    98.004    |
|        **Pb_d**         |           **14**            | **237.829**  |
|           Bi            |              5              |   105.043    |
|        **Bi_d**         |           **15**            | **242.843**  |
|         **Ac**          |           **11**            | **169.923**  |
|          Ac_s           |              9              |   119.913    |
|         **Th**          |           **12**            | **247.429**  |
|          Th_s           |             10              |   169.492    |
|         **Pa**          |           **13**            | **252.303**  |
|          Pa_s           |             11              |   193.575    |
|          **U**          |           **14**            | **252.603**  |
|           U_s           |             14              |   209.102    |
|         **Np**          |           **15**            | **254.354**  |
|          Np_s           |             15              |   210.883    |
|         **Pu**          |           **16**            | **254.444**  |
|          Pu_s           |             16              |   211.377    |

|                        |                             |              |
|:----------------------:|:---------------------------:|:------------:|
| List of PBE potentials |                             |              |
|     Potential name     | Number of valence electrons | ENAMX \[eV\] |
|         **H**          |            **1**            |  **250.0**   |
|          H.5           |             0.5             |    250.0     |
|          H.75          |            0.75             |    250.0     |
|         H1.25          |            1.25             |    250.0     |
|          H1.5          |             1.5             |    250.0     |
|          H_h           |              1              |    700.0     |
|         **He**         |            **2**            | **478.896**  |
|           Li           |              1              |    140.0     |
|       **Li_sv**        |            **3**            | **499.034**  |
|         Li_sv2         |              3              |   555.106    |
|         **Be**         |            **2**            | **247.544**  |
|         Be_sv          |              4              |    308.75    |
|         **B**          |            **3**            | **318.606**  |
|          B_h           |              3              |    700.0     |
|          B_s           |              3              |   269.245    |
|         **C**          |            **4**            |  **400.0**   |
|          C_d           |              4              |   413.992    |
|          C_h           |              4              |    700.0     |
|         C_h_nr         |              4              |   741.684    |
|          C_s           |              4              |   273.901    |
|      runelements       |              4              |    400.0     |
|         **N**          |            **5**            |  **400.0**   |
|          N_h           |              5              |    700.0     |
|          N_s           |              5              |    279.68    |
|          N_vs          |              5              |    279.68    |
|         **O**          |            **6**            |  **400.0**   |
|          O_h           |              6              |    700.0     |
|          O_s           |              6              |   282.841    |
|          O_sv          |              8              |   1421.493   |
|         **F**          |            **7**            |  **400.0**   |
|          F_h           |              7              |    700.0     |
|          F_s           |              7              |   289.825    |
|         **Ne**         |            **8**            | **343.606**  |
|           Na           |              1              |   101.968    |
|       **Na_pv**        |            **7**            | **259.561**  |
|         Na_sv          |              9              |    700.0     |
|         **Mg**         |            **2**            | **210.012**  |
|         Mg_new         |              2              |   126.143    |
|         Mg_pv          |              8              |   403.929    |
|       Mg_pv.old        |              8              |   265.574    |
|         Mg_sv          |             10              |   495.223    |
|         **Al**         |            **3**            |  **240.3**   |
|         **Si**         |            **4**            | **245.345**  |
|          Si_h          |              4              |   380.146    |
|        Si_h_old        |              4              |   380.146    |
|        Si_nopc         |              4              |   245.345    |
|    runelements_PBE0    |              4              |   245.345    |
|         **P**          |            **5**            |  **270.0**   |
|          P_h           |              5              |   390.202    |
|         **S**          |            **6**            |  **280.0**   |
|          S_h           |              6              |   402.436    |
|         **Cl**         |            **7**            |  **280.0**   |
|          Cl_h          |              7              |   409.136    |
|         **Ar**         |            **8**            | **266.393**  |
|          K_pv          |              7              |   116.731    |
|        **K_sv**        |            **9**            | **259.216**  |
|           Ca           |              2              |   102.755    |
|         Ca_pv          |              8              |   119.554    |
|       **Ca_sv**        |           **10**            | **266.586**  |
|           Sc           |              3              |   154.763    |
|       **Sc_sv**        |           **11**            | **222.664**  |
|        Sc_sv_h         |             11              |   380.696    |
|           Ti           |              4              |    178.33    |
|         Ti_pv          |             10              |   222.338    |
|       **Ti_sv**        |           **12**            | **274.574**  |
|        Ti_sv_h         |             12              |   388.698    |
|       Ti_sv_new        |             12              |    274.61    |
|       Ti_sv_new2       |             12              |    274.61    |
|      runelements2      |             12              |   863.342    |
|           V            |              5              |   192.543    |
|          V_pv          |             11              |   263.675    |
|        **V_sv**        |           **13**            | **263.675**  |
|         V_sv_h         |             13              |   390.664    |
|        V_sv_new        |             13              |   263.673    |
|           Cr           |              6              |   227.082    |
|       **Cr_pv**        |           **12**            | **265.683**  |
|       Cr_pv_new        |             12              |   265.681    |
|         Cr_sv          |             14              |   395.471    |
|       Cr_sv_new        |             14              |   395.471    |
|           Mn           |              7              |   269.865    |
|       **Mn_pv**        |           **13**            | **269.865**  |
|       Mn_pv_new        |             13              |   269.864    |
|         Mn_sv          |             15              |   387.187    |
|         **Fe**         |            **8**            | **267.883**  |
|         Fe_pv          |             14              |   293.238    |
|       Fe_pv_new        |             14              |   293.238    |
|         Fe_sv          |             16              |   390.558    |
|        Fe_sv_h         |             16              |   547.365    |
|         **Co**         |            **9**            | **267.969**  |
|         Co_new         |              9              |   267.968    |
|         Co_sv          |             17              |   390.362    |
|         **Ni**         |           **10**            | **269.533**  |
|         Ni_new         |             10              |   269.532    |
|         Ni_pv          |             16              |   367.945    |
|         **Cu**         |           **11**            | **273.214**  |
|          Cu_f          |             11              |   295.446    |
|         Cu_new         |             11              |   295.446    |
|         Cu_pv          |             17              |   368.605    |
|         Cu_pvf         |             17              |   368.648    |
|         **Zn**         |           **12**            | **276.727**  |
|         Zn_pv          |             18              |   376.607    |
|           Ga           |              3              |   134.678    |
|        **Ga_d**        |           **13**            | **282.697**  |
|          Ga_h          |             13              |   404.601    |
|          Ga_s          |              3              |    83.836    |
|           Ge           |              4              |   173.807    |
|        **Ge_d**        |           **14**            | **310.294**  |
|         Ge_d3          |             14              |   226.106    |
|          Ge_h          |             14              |   410.425    |
|         **As**         |            **5**            |  **208.68**  |
|          As_d          |             15              |   288.651    |
|         **Se**         |            **6**            | **211.534**  |
|         **Br**         |            **7**            | **216.264**  |
|         **Kr**         |            **8**            |  **185.26**  |
|         Rb_pv          |              7              |   121.919    |
|       **Rb_sv**        |            **9**            | **220.022**  |
|       **Sr_sv**        |           **10**            | **229.282**  |
|        **Y_sv**        |           **11**            | **211.641**  |
|           Zr           |              4              |   154.632    |
|       **Zr_sv**        |           **12**            | **229.839**  |
|       Zr_sv_new        |             12              |   229.898    |
|         Nb_pv          |             11              |   208.608    |
|       **Nb_sv**        |           **13**            | **293.235**  |
|       Nb_sv_new        |             13              |   293.235    |
|           Mo           |              6              |   224.584    |
|         Mo_pv          |             12              |   224.584    |
|       Mo_pv_new        |             12              |   224.584    |
|       **Mo_sv**        |           **14**            | **242.676**  |
|           Tc           |              7              |   228.694    |
|         Tc_new         |              7              |   228.694    |
|       **Tc_pv**        |           **13**            | **228.699**  |
|       Tc_pv_new        |             13              |   263.523    |
|           Ru           |              8              |   213.276    |
|         Ru_new         |              8              |   213.271    |
|       **Ru_pv**        |           **14**            | **230.429**  |
|       Ru_pv_new        |             14              |   240.049    |
|         Ru_sv          |             16              |   318.855    |
|           Rh           |              9              |    229.0     |
|         Rh_new         |              9              |   228.996    |
|       **Rh_pv**        |           **15**            |  **271.47**  |
|       Rh_pv_new        |             15              |   247.408    |
|         **Pd**         |           **10**            | **250.925**  |
|         Pd_new         |             10              |   250.925    |
|         Pd_pv          |             16              |   271.098    |
|       Pd_pv_new        |             16              |   250.925    |
|        Pd_vnew         |             10              |   250.925    |
|         **Ag**         |           **11**            | **249.846**  |
|         Ag_new         |             11              |   249.844    |
|         Ag_pv          |             17              |   297.865    |
|         **Cd**         |           **12**            | **274.342**  |
|           In           |              3              |    95.934    |
|        **In_d**        |           **13**            | **239.218**  |
|           Sn           |              4              |   103.236    |
|        **Sn_d**        |           **14**            |  **241.09**  |
|         **Sb**         |            **5**            | **172.037**  |
|         **Te**         |            **6**            | **174.982**  |
|         Te_rel         |              6              |   174.979    |
|         **I**          |            **7**            | **175.647**  |
|         **Xe**         |            **8**            | **153.098**  |
|       **Cs_sv**        |            **9**            | **220.318**  |
|       **Ba_sv**        |           **10**            |  **187.21**  |
|         **La**         |           **11**            | **219.313**  |
|          La_s          |              9              |   136.552    |
|         **Ce**         |           **12**            | **273.042**  |
|          Ce_3          |             11              |   181.286    |
|          Ce_h          |             12              |    299.9     |
|           Pr           |             13              |   272.941    |
|        **Pr_3**        |           **11**            | **182.312**  |
|           Nd           |             14              |   253.189    |
|        **Nd_3**        |           **11**            | **182.546**  |
|           Pm           |             15              |   258.627    |
|        **Pm_3**        |           **11**            | **183.908**  |
|           Sm           |             16              |   257.515    |
|        **Sm_3**        |           **11**            | **177.087**  |
|           Eu           |             17              |   249.668    |
|        **Eu_2**        |            **8**            |  **99.304**  |
|          Eu_3          |              9              |   129.057    |
|           Gd           |             18              |   256.472    |
|        **Gd_3**        |            **9**            | **154.348**  |
|           Tb           |             19              |   264.824    |
|        **Tb_3**        |            **9**            | **155.628**  |
|           Dy           |             20              |   255.467    |
|        **Dy_3**        |            **9**            | **155.729**  |
|           Ho           |             21              |   257.168    |
|        **Ho_3**        |            **9**            | **154.153**  |
|           Er           |             22              |   298.116    |
|          Er_2          |              8              |    119.75    |
|        **Er_3**        |            **9**            | **155.053**  |
|           Tm           |             23              |   257.419    |
|        **Tm_3**        |            **9**            | **149.221**  |
|           Yb           |             24              |   253.028    |
|        **Yb_2**        |            **8**            | **112.543**  |
|         Yb_2_n         |             10              |   144.685    |
|           Lu           |             25              |   255.695    |
|        **Lu_3**        |            **9**            | **155.009**  |
|           Hf           |              4              |   220.333    |
|       **Hf_pv**        |           **10**            | **220.342**  |
|         Hf_sv          |             12              |   237.444    |
|           Ta           |              5              |   223.667    |
|       **Ta_pv**        |           **11**            | **223.675**  |
|           W            |              6              |   223.057    |
|          W_pv          |             12              |   223.065    |
|        W_pv_new        |             12              |   223.057    |
|         **Re**         |            **7**            | **226.216**  |
|         Re_pv          |             13              |   226.223    |
|         **Os**         |            **8**            | **228.022**  |
|         Os_pv          |             14              |   228.022    |
|         **Ir**         |            **9**            |  **210.87**  |
|         **Pt**         |           **10**            | **230.283**  |
|        Pt_ZORA         |             10              |   230.281    |
|         Pt_new         |             10              |   230.283    |
|         Pt_pv          |             16              |   294.607    |
|       Pt_pv_ZORA       |             16              |   294.604    |
|         **Au**         |           **11**            | **229.948**  |
|         Au_new         |             11              |   229.943    |
|         **Hg**         |           **12**            | **233.214**  |
|           Tl           |              3              |    90.14     |
|        **Tl_d**        |           **13**            | **237.063**  |
|           Pb           |              4              |    97.973    |
|        **Pb_d**        |           **14**            | **237.846**  |
|        Pb_d_rel        |             14              |   237.809    |
|       Pb_d_rel2        |             14              |   237.809    |
|           Bi           |              5              |   105.037    |
|        **Bi_d**        |           **15**            | **242.851**  |
|         Bi_pv          |             21              |   309.187    |
|           Po           |              6              |   159.707    |
|        **Po_d**        |           **16**            | **264.565**  |
|         **At**         |            **7**            |  **161.43**  |
|          At_d          |             17              |   266.251    |
|         **Rn**         |            **8**            | **152.121**  |
|       **Fr_sv**        |            **9**            |  **214.54**  |
|       **Ra_sv**        |           **10**            | **237.367**  |
|         **Ac**         |           **11**            | **172.237**  |
|         **Th**         |           **12**            | **247.449**  |
|          Th_s          |             10              |   169.492    |
|         **Pa**         |           **13**            | **252.316**  |
|          Pa_s          |             11              |   193.576    |
|         **U**          |           **14**            | **252.616**  |
|          U_s           |             14              |   209.069    |
|         **Np**         |           **15**            | **254.369**  |
|          Np_s          |             15              |   210.851    |
|         **Pu**         |           **16**            | **254.458**  |
|          Pu_h          |             16              |   444.783    |
|          Pu_s          |             16              |   211.344    |
|         **Am**         |           **17**            | **255.875**  |

#### GW potentials\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: GW potentials">edit</a> \| (./index.php.md)\]

|                        |                             |              |
|:----------------------:|:---------------------------:|:------------:|
| List of LDA potentials |                             |              |
|     Potential name     | Number of valence electrons | ENAMX \[eV\] |
|        **H_GW**        |            **1**            | **400.725**  |
|         H_h_GW         |              1              |   822.759    |
|        H_nc_GW         |              1              |    1000.0    |
|       **He_GW**        |            **2**            | **404.806**  |
|        Li_AE_GW        |              3              |   433.253    |
|       Li_AE_GW2        |              3              |   509.283    |
|         Li_GW          |              1              |   112.417    |
|      **Li_sv_GW**      |            **3**            | **433.253**  |
|       Li_sv_GW\_       |              3              |   433.253    |
|        Be_AE_GW        |              4              |   536.216    |
|         Be_GW          |              2              |   247.951    |
|        **B_GW**        |            **3**            | **318.762**  |
|        **C_GW**        |            **4**            | **413.992**  |
|         C_f_GW         |              4              |   742.464    |
|         C_h_GW         |              4              |   742.464    |
|        C_nc_GW         |              4              |   1261.234   |
|        **N_GW**        |            **5**            | **420.681**  |
|         N_s_GW         |              5              |   296.222    |
|        **O_GW**        |            **6**            | **414.315**  |
|         O_h_GW         |              6              |   765.442    |
|         O_s_GW         |              6              |   300.418    |
|        **F_GW**        |            **7**            | **487.335**  |
|         F_d_GW         |              7              |   487.335    |
|         F_h_GW         |              7              |   772.351    |
|       **Ne_GW**        |            **8**            |  **400.0**   |
|         Ne_GW2         |              8              |   317.594    |
|         Na_GW          |              1              |    81.642    |
|        Na_pv_GW        |              7              |   259.494    |
|      **Na_sv_GW**      |            **9**            | **260.372**  |
|         Mg_GW          |              2              |   126.671    |
|        Mg_pv_GW        |              8              |   403.538    |
|     Mg_pv_parsv_GW     |              8              |   454.933    |
|      **Mg_sv_GW**      |           **10**            |  **473.54**  |
|        Al_d_GW         |              3              |   240.957    |
|        Al_sv_GW        |             11              |   411.007    |
|        Si_d_GW         |              4              |   245.704    |
|       Si_d_GW_nr       |              4              |   245.702    |
|        Si_f_GW         |              4              |   245.704    |
|        Si_sv_GW        |             12              |   546.548    |
|       Si_sv_GW\_       |             12              |    475.15    |
|      Si_sv_GW\_\_      |             12              |   546.548    |
|      Si_sv_GW_nr       |             12              |   475.153    |
|         P_d_GW         |              5              |   255.155    |
|         S_d_GW         |              6              |   258.602    |
|        Cl_d_GW         |              7              |    262.25    |
|       **Ar_GW**        |            **8**            | **266.101**  |
|      **Ti_sv_GW**      |           **12**            | **312.205**  |
|         Mn_GW          |              7              |   278.537    |
|        Mn_pv_GW        |             13              |   352.359    |
|      **Mn_sv_GW**      |           **15**            | **357.618**  |
|         Fe_GW          |              8              |   321.044    |
|        Fe_pv_GW        |             14              |   365.183    |
|      **Fe_sv_GW**      |           **16**            | **402.658**  |
|       Fe_sv_GW_f       |             16              |   443.614    |
|         Co_GW          |              9              |   323.447    |
|        Co_pv_GW        |             15              |   364.275    |
|      **Co_sv_GW**      |           **17**            | **363.483**  |
|         Ni_GW          |             10              |   357.352    |
|        Ni_pv_GW        |             16              |   367.726    |
|      **Ni_sv_GW**      |           **18**            | **485.721**  |
|         Cu_GW          |             11              |   417.032    |
|        Cu_GW_h         |             11              |    971.8     |
|        Cu_pv_GW        |             17              |   466.991    |
|         Zn_GW          |             12              |   360.353    |
|       Zn_GW.old        |             12              |   401.745    |
|         Zn_GW2         |             12              |   556.955    |
|        Zn_pv_GW        |             18              |   401.745    |
|      Zn_pv_GW.old      |             18              |   499.462    |
|      **Zn_sv_GW**      |           **20**            | **499.462**  |
|      Zn_sv_GW.old      |             20              |   1708.968   |
|       Zn_sv_GW\_       |             20              |   499.462    |
|         Ga_GW          |              3              |    134.8     |
|      **Ga_d_GW**       |           **13**            | **369.987**  |
|      Ga_d_GW.old       |             13              |   333.963    |
|        Ga_pv_GW        |             19              |   422.752    |
|     Ga_pv_GW.nrel      |             19              |   422.391    |
|      Ga_pv_GW.old      |             19              |   449.579    |
|        Ga_sv_GW        |             21              |   503.451    |
|      Ga_sv_GW.old      |             21              |   449.579    |
|       Ga_sv_GW2        |             21              |   642.887    |
|         Ge_GW          |              4              |   173.969    |
|      **Ge_d_GW**       |           **14**            | **310.448**  |
|       **As_GW**        |            **5**            |  **208.87**  |
|        As_GW_n         |              5              |    208.87    |
|        As_d2_GW        |             15              |   752.859    |
|        As_d_GW         |             15              |   863.991    |
|       **Se_GW**        |            **6**            | **211.602**  |
|       **Kr_GW**        |            **8**            | **185.392**  |
|      **Zr_sv_GW**      |           **12**            | **307.802**  |
|         Ru_GW          |              8              |   230.359    |
|        Ru_f_GW         |              8              |   268.875    |
|        Ru_pv_GW        |             14              |   239.907    |
|         Rh_GW          |              9              |   247.321    |
|        Rh_f_GW         |              9              |   247.321    |
|        Rh_pv_GW        |             15              |   247.321    |
|         Pd_GW          |             10              |   250.832    |
|        Pd_f_GW         |             10              |   250.832    |
|         Ag_GW          |             11              |   249.752    |
|        Ag_f_GW         |             11              |   249.752    |
|         Cd_GW          |             12              |   361.653    |
|       Cd_GW.old        |             12              |   274.265    |
|        Cd_f_GW         |             12              |   217.846    |
|        Cd_pv_GW        |             18              |   396.576    |
|      **Cd_sv_GW**      |           **20**            |  **650.91**  |
|      **In_d_GW**       |           **13**            | **278.582**  |
|         Sn_GW          |              4              |   103.318    |
|         Sb_GW          |              5              |   172.301    |
|      **Sb_d_GW**       |           **15**            | **263.147**  |
|       **Te_GW**        |            **6**            | **175.144**  |
|       **Xe_GW**        |            **8**            | **179.528**  |
|      **Hf_sv_GW**      |           **12**            | **296.646**  |
|        Pt_f_GW         |             10              |   248.657    |
|      **Pb_d_GW**       |           **14**            | **237.793**  |
|      **Bi_d_GW**       |           **15**            | **242.856**  |

|                        |                             |              |
|:----------------------:|:---------------------------:|:------------:|
| List of PBE potentials |                             |              |
|     Potential name     | Number of valence electrons | ENAMX \[eV\] |
|        **C_GW**        |            **4**            | **413.992**  |
|         N_s_GW         |              5              |   296.495    |
|        **O_GW**        |            **6**            | **414.635**  |
|         O_s_GW         |              6              |   300.688    |
|         F_d_GW         |              7              |   487.698    |
|        Mg_pv_GW        |              8              |   403.929    |
|        Si_d_GW         |              4              |   245.345    |
|       Si_d_GW_nr       |              4              |   245.338    |
|        Si_pv_GW        |             10              |   475.096    |
|        Si_sv_GW        |             12              |   475.096    |
|      Si_sv_GW_nr       |             12              |   475.101    |
|      **Ti_sv_GW**      |           **12**            | **312.571**  |
|      **Ga_d_GW**       |           **13**            | **369.848**  |
|        Ga_sv_GW        |             21              |   503.418    |
|      **Ge_d_GW**       |           **14**            | **310.294**  |
|        Ge_d_GW2        |             14              |    339.13    |
|      Ge_d_GW_ref       |             14              |    572.01    |
|       **As_GW**        |            **5**            | **208.702**  |
|        As_d_GW         |             15              |   346.172    |
|       **Se_GW**        |            **6**            | **211.555**  |
|      **Zr_sv_GW**      |           **12**            | **307.836**  |
|         Sn_GW          |              4              |   103.236    |
|         Eu_GW          |             17              |   603.254    |
|      **Hf_sv_GW**      |           **12**            | **317.394**  |

### Ultrasoft pseudopotentials for LDA and PW91 (2002)\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Ultrasoft pseudopotentials for LDA and PW91 (2002)">edit</a> \| (./index.php.md)")\]

Ultrasoft pseudo potentials for LDA and PW91 (dated 2002-08-20 and
2002-04-08, respectively). These files are outdated, not supported and
only distributed as is. Some VASP feature might yield undesired results
with these files (e.g. [METAGGA](../incar-tags/METAGGA.md)).

|                        |                             |              |
|:----------------------:|:---------------------------:|:------------:|
| List of LDA potentials |                             |              |
|     Potential name     | Number of valence electrons | ENAMX \[eV\] |
|          H.75          |            0.75             |    200.0     |
|         H1.25          |            1.25             |    200.0     |
|        H_200eV         |              1              |    200.0     |
|         H_soft         |              1              |    150.0     |
|           Li           |              1              |    76.427    |
|          Li_h          |              1              |    200.0     |
|         Li_pv          |              1              |    200.0     |
|         **Be**         |            **2**            | **251.805**  |
|         **B**          |            **3**            | **257.148**  |
|          B_s           |              3              |   207.526    |
|         **C**          |            **4**            | **286.567**  |
|          C_s           |              4              |   211.061    |
|         **N**          |            **5**            | **347.853**  |
|          N_s           |              5              |   224.546    |
|         **O**          |            **6**            |  **395.7**   |
|          O_s           |              6              |   269.946    |
|         **F**          |            **7**            |  **424.54**  |
|          F_s           |              7              |   272.497    |
|         **Ne**         |            **8**            | **359.508**  |
|           Na           |              1              |    49.003    |
|          Na_h          |              1              |   165.481    |
|       **Na_pv**        |            **7**            | **216.702**  |
|         **Mg**         |            **2**            | **106.255**  |
|          Mg_h          |              2              |    250.0     |
|         Mg_pv          |              8              |   366.368    |
|         **Al**         |            **3**            | **129.206**  |
|          Al_h          |              3              |    250.0     |
|         **Si**         |            **4**            | **150.544**  |
|          Si_h          |              4              |    300.0     |
|         **P**          |            **5**            | **173.366**  |
|         **S**          |            **6**            | **197.787**  |
|         **Cl**         |            **7**            | **219.242**  |
|         **Ar**         |            **8**            | **215.808**  |
|           K            |              1              |    70.923    |
|          K_pv          |              7              |   146.685    |
|          K_s           |              1              |    35.993    |
|           Ca           |              2              |   104.743    |
|         Ca_pv          |              8              |    400.0     |
|           Sc           |              3              |    150.21    |
|         Sc_pv          |              9              |   178.616    |
|           Ti           |              4              |   181.353    |
|         Ti_pv          |             10              |   222.444    |
|           V            |              5              |   211.721    |
|          V_pv          |             11              |   263.722    |
|           Cr           |              6              |    227.21    |
|           Mn           |              7              |    227.24    |
|       **Mn_pv**        |           **13**            |  **227.24**  |
|         **Fe**         |            **8**            | **237.587**  |
|         **Co**         |            **9**            | **236.542**  |
|         **Ni**         |           **10**            | **241.683**  |
|         **Cu**         |           **11**            | **233.781**  |
|         **Zn**         |           **12**            |  **209.61**  |
|           Ga           |              3              |   129.849    |
|        **Ga_d**        |           **13**            | **213.675**  |
|           Ge           |              4              |   139.215    |
|         **As**         |            **5**            | **144.267**  |
|         **Se**         |            **6**            | **155.091**  |
|         **Br**         |            **7**            | **165.656**  |
|         **Kr**         |            **8**            | **167.754**  |
|           Rb           |              1              |    63.553    |
|         Rb_pv          |              7              |    122.21    |
|          Rb_s          |              1              |    31.936    |
|           Sr           |              2              |    85.927    |
|         Sr_pv          |              8              |   119.124    |
|           Y            |              3              |   119.285    |
|          Y_pv          |              9              |   119.285    |
|           Zr           |              4              |   149.994    |
|         Zr_pv          |             10              |   149.994    |
|           Nb           |              5              |   174.786    |
|         Nb_pv          |             11              |   174.786    |
|           Mo           |              6              |   186.479    |
|         Mo_pv          |             12              |   186.479    |
|           Tc           |              7              |   195.876    |
|           Ru           |              8              |   203.565    |
|           Rh           |              9              |    205.46    |
|         **Pd**         |           **10**            | **198.955**  |
|         **Ag**         |           **11**            | **180.602**  |
|         **Cd**         |           **12**            | **167.891**  |
|           In           |              3              |    91.885    |
|        **In_d**        |           **13**            | **151.593**  |
|           Sn           |              4              |   106.396    |
|        **Sn_d**        |           **14**            | **175.475**  |
|         **Sb**         |            **5**            | **106.592**  |
|         **Te**         |            **6**            | **114.866**  |
|         **I**          |            **7**            | **122.098**  |
|         **Xe**         |            **8**            | **124.672**  |
|           Cs           |              1              |    47.984    |
|         Cs_pv          |              7              |   106.139    |
|         Ba_pv          |              8              |   101.184    |
|           Hf           |              4              |   149.521    |
|           W            |              6              |   188.254    |
|         **Re**         |            **7**            |  **193.9**   |
|         **Os**         |            **8**            | **201.567**  |
|         **Ir**         |            **9**            | **198.239**  |
|         **Pt**         |           **10**            | **191.383**  |
|         **Au**         |           **11**            | **179.692**  |
|         **Hg**         |           **12**            | **158.977**  |
|        **Tl_d**        |           **13**            | **177.499**  |
|           Bi           |              5              |    99.087    |
|           Pb           |              4              |    88.444    |
|        **Pb_d**        |           **14**            | **144.342**  |
|        **Bi_d**        |           **15**            | **242.856**  |

|                         |                             |              |
|:-----------------------:|:---------------------------:|:------------:|
| List of PW91 potentials |                             |              |
|     Potential name      | Number of valence electrons | ENAMX \[eV\] |
|         H_200eV         |              1              |    200.0     |
|         H_soft          |              1              |    150.0     |
|           Li            |              1              |    76.254    |
|          Li_h           |              1              |    250.0     |
|          Li_pv          |              1              |    250.0     |
|         **Be**          |            **2**            | **251.408**  |
|          **B**          |            **3**            |  **257.17**  |
|           B_s           |              3              |   207.644    |
|          **C**          |            **4**            | **286.744**  |
|           C_s           |              4              |   211.293    |
|          **N**          |            **5**            | **348.097**  |
|           N_s           |              5              |   224.806    |
|          **O**          |            **6**            | **395.994**  |
|           O_s           |              6              |   270.222    |
|          **F**          |            **7**            | **424.865**  |
|           F_s           |              7              |   272.744    |
|         **Ne**          |            **8**            | **359.508**  |
|           Na            |              1              |    48.686    |
|          Na_h           |              1              |    165.08    |
|        **Na_pv**        |            **7**            | **300.769**  |
|         **Mg**          |            **2**            | **106.148**  |
|          Mg_h           |              2              |    250.0     |
|          Mg_pv          |              8              |   365.887    |
|         **Al**          |            **3**            | **129.208**  |
|          Al_h           |              3              |    250.0     |
|         **Si**          |            **4**            | **150.615**  |
|          Si_h           |              4              |    300.0     |
|          **P**          |            **5**            | **173.498**  |
|          **S**          |            **6**            |  **197.97**  |
|         **Cl**          |            **7**            | **219.471**  |
|         **Ar**          |            **8**            | **215.808**  |
|            K            |              1              |    70.923    |
|          K_pv           |              7              |    140.0     |
|           Ca            |              2              |   104.434    |
|          Ca_pv          |              8              |    300.0     |
|           Sc            |              3              |   150.002    |
|          Sc_pv          |              9              |   178.471    |
|           Ti            |              4              |   181.203    |
|          Ti_pv          |             10              |   222.373    |
|            V            |              5              |   211.612    |
|          V_pv           |             11              |   243.767    |
|           Cr            |              6              |   227.117    |
|           Mn            |              7              |   227.152    |
|         **Fe**          |            **8**            |  **237.51**  |
|         **Co**          |            **9**            | **236.473**  |
|         **Ni**          |           **10**            | **241.622**  |
|         **Cu**          |           **11**            | **233.729**  |
|         **Zn**          |           **12**            | **209.545**  |
|           Ga            |              3              |   129.795    |
|        **Ga_d**         |           **13**            | **213.598**  |
|           Ge            |              4              |   139.187    |
|         **As**          |            **5**            | **144.302**  |
|         **Se**          |            **6**            | **155.175**  |
|         **Br**          |            **7**            | **165.786**  |
|         **Kr**          |            **8**            | **167.754**  |
|           Rb            |              1              |    63.093    |
|          Rb_pv          |              7              |   121.987    |
|           Sr            |              2              |    85.674    |
|          Sr_pv          |              8              |   118.811    |
|            Y            |              3              |   119.149    |
|          Y_pv           |              9              |   119.149    |
|           Zr            |              4              |   149.928    |
|          Zr_pv          |             10              |   149.927    |
|           Nb            |              5              |   174.766    |
|          Nb_pv          |             11              |   174.766    |
|           Mo            |              6              |   186.486    |
|          Mo_pv          |             12              |   186.486    |
|           Tc            |              7              |   195.904    |
|           Ru            |              8              |   203.611    |
|           Rh            |              9              |   205.518    |
|         **Pd**          |           **10**            |  **199.02**  |
|         **Ag**          |           **11**            |  **180.67**  |
|         **Cd**          |           **12**            | **167.929**  |
|           In            |              3              |    91.829    |
|        **In_d**         |           **13**            | **151.604**  |
|           Sn            |              4              |   106.334    |
|        **Sn_d**         |           **14**            | **175.467**  |
|         **Sb**          |            **5**            |  **106.59**  |
|         **Te**          |            **6**            | **114.902**  |
|          **I**          |            **7**            | **122.175**  |
|         **Xe**          |            **8**            | **124.672**  |
|           Cs            |              1              |    47.697    |
|          Cs_pv          |              7              |   101.438    |
|          Ba_pv          |              8              |    99.451    |
|           Hf            |              4              |   149.377    |
|           Ta            |              5              |   174.569    |
|            W            |              6              |   188.192    |
|         **Re**          |            **7**            | **193.873**  |
|         **Os**          |            **8**            | **201.569**  |
|         **Ir**          |            **9**            |  **198.27**  |
|         **Pt**          |           **10**            |  **191.44**  |
|         **Au**          |           **11**            |  **179.77**  |
|         **Hg**          |           **12**            |  **159.06**  |
|        **Tl_d**         |           **13**            | **177.536**  |
|           Bi            |              5              |    99.073    |
|           Pb            |              4              |    88.425    |
|        **Pb_d**         |           **14**            | **144.354**  |

### LDA & PBE, 5.2 & 5.4 (original univie release version)\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: LDA &amp; PBE, 5.2 &amp; 5.4 (original univie release version)">edit</a> \| (./index.php.md)")\]

|  |
|----|
| **Mind:** *LDA & PBE, 5.2 & 5.4 (original univie release version)* potentials are equivalent to the [potpaw.52](#potpaw.52) and [potpaw.54](#potpaw.54) sets, other than some TITLE strings and missing hash keys. Thus, they are not listed explicitly here. Use them only if you need strictly identical files. |

## Different variants specified by the suffix\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: Different variants specified by the suffix">edit</a> \| (./index.php.md)\]

For most elements different variants of [POTCAR](POTCAR.md)
files exist for each element within a specific set (e.g. potpaw_PBE.64).
The different [POTCAR](POTCAR.md) vartiations are
distinguished by their suffixes. Not all variants are available for
every element or in all pseudopotential sets.

|  |  |  |
|----|----|----|
| Suffix | Explanation | Example |
| **\_s** | This suffix indicates a soft potential, with a larger core radius and a lower requirement for the plane-wave energy cutoff. Although computation time is significantly reduced, transferability and accuracy are compromised to some extent. | The O potential has a core radius of 1.52 atomic units (a.u.) and <a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> of 400 electron Volts (eV). The O_s potential has a core radius of 1.85 a.u. and a cutoff of 282.9 eV. |
| **\_h** | This suffix signifies a hard potential, with a smaller core radius and a higher requirement for the plane-wave energy cutoff. Although this type of potentials increases computational cost, it might be required for some systems, particularly when dealing with short bonds. Additionally, hard potentials tend to be more transferable than soft ones. | The O_h potential has a core radius of 1.1 a.u. and <a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> is set to 765.5 eV. |
| **\_pv** | Semicore *p* states are considered valence states. Additionally, these types of potentials are a bit harder. Computational cost increases, but accuracy and transferability as well. | The Ti potential has four valence electrons, two in the 3*d* shell, and two in the 4*s* shell. Ti_pv adds six electrons in the 3*p* shell. |
| **\_sv** | Semicore *p* and *s* states are considered valence states. Additionally, these types of potentials are harder than those without a suffix. Computational cost increases, but accuracy and transferability as well. | Ti_sv adds two more electrons, so now we have a 3*s*<sup>2</sup>3*p*<sup>6</sup>3*d*<sup>2</sup>4*s*<sup>2</sup> configuration with 12 total electrons |
| **\_d** | Semicore *d* states are considered valence states. Additionally these type of potentials are a bit harder. Computational cost increases, but accuracy and transferability as well. | The Ge potential has four valence electrons, two in the 4*s* shell, and two in the 4*p* shell. Ge_d adds ten electrons in the *3d* shell. |
| **\_2** or **\_3** | Pseudopotentials with an integer suffix denote a specific valence state. These potentials are only provided for the Lanthanides. Some 4*f* electrons for these potentials are put in the frozen core, although they are higher in energy than other valence states. Be careful when using these potentials and read [the section about lanthanides with fixed valence](../tutorials/Choosing_pseudopotentials.md) beforehand. | The Er potential has 22 valence electrons with the configuration 4*f*<sup>12</sup>5*s*<sup>2</sup>5*p*<sup>6</sup>6*s*<sup>2</sup> and an energy cutoff of ~350 eV. Er_2 has 8 valence electrons with the configuration 5*p*<sup>6</sup>6*s*<sup>2</sup> and a recommended cutoff energy of ~120 eV, while Er_3 has 9 valence electrons and the configuration 5*p*<sup>6</sup>5*d*<sup>1</sup>6*s*<sup>2</sup> and a cutoff of ~155 eV. |
| **\_AE** | These potentials are only provided for H, He, and Li. They are very hard and contain all electrons (AE). These potentials are optimized to reproduce the wave functions in the atomic core region as well as possible. | Both the He and the HE_AE pseudopotentials contain two electrons, but the \_AE variant has an extremely small core radius of 0.6 a.u. (compared to 1.1 a.u. for He), and <a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> of ~2135 eV, and [EAUG](../incar-tags/EAUG.md) of ~2900 eV. |
| **\_GW** | These potentials are optimized for calculations requiring a large number of unoccupied states well above the Fermi level. This is achieved by using different projectors and taking care to reproduce the all-electron scattering properties for high energies. They are superior for excited-state properties and any calculation considering [electron-electron correlation](../categories/Category-Many-body_perturbation_theory.md) like GW, RPA, BSE, and MP2. There are some results that indicate that the \_GW potentials are also more accurate for ground-state-DFT calculations<sup>[\[3\]](#cite_note-bosoni:natphysrev:2023-3)</sup>, but the results should be very comparable with the standard potentials in most cases. Note that the \_GW suffix is the only one that is often combined with other suffixes. | The Ge and the Ge_GW potential do not differ in core-radius, recommended plane-wave-energy cutoff, or the reference configuration of the atom. However, the partial waves and projector functions used in the generation of the potential are different. |

## Related tags and sections\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

<a href="/wiki/Pseudopotentials" class="mw-redirect"
title="Pseudopotentials">Pseudopotentials</a>,
[POTCAR](POTCAR.md), <a
href="/wiki/index.php?title=Pseudopotential_basics&amp;action=edit&amp;redlink=1"
class="new"
title="Pseudopotential basics (page does not exist)">Pseudopotential
basics</a>, [Projector-augmented-wave
formalism](../methods/Projector-augmented-wave_formalism.md)

Simple instructions to set up a [POTCAR](POTCAR.md) with the
correct format: <a href="/wiki/Prepare_a_POTCAR" class="mw-redirect"
title="Prepare a POTCAR">Prepare a POTCAR</a>

Guide on how to check which flavor of pseudopotential is appropriate for
a specific calculation: [Choosing
pseudopotentials](../tutorials/Choosing_pseudopotentials.md)

## References\[<a
href="/wiki/index.php?title=Available_pseudopotentials&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-bloechl:prb:94b_1-0)</sup>
    <sup>[b](#cite_ref-bloechl:prb:94b_1-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.50.17953"
    class="external text" rel="nofollow">P. E. Blöchl, Phys. Rev. B
    <strong>50</strong>, 17953 (1994).</a>
2.  ↑
    <sup>[a](#cite_ref-kresse:prb:99_2-0)</sup>
    <sup>[b](#cite_ref-kresse:prb:99_2-1)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.59.1758" class="external text"
    rel="nofollow">I. G. Kresse and D. Joubert, Phys. Rev. B
    <strong>59</strong>, 1758 (1999).</a>
3.  [↑](#cite_ref-bosoni:natphysrev:2023_3-0)
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


