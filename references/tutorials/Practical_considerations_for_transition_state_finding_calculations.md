<!-- Source: https://vasp.at/wiki/index.php/Practical_considerations_for_transition_state_finding_calculations | revid: 28055 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Practical considerations for transition state finding calculations
This page details a few practical considerations for obtaining accurate
and reliable transition state energies using the [Nudged Elastic
Band](Nudged_elastic_bands.md)
(NEB)^([\[1\]](#cite_note-mills:surf-sci:1995-1)[\[2\]](#cite_note-jonsson:book:1998-2))
and [Intrinsic Reaction
Coordinate](../redirects/IRC_calculations.md) (IRC)
^([\[3\]](#cite_note-hratchian:jpc:2002-3)) methods implemented in VASP.
We list a few common issues encountered when running calculations with
the NEB and IRC methods and identify possible solutions.

## Contents

- [1 NEB calculations](#NEB_calculations)
  - [1.1 Restart with a better guess for the initial and final state
    configurations](#Restart_with_a_better_guess_for_the_initial_and_final_state_configurations)
  - [1.2 Band becomes "floppy"](#Band_becomes_%22floppy%22)
  - [1.3 Band does not converge](#Band_does_not_converge)
  - [1.4 Checking convergence](#Checking_convergence)
- [2 IRC calculations](#IRC_calculations)
- [3 Related articles](#Related_articles)
- [4 References](#References)

## NEB calculations
### Restart with a better guess for the initial and final state configurations
[![](https://vasp.at/wiki/images/thumb/a/a3/Example_neb_negative_energies.png/200px-Example_neb_negative_energies.png)](https://vasp.at/wiki/File:Example_neb_negative_energies.png)

An example band which shows intermediate structures with lower energy
than the initial and final configurations.

**Problem**: While performing an NEB calculation, there might be points
on the band which have lower energy than that of the initial and final
state configurations (corresponding to the structures that were placed
in the 00 and 0x, where x is the number of
[IMAGES](../incar-tags/IMAGES.md) plus one). The figure on the right shows
an example where the red (computed) points of the intermediate images
are more stable than the initial and final configurations. The presence
of these intermediate states is not an issue for the NEB methodology.
However, if we are seeking to understand elementary reaction steps of
one reaction event each, then we would like to have a band consisting of
only one maxima and two minima (consisting of the initial and final
states).

**Possible solutions**

- Relax the configurations with lower energy. These structures would
  then correspond to new initial and final configurations. Restart the
  NEB with these new configurations as the endpoints of the band.
- Make sure that the NEB was run with sufficient (and commensurate to
  the initial and final structures) accuracy. An important requirement
  is a small enough [EDIFF](../incar-tags/EDIFF.md), which governs the
  accuracy of the forces used in the NEB method.

### Band becomes "floppy"
**Problem** The band between the [IMAGES](../incar-tags/IMAGES.md) of the
NEB calculation is non-monotonic and appears "floppy". In such a
scenario the interpolated band is likely to oscillate between the
computed points. This problem typically appears when one or more images
are added to an already computed band.

**Possible solutions**

- This problem is likely caused by the value of
  [SPRING](../incar-tags/SPRING.md) being too small.
- Check if [EDIFF](../incar-tags/EDIFF.md) is accurate enough for
  computation of the forces.
- Check the interpolation algorithm that you use to determine the
  interpolated band. A cubic spline might suffice in most cases.

### Band does not converge
**Problem** The calculation does not converge, i.e., the NEB method does
not find a reasonable path between an initial and final state
configuration. Sometimes a completely different path is found than the
desired path.

**Possible solutions**

- Choose a different interpolation strategy to generate your initial
  guessed path
- Try the [Improved dimer
  method](../misc/Improved_Dimer_Method.md) instead
- Check if the numbering of the atoms is the initial and final
  configurations. Different ordering of atoms will lead to an unexpected
  path. Visualizing the initial interpolated path should help with
  diagnosing any issues related to incorrectly ordered atoms.

### Checking convergence
**Problem** Unsure if the highest energy point in the NEB is the first
order saddle point between the initial and final state configurations

**Possible solutions**

- Check if there is exactly one imaginary mode by computing the second
  derivatives of the energy as implemented in
  [IBRION](../incar-tags/IBRION.md).

## IRC calculations
**Problem** Unrealistic structures are generated along the IRC path

**Possible solution**

- Make sure that a very tight force convergence criteria has been used
  to determine the transition state; [EDIFFG](../incar-tags/EDIFFG.md)
  must be at most -0.025.
- Choose a smaller value of [IRC_VNORM0](../incar-tags/IRC_VNORM0.md)
  so that the path conforms with the intrinsic reaction coordinate more
  closely.

## Related articles
[Nudged elastic
bands](Nudged_elastic_bands.md), [IRC
calculations](../redirects/IRC_calculations.md)

## References
1.  [↑](#cite_ref-mills:surf-sci:1995_1-0) [G. Mills, H. Jonsson
    and G. K. Schenter, *Reversible work transition state theory:
    application to dissociative adsorption of hydrogen*, Surf. Sci.,
    **324**, 305 (1995).](http://doi.org/10.1016/0039-6028(94)00731-4)
2.  [↑](#cite_ref-jonsson:book:1998_2-0) [H. Jonsson, G. Mills and K. W.
    Jacobsen, *Nudged Elastic Band Method for Finding Minimum Energy
    Paths of Transitions*, in *Classical and Quantum Dynamics in
    Condensed Phase Simulations*, ed. B. J. Berne, G. Ciccotti and D. F.
    Coker (World Scientific,
    1998).](https://doi.org/10.1142/9789812839664_0016)
3.  [↑](#cite_ref-hratchian:jpc:2002_3-0) [H. P. Hratchian and H. B.
    Schlegel, *Following Reaction Pathways Using a Damped Classical
    Trajectory Algorithm*, J. Phys. Chem. A **106**, 165
    (2002).](https://doi.org/10.1021/jp012125b)
