<!-- Source: https://vasp.at/wiki/index.php/NUPDOWN | revid: 33286 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NUPDOWN
NUPDOWN = \[positive real\]  
Default: **NUPDOWN** = not set 

Description: Sets the difference between the number of electrons in the
up and down spin components.

------------------------------------------------------------------------

  
Allows calculations for a specific spin multiplet, i.e. the difference
of the number of electrons in the up and down spin component will be
kept fixed to the specified value.

|  |
|----|
| **Important:** If NUPDOWN is set in the [INCAR](../input-files/INCAR.md) file the initial moment for the charge density should be the same. Otherwise convergence can slow down. When starting from atomic charge densities ([ICHARG](ICHARG.md)=2), VASP will try to do this automatically by setting [MAGMOM](MAGMOM.md) to NUPDOWN/**NIONS** (NIONS - total number of ions). The user can of course overwrite this default by specifying a different [MAGMOM](MAGMOM.md) (which should still result in the correct total moment). If one initializes the charge density from the one-electron wavefunctions, the initial moment is always correct, because VASP "pushes" the required number of electrons from the down to the up component. Initializing the charge density from the [CHGCAR](../input-files/CHGCAR.md) file ([ICHARG](ICHARG.md)=1), however, the initial moment is usually incorrect! |

If no value is set (or NUPDOWN=-1) a full relaxation will be performed.
This is also the default.

## Related tags and articles
[MAGMOM](MAGMOM.md),[ICHARG](ICHARG.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-NUPDOWN-_incategory-Examples)

------------------------------------------------------------------------
