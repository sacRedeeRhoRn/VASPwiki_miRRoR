<!-- Source: https://vasp.at/wiki/index.php/ANTIRES | revid: 15891 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ANTIRES
ANTIRES = 0 \| 1 \| 2  
Default: **ANTIRES** = 0 

Description: ANTIRES determines whether the Tamm-Dancoff approximation
is used or not.

------------------------------------------------------------------------

- ANTIRES=0 Tamm-Dancoff approximation (TDA)
- ANTIRES=1 yields exact results at ω=0 at roughly the same cost as TDA
- ANTIRES=2 beyond Tamm-Dancoff, coupling between positive and negative
  frequencies

VASP uses the procedures outlined in reference
^([\[1\]](#cite_note-Sander-1)) to include contributions beyond TDA.
Beyond-TDA calculations increase the computational time and memory
requirements by typically a factor of 2.

## Related tags and articles
[BSE calculations](../redirects/BSE_calculations.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-ANTIRES-_incategory-Examples)

## References
1.  [↑](#cite_ref-Sander_1-0) [T. Sander, E. Maggio and G. Kresse, Phys.
    Rev. B 92, 045209
    (2015).](http://journals.aps.org/prb/abstract/10.1103/PhysRevB.92.045209)

------------------------------------------------------------------------
