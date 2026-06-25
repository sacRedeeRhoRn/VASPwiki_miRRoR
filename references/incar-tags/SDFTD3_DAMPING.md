<!-- Source: https://vasp.at/wiki/index.php/SDFTD3_DAMPING | revid: 34363 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# SDFTD3_DAMPING


SDFTD3_DAMPING = zero \|
rational \| mzero \| mrational \| optimizedpower 

Description: SDFTD3_DAMPING
sets the type of damping function in the DFT-D3 method implemented in
the [simple-DFT-D3](../methods/Simple-DFT-D3.md) package.

------------------------------------------------------------------------

SDFTD3_DAMPING allows to set
the type of damping function to be used in the DFT-D3 method implemented
in the [simple-DFT-D3](../methods/Simple-DFT-D3.md) package
([IVDW](IVDW.md)=15). The available damping functions are
SDFTD3_DAMPING=zero,[^grimme:jcp:10-1]
rational,[^grimme:jcc:11-2]
mzero,[^smith:jpcl:2016-3]
mrational,[^smith:jpcl:2016-3]
and
optimizedpower.[^witte:jctc:2017-4]

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong>
<ul>
<li>The <span class="mw-selflink selflink">SDFTD3_DAMPING</span> tag is
available from VASP.6.6.0 onwards.</li>
<li>The <span class="mw-selflink selflink">SDFTD3_DAMPING</span> can be
used only for the <a href="/wiki/Simple-DFT-D3"
title="Simple-DFT-D3">simple-DFT-D3</a> package (<a href="/wiki/IVDW"
title="IVDW">IVDW</a>=15).</li>
</ul></td>
</tr>
</tbody>
</table>

## Related tags and articles\[<a
href="/wiki/index.php?title=SDFTD3_DAMPING&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[IVDW](IVDW.md),
[simple-DFT-D3](../methods/Simple-DFT-D3.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-SDFTD3_DAMPING-_incategory-Examples)

## References\[<a
href="/wiki/index.php?title=SDFTD3_DAMPING&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^grimme:jcp:10-1]: [S. Grimme, J. Antony, S. Ehrlich, and S. Krieg, J. Chem. Phys. **132**, 154104 (2010).](https://doi.org/10.1063/1.3382344)
[^grimme:jcc:11-2]: [S. Grimme, S. Ehrlich, and L. Goerigk, J. Comput. Chem. **32**, 1456 (2011).](https://doi.org/10.1002/jcc.21759)
[^smith:jpcl:2016-3]: [D. G. A. Smith, L. A. Burns, K. Patkowski, and C. D. Sherrill, *Revised Damping Parameters for the D3 Dispersion Correction to Density Functional Theory*, J. Phys. Chem. Lett. **7**, 2197 (2016).](http://dx.doi.org/10.1021/acs.jpclett.6b00780)
[^witte:jctc:2017-4]: [J. Witte, N. Mardirossian, J. B. Neaton, and M. Head-Gordon, *Assessing DFT-D3 Damping Functions Across Widely Used Density Functionals: Can We Do Better?*, J. Chem. Theory Comput. **13**, 2043 (2017).](http://dx.doi.org/10.1021/acs.jctc.7b00176)
