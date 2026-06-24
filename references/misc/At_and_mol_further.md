<!-- Source: https://vasp.at/wiki/index.php/At_and_mol_further | revid: 10408 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# At and mol further
[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O atom](O_atom.md) \> [O atom
spinpolarized](O_atom_spinpolarized.md) \> [O
atom spinpolarized low
symmetry](O_atom_spinpolarized_low_symmetry.md) \>
[O dimer](O_dimer.md) \> [CO](../incar-tags/CO.md) \> [CO
vibration](CO_vibration.md) \> [CO partial
DOS](CO_partial_DOS.md) \> [H2O](../incar-tags/H2O.md) \>
[H2O vibration](H2O_vibration.md) \> [H2O molecular
dynamics](H2O_molecular_dynamics.md) \>
Further things to try  \> [List of
tutorials](../categories/Category-Tutorials.md)

- How does the energy change when one decreases
  [SIGMA](../incar-tags/SIGMA.md) to 0.001 in the
  [INCAR](../input-files/INCAR.md) file starting from the \[\[O_atom? Why?

&nbsp;

- Try to copy [CONTCAR](../output-files/CONTCAR.md) to
  [POSCAR](../input-files/POSCAR.md) after running the example
  [O_dimer](O_dimer.md). Why is the calculation so fast?

&nbsp;

- Try to play with the parameter [POTIM](../incar-tags/POTIM.md) for the
  example [O_dimer](O_dimer.md). What is the optimal value?

&nbsp;

- What is the reason for the imaginary frequency in the example
  [CO_vibration](CO_vibration.md)? Does the behaviour
  improve when the step width (smaller or larger) is changed? Also try
  to improve the precision to which the ground state is converged
  ([EDIFF](../incar-tags/EDIFF.md)=1E-5). What happens if the accuracy of
  the calculations is improved ([PREC](../incar-tags/PREC.md)=*Accurate*).

&nbsp;

- Try to use the conjugate gradient algorithm to the
  $\mathrm{H}_{2}\mathrm{O}$ molecule
  (example [H2O](../incar-tags/H2O.md)).

&nbsp;

- Calculate the vibrational frequencies of the $\mathrm{H}_{2}\mathrm{O}$ molecule (example
  [H2O](../incar-tags/H2O.md)) after relaxation (example [H2O
  vibration](H2O_vibration.md)). Why does one find 3
  modes that have small frequencies? Try
  [EDIFF](../incar-tags/EDIFF.md)=1E-5 instead of
  [EDIFF](../incar-tags/EDIFF.md)=1E-4.

  

[Overview](../tutorials/Atoms_and_Molecules_-_Tutorial.md) \>
[O atom](O_atom.md) \> [O atom
spinpolarized](O_atom_spinpolarized.md) \> [O
atom spinpolarized low
symmetry](O_atom_spinpolarized_low_symmetry.md) \>
[O dimer](O_dimer.md) \> [CO](../incar-tags/CO.md) \> [CO
vibration](CO_vibration.md) \> [CO partial
DOS](CO_partial_DOS.md) \> [H2O](../incar-tags/H2O.md) \>
[H2O vibration](H2O_vibration.md) \> [H2O molecular
dynamics](H2O_molecular_dynamics.md) \>
Further things to try  \> [List of
tutorials](../categories/Category-Tutorials.md)
