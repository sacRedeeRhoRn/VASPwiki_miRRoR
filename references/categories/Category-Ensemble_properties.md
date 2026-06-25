<!-- Source: https://vasp.at/wiki/index.php/Category:Ensemble_properties | revid: 16500 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:Ensemble properties


In a
[molecular-dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
calculation, VASP simulates a specific
[ensemble](Category-Ensembles.md). In principle,
any property of the system can be monitored, and then one can take the
ensemble average of this property. For some observables, VASP provides
convenient tags, articles, and files that help evaluate these so-called
**ensemble properties**.

## Theory\[<a
href="/wiki/index.php?title=Category:Ensemble_properties&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Theory">edit</a> \| (./index.php.md)\]

For any property $\mathcal{A}$
of the system, we can define the observable macroscopic property
$\mathcal{A}_{\mathrm{obs}}$ by taking the ensemble
average:

$\mathcal{A}_{\mathrm{obs}} = \left\langle \mathcal{A}\left(p(t),
q(t)\right)\right\rangle_{\mathrm{time}} = \lim_{t_{\mathrm{obs}} \to
\infty} \frac{1}{t_{\mathrm{obs}}} \int_0^{t_{\mathrm{obs}}} \\
\mathcal{A}\left(p(t), q(t)\right) \\ \mathrm{d}t.$

Here, $t_\mathrm{obs}$ corresponds to the simulation time,
$p(t)$ and $q(t)$ are the
canonical momenta and positions, and an average of
$\mathcal{A}\left(p(t), q(t)\right)$ is taken over time
$t$.

## How to\[<a
href="/wiki/index.php?title=Category:Ensemble_properties&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: How to">edit</a> \| (./index.php.md)\]

## References\[<a
href="/wiki/index.php?title=Category:Ensemble_properties&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


