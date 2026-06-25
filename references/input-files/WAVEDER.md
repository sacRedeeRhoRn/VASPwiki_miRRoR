<!-- Source: https://vasp.at/wiki/index.php/WAVEDER | revid: 35849 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# WAVEDER


The WAVEDER binary file is
written when [LOPTICS](../incar-tags/LOPTICS.md) = True  is set in the
[INCAR](INCAR.md) file. It contains the derivative of the
Kohn-Sham orbitals with respect to the Bloch vector **k**, written in
units of $\AA$. More
precisely, it contains the following matrix

$\braket{\tilde u_{n'\mathbf{k}s} | \tilde u_{n\mathbf{k}+k_i s} }=
\langle \tilde\psi_{n'\mathbf k s} |{\bf S} | \frac{\partial
\tilde\psi_{n\mathbf k s}}{\partial k_i}\rangle =
\frac{1}{\epsilon_{n\mathbf k s} -\epsilon_{n'\mathbf k s}} \langle
\tilde\psi_{n'\mathbf k s} | \frac{\partial (\mathbf{ H} -
\epsilon_{n\mathbf k s} \mathbf{S})}{\partial k_i} |
\tilde\psi_{n\mathbf k s} \rangle,$

where $\ket{\tilde u_{n\mathbf{k}s}}$ is the [cell periodic part of the pseudo-wave
function](../methods/Projector-augmented-wave_formalism.md),
$\ket{\tilde\psi_{n\mathbf k s}}$.

These matrix elements correspond to the dipole moment between the states
$\tilde\psi_{n'\mathbf k s}$ and
$\tilde\psi_{n\mathbf k s}$, which are important in the
context of dielectric properties. They serve as input for
[GW](../methods/Practical_guide_to_GW_calculations.md)
and
[Bethe-Salpeter](../tutorials/Bethe-Salpeter-equations_calculations.md)
calculations, as well as the [time-evolution
algorithm](../tutorials/Time-evolution_algorithm.md).

In the case of degenerate states, the matrix elements are set to zero,
within numerical accuracy.

|  |
|----|
| **Important:** Please note that only the matrix elements where $n$ or $n'$ correspond to a pair of an occupied and an unoccupied state are calculated and written to the WAVEDER file. Matrix elements involving both occupied or both unoccupied states are not computed. |

To include more empty states in the calculation, set the
[NBANDS](../incar-tags/NBANDS.md) tag in the [INCAR](INCAR.md)
file to a larger value with respect to the default. The default value of
[NBANDS](../incar-tags/NBANDS.md) can be obtained with a VASP [a dry
run](../misc/Command-line_arguments.md).
Setting [NBANDS](../incar-tags/NBANDS.md) is generally recommended for
[LOPTICS](../incar-tags/LOPTICS.md) = True , since the [dielectric
function](../categories/Category-Dielectric_properties.md)
is computed using a summation over empty states (see the page for
[LOPTICS](../incar-tags/LOPTICS.md) for more information).

## Format\[<a href="/wiki/index.php?title=WAVEDER&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Format">edit</a> \| (./index.php.md)\]

The header of the WAVEDER file
contains the following information:

- Total number of bands ([NBANDS](../incar-tags/NBANDS.md)), number of
  bands used in evaluation of matrix elements, number of k-points,
  number of spin channels (1 for unpolarised or non-collinear
  calculations, 2 for polarised calculations).
- Frequency node of the real part of the dielectric function, i.e. the
  solution for $\Re\[\epsilon(\omega)\] = 0$.
- Plasmon frequency.

They are then followed by the matrix elements
$\braket{\tilde\psi_{n'\mathbf k} |{\bf S} | \frac{\partial
\tilde\psi_{n\mathbf k}}{\partial k_i}}$. This is
stored in an five-indexed array, with the indices' order being
$(n',n,\mathbf k, i)$, where $i=1,2,3$ for
the Cartesian direction. The maximum value of each index is defined in
the file header, as mentioned above. For collinear spin-polarized
calculations ([`ISPIN`](../incar-tags/ISPIN.md)` = 2`) the
\$\uparrow\uparrow\$ and \$\downarrow\downarrow\$ matrix elements are
computed. For noncollienar magnetic calculations
([`LNONCOLLINEAR`](../incar-tags/LNONCOLLINEAR.md)` = True`) the KS
orrbitals are stored as spinors and the \$\uparrow\uparrow\$,
\$\uparrow\downarrow\$, \$\downarrow\uparrow\$ and
\$\downarrow\downarrow\$ components are computed.

## Usage\[<a href="/wiki/index.php?title=WAVEDER&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Usage">edit</a> \| (./index.php.md)\]

If the WAVEDER file is read
successfully, it can be used as a starting point in the following types
of calculations:

- <a href="/wiki/GW_calculations" class="mw-redirect"
  title="GW calculations">GW calculations</a>
- <a href="/wiki/BSE_calculations" class="mw-redirect"
  title="BSE calculations">BSE calculations</a>
- [Time
  evolution](../tutorials/Time-evolution_algorithm.md)

The information on the number of bands, k-points, and spin channels is
used by VASP in subsequent calculations to check for compatibility
between runs. If these parameters are different between different runs,
the matrix elements inside the
WAVEDER file are not read. A
warning will then be printed to the standard output reporting that the
WAVEDER file is incompatible with the present calculation and advising
to run the previous step (i.e., the calculation where
[LOPTICS](../incar-tags/LOPTICS.md) = TRUE ).

Information on the frequency node of the real part of the dielectric
function is used in defining the frequency grid for
<a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW calculations</a> and the [time-evolution
algorithm](../tutorials/Time-evolution_algorithm.md),
while the plasmon frequency is used for computing the Drude-term
contribution to the dielectric function. This term used in [GW
calculations](../methods/Practical_guide_to_GW_calculations.md)
to include the intra-band contribution to the dielectric function.

## Related tags and sections\[<a href="/wiki/index.php?title=WAVEDER&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and sections">edit</a> \| (./index.php.md)\]

[LOPTICS](../incar-tags/LOPTICS.md),
<a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW calculations</a>,
<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a>, [Time-evolution
algorithm](../tutorials/Time-evolution_algorithm.md)

------------------------------------------------------------------------


