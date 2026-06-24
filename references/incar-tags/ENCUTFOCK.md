<!-- Source: https://vasp.at/wiki/index.php/ENCUTFOCK | revid: 21508 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ENCUTFOCK
ENCUTFOCK = \[real\] 

Default: none

Description: The ENCUTFOCK tag sets the energy cutoff that determines
the FFT grids used by the Hartree-Fock routines.

------------------------------------------------------------------------

The flag ENCUTFOCK is no longer supported in VASP.5.2.4 and newer
versions. Please use [PRECFOCK](PRECFOCK.md) instead.

  
The only sensible value for ENCUTFOCK is ENCUTFOCK=0. This implies that
the smallest possible FFT grid, which just encloses the cutoff sphere
corresponding to the plane wave cutoff, is used. This accelerates the
calculations by roughly a factor two to three, but causes slight changes
in the total energies and some noise in the calculated forces. The FFT
grid used internally in the exact exchange (Hartree-Fock) routines is
written to the [OUTCAR](../output-files/OUTCAR.md) file. Simply search for
lines starting with

    FFT grid for exact exchange (Hartree Fock)

  
In many cases, a sensible approach is to determine the electronic and
ionic groundstate using ENCUTFOCK=0, and to make one final total energy
calculation without the flag ENCUTFOCK.

## Related tags and articles
[PRECFOCK](PRECFOCK.md), [PREC](PREC.md),
[ENCUT](ENCUT.md), [List of hybrid
functionals](../methods/List_of_hybrid_functionals.md),
[Hybrid functionals:
formalism](../methods/Hybrid_functionals-_formalism.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ENCUTFOCK-_incategory-Examples)

------------------------------------------------------------------------
