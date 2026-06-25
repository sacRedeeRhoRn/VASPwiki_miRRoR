<!-- Source: https://vasp.at/wiki/index.php/LWANNIER90 | revid: 30237 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LWANNIER90


LWANNIER90 = .TRUE. \|
.FALSE.  
Default: **LWANNIER90** = .FALSE. 

Description: LWANNIER90=.TRUE.
switches on the interface between VASP and
<a href="http://www.wannier.org" class="external text"
rel="nofollow">WANNIER90</a>.

**N.B.**: This feature is only present if VASP is compiled with
<a href="/wiki/Precompiler_flags#Optional" class="mw-redirect"
title="Precompiler flags">-DVASP2WANNIER90 or -DVASP2WANNIER90v2</a>.

------------------------------------------------------------------------

For LWANNIER90=.TRUE., VASP
will write the input files for a WANNIER90 run: **wannier90.win**,
**wannier90.mmn**, **wannier90.eig**, **wannier90.amn**, and if
[LWRITE_UNK](LWRITE_UNK.md)=.TRUE. **wannier90.UNKp.s**.
This is done by running `wannier_setup` in library mode as described in
Chapter 6 of the <a href="http://www.wannier.org/doc/user_guide.pdf"
class="external text" rel="nofollow">WANNIER90 manual</a>. For
documentation of these files and tags therein, please refer to the
<a href="http://www.wannier.org/doc/user_guide.pdf"
class="external text" rel="nofollow">WANNIER90 manual</a>.

The following cases may occur:

- If **wannier90.win** does not exist, VASP will write the following
  template

<!-- -->

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
LWANNIER90=.TRUE., and specify
any tag and/or block that is understood by `wannier_setup` and/or
`wannier_run`. For instance, one can specify the `projections` block in
the **wannier90.win** file that controls the initial guess for the
maximally localized Wannier functions. Then, VASP writes the projections
of the Bloch functions onto the relevant projectors to the
**wannier90.amn** file. See Chapter 3 of the
<a href="http://www.wannier.org/doc/user_guide.pdf"
class="external text" rel="nofollow">WANNIER90 manual</a> for more
information.

## Related tags and articles\[<a
href="/wiki/index.php?title=LWANNIER90&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LWRITE_UNK](LWRITE_UNK.md),
[LWRITE_MMN_AMN](LWRITE_MMN_AMN.md),
[LWRITE_SPN](LWRITE_SPN.md),
[LWANNIER90_RUN](LWANNIER90_RUN.md),
[NUM_WANN](NUM_WANN.md),
[WANNIER90_WIN](WANNIER90_WIN.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-LWANNIER90-_incategory-Examples)

------------------------------------------------------------------------


