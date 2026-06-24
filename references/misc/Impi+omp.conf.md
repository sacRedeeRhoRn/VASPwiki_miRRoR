<!-- Source: https://vasp.at/wiki/index.php/Impi%2Bomp.conf | revid: 10911 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Impi+omp.conf
    #
    # define the commands that run vasp_std, vasp_ncl, and vasp_gam
    #
    nthrds=4
    nranks=2

    mpi="-np $nranks -ppn $nranks"
    omp="-genv OMP_NUM_THREADS=$nthrds -genv OMP_STACKSIZE=512m"

    export VASP_TESTSUITE_EXE_STD="mpirun $mpi $omp $PWD/../bin/vasp_std"
    export VASP_TESTSUITE_EXE_NCL="mpirun $mpi $omp $PWD/../bin/vasp_ncl"
    export VASP_TESTSUITE_EXE_GAM="mpirun $mpi $omp $PWD/../bin/vasp_gam"
