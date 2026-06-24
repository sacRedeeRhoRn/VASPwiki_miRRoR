<!-- Source: https://vasp.at/wiki/index.php/PREC | revid: 31482 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PREC
PREC = Normal \| Single \| SingleN \| Accurate \| Low \| Medium \| High 

|                   |          |                |
|-------------------|----------|----------------|
| Default: **PREC** | = Medium | for VASP.4.X   |
|                   | = Normal | since VASP.5.X |

Description: PREC specifies the "precision" mode.

------------------------------------------------------------------------

PREC sets default values for the energy cutoff
[ENCUT](ENCUT.md), the FFT grids
([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md))
and
([NGXF](NGXF.md),[NGYF](NGYF.md),[NGZF](NGZF.md)),
and the accuracy of the projectors in real space
[ROPT](ROPT.md) (used only when
[LREAL](LREAL.md)=.TRUE.). Details are given below in the
table.

We recommend using PREC=Normal or PREC=Accurate. PREC=Normal can be used
for most routine calculations. PREC=Accurate leads to a denser grid
([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md)).
Thus, it reduces egg-box effects and strictly avoids any
[aliasing/wrap-around
errors](../theory/Wrap-around_errors.md). PREC=Normal and
PREC=Accurate use an augmentation fine grid
([NGXF](NGXF.md),[NGYF](NGYF.md),[NGZF](NGZF.md))
that is twice larger than the grid
([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md))
used for the representation of the pseudo-orbitals. PREC=Accurate
increases the memory requirements somewhat, but it should be used (in
combination with an increased value for [ENCUT](ENCUT.md))
when a very good accuracy is required, e.g., for accurate forces, for
phonons and stress tensor or in general when second derivatives are
computed. The accuracy of forces can also be sometimes further improved
by specifying [ADDGRID](ADDGRID.md)=.TRUE., however,
reports from users are somewhat contradictory about whether this really
helps. More details can be found at [Energy cutoff and FFT
mesh](../redirects/Energy_cut_off_and_FFT_mesh.md).

[TABLE]

[TABLE]

|  |
|----|
| **Deprecated:** The old settings PREC=Medium, High and Low are no longer recommended and are available only for backward compatibility. Essentially, PREC=High only increases the energy cutoff by 30 %, which can also be achieved by just manually increasing [ENCUT](ENCUT.md). |

## Default values set by PREC
Default values set by PREC for the parameters
[ENCUT](ENCUT.md),
([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md)),
([NGXF](NGXF.md),[NGYF](NGYF.md),[NGZF](NGZF.md))
and [ROPT](ROPT.md):

|  |  |  |  |  |  |
|----|:--:|:--:|:--:|:--:|:--:|
| PREC | [ENCUT](ENCUT.md) | [NGX](NGX.md),[Y](NGY.md),[Z](NGZ.md) | [NGXF](NGXF.md),[YF](NGYF.md),[ZF](NGZF.md) | [ROPT](ROPT.md) ([LREAL](LREAL.md)=A) | [ROPT](ROPT.md) ([LREAL](LREAL.md)=O) |
| Normal | max([ENMAX](../redirects/ENMAX.md)) | 3/2×$G_{\rm cut}$ | 2×[NGX](NGX.md) | -5×10⁻⁴ | 1.0 |
| Single (VASP.5) | max([ENMAX](../redirects/ENMAX.md)) | 3/2×$G_{\rm cut}$ | [NGX](NGX.md) | -5×10⁻⁴ | 1.0 |
| Single (VASP.6) | max([ENMAX](../redirects/ENMAX.md)) | 2×$G_{\rm cut}$ | [NGX](NGX.md) | -5×10⁻⁴ | 1.0 |
| SingleN (VASP.6) | max([ENMAX](../redirects/ENMAX.md)) | 3/2×$G_{\rm cut}$ | [NGX](NGX.md) | -5×10⁻⁴ | 1.0 |
| Accurate | max([ENMAX](../redirects/ENMAX.md)) | 2×$G_{\rm cut}$ | 2×[NGX](NGX.md) | -2.5×10⁻⁴ | 1.0 |
|  **Deprecated settings:** |  |  |  |  |  |
| Low | max([ENMIN](ENMIN.md)) | 3/2×$G_{\rm cut}$ | 3×$G_{\rm aug}$ | -1×10⁻² | 2/3 |
| Medium | max([ENMAX](../redirects/ENMAX.md)) | 3/2×$G_{\rm cut}$ | 4×$G_{\rm aug}$ | -2×10⁻³ | 1.0 |
| High | 1.3×max([ENMAX](../redirects/ENMAX.md)) | 2×$G_{\rm cut}$ | 16/3×$G_{\rm aug}$ | -4×10⁻⁴ | 1.5 |

