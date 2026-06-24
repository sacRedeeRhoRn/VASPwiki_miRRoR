<!-- Source: https://vasp.at/wiki/index.php/WRT_NMRCUR | revid: 35862 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# WRT_NMRCUR
WRT_NMRCUR = 0 \| 1 \| 2 \| 3 \| 4  
Default: **WRT_NMRCUR** = 0 

Description: Allows to write the
[NMR](../categories/Category-NMR.md) current response in atomic
units to file.

|                                      |
|--------------------------------------|
| **Mind:** Available as of VASP 6.6.0 |

------------------------------------------------------------------------

In conjunction with [`LCHIMAG`](LCHIMAG.md)` = True`,
WRT_NMRCUR allows to write the current response on the fine grid
[NGXF](NGXF.md) x [NGYF](NGYF.md) x
[NGZF](NGZF.md) in atomic units (hartree
bohr$^{-2}$) to an external magnetic
field within [linear response NMR](../categories/Category-NMR.md).

|  |
|----|
| **Important:** The fine FFT grid is only the plane-wave contribution to the current response; the one-center diamagnetic and paramagnetic contributions are calculated on radial grids and not the fine FFT grid. This does not affect the chemical shieldings, which include the contribution from all three parts. |

The output is written to [NMRCURBX](../output-files/NMRCURBX.md),
[NMRCURBY](../redirects/NMRCURBY.md), and/or
[NMRCURBZ](../redirects/NMRCURBZ.md) depending on the selected
direction of the perturbing $\mathbf{B}$
field:

- `WRT_NMRCUR`` = 0`: no current response written to file (default)
- `WRT_NMRCUR`` = 1`: $B_x$
- `WRT_NMRCUR`` = 2`: $B_y$
- `WRT_NMRCUR`` = 3`: $B_z$
- `WRT_NMRCUR`` = 4`: all three directions of $\mathbf{B}=(B_x,B_y,B_z)^T$

It is also written to [vaspout.h5](../output-files/Vaspout.h5.md), if
compiled with [HDF5
support](../misc/Makefile.include.md). You can
find the data groups

     /results/nmrcurbx        Group
     /results/nmrcurbx/grid   Dataset {3}
     /results/nmrcurbx/structure Group
     /results/nmrcurbx/structure/position Group
     /results/nmrcurbx/structure/position/direct_coordinates Dataset {SCALAR} 
     /results/nmrcurbx/structure/position/ion_sha256 Dataset {1}
     /results/nmrcurbx/structure/position/ion_types Dataset {1}
     /results/nmrcurbx/structure/position/lattice_vectors Dataset {3, 3}
     /results/nmrcurbx/structure/position/number_ion_types Dataset {1}
     /results/nmrcurbx/structure/position/position_ions Dataset {2, 3}
     /results/nmrcurbx/structure/position/scale Dataset {SCALAR}
     /results/nmrcurbx/structure/position/system Dataset {SCALAR}
     /results/nmrcurbx/values Dataset {3, 24, 24, 24}

and use [py4vasp](https://vasp.at/py4vasp/latest/index.html) to access
these, e.g., using

    import py4vasp as pv
    calc = pv.Calculation.from_path(".")
    calc.current_density.to_contour("NMR(x)", a=0.5) + calc.current_density.to_quiver("NMR(x)", a=0.5)

to select the current response triggered by $B_x$. It will result in a contour plot showing the magnitude of
the current density and a quiver plot with the projected current in the
selected plane. The plane is selected as a fraction
$x$ of the lattice vector. Here, `x=0.5`
along $\mathbf{a}$. For the other
lattice vectors use `b=x` or `c=x`.

|  |
|----|
| **Warning:** For bulk calculations you must switch off the use of symmetry. In other words, set [`ISYM`](ISYM.md)` <= 0` if there is more than a single k point at zero (the Γ point). |

|  |
|----|
| **Tip:** Consider switching on current augmentation ([`LLRAUG`](LLRAUG.md)` = True`). |

## Related tags and articles
[LCHIMAG](LCHIMAG.md), [LLRAUG](LLRAUG.md),
[NMRCURBX](../output-files/NMRCURBX.md)
