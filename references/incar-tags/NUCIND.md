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
[^schleyer:1996-1][^chen:schleyer:2005-2].
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
[^klod:kleinpeter:2001-3][^kleinpeter:klod:koch:2007-4].
It will produce an isosurface of the shielding (positive) and
deshielding (negative) over the crystal structure.

Alternatively, produce a 2D contour plot of the NICS in a plane
[^karadakov:horner:2013-5]:


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
[^mason:ssn:1993-6])
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

[^schleyer:1996-1]: [P. von Ragué Schleyer, C. Maerker, A. Dransfeld, H. Jiao, and N. J. R. van Eikema Hommes, *Nucleus-Independent Chemical Shifts:  A Simple and Efficient Aromaticity Probe*, J. Am. Chem. Soc. **118**, 6317 (1996).](https://doi.org/10.1021/ja960582d)
[^chen:schleyer:2005-2]: [Z. Chen, C. S. Wannere, C. Corminboeuf, R. Puchta, and P. von Ragué Schleyer, *Nucleus-Independent Chemical Shifts (NICS) as an Aromaticity Criterion*, Chem. Rev. 10, **105**, 3842–3888 (2005).](https://doi.org/10.1021/cr030088+)
[^klod:kleinpeter:2001-3]: [S. Klod and E. Kleinpeter, *Ab initio calculation of the anisotropy effect of multiple bonds and the ring current effect of arenes—application in conformational and configurational analysis*, J. Chem. Soc., Perkin Trans. **2**, 1893-1898 (2001).](https://doi.org/10.1039/B009809O)
[^kleinpeter:klod:koch:2007-4]: [E. Kleinpeter, S. Klod, and A. Koch, *Visualization of through space NMR shieldings of aromatic and anti-aromatic molecules and a simple means to compare and estimate aromaticity*, J. Mol. Struct. THEOCHEM **811**, 45-60 (2007).](https://doi.org/10.1016/j.theochem.2007.02.049)
[^karadakov:horner:2013-5]: [P. Karadakov and K. Horner, *Magnetic Shielding in and around Benzene and Cyclobutadiene: A Source of Information about Aromaticity, Antiaromaticity, and Chemical Bonding*, J. Phys. Chem. A, **117**, 518-523 (2013).](https://doi.org/10.1021/jp311536c)
[^mason:ssn:1993-6]: [J. Mason, *Conventions for the reporting of nuclear magnetic shielding (or shift) tensors suggested by participants in the NATO ARW on NMR shielding constants at the University of Maryland, College Park, July 1992*, Solid State Nucl. Magn. Reson. **2**, 285 (1993).](https://doi.org/10.1016/0926-2040(93)90010-K)
