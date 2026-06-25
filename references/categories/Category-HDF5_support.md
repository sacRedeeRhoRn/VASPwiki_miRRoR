<!-- Source: https://vasp.at/wiki/index.php/Category:HDF5_support | revid: 35102 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Category:HDF5 support


Since VASP 6.2.0 we started supporting the feature of reading and
writing hdf5 files. The HDF5 file format
<sup>[\[1\]](#cite_note-hdf5format:web-1)</sup>
is a hierarchical data file designed to store large amounts of numeric
data. This file format combines the flexibility and hierarchy of an XML
file with the speed and size economy of binary files. The writing and
reading of hdf5 files are handled by the HDF5 library which is written
in C but wrappers for Fortran, python, and C++ are available.

Currently, VASP accepts the following HDF5 files:

|  |  |
|----|----|
| Filename | Usage |
| [vaspin.h5](../input-files/Vaspin.h5.md) | Contains the necessary inputs to start the calculation instead of [INCAR](../input-files/INCAR.md), [POSCAR](../input-files/POSCAR.md), [POTCAR](../input-files/POTCAR.md) and [KPOINTS](../input-files/KPOINTS.md) |
| [vaspout.h5](../output-files/Vaspout.h5.md) | Contains the outputs of the VASP calculation |
| [vaspwave.h5](../output-files/Vaspwave.h5.md) | Contains large output datasets usually stored in binary format when [LH5](../incar-tags/LH5.md)=.TRUE. (fine grained control still possible with [LWAVE](../incar-tags/LWAVE.md)=.TRUE. and [LCHARG](../incar-tags/LCHARG.md)=.TRUE.) |

To enable the reading and writing of these files, VASP should be
compiled with HDF5 support active. This is done by modifying the
[makefile.include](../misc/Makefile.include.md)
accordingly.

As of VASP 6.2.0 we only support reading/writing of hdf5 files in serial
mode. For extracting data from the
[vaspout.h5](../output-files/Vaspout.h5.md) file we strongly recommend
using the <a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> package.

## Command line tools\[<a
href="/wiki/index.php?title=Category:HDF5_support&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Command line tools">edit</a> \| (./index.php.md)\]

The HDF5 library ships with a series of command-line tools that can be
used to quickly inspect the contents of any HDF5 file.

In particular `h5ls` outputs the hierarchy of groups and datasets. It is
useful to check which data is present in the file. For example:

    $ h5ls vaspout.h5
    input                    Group
    intermediate             Group
    original                 Group
    results                  Group
    version                  Group

Adding the `-r` modifier lists the contents of the groups recursively,
giving an overview of the data contained in the file.

Another very useful tool is the `h5dump` command that with the
`-d variable_name` argument outputs the contents of the variable to the
screen. For example:

    $ h5dump -d /intermediate/ion_dynamics/energies vaspout.h5
    HDF5 "vaspout.h5" {
    DATASET "/intermediate/ion_dynamics/energies" {
       DATATYPE  H5T_IEEE_F64LE
       DATASPACE  SIMPLE { ( 1, 3 ) / ( H5S_UNLIMITED, 3 ) }
       DATA {
       (0,0): -11.8515, -11.8515, -11.8515
       }
    }
    }

The meaning of each of the energy values can be printed by replacing
`energies` by `energies_tags` in the command above. For a complete list
of HDF5 tools, the user is referred to the official HDF5 documentation
<sup>[\[2\]](#cite_note-hdf5tools:web-2)</sup>.

## References\[<a
href="/wiki/index.php?title=Category:HDF5_support&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-hdf5format:web_1-0)
    <a href="https://www.hdfgroup.org/solutions/hdf5/" class="external text"
    rel="nofollow">https://www.hdfgroup.org/solutions/hdf5/ (2023).</a>
2.  [↑](#cite_ref-hdf5tools:web_2-0)
    <a
    href="https://portal.hdfgroup.org/display/hdf5/hdf5+command-line+tools"
    class="external text"
    rel="nofollow">https://portal.hdfgroup.org/display/hdf5/hdf5+command-line+tools
    (2023).</a>


