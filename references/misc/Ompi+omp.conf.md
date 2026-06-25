<!-- Source: https://vasp.at/wiki/index.php/Ompi%2Bomp.conf | revid: 10912 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Ompi+omp.conf


    #
    # define the commands that run vasp_std, vasp_ncl, and vasp_gam
    #
    kmp="-x KMP_AFFINITY=verbose,granularity=fine,compact,1,0 -x KMP_STACKSIZE=512m"

    nthrds=4
    nranks=2

    mpi="--map-by node:PE=$nthrds --bind-to core"
    omp="-x OMP_NUM_THREADS=$nthrds"

    export VASP_TESTSUITE_EXE_STD="mpirun -np $nranks $kmp $mpi $omp $PWD/../bin/vasp_std"
    export VASP_TESTSUITE_EXE_NCL="mpirun -np $nranks $kmp $mpi $omp $PWD/../bin/vasp_ncl"
    export VASP_TESTSUITE_EXE_GAM="mpirun -np $nranks $kmp $mpi $omp $PWD/../bin/vasp_gam"


