<!-- Source: https://vasp.at/wiki/index.php/Cuda.conf | revid: 10913 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Cuda.conf


    #
    # N.B.: there is no CUDA-GPU gamma-only version
    #
    export VASP_TESTSUITE_EXE_STD="mpirun -np 4 $PWD/../bin/vasp_gpu"
    export VASP_TESTSUITE_EXE_NCL="mpirun -np 4 $PWD/../bin/vasp_gpu_ncl"
    export VASP_TESTSUITE_EXE_GAM=

    #
    # tell runtest that these executables will run with the CUDA port
    # (will skip tests that are not supported).
    #
    export VASP_TESTSUITE_CUDA=Y

    #
    # the above is equivalent to setting
    #
    ##export VASP_TESTSUITE_SKIP_NOCUDA=Y
    ##export VASP_TESTSUITE_SKIP_GAMMA=Y
    ##export VASP_TESTSUITE_RUN_LREAL=Y
    ##export VASP_TESTSUITE_INCAR_PREPEND="LSCAAWARE=.FALSE. ; $VASP_TESTSUITE_INCAR_PREPEND "


