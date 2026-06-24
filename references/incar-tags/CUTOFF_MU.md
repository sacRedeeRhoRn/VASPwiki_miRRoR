<!-- Source: https://vasp.at/wiki/index.php/CUTOFF_MU | revid: 32845 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# CUTOFF_MU
CUTOFF_MU = \[real\] ( \[real\] ) 

|  |  |  |
|----|----|----|
| Default: **CUTOFF_MU** | = 0.8 \* Fermi level of a system with [NUM_WANN](NUM_WANN.md) orbitals occupied |  |

Description: CUTOFF_MU specifies the energy cutoff
$\mu$ in eV for the function specified
by CUTOFF_MU.

------------------------------------------------------------------------

The value $\mu$ of CUTOFF_MU corresponds
to the energy cutoff of the cutoff function used to obtain Wannier
functions with the [one-shot
method](https://vasp.at/wiki/index.php/Wannier_functions) "Wannier functions").
The meaning of $\mu$ depends on the
[CUTOFF_TYPE](CUTOFF_TYPE.md) tag.

For spin-polarized calculations ([`ISPIN`](ISPIN.md)` = 2`),
two values can be specified for CUTOFF_MU, one for each spin channel. If
only a single value is specified, it will be used for both spin
channels.

The default value is computed by first determining the Fermi level of
the system if it had [NUM_WANN](NUM_WANN.md) orbitals
occupied and multiplying by 0.8. This gives reasonable freedom to
determine the unitary transformation $U_{mn\mathbf{k}}$ from Bloch states to Wannier functions.

|  |
|----|
| **Tip:** Careful tuning of this parameter is required to obtain a good Wannierization. |

## Related tags and articles
[CUTOFF_TYPE](CUTOFF_TYPE.md),
[CUTOFF_SIGMA](CUTOFF_SIGMA.md),
[LSCDM](LSCDM.md), [LOCPROJ](LOCPROJ.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-CUTOFF_MU-_incategory-Examples)
