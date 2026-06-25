<!-- Source: https://vasp.at/wiki/index.php/Metadynamics | revid: 36183 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Metadynamics


In
metadynamics,[^laio:pnas:02-1][^iannuzzi:prl:03-2]
the bias potential that acts on a selected number of geometric
parameters (collective variables) ξ={ξ<sub>1</sub>, ξ<sub>2</sub>,
...,ξ<sub>*m*</sub>} is constructed on-the-fly during the simulation.
The Hamiltonian for the metadynamics $\tilde{H}(q,p)$ can be written as:

$\tilde{H}(q,p,t) = H(q,p) + \tilde{V}(t,\xi),$

where $H(q,p)$ is
the Hamiltonian for the original (unbiased) system, and
$\tilde{V}(t,\xi)$ is the time-dependent bias potential.
The latter term is usually defined as a sum of Gaussian hills with
height *h* and width *w*:

$\tilde{V}(t,\xi) = h \sum_{i=1}^{\lfloor t/t_G \rfloor} \exp{\left\\
-\frac{|\xi^{(t)}-\xi^{(i \cdot t_G)}|^2}{2 w^2} \right\}.$

In practice, $\tilde{V}(t,\xi)$ is updated by adding a new Gaussian with a time
increment *t*<sub>G</sub>, which is typically one or two orders of
magnitude greater than the time step used in the MD simulation.

In the limit of infinite simulation time, the bias potential is related
to the free energy via:

$A(\xi) = - \lim_{t \to \infty} \tilde{V}(t,\xi) + const.$

Practical hints as how to adjust the parameters used in metadynamics
(*h*, *w*, *t*<sub>G</sub>) are given in
Refs.[^ensing:jpc:05-3]
and
[^laio:jpc:05-4].

The error estimation in free-energy calculations with metadynamics is
discussed in
Ref.[^laio:jpc:05-4].

## Related tags and sections\[<a
href="/wiki/index.php?title=Metadynamics&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[ICONST](../input-files/ICONST.md), [HILLS_H](../incar-tags/HILLS_H.md),
[HILLS_W](../incar-tags/HILLS_W.md),
[HILLS_BIN](../incar-tags/HILLS_BIN.md),
[PENALTYPOT](../input-files/PENALTYPOT.md),
[HILLSPOT](../incar-tags/HILLSPOT.md), [REPORT](../output-files/REPORT.md)

[Metadynamics
calculations](../tutorials/Metadynamics_calculations.md)

## References\[<a
href="/wiki/index.php?title=Metadynamics&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
------------------------------------------------------------------------

[^laio:pnas:02-1]: [R. A. Laio and M. Parrinello, Proc. Natl. Acad, Sci. USA **99**, 12562 (2002).](https://doi.org/10.1073/pnas.202427399)
[^iannuzzi:prl:03-2]: [M. Iannuzzi, A. Laio, and M. Parrinello, Phys. Rev. Lett. **90**, 238302 (2003).](https://doi.org/10.1103/PhysRevLett.90.238302)
[^ensing:jpc:05-3]: [B. Ensing, A. Laio, M. Parrinello, and M. L. Klein, J. Phys. Chem. B **109**, 6676 (2005).](https://doi.org/10.1021/jp045571i)
[^laio:jpc:05-4]: [A. Laio, A. Rodriguez-Fortea, F. L. Gervasio, M. Ceccarelli, and M. Parrinello, J. Phys. Chem. B **109**, 6714 (2005).](https://doi.org/10.1021/jp045424k)
