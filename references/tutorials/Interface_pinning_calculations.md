<!-- Source: https://vasp.at/wiki/index.php/Interface_pinning_calculations | revid: 36241 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Interface pinning calculations
**Interface pinning** uses the $Np_zT$
ensemble where the barostat only acts along the $z$ direction. This ensemble uses a Langevin thermostat and a
Parrinello-Rahman barostat with lattice constraints in the remaining two
dimensions. The solid-liquid interface must be in the
$x$-$y$
plane perpendicular to the action of the barostat.

Set the following tags for the **interface pinning** method:

[OFIELD_Q6_NEAR](../incar-tags/OFIELD_Q6_NEAR.md)  
Defines the near-fading distance $n$.

[OFIELD_Q6_FAR](../incar-tags/OFIELD_Q6_FAR.md)  
Defines the far-fading distance $f$.

[OFIELD_KAPPA](../incar-tags/OFIELD_KAPPA.md)  
Defines the coupling strength $\kappa$
of the bias potential.

[OFIELD_A](../incar-tags/OFIELD_A.md)  
Defines the desired value of the order parameter $A$.

The following example [INCAR](../input-files/INCAR.md) file calculates the
interface pinning in sodium^([\[1\]](#cite_note-pedersen:prb:13-1)):

    TEBEG = 400                   # temperature in K
    POTIM = 4                     # timestep in fs
    IBRION = 0                    # run molecular dynamics
    ISIF = 3                      # use Parrinello-Rahman barostat for the lattice
    MDALGO = 3                    # use Langevin thermostat
    LANGEVIN_GAMMA_L = 3.0        # friction coefficient for the lattice degree of freedoms (DoF)
    LANGEVIN_GAMMA = 1.0          # friction coefficient for atomic DoFs for each species
    PMASS = 100                   # mass for lattice DoFs
    LATTICE_CONSTRAINTS = F F T   # fix x-y plane, release z lattice dynamics
    OFIELD_Q6_NEAR = 3.22         # near fading distance for function w(r) in Angstrom
    OFIELD_Q6_FAR = 4.384         # far fading distance for function w(r) in Angstrom
    OFIELD_KAPPA = 500            # strength of bias potential in eV/(unit of Q)^2
    OFIELD_A = 0.15               # desired value of the Q6 order parameter

## Related tags and articles
[ICONST](../input-files/ICONST.md),
[OFIELD_Q6_NEAR](../incar-tags/OFIELD_Q6_NEAR.md),
[OFIELD_Q6_FAR](../incar-tags/OFIELD_Q6_FAR.md),
[OFIELD_KAPPA](../incar-tags/OFIELD_KAPPA.md),
[OFIELD_A](../incar-tags/OFIELD_A.md), [REPORT](../output-files/REPORT.md)

[Interface pinning](../theory/Interface_pinning.md)

## References
1.  [↑](#cite_ref-pedersen:prb:13_1-0) [U. R. Pedersen, F. Hummel, G.
    Kresse, G. Kahl, and C. Dellago, Phys. Rev. B **88**, 094101
    (2013).](https://doi.org/10.1103/PhysRevB.88.094101)

  

------------------------------------------------------------------------
