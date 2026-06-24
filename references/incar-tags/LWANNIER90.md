<!-- Source: https://vasp.at/wiki/index.php/LWANNIER90 | revid: 30237 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LWANNIER90
LWANNIER90 = .TRUE. \| .FALSE.  
Default: **LWANNIER90** = .FALSE. 

Description: LWANNIER90=.TRUE. switches on the interface between VASP
and [WANNIER90](http://www.wannier.org).

**N.B.**: This feature is only present if VASP is compiled with
[-DVASP2WANNIER90 or
-DVASP2WANNIER90v2](../redirects/Precompiler_flags.md).

------------------------------------------------------------------------

For LWANNIER90=.TRUE., VASP will write the input files for a WANNIER90
run: **wannier90.win**, **wannier90.mmn**, **wannier90.eig**,
**wannier90.amn**, and if
[LWRITE_UNK](LWRITE_UNK.md)=.TRUE. **wannier90.UNKp.s**.
This is done by running `wannier_setup` in library mode as described in
Chapter 6 of the [WANNIER90
manual](http://www.wannier.org/doc/user_guide.pdf). For documentation of
these files and tags therein, please refer to the [WANNIER90
manual](http://www.wannier.org/doc/user_guide.pdf).

The following cases may occur:

- If **wannier90.win** does not exist, VASP will write the following
  template

&nbsp;

    num_wann = NBANDS

    begin unit_cell_cart
      ... ... ...
      ... ... ...
      ... ... ...
    end unit_cell_cart

    begin atoms_cart
       ... ... ...
       ... ... ...
       ... ... ...
       ... ... ...  
    end atoms_cart

    mp_grid = .. .. ..

    begin kpoints
       ... ... ...
       ... ... ...
       ... ... ...
       ... ... ...
    end kpoints

Here, the `unit_cell_cart`, `atoms_cart`, and `kpoints` blocks, and
`mp_grid` array, will be set in accordance with the setup of the VASP
calculation. This basically corresponds to the information given in the
[POSCAR](../input-files/POSCAR.md) and [KPOINTS](../input-files/KPOINTS.md)
files.

- If the **wannier90.win** file already exists, VASP will only add the
  aforementioned information if it is not already present. This means
  that VASP will check, for instance, whether or not the
  **wannier90.win** file contains a `kpoints` block, and add one if not.
  **Mind**: If it finds a `kpoints` block, VASP will not check whether
  this block agrees with the k points used in the VASP calculation!

The user may create a **wannier90.win** file prior to running VASP with
LWANNIER90=.TRUE., and specify any tag and/or block that is understood
by `wannier_setup` and/or `wannier_run`. For instance, one can specify
the `projections` block in the **wannier90.win** file that controls the
initial guess for the maximally localized Wannier functions. Then, VASP
writes the projections of the Bloch functions onto the relevant
projectors to the **wannier90.amn** file. See Chapter 3 of the
[WANNIER90 manual](http://www.wannier.org/doc/user_guide.pdf) for more
information.

## Related tags and articles
[LWRITE_UNK](LWRITE_UNK.md),
[LWRITE_MMN_AMN](LWRITE_MMN_AMN.md),
[LWRITE_SPN](LWRITE_SPN.md),
[LWANNIER90_RUN](LWANNIER90_RUN.md),
[NUM_WANN](NUM_WANN.md),
[WANNIER90_WIN](WANNIER90_WIN.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LWANNIER90-_incategory-Examples)

------------------------------------------------------------------------
