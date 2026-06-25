<!-- Source: https://vasp.at/wiki/index.php/NUCIND | revid: 34906 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NUCIND


NUCIND = .TRUE. \| .FALSE.  
Default: **NUCIND** = .FALSE. 

Description: Allows the nucleus-independent chemical shielding (NICS) to
be calculated.

|  |
|----|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

In conjunction with [`LCHIMAG`](LCHIMAG.md)` = True`,
NUCIND calculates the chemical
shielding tensor $\sigma_{ij}(\mathbf{R})$ at positions $\textbf{R}$
off-nucleus, hence nucleus-independent chemical shielding (NICS)
<sup>[\[1\]](#cite_note-schleyer:1996-1)[\[2\]](#cite_note-chen:schleyer:2005-2)</sup>.
VASP calculates only from the plane wave grid, there is no one-center
augmentation.

When `NUCIND`` = True`, by
default these are calculated on the fine FFT grid
[NGXF](NGXF.md) x [NGYF](NGYF.md) x
[NGZF](NGZF.md) in ppm. The output is written to
[NICS](NICS.md).

It is also written to [vaspout.h5](../output-files/Vaspout.h5.md), if
compiled with [HDF5
support](../misc/Makefile.include.md). You can
find the data groups:

    /results/nics            Group
    /results/nics/grid       Dataset {3}
    /results/nics/structure  Group
    /results/nics/structure/position Group
    /results/nics/structure/position/direct_coordinates Dataset {SCALAR}
    /results/nics/structure/position/ion_sha256 Dataset {2}
    /results/nics/structure/position/ion_types Dataset {2}
    /results/nics/structure/position/lattice_vectors Dataset {3, 3}
    /results/nics/structure/position/number_ion_types Dataset {2}
    /results/nics/structure/position/position_ions Dataset {8, 3}
    /results/nics/structure/position/scale Dataset {SCALAR}
    /results/nics/structure/position/system Dataset {SCALAR}
    /results/nics/values     Dataset {9, 108, 108, 108}

and use <a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> to access these, e.g.,
using


    import py4vasp as pv
    calc = pv.Calculation.from_path(".")
    calc.nics.plot()


to select the isotropic chemical shielding $\sigma_{iso}$ in 3D space
<sup>[\[3\]](#cite_note-klod:kleinpeter:2001-3)[\[4\]](#cite_note-kleinpeter:klod:koch:2007-4)</sup>.
It will produce an isosurface of the shielding (positive) and
deshielding (negative) over the crystal structure.

Alternatively, produce a 2D contour plot of the NICS in a plane
<sup>[\[5\]](#cite_note-karadakov:horner:2013-5)</sup>:


    import py4vasp as pv
    calc = pv.Calculation.from_path(".")
    calc.nics.to_contour(a=0.5)


It will result in a contour plot showing the isotropic chemical
shielding $\sigma_{iso}$ in the selected plane. The plane is selected as a
fraction `x` of the lattice vector. Here, `x=0.5` corresponds to half of
the primary lattice vector $\mathbf{a}$.
For the other lattice vectors use `b=x` or `c=x`.

For both the 2D and 3D plots, the isotropic chemical shielding is used
by default. You can alternatively select the other properties (see
[LCHIMAG](LCHIMAG.md) for details. Herzfeld-Berger
convention is followed
<sup>[\[6\]](#cite_note-mason:ssn:1993-6)</sup>)
by inputting them as arguments into the functions, e.g.,
`calc.nics.plot("anisotropic")` or
`calc.nics.to_contour("span", a=0.5)`:

- `"isotropic"` (default) - plot the isotropic chemical shielding
  $\sigma_{iso}$
- `"anisotropic"` - plot the anisotropic chemical shielding
  $\sigma_{ani}$
- `"span"` - plots the span $\Omega$
- `"skew"` - plot the skew $\kappa$

## POSNICS\[<a href="/wiki/index.php?title=NUCIND&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: POSNICS">edit</a> \| (./index.php.md)\]

Alternatively, if the [POSNICS](POSNICS.md) file is
present, then the positions defined within that file will be used. The
calculation takes longer as each point is calculated in serial and not
in parallel as for the grid. However, there is far greater flexibility
for defining physically relevant positions, e.g., hydrogen bonds, close
to nuclei, or chemical bonds. These chemical shielding tensors are
printed in the [OUTCAR](../output-files/OUTCAR.md) file as follows, e.g.,
for the 100th NICS point:

     nics 100
              1.187143         -0.003408         -0.000000
             -0.002977         -1.893648         -0.000000
             -0.000000         -0.000000         -0.326272

It is also written to [vaspout.h5](../output-files/Vaspout.h5.md), if
compiled with [HDF5
support](../misc/Makefile.include.md). You can
find the data groups:

    /results/posnics         Group
    /results/posnics/label   Dataset {SCALAR}
    /results/posnics/positions Dataset {3, 10000}
    /results/posnics/values  Dataset {10000, 3, 3}

and use <a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> to access these, e.g.,
using


    import py4vasp as pv
    calc = pv.Calculation.from_path(".")
    calc.nics.read()


to read the NICS values for the positions defined in
[POSNICS](POSNICS.md). Since the grid is not necessarily
regular, you will need to plot these yourself.

## Related tags and articles\[<a href="/wiki/index.php?title=NUCIND&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[LCHIMAG](LCHIMAG.md), [NICS](NICS.md),
[LNICSALL](LNICSALL.md),
[LPOSNICS](LPOSNICS.md),
[POSNICS](POSNICS.md)

<a href="https://www.vasp.at/tutorials/latest/nmr/part3/#NMR-e09"
class="external text" rel="nofollow">LPOSNICS tutorial</a>,
<a href="https://www.vasp.at/tutorials/latest/nmr/part3/#NMR-e11"
class="external text" rel="nofollow">LNICSALL tutorial</a>

## References\[<a href="/wiki/index.php?title=NUCIND&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-schleyer:1996_1-0)
    <a href="https://doi.org/10.1021/ja960582d" class="external text"
    rel="nofollow">P. von Ragué Schleyer, C. Maerker, A. Dransfeld, H. Jiao,
    and N. J. R. van Eikema Hommes, <em>Nucleus-Independent Chemical
    Shifts:  A Simple and Efficient Aromaticity Probe</em>, J. Am. Chem.
    Soc. <strong>118</strong>, 6317 (1996).</a>
2.  [↑](#cite_ref-chen:schleyer:2005_2-0)
    <a href="https://doi.org/10.1021/cr030088+" class="external text"
    rel="nofollow">Z. Chen, C. S. Wannere, C. Corminboeuf, R. Puchta, and P.
    von Ragué Schleyer, <em>Nucleus-Independent Chemical Shifts (NICS) as an
    Aromaticity Criterion</em>, Chem. Rev. 10, <strong>105</strong>,
    3842–3888 (2005).</a>
3.  [↑](#cite_ref-klod:kleinpeter:2001_3-0)
    <a href="https://doi.org/10.1039/B009809O" class="external text"
    rel="nofollow">S. Klod and E. Kleinpeter, <em>Ab initio calculation of
    the anisotropy effect of multiple bonds and the ring current effect of
    arenes—application in conformational and configurational analysis</em>,
    J. Chem. Soc., Perkin Trans. <strong>2</strong>, 1893-1898 (2001).</a>
4.  [↑](#cite_ref-kleinpeter:klod:koch:2007_4-0)
    <a href="https://doi.org/10.1016/j.theochem.2007.02.049"
    class="external text" rel="nofollow">E. Kleinpeter, S. Klod, and A.
    Koch, <em>Visualization of through space NMR shieldings of aromatic and
    anti-aromatic molecules and a simple means to compare and estimate
    aromaticity</em>, J. Mol. Struct. THEOCHEM <strong>811</strong>, 45-60
    (2007).</a>
5.  [↑](#cite_ref-karadakov:horner:2013_5-0)
    <a href="https://doi.org/10.1021/jp311536c" class="external text"
    rel="nofollow">P. Karadakov and K. Horner, <em>Magnetic Shielding in and
    around Benzene and Cyclobutadiene: A Source of Information about
    Aromaticity, Antiaromaticity, and Chemical Bonding</em>, J. Phys. Chem.
    A, <strong>117</strong>, 518-523 (2013).</a>
6.  [↑](#cite_ref-mason:ssn:1993_6-0)
    <a href="https://doi.org/10.1016/0926-2040(93)90010-K"
    class="external text" rel="nofollow">J. Mason, <em>Conventions for the
    reporting of nuclear magnetic shielding (or shift) tensors suggested by
    participants in the NATO ARW on NMR shielding constants at the
    University of Maryland, College Park, July 1992</em>, Solid State Nucl.
    Magn. Reson. <strong>2</strong>, 285 (1993).</a>


