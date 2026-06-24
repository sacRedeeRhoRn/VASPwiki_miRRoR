<!-- Source: https://vasp.at/wiki/index.php/ML_AB | revid: 32826 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# ML_AB
This file is used as input (with file name ML_AB) and output
([ML_ABN](../output-files/ML_ABN.md)) within the machine learning force
field method. It contains the collection of ab initio data from previous
calculations: Bravais matrices, atom positions, energies, forces, and
stress tensors. Depending on the mode of operation it is used in the
following ways:

- **[`ML_MODE`](../incar-tags/ML_MODE.md)` = train`, starting from
  scratch:** A complete [ML_ABN](../output-files/ML_ABN.md) file containing
  all ab initio data and the list of current local reference
  configurations is written whenever a learning step is performed (check
  the line `STATUS` in the log file
  [ML_LOGFILE](../output-files/ML_LOGFILE.md) for entries `learning` and
  `critical`).
- **[`ML_MODE`](../incar-tags/ML_MODE.md)` = train`, continuation run:**
  Same [ML_ABN](../output-files/ML_ABN.md) output as above. In addition,
  upon start-up, the user-provided ML_AB file is read and an initial
  machine-learned force field is generated from the contained data.
- **[`ML_MODE`](../incar-tags/ML_MODE.md)` = select`, reselection of
  local reference configurations:** Same [ML_ABN](../output-files/ML_ABN.md)
  output as for [`ML_MODE`](../incar-tags/ML_MODE.md)` = train`. The
  ML_AB file is read and the contained structures are fed sequentially
  to the on-the-fly training algorithm. The list of local reference
  configurations in the ML_AB file is ignored, however, a dummy section
  must still be present (see below).

|  |
|----|
| **Tip:** The ML_AB file is not required for [`ML_MODE`](../incar-tags/ML_MODE.md)` = run` (prediction only) because all necessary data (e.g. descriptors of local reference configurations) are already stored in the [ML_FF](ML_FF.md) file. |

An [ML_ABN](../output-files/ML_ABN.md) output file from
[`ML_MODE`](../incar-tags/ML_MODE.md)` = train, select` can always be
reused as input for
[`ML_MODE`](../incar-tags/ML_MODE.md)` = train, select` by just renaming
(copying) it to ML_AB.

## Contents

