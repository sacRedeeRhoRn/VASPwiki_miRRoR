<!-- Source: https://vasp.at/wiki/index.php/LANGEVIN_GAMMA_L | revid: 36572 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LANGEVIN_GAMMA_L
LANGEVIN_GAMMA_L = \[Real\]  
Default: **LANGEVIN_GAMMA_L** = 0 

Description: LANGEVIN_GAMMA_L specifies the friction coefficient (in
ps⁻¹) for lattice degrees-of-freedom in case of Parrinello-Rahman
dynamics (in case VASP was compiled with
[-Dtbdyn](../redirects/Precompiler_flags.md)).

------------------------------------------------------------------------

When running *NpT* simulations with a [Langevin
thermostat](MDALGO.md)^([\[1\]](#cite_note-allen:book:1991-1))
([MDALGO](MDALGO.md)=3), using the method of [Parrinello and
Rahman](MDALGO.md)^([\[2\]](#cite_note-parrinello:prl:1980-2)[\[3\]](#cite_note-parrinello:jap:1981-3)),
the friction coefficient for lattice degrees-of-freedom have to be
specified (in ps⁻¹) by means of the LANGEVIN_GAMMA_L-tag. A fictitious
mass for the lattice degrees-of-freedom has to be assigned using the
[PMASS](PMASS.md) tag.

The friction coefficients γ for the atomic degrees-of-freedom are
specified using the
[LANGEVIN_GAMMA](LANGEVIN_GAMMA.md)-tag.

## Related tags and articles
[LANGEVIN_GAMMA](LANGEVIN_GAMMA.md),
[PMASS](PMASS.md), [MDALGO](MDALGO.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LANGEVIN_GAMMA_L-_incategory-Examples)

## References
------------------------------------------------------------------------

1.  [↑](#cite_ref-allen:book:1991_1-0) [M. P. Allen and D. J. Tildesley,
    *Computer simulation of liquids* (Oxford university press: New York,
    1991).](https://books.google.co.jp/books?id=WFExDwAAQBAJ&lpg=PP1&hl=ja&pg=PP1#v=onepage&q&f=false)
2.  [↑](#cite_ref-parrinello:prl:1980_2-0) [M. Parrinello and A. Rahman,
    Phys. Rev. Lett. **45**, 1196
    (1980).](https://doi.org/10.1103/PhysRevLett.45.1196)
3.  [↑](#cite_ref-parrinello:jap:1981_3-0) [M. Parrinello and A.
    Rahman, J. Appl. Phys. **52**, 7182
    (1981).](https://doi.org/10.1063/1.328693)
