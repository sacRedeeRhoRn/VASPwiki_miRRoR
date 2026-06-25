<!-- Source: https://vasp.at/wiki/index.php/LOCPROJ | revid: 26048 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LOCPROJ


LOCPROJ = **\<sites\>** :
**\<functions-Ylm-specs\>** : **\<functions-radial-specs\>**  
Default: **LOCPROJ** = None 

Description: The LOCPROJ tag
specifies local functions on which the orbitals are projected. These
projections are written to the [PROJCAR](PROJCAR.md) file,
[LOCPROJ file](#locproj-file), and
[vasprun.xml](../output-files/Vasprun.xml.md) file.

------------------------------------------------------------------------

|  |
|----|
| **Disambiguation** May also refer to [LOCPROJ file](#locproj-file). |

When the LOCPROJ tag is set,
VASP performs the projection of the Kohn-Sham orbitals
$|\psi_{n\mathbf{k}}\rangle$ onto a localized orbitals
basis $|\beta^\alpha_{lm}\rangle$ which can be written as

$P^\alpha_{lmn\mathbf{k}} \equiv \langle
\beta_{lm}^{\alpha}|S|\psi_{n\mathbf{k}}\rangle =
\underbrace{\langle
\beta_{lm}^{\alpha}|\psi_{n\mathbf{k}}\rangle}_{P^{\text{SOFT},\alpha}_{lmn\mathbf{k}}} +
\underbrace{\sum_{ij} \langle \beta^\alpha_{lm}|\tilde{p}_i\rangle
Q_{ij} \langle \tilde{p}_j |
\psi_{n\mathbf{k}}\rangle}_{P^{\text{AUG},\alpha}_{lmn\mathbf{k}}}.$

Here, the two terms on the right-hand side are called soft and
augmentation part, respectively. $S$ is the
overlap matrix,

$S
= 1+\sum_{ij} |\tilde{p}_i\rangle Q_{ij} \langle \tilde{p}_j|.$

The radial and the angular part of $\beta^\alpha_{lm}(\mathbf{r})$ are described by the
LOCPROJ tag, which comprises
three parts separated by colons that are denoted as **\<sites\>**,
**\<functions-Ylm-specs\>**, and **\<functions-radial-specs\>**. For
instance, to perform the projection onto a hydrogen-like *1s* function
on the first ionic position specified in the
[POSCAR](../input-files/POSCAR.md) file, the tag reads

    LOCPROJ = 1 : s : Hy


## Contents


- [1 Specifying the
  local basis](#specifying-the-local-basis)
- [2 Example for
  LOCPROJ tag](#example-for-locproj-tag)
- [3 LOCPROJ
  file](#locproj-file)
- [4 Related tags
  and articles](#related-tags-and-articles)
- [5
  References](#references)


## Specifying the local basis\[<a href="/wiki/index.php?title=LOCPROJ&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Specifying the local basis">edit</a> \| (./index.php.md)\]

- **\<sites\>**: The sites on which the local functions are centered.

It is specified either using the index of the ionic positions as defined
in the [POSCAR](../input-files/POSCAR.md) file, or in terms of direct
coordinates of the real space lattice. For instance, `1 2 6-8` will
select sites 1, 2, 6, 7, and 8 as defined in the
[POSCAR](../input-files/POSCAR.md) file. On the other hand, `(0.5, 0, 0)`
specifies the position in terms of direct coordinates of the real space
lattice. The modes of the specification can be mixed as well, e.g.,
` 1 (0.5, 0, 0) 8`.

- **\<functions-Ylm-specs\>**: The angular character of the local
  functions on the specified sites.

Possible specifications are presented in the table below.

|       |            |         |         |         |         |           |            |
|-------|------------|---------|---------|---------|---------|-----------|------------|
| s     |            |         |         |         |         |           |            |
| p     | py         | pz      | px      |         |         |           |            |
| d     | dxy        | dyz     | dz2     | dxz     | dx2-y2  |           |            |
| f     | fy(3x2-y2) | fxyz    | fyz2    | fz3     | fxz2    | fz(x2-y2) | fx(x2-3y2) |
| sp    | sp-1       | sp-2    |         |         |         |           |            |
| sp2   | sp2-1      | sp2-2   | sp2-3   |         |         |           |            |
| sp3   | sp3-1      | sp3-2   | sp3-3   | sp3-4   |         |           |            |
| sp3d  | sp3d-1     | sp3d-2  | sp3d-3  | sp3d-4  | sp3d-5  |           |            |
| sp3d2 | sp3d2-1    | sp3d2-2 | sp3d2-3 | sp3d2-4 | sp3d2-5 | sp3d2-6   |            |

For more details, have a look at the section on [angular
functions](../misc/Angular_functions.md). These functions
are consistent with the definition of the *initial guesses* used by
<a href="http://www.wannier.org" class="external text"
rel="nofollow">WANNIER90</a> (see section 3.4 of the
<a href="http://www.wannier.org/doc/user_guide.pdf"
class="external text" rel="nofollow">WANNIER90 manual</a>).

It is possible to select multiple characters by creating a list
separated by spaces, e.g., `p sp-1 dxy` performs a projection for all
*p* functions (≡ *p*<sub>x</sub>, *p*<sub>y</sub>, and *p*<sub>z</sub>),
an *sp*-1 function, and a *d*<sub>xy</sub> function on all sites
specified by **\<sites\>**.

- **\<functions-radial-specs\>**: The radial dependency of the local
  functions.

There are three options:

**Pr**: use the PAW projectors

**Ps**: use the PAW pseudo partial waves

**Hy**: use hydrogen-like (Slater type) functions (see section 3.4 of
the <a href="http://www.wannier.org/doc/user_guide.pdf"
class="external text" rel="nofollow">WANNIER90 manual</a>)

|  |
|----|
| **Mind:** For **Pr** or **Ps**, which are radial functions derived from the PAW datasets, one can only specify spherical harmonics with *the same angular moment l* in the **\<functions-Ylm-specs\>** part. This means, *s*, *p*, *d*, *f*, and/or their respective separate constituents. |

The radial specifiers can optionally be modified using the following
modification statements:

**Pr** \[ *n<sup>th</sup>-of-l* \[ *species-number* \] \]

*n<sup>th</sup>-of-l*: Uses the radial function of the *n<sup>th</sup>*
projector with the angular moment specified in
**\<functions-Ylm-specs\>**. The local basis of our PAW datasets
typically contains 2 projectors per angular moment. By default, the
projector that corresponds to the highest bound state of the relevant
angular moment will be used.

*species-number*: Specifies from which PAW dataset in the current
[POTCAR](../input-files/POTCAR.md) file the radial functions should be
derived. When the positions of the local functions are specified using
the ionic site indices of the [POSCAR](../input-files/POSCAR.md) file, the
code will default to the corresponding atomic types.

  

**Ps** \[ *n<sup>th</sup>-of-l* \[ *species-number* \] \]

*n<sup>th</sup>-of-l*: Uses the radial function of the *n<sup>th</sup>*
pseudo partial wave with the angular moment specified in
**\<functions-Ylm-specs\>**. The local basis of our PAW datasets
typically contains 2 pseudo partial waves per angular moment. By
default, the pseudo partial wave that corresponds to the highest bound
state of the relevant angular moment is used.

*species-number*: Specifies from which PAW dataset in the current
[POTCAR](../input-files/POTCAR.md) file the radial functions should be
derived. When the positions of the local functions are specified using
the ionic site indices of the [POSCAR](../input-files/POSCAR.md) file, the
default is the corresponding atomic type.

  

**Hy** \[ *n* \[ *α* \] \]

*n*: Main quantum number of the hydrogen-like radial functions. Default:
*n=1*.

*α*: controls the diffusivity of the [radial
functions](../misc/Hydrogenic_radial_function.md)
( *α=Z/a<sub>0</sub>* in Å<sup>-1</sup>). Default: *α*=1.0
Å<sup>-1</sup>.

|  |  |
|----|----|
| $n$ | $R(r)$ |
| $1$ | $2\alpha^{3/2}\exp(-\alpha r)$ |
| $2$ | $\frac{1}{2\sqrt 2}\alpha^{3/2}(2-\alpha r)\exp(-\alpha r /2)$ |
| $3$ | ${\sqrt \frac{4}{27}}\alpha^{3/2}(1-2\alpha r/3+2\alpha^2 r^2/27)\exp(-\alpha r /3)$ |

*n*s type Hydrogen radial wave functions

This is consistent with the definition of the *initial guesses* used by
<a href="http://www.wannier.org" class="external text"
rel="nofollow">WANNIER90</a> (section 3.4 of the
<a href="http://www.wannier.org/doc/user_guide.pdf"
class="external text" rel="nofollow">WANNIER90 manual</a>).

  

|  |
|----|
| **Important:** Different projections have to be specified in multiple lines, as the LOCPROJ tag can only be set once. |

For instance,

    LOCPROJ = "1 : s : Hy 2
               1 3 : dxy : Ps 2 3"

performs the projection onto a hydrogen-like *2s* function and a
*d*<sub>xy</sub> pseudo partial wave (2<sup>nd</sup> *d* channel of
atomic species 3) on ionic site 1, and a *d*<sub>xy</sub> pseudo partial
wave (identical type) on site 3.

|  |
|----|
| **Deprecated:** For VASP versions \<= 6.1.x, multiple occurrences of the LOCPROJ tag are allowed and taken into account. |

For other tags, the second instance of a tag in the
[INCAR](../input-files/INCAR.md) is normally ignored. However, here

    LOCPROJ = 1 : s : Hy 2
    LOCPROJ = 1 3 : dxy : Ps 2 3

is possible.

## Example for LOCPROJ tag\[<a href="/wiki/index.php?title=LOCPROJ&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Example for LOCPROJ tag">edit</a> \| (./index.php.md)\]

As mentioned above, to put a hydrogen-like *1s* function on the first
ionic position specified in the [POSCAR](../input-files/POSCAR.md) file,
the tag reads

    LOCPROJ = 1 : s : Hy

in the [INCAR](../input-files/INCAR.md) file. To change this into a *2s*
function, specify

    LOCPROJ = 1 : s : Hy 2

To project the orbitals onto the PAW projectors of the valence atomic
*d*<sub>xy</sub>-states of the atoms on sites 1 and 3, write

    LOCPROJ = 1 3 : dxy : Pr

This will only work if the atoms on these sites have valence atomic
*d*-states. Otherwise, the necessary projectors will not be available in
the relevant PAW datasets, and the code will exit in error at startup.

To forcibly use the radial function of the second *d* channel, write

    LOCPROJ = 1 3 : dxy : Pr 2

Again, provided the PAW dataset(s) contain more than one *d* channel.
Similarly, one can project onto the pseudo partial waves of the second
*d* channel in the PAW dataset(s) by writing

    LOCPROJ = 1 3 : dxy : Ps 2

To project onto the functions of the third PAW dataset in the
[POTCAR](../input-files/POTCAR.md) file, specify

    LOCPROJ = 1 3 : dxy : Ps 2 3

## LOCPROJ file\[<a href="/wiki/index.php?title=LOCPROJ&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: LOCPROJ file">edit</a> \| (./index.php.md)\]

The LOCPROJ file contains
information about the projections of the Bloch states onto the localized
orbitals specified with the
LOCPROJ tag described above.

The file contains a header with the information about all projections:

- ISITE: Index of the site in the [POSCAR](../input-files/POSCAR.md) file.
- R: Position in fractional coordinates.
- Radial type: Is one of "PAW projector","PS partial wave",
  "Hydrogen-like" depending on the choice of **Pr**, **Ps** or **Hy**,
  respectively.
- Angular type: Angular character of the local functions, as presented
  in the table above in **\<functions-Ylm-specs\>**.

Each Kohn-Sham orbital is identified by the spin, k point, band index,
eigenvalue, and occupation. For each of these Kohn-Sham orbitals, VASP
writes the real and imaginary part of the projection onto localized
orbitals $\langle
\beta_{lm}^{\alpha}|S|\psi_{n\mathbf{k}}\rangle$.
Note that for **vasp_gam** only the real part exists.

## Related tags and articles\[<a href="/wiki/index.php?title=LOCPROJ&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LORBIT](LORBIT.md), [PROJCAR](PROJCAR.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-MYTAG-_incategory-Examples)

## References\[<a href="/wiki/index.php?title=LOCPROJ&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

  

------------------------------------------------------------------------


