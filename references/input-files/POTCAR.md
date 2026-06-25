<!-- Source: https://vasp.at/wiki/index.php/POTCAR | revid: 33125 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# POTCAR


The POTCAR file is a mandatory
<a href="/wiki/Input_file" class="mw-redirect" title="Input file">input
file</a>. It contains the
<a href="/wiki/Pseudopotential" class="mw-redirect"
title="Pseudopotential">pseudopotential</a> for each atomic species in
the same order as in the [POSCAR](POSCAR.md). An example to
create the POTCAR file for a
structure with three elements is

     cat ~/pot/Al/POTCAR ~/pot/C/POTCAR ~/pot/H/POTCAR > POTCAR

The order must be the same order as defined in the
[POSCAR](POSCAR.md) file.

Also see:

- Simple instructions to set up a
  POTCAR file with the correct
  format: [Preparing a
  POTCAR](../tutorials/Preparing_a_POTCAR.md).

<!-- -->

- Guide on recommendations: [Choosing
  pseudopotentials](../tutorials/Choosing_pseudopotentials.md).

|  |
|----|
| **Important:** The settings in the POTCAR file are read-only and must not be edited. |

No standard usage of VASP requires modifying the
POTCAR file. Specifically, do
not modify the [LEXCH](../incar-tags/LEXCH.md) tag in the
POTCAR file. If you want to
select a different functional, set the [XC](../incar-tags/XC.md),
[GGA](../incar-tags/GGA.md) or [METAGGA](../incar-tags/METAGGA.md) tag in the
[INCAR](INCAR.md) file.

## File format\[<a href="/wiki/index.php?title=POTCAR&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: File format">edit</a> \| (./index.php.md)\]

POTCAR files contain a header
section with some tags, and large blocks of tabulated data containing
the actual pseudopotential. More recent potential sets contain more
information in the headers, so not all tags described below are present
in all files ever distributed. Information about the atoms, i.e., their
mass [POMASS](../incar-tags/POMASS.md), their number of valence electrons
[ZVAL](../incar-tags/ZVAL.md), the energy of the reference configuration for
which the pseudopotential was created, etc. is present since VASP
version 3.2. Since the release of the potpaw.54 potential set (VASP
version 5.4) POTCAR files also
contain a copyright notice and a unique hash that can be used for
verification of the file.

Some data, e.g., additional information about the kinetic-energy density
of the core-electrons, is not available in all
POTCAR files, but required for
[METAGGA
calculations](../incar-tags/METAGGA.md)

All POTCARs end with the line
` End of Dataset`.

The Ti_pv potential from the potpaw_PBE.64 set, where the *3p* states
are included in the valence, serves as an example to explain some tags
in the following.

|  |
|----|
| **Mind:** The information below is not complete. However, we believe that it covers the most information required in practice. Some other tags are also documented in the POTCAR file itself. |

[TITEL](../incar-tags/TITEL.md)  
The first line in any POTCAR
file is the title of the pseudopotential. It is later printed again
under the [TITEL](../incar-tags/TITEL.md) tag. Depending on the potential
set, this might be more or less verbose. In our example, we have a
[PAW](../methods/Projector-augmented-wave_formalism.md)
potential of Ti created with the PBE functional. The "\_pv" suffix
indicates that semicore *p*-states are included as valence electrons. We
also see that this potential was created in September of 2000.

`TITEL = PAW_PBE Ti_pv 07Sep2000`

|  |
|----|
| **Tip:** You may choose this string to indicate what pseudopotential you have used in your publication to ensure the reproducibility of your results. |

[LEXCH](../incar-tags/LEXCH.md)  
This tag specifies the
<a href="/wiki/Exchange-correlation_functional" class="mw-redirect"
title="Exchange-correlation functional">exchange-correlation
functional</a> used to create the potential. Even if another functional
is selected in the [INCAR](INCAR.md) via the
[XC](../incar-tags/XC.md), [GGA](../incar-tags/GGA.md) or
[METAGGA](../incar-tags/METAGGA.md) tag, this information is required to
recalculate the exchange-correlation energy inside the PAW spheres.
Here, PE stands for the PBE functional.

`LEXCH = PE`

[ZVAL](../incar-tags/ZVAL.md)  
This specifies the number of valence electrons considered in the
pseudopotential. It is printed in the second line of the
POTCAR and again in the same
line as [POMASS](../incar-tags/POMASS.md).

[POMASS](../incar-tags/POMASS.md)  
The atomic mass in atomic units. One can increase this in
<a href="/wiki/MD" class="mw-redirect" title="MD">molecular dynamics
calculations</a> for light elements

`POMASS = 47.880; ZVAL = 10.000 mass and valenz`

<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> and [ENMIN](../incar-tags/ENMIN.md)  
These two tags are default plane-wave cutoffs for the pseudopotential in
electron Volt (eV). [ENMIN](../incar-tags/ENMIN.md) is the minimum viable,
end <a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a>
the recommended cutoff. For
POTCAR files with more than
one species, the maximum cutoffs
(<a href="/wiki/ENMAX" class="mw-redirect" title="ENMAX">ENMAX</a> or
[ENMIN](../incar-tags/ENMIN.md)) are used for the calculation. Note that
the [INCAR](INCAR.md) tag [ENCUT](../incar-tags/ENCUT.md)
overwrites the default from the
POTCAR.

`ENMAX = 222.335; ENMIN = 166.751 eV`

|  |
|----|
| **Tip:** We recommend setting the [ENCUT](../incar-tags/ENCUT.md) tag in the [INCAR](INCAR.md) file. |

[EAUG](../incar-tags/EAUG.md)  
The energy cutoff for the plane-wave representation for the augmentation
charges in eV. This might be overwritten in the
[INCAR](INCAR.md) using the tag [ENAUG](../incar-tags/ENAUG.md).

`EAUG = 482.848`

Atomic configuration  
This block describes the atomic reference configuration used to create
the pseudopotential. The first three columns, *n*, *l*, and *j*
represent the principal, angular momentum, and total angular momentum
*j*=\|*l*+*s*\| quantum numbers. This is followed by the total energy
and the occupation numbers of the orbitals. Note that fractional
occupations are possible because the reference configuration does not
have to be the ground state. It is possible to deduce the
valence-electron configuration of the potentential using the valence
electron number ([ZVAL](../incar-tags/ZVAL.md)): Add occupied states from
the bottom of the table until it counts [ZVAL](../incar-tags/ZVAL.md), i.e.,
10 in our example. Thus, we arrive at
3*p*<sup>6</sup>3*d*<sup>3</sup>4*s*<sup>1</sup> for Ti_pv.

<!-- -->

    Atomic configuration
        8 entries
         n  l   j            E        occ.
         1  0  0.50     -4865.3608   2.0000
         2  0  0.50      -533.1368   2.0000
         2  1  1.50      -440.5031   6.0000
         3  0  0.50       -59.3186   2.0000
         3  1  1.50       -35.7012   6.0000
         3  2  2.50        -1.9157   3.0000
         4  0  0.50        -3.7291   1.0000
         4  3  2.50        -1.3606   0.0000

## Related tags and sections\[<a href="/wiki/index.php?title=POTCAR&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[Available
pseudopotentials](Available_pseudopotentials.md),
<a href="/wiki/Prepare_a_POTCAR" class="mw-redirect"
title="Prepare a POTCAR">Prepare a POTCAR</a>, [Choosing
pseudopotentials](../tutorials/Choosing_pseudopotentials.md),
[Projector-augmented-wave
formalism](../methods/Projector-augmented-wave_formalism.md)


