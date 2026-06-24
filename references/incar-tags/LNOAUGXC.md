<!-- Source: https://vasp.at/wiki/index.php/LNOAUGXC | revid: 29473 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LNOAUGXC
LNOAUGXC = .TRUE. \| .FALSE.  
Default: **LNOAUGXC** = .FALSE. 

Description: LNOAUGXC specifies if a [METAGGA](METAGGA.md)
functional is evaluated with a density that is augmented or not.

------------------------------------------------------------------------

The Kohn-Sham kinetic-energy density

$\tau_{\sigma}=\frac{1}{2}\sum_{i}\nabla\psi_{i\sigma}^{\*}\cdot\nabla\psi_{i\sigma}$

should, in principle, be larger than the von Weizsäcker kinetic-energy
density^([\[1\]](#cite_note-kurth:ijqc:1999-1))

$\tau_{\sigma}^{\textrm{W}}=\frac{\left\vert\nabla
n_{\sigma}\right\vert^{2}}{8 n_{\sigma}}.$

However, this may not always be the case, particularly within the PAW
spheres, when the pseudo density is augmented with the compensation
charge. If LNOAUGXC=.TRUE. is set in the [INCAR](../input-files/INCAR.md)
file, then the pseudo density is not augmented, which should alleviate
the breaking of the condition $\tau_{\sigma}^{\textrm{W}}<\tau_{\sigma}$.

A violation of $\tau_{\sigma}^{\textrm{W}}<\tau_{\sigma}$ can make the
calculations unstable, in particular with the TPSS family of
functionals.

[TABLE]

## Related tags and articles
[METAGGA](METAGGA.md),
[LTBOUNDLIBXC](LTBOUNDLIBXC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LNOAUGXC-_incategory-Examples)

## References
1.  [↑](#cite_ref-kurth:ijqc:1999_1-0) [S. Kurth, J. P. Perdew, and P.
    Blaha, *Molecular and solid-state tests of density functional
    approximations: LSD, GGAs, and meta-GGAs*, Int. J. Quantum Chem.
    **75**, 889
    (1999).](https://doi.org/10.1002/(SICI)1097-461X(1999)75:4/5%3C889::AID-QUA54%3E3.0.CO;2-8)
