<!-- Source: https://vasp.at/wiki/index.php/Pulay_stress | revid: 32951 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Pulay stress


Pulay stress is unphysical stress resulting from unconverged
calculations with respect to the basis set. It distorts the cell
structure, decreasing it from the equilibrium volume and creating
difficulties in volume relaxation. The resultant energy vs. volume
curves, cf. Figure 1 (top), are jagged and special care must be taken to
obtain reasonable structures, cf. [Volume
relaxation](../methods/Volume_relaxation.md). In this
article, the computational origin of this is discussed.

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Pressure_energy_volume.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/7/7a/Pressure_energy_volume.png/400px-Pressure_energy_volume.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/7/7a/Pressure_energy_volume.png/600px-Pressure_energy_volume.png 1.5x, /wiki/images/thumb/7/7a/Pressure_energy_volume.png/800px-Pressure_energy_volume.png 2x"
width="400" height="560" /></a>
<figcaption>Figure 1. Total energy (left y-axis) and absolute pressure
(right y-axis) vs. lattice parameter. Equilibrium lattice parameters for
energy and pressure are shown. These coincide when Pulay stress is
eliminated. ENCUT = 250 eV (top - unconverged) and 540 eV (bottom -
converged). Diamond in a primitive cell - 2x2x2 k-point
mesh.</figcaption>
</figure>

It is important to note that problems due to the Pulay stress can often
be neglected if only volume-conserving relaxations are performed. This
is because the Pulay stress is, usually, nearly uniform and only changes
the diagonal elements of the stress tensor by a constant amount.


## Contents


