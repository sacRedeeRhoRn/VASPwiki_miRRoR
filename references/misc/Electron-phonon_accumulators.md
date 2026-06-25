<!-- Source: https://vasp.at/wiki/index.php/Electron-phonon_accumulators | revid: 32896 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Electron-phonon accumulators


Performing electron-phonon calculations using the , for example, to
compute [transport
coefficients](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
or the [renormalization of the electronic band
structure](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md),
one of the most expensive task is computing the electron-phonon matrix
elements. Accumulators provide a mechanism to efficiently reuse computed
matrix elements in the electron–phonon module. It allows to perform a
single VASP run while evaluating multiple derived quantities—such as
transport coefficients under different scattering approximations or at
varying chemical potentials—without recalculating the matrix elements
(for more information on the theory of chemical potentials see
<a href="/wiki/Chemical_potential" class="mw-redirect"
title="Chemical potential">chemical potential</a>). The accumulator
technique circumvents the need to repeat these calculations for every
set of parameters.


## Contents


- [1 How it
  works](#How_it_works)
- [2
  Output](#Output)
  - [2.1 Plain-text
    output in the OUTCAR
    file](#Plain-text_output_in_the_OUTCAR_file)
  - [2.2 Binary
    output in the vaspout.h5 HDF5
    file](#Binary_output_in_the_vaspout.h5_HDF5_file)
- [3 Related tags
  and articles](#Related_tags_and_articles)


## How it works\[<a
href="/wiki/index.php?title=Electron-phonon_accumulators&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: How it works">edit</a> \| (./index.php.md)\]

The basic idea behind accumulators is to separate the calculation of
matrix elements from their subsequent use. Once computed, these elements
are “accumulated” into different bins corresponding to various parameter
sets. For example, in transport calculations, different accumulators may
be defined for:

- Various scattering approximations set via
  [ELPH_SCATTERING_APPROX](../incar-tags/ELPH_SCATTERING_APPROX.md).
- Multiple chemical potentials set via
  [ELPH_SELFEN_MU](../incar-tags/ELPH_SELFEN_MU.md).

Let us look at the following example. If we set

- [`ELPH_SCATTERING_APPROX`](../incar-tags/ELPH_SCATTERING_APPROX.md)` = SERTA MRTA_TAU`
- [`ELPH_SELFEN_MU`](../incar-tags/ELPH_SELFEN_MU.md)` = -0.1 0.0 0.1`

then it would take a total of 6 calculations to get all combinations of
scattering approximations and chemical potentials. It would be very
inefficient to recalculate all the electron-phonon matrix elements for
each such combination. Instead, VASP internally creates an accumulator
for each combination of
[ELPH_SCATTERING_APPROX](../incar-tags/ELPH_SCATTERING_APPROX.md)
and [ELPH_SELFEN_MU](../incar-tags/ELPH_SELFEN_MU.md),
accumulating the results for all combinations without the need to
recompute matrix elements. This is a much more efficient approach, often
with negligible additional computational cost.

|  |
|----|
| **Mind:** Different temperatures supplied via [ELPH_SELFEN_TEMPS](../incar-tags/ELPH_SELFEN_TEMPS.md) will *not* create additional accumulators. The temperatures are handled as an array inside each accumulator. |

## Output\[<a
href="/wiki/index.php?title=Electron-phonon_accumulators&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Output">edit</a> \| (./index.php.md)\]

The output of each accumulator is provided in the
[OUTCAR](../output-files/OUTCAR.md) file as well as in the
[vaspout.h5](../output-files/Vaspout.h5.md) file. In both cases, each
accumulator is labeled by a unique ID that simply counts the number of
accumulators. In this section, we explain the format of the output.

### Plain-text output in the [OUTCAR](../output-files/OUTCAR.md) file\[<a
href="/wiki/index.php?title=Electron-phonon_accumulators&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Plain-text output in the OUTCAR file">edit</a> \| (./index.php.md)\]

In the [OUTCAR](../output-files/OUTCAR.md) file, each accumulator is first
listed with its ID, `N`, and all the relevant information that defines
this accumulator is written in a corresponding block. Here is an example
output that defines two self-energy accumulators:

``` mw-collapsible
Electron self-energy accumulator N =  1
----------------------------------
 Band range:               [       2:       4]
 Number of bands to sum over:     8
 Scattering approximation: constant relaxation-time approximation (CRTA)
 Static self-energy: F
 Complex imaginary shift (delta): 0.000
 Chemical potentials mu(T):
     Temperature (K)             mu (eV)
          0.00000000          9.79452083
        100.00000000          9.80301003
        200.00000000          9.82655169
 Transport energy range:   [   9.434:  10.474]  wich corresponds to    1.040 eV
 Number of selected k-points at which to compute the self-energy: [     3 /     29]
 Selected bands and k-points at which to compute the self-energy:
         2   3   4
     1   T   T   T
     2   T   T   T
     6   T   T   T

Electron self-energy accumulator N =  2
----------------------------------
 Band range:               [       2:       4]
 Number of bands to sum over:     8
 Scattering approximation: self-energy relaxation-time approximation (SERTA)
 Static self-energy: F
 Complex imaginary shift (delta): 0.000
 Chemical potentials mu(T):
     Temperature (K)             mu (eV)
          0.00000000          9.79452083
        100.00000000          9.80301003
        200.00000000          9.82655169
 Transport energy range:   [   9.434:  10.474]  wich corresponds to    1.040 eV
 Number of selected k-points at which to compute the self-energy: [     3 /     29]
 Selected bands and k-points at which to compute the self-energy:
        2   3   4
    1   T   T   T
    2   T   T   T
    6   T   T   T
```

The difference between the two accumulators is in the scattering
approximation (set by
[ELPH_SCATTERING_APPROX](../incar-tags/ELPH_SCATTERING_APPROX.md)):
one uses CRTA and one uses SERTA.

|  |
|----|
| **Mind:** The difference between CRTA and SERTA is only relevant in the context of [transport calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md). The computed self-energies do not depend on the scattering approximation. |

This way, you can quickly figure out which accumulator corresponds to
which combination of computational parameters. The computed
self-energies for each accumulator are then given below. Here is an
example output for the first accumulator and the first temperature:

``` mw-collapsible
Electron self-energy accumulator N=  1
 T=       0. K
 ispin  ikpt iband       KS eV  re(Fan) eV  im(Fan) eV       DW eV   Fan+DW eV
     1     1     2    9.822840    0.000000   -0.001688    0.000000    0.000000
     1     1     3    9.822840    0.000000   -0.001688    0.000000    0.000000
     1     1     4    9.822841    0.000000   -0.001688    0.000000    0.000000
     1     2     2    7.396326    0.000000   -0.110687    0.000000    0.000000
     1     2     3    9.166331    0.000000   -0.013618    0.000000    0.000000
     1     2     4    9.166332    0.000000   -0.013618    0.000000    0.000000
     1     6     2    8.086060    0.000000   -0.073793    0.000000    0.000000
     1     6     3    8.086060    0.000000   -0.073793    0.000000    0.000000
     1     6     4    8.496795    0.000000   -0.067575    0.000000    0.000000
```

|  |
|----|
| **Mind:** In this case, only the imaginary part of the self-energy is calculated (useful for transport calculations). |

For transport calculations, there are additional *transport*
accumulators. The corresponding [OUTCAR](../output-files/OUTCAR.md) output
has a structure that is similar to that of the self-energy. First, the
transport accumulators are listed and defined:

``` mw-collapsible
Transport calculator N =  1
----------------------------------
 transport driver: 2 ! Gauss-Legendre integration
 Scattering approximation: constant relaxation-time approximation (CRTA)
 Static self-energy: F
 Transport number of points:   501
 temperature:    0.000 K
   Transport energy range:   [   9.795:   9.795]  wich corresponds to    0.000 eV
   Average relaxation time:           NaN s
   Number of electrons:    0.0000E+00
   Number of holes:        1.1297E-06
 temperature:  100.000 K
   Transport energy range:   [   9.699:   9.907]  wich corresponds to    0.208 eV
   Average relaxation time:    1.0000E-14 s
   Number of electrons:    0.0000E+00
   Number of holes:        1.1296E-06
 temperature:  200.000 K
   Transport energy range:   [   9.619:  10.035]  wich corresponds to    0.416 eV
   Average relaxation time:    1.0000E-14 s
   Number of electrons:    0.0000E+00
   Number of holes:        1.1298E-06

Transport calculator N =  2
----------------------------------
 transport driver: 2 ! Gauss-Legendre integration
 Scattering approximation: self-energy relaxation-time approximation (SERTA)
 Static self-energy: F
 Transport number of points:   501
 temperature:    0.000 K
   Transport energy range:   [   9.795:   9.795]  wich corresponds to    0.000 eV
   Average relaxation time:           NaN s
   Number of electrons:    0.0000E+00
   Number of holes:        1.1297E-06
 temperature:  100.000 K
   Transport energy range:   [   9.699:   9.907]  wich corresponds to    0.208 eV
   Average relaxation time:    2.1451E-13 s
   Number of electrons:    0.0000E+00
   Number of holes:        1.1296E-06
 temperature:  200.000 K
   Transport energy range:   [   9.619:  10.035]  wich corresponds to    0.416 eV
   Average relaxation time:    4.3674E-13 s
   Number of electrons:    0.0000E+00
   Number of holes:        1.1298E-06
```

This is then followed by the output of the transport coefficients for
each accumulator and each temperature. The corresponding example output
looks like this:

``` mw-collapsible
Transport for self-energy accumulator N=     1
                 T K               mu eV           sigma S/m      mob cm^2/(V.s)       seebeck μV/K         peltier μV     kappa_e W/(m.K)
          0.00000000          9.79452083         87.62375412         54.69155048          0.00000000          0.00000000          0.00000000 Gauss-Legendre grids
        100.00000000          9.80301003         87.61741132         54.69107335        228.06848886      22806.84888640          0.00023958 Gauss-Legendre grids
        200.00000000          9.82655169         87.62716236         54.69106480        377.34594846      75469.18969136          0.00050233 Gauss-Legendre grids

Transport for self-energy accumulator N=     2
                 T K               mu eV           sigma S/m      mob cm^2/(V.s)       seebeck μV/K         peltier μV     kappa_e W/(m.K)
          0.00000000          9.79452083        153.09934046         95.55902268          0.00000000          0.00000000          0.00000000 Gauss-Legendre grids
        100.00000000          9.80301003        149.76360902         93.48293224        228.06843439      22806.84343939          0.00040952 Gauss-Legendre grids
        200.00000000          9.82655169        134.56767701         83.98822174        377.34590243      75469.18048584          0.00077142 Gauss-Legendre grids
```

This allows us to identify the first data set (`N = 1`) as the CRTA
calculation and the second data set (`N = 2`) as the SERTA calculation.

### Binary output in the [vaspout.h5](../output-files/Vaspout.h5.md) HDF5 file\[<a
href="/wiki/index.php?title=Electron-phonon_accumulators&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Binary output in the vaspout.h5 HDF5 file">edit</a> \| (./index.php.md)\]

The information in each accumulator is also written to the standard
[vaspout.h5](../output-files/Vaspout.h5.md) binary output file. In this
case, the accumulators are organized as HDF5 groups, with the unique
accumulator ID being part of the group name. This is an example output
showing the electron-phonon section of the HDF5 file:

``` mw-collapsible
$ h5ls vaspout.h5/results/electron_phonon/electrons
chemical_potential       Group
dos                      Group
eigenvalues              Group
self_energy_1            Group
self_energy_2            Group
self_energy_3            Group
self_energy_4            Group
self_energy_5            Group
self_energy_6            Group
self_energy_meta         Group
transport_1              Group
transport_2              Group
transport_3              Group
transport_4              Group
transport_5              Group
transport_6              Group
transport_meta           Group
velocity                 Dataset {3, 1, 29, 8}
```

The `self_energy_N` and `transport_N` HDF5 groups correspond to the
self-energy and transport accumulators with the ID `N`, respectively.
Meta information regarding the accumulators is contained in the
`self_energy_meta` and `transport_meta` subgroups. Each subgroup
currently holds three datasets that describe the labeling of the
accumulators:

`id_name`  
lists the kind of parameters that accumulators can be created for. Each
name refers to one or more [INCAR](../input-files/INCAR.md) tags.

`selfen_delta`  
accumulators created via
[ELPH_SELFEN_DELTA](../incar-tags/ELPH_SELFEN_DELTA.md)

`nbands_sum`  
accumulators created via
[ELPH_NBANDS_SUM](../incar-tags/ELPH_NBANDS_SUM.md)

`selfen_muij`  
accumulators created via
[ELPH_SELFEN_MU](../incar-tags/ELPH_SELFEN_MU.md),
[ELPH_SELFEN_CARRIER_DEN](../incar-tags/ELPH_SELFEN_CARRIER_DEN.md)
or
[ELPH_SELFEN_CARRIER_PER_CELL](../incar-tags/ELPH_SELFEN_CARRIER_PER_CELL.md)

`selfen_approx`  
accumulators created via
[ELPH_SCATTERING_APPROX](../incar-tags/ELPH_SCATTERING_APPROX.md)

<!-- -->

`id_size`  
lists the number of accumulators created for each kind of parameters (in
the same order)

`ncalculators`  
total number of accumulators (product of all `id_size` entries)

So, for example, if the meta-data output looks like this:

``` mw-collapsible
id_name: "selfen_delta   ", "nbands_sum     ", "selfen_muij    ", "selfen_approx  "
id_size: 1, 1, 3, 2
ncalculators: 6
```

that means there is only one $\mathrm{i} \delta$ value from
[ELPH_SELFEN_DELTA](../incar-tags/ELPH_SELFEN_DELTA.md), one
band count from
[ELPH_NBANDS_SUM](../incar-tags/ELPH_NBANDS_SUM.md), three
different chemical potentials from
[ELPH_SELFEN_MU](../incar-tags/ELPH_SELFEN_MU.md) (or related
tags) and two different scattering approximations from
[ELPH_SCATTERING_APPROX](../incar-tags/ELPH_SCATTERING_APPROX.md),
for a total of six accumulators (all combinations).

In addition to the meta-data contained within the `_meta` groups, each
electron-phonon accumulator describes itself. For example, here is the
data contained with the first self-energy accumulator group:

``` mw-collapsible
h5ls vaspout.h5/results/electron_phonon/electrons/self_energy_1
band_start               Dataset {SCALAR}
band_stop                Dataset {SCALAR}
bks_idx                  Dataset {1, 29, 3}
carrier_per_cell         Dataset {6}
delta                    Dataset {SCALAR}
efermi                   Dataset {6}
energies                 Dataset {9, 1}
enwin                    Dataset {SCALAR}
id_idx                   Dataset {4}
id_name                  Dataset {4}
nbands                   Dataset {SCALAR}
nbands_sum               Dataset {SCALAR}
nw                       Dataset {SCALAR}
scattering_approximation Dataset {SCALAR}
select_energy_window     Dataset {2}
selfen_dw                Dataset {9, 6}
selfen_fan               Dataset {9, 1, 6, 2}
static                   Dataset {SCALAR}
temps                    Dataset {6}
tetrahedron              Dataset {SCALAR}
```

The `id_name` is the same as in the meta-data, and the `id_idx` indexes
the `id_size`.

## Related tags and articles\[<a
href="/wiki/index.php?title=Electron-phonon_accumulators&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [Band-structure
  renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md)
- [Transport
  calculations](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md)
- [Electronic transport
  coefficients](../theory/Electronic_transport_coefficients.md)
- [Chemical potential in electron-phonon
  interactions](../theory/Chemical_potential_in_electron-phonon_interactions.md)
- [ELPH_SCATTERING_APPROX](../incar-tags/ELPH_SCATTERING_APPROX.md)
- [ELPH_SELFEN_MU](../incar-tags/ELPH_SELFEN_MU.md)
- [ELPH_SELFEN_MU_RANGE](../incar-tags/ELPH_SELFEN_MU_RANGE.md)
- [ELPH_SELFEN_CARRIER_DEN](../incar-tags/ELPH_SELFEN_CARRIER_DEN.md)
- [ELPH_SELFEN_CARRIER_DEN_RANGE](../incar-tags/ELPH_SELFEN_CARRIER_DEN_RANGE.md)
- [ELPH_SELFEN_CARRIER_PER_CELL](../incar-tags/ELPH_SELFEN_CARRIER_PER_CELL.md)
- [ELPH_MODE](../incar-tags/ELPH_MODE.md)
- [ELPH_RUN](../incar-tags/ELPH_RUN.md)


