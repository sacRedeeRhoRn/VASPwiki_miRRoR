<!-- Source: https://vasp.at/wiki/index.php/ML_REG | revid: 32828 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_REG


This file contains the regression results of the force field training
compared to the ab-initio training data in the last training step. This
file is written for
[`ML_MODE`](../incar-tags/ML_MODE.md)` = train, select`.

A sample output should look like the following:

    ****************************************************************************************************
         Results at         52 MD step.
    ====================================================================================================
         Total energies (eV)
    ----------------------------------------------------------------------------------------------------
           -16.991157   -17.523764
           -17.130082   -17.637286
           -17.327379   -17.802581
                  ...          ...
    ====================================================================================================
         Forces (eV ang.^-1)
    ----------------------------------------------------------------------------------------------------
             1.180622     0.723282
             0.136526     0.018732
            -0.033733     0.103882
             0.888107     0.516528
            -0.148552    -0.401311
             0.159014     0.315306
             0.689279     0.218246
             0.718439     0.750706
                  ...          ...
    ====================================================================================================
         Stress (kbar)
    ----------------------------------------------------------------------------------------------------
           208.393665   178.750015
            15.421420     8.376722
            -5.264501    -3.403226
                  ...          ...

The first column contains the ab-initio data. The second column contains
the fitted data.

- `Total energies (eV)`: The number of lines corresponds to the number
  of training structures (`The number of configurations` in the
  corresponding [ML_ABN](ML_ABN.md) file).
- `Forces (eV ang.^-1)`: Contains 3 lines (Cartesian directions) for
  each atom in each training structure. The direction varies first, then
  the atoms, and last the training structures.
- `Stress (kbar)`: Contains 6 lines for the tensor components of each
  training structure.

------------------------------------------------------------------------


