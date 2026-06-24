<!-- Source: https://vasp.at/wiki/index.php/Interface_pinning | revid: 36240 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Interface pinning
**Interface pinning**^([\[1\]](#cite_note-pedersen:prb:13-1)) is used to
determine the melting point from a
[molecular-dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics)
simulation of the interface between a liquid and a solid phase. The
typical behavior of such a simulation is to freeze or melt, while the
interface is *pinned* with a bias potential. This potential applies an
energy penalty for deviations from the desired two-phase system. It is
preferred simulating above the melting point because the bias potential
prevents melting better than freezing.

The Steinhardt-Nelson^([\[2\]](#cite_note-steinhardt:prb:83-2)) order
parameter $Q_6$ discriminates between
the solid and the liquid phase. With the bias potential

$U_\text{bias}(\mathbf{R}) = \frac\kappa2
\left(Q_6(\mathbf{R}) - A\right)^2$

penalizes differences between the order parameter for the current
configuration $Q_6({\mathbf{R}})$ and
the one for the desired interface $A$.
$\kappa$ is an adjustable parameter
determining the strength of the pinning.

Under the action of the bias potential, the system equilibrates to the
desired two-phase configuration. An important observable is the
difference between the average order parameter $\langle Q_6\rangle$ in equilibrium and the desired order
parameter $A$. This difference relates
to the the chemical potentials of the solid $\mu_\text{solid}$ and the liquid $\mu_\text{liquid}$ phase

$N(\mu_\text{solid} - \mu_\text{liquid}) =
\kappa (Q_{6,\text{solid}} - Q_{6,\text{liquid}})(\langle Q_6
\rangle - A)$

where $N$ is the number of atoms in the
simulation.

Computing the forces requires a differentiable $Q_6(\mathbf{R})$. In the VASP implementation a smooth fading
function $w(r)$ is used to weight each
pair of atoms at distance $r$ for the
calculation of the $Q_6(\mathbf{R},w)$
order parameter. This fading function is given as

$w(r) = \left\\ \begin{array}{cl} 1 &\textrm{for}
\\\\ r\leq n \\ \frac{(f^2 - r^2)^2 (f^2 - 3n^2 + 2r^2)}{(f^2 - n^2)^3}
&\textrm{for} \\\\ n<r<f \\ 0 &\textrm{for} \\\\f\leq r
\end{array}\right.$

  
Here $n$ and $f$ are the near- and far-fading distances, respectively. The
radial distribution function $g(r)$ of
the crystal phase yields a good choice for the fading range. To prevent
spurious stress, $g(r)$ should be small
where the derivative of $w(r)$ is large.
Set the near fading distance $n$ to the
distance where $g(r)$ goes below 1 after
the first peak. Set the far fading distance $f$ to the distance where $g(r)$
goes above 1 again before the second peak.

## Related tags and articles
[ICONST](../input-files/ICONST.md),
[OFIELD_Q6_NEAR](../incar-tags/OFIELD_Q6_NEAR.md),
[OFIELD_Q6_FAR](../incar-tags/OFIELD_Q6_FAR.md),
[OFIELD_KAPPA](../incar-tags/OFIELD_KAPPA.md),
[OFIELD_A](../incar-tags/OFIELD_A.md), [REPORT](../output-files/REPORT.md)

[Interface pinning
calculations](../tutorials/Interface_pinning_calculations.md)

## References
1.  [↑](#cite_ref-pedersen:prb:13_1-0) [U. R. Pedersen, F. Hummel, G.
    Kresse, G. Kahl, and C. Dellago, Phys. Rev. B **88**, 094101
    (2013).](https://doi.org/10.1103/PhysRevB.88.094101)
2.  [↑](#cite_ref-steinhardt:prb:83_2-0) [P. J. Steinhardt, D. R.
    Nelson, and M. Ronchetti, Phys. Rev. B **28**, 784
    (1983).](https://doi.org/10.1103/PhysRevB.28.784)

  

------------------------------------------------------------------------
