<!-- Source: https://vasp.at/wiki/index.php/VELOCITY | revid: 32707 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VELOCITY
VELOCITY = \[logical\]  
Default: **VELOCITY** = .false. 

Description: Determines whether the ionic velocities are written to the
[vaspout.h5](../output-files/Vaspout.h5.md) file during an [MD
run](../tutorials/Molecular-dynamics_calculations.md).

|                                                        |
|--------------------------------------------------------|
| **Mind:** This tag is only available as of VASP.6.4.0. |

------------------------------------------------------------------------

You can use
[py4vasp](https://vasp.at/py4vasp/latest/calculation/velocity/) to read
the velocities into a Python dictionary

    from py4vasp import calculation
    calculation.velocity.read()

or to visualize the velocity in the crystal structure

    from py4vasp import calculation
    calculation.velocity.plot()

## Related tags and articles
[Sampling phonon spectra from molecular-dynamics
simulations](../tutorials/Sampling_phonon_spectra_from_molecular-dynamics_simulations.md)

  
[Workflows that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-VELOCITY-_incategory-Howto)
