<!-- Source: https://vasp.at/wiki/index.php/VDW_BETA | revid: 34380 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# VDW_BETA
VDW_BETA = \[real\] 

Description: VDW_BETA sets the offset for the damping radius or the
power for the zero-damping component in the DFT-D3 methods implemented
in the [simple-DFT-D3](../methods/Simple-DFT-D3.md) package.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

VDW_BETA allows to set the value of a parameter in the following
versions of DFT-D3 (only available in the
[simple-DFT-D3](../methods/Simple-DFT-D3.md) package):

- Offset $\beta$ for the damping radius
  in the modified zero-damping function ([IVDW](IVDW.md)=15
  with [SDFTD3_DAMPING](SDFTD3_DAMPING.md)=mzero).
- Power $\beta$ for the zero-damping
  component in the optimized-power damping function
  ([IVDW](IVDW.md)=15 with
  [SDFTD3_DAMPING](SDFTD3_DAMPING.md)=optimizedpower).
  Note that $\beta-6$ corresponds to the
  values of $\beta$ reported in
  Ref.^([\[1\]](#cite_note-witte:jctc:2017-1)).

## Related tags and articles
[IVDW](IVDW.md),
[SDFTD3_DAMPING](SDFTD3_DAMPING.md),
[simple-DFT-D3](../methods/Simple-DFT-D3.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-VDW_BETA-_incategory-Examples)

## References
1.  [↑](#cite_ref-witte:jctc:2017_1-0) [J. Witte, N. Mardirossian, J. B.
    Neaton, and M. Head-Gordon, *Assessing DFT-D3 Damping Functions
    Across Widely Used Density Functionals: Can We Do Better?*, J. Chem.
    Theory Comput. **13**, 2043
    (2017).](http://dx.doi.org/10.1021/acs.jctc.7b00176)

------------------------------------------------------------------------