where max([ENMAX](../redirects/ENMAX.md)) and
max([ENMIN](ENMIN.md)) are the maxima of
[ENMAX](../redirects/ENMAX.md) and [ENMIN](ENMIN.md) found in
the [POTCAR](../input-files/POTCAR.md) file, and $G_{\rm cut}$ and $G_{\rm aug}$ are defined by

$E_{\rm cut}=\frac{\hbar^2}{2m_e}G_{\rm cut}^2
\qquad E_{\rm aug}=\frac{\hbar^2}{2m_e}G_{\rm aug}^2$

with $E_{\rm cut}$=[ENCUT](ENCUT.md) and $E_{\rm aug}$=[ENAUG](ENAUG.md).

## Further remarks
- With PREC=Normal, Single, and Accurate the grid
  ([NGXF](NGXF.md),[NGYF](NGYF.md),[NGZF](NGZF.md))
  representing the augmentation charges, charge densities and potentials
  has either the same size (PREC=Single) or the double size (PREC=Normal
  or Accurate) as the grid
  ([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md)).
  With the deprecated (and no longer recommended) settings for PREC
  (Low, Medium and High), the grid
  ([NGXF](NGXF.md),[NGYF](NGYF.md),[NGZF](NGZF.md))
  is determined by some heuristic formula from
  [ENAUG](ENAUG.md).

&nbsp;

- PREC=Single uses the same grid
  ([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md))
  as PREC=Normal in VASP.5, but the same grid as PREC=Accurate in
  VASP.6. However, the double grid technique is not used, i.e.,
  ([NGXF](NGXF.md),[NGYF](NGYF.md),[NGZF](NGZF.md))=([NGX](NGX.md),[NGY](NGY.md),[NGZ](NGZ.md)).
  This is convenient if one needs to cut down on storage demands or if
  one wants to reduce the size of the files [CHG](../output-files/CHG.md) and
  [CHGCAR](../input-files/CHGCAR.md). Furthermore, PREC=Single avoids
  high-frequency oscillations caused by the double-grid technique and
  the resulting Fourier interpolation. It is often expedient for
  scanning tunneling simulations or other calculations where
  high-frequency wiggles of the charge density in the vacuum region are
  undesirable.

&nbsp;

- PREC=High should guarantee that the absolute energies are converged to
  a few meV and the stress tensor converged within a few kBar.

## Related tags and articles
[NGX](NGX.md), [NGY](NGY.md), [NGZ](NGZ.md),
[NGXF](NGXF.md), [NGYF](NGYF.md),
[NGZF](NGZF.md), [ENCUT](ENCUT.md),
[ENAUG](ENAUG.md), [ENMIN](ENMIN.md),
[ENMAX](../redirects/ENMAX.md), [ROPT](ROPT.md),
[LREAL](LREAL.md), [ADDGRID](ADDGRID.md),
[PRECFOCK](PRECFOCK.md), [Energy cutoff and FFT
mesh](../redirects/Energy_cut_off_and_FFT_mesh.md),
[Wrap-around errors](../theory/Wrap-around_errors.md)

[Examples that use this
tag](https://vasp.at/wiki/index.php/Special-Search/-PREC-_incategory-Examples)
