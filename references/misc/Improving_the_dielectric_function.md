<!-- Source: https://vasp.at/wiki/index.php/Improving_the_dielectric_function | revid: 35879 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Improving the dielectric function
[Overview](../tutorials/BSE_-_Tutorial.md) \> [Dielectric
properties of Si using
BSE](Dielectric_properties_of_Si_using_BSE.md) \>
Improving the dielectric function  \> [Plotting the BSE fatband
structure of
Si](Plotting_the_BSE_fatband_structure_of_Si.md) \>
[List of tutorials](../categories/Category-Tutorials.md)

## Contents

- [1 Task](#Task)
- [2 Input](#Input)
  - [2.1 INCAR](#INCAR)
  - [2.2 KPOINTS](#KPOINTS)
- [3 Calculation](#Calculation)
  - [3.1 Averaging over multiple grids](#Averaging_over_multiple_grids)
  - [3.2 Model-BSE](#Model-BSE)
- [4 Download](#Download)
- [5 References](#References)

## Task
Calculate the dielectric function of Si using an averaging over multiple
grids or a model-BSE to improve k-sampling in BSE calculations.

## Input
    Si
     5.4300
    0.5 0.5 0.0
    0.0 0.5 0.5
    0.5 0.0 0.5
    2
    cart
    0.00 0.00 0.00 
    0.25 0.25 0.25 

### [INCAR](../input-files/INCAR.md)
- This is the [INCAR](../input-files/INCAR.md) file for the basic DFT
  calculation:

&nbsp;

    System  = Si
    PREC = Normal ; ENCUT = 250.0
    ISMEAR = 0 ; SIGMA = 0.01
    KPAR = 2
    EDIFF = 1.E-8

### [KPOINTS](../input-files/KPOINTS.md)
    Automatic
     0
    Gamma
     4 4 4 
     0 0 0

## Calculation
The calculated spectra can be improved in two ways:

- Averaging over multiple grids:

Compute *N* independent dielectric functions using BSE (or any other
method), using *shifted* grids of **k**-points, and take the average
over the results.

- Model-BSE:

Use a parametrized
model^([\[1\]](#cite_note-bokdam:scr:6-1)[\[2\]](#cite_note-liu:bse-2))
for the dielectric screening, and DFT eigenenergies moved with a
*scissor* operator, instead of RPA screening and GW quasiparticle
energies.

### Averaging over multiple grids
- Construct shifted k-point grid with the same density.
- $n\times n\times n$ k-point grid
  $\rightarrow$ $X_{n}$ irreducible k-points ${K_{n}}$ with weights $W_{n}$. We
  do $x_{n}$ calculations on a
  $m\times m\times m$ grid, shifted of
  Gamma by $K_{n}$.
- Extract the dielectric function of each calculation and average over
  them with respect to the weights $W_{n}$:

We have now effectively constructed the result for a
$(n\times m) \times (n\times m) \times (n\times m)$ grid. But interactions of range longer than
$m$ times the supercell size have been
ignored.

- In our example we use $n=4$ and
  $m=4$: Effectively we use
  $16\times 16\times 16$ k-points.

[![](https://vasp.at/wiki/images/thumb/d/d6/Fig_BSE_example2_1.png/500px-Fig_BSE_example2_1.png)](https://vasp.at/wiki/File:Fig_BSE_example2_1.png)

- In the script *doall-average.sh* the scheme is written for
  $n=4$ and $n=\textrm{\\NKPT}$. At the end the dielectric functions are
  extracted and averaged accordingly. You can choose up to which level
  of theory (DFT, RPA, BSE) the dielectric function is computed by
  commenting out the corresponding lines in the script (default is all
  the way up to BSE).
- Because of the shifted grids we have to use density functional
  perturbation theory to calculate the derivatives of the wave functions
  with respect to $\mathbf{k}$ and not
  the finite difference scheme. We also have to switch off all k-points
  symmetry in all [INCAR](../input-files/INCAR.md) files. These two
  important parameters look like the following in the
  [INCAR](../input-files/INCAR.md) file:

&nbsp;

    PREC = Normal ; ENCUT = 250.0
     
    ALGO = EXACT ; NELM = 1
    ISMEAR = 0 ; SIGMA = 0.01
    KPAR = 2

    NBANDS = 32 # The number of bands in the consecutive BSE calculation should be the same!  
    LOPTICS = .TRUE.; LPEAD = .FALSE.
    ISYM = -1
    OMEGAMAX = 40

- Finally the averaging over multiple grids should should give spectra
  that are in much closer agreement than the calculations using
  $4\times 4\times 4$ k-points:

[![](https://vasp.at/wiki/images/thumb/e/e0/Fig_BSE_example2_2.png/500px-Fig_BSE_example2_2.png)](https://vasp.at/wiki/File:Fig_BSE_example2_2.png)

### Model-BSE
The dielectric function $\epsilon^{-1}_{\mathbf{G},\mathbf{G'}} (\mathbf{q})$ is
replaced by the local model function:

${\varepsilon}_{\mathbf{G},\mathbf{G}}^{-1}(\mathbf{q})=1-(1-{{\varepsilon}_{\infty}^{-1}})\text{exp}(-\frac{|\mathbf{q+G}|^2}{4{\lambda}^2})$.

This makes the screened Coulomb kernel diagonal $(\mathbf{G}=\mathbf{G'})$ in the screened Coulomb potential:

$W^{cv\mathbf{k}}_{c'v'\mathbf{k}} = \frac{4\pi
e^{2}}{\Omega} \sum\limits_{\mathbf{G}}
\frac{\epsilon^{-1}_{\mathbf{G},\mathbf{G}}(\mathbf{0})}{|\mathbf{G}|^{2}}B^{c\mathbf{k}}_{c'\mathbf{k}}(\mathbf{G})
\[B^{v\mathbf{k}}_{v'\mathbf{k}}(\mathbf{G})\]^\*$,

where $B^{n\mathbf{k}}_{n'\mathbf{k}}(\mathbf{G})$ denote Bloch integrals of the cell-periodic part of the Bloch
waves.

- In addition to a model dielectric function we need approximate
  quasiparticle energies and wave functions.

Approximation:

- Use DFT single particle eigenvalues + SCISSOR (SCISSOR=GW band gap -
  DFT band gap).
- Use DFT single particle orbitals.

&nbsp;

- Extract $\mathbf{G}=\mathbf{G'}$
  dielectric function from the
  [vasprun.xml](../output-files/Vasprun.xml.md) file from the previous
  GW calculation using the script *./extract_die_G.sh vasprun.xml \>
  dieG_g6x6x6-GW0.dat'* or view the attached file *dieG_g6x6x6-GW0.dat*.
  Use [AEXX](../incar-tags/AEXX.md)=0.088 for $\epsilon^{-1}_{\infty}$ and
  [HFSCREEN](../incar-tags/HFSCREEN.md)=1.26 for $\lambda$.Then fit the model to get:

[![](https://vasp.at/wiki/images/thumb/7/70/Fig_BSE_example2_4.png/500px-Fig_BSE_example2_4.png)](https://vasp.at/wiki/File:Fig_BSE_example2_4.png)

- Check the GW+BSE and DFT+mBSE calculations for constistency:

[![](https://vasp.at/wiki/images/thumb/4/45/Fig_BSE_example2_5.png/500px-Fig_BSE_example2_5.png)](https://vasp.at/wiki/File:Fig_BSE_example2_5.png)

- The sequence of calculations as given in the script *doall-model.sh*
  consists of two steps:

&nbsp;

- Step 1: standard DFT calculation. The [INCAR](../input-files/INCAR.md)
  file (INCAR.DFT) for this step looks as follows:

&nbsp;

    PREC = Normal ; ENCUT = 250.0
    ISMEAR = 0 ; SIGMA = 0.01
    EDIFF = 1.E-8
    NBANDS = 16
    PRECFOCK = Normal
     
    #WAVEDER file must be made:
    LOPTICS = .TRUE.
    LPEAD = .TRUE.
    OMEGAMAX = 40

- Step2: model BSE calculation. The [INCAR](../input-files/INCAR.md) file
  (INCAR.mBSE) for this step looks as follows:

&nbsp;

    PREC = Normal ; ENCUT = 250.0
     
    ALGO = TDHF
    ANTIRES = 0 ; SIGMA = 0.01
    ENCUTGW = 150
     
    EDIFF = 1.E-8
    NBANDS = 16
    NBANDSO = 4
    NBANDSV = 8
    OMEGAMAX = 20

    PRECFOCK = Normal

    LMODELHF = .TRUE.
    HFSCREEN = 1.26
    AEXX = 0.088
    SCISSOR = 0.69

- Finally the result of the DFT+mBSE should be of similar accuracy as
  the GW+BSE calculations when compared to experiment:

[![](https://vasp.at/wiki/images/thumb/d/d7/Fig_BSE_example2_6.png/500px-Fig_BSE_example2_6.png)](https://vasp.at/wiki/File:Fig_BSE_example2_6.png)

## Download
[Si_improve_eps.tgz](https://vasp.at/wiki/images/e/e8/Si_improve_eps.tgz "Si improve eps.tgz")

## References
1.  [↑](#cite_ref-bokdam:scr:6_1-0) [M.Bokdam et al., Scientific Reports
    6, 28618 (2016).](https://www.nature.com/articles/srep28618)
2.  [↑](#cite_ref-liu:bse_2-0) [P.Liu et al., Phys. Rev. Materials 2,
    075003
    (2018).](https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.2.075003)

[Overview](../tutorials/BSE_-_Tutorial.md) \> [Dielectric
properties of Si using
BSE](Dielectric_properties_of_Si_using_BSE.md) \>
Improving the dielectric function  \> [Plotting the BSE fatband
structure of
Si](Plotting_the_BSE_fatband_structure_of_Si.md) \>
[List of tutorials](../categories/Category-Tutorials.md)
