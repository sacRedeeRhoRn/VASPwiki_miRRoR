<!-- Source: https://vasp.at/wiki/index.php/Volume_relaxation | revid: 33040 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Volume relaxation



## Contents


- [1
  Introduction](#introduction)
- [2 How to
  correct](#how-to-correct)
  - [2.1 1. Volume
    relaxation](#1-volume-relaxation)
    - [2.1.1 Step
      1.](#step-1)
    - [2.1.2 Step
      2.](#step-2)
    - [2.1.3 Step
      3.](#step-3)
    - [2.1.4
      (Optional)](#optional))
    - [2.1.5 Step
      4a.](#step-4a)
    - [2.1.6 Step
      4b.](#step-4b)
  - [2.2 2.
    Equation of state fitting](#2-equation-of-state-fitting)
    - [2.2.1 Step
      0.](#step-0)
    - [2.2.2 Step
      1.](#step-1-1)
    - [2.2.3 Step
      2.](#step-2-1)
    - [2.2.4 Step
      3.](#step-3-1)
    - [2.2.5 Step
      4.](#step-4)
- [3 Possible
  issues and advice on how to address
  them](#possible-issues-and-advice-on-how-to-address-them)
  - [3.1
    References](#references)


# Introduction\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Introduction">edit</a> \| (./index.php.md)\]

When relaxing the volume of cells, care must be taken. If too small an
[ENCUT](../incar-tags/ENCUT.md) or k-mesh are used, then discontinuities in
energy vs. volume curves can be seen, cf. Fig. 1 and 2. This is due to
an unconverged basis set being used. This creates unphysical forces,
known as [Pulay stress](../tutorials/Pulay_stress.md), that distort
the cell structure away from equilibrium, decreasing the volume. This
Pulay stress can be neglected in volume-conserving relaxations but
becomes important in volume relaxations.

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:ENCUT_comp.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/2/2f/ENCUT_comp.png/400px-ENCUT_comp.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/2/2f/ENCUT_comp.png/600px-ENCUT_comp.png 1.5x, /wiki/images/2/2f/ENCUT_comp.png 2x"
width="400" height="286" /></a>
<figcaption>Figure 1. Total energy vs. lattice parameter for converged
and unconverged plane wave energy cutoffs. Diamond in a primitive cell -
2x2x2 k-point mesh.</figcaption>
</figure>

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:Kpoint_comp.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/a/ac/Kpoint_comp.png/400px-Kpoint_comp.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/a/ac/Kpoint_comp.png/600px-Kpoint_comp.png 1.5x, /wiki/images/a/ac/Kpoint_comp.png 2x"
width="400" height="286" /></a>
<figcaption>Figure 2. Total energy vs. lattice parameter for converged
and unconverged k-point meshes. Diamond in a primitive cell - 180 eV
energy cutoff.</figcaption>
</figure>

# How to correct\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: How to correct">edit</a> \| (./index.php.md)\]

The Pulay stress may be corrected in multiple ways. Generally, by
calculating the relaxed structure with a larger basis set by increasing
the [ENCUT](../incar-tags/ENCUT.md) until convergence is reached:

1.  Set [ENCUT](../incar-tags/ENCUT.md) to 1.3 × the default cutoff, or
    [PREC](../incar-tags/PREC.md)=*High* in VASP.4.4. Note: this is the
    lower recommended limit.
2.  Re-run VASP with the default cutoff to obtain the final relaxed
    positions and cell parameters.
3.  Further increase the [ENCUT](../incar-tags/ENCUT.md) and repeat Steps 1
    and 2, until the structure no longer changes, i.e. is converged.

|  |
|----|
| **Mind:** This relaxation is done along all of the lattice vectors. If you want to relax only one and keep the others fixed, e.g. for the vacuum in a surface relaxation, then [LATTICE_CONSTRAINTS](../incar-tags/LATTICE_CONSTRAINTS.md) may be used instead. This can constrain any of the three lattice vectors for orthorhombic cells, or specific rows and columns in the lattice matrix for non-orthorhombic cells. |

If volume relaxations are necessary, the following two procedures may be
followed:

## 1. Volume relaxation\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: 1. Volume relaxation">edit</a> \| (./index.php.md)\]

One way is to very accurately relax the structure in a series of
calculations on one structure:

### Step 1.\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Step 1.">edit</a> \| (./index.php.md)\]

Relax from the starting structure ([ISIF](../incar-tags/ISIF.md) = 7;
[IBRION](../incar-tags/IBRION.md) = 1, 2, or 3) with Gaussian or
Methfessel-Paxton smearing ([ISMEAR](../incar-tags/ISMEAR.md) = 0 or 1).
Note: other settings can be used for [ISIF](../incar-tags/ISIF.md), e.g. 3,
6, or 8 but it is not recommended to relax more than one degree of
freedom at a time. For instance,

    ISMEAR = 0 ; SIGMA = 0.05 # change smearing to ISMEAR = 1 ; SIGMA = 0.2 for metals
    ISIF = 7 ; IBRION = 2; NSW = 20

### Step 2.\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Step 2.">edit</a> \| (./index.php.md)\]

Copy the [CONTCAR](../output-files/CONTCAR.md) to
[POSCAR](../input-files/POSCAR.md) and relax the structure again.

    ISMEAR = 0 ; SIGMA = 0.05 # change smearing to ISMEAR = 1 ; SIGMA = 0.2 for metals
    ISIF = 7 ; IBRION = 2; NSW = 20
    ISTART = 1 # this keeps that energy cut-off constant, while updating the plane wave basis for the new cell volume

|  |
|----|
| **Mind:** In this procedure, it is important to set [ISTART](../incar-tags/ISTART.md) = 1 so that the basis is updated and the energy cut-off remains constant. If [ISTART](../incar-tags/ISTART.md) = 2, the basis remains constant, which will also keep the artificial, Pulay stress, i.e., it is an exact restart of the calculation in Step 1, with identically poor settings. |

### Step 3.\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Step 3.">edit</a> \| (./index.php.md)\]

Change the smearing method to the tetrahedron method (i.e.
[ISMEAR](../incar-tags/ISMEAR.md)=-5) and perform a single point
calculation, i.e. no relaxation of structure. These will give highly
accurate energies.

    ISMEAR = -5 # tetrahedron method
    NSW = 0

### (Optional)\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: (Optional)">edit</a> \| (./index.php.md)")\]

The previous steps should yield good energies. If there are still
problems, such as the energy vs. volume curve remaining jagged, a few
more additional steps may be tried:

### Step 4a.\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Step 4a.">edit</a> \| (./index.php.md)\]

Try further increasing the [ENCUT](../incar-tags/ENCUT.md). Alternatively,
improve the FFT grid by setting [PREC](../incar-tags/PREC.md)=Accurate.

### Step 4b.\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Step 4b.">edit</a> \| (./index.php.md)\]

To avoid additional computational cost due to increased cutoff energy,
the *STRESS* output in VASP may be corrected using
[PSTRESS](../incar-tags/PSTRESS.md). The Pulay stress is only weakly
dependent on volume and ionic configuration; it is mainly determined by
the composition and basis set. A good estimation for it is given in the
output, e.g.:

      external pressure =    -100.29567 kB

The difference in this pressure (between the desired and a very large
[ENCUT](../incar-tags/ENCUT.md)) may then be used to correct for the Pulay
stress. [PSTRESS](../incar-tags/PSTRESS.md) is set to this difference,
then all volume relaxations will take [PSTRESS](../incar-tags/PSTRESS.md)
into account. It is important keep in mind that
[PSTRESS](../incar-tags/PSTRESS.md) should only be used if increasing the
cutoff is not a viable option.

1.  Perform two single point calculations, one for the default and one
    for the higher [ENCUT](../incar-tags/ENCUT.md).
2.  Find the external pressure in the [OUTCAR](../output-files/OUTCAR.md)
    file, e.g.:

<!-- -->

      external pressure =    -1311.32 kB
      
      external pressure =    -95.66 kB

3.  Find the difference between these external pressures. This is a good
    approximation of the Pulay stress. E.g.

<!-- -->

      difference in pressure = -1215.66 kB

4.  Set [PSTRESS](../incar-tags/PSTRESS.md) equal to this difference in
    the [OUTCAR](../output-files/OUTCAR.md) file, i.e.:

<!-- -->

      PSTRESS = -1215.66

This results in structures similar to the higher cutoff at the cost of
the default cutoff. We reiterate that [PSTRESS](../incar-tags/PSTRESS.md)
should only be used if the higher cutoff is not a viable option, as this
only improves the structure and not the energy.

## 2. Equation of state fitting\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: 2. Equation of state fitting">edit</a> \| (./index.php.md)\]

An alternative way to avoid relaxing the volume is to relax the ionic
positions and cell shape for a fixed set of volumes, i.e., multiple
[POSCAR](../input-files/POSCAR.md) files. These are then fitted to an
equation of state (EOS), e.g., Murnaghan
[^murnaghan:web-1].
As the Pulay stress is almost isotropic, only a constant value is added
to the diagonal elements of the stress tensor. Therefore, the relaxation
for a fixed volume will yield highly accurate structures. This approach
has the advantage of also providing the bulk modulus, and we have found
it may be used safely with the default energy cutoff.

To fit the equation of state, you need to do calculations for a set of
fixed volumes
[^2].
The following steps are required:

### Step 0.\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Step 0.">edit</a> \| (./index.php.md)\]

Build an initial structure. You can take a unit cell for this and the
experimental lattice parameter a (if known).

### Step 1.\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Step 1.">edit</a> \| (./index.php.md)\]

From your initial structure, create four additional structures with
lattice parameters ±5 % and ±10 % of the initial lattice parameter.
I.e., you should have 5 structures: `0.90a 0.95a 1.0a 1.05a 1.10a`. The
experimental lattice parameter of C diamond is 3.567 Å, so the value of
`X` in the following [POSCAR](../input-files/POSCAR.md) should be
`3.210 3.389 3.567 3.745 3.924`

    cubic diamond
    X
     0.0    0.5     0.5
     0.5    0.0     0.5
     0.5    0.5     0.0
    2
    Direct
     -0.125 -0.125 -0.125
      0.125  0.125  0.125

### Step 2.\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Step 2.">edit</a> \| (./index.php.md)\]

Calculate the energy for each of your structures. You can use the
following basic [INCAR](../input-files/INCAR.md) settings:

    ISMEAR = 0; SIGMA = 0.05 # change smearing to ISMEAR  = 1; SIGMA = 0.2 for metals
    IBRION = 0

For extremely accurate energies, you can instead use the tetrahedron
method by setting [`ISMEAR`](../incar-tags/ISMEAR.md)` = -5` (not for
metals).

### Step 3.\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: Step 3.">edit</a> \| (./index.php.md)\]

Find the lattice parameter and the energy for each structure:

    #!/bin/bash
    # Remove any previous data file
    rm -f loop_lattice_constant.dat

    # Loop through each subdirectory
    for a in */; do
      latt=$(grep "ALAT" "$a"/OUT* | awk '{print $3}')
      E=$(grep "free  e" "$a"/OUTCAR | awk '{print $5}')
      echo "$latt $E" >> loop_lattice_constant.dat
    done

### Step 4.\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: Step 4.">edit</a> \| (./index.php.md)\]

Plot the lattice parameter against the energy and fit according to the
Murnaghan equation (or another equation of state like the
Birch-Murnaghan).


**Click to reveal a Python script to plot this**


    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.optimize import curve_fit

    # Load data
    data = np.loadtxt("loop_lattice_constant.dat")
    a = data[:, 0]
    E = data[:, 1]

    # Murnaghan EOS with fixed B0_prime
    def murnaghan_fixed(a, E0, B0, a0):
        B0_prime = 4.0  # fixed
        V = a**3
        V0 = a0**3
        return E0 + (B0*V/V0/B0_prime) * (((V0/V)**B0_prime)/(B0_prime-1) + 1) - B0*V0/(B0_prime-1)

    # Initial guess [E0, B0, a0]
    initial_guess = [min(E), 1.0, a[np.argmin(E)]]

    # Optional: bounds to avoid unphysical results
    bounds = ([-np.inf, 0, min(a)], [np.inf, np.inf, max(a)])

    # Fit with more iterations
    popt, pcov = curve_fit(murnaghan_fixed, a, E, p0=initial_guess, bounds=bounds, maxfev=5000)
    E0, B0, a0 = popt

    print(f"Fitted parameters:\nE0 = {E0:.5f} eV, B0 = {B0:.5f} eV/Å³, a0 = {a0:.5f} Å")

    # Plot
    a_fit = np.linspace(min(a), max(a), 200)
    E_fit = murnaghan_fixed(a_fit, *popt)

    plt.figure(figsize=(6,4))
    plt.scatter(a, E, color='#A82C35', label='Data')
    plt.plot(a_fit, E_fit, color='#3E70EA', label='Murnaghan fit')
    plt.axvline(a0, color='#8342A4', linestyle='--', label=f'a0 = {a0:.3f} Å')
    plt.xlabel('Lattice constant a (Å)')
    plt.ylabel('Energy (eV)')
    plt.title('Murnaghan EOS Fit')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


<figure class="mw-halign-left" typeof="mw:File/Thumb">
<a href="/wiki/File:Murnaghan_fit.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/d/d5/Murnaghan_fit.png/400px-Murnaghan_fit.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/d/d5/Murnaghan_fit.png 1.5x" width="400"
height="267" /></a>
<figcaption>Figure 3. Murnaghan fit of 5 different lattice parameters
for C diamond.</figcaption>
</figure>


In the above script, we have defined Murnaghan fit explicitly. Other
tools, e.g., <a
href="https://pymatgen.org/pymatgen.analysis.html#module-pymatgen.analysis.eos"
class="external text" rel="nofollow">pymatgen</a>, are available where
EOS have been defined.

The optimized lattice parameter is the minimum of the Murnaghan fit.
Five points are used here as an example; we recommend using more to
improve the fit. Take a look at our tutorials for an alternative
approach where
<a href="https://www.vasp.at/tutorials/latest/bulk/part1/"
class="external text" rel="nofollow">a range of lattice parameters are
taken for silicon</a>.

# Possible issues and advice on how to address them\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: Possible issues and advice on how to address them">edit</a> \| (./index.php.md)\]

When producing energy vs. volume plots, improper settings may result in
jagged curves, cf. Fig. 1 and 2. This is commonly due to two reasons:

1.  **Basis set incompleteness**

    The basis set is discrete and incomplete, so when the volume
    changes, additional plane waves are added. That causes small
    discontinuous changes in the energy.

    1.  Use a larger plane wave cutoff, cf. Fig. 1. This is usually the
        preferred and simplest solution.
    2.  Use more k-points, cf. Fig. 2.
        |  |
        |----|
        | **Important:** This solves the problem because the criterion for including a plane wave in the basis set is $\vert {\bf G} + {\bf k} \vert < {\bf G}_{\rm cut}$. This means at each k-point a different basis set is used, and additional plane waves are added at each k-point at different volumes. In turn, the energy vs. volume curve becomes smoother. |

2.  **Discontinuity of FFT grids**

    Different precisions of the FFT grid defined by
    [PREC](../incar-tags/PREC.md) may be used, e.g. Normal or Accurate.

    |  |
    |----|
    | **Mind:** For [PREC](../incar-tags/PREC.md)=Accurate, the FFT grids are chosen such that ${\bf H} \vert \phi>$ is exactly evaluated. Whereas, for [PREC](../incar-tags/PREC.md)=Normal the FFT grids are set to 3/4 of the value that is required for an exact evaluation of ${\bf H} \vert \phi>$. |

    This introduces small errors when the volume changes, as the FFT
    grids change discontinuously. In other words, at each volume a
    different FFT grid is used, causing the energy to jump
    discontinuously between different volumes. For more details on FFT
    grids, see
    [^vasp:intro:lecture:web-3].

    1.  Use [PREC](../incar-tags/PREC.md)=Accurate
    2.  Increase the plane wave cutoff.
    3.  Set your FFT grids manually, and choose the one that is used per
        default for the largest volume.

## References\[<a
href="/wiki/index.php?title=Volume_relaxation&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

[^murnaghan:web-1]: [Murnaghan Equation of State, www.wikipedia.org (2024)](https://en.wikipedia.org/wiki/Murnaghan_equation_of_state)
[^2]: This, of course, implies that the number of basis vectors is different at each volume. Calculations with many plane-wave codes have shown that such calculations yield reliable results for the lattice constants and the bulk modulus and other elastic properties even at relatively modest energy cutoffs. Constant energy cut-off calculations are less prone to errors caused by the basis set incompleteness than constant basis set calculations. But it should be kept in mind that volume and cell shape changes must be rather large in order to obtain reliable results from this method, because within the limit of very small distortions, the energy changes obtained with this method are equivalent to those obtained from the stress tensor and are therefore affected by the Pulay stress. Only volume changes of the order of 5-10 % guarantee that the errors introduced by the basis set incompleteness are averaged out.
[^vasp:intro:lecture:web-3]: [Introduction to ab-initio simulation in VASP](https://youtu.be/Fv3F4LHGPuc?si=dJlZD9dTuxQz__R9)
