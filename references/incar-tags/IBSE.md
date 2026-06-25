<!-- Source: https://vasp.at/wiki/index.php/IBSE | revid: 37229 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IBSE


IBSE = 0 \| 1 \| 2 \| 3  
Default: **IBSE** = 2 

Description: IBSE can be used
to select the algorithm for solving the Bethe-Salpeter or Casida
equation.

------------------------------------------------------------------------

The following options are available to solve the Bethe-Salpeter or
Casida equation:

- IBSE = 0:
  <a href="/wiki/Bethe-Salpeter_equations#Exact_diagonalization"
  class="mw-redirect" title="Bethe-Salpeter equations">Exact
  diagonalization with old BSE driver</a>
- IBSE = 1:
  <a href="/wiki/Bethe-Salpeter_equations#Time_evolution"
  class="mw-redirect" title="Bethe-Salpeter equations">Time evolution</a>
- IBSE = 2:
  <a href="/wiki/Bethe-Salpeter_equations#Exact_diagonalization"
  class="mw-redirect" title="Bethe-Salpeter equations">Exact
  diagonalization</a>
- IBSE = 3:
  <a href="/wiki/Bethe-Salpeter_equations#Lanczos_algorithm"
  class="mw-redirect" title="Bethe-Salpeter equations">Lanczos
  algorithm</a>

`IBSE`` = 2` and
`IBSE`` = 0` yield exactly the
same results but the old driver
(`IBSE`` = 0`) is typically
much slower and will be deprecated in the future.

|  |
|----|
| **Mind:** `IBSE`` = 2` and `IBSE`` = 3` are only available for VASP version 6.5.0 and above. |


## Contents


- [1 Scientific
  output](#scientific-output)
- [2 Performance
  output](#performance-output)
  - [2.1 IBSE =
    0,2](#IBSE_=_0,2)
  - [2.2 IBSE =
    1](#IBSE_=_1)
  - [2.3 IBSE =
    3](#IBSE_=_3)
- [3 Related tag
  and articles](#related-tag-and-articles)


## Scientific output\[<a href="/wiki/index.php?title=IBSE&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Scientific output">edit</a> \| (./index.php.md)\]

Not all solvers provide all types of scientifically relevant output. The
table below summarises for each value of IBSE what kinds of results can
be obtained.

<table class="wikitable" style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<th rowspan="2">Output type</th>
<th rowspan="2">Output file(s)</th>
<th colspan="4">IBSE</th>
</tr>
<tr>
<th>0</th>
<th>1</th>
<th>2</th>
<th>3</th>
</tr>
&#10;<tr>
<td>Dielectric function</td>
<td><a href="/wiki/Vasprun.xml" title="Vasprun.xml">vasprun.xml</a>, <a
href="/wiki/Vaspout.h5" title="Vaspout.h5">vaspout.h5</a></td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>Optical transitions</td>
<td><a href="/wiki/Vasprun.xml" title="Vasprun.xml">vasprun.xml</a>, <a
href="/wiki/Vaspout.h5" title="Vaspout.h5">vaspout.h5</a></td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr>
<td>BSE fatbands<sup>1</sup></td>
<td><a href="/wiki/BSEFATBAND" title="BSEFATBAND">BSEFATBAND</a>, <a
href="/wiki/Vaspout.h5" title="Vaspout.h5">vaspout.h5</a></td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td>Exciton wavefunction<sup>1,2</sup></td>
<td><a href="/wiki/CHG" title="CHG">CHG</a>.X (X = excitonic state
index), <a href="/wiki/Vaspout.h5"
title="Vaspout.h5">vaspout.h5</a></td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr>
<td colspan="6" style="background: ; font-size: 90%"><p><sup>1</sup>
Only written if <a href="/wiki/NBSEEIG" title="NBSEEIG">NBSEEIG</a> is
set in the INCAR<br />
<sup>2</sup> Only written if one of <a href="/wiki/BSEHOLE"
title="BSEHOLE">BSEHOLE</a> or <a href="/wiki/BSEELECTRON"
title="BSEELECTRON">BSEELECTRON</a> is set in the INCAR</p></td>
</tr>
</tbody>
</table>

## Performance output\[<a href="/wiki/index.php?title=IBSE&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Performance output">edit</a> \| (./index.php.md)\]

Besides the numerical results, different solvers will write different
information on the OUTCAR. In the following examples we used a small
bulk-LiF unit cell on a sparse k-grid.

### IBSE = 0,2\[<a href="/wiki/index.php?title=IBSE&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: IBSE = 0,2">edit</a> \| (./index.php.md)\]

The old and new BSE driver perform exact diagonalization of the BSE
Hamiltonian. At the end they only provide information on how long it
took to diagonalize the matrix and how long it needed to compute the
optical amplitudes.

### IBSE = 1\[<a href="/wiki/index.php?title=IBSE&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: IBSE = 1">edit</a> \| (./index.php.md)\]

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

### IBSE = 3\[<a href="/wiki/index.php?title=IBSE&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: IBSE = 3">edit</a> \| (./index.php.md)\]

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

## Related tag and articles\[<a href="/wiki/index.php?title=IBSE&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Related tag and articles">edit</a> \| (./index.php.md)\]

IBSE,
[BSEPREC](BSEPREC.md), [NBANDSV](NBANDSV.md),
[NBANDSO](NBANDSO.md), [CSHIFT](CSHIFT.md),
[OMEGAMAX](OMEGAMAX.md),
<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a>, [Time-dependent
density-functional theory
calculations](../methods/Time-dependent_density-functional_theory_calculations.md),
<a href="/wiki/Bethe-Salpeter_equations" class="mw-redirect"
title="Bethe-Salpeter equations">Bethe-Salpeter equations</a>

------------------------------------------------------------------------


