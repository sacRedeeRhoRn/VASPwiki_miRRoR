<!-- Source: https://vasp.at/wiki/index.php/Blue_moon_ensemble | revid: 36244 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Blue moon ensemble


In general, [constrained molecular
dynamics](../categories/Category-Constrained_molecular_dynamics.md)
generates biased statistical averages. The blue moon ensemble average,
also known as constrained-reaction-coordinate-dynamic (CRCD) ensemble,
connects constrained and unconstrained molecular dynamics, cf. [blue
moon ensemble
calculations](../tutorials/Blue_moon_ensemble_calculations.md).
It shows that the correct average for a quantity
$a(\xi)$ can be obtained using the formula:

$a(\xi)=\frac{\langle |\mathbf{Z}|^{-1/2} a(\xi^\*)
\rangle_{\xi^\*}}{\langle |\mathbf{Z}|^{-1/2}\rangle_{\xi^\*}},$

where ${\xi}$ is the
reaction coordinate, $\xi^\*$
restrains the reference coordinate, e.g. to a transition state, where
the associate velocity is $\dot{\xi^\*} = 0$, the $\langle ... \rangle_{\xi^\*}$ stands for the statistical average of the quantity
enclosed in angle brackets computed for a constrained ensemble, and
$Z$ is a mass metric tensor defined as:

$Z_{\alpha,\beta}={\sum}_{i=1}^{3N} m_i^{-1} \nabla_i \xi_\alpha \cdot
\nabla_i \xi_\beta, \\ \alpha=1,...,r, \\ \beta=1,...,r,$

It can be shown that the free energy gradient can be computed using the
equation:
[^carter:kapral:1989-1][^denotter:briels:2000-2][^darve:pohorille:2010-3][^fleurat:ziegler:2005-4]

$\Bigl(\frac{\partial A}{\partial
\xi_k}\Bigr)_{\xi^\*}=\frac{1}{\langle|Z|^{-1/2}\rangle_{\xi^\*}}\langle
|Z|^{-1/2} \[\lambda_k +\frac{k_B T}{2 |Z|}
\sum_{j=1}^{r}(Z^{-1})_{kj} \sum_{i=1}^{3N} m_i^{-1}\nabla_i \xi_j
\cdot \nabla_i |Z|\]\rangle_{\xi^\*},$

where $A$ is the
free energy, $k_B$ is the
Boltzmann constant, $T$ is the
temperature, and $\lambda_{\xi_k}$ is the Lagrange multiplier associated with the
parameter ${\xi_k}$ used
in the [SHAKE
algorithm](Constrained_molecular_dynamics.md)
[^ryckaertt:jcp:1977-5]

The free-energy difference between states (1) and (2) can be computed by
integrating the free-energy gradients over a connecting path, e.g. using
the Simpson
method[^simpson:web-6]:

${\Delta}A_{1 \rightarrow 2} = \int_{{\xi(1)}}^{{\xi(2)}}\Bigl(
\frac{\partial {A}} {\partial \xi} \Bigr)_{\xi^\*} \cdot d{\xi}.$

Note that as the free energy is a state quantity, the choice of path
connecting (1) with (2) is irrelevant. As an example, when calculating
the transition state, if (1) were set to the reactant and (2) to the
transition state, then ${\Delta}A_{1 \rightarrow 2}$ would be the activation free energy for the reaction.

## Related tags and articles\[<a
href="/wiki/index.php?title=Blue_moon_ensemble&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[ICONST](../input-files/ICONST.md),
[SHAKEMAXITER](../incar-tags/SHAKEMAXITER.md),
[SHAKETOL](../incar-tags/SHAKETOL.md),
[SHAKETOLSOFT](../incar-tags/SHAKETOLSOFT.md),
[LBLUEOUT](../incar-tags/LBLUEOUT.md), [REPORT](../output-files/REPORT.md)

[Blue moon ensemble
calculations](../tutorials/Blue_moon_ensemble_calculations.md)

## References\[<a
href="/wiki/index.php?title=Blue_moon_ensemble&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^carter:kapral:1989-1]: [E. Carter, G. Ciccotti, J. Hynes, R. Kapral, Chem. Phys. Lett., **156**, 472 (1989).](https://doi.org/10.1016/S0009-2614(89)87314-2)
[^denotter:briels:2000-2]: [W. den Otter, W. Briels, Mol. Phys., **98**, 773 (2000).](https://doi.org/10.1080/00268970009483348)
[^darve:pohorille:2010-3]: [E. Darve, M. Wilson, A. Pohorille, Mol. Simul., **28**, 113 (2010).](https://doi.org/10.1080/08927020211975)
[^fleurat:ziegler:2005-4]: [P. Fleurat-Lessard, T. Ziegler, J. Chem. Phys., **123**, 084101 (2005).](https://doi.org/10.1063/1.1948367)
[^ryckaertt:jcp:1977-5]: [J. P. Ryckaert, G. Ciccotti, and H. J. C. Berendsen, J. Comp. Phys. **23**, 327 (1977).](http://dx.doi.org/10.1016/0021-9991(77)90098-5)
[^simpson:web-6]: [Simpson's rule, www.wikipedia.org (2024)](https://en.wikipedia.org/wiki/Simpson%27s_rule)
