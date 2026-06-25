<!-- Source: https://vasp.at/wiki/index.php/CH_LSPEC | revid: 28405 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CH_LSPEC


CH_LSPEC = \[logical\]  
Default: **CH_LSPEC** = .FALSE. 

Description: This flag controls whether the dielecectric function using
the supercell core-hole method is calculated or not.

------------------------------------------------------------------------

How to calculate X-ray absorption spectra from the supercell core-hole
method are is explained
[here](../tutorials/Supercell_core-hole_calculations.md).

This tag should be used in combination with the following important tags
for the core-hole approximation:

- [ICORELEVEL](ICORELEVEL.md): To enable core-hole
  calculations in the final-state approximation with self-consistent
  field cycles (SCF) one has to set
  [ICORELEVEL](ICORELEVEL.md)=2. Core-hole calculations
  in the initial-state approximation
  ([ICORELEVEL](ICORELEVEL.md)=1) are also available,
  but they are physically less relevant and should be only used if
  especially needed.
- [CLNT](CLNT.md): This tag selects the species holding the
  core hole. This number corresponds to the species defined in the
  [POSCAR](../input-files/POSCAR.md) and [POTCAR](../input-files/POTCAR.md)
  files.
- [CLN](CLN.md): Specifies the $n$ quantum
  number of the excited electron.
- [CLL](CLL.md): Specifies the $l$ quantum
  number of the excited electron.
- [CLZ](CLZ.md): Specifies how much of a faction of the chosen
  electron should be excited. Usually one always sets
  [CLZ](CLZ.md)=1.0, but in some cases values lesser than 1 can
  lead to better agreement with experiment. However, this should be
  handled with caution since the physics behind is very dubious.

And following tags to control the calculation of the dieletric function:

- [CH_SIGMA](CH_SIGMA.md): The broadening of the spectrum
  is by default of Gaussian form and the broadening width in eV is set
  by [CH_SIGMA](CH_SIGMA.md). We recommend using a very
  small broadening
  [CH_SIGMA](CH_SIGMA.md)$\le$0.001
  in the calculations and to broaden the spectrum in post-processing.
  Also, the spectrum can be recalculated with different parameters
  without the need to redo the electronic self-consistent field cycle.
  For that one can use the converged [WAVECAR](../input-files/WAVECAR.md)
  from the previous calculation and set [ALGO](ALGO.md)=*None*
  together with the new parameters for the spectrum "CH\_\*" in the
  [INCAR](../input-files/INCAR.md) file.
- [CH_NEDOS](CH_NEDOS.md): Sets the number of grid points
  on the energy axis of the spectrum.
- [CH_AMPLIFICATION](CH_AMPLIFICATION.md): Scaling
  of the spectrum by the specified value. This tag is not important but
  can be useful sometimes if one needs to scale the spectrum a priori.
  Otherwise, it is recommended to scale the spectrum a posteriori.

  

|  |
|----|
| **Warning:** For XAS calculations it is strongly recommended to use the available GW PAW potentials for the [POTCAR](../input-files/POTCAR.md) files, since many standard potentials don't have projectors with quantum numbers 2 or larger and the GW potentials are more exact for excited states than the standard potentials. |

## Related tags and articles\[<a href="/wiki/index.php?title=CH_LSPEC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[CH_SIGMA](CH_SIGMA.md),
[CH_NEDOS](CH_NEDOS.md),
[CH_AMPLIFICATION](CH_AMPLIFICATION.md),
[ICORELEVEL](ICORELEVEL.md), [CLNT](CLNT.md),
[CLN](CLN.md), [CLL](CLL.md), [CLZ](CLZ.md),
[ISMEAR](ISMEAR.md),
[CH_AMPLIFICATION](CH_AMPLIFICATION.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-CH_LSPEC-_incategory-Examples)

------------------------------------------------------------------------


