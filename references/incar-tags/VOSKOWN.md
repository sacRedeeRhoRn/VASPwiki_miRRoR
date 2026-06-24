<!-- Source: https://vasp.at/wiki/index.php/VOSKOWN | revid: 17005 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VOSKOWN
VOSKOWN = 0 \| 1  
Default: **VOSKOWN** = 0 

Description: Determines whether Vosko-Wilk-Nusair interpolation is used
or not.

------------------------------------------------------------------------

This flag is not relevant for most "modern" gradient corrected
functionals, such as PBE or PBEsol.

For the LDA and some "older" gradient corrected functionals such as
PW91, VASP interpolates the correlation energy from the
non-spinpolarized to the fully spinpolarized case in the same way as the
exchange energy (Barth-Hedin spin
interpolation^([\[1\]](#cite_note-barth:jpc:1972-1)). If VOSKOWN is set
to 1, the interpolation formula according to Vosko, Wilk and
Nusair^([\[2\]](#cite_note-vosko1980-2)) is used (this interpolation is
based on the RPA correlation energy of partially spin polarized
systems). The Vosko, Wilk and Nusair interpolation usually enhances the
magnetic moments and the magnetic energies. Because the
Vosko-Wilk-Nusair interpolation is the interpolation usually applied in
the context of gradient corrected functionals, it is desirable to use
this interpolation whenever the PW91 functional is applied. Setting this
tag is not required for most modern functions, such as the PBE or PBEsol
functional, since these functional strictly follow the original
publications and disregard the setting of this flag entirely (this
implicitly implies that the correlation energy is interpolated according
to Vosko, Wilk and Nusair).

## References
1.  [↑](#cite_ref-barth:jpc:1972_1-0) [U. V. Barth and L. Hedin, J.
    Phys. C **5**, 1629
    (1972).](https://doi.org/10.1088/0022-3719/5/13/012)
2.  [↑](#cite_ref-vosko1980_2-0) [S. H. Vosko, L. Wilk, and M. Nusair,
    Can. J. Phys. **58**, 1200 (1980).](https://doi.org/10.1139/p80-159)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-VOSKOWN-_incategory-Examples)

------------------------------------------------------------------------
