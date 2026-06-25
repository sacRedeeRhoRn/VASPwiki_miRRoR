<!-- Source: https://vasp.at/wiki/index.php/TS_search_using_the_NEB_Method | revid: 8919 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# TS search using the NEB Method


Description: the Nudged Elastic Band Method generates an energy profile
along a reaction path, using equidistant IMAGES along the path. The
input geometries of the IMAGES are interpolated between the geometries
of the initial and the final states, e.g. using the script
interpolatePOSCAR, which processes the con-catenated POSCAR files of the
initial and the final state of the reaction (POSCAR_if). in the case of
ammonia flipping the final state is a mirror of the initial state and
need not be calculated explicitely. For each IMAGE, a separate
sub-directory 00 ... (IMAGES+1) is needed, which contains all output of
the respective IMAGE. The number of cores on which VASP is run has to be
an integer multiple of the number of IMAGES.

------------------------------------------------------------------------

- [INCAR](../input-files/INCAR.md)

<!-- -->

    SYSTEM = Ammonia flipping
    IMAGES = 6
    SPRING = -5
    IBRION = 2
    NSW = 50
    ALGO = N
    POTIM = 1.0
    EDIFF = 1e-6

  

- [KPOINTS](../input-files/KPOINTS.md)

<!-- -->

    k-points
     0
    G
     1 1 1

  

- [POSCAR](../input-files/POSCAR.md)\_if

<!-- -->

    ammonia flipping
      1.00000000000000
        6.000000    0.000000    0.000000
        0.000000    7.000000    0.000000
        0.000000    0.000000    8.000000
        3     1
    Direct
     0.636428  0.567457  0.5491645
     0.500000  0.364985  0.5491330
     0.363572  0.567457  0.5491645
     0.500000  0.500000  0.5000000
    ammonia flipping
      1.00000000000000
        6.000000    0.000000    0.000000
        0.000000    7.000000    0.000000
        0.000000    0.000000    8.000000
        3     1
    Direct
     0.636428  0.567457  0.4508355
     0.500000  0.364985  0.4508670
     0.363572  0.567457  0.4508355
     0.500000  0.500000  0.5000000

## Download\[<a
href="/wiki/index.php?title=TS_search_using_the_NEB_Method&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="http://www.vasp.at/vasp-workshop/examples/ammonia_flipping.tgz"
class="external text" rel="nofollow">ammonia_flipping.tgz, sub-folder
NEB</a>

------------------------------------------------------------------------

<a
href="/wiki/index.php?title=VASP_example_calculations&amp;action=edit&amp;redlink=1"
class="new" title="VASP example calculations (page does not exist)">To
the list of examples</a> or to the [main
page](The_VASP_Manual.md)

  


