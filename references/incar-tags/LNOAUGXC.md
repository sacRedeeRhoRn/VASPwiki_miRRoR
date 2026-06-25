<!-- Source: https://vasp.at/wiki/index.php/LNOAUGXC | revid: 29473 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LNOAUGXC


LNOAUGXC = .TRUE. \| .FALSE.  
Default: **LNOAUGXC** = .FALSE. 

Description: LNOAUGXC
specifies if a [METAGGA](METAGGA.md) functional is
evaluated with a density that is augmented or not.

------------------------------------------------------------------------

The Kohn-Sham kinetic-energy density

$\tau_{\sigma}=\frac{1}{2}\sum_{i}\nabla\psi_{i\sigma}^{\*}\cdot\nabla\psi_{i\sigma}$

should, in principle, be larger than the von Weizsäcker kinetic-energy
density[^kurth:ijqc:1999-1]

$\tau_{\sigma}^{\textrm{W}}=\frac{\left\vert\nabla
n_{\sigma}\right\vert^{2}}{8 n_{\sigma}}.$

However, this may not always be the case, particularly within the PAW
spheres, when the pseudo density is augmented with the compensation
charge. If LNOAUGXC=.TRUE. is
set in the [INCAR](../input-files/INCAR.md) file, then the pseudo density is
not augmented, which should alleviate the breaking of the condition
$\tau_{\sigma}^{\textrm{W}}<\tau_{\sigma}$.

A violation of $\tau_{\sigma}^{\textrm{W}}<\tau_{\sigma}$ can make
the calculations unstable, in particular with the TPSS family of
functionals.

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>This tag is available since VASP.6.5.0 and is a replacement of the
compiler option <a href="/wiki/Precompiler_options#-DnoAugXCmeta"
title="Precompiler options">-DnoAugXCmeta</a> that was available until
VASP.6.4.3.</li>
<li>This option may negatively affect the results, therefore it should
be used only for functionals, e.g., TPSS, for which the breaking of the
condition <span class="smj-container"
style="opacity:.5">$\tau_{\sigma}^{\textrm{W}}&lt;\tau_{\sigma}$</span> may lead to
numerical problems.</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a href="/wiki/index.php?title=LNOAUGXC&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[METAGGA](METAGGA.md),
[LTBOUNDLIBXC](LTBOUNDLIBXC.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LNOAUGXC-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=LNOAUGXC&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^kurth:ijqc:1999-1]: [S. Kurth, J. P. Perdew, and P. Blaha, *Molecular and solid-state tests of density functional approximations: LSD, GGAs, and meta-GGAs*, Int. J. Quantum Chem. **75**, 889 (1999).](https://doi.org/10.1002/(SICI)1097-461X(1999)75:4/5%3C889::AID-QUA54%3E3.0.CO;2-8)
