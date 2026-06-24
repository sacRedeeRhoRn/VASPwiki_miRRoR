<!-- Source: https://vasp.at/wiki/index.php/Fast.conf | revid: 10909 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Fast.conf
    #
    # define the commands that run vasp_std, vasp_ncl, and vasp_gam
    #
    # Default:
    #
    ##export VASP_TESTSUITE_EXE_STD="mpirun -np 4 $PWD/../bin/vasp_std"
    ##export VASP_TESTSUITE_EXE_NCL="mpirun -np 4 $PWD/../bin/vasp_ncl"
    ##export VASP_TESTSUITE_EXE_GAM="mpirun -np 4 $PWD/../bin/vasp_gam"

    #
    # Run the tests in the FAST category
    #
    export VASP_TESTSUITE_RUN_FAST=Y
