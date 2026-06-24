<!-- Source: https://vasp.at/wiki/index.php/ENMIN | revid: 25193 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ENMIN
ENMIN = \[real\]  
Default: **ENMIN** = value read from [POTCAR](../input-files/POTCAR.md) 

Description: ENMIN describes the minimum viable [plane-wave energy
cutoff](../redirects/Energy_cut_off_and_FFT_mesh.md)
in eV for the pseudopotential it is read from.

------------------------------------------------------------------------

For a multi-element [POTCAR](../input-files/POTCAR.md) file, the maximum
ENMIN determines the absolutely lowest cutoff energy for the plane-wave
basis that should be used. If the deprecated [PREC](PREC.md)
setting *Low* is used, this value is used by default. With all
recommended [PREC](PREC.md) setting VASP will use the largest
*recommended* cutoff energy [ENMAX](../redirects/ENMAX.md) found in the
POTCAR file instead. In all cases, the value can be overwritten by
setting [ENCUT](ENCUT.md) in the [INCAR](../input-files/INCAR.md)
file.

## Related tags and articles
[POTCAR](../input-files/POTCAR.md),
[pseudopotentials](../redirects/Pseudopotentials.md)

------------------------------------------------------------------------
