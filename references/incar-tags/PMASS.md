<!-- Source: https://vasp.at/wiki/index.php/PMASS | revid: 34227 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PMASS
PMASS = \[Real\]  
Default: **PMASS** = 1000 

Description: PMASS assigns a fictitious mass (in amu) to the lattice
degrees-of-freedom in case of Parrinello-Rahman dynamics (in case VASP
was compiled with
[-Dtbdyn](../misc/Precompiler_options.md)).

------------------------------------------------------------------------

When running *NpT* simulations with a [Langevin
thermostat](MDALGO.md)^([\[1\]](#cite_note-Allen91-1))
([MDALGO](MDALGO.md)=3), using the method of [Parrinello and
Rahman](../misc/NpT_ensemble.md),^([\[2\]](#cite_note-Parrinello80-2)[\[3\]](#cite_note-Parrinello81-3))
a fictitious mass (in amu) for the lattice degrees-of-freedom has to be
assigned using the PMASS tag. The friction coefficient for lattice
degrees-of-freedom have to be specified (in ps⁻¹) by means of the
[LANGEVIN_GAMMA_L](LANGEVIN_GAMMA_L.md) tag.

The friction coefficients γ for the atomic degrees-of-freedom are
specified using the
[LANGEVIN_GAMMA](LANGEVIN_GAMMA.md) tag.

The optimal setting for PMASS depends very much on the particular system
at hand and can be considered as a compromise between two opposing
factors: too large values lead to very slow variation of lattice degrees
of freedom (and hence the sampling becomes inefficient) while too small
value can lead to too large geometric changes in an MD step and hence
may cause numerical problems. We strongly recommend to make careful
tests with various settings before performing the production run.

As demonstrated by Nosé and Klein^([\[4\]](#cite_note-4)), the harmonic
frequency of oscillation of a cubic cell can be expressed as
$\omega_L = \sqrt{\frac{3BL}{W}}$, where
$B$, $L$, and $W$ are bulk modulus,
size of the unit cell, and mass of the lattice degrees-of-freedom,
respectively. Should $\omega_L$ remain
the same upon (say) doubling one of the cell dimensions, the PMASS
should also be doubled.

## Related tags and articles
[LANGEVIN_GAMMA_L](LANGEVIN_GAMMA_L.md),
[LANGEVIN_GAMMA](LANGEVIN_GAMMA.md),
[MDALGO](MDALGO.md)

## References
1.  [↑](#cite_ref-Allen91_1-0) M. P. Allen and D. J. Tildesley,
    *Computer simulation of liquids*, Oxford university press: New York,
    1991.
2.  [↑](#cite_ref-Parrinello80_2-0) [M. Parrinello and A. Rahman, Phys.
    Rev. Lett. 45, 1196
    (1980).](http://dx.doi.org/10.1103/PhysRevLett.45.1196)
3.  [↑](#cite_ref-Parrinello81_3-0) [M. Parrinello and A. Rahman, J.
    Appl. Phys. 52, 7182 (1981).](http://dx.doi.org/10.1063/1.328693)
4.  [↑](#cite_ref-4) [S. Nosé and M. L. Klein, Mol. Phys. 50, 1055
    (1983)](http://dx.doi.org/10.1080/00268978300102851 "doi:10.1080/00268978300102851")

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PMASS-_incategory-Examples)

------------------------------------------------------------------------
