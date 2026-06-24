<!-- Source: https://vasp.at/wiki/index.php/Technical_errors | revid: 13316 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Technical errors
Technical errors fall into four categories:

- Errors due to k-point sampling. This will be discussed in [Number of k
  points and method for
  smearing](Number_of_k_points_and_method_for_smearing.md).
  Mind that the errors due to the k-point mesh are not transferable i.e.
  a $9\times 9\times 9$ k-points grid
  leads to a completely different error for fcc, bcc and sc. It is
  therefore absolutely essential to be very careful with respect to the
  k-point sampling.
- Errors due to the cut-off [ENCUT](../incar-tags/ENCUT.md). This error is
  highly transferable, i.e. the default cutoff
  [ENCUT](../incar-tags/ENCUT.md) (read from the
  [POTCAR](../input-files/POTCAR.md) file) is in most cases safe, and one
  can expect that energy differences will be accurate within a few meV
  (see [Energy cut off and FFT
  mesh](../redirects/Energy_cut_off_and_FFT_mesh.md)).
  An exception is the stress tensor which converges notoriously slow
  with respect to the size of the plane wave basis set (see [Energy vs
  volume Volume relaxations and Pulay
  stress](https://vasp.at/wiki/index.php/index.php)")).
- Wrap around errors (see [Wrap-around
  errors](../theory/Wrap-around_errors.md)): These errors
  are due to an insufficient FFT mesh and they are not as well behaved
  as the errors due to the energy cut off (see [Energy cut off and FFT
  mesh](../redirects/Energy_cut_off_and_FFT_mesh.md)).
  But once again, if one uses the default cut off (read from the
  [POTCAR](../input-files/POTCAR.md) file) the wrap around errors are
  usually very small (a few meV per atom) even if the FFT mesh is not
  sufficient. The reason is that the default cut offs in VASP are rather
  large, and therefore the charge density and the potentials contain
  only small components in the region where the wrap around error
  occurs.
- Errors due to the real space projection: Real space projection always
  introduces additional (small) errors. These errors are also quite well
  behaved i.e. if one uses the same real space projection operators all
  the time, the errors are almost constants. Anyway, one should try to
  avoid the evaluation of energy differences between calculations with
  [LREAL](../incar-tags/LREAL.md)=*.FALSE.* and
  [LREAL](../incar-tags/LREAL.md)=*.TRUE.* (see
  [LREAL](../incar-tags/LREAL.md)). Mind that for
  [LREAL](../incar-tags/LREAL.md)=*Auto* (the recommended setting) the real
  space operators are optimized by VASP according to
  [ENCUT](../incar-tags/ENCUT.md) and [PREC](../incar-tags/PREC.md) i.e. one
  gets different real space projection operators if
  [ENCUT](../incar-tags/ENCUT.md) or [PREC](../incar-tags/PREC.md) is changed.

In conclusion, to minimize errors one should use the same setting for
[ENCUT](../incar-tags/ENCUT.md), [ENAUG](../incar-tags/ENAUG.md),
[PREC](../incar-tags/PREC.md), [LREAL](../incar-tags/LREAL.md) and
[ROPT](../incar-tags/ROPT.md) throughout all calculations, and these flags
should be specified explicitly in the [INCAR](../input-files/INCAR.md) file.
In addition it is also preferable to use the same supercell for all
calculations whenever possible.

------------------------------------------------------------------------
