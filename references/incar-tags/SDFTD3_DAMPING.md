<!-- Source: https://vasp.at/wiki/index.php/SDFTD3_DAMPING | revid: 34363 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SDFTD3_DAMPING
SDFTD3_DAMPING = zero \| rational \| mzero \| mrational \|
optimizedpower 

Description: SDFTD3_DAMPING sets the type of damping function in the
DFT-D3 method implemented in the
[simple-DFT-D3](../methods/Simple-DFT-D3.md) package.

------------------------------------------------------------------------

SDFTD3_DAMPING allows to set the type of damping function to be used in
the DFT-D3 method implemented in the
[simple-DFT-D3](../methods/Simple-DFT-D3.md) package
([IVDW](IVDW.md)=15). The available damping functions are
SDFTD3_DAMPING=zero,^([\[1\]](#cite_note-grimme:jcp:10-1))
rational,^([\[2\]](#cite_note-grimme:jcc:11-2))
mzero,^([\[3\]](#cite_note-smith:jpcl:2016-3))
mrational,^([\[3\]](#cite_note-smith:jpcl:2016-3)) and
optimizedpower.^([\[4\]](#cite_note-witte:jctc:2017-4))

[TABLE]

## Related tags and articles
[IVDW](IVDW.md),
[simple-DFT-D3](../methods/Simple-DFT-D3.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-SDFTD3_DAMPING-_incategory-Examples)

## References
1.  [↑](#cite_ref-grimme:jcp:10_1-0) [S. Grimme, J. Antony, S. Ehrlich,
    and S. Krieg, J. Chem. Phys. **132**, 154104
    (2010).](https://doi.org/10.1063/1.3382344)
2.  [↑](#cite_ref-grimme:jcc:11_2-0) [S. Grimme, S. Ehrlich, and L.
    Goerigk, J. Comput. Chem. **32**, 1456
    (2011).](https://doi.org/10.1002/jcc.21759)
3.  ↑ ^([a](#cite_ref-smith:jpcl:2016_3-0))
    ^([b](#cite_ref-smith:jpcl:2016_3-1)) [D. G. A. Smith, L. A.
    Burns, K. Patkowski, and C. D. Sherrill, *Revised Damping Parameters
    for the D3 Dispersion Correction to Density Functional Theory*, J.
    Phys. Chem. Lett. **7**, 2197
    (2016).](http://dx.doi.org/10.1021/acs.jpclett.6b00780)
4.  [↑](#cite_ref-witte:jctc:2017_4-0) [J. Witte, N. Mardirossian, J. B.
    Neaton, and M. Head-Gordon, *Assessing DFT-D3 Damping Functions
    Across Widely Used Density Functionals: Can We Do Better?*, J. Chem.
    Theory Comput. **13**, 2043
    (2017).](http://dx.doi.org/10.1021/acs.jctc.7b00176)

------------------------------------------------------------------------
