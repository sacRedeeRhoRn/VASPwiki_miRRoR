<!-- Source: https://vasp.at/wiki/index.php/Graphite_TS_binding_energy | revid: 10432 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Graphite TS binding energy
[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> [cd
Si](Cd_Si.md) \> [cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si relaxation](Cd_Si_relaxation.md) \>
[beta-tin Si](Beta-tin_Si.md) \> [fcc
Ni](Fcc_Ni.md) \> graphite TS binding energy \> [graphite
MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 Input](#Input)
  - [2.1 POSCAR](#POSCAR)
  - [2.2 INCAR](#INCAR)
  - [2.3 KPOINTS](#KPOINTS)
- [3 Running this example](#Running_this_example)
- [4 Download](#Download)
- [5 References](#References)

## Task
In this example you will determine the interlayer binding energy of
graphite in its experimental structure using the method of Tchatchenko
and Scheffler to account for van der Waals interactions.

Semilocal DFT at the GGA level underestimates long-range dispersion
interactions. In the case of graphite, PBE predicts the interlayer
binding energy of ~1 meV/atom which is too small compared to the RPA
reference of 0.048 eV/atom ^([\[1\]](#cite_note-lebegue-1)).

In this example, the interlayer binding energy of graphite in its
experimental structure is determined using the [Tkatchenko-Scheffler
method](../methods/Tkatchenko-Scheffler_method.md),
which performs well in description of the structure of graphite (see
e.g. example [graphite interlayer
distance](Graphite_interlayer_distance.md)).

------------------------------------------------------------------------

## Input
### POSCAR
- Graphite:

&nbsp;

    graphite
    1.0
    1.22800000 -2.12695839  0.00000000
    1.22800000  2.12695839  0.00000000
    0.00000000  0.00000000  6.71
    4
    direct
       0.00000000  0.00000000  0.25000000
       0.00000000  0.00000000  0.75000000
       0.33333333  0.66666667  0.25000000
       0.66666667  0.33333333  0.75000000

- Graphene:

&nbsp;

    graphite
    1.0
    1.22800000 -2.12695839  0.00000000
    1.22800000  2.12695839  0.00000000
    0.00000000  0.00000000  20.
    2
    direct
       0.00000000  0.00000000  0.25000000
       0.33333333  0.66666667  0.25000000

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
- Graphite:

&nbsp;

    Monkhorst Pack
    0
    gamma
    16 16 8
    0 0 0

- Graphene:

&nbsp;

    Monkhorst Pack
    0
    gamma
    16 16 1
    0 0 0

There is no interaction of layers in z-direction for graphene so we need
only 1 k point in this direction.

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

    drct=$(pwd)

    for i in graphene graphite
    do
      cd $drct/$i
      $vasp_std
    done

    cd $drct

    # obtain total energy for graphite 
    en2=$(grep "free  ene" graphite/OUTCAR |tail -1|awk '{print $5}') 

    # obtain total energy for graphene
    en1=$(grep "free  ene" graphene/OUTCAR |tail -1|awk '{print $5}')

    # compute interlayer binding energy (eV/atom)
    deltaE=$(echo print $en2/4 - $en1/2 |python)

    echo "Binding energy (eV/atom): " $deltaE >results.dat

Note that the calculation is performed in two steps (two separate
single-point calculations) in which the energy for bulk graphite and for
graphene are obtained. The binding energy is computed automatically and
it is written in the file `results.dat`. (N.B.: for the latter *python*
needs to be available.)

Even though the TS method predicts a reasonable geometry (see the
[Graphite interlayer
distance](Graphite_interlayer_distance.md)
example) it overestimates the energetics strongly: the computed binding
energy of -0.083 eV/atom is too large compared to the RPA reference of
0.048 eV/atom. This overestimation is - at least in part - due to
neglecting the many-body interactions (see example [Graphite MBD binding
energy](Graphite_MBD_binding_energy.md)).

## Download
[graphiteBinding_ts.tgz](https://vasp.at/wiki/images/3/3a/GraphiteBinding_ts.tgz "GraphiteBinding ts.tgz")

## References
1.  [↑](#cite_ref-lebegue_1-0) [S. Lebègue, J. Harl, Tim Gould, J. G.
    Ángyán, G. Kresse, and J. F. Dobson, Phys. Rev. Lett. 105, 196401
    (2010).](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.105.196401)

[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc Si](Fcc_Si.md) \> [fcc Si
DOS](Fcc_Si_DOS.md) \> [fcc Si
bandstructure](Fcc_Si_bandstructure.md) \> [cd
Si](Cd_Si.md) \> [cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si relaxation](Cd_Si_relaxation.md) \>
[beta-tin Si](Beta-tin_Si.md) \> [fcc
Ni](Fcc_Ni.md) \> graphite TS binding energy \> [graphite
MBD binding
energy](Graphite_MBD_binding_energy.md)
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
 \> [List of tutorials](../categories/Category-Tutorials.md)
