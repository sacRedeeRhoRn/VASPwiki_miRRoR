<!-- Source: https://vasp.at/wiki/index.php/Graphite_MBD_binding_energy | revid: 10431 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Graphite MBD binding energy



[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc
Si](Fcc_Si.md) \>
[fcc Si
DOS](Fcc_Si_DOS.md) \>
[fcc Si
bandstructure](Fcc_Si_bandstructure.md) \>
[cd
Si](Cd_Si.md) \>
[cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si
relaxation](Cd_Si_relaxation.md) \>
[beta-tin
Si](Beta-tin_Si.md) \>
[fcc
Ni](Fcc_Ni.md) \>
[graphite TS binding
energy](Graphite_TS_binding_energy.md) \>
graphite MBD binding energy
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)


## Contents


- [1
  Task](#task)
- [2
  Input](#input)
  - [2.1
    POSCAR](#poscar)
  - [2.2
    INCAR](#incar)
  - [2.3
    KPOINTS](#kpoints)
- [3 Running this
  example](#running-this-example)
- [4
  Download](#download)
- [5
  References](#references)


## Task\[<a
href="/wiki/index.php?title=Graphite_MBD_binding_energy&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Task">edit</a> \| (./index.php.md)\]

In this example you will determine the interlayer binding energy of
graphite in its experimental structure using the MBD@rsSCS method of
Tchatchenko *et al.* to account for van der Waals interactions.

Semilocal DFT at the GGA level underestimates long-range dispersion
interactions. In the case of graphite, PBE predicts the interlayer
binding energy of ~1 meV/atom which is too small compared to the RPA
reference of 0.048 eV/atom
[^lebegue-1].
In contrast, the pairwise correction scheme of Tkatchenko and Scheffler,
overestimates this quantity strongly (0.083 eV/atom, see the [Graphite
TS binding
energy](Graphite_TS_binding_energy.md)
example). Here we show that this problem can be eliminated by if
many-body effects in dispersion energy are taken into account using the
MBD@rsSCS method of Tchatchenko et al. (see [Many-body dispersion
energy](../methods/Many-body_dispersion_energy.md)).

## Input\[<a
href="/wiki/index.php?title=Graphite_MBD_binding_energy&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Input">edit</a> \| (./index.php.md)\]

### POSCAR\[<a
href="/wiki/index.php?title=Graphite_MBD_binding_energy&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: POSCAR">edit</a> \| (./index.php.md)\]

- Graphite:

<!-- -->

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

<!-- -->

    graphite
    1.0
    1.22800000 -2.12695839  0.00000000
    1.22800000  2.12695839  0.00000000
    0.00000000  0.00000000  20.
    2
    direct
       0.00000000  0.00000000  0.25000000
       0.33333333  0.66666667  0.25000000

### INCAR\[<a
href="/wiki/index.php?title=Graphite_MBD_binding_energy&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

    IVDW = 202           
    LVDWEXPANSION =.TRUE. 
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

### KPOINTS\[<a
href="/wiki/index.php?title=Graphite_MBD_binding_energy&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: KPOINTS">edit</a> \| (./index.php.md)\]

- Graphite:

<!-- -->

    Monkhorst Pack
    0
    gamma
    16 16 8
    0 0 0

- Graphene:

<!-- -->

    Monkhorst Pack
    0
    gamma
    16 16 1
    0 0 0

  

## Running this example\[<a
href="/wiki/index.php?title=Graphite_MBD_binding_energy&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Running this example">edit</a> \| (./index.php.md)\]

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

    # Here the work starts
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

The computed value of 0.050 eV/A is now fairly close to the RPA
reference of 0.048 eV/atom
[^lebegue-1].

## Download\[<a
href="/wiki/index.php?title=Graphite_MBD_binding_energy&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/2/2a/GraphiteBinding_mbd.tgz" class="internal"
title="GraphiteBinding mbd.tgz">graphiteBinding_mdb.tgz</a>

## References\[<a
href="/wiki/index.php?title=Graphite_MBD_binding_energy&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]
[Overview](../tutorials/Bulk_Systems_-_Tutorial.md) \>
[fcc
Si](Fcc_Si.md) \>
[fcc Si
DOS](Fcc_Si_DOS.md) \>
[fcc Si
bandstructure](Fcc_Si_bandstructure.md) \>
[cd
Si](Cd_Si.md) \>
[cd Si volume
relaxation](Cd_Si_volume_relaxation.md) \>
[cd Si
relaxation](Cd_Si_relaxation.md) \>
[beta-tin
Si](Beta-tin_Si.md) \>
[fcc
Ni](Fcc_Ni.md) \>
[graphite TS binding
energy](Graphite_TS_binding_energy.md) \>
graphite MBD binding energy
 \> [graphite interlayer
distance](Graphite_interlayer_distance.md)
 \> [List of
tutorials](../categories/Category-Tutorials.md)

[^lebegue-1]: [S. Lebègue, J. Harl, Tim Gould, J. G. Ángyán, G. Kresse, and J. F. Dobson, Phys. Rev. Lett. 105, 196401 (2010).](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.105.196401)
