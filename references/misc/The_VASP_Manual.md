<!-- Source: https://vasp.at/wiki/index.php/The_VASP_Manual | revid: 36559 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# The VASP Manual
|  |  |  |
|----|----|----|
| [Take a tour](Welcome.md) | [Install VASP](Installing_VASP.6.X.X.md) | [Get a license](https://www.vasp.at/sign_in/registration_form/) |
| [Release notes](Changelog.md) | [VASP website and news](https://www.vasp.at) | [Forum](https://www.vasp.at/forum/) |
| [Learn](https://www.vasp.at/learn/), [examples](../categories/Category-Examples.md), [Wiki tutorials](../categories/Category-Tutorials.md) | [py4vasp](https://vasp.at/py4vasp/latest/index.html) | [Portal](https://www.vasp.at/sign_in/portal) |
| [Known issues](Known_issues.md) | [Tutorials](https://www.vasp.at/tutorials/latest/) | [Lectures](https://www.youtube.com/channel/UCBATkNZ7pkAXU9tx7GVhlaw) |

## Featured topics
|  |  |
|----|----|
| **Category** | *subtopics (amongst others)* |
| [Theoretical background](../categories/Category-Theory.md) | We collect **theory pages** from all the different areas VASP offers functionalities. These can also be found in the corresponding category of the topic. For instance, the article on the [Blocked-Davidson algorithm](../theory/Blocked-Davidson_algorithm.md) is also linked from the [electronic minimization](../redirects/Electronic_minimization.md) page. |
| [Calculation setup](../categories/Category-Calculation_setup.md) | The **computational setup** considers the [installation](../redirects/Installation.md), the input and output [files](../redirects/Files.md), [performance](../redirects/Performance.md), etc. To learn how to set up your calculation, it is probably best to look for a [how-to page](../categories/Category-Howto.md), e.g., [setting up an electronic minimization](../tutorials/Setting_up_an_electronic_minimization.md), [band-structure calculation using DFT](../redirects/Band-structure_calculation_using_DFT.md), [constructing Wannier orbitals](../tutorials/Constructing_Wannier_orbitals.md), [structure optimization](../tutorials/Structure_optimization.md), etc. |
| [Electronic minimization](../categories/Category-Electronic_minimization.md) | **Electronic minimization** is the central task in many calculations. Here, you find pages describing the [self-consistency cycle](../theory/Self-consistency_cycle.md), different algorithms, e.g., [blocked-Davidson algorithm](../theory/Blocked-Davidson_algorithm.md), [RMM-DIIS](../theory/RMM-DIIS.md), [direct optimization of the orbitals](../theory/Direct_optimization_of_the_orbitals.md), and related topics like [preconditioning](../theory/Preconditioning.md), [density mixing](../redirects/Density_mixing.md), etc. |
| [Electronic ground-state properties](../categories/Category-Electronic_ground-state_properties.md) | [Band structure](../categories/Category-Band_structure.md), [density of states](../categories/Category-Density_of_states.md), partial DOS and on-site charge and magnetization ([LORBIT](../incar-tags/LORBIT.md)), [electrostatics](../categories/Category-Electrostatics.md), [charge density](../categories/Category-Charge_density.md), [potential](../categories/Category-Potential.md), etc. |
| [Spin degree of freedom](../categories/Category-Magnetism.md) | [Spin-orbit coupling](../redirects/Spin-orbit_coupling.md), noncollinear magnetism, spin spirals, constrained magnetism, etc. |
| [Exchange-correlation functionals](../categories/Category-Exchange-correlation_functionals.md) | [LDA](../categories/Category-Exchange-correlation_functionals.md), [GGA](../categories/Category-Exchange-correlation_functionals.md), [meta-GGA](../categories/Category-Exchange-correlation_functionals.md), [DFT+U](../methods/Category-DFT+U.md), [hybrid functionals](../methods/Category-Hybrid_functionals.md), [van der Waals functionals](../methods/Category-Van_der_Waals_functionals.md). |
| [Symmetry and structure](../categories/Category-Symmetry.md) | Crystal symmetry, [reciprocal space](../categories/Category-Crystal_momentum.md), [surfaces](../categories/Category-2D_materials.md), pair-correlation function for liquids, etc. |
| [Ionic minimization](../categories/Category-Ionic_minimization.md) | [Structure optimization](../tutorials/Structure_optimization.md), ionic-minimization methods, [forces](../methods/Category-Forces.md), [transition states](../categories/Category-Transition_States.md), etc. |
| [Molecular dynamics](https://vasp.at/wiki/index.php/Category:Molecular_dynamics) | Barostats, [thermostats](../categories/Category-Thermostats.md), [ensembles](../categories/Category-Ensembles.md), etc. |
| [Ensemble properties](../categories/Category-Ensemble_properties.md) | Monitoring geometric parameters, pair-correlation function, thermal conductivity, diffusion, etc. |
| [Advanced molecular-dynamics sampling](../categories/Category-Advanced_molecular-dynamics_sampling.md) | [Interface pinning](../theory/Interface_pinning.md), [constrained molecular dynamics](../theory/Constrained_molecular_dynamics.md), [metadynamics](../theory/Metadynamics.md), [thermodynamic integration](../theory/Thermodynamic_integration.md), etc. |
| [Machine-learned force fields](../categories/Category-Machine-learned_force_fields.md) | Training and application of force fields. |
| [Phonons](../categories/Category-Phonons.md) | Lattice vibrations, [finite differences](../tutorials/Phonons_from_finite_differences.md), [phonon dispersion relation](../tutorials/Computing_the_phonon_dispersion_and_DOS.md). |
| [Electron-phonon interactions](../categories/Category-Electron-phonon_interactions.md) | [Band-structure renormalization](../tutorials/Bandgap_renormalization_due_to_electron-phonon_coupling.md), [transport](../tutorials/Transport_coefficients_including_electron-phonon_scattering.md), [stochastic sampling](../tutorials/Electron-phonon_interactions_from_Monte-Carlo_sampling.md). |
| [Response theory](../categories/Category-Linear_response.md) | Static and frequency-dependent [dielectric properties](../categories/Category-Dielectric_properties.md), Berry phases, spectroscopy (UV, VIS, [X-ray](../categories/Category-XAS.md), [NMR](../categories/Category-NMR.md)), [phonons](../categories/Category-Phonons.md), etc. |
| [Many-body perturbation theory](../categories/Category-Many-body_perturbation_theory.md) | ACFDT, BSE, GW, MP2, cRPA. |
| [Localized basis and projection](../categories/Category-Wannier_functions.md) | Obtaining [Wannier functions](https://vasp.at/wiki/index.php/Wannier_functions), SCDM, partial DOS and on-site charge and magnetization ([LORBIT](../incar-tags/LORBIT.md)), [Constrained-random-phase approximation](../redirects/Constrained-random-phase_approximation.md) |
| [Performance](../categories/Category-Performance.md) | [Parallelization](../categories/Category-Parallelization.md), [memory management](../categories/Category-Memory.md), profiling, etc. |

## Support
If you have questions or run into trouble, please have a look at the
[known issues](Known_issues.md) and/or post a question
on the [VASP Forum](https://www.vasp.at/forum/).

|  |
|----|
| **Mind:** We offer support on a courtesy basis only, not as a contractual service. |

------------------------------------------------------------------------

[Back to the top](#toc)
