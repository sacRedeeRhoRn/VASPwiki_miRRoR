<!-- Source: https://vasp.at/wiki/index.php/ICAMM_Rennes_2019_HOWTO | revid: 9177 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ICAMM Rennes 2019 HOWTO
Here is a brief tutorial on how to run a calculation and how to run
post-treatment tools during the VASP training school in Rennes.

- **First thing to do**:

launch terminal:

go to **openSUSE** booklet (down left of the screen), select **Système**
and choose **Terminal**

in this terminal you run the following 5 commands (copy/paste):

    export LC_NUMERIC="en_US.UTF-8"
    export LIBGL_ALWAYS_SOFTWARE=1
    export vasp_std="mpirun -np 2 /usr/local/ICAMM_2019/bin_vasp/5.4/vasp_std"
    export vasp_gam="mpirun -np 2 /usr/local/ICAMM_2019/bin_vasp/5.4/vasp_gam"
    export vasp_ncl="mpirun -np 2 /usr/local/ICAMM_2019/bin_vasp/5.4/vasp_ncl"

**3 versions of the VASP code are available for vasp5.4**:

the so-called *standard* version which allows you to make *standard*
calculation with several K-points

To use it, enter the following command on a terminal

In sequential:

`vasp5_std`

the so-called *non-colinear* version which allows you to make
*non-colinear* calculation with several K-points

To use it, enter the following command on a terminal

In sequential:

`vasp5_ncl`

the so-called *gamma* version which allows you to make *gamma*
calculation but with only 1 K-point

To use it, enter the following command on a terminal

In sequential:

`vasp5_gam`

**3 versions of the VASP code are available for vasp6:**

the so-called *standard* version which allows you to make *standard*
calculation with several K-points

To use it, enter the following command on a terminal

In sequential:

`vasp6_std`

In parallel:

`mpirun –np 2 /usr/local/ICAMM_2019/bin_vasp/6/vasp_std`

the so-called *non-colinear* version which allows you to make
*non-colinear* calculation with several K-points

To use it, enter the following command on a terminal

In sequential:

`vasp6_ncl`

In parallel:

`mpirun –np 2 /usr/local/ICAMM_2019/bin_vasp/6/vasp_ncl`

the so-called *gamma* version which allows you to make *gamma*
calculation but with only 1 K-point

To use it, enter the following command on a terminal

In sequential:

`vasp6_gam`

In parallel:

`mpirun –np 2 /usr/local/ICAMM_2019/bin_vasp/6/vasp_gam`

  

**Please always keep in mind that our local workstation are quite
limited so please avoid to run two VASP calculations simultaneously.**

- **wannier90**

To use wannier90, use the following command:

`/usr/local/ICAMM_2019/wannier90-1.2/wannier90.x`

- **phonopy**

To use phonopy, use the following command:

`phonopy`

- **Gnuplot**:

Gnuplot is a portable command-line driven graphing utility.

To use it, enter the following command on a terminal

`gnuplot`

For more infos about gnuplot, visit the [following
website](http://www.gnuplot.info)

- **p4vasp**:

To use the p4vasp visualization software, use the following command:

`p4v`

- **VESTA**:

To use the VESTA visualization software, use the following command:

`VESTA`

- **VMD**:

To use the vmd visualization software, use the following command:

`VMD`
