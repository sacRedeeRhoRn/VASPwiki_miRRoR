<!-- Source: https://vasp.at/wiki/index.php/IBSE | revid: 37229 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IBSE
IBSE = 0 \| 1 \| 2 \| 3  
Default: **IBSE** = 2 

Description: IBSE can be used to select the algorithm for solving the
Bethe-Salpeter or Casida equation.

------------------------------------------------------------------------

The following options are available to solve the Bethe-Salpeter or
Casida equation:

- IBSE = 0: [Exact diagonalization with old BSE
  driver](../redirects/Bethe-Salpeter_equations.md)
- IBSE = 1: [Time
  evolution](../redirects/Bethe-Salpeter_equations.md)
- IBSE = 2: [Exact
  diagonalization](../redirects/Bethe-Salpeter_equations.md)
- IBSE = 3: [Lanczos
  algorithm](../redirects/Bethe-Salpeter_equations.md)

`IBSE`` = 2` and `IBSE`` = 0` yield exactly the same results but the old
driver (`IBSE`` = 0`) is typically much slower and will be deprecated in
the future.

|  |
|----|
| **Mind:** `IBSE`` = 2` and `IBSE`` = 3` are only available for VASP version 6.5.0 and above. |

## Contents

- [1 Scientific output](#Scientific_output)
- [2 Performance output](#Performance_output)
  - [2.1 IBSE = 0,2](#IBSE_=_0,2)
  - [2.2 IBSE = 1](#IBSE_=_1)
  - [2.3 IBSE = 3](#IBSE_=_3)
- [3 Related tag and articles](#Related_tag_and_articles)

## Scientific output
Not all solvers provide all types of scientifically relevant output. The
table below summarises for each value of IBSE what kinds of results can
be obtained.

[TABLE]

## Performance output
Besides the numerical results, different solvers will write different
information on the OUTCAR. In the following examples we used a small
bulk-LiF unit cell on a sparse k-grid.

### IBSE = 0,2
The old and new BSE driver perform exact diagonalization of the BSE
Hamiltonian. At the end they only provide information on how long it
took to diagonalize the matrix and how long it needed to compute the
optical amplitudes.

### IBSE = 1
At the end of the run the time-evolution solver will write to the OUTCAR
the relevant parameters used in its execution, as well as how long it
took to perform the full computation.

     Time evolution parameters used:
     -------------------------------

     Calculating BSE spectra using full res.-antires. coupling
     Matrix rank:       2430

      Omega_max:   94.2354
     Broadening:    0.4000
          T_max:   25.0000
        BSEPREC:  Accurate
         Scheme:  3rd order update equations

     Number of time steps:     9423

     First time step:  0.265293E-02 1/eV
     Last  time step:  0.265293E-02 1/eV

     dOmega  :  0.01000
     N_Omega :   9425

     CPU time (time steps)        55.76sec

        BSE_TE:  cpu time     60.0951: real time     65.1642

### IBSE = 3
The Haydock-Lanczos solver terminates the calculation once the trace of
the dielectric function converges. At the end, information about
convergence of the dielectric function along each direction is written
to the OUTCAR file.

     Parameters set for Lanczos algorithm
       Threshold:  0.1000000E-04
       Maximum energy:   94.235
        Number of energy steps:         1000
        Number of iterations needed to reach set accuracy:         250
        Final accuracy along all directions:
        x          0.6277122E-05
        y          0.4480512E-05
        z          0.1392376E-04
        xy         0.1792577E-04
        yz         0.4541156E-05
        zx         0.1034294E-04

## Related tag and articles
IBSE, [BSEPREC](BSEPREC.md),
[NBANDSV](NBANDSV.md), [NBANDSO](NBANDSO.md),
[CSHIFT](CSHIFT.md), [OMEGAMAX](OMEGAMAX.md),
[BSE calculations](../redirects/BSE_calculations.md),
[Time-dependent density-functional theory
calculations](../methods/Time-dependent_density-functional_theory_calculations.md),
[Bethe-Salpeter
equations](../redirects/Bethe-Salpeter_equations.md)

------------------------------------------------------------------------
