<!-- Source: https://vasp.at/wiki/index.php/LTEMPER | revid: 33094 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LTEMPER
LTEMPER = \[logical\]  
Default: **LTEMPER** = .FALSE. 

Description: LTEMPER specified whether parallel tempering is used. The
flag must be used in combination with [IMAGES](IMAGES.md).

------------------------------------------------------------------------

VASP supports various modes where simultaneous calculations for
different INCAR, KPOINTS, POTCAR, or POSCAR files are performed. The
parallel tempering mode is explained in this section, however, please
read the section [IMAGES](IMAGES.md) first. Parallel
tempering is also known as replica-exchange molecular
dynamics.^([\[1\]](#cite_note-sugi99-1))

If the tags [IMAGES](IMAGES.md)=nn and LTEMPER=.TRUE. are
set in the [INCAR](../input-files/INCAR.md) file, VASP performs parallel
tempering calculations. In this case, it is expedient to supply
different [INCAR](../input-files/INCAR.md) and
[POSCAR](../input-files/POSCAR.md) files in each subdirectory 01, 02, 03,
..., nn. For each subdiretory a different simulation temperature should
be supplied using the tags [TEBEG](TEBEG.md) in the INCAR
files 01/INCAR, 02/INCAR ... nn/INCAR.

In the course of the simulations, VASP will attempt to swap the
temperatures between the images. Swapping attempts are made every
[NTEMPER](NTEMPER.md) MD steps and accepted with a
likelyhood of

$p = \min \left( 1, \frac{ \exp \left(
-\frac{E_j}{kT_i} - \frac{E_i}{kT_j} \right) }{ \exp \left(
-\frac{E_i}{kT_i} - \frac{E_j}{kT_j} \right) } \right) = \min \left( 1,
e^{(E_i - E_j) \left( \frac{1}{kT_i} - \frac{1}{kT_j} \right)} \right) ,$

  
where $E_i, E_j$ and
$T_i, T_j$ are the energies and
temperatures of the considered two replicas. Note that VASP swaps the
temperatures and not the positions between images. This means that the
temperatures in each subdirectory change as the MD progresses.
Information on the current temperatures for each image can be found in
the [OUTCAR](../output-files/OUTCAR.md) files around the lines (all OUTCAR
files will show the same information):

    parallel tempering new

The average acceptance ratios are also written to the
[OUTCAR](../output-files/OUTCAR.md) file. For efficient parallel tempering
the acceptance ratio should not fall much below 0.2-0.3. If the
acceptance ratio is too small, one usually needs to increase the number
of images. However, too many images can also decrease the probability
that all images visit all allowed temperatures.

## Related tags and articles
[IMAGES](IMAGES.md), [NTEMPER](NTEMPER.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-IMAGES-_incategory-Examples)

## References
1.  [↑](#cite_ref-sugi99_1-0) [Y. Sugita and Y. Okamoto, Chemical
    Physics Letters. 314, 141
    (1999).](http://dx.doi.org/10.1016/S0009-2614(99)01123-9)

------------------------------------------------------------------------
