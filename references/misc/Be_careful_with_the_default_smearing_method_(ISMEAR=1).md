<!-- Source: https://vasp.at/wiki/index.php/Be_careful_with_the_default_smearing_method_%28ISMEAR%3D1%29 | revid: 11690 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Be careful with the default smearing method (ISMEAR=1)


The default for [ISMEAR](../incar-tags/ISMEAR.md) is 1 in VASP. This
setting is not appropriate for insulators and semiconductors, and can
results in one-electron occupancies that are larger than 1 (2 for non
spinpolarized) systems, and conversely some states being occupied by
less than 1 electron close to the Fermi-level. It is strongly
recommended to set [ISMEAR](../incar-tags/ISMEAR.md)=0 in the INCAR file
and use a small width [SIGMA](../incar-tags/SIGMA.md)=0.05 (do not make
SIGMA too small, values below 0.001 can also lead to undesirable
symmetry breaking).

Read more on this in [Number of k points and method for
smearing](Number_of_k_points_and_method_for_smearing.md)!

  

------------------------------------------------------------------------


