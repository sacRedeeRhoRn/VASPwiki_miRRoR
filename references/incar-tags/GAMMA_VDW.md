<!-- Source: https://vasp.at/wiki/index.php/GAMMA_VDW | revid: 24423 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# GAMMA_VDW
GAMMA_VDW = \[real\] 

|                        |        |                                             |
|------------------------|--------|---------------------------------------------|
| Default: **GAMMA_VDW** | = 1.12 | for [IVDW_NL](IVDW_NL.md)=3 or |
|                        | = 1.29 | for [IVDW_NL](IVDW_NL.md)=4    |

Description: Specify $\gamma$ in
vdW-DF3-opt1/vdW-DF3-opt2.

------------------------------------------------------------------------

The GAMMA_VDW tag allows to specify the value of the parameter
$\gamma$ in the kernel of the
vdW-DF3-opt1/vdW-DF3-opt2 nonlocal van der Waals
functionals.^([\[1\]](#cite_note-chakraborty:jctc:2020-1))

## Related tags and articles
[ALPHA_VDW](ALPHA_VDW.md),
[PARAM1](PARAM1.md), [PARAM2](PARAM2.md),
[Nonlocal vdW-DF
functionals](../methods/Nonlocal_vdW-DF_functionals.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-GAMMA_VDW-_incategory-Examples)

## References
1.  [↑](#cite_ref-chakraborty:jctc:2020_1-0) [D. Chakraborty, K.
    Berland, and T. Thonhauser, *Next-Generation Nonlocal van der Waals
    Density Functional*, J. Chem. Theory Comput. **16**, 5893
    (2020).](https://doi.org/10.1021/acs.jctc.0c00471)