- [1
  Introduction](#Introduction)
- [2 Further
  explanation](#Further_explanation)
  - [2.1
    References](#References)
  - [2.2 Related
    tags and articles](#Related_tags_and_articles)


# Introduction\[<a
href="/wiki/index.php?title=Pulay_stress&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Introduction">edit</a> \| (./index.php.md)\]

The energy for a periodic system, e.g., band structures, is calculated
using a finite number of plane waves and a finite number of k-points. A
fixed number of plane waves or plane-wave energy cutoff may be used to
set a constant basis
<sup>[\[1\]](#cite_note-gomesdacosta:nielsen:kunc:1986-1)</sup>.
In VASP, a constant energy cutoff is used, cf.
[ENCUT](../incar-tags/ENCUT.md). The number of plane waves
***N****<sub>PW</sub>* (Note: the number of plane waves in VASP can be
found using by searching for `NPLWV` in the
[OUTCAR](../output-files/OUTCAR.md) file) is related to the energy cutoff
***E****<sub>cutoff</sub>* and the size of the cell **Ω**<sub>0</sub>:

$N_{PW} \propto\\ \Omega_0\\ E_{cutoff}^{3/2}$

***N****<sub>PW</sub>* is constant in a relaxation calculation, which
means that ***E****<sub>cutoff</sub>* must change to compensate for
changes in **Ω**<sub>0</sub>. All the initial G-vectors within a sphere
are included in the basis. However, when comparing cells of different
sizes, i.e., during a relaxation, the cell shape is relaxed, so the
direct and reciprocal lattice vectors change. The number of reciprocal
G-vectors in the basis is kept fixed, but the length of the G-vectors
changes, indirectly changing the energy cutoff. In other words, the
shape of the cutoff region changes from a sphere to an ellipsoid. This
can be solved by using an infinite number of k-points and plane waves.
In practice, a large enough plane wave energy cutoff and number of
k-points leads to converged energies
<sup>[\[2\]](#cite_note-payne:francis:1990-2)</sup>.
All energy changes are strictly consistent with the stress tensor;
however, when the basis set is too small, i.e., prematurely truncated,
this results in discontinuities in the total energy between cells of
varying volumes. These discontinuities between energy and volume create
stress that decreases the equilibrium volume (cf. Fig. 1 (top)), due to
the diagonal components of the stress tensor being incorrect. This is
called the *Pulay stress*.

The pressure of the cell, being proportional to the trace of the stress
tensor, can be used to visualize this. When the cell volume is below the
equilibrium volume, the pressure is positive; conversely, it is negative
when above the equilibrium volume, so at equilibrium, this is zero.
Plotting the magnitude of the pressure vs. volume curve and the total
energy allows comparison between these two minima. In Figure 1 it is
clear that the the absolute pressure-volume and energy-volume minima
coincide for a converged basis, while the pressure equilibrium is much
lower than the energy equilibrium for the unconverged basis. This is the
effect of the Pulay stress.

# Further explanation\[<a
href="/wiki/index.php?title=Pulay_stress&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Further explanation">edit</a> \| (./index.php.md)\]

As mentioned previously, ***N****<sub>PW</sub>* is constant in a
relaxation calculation, which means that ***E****<sub>cutoff</sub>* must
change to compensate for changes in **Ω**<sub>0</sub>. This is
illustrated in Fig. 2. The initial G-vectors within a sphere are
included within the basis.

When the cell volume increases (**V**<sub>1</sub> \< **V**<sub>1</sub>),
the number of G-vectors in reciprocal space remains constant, but their
length increases (cf. Fig. 2 (top)). This effectively results in a
change of basis, leading to (***E****<sub>cutoff, 1</sub>* \>
***E****<sub>cutoff, 2</sub>*). This basis remains constant for the
duration of the relaxation. However, if the calculation is then
restarted, the basis is reset. This means that the number of G-vectors
is greater for the larger, real-space cell. One effect of this is that
there are more real-space grid points. However, the corresponding
reciprocal space decreases.

Contrastingly, see Fig. 2 (bottom), when the volume decreases on
relaxation (**V**<sub>1</sub> \> **V**<sub>1</sub>), the length of the
G-vectors decreases. The effective ***E****<sub>cutoff</sub>* should
increase but this does not improve the situation, as it creates an
artificial pressure. The reciprocal space grid points are effectively
sparser. If the calculation restarts, the basis is reset, so the number
of G-vectors decreases for the smaller real space cell.

<figure class="mw-halign-center" typeof="mw:File/Thumb">
<a href="/wiki/File:Pulay_stress_grids.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/b/b1/Pulay_stress_grids.png/700px-Pulay_stress_grids.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/b/b1/Pulay_stress_grids.png/1050px-Pulay_stress_grids.png 1.5x, /wiki/images/thumb/b/b1/Pulay_stress_grids.png/1400px-Pulay_stress_grids.png 2x"
width="700" height="478" /></a>
<figcaption>Figure 2. Cell shape and lattice positions are kept
constant, while the volume <strong>V</strong> is free to
change (ISIF = 7). The initial volume
<strong>V</strong><sub>1</sub> changes to the final volume
<strong>V</strong><sub>2</sub>. Two cases are given, one
for volume increasing on relaxation (top) and one for it decreasing
(bottom). The change in real space is given on the left, while the
change in reciprocal space and the subsequent effect on the G-vectors is
given on the right. Blue is the initial basis, while red is the new,
restarted basis. The relation between
<strong><em>E</em></strong><em><sub>cutoff</sub></em>,
<strong><em>N</em></strong><em><sub>PW</sub></em>, and
G-vectors is given for the initial and final volumes.</figcaption>
</figure>

Alternatively, the shape of the cell could change. As the shape changes,
the G-vectors continue to be directed along the lattice coordinates,
meaning that some shorten while others lengthen, see Fig. 3. This
results in a shift from a spherical basis, where all G-vectors are of
equal length, to one where some are stretched and others compressed,
i.e. an ellipsoid. This changes the effective ***E****<sub>cutoff</sub>*
along each lattice parameter. On resetting the calculation, the cutoff
is once again spherical. This draws an analogy to the symmetry breaking
of the Bravais lattice seen for gradient-corrected functionals (cf.
[GGA_COMPAT](../incar-tags/GGA_COMPAT.md)), where the spherical
symmetry of the G-vectors is broken for non-cubic cells.

<figure class="mw-halign-center" typeof="mw:File/Thumb">
<a href="/wiki/File:Shape_pulay_grids.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/c/cc/Shape_pulay_grids.png/700px-Shape_pulay_grids.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/c/cc/Shape_pulay_grids.png/1050px-Shape_pulay_grids.png 1.5x, /wiki/images/thumb/c/cc/Shape_pulay_grids.png/1400px-Shape_pulay_grids.png 2x"
width="700" height="257" /></a>
<figcaption>Figure 3. Cell volume and lattice positions are kept
constant, while the shape is free to change (ISIF = 5). The shape
changes from cubic to hexagonal. The blue spherical basis changes to the
red ellipsoid basis, along the direction of the sheer. On restarting, a
spherical basis returns.</figcaption>
</figure>

## References\[<a
href="/wiki/index.php?title=Pulay_stress&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-gomesdacosta:nielsen:kunc:1986_1-0)
    <a href="https://doi.org/10.1088/0953-8984/2/19/007"
    class="external text" rel="nofollow">P. Gomes Dacosta, O. Nielsen, and
    K. Kunc, <em>Stress theorem in the determination of static equilibrium
    by the density functional method</em>, J. Phys. C: Solid State Phys.
    <strong>19</strong>, 3163 (1986).</a>
2.  [↑](#cite_ref-payne:francis:1990_2-0)
    <a href="https://doi.org/10.1088/0953-8984/2/19/007"
    class="external text" rel="nofollow">G. P. Francis and M. C. Payne,
    <em>Finite basis set corrections to total energy pseudopotential
    calculations</em>, J. Condens. Matter Phys. <strong>2</strong>, 4395
    (1990).</a>


## Related tags and articles\[<a
href="/wiki/index.php?title=Pulay_stress&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[PSTRESS](../incar-tags/PSTRESS.md)

[volume relaxation](../methods/Volume_relaxation.md),
[energy cutoff and FFT
meshes](Energy_cutoff_and_FFT_meshes.md)


