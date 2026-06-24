<!-- Source: https://vasp.at/wiki/index.php/Graphite_interlayer_distance | revid: 10430 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Graphite interlayer distance
[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> [cd
Si](Cd_Si.md) \> [cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si relaxation](Cd_Si_relaxation.md) \>
[beta-tin Si](Beta-tin_Si.md) \> [fcc
Ni](Fcc_Ni.md) \> [graphite TS binding
energy](Graphite_TS_binding_energy.md) \>
[graphite MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> graphite interlayer distance  \> [List of
tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 Input](#Input)
  - [2.1 POSCAR](#POSCAR)
  - [2.2 INCAR](#INCAR)
  - [2.3 KPOINTS](#KPOINTS)
- [3 Running this example](#Running_this_example)
- [4 Download](#Download)

## Task
In this example you will determine the interlayer distance of graphite
in the stacking direction using the method of Tchatchenko and Scheffler
to account for van der Waals interactions.

Semilocal DFT at the GGA level underestimates long-range dispersion
interactions. This problem causes a bad overestimation of graphite
lattice in the stacking direction: 8.84 Å (PBE) vs. 6.71 Å (exp).

In this example, the [dispersion correction method of Tchatchenko and
Scheffler](../methods/Tkatchenko-Scheffler_method.md)
is used to cope with this problem.

## Input
### POSCAR
    graphite
    1.0
    1.22800000 -2.12695839  0.00000000
    1.22800000  2.12695839  0.00000000
    0.00000000  0.00000000  7.0
    4
    direct
       0.00000000  0.00000000  0.25000000
       0.00000000  0.00000000  0.75000000
       0.33333333  0.66666667  0.25000000
       0.66666667  0.33333333  0.75000000

### INCAR
    IVDW = 20           
    LVDW_EWALD =.TRUE. 
    NSW = 1 
    IBRION = 2
    ISIF = 4
    PREC = Accurate
    EDIFFG = 1e-5
    LWAVE = .FALSE.
    LCHARG = .FALSE.
    ISMEAR = -5
    SIGMA = 0.01
    EDIFF = 1e-6
    ALGO = Fast
    NPAR = 2

### KPOINTS
    Monkhorst Pack
    0
    gamma
    16 16 8
    0 0 0

## Running this example
To run this example, execute the `run.sh` bash-script:

    #
    # To run VASP this script calls $vasp_std
    # (or posibly $vasp_gam and/or $vasp_ncl).
    # These variables can be defined by sourcing vaspcmd
    . vaspcmd 2> /dev/null

    #
    # When vaspcmd is not available and $vasp_std,
    # $vasp_gam, and/or $vasp_ncl are not set as environment
    # variables, you can specify them here
    [ -z "`echo $vasp_std`" ] && vasp_std="mpirun -np 8 /path-to-your-vasp/vasp_std"
    [ -z "`echo $vasp_gam`" ] && vasp_gam="mpirun -np 8 /path-to-your-vasp/vasp_gam"
    [ -z "`echo $vasp_ncl`" ] && vasp_ncl="mpirun -np 8 /path-to-your-vasp/vasp_ncl"

    #
    # The real work starts here
    #

    rm results.dat

    for d in 6.5 6.6 6.65 6.7 6.75 6.8 6.9 7.0
    do
      cat>POSCAR<<!
    graphite
    1.0
    1.22800000 -2.12695839  0.00000000
    1.22800000  2.12695839  0.00000000
    0.00000000  0.00000000  $d
    4
    direct
       0.00000000  0.00000000  0.25000000
       0.00000000  0.00000000  0.75000000
       0.33333333  0.66666667  0.25000000
       0.66666667  0.33333333  0.75000000
    !
      $vasp_std
      cp OUTCAR OUTCAR.$d
      energy=$(grep "free  ene" OUTCAR.$d|awk '{print $5}')
      echo $d $energy >> results.dat 
    done

The optimal length of the lattice vector *c* normal to the stacking
direction is determined in a series of single point calculations with
varied value of *c* (all other degrees of freedom are fixed at their
experimental values).

The computed *c* vs. energy dependence is written in the file
`results.dat` and can be visualized e.g. using *xmgrace*. The optimal
value can be obtained using the attached utility (python with numpy or
Numeric is needed):

    ./utilities/fit.py results.dat

This should yield:

    200 iterations performed
    Ch-square: 4.30305519481e-09
    ---------

           E0(eV):         -37.433456779
           d0(A):  6.65603352689

The computed value of 6.66 Å agrees well with experiment (6.71 Å).

## Download
[graphiteDistance_ts.tgz](https://vasp.at/wiki/images/6/65/GraphiteDistance_ts.tgz "GraphiteDistance ts.tgz")

[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> [cd
Si](Cd_Si.md) \> [cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si relaxation](Cd_Si_relaxation.md) \>
[beta-tin Si](Beta-tin_Si.md) \> [fcc
Ni](Fcc_Ni.md) \> [graphite TS binding
energy](Graphite_TS_binding_energy.md) \>
[graphite MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> graphite interlayer distance  \> [List of
tutorials](../categories/Category-Tutorials.md)
