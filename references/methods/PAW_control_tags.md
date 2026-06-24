<!-- Source: https://vasp.at/wiki/index.php/PAW_control_tags | revid: 15317 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# PAW control tags
There are a few tags that control the behavior of the PAW
implementation. The first one is [LMAXPAW](../incar-tags/LMAXPAW.md)=*l*.
This flag sets the maximum *l*-quantum number for the evaluation of the
on-site terms on the radial support grids in the PAW method. The default
for [LMAXPAW](../incar-tags/LMAXPAW.md) is $2\*l_{max}$, where $l_{max}$
is the maximum angular quantum number of the partial waves. A useful
setting for this tag is for instance
[LMAXPAW](../incar-tags/LMAXPAW.md)=0. In this case, only spherical terms
are evaluated on the radial grid. This does not mean that a-spherical
terms are totally neglected, because the compensation charges are always
expanded up to $2\*l_{max}$ on the
plane wave grid.

For [LMAXPAW](../incar-tags/LMAXPAW.md)=-1, no on-site correction terms
are evaluated on the radial support grid, which effectively means that
the behavior of US-PP's is recovered with PAW input datasets. Usually
this allows very efficient and fast calculations, and this switch might
be of interest for relaxations and molecular dynamics runs. Energies
should be evaluated with the default setting for
[LMAXPAW](../incar-tags/LMAXPAW.md).

An additional tag [LMAXMIX](../incar-tags/LMAXMIX.md)=*l* controls up to
which *l* quantum number the on-site PAW charge densities are passed
through the charge density mixer and written to the
[CHGCAR](../input-files/CHGCAR.md) file.

The default is [LMAXMIX](../incar-tags/LMAXMIX.md)}=2. Higher l-quantum
numbers are usually **not** handled by the mixer, i.e. a straight mixing
is applied for them (the PAW on-site charge density for higher l quantum
numbers is reset precisely to the value corresponding to the present
orbitals). Usually, it is not required to increase
[LMAXMIX](../incar-tags/LMAXMIX.md), but the following two cases are
exceptions:

- L(S)DA+U calculations require in many cases an increase of
  [LMAXMIX](../incar-tags/LMAXMIX.md) to 4 (or 6 for f-elements) in order
  to obtain fast convergence to the groundstate.
- The [CHGCAR](../input-files/CHGCAR.md) file also contains only
  information up to [LMAXMIX](../incar-tags/LMAXMIX.md) for the on-site
  PAW occupancy matrices. When the [CHGCAR](../input-files/CHGCAR.md) file
  is read and kept fixed in the course of the calculations
  ([ICHARG](../incar-tags/ICHARG.md)=11), the results will be necessarily
  not identical to a self-consistent run. The deviations can be (or
  actually are) large for L(S)DA+U calculations. For the calculation of
  band structures within the L(S)DA+U approach it is strictly required
  to increase [LMAXMIX](../incar-tags/LMAXMIX.md) to 4 (d elements) and 6
  (f elements).

The second switch, that is useful in the context of the PAW method (and
US-PP) is [ADDGRID](../incar-tags/ADDGRID.md). The default is
[ADDGRID](../incar-tags/ADDGRID.md)=*.FALSE.*. If
[ADDGRID](../incar-tags/ADDGRID.md)=*.TRUE.* is written in the
[INCAR](../input-files/INCAR.md) file, an additional (third) support grid is
used for the evaluation of the augmentation charges. This third grid
contains 8 times more points than the fine grid
[NGXF](../incar-tags/NGXF.md), [NGYF](../incar-tags/NGYF.md),
[NGZF](../incar-tags/NGZF.md). Whenever terms involving augmentation charges
are evaluated, this third grid is used. For instance: The augmentation
charge is evaluated first in real space on this fine grid,
FFT-transformed to reciprocal space and then added to the total charge
density on the grid [NGXF](../incar-tags/NGXF.md),
[NGYF](../incar-tags/NGYF.md), [NGZF](../incar-tags/NGZF.md). The additional
grid helps to reduce the noise in the forces significantly. In many
cases, it even allows to perform calculations in which
[NGXF](../incar-tags/NGXF.md)=[NGX](../incar-tags/NGX.md) etc. This can be
achieved by setting [ENAUG](../incar-tags/ENAUG.md) = 1 and
[ADDGRID](../incar-tags/ADDGRID.md)=*.TRUE.* in the
[INCAR](../input-files/INCAR.md) file. The flag can also be used for US-PPs,
in particular, to reduce the noise in the forces.
