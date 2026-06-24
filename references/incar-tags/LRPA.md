<!-- Source: https://vasp.at/wiki/index.php/LRPA | revid: 25292 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LRPA
LRPA = .TRUE. \| .FALSE.  
Default: **LRPA** = .FALSE. 

Description: LRPA=.TRUE. includes local field effect on the Hartree
level only.

------------------------------------------------------------------------

For LRPA=.TRUE. local field effects are included on the Hartree level
only. This means that cell periodic microscopic changes of the local
potential related to the change of the Hartree potential are included.

For LRPA=.FALSE. changes of the Hartree *and the exchange-correlation
potential* are included. This usually increases the dielectric
constants. The final values for the dielectric tensor can be found in
the [OUTCAR](../output-files/OUTCAR.md) file after the lines.

    MACROSCOPIC STATIC DIELECTRIC TENSOR (including local field effects in RPA (Hartree))

For LRPA=.FALSE. the dielectric tensor is written after the lines:

    MACROSCOPIC STATIC DIELECTRIC TENSOR (including local field effects in DFT)

The dielectric tensor *excluding* local field effects is always
calculated (regardless of LRPA). The piezoelectric tensors and the Born
effective charges as well as the ionic contributions the to dielectric
tensor are only calculated for LRPA=.FALSE..

|  |
|----|
| **Warning:** We recommend using the LRPA tag only in combination with [LEPSILON](LEPSILON.md) or [LCALCEPS](LCALCEPS.md), where the treatment of the terms beyond RPA is unambiguous. In the [MBPT calculations](../redirects/Many-body_perturbation_theory.md) various approximations beyond RPA can be used, hence more precise control of the included terms should be used via the tags [LHARTREE](LHARTREE.md), [LADDER](LADDER.md), and [LFXC](LFXC.md). |

## Related tags and articles
[LEPSILON](LEPSILON.md),
[LCALCEPS](LCALCEPS.md),
[LHARTREE](LHARTREE.md), [LADDER](LADDER.md),
[LFXC](LFXC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LRPA-_incategory-Examples)

------------------------------------------------------------------------
