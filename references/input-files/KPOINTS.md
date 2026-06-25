<!-- Source: https://vasp.at/wiki/index.php/KPOINTS | revid: 35974 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# KPOINTS


The KPOINTS file specifies the
Bloch vectors (**k** points) used to sample the Brillouin zone.
Converging this sampling is one of the essential tasks in many
calculations concerning the
<a href="/wiki/Electronic_minimization" class="mw-redirect"
title="Electronic minimization">electronic minimization</a>. A [regular
mesh](#regular-k-point-mesh) is the most common choice to select **k**
points:

    Regular 4 x 4 x 4 mesh centered at Gamma 
    0
    Gamma
    4 4 4

|  |
|----|
| **Tip:** Choose the number of points along each direction approximately inversely proportional to the corresponding length of the unit cell. |

A [band
structure](../categories/Category-Band_structure.md) is
often visualized along high-symmetry paths. Some external
tools[^bilbao:kvec-1][^seekpath-2]
help to identify these points for materials of any symmetry. Use the
template below to setup [band-structure
calculations](#band-structure-calculations). Alternatively, use a
[KPOINTS_OPT](KPOINTS_OPT.md) file to get the band
structure as a postprocessing step after the regular calculation.

    k points along high symmetry lines
     40              ! number of points per line
    line mode
    fractional
      0    0    0    Γ
      0.5  0.5  0    X

      0.5  0.5  0    X
      0.5  0.75 0.25 W

      0.5  0.75 0.25 W
      0    0    0    Γ

|  |
|----|
| **Tip:** If the KPOINTS file is not present, the tag [KSPACING](../incar-tags/KSPACING.md) determines the **k**-point sampling. Use that option for a quick first run but prefer generating a [regular mesh](#regular-k-point-mesh) for production calculations. |


## Contents


- [1 Coordinate
  system](#coordinate-system)
- [2 Explicit
  **k**-point mesh](#explicit-k-point-mesh)
- [3 Regular
  **k**-point mesh](#regular-k-point-mesh)
- [4 Symmetry
  reduction of the mesh](#symmetry-reduction-of-the-mesh)
- [5 Generalized
  regular meshes](#generalized-regular-meshes)
- [6 Band-structure
  calculations](#band-structure-calculations)
- [7 Automatic
  **k**-point mesh](#automatic-k-point-mesh)
- [8 Related tags
  and sections](#related-tags-and-sections)
- [9
  References](#references)


## Coordinate system\[<a href="/wiki/index.php?title=KPOINTS&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Coordinate system">edit</a> \| (./index.php.md)\]

When specifying coordinates in the
KPOINTS file, use one of the
following coordinate systems:

Fractional coordinate system  
The **k** points are linear combinations of the reciprocal lattice
vectors ${\mathbf b}_{1\ldots3}$

${\mathbf k} = x_1 {\mathbf b}_1 + x_2 {\mathbf b}_2 + x_3 {\mathbf
b}_3~.$

Use the factors $x_{1\ldots3}$ as the coordinates in
KPOINTS.

Cartesian coordinate system  
The coordinates $x_{1\ldots3}$ directly correspond to the **k** point

${\mathbf k} =\frac{2 \pi}{a} (x_1, x_2 , x_3)~.$

up to the scaling factor $2\pi / a$.
Here, $a$ is the
scaling parameter specified on the second line of the
[POSCAR](POSCAR.md) file.

**Example: face-centered-cubic (fcc) lattice**

The following lattice vectors $\mathbf a_i$
span the unit cell:

$\mathbf a_1 = a \begin{pmatrix} 0 \\ 1/2 \\ 1/2\end{pmatrix} \qquad
\mathbf a_2 = a \begin{pmatrix} 1/2 \\ 0 \\ 1/2\end{pmatrix} \qquad
\mathbf a_3 = a \begin{pmatrix} 1/2 \\ 1/2 \\ 0\end{pmatrix}$

The corresponding reciprocal lattice vectors $\mathbf b_i$
are

$\mathbf b_1 = \frac{2 \pi}{a} \begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}
\qquad \mathbf b_2 = \frac{2 \pi}{a} \begin{pmatrix} 1 \\ -1 \\ 1
\end{pmatrix} \qquad \mathbf b_3 = \frac{2 \pi}{a} \begin{pmatrix} 1 \\
1 \\ -1 \end{pmatrix}~.$

The following table shows several high-symmetry points of the fcc
lattice expressed in Cartesian and fractional coordinates, respectively:

    Point     Cartesian coordinates     Fractional coordinates
                (units of 2pi/a)         (units of b1,b2,b3)
    ----------------------------------------------------------
      Γ         (  0    0    0  )         (  0    0    0  )
      X         (  0    0    1  )         ( 1/2  1/2   0  )
      W         ( 1/2   0    1  )         ( 1/2  3/4  1/4 )
      K         ( 3/4  3/4   0  )         ( 3/8  3/8  3/4 )
      L         ( 1/2  1/2  1/2 )         ( 1/2  1/2  1/2 )

## Explicit **k**-point mesh\[<a href="/wiki/index.php?title=KPOINTS&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Explicit k-point mesh">edit</a> \| (./index.php.md)\]

When an explicit **k**-point mesh is provided, VASP uses exactly the
provided points. The primary use case of this mode is to look at
particular features in the band structure, e.g., for effective mass
calculations. For [regular meshes](#Regular_regular_k-point_mesh) and
[band structures](#band-structure-calculations), we recommend using the
automatic generation to avoid mistakes. Nevertheless, all other modes
write the processed input in this format to the
[IBZKPT](../output-files/IBZKPT.md) file, so understanding this format helps
analyze mistakes in setting up the
KPOINTS file. A typical
example has the following format:

    Explicit k-point list
    4
    Cartesian
    0.0  0.0  0.0   1
    0.0  0.0  0.5   1
    0.0  0.5  0.5   2
    0.5  0.5  0.5   4

- The first line is treated as a
  comment line.
- Provide the number of **k**
  points on the second line.
- The first character on the third line specifies the [coordinate
  system](#coordinate-system). Use *C*,
  *c*, *K*, or *k* to indicate Cartesian coordinates. Any other
  character is interpreted as fractional/reciprocal coordinates
  but we advise writing *fractional* or *reciprocal* to make this clear.
- Each following line contains the
  coordinates and weight of one **k**
  point. VASP takes care that weights are properly normalized so
  only relative weight is important. Typically the weights correspond to
  the symmetry degeneracy of a **k** point.

Use the explicit mode for

- a (small) number of **k** points not forming a regular mesh.
- the calculation of band structure when [the line
  mode](#band-structure-calculations) is not suitable (example: [hybrid
  functionals](../misc/Si_bandstructure.md)).
- the irreducible part of the <a href="#generalized_regular_meshes"
  class="mw-selflink-fragment">genereralized regular meshes</a>
  generated for a particular target sampling
  density.[^wisesa:prb:2016-3][^morgan:cms:2020-4]
  Generate the corresponding
  KPOINTS files with
  KpLib[^kplib-5]
  or
  autoGR[^auto_gr-6].

**Tetrahedron method**

When using the tetrahedron method (see [ISMEAR](../incar-tags/ISMEAR.md)),
extend the list of **k** points by a list of all tetrahedra.

    Explicit k-point list
    4
    Cartesian
    0.0  0.0  0.0   1
    0.0  0.0  0.5   1
    0.0  0.5  0.5   2
    0.5  0.5  0.5   4
    Tetrahedra
    1  0.183333333333333
    6    1 2 3 4

The line following the list of **k** point coordinates and weights must
start with 'T' or 't'. On the next line, enter the number of tetrahedra
and the volume weight common to all the tetrahedra. The volume weight is
simply the ratio between the volume of a tetrahedron and the volume of
the first Brillouin zone.

Subsequently, list the symmetry-degeneration weight and the four corner
points of each tetrahedron. The four integers represent the indices of
the corners of the tetrahedron in the **k**-point list given above.
Here, the counter starts at 1 and corresponds to the **k** point
specified in the fourth line.

|  |
|----|
| **Warning:** VASP does not renormalize the weights of the tetrahedra. Make sure they are appropriately normalized. |

|  |
|----|
| **Important:** Explicitly listing all the **k** points is not very convenient, especially in the context of the tetrahedron method. Keep in mind that the automatic modes generate the [IBZKPT](../output-files/IBZKPT.md) file in this format. For any nontrivial case, preferably modify an automatically-generated [IBZKPT](../output-files/IBZKPT.md) instead of building an explicit list from scratch. |

## Regular **k**-point mesh\[<a href="/wiki/index.php?title=KPOINTS&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Regular k-point mesh">edit</a> \| (./index.php.md)\]

This mode will automatically generate a mesh where each lattice vector
is subdivided into an explicitly defined number of subdivisions. It
offers sufficient flexibility and stability and should be preferred for
most production calculations. Choose the number of subdivisions
$N_1$, $N_2$ and
$N_3$ in the
KPOINTS file like this

    Regular k-point mesh
    0              ! 0 -> determine number of k points automatically
    Gamma          ! generate a Gamma centered mesh
    4  4  4        ! subdivisions N_1, N_2 and N_3 along the reciprocal lattice vectors
    0  0  0        ! optional shift of the mesh (s_1, s_2, s_3)

- The first line is a comment
  line.
- In the second line, set the number of **k** points to
  0 to indicate an automatic mesh
  generation.
- The first nonblank character of the third line determines the center
  of the mesh. The possible choice are
  Γ-centered (*G*, *g*) or the Monkhorst-Pack scheme (*M*,
  *m*).[^monkhorst:prb:1976-7]
- Specify the desired number of
  subdivisions
  $N_1$, $N_2$ and
  $N_3$ in the fourth line.
- Optionally add a fifth line to
  shift the mesh by
  $(s_1, s_2, s_3)$ with respect to the default.

Γ-centered mesh  
The following **k** points sample the Brillouin zone

${\mathbf k} = \sum_{i = 1}^3 \frac{n_i+s_i}{N_i} {\mathbf b}_i \qquad
\forall {n_i \in \[0, N_i\[}$

<!-- -->

Monkhorst-Pack mesh  
The **k** point mesh results from this definition

${\mathbf k} = \sum_{i = 1}^3 \frac{n_i+s_i+\frac{1-N_i}{2}}{N_i}
{\mathbf b}_i \qquad \forall {n_i \in \[0, N_i\[}$

The spacing between the points is the same for both meshes. The only
difference is the shift $(1-N_i)/2$ in
the numerator of the Monkhorst-Pack mesh. For an odd number of
subdivisions, this term is an integer, and therefore the two meshes
agree due to periodic boundaries. When the number of subdivisions is
even the Γ-centered mesh is shifted by $s_i = 1/2$
compared to the Monkhorst-Pack one.

|  |
|----|
| **Important:** Monkhorst-Pack meshes may converge faster than the Γ-centered ones. However, carefully read the <a href="#Symmetry_reduction_of_the_mesh"
class="mw-selflink-fragment">section on symmetry considerations</a> to avoid breaking the symmetry with a Monkhorst-Pack mesh. |

**Guidelines for the choice of the subdivisions**

As a rule of thumb, choose $N_1$,
$N_2$, and $N_3$ such
that

$N_1 : N_2 : N_3 \approx |\mathbf b_1| : |\mathbf b_2| : |\mathbf
b_3|~.$

This guideline is also implemented for the automatic **k**-point
generation using [KSPACING](../incar-tags/KSPACING.md). Nevertheless,
specifying the $N_1$,
$N_2$, and $N_3$ manually
ensures that changes in the lattice vectors do not affect the
**k**-point mesh. When the primitive cell has (nearly) perpendicular
axes (cubic, tetragonal, orthorhombic), this is equivalent to:

$N_1 : N_2 : N_3 \approx \frac{1}{|\mathbf a_1|} : \frac{1}{|\mathbf
a_2|} : \frac{1}{|\mathbf a_3|}~.$

Of course, this only provides a guide for the ratios between the
subsections. The actual density of the **k** point mesh has to be
increased until some relevant output quantity of the calculation is
converged.

## Symmetry reduction of the mesh\[<a href="/wiki/index.php?title=KPOINTS&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Symmetry reduction of the mesh">edit</a> \| (./index.php.md)\]

VASP determines the [symmetry of the
system](../categories/Category-Symmetry.md). For
[ISYM](../incar-tags/ISYM.md) $\ge$ 0, the
automatically generated **k**-point meshes are reduced to the
irreducible subset. Every **k** point acquires a weight following their
symmetry multiplicity. This can significantly reduce the total number of
**k** points.

|  |
|----|
| **Important:** To enable an efficient symmetry reduction, the (shifted) regular mesh of **k** points should conserve the point-group symmetry of the reciprocal lattice. Specifically, the generating lattice ($\mathbf g_i = \mathbf k_i / N_i$) should belong to the same class of Bravais lattice as the reciprocal lattice. |

Consequently, refrain from using a shifted regular mesh for some Bravais
lattices, see table. Importantly, this includes the default
Monkhorst-Pack mesh for even numbers of subdivisions. Furthermore, the
reciprocal lattice vectors do not in general align with lattice vectors.
There is typically a difference in the subdivisions obtained from the
inverse of the lattice vectors or the reciprocal lattice vectors.

$\frac{1}{|\mathbf a_1|} : \frac{1}{|\mathbf a_2|} :
\frac{1}{|\mathbf a_3|} \neq |\mathbf b_1| : |\mathbf b_2| :
|\mathbf b_3| \qquad \text{in general}$

In some special cases, the two options are equal, e.g., when the length
of all vectors is the same, or they are mutually perpendicular.
Unfortunately, either choice yields incompatible **k** point meshes for
some of the Bravais lattices. Consult the table below to make an
informed choice depending on the symmetry of the system.

|  |  |  |  |
|----|----|----|----|
| Bravais lattice | variant | mesh choices | subsection choices |
| triclinic | primitive | $\Gamma$-centered, Monkhorst Pack | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$, $|\mathbf b_1| : |\mathbf b_2| : |\mathbf b_3|$ |
| monoclinic | primitive | $\Gamma$-centered, Monkhorst Pack | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$, $|\mathbf b_1| : |\mathbf b_2| : |\mathbf b_3|$ |
|  | base-centered | $\Gamma$-centered, Monkhorst Pack | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$, $|\mathbf b_1| : |\mathbf b_2| : |\mathbf b_3|$ |
| orthorhombic | primitive | $\Gamma$-centered, Monkhorst Pack | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$, $|\mathbf b_1| : |\mathbf b_2| : |\mathbf b_3|$ |
|  | base-centered | $\Gamma$-centered, Monkhorst Pack | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$, $|\mathbf b_1| : |\mathbf b_2| : |\mathbf b_3|$ |
|  | body-centered | $\Gamma$-centered, Monkhorst Pack | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$ |
|  | face-centered | $\Gamma$-centered | $|\mathbf b_1| : |\mathbf b_2| : |\mathbf b_3|$ |
| tetragonal | primitive | $\Gamma$-centered, Monkhorst Pack | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$, $|\mathbf b_1| : |\mathbf b_2| : |\mathbf b_3|$ |
|  | body-centered | $\Gamma$-centered, Monkhorst Pack | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$ |
| hexagonal | rhombohedral | $\Gamma$-centered | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$, $|\mathbf b_1| : |\mathbf b_2| : |\mathbf b_3|$ |
|  | hexagonal | $\Gamma$-centered | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$, $|\mathbf b_1| : |\mathbf b_2| : |\mathbf b_3|$ |
| cubic | primitive | $\Gamma$-centered, Monkhorst Pack | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$, $|\mathbf b_1| : |\mathbf b_2| : |\mathbf b_3|$ |
|  | body-centered | $\Gamma$-centered, Monkhorst Pack | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$, $|\mathbf b_1| : |\mathbf b_2| : |\mathbf b_3|$ |
|  | face-centered | $\Gamma$-centered | $|\mathbf a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$, $|\mathbf b_1| : |\mathbf b_2| : |\mathbf b_3|$ |

|  |
|----|
| **Tip:** VASP issues an error when it detects an incompatible **k**-point mesh. The specific error message depends on the particular setup but includes the name of the routine *IBZKPT*, some warning about the *generating k-lattice*, and some suggestions to overcome the problem. |

Summarizing the information in the table above

- Use **only** $\Gamma$-centered meshes for face-centered cubic (fcc),
  hexagonal, and fcc-orthorhombic crystalline lattices.
- Choose the ratios of the subdivisions $N_1 : N_2 : N_3 = |\mathbf
  a_1|^{-1} : |\mathbf a_2|^{-1} : |\mathbf a_3|^{-1}$ for *body-centered tetragonal* and *body-centered
  orthorhombic* lattices. Keep in mind that the
  [KSPACING](../incar-tags/KSPACING.md) uses the reciprocal lattice
  vectors so may not be suitable for these symmetries.
- For *face-centered orthorhombic* crystal structures, choose
  subdivisions according to $N_1 : N_2 : N_3 = |\mathbf
  b_1| : |\mathbf b_2| : |\mathbf b_3|$.
- For any other symmetry, all combinations should work but a change to
  other subdivisions or meshes may overcome possible issues.

Solve problems with the primitive cells of the body-centered tetragonal
and body/face-centered orthorhombic Bravais lattices with one of these
options:

1.  Choose $N_1=N_2=N_3$. For $N \times N \times N$ Monkhorst-Pack meshes the reciprocal lattice is
    always of the same Bravais lattice as the generating lattice. For
    body-centered tetragonal and face-centered orthorhombic primitive
    cells, the reciprocal lattices are body-centered tetragonal and
    body-centered orthorhombic, respectively. Therefore, choosing equal
    subdivisions is justified because the length of all reciprocal
    lattice vectors is the same $|\mathbf b_1|=|\mathbf
    b_2|=|\mathbf b_3|$.
2.  A simple but computationally-expensive option is to change to the
    conventional cell of the structure. For the body-centered
    tetragonal/orthorhombic structure, the conventional cell is two
    times bigger than the primitive cell.
3.  Alternatively, define the **k**-point mesh for the conventional
    cell. This approach requires a <a href="#Generalized_regular_meshes"
    class="mw-selflink-fragment">generalized regular mesh</a> introduced
    in the next section and is demonstrated for the example of a
    body-centered orthorhombic lattice.

## Generalized regular meshes\[<a href="/wiki/index.php?title=KPOINTS&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Generalized regular meshes">edit</a> \| (./index.php.md)\]

When more control about the generated mesh is desired, one can specify
the generating vectors explicitly. A typical use case would be to
generate the mesh for the *conventional* unit cell and apply it to the
*primitive* one. Build a
KPOINTS file for this mode
starting from this template

    Automatic generation
    0
    Cartesian
    0.25 0.00 0.00
    0.00 0.25 0.00
    0.00 0.00 0.25
    0.00 0.00 0.00

The mode is activated by specifying the [coordinate
system](#coordinate-system) with the first nonblank character in line 3.
A *C*, *c*, *K* or *k* character determines that the generating basis
vectors are in Cartesian coordinates. Use *r* or *R* to select the
reciprocal coordinate system instead. The latter is also the default
used if VASP cannot interpret the provided character but we recommend
not relying on this behavior. Otherwise, the introduction of further
automatic modes in the future versions of VASP may change the
interpretation of the KPOINTS
file.

VASP generates three vectors $\mathbf g_1$,
$\mathbf g_2$, and $\mathbf g_3$
from the coefficients $x_i$ given in
line 4–6. Depending on the selected [coordinate
system](#coordinate-system) these vectors are either multiples of the
reciprocal lattice vectors $\mathbf b_i$
(reciprocal) or simply multiplying the coefficients by
$2\pi/a$ (Cartesian). Here $a$ is the
scaling parameter you have specified on the second line of the
[POSCAR](POSCAR.md) file.

|  |
|----|
| **Important:** The generating vectors $\mathbf g_1$, $\mathbf g_2$, and $\mathbf g_3$ must be commensurate with the reciprocal lattice. This means $\mathbf b_i = \textstyle \sum_{j} M_{ij} \mathbf g_j$ where the matrix $M$ contains only integer entries. If this is not the case the code will exit in error. |

Combined with the shift ($s_1$,
$s_2$, $s_3$)
specified in the last line, VASP uses the generating vectors
$\mathbf g_i$ to construct the **k**-point mesh

${\mathbf k} = \sum_i {\mathbf g}_i (n_i + s_i) \qquad n_i \in \[0,
N_i\[$

where VASP chooses the $N_i$ to
include all possible points of the generating mesh in the first
Brillouin zone.

The [regular **k**-point meshes](#regular-k-point-mesh) are a subset of
the generalized regular meshes, for which

$\mathbf g_i = \mathbf b_i / N_i~.$

Here, the generating lattice vectors are integer subdivisions of the
reciprocal lattice vectors according to the $N_i$ defined
in the KPOINTS file.

For instance, the generalized regular mesh given by

    Automatic generation
    0
    Reciprocal
     0.25 0.00 0.00
     0.00 0.25 0.00
     0.00 0.00 0.25
     0.50 0.50 0.50

is equivalent to the Monkhorst-Pack mesh specified by

    Automatic generation
    0
    Monkhorst-pack
     4 4 4
     0 0 0

  
A typical use-case for generalized regular meshes is to generate a
**k**-point mesh based on the *conventional* cell of a particular
Bravais lattice to be used with the *primitive* cell of that lattice
(see the [subsection on symmetry
considerations](#symmetry-reduction-of-the-mesh)). As an example,
consider the primitive cell of a *body-centered orthorhombic* lattice:

$A
= a \left( \begin{array}{rrr} -1/2 & b/2a & c/2a \\ 1/2 & -b/2a & c/2a
\\ 1/2 & b/2a & -c/2a \\ \end{array} \right)$

where the rows of $A$ represent
the lattice vector of the primitive cell. The corresponding conventional
cell is given by

$A
= a \left( \begin{array}{rrr} 1 & 0 & 0 \\ 0 & b/a & 0 \\ 0 & 0 & c/a \\
\end{array} \right)$

and its reciprocal lattice by

$B
= \frac{2\pi}{a} \left( \begin{array}{rrr} 1 & 0 & 0 \\ 0 & a/b & 0 \\ 0
& 0 & a/c \\ \end{array} \right)~.$

Then the following generating lattice based on the reciprocal lattice of
the conventional cell

$G
= \frac{2\pi}{a} \left( \begin{array}{rrr} 1/N_1 & 0 & 0 \\ 0 & a/bN_2 &
0 \\ 0 & 0 & a/cN_3 \\ \end{array} \right)$

yields a roughly uniform sampling of the Brillouin zone when
$N_1$, $N_2$, and
$N_3$ are chosen such that:

$N_1 : N_2 : N_3 \approx 1 : \frac{a}{b} : \frac{a}{c}$

For instance, for a body-centered orthorhombic primitive cell with
$a=5, \\ b/a=1.2 \\ c/a=0.5$, here given in
[POSCAR](POSCAR.md) file format:

    body-centered orthorhombic primitive cell
    5.0
    -0.500000  0.600000  0.250000
     0.500000 -0.600000  0.250000
     0.500000  0.600000 -0.250000
    1
    direct
    0.000000 0.000000 0.000000

this following KPOINTS file

    Generalized regular mesh
    0
    Cartesian
     0.50000000  0.00000000  0.00000000
     0.00000000  0.41666667  0.00000000
     0.00000000  0.00000000  0.50000000
     0.00000000  0.00000000  0.00000000

corresponds to the aforementioned generating lattice for
$N_1=2$, $N_2=2$, and
$N_3=4$.

Furthermore, using generalized regular meshes potentially requires fewer
**k** points compared to Monkhorst-Pack meshes to converge total energy
calculations.[^wisesa:prb:2016-3][^morgan:cms:2020-4]
Specifically this statement applies to the number of **k** points in the
irreducible part of the Brillouin zone after symmetry reduction. For the
moment, however, VASP does not automatically construct optimal
generalized regular **k**-point meshes. But external
tools[^kplib-5][^auto_gr-6]
construct meshes with certain target sampling density in the spirit of
the aforementioned publications.

## Band-structure calculations\[<a href="/wiki/index.php?title=KPOINTS&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Band-structure calculations">edit</a> \| (./index.php.md)\]

When properties depend on the **k** vector, it is often convenient to
visualize the property along high-symmetry lines. The line mode
generates **k** points between user-defined points in the Brillouin
zone. The most common use case is analyzing the electronic band
structure.

|  |
|----|
| **Warning:** The mesh generated by this mode is not suitable for self-consistent calculations. Please set [ICHARG](../incar-tags/ICHARG.md) = 11 to avoid updating the density. |

|  |
|----|
| **Mind:** For meta-GGA and hybrid functionals, a regular mesh must always be provided. Refer to [band-structure calculations using meta-GGA functionals](../methods/Band-structure_calculation_using_meta-GGA_functionals.md) *or* [using hybrid functionals](../methods/Band-structure_calculation_using_hybrid_functionals.md), respectively. |

Build the KPOINTS based on
this template

    k points along high symmetry lines
     40              ! number of points per line
    line mode
    fractional
      0    0    0    Γ
      0.5  0.5  0    X

      0.5  0.5  0    X
      0.5  0.75 0.25 W

      0.5  0.75 0.25 W
      0    0    0    Γ

- The first line is a comment
  line.
- Specify the number of points per line
  segment on the second line.
- The line mode activates when the first nonblank character on the third
  line is an *L* or *l* (for *line
  mode*)
- The fourth line defines the [coordinate system](#coordinate-system).
  Use Cartesian (*C*, *c*, *K*, or *k*)
  or fractional (any other character) coordinates.
- Afterwards, any pair of lines define one
  path through the Brillouin
  zone. The empty lines and the label of the high-symmetry points
  are not required but simplify understanding the
  KPOINTS file.
  <a href="https://vasp.at/py4vasp/latest/index.html"
  class="external text" rel="nofollow">py4vasp</a> uses the labels for
  the band structure plots.

The generated **k**-point mesh depends on the selected [coordinate
system](#coordinate-system). VASP produces equidistant **k** points for
each segment such that the total of points including the endpoints
equals the required number. Specifically for the template above, 40
points from $\Gamma$ to X,
40 points from X to W, and 40 points from W to
$\Gamma$. Because the endpoints are included every time,
this generates two X and W points.

Transforming the same template to Cartesian coordinates produces

    k points along high symmetry lines
     40              ! number of points per line
    line mode
    Cartesian
      0   0   0   Γ
      0   0   1   X

      0   0   1   X
      0.5 0   1   W

      0.5 0   1   W
      0   0   1   Γ

External
tools[^bilbao:kvec-1][^seekpath-2]
are useful to decide which paths in the Brillouin zone to include. The
tools provide the coordinates and the labels for a given structure.
Because these paths depend on the symmetry, take special care that the
analysis is not tainted by finite precision or rounding. Also, keep in
mind that the primitive and the conventional unit cell have different
reciprocal coordinate systems.

Here is an example of a hexagonal structure

    k-points along high symmetry lines for hexagonal structure
     40
    line
    reciprocal
    0.000    0.000    0.500  A
    0.000    0.000    0.000  Gamma

    0.000    0.000    0.000  Gamma 
    0.500    0.000    0.000  M

    0.500    0.000    0.000  M
    0.333333 0.333333 0.000  K 

    0.333333 0.333333 0.000  K
    0.000    0.000    0.000  Gamma

<table class="vasp-dark-link-panel"
style="border: 0px solid var(--vcyan); --box-emph-color: var(--vcyan); padding: 5px; color: var(--vdefault-text-nb); background: var(--vcyan-bg)">
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td><strong><span style="color: var(--vcyan);">Mind:</span></strong> The
primary use of this particular mode of <strong>k</strong>-point
generation is the calculation of DFT band structures. Because the mesh
does not yield a good electronic density, it should only be used on a
converged density. Therefore, run a calculation using a <a
href="#Regular_k-point_mesh">regular <strong>k</strong>-point mesh</a>
first. Freeze this density by setting <a href="/wiki/ICHARG"
title="ICHARG">ICHARG</a> = 11 and run a non-self-consistent calculation
with the line-mode <strong>k</strong>-point mesh afterward.
<p>As of VASP.6.3, the <a href="/wiki/KPOINTS_OPT"
title="KPOINTS OPT">KPOINTS_OPT</a> file runs these two steps in a
single calculation. It uses the same format and its presence triggers
the postprocessing step. Use it for band-structure calculations with
hybrid functionals to avoid the more cumbersome <a
href="/wiki/Si_bandstructure" title="Si bandstructure">manual
specification</a>.</p></td>
</tr>
</tbody>
</table>

## Automatic **k**-point mesh\[<a href="/wiki/index.php?title=KPOINTS&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Automatic k-point mesh">edit</a> \| (./index.php.md)\]

|  |
|----|
| **Deprecated:** The [KSPACING](../incar-tags/KSPACING.md) tag provides almost the same functionality. Preferably use that method instead. |

The following KPOINTS file
generates a regular $\Gamma$-centered **k**-point. The subdivisions
$N_1$, $N_2$, and
$N_3$ are along the reciprocal lattice vectors
$\mathbf b_1$, $\mathbf b_2$,
and $\mathbf b_3$,
respectively.

    Fully automatic mesh
    0              ! 0 -> automatic generation scheme 
    Auto           ! fully automatic
      10           ! length (R_k)

- The first line is a comment
  line.
- Automatically determine the
  number of **k** points by setting
  '0' on the second line.
- The first nonblank character in the third line is
  *A* or *a* activating the
  fully-automatic mode.
- The fourth line defines a length
  ($R_k$) that determines the subdivisions
  $N_1$, $N_2$, and
  $N_3$.

For every lattice vector $\mathbf b_i$
the number of subdivisions is calculated as

$N_i = \text{int}\left(\max(1, R_k |{\mathbf b}_i| + 0.5)\right)~.$

Note that this similar to the [KSPACING](../incar-tags/KSPACING.md) tag,
when the length $R_k = 2\pi/\text{KSPACING}$. The generated mesh is centered at
$\Gamma$

${\mathbf k} = \sum_{i=1}^3 {\mathbf b}_i \frac{n_i}{N_i} \qquad
\forall n_i \in \[0, N_i\[$

Useful values for the length vary between $R_k = 10$
(large gap insulators) and $R_k = 100$
(*d* metals). Please verify that changes to $R_k$ do not
affect the quantity of interest. For production calculations, preferably
specify the mesh dimensions explicitly to avoid discontinuities between
different cell sizes.

## Related tags and sections\[<a href="/wiki/index.php?title=KPOINTS&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[KSPACING](../incar-tags/KSPACING.md),
[KPOINTS_OPT](KPOINTS_OPT.md),
[IBZKPT](../output-files/IBZKPT.md), [Number of k points and method for
smearing](../misc/Number_of_k_points_and_method_for_smearing.md)

## References\[<a href="/wiki/index.php?title=KPOINTS&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^bilbao:kvec-1]: [www.cryst.ehu.es/cryst/get_kvec.html (2022).](https://www.cryst.ehu.es/cryst/get_kvec.html)
[^seekpath-2]: [www.materialscloud.org/work/tools/seekpath (2022).](https://www.materialscloud.org/work/tools/seekpath)
[^wisesa:prb:2016-3]: [P. Wisesa, K.A. McGill, and T. Mueller, Phys. Rev. B **93**, 155109 (2016).](https://doi.org/10.1103/PhysRevB.93.155109)
[^morgan:cms:2020-4]: [W.S. Morgan, J.E. Christensen, P.K. Hamilton, J.J. Jorgensen, B.J. Campbell, G.L.W. Hart, and R.W. Forcade, Comput. Mater. Sci. **173**, 109340 (2020).](https://doi.org/10.1016/j.commatsci.2019.109340)
[^kplib-5]: [https://muellergroup.jhu.edu/K-Points.html (2022).](https://muellergroup.jhu.edu/K-Points.html)
[^auto_gr-6]: [https://github.com/msg-byu/autoGR (2022).](https://github.com/msg-byu/autoGR)
[^monkhorst:prb:1976-7]: [H.J. Monkhorst and J.D. Pack, Phys. Rev. B **13**, 5188 (1976).](https://doi.org/10.1103/PhysRevB.13.5188)