- [1 Example](#Example)
- [2 General format remarks](#General_format_remarks)
- [3 Header specification](#Header_specification)
- [4 Training structure data format](#Training_structure_data_format)
- [5 Merging different ML_AB files](#Merging_different_ML_AB_files)

## Example
As an example, here is a shortened version of an actual ML_AB file:

     1.0 Version
    **************************************************
         The number of configurations
    --------------------------------------------------
            299
    **************************************************
         The maximum number of atom type
    --------------------------------------------------
           5
    **************************************************
         The atom types in the data file
    --------------------------------------------------
         Pb I  C
         N  H
    **************************************************
         The maximum number of atoms per system
    --------------------------------------------------
                 96
    **************************************************
         The maximum number of atoms per atom type
    --------------------------------------------------
                 48
    **************************************************
         Reference atomic energy (eV)
    --------------------------------------------------
      -72.5297190000000       -35.4081430000000       -2.39269120000000
      -4.60003440000000       -1.12020270000000
    **************************************************
         Atomic mass
    --------------------------------------------------
       20.0000000000000        20.0000000000000        12.0110000000000
       14.0010000000000        8.00000000000000
    **************************************************
         The numbers of basis sets per atom type
    --------------------------------------------------
           130  1202   128
           125   790
    **************************************************
         Basis set for Pb
    --------------------------------------------------
              1      1
            100      8
              1      3
            100      4
              1      5
              1      6
     ...
     ...
     ...
    **************************************************
         Basis set for I
    --------------------------------------------------
              1      9
              1     10
            100     32
            100     31
              1     13
            100     29
              1     15
              1     16
     ...
     ...
     ...
    **************************************************
         Basis set for C
    --------------------------------------------------
            100     39
            101     40
            104     40
            101     39
            101     38
            108     40
            101     37
     ...
     ...
     ...
    **************************************************
         Basis set for N
    --------------------------------------------------
              1     41
            100     47
              1     43
              1     44
            100     45
              1     46
     ...
     ...
     ...
    **************************************************
         Basis set for H
    --------------------------------------------------
            101     96
            108     96
            101     95
            101     94
            108     95
            101     93
            101     92
     ...
     ...
     ...
    **************************************************
         Configuration num.      1
    ==================================================
         System name
    --------------------------------------------------
         Optimal
    ==================================================
         The number of atom types
    --------------------------------------------------
           5
    ==================================================
         The number of atoms
    --------------------------------------------------
             96
    **************************************************
         Atom types and atom numbers
    --------------------------------------------------
         Pb      8
         I      24
         C       8
         N       8
         H      48
    ==================================================
         CTIFOR
    --------------------------------------------------
       7.2153124269575984E-003
    ==================================================
         Primitive lattice vectors (ang.)
    --------------------------------------------------
       12.6230002000000       0.000000000000000E+000  0.000000000000000E+000
      0.000000000000000E+000   12.6230002000000       0.000000000000000E+000
      0.000000000000000E+000  0.000000000000000E+000   12.6322002000000
    ==================================================
         Atomic positions (ang.)
    --------------------------------------------------
       3.53104385888580        2.84086367297985        2.90622172474177
       9.81419124013876        2.65432768009571        3.05638374363947
       3.26003769786731        9.08189602171279        2.78238128942769
       9.68338433877730        9.01798419847282        3.33422943250601
       3.97567522985842        2.30549969401587        9.43194287333753
       10.2367187113626        2.60925731212548        9.47119538915201
       3.14970369394084        8.58643640964228        9.24921780934012
       9.89456550951183        9.28033187172892        9.29623786496524
       10.2580847101708        12.3062955711284        3.18366035907868
       3.82895321819843        12.3181255490181        2.42031967883849
     ...
     ...
     ...
    ==================================================
         Total energy (eV)
    --------------------------------------------------
      -1844.06244866897
    ==================================================
         Forces (eV ang.^-1)
    --------------------------------------------------
      2.660349497586850E-002 -4.547882666592111E-003  0.190783123263071
      0.130884508367191       0.299290099652476       1.596358887670635E-002
      3.408685056302496E-002 -4.091615555857331E-002  0.178271772476586
     -8.681206662816165E-002 -2.646077052932483E-002 -0.627496783708147
     -2.387963973365542E-002  0.272206550808848      -0.188554040851596
     -0.349175317569579       0.372666466514608       9.810640873955712E-002
      0.508292852334109       2.851700722091148E-002 -0.297636066674050
     -0.477466544993604      -0.767209034380190       0.537092981997701
      1.081052495208487E-002 -0.454162570762754      -2.885905409516716E-002
      5.233785861238309E-002 -4.907001101287316E-002  0.357709899123724
     ...
     ...
     ...
    ==================================================
         Stress (kbar)
    --------------------------------------------------
         XX YY ZZ
    --------------------------------------------------
      -12.6559383536223       -8.82753684858342       -13.1791695209263
    --------------------------------------------------
         XY YZ ZX
    --------------------------------------------------
      -1.91691819690402        2.12274173946129       0.103818583636094
    **************************************************
         Configuration num.      2
    ==================================================
     ...
     ...
     ...

## General format remarks
|  |
|----|
| **Important:** All element-dependent quantities must follow the order of the element entries given in the header entry named `The atom types in the data file`. |

- All element-type-dependent information is limited to 3 entries per
  line. For more than 3 types or multiples of 3, the entries are written
  over multiple lines.
- The order of the entries for the header and also the data is fixed.
- The ledger lines cannot be omitted. `*****` and `-----` lines for the
  header. `*****`, `-----` and `=====` lines for the data.

## Header specification
- `1.0 Version`: In the very beginning of the header this entry
  specifies to the version of the ML_AB file. If in the future the
  contents of the file will be changed or extended the version number
  will ensure I/O compatibility. If not stated otherwise use
  `1.0 Version`.
- `The number of configurations`: Total number of training structures
  stored in this ML_AB file.
- `The maximum number of atom type`: Total number of unique types listed
  in all structures (e.g. if the file contains some ab initio data for
  H₂O, some data for MgO and some data for NaCl, then the total number
  of types is 5).
- `The atom types in the data file`: Listing of all atom types (two
  characters for each type as in VASP) appearing in all structures.
  Multiple lines for more than 3 element types. Maximum 3 entries per
  line.
- `The maximum number of atoms per system`: The largest number of atoms
  within one structure among all training structures.
- `The maximum number of atoms per atom type`: The largest number of
  atoms per element within one structure among all elements within all
  training structures.
- `Reference atomic energy (eV)`: Reference atomic energies used in the
  calculation for each element type. Multiple lines for more than 3
  element types. Maximum 3 entries per line. This entry is only
  important for
  [`ML_ISCALE_TOTEN`](../incar-tags/ML_ISCALE_TOTEN.md)` = 1`.
- `Atomic mass`: Atomic mass of each element type (in u). Multiple lines
  for more than 3 element types. Maximum 3 entries per line.
- `The numbers of basis sets per atom type`: Number of local reference
  configurations for each type. Multiple lines for more than 3 element
  types. Maximum 3 entries per line.
- `Basis set for X`: List of local reference configurations for each
  type. This line is followed by a block with two columns. The first
  column denotes from which training structure the local reference
  configuration is taken. The second column is the index of the atom in
  the given training structure that is chosen as a local reference
  configuration. This whole block (together with the title line) is
  repeated for each element type in the force field. For
  [`ML_MODE`](../incar-tags/ML_MODE.md)` = select` this section is
  ignored and a new list of local reference configurations will be
  written to [ML_ABN](../output-files/ML_ABN.md). However, upon reading in
  the ML_AB file a dummy line (e.g. only one line with `1 1`) for each
  type still needs to be present (also set
  `The numbers of basis sets per atom type` to 1 in this case).

|  |
|----|
| **Warning:** The maximum number of the training structures [ML_MCONF](../incar-tags/ML_MCONF.md) and the maximum number of the local reference configurations [ML_MB](../incar-tags/ML_MB.md) in the [INCAR](INCAR.md) file have to be set larger than the entries `The number of configurations` and `The numbers of basis sets per atom type` in the ML_AB file, respectively. |

## Training structure data format
- `Configuration num. n`: Denotes the beginning of a structure in the
  training data. Training structures have to be numbered consecutively
  starting with 1.
- `System name`: Name of the structure, taken from the
  [POSCAR](POSCAR.md) file which was used to start the
  [`ML_MODE`](../incar-tags/ML_MODE.md)` = train` run. Copied from the
  input ML_AB file in case of
  [`ML_MODE`](../incar-tags/ML_MODE.md)` = select`. The length of system
  names is limited to 40 characters.
- `The number of atom types`: The number of atom types in the structure.
  Because the list of types in this structure has to be a subset of all
  types appearing in the ML_AB this number must be smaller or equal to
  the number given in the header section
  `The atom types in the data file`.
- `The number of atoms`: Number of atoms in the structure.
- `Atom types and atom numbers`: Atom types and the number of atoms per
  type in the structure. Each type is written on a separate line.
- `CTIFOR` (*optional*): Value of
  [ML_CTIFOR](../incar-tags/ML_CTIFOR.md) used while sampling this
  structure. Depending on
  [ML_ICRITERIA](../incar-tags/ML_ICRITERIA.md) the value may change
  between structures. This line is always present if the
  [ML_ABN](../output-files/ML_ABN.md) file was created by VASP with
  [`ML_MODE`](../incar-tags/ML_MODE.md)` = train`. Then, also
  continuation and re-selection runs with
  [`ML_MODE`](../incar-tags/ML_MODE.md)` = train, select` will write out
  current `CTIFOR` values in [ML_ABN](../output-files/ML_ABN.md) files. On
  the other hand, if ML_AB files are created from external training data
  this section may be omitted. In this case
  [`ML_MODE`](../incar-tags/ML_MODE.md)` = train, select` runs will also
  not include `CTIFOR` sections.

|  |
|----|
| **Warning:** Training structures with a value for `CTIFOR` and without must not be combined. Either `CTIFOR` is provided for all structures or none of them. |

- `Primitive lattice vectors (ang.)`: Bravais matrix of the structure,
  one line corresponds to one lattice vector. The unit of length units
  is Angstrom.
- `Atomic positions (ang.)`: Ionic positions in Cartesian coordinates
  (given in Angstrom). Note that the order of atoms needs to correspond
  to the atom types list in `Atom types and atom numbers`.
- `Total energy (eV)`: Total energy (in eV) of the structure.
- `Forces (eV ang.^-1)`: Forces (in eV/Angstrom) for each atom in the
  structure.
- `Stress (kbar)`: 6 entries for the stress tensor (in kb) of the
  structure.

## Merging different ML_AB files
Multiple ML_AB files may be merged by hand, keeping the following
restrictions and tips in mind:

- The training structure data can be simply concatenated, i.e., by just
  adding more structure sections starting with `Configuration num. n` at
  the end of the file. However, the structure numbering needs to be
  updated in such a way that they are enumerated continuously starting
  from 1.
- We strongly advise to group structures with the same number of
  elements and atoms per element in the training data together,
  otherwise the code will automatically reorder the data, such that
  those are sticking together. If one relies on the automatic reordering
  it will not be possible to easily "diff" the input ML_AB file and its
  corresponding [ML_ABN](../output-files/ML_ABN.md) output file.
- The header must be adjusted to reflect the combined number of element
  types, the maximum number of atoms, etc.
- The lists of local reference configurations cannot be easily merged
  (renumbering would be required). Instead, it is recommended to
  recalculate them using
  [`ML_MODE`](../incar-tags/ML_MODE.md)` = select`. However, to start
  with a valid ML_AB file first manually set
  `The numbers of basis sets per atom type` to 1 for each species. Also,
  set the block `Basis set for X` with dummy value `1 1` for each
  species. After running with
  [`ML_MODE`](../incar-tags/ML_MODE.md)` = select` the output
  [ML_ABN](../output-files/ML_ABN.md) will contain the selected new local
  reference configurations for the combined training data.

|  |
|----|
| **Tip:** If calculations for [`ML_MODE`](../incar-tags/ML_MODE.md)` = select` are too time consuming using the default settings it is useful to increase [ML_MCONF_NEW](../incar-tags/ML_MCONF_NEW.md) to values around 10-16 and set [`ML_CDOUB`](../incar-tags/ML_CDOUB.md)` = 4`. This often accelerates the calculations by a factor of 2-4. |

------------------------------------------------------------------------
