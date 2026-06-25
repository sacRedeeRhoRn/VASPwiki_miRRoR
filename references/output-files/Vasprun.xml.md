<!-- Source: https://vasp.at/wiki/index.php/Vasprun.xml | revid: 37162 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# vasprun.xml


The vasprun.xml is written in
xml format and contains both, general output that is written for any
calculation and specific output depending on the method or quantity that
is being computed. Below you see details regarding the general output,
while the specific output, e.g. the dielectric function
([LOPTICS](../incar-tags/LOPTICS.md)), partial density of states
([LORBIT](../incar-tags/LORBIT.md)), the electronic self-energy
([LSELFENERGY](../incar-tags/LSELFENERGY.md)) etc., are detailed on
the corresponding tag documentation. Mind that newer features tend to
write to [vaspout.h5](Vaspout.h5.md). The
[vaspout.h5](Vaspout.h5.md) should generally be
preferred for reading large datasets.


## Contents


- [1 File
  format](#File_format)
- [2
  Sections](#Sections)
  - [2.1
    Generator](#Generator)
  - [2.2
    INCAR](#INCAR)
  - [2.3 Primitive
    cell](#Primitive_cell)
  - [2.4 k
    points](#k_points)
  - [2.5
    Parameters](#Parameters)
  - [2.6 Atom
    info](#Atom_info)
  - [2.7 Initial
    structure](#Initial_structure)
  - [2.8 Ionic
    steps](#Ionic_steps)
  - [2.9
    Electronic-structure calculation
    block](#Electronic-structure_calculation_block)
  - [2.10 Final
    structure](#Final_structure)
- [3 Reading
  vasprun.xml](#Reading_vasprun.xml)
  - [3.1
    pymatgen](#pymatgen)
  - [3.2
    ASE](#ASE)
  - [3.3 Direct XML
    parsing](#Direct_XML_parsing)
    - [3.3.1
      ElementTree](#ElementTree)
    - [3.3.2
      lxml](#lxml)
  - [3.4 Terminal
    commands](#Terminal_commands)
    - [3.4.1
      xmllint](#xmllint)
    - [3.4.2
      xmlstarlet](#xmlstarlet)
- [4 Related tags
  and articles](#Related_tags_and_articles)


## File format\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: File format">edit</a> \| (./index.php.md)\]

The root element is `<modeling>`. The file uses four repeating XML
primitives throughout:

- *`value`* — a named scalar (real, integer, logical, or string).
- `<v name="...">x y z</v>` — a named row vector.
- `<varray name="...">` — a named array of vectors, each on a `<v>`
  line.
- `<array>` — a labelled multi-field table with named dimensions; rows
  are stored as `<r>` elements inside `<set>` blocks.

The overall layout of
vasprun.xml is:


     <modeling>
       <generator>   ...  </generator>
       <incar>       ...  </incar>
       <primitive_cell> ... </primitive_cell>
       <kpoints>     ...  </kpoints>
       <parameters>  ...  </parameters>
       <atominfo>    ...  </atominfo>
       <structure name="initialpos"> ... </structure>
     
       <!-- one block per ionic step (MD, relaxation): -->
       <structure> ... </structure>
       <varray name="forces"> ... </varray>
       <varray name="stress"> ... </varray>
       <energy> ... </energy>
       <time name="totalsc"> ... </time>
       ...
     
       <!-- OR a single calculation block (single-point, GW, BSE): -->
       <calculation> ... </calculation>
     
       <structure name="finalpos"> ... </structure>
     </modeling>


## Sections\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Sections">edit</a> \| (./index.php.md)\]

### Generator\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Generator">edit</a> \| (./index.php.md)\]

Contains the VASP version, build details, and the date and time of the
run.


     <generator>
       <i name="program"    type="string">vasp </i>
       <i name="version"    type="string">6.5.0  </i>
       <i name="subversion" type="string">29Jan2024 (build Feb 14 2024) complex parallel</i>
       <i name="platform"   type="string">LinuxGNU </i>
       <i name="date"       type="string">2024 01 01 </i>
       <i name="time"       type="string">12:00:00 </i>
     </generator>


### INCAR\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: INCAR">edit</a> \| (./index.php.md)\]

Contains only the tags explicitly set in the
[INCAR](../input-files/INCAR.md) file, without defaults. This is a compact
record of the user-specified settings for the run.


     <incar>
       <i type="string" name="SYSTEM">diamond Si</i>
       <i type="string" name="ALGO">Normal</i>
       <i name="ENCUT">    500.00000000</i>
       <i type="int" name="ISMEAR">     0</i>
       <i name="SIGMA">      0.05000000</i>
     </incar>


### Primitive cell\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Primitive cell">edit</a> \| (./index.php.md)\]

Contains the structure and lattice of the primitive unit cell, along
with the mapping of primitive-cell ion indices to the full
simulation-cell ion indices.


     <primitive_cell>
       <structure name="primitive_cell">
         <crystal>
           <varray name="basis">            <!-- lattice vectors in A -->
             <v>  1.92  1.92  0.00 </v>
             <v>  0.00  1.92  1.92 </v>
             <v>  1.92  0.00  1.92 </v>
           </varray>
           <i name="volume">     28.35 </i>  <!-- volume in A^3 -->
           <varray name="rec_basis">        <!-- reciprocal lattice vectors in A^-1 -->
             <v>  0.26  0.26 -0.26 </v>
             <v> -0.26  0.26  0.26 </v>
             <v>  0.26 -0.26  0.26 </v>
           </varray>
         </crystal>
         <varray name="positions">          <!-- fractional (direct) coordinates -->
           <v> 0.00  0.00  0.00 </v>
           <v> 0.25  0.25  0.25 </v>
         </varray>
       </structure>
       <varray name="primitive_index">      <!-- index of each primitive ion in the full cell -->
         <v type="int"> 1 </v>
         <v type="int"> 2 </v>
       </varray>
     </primitive_cell>


### k points\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: k points">edit</a> \| (./index.php.md)\]

Specifies the **k**-point sampling of the Brillouin zone, mirroring the
[KPOINTS](../input-files/KPOINTS.md) file.


     <kpoints>
       <generation param="Gamma">             <!-- generation scheme: Gamma, Monkhorst-Pack, or Explicit -->
         <v type="int" name="divisions"> 4 4 4 </v>
         <v name="usershift"> 0.0  0.0  0.0 </v>
         <v name="genvec1">   0.25 0.00 0.00 </v>
         <v name="genvec2">   0.00 0.25 0.00 </v>
         <v name="genvec3">   0.00 0.00 0.25 </v>
         <v name="shift">     0.00 0.00 0.00 </v>
       </generation>
       <varray name="kpointlist">             <!-- '''k'''-point coordinates in reciprocal space -->
         <v>  0.000  0.000  0.000 </v>
         <v>  0.250  0.000  0.000 </v>
         ...
       </varray>
       <varray name="weights">               <!-- integration weights, normalized to sum to 1 -->
         <v> 0.00463 </v>
         <v> 0.03704 </v>
         ...
       </varray>
     </kpoints>


### Parameters\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Parameters">edit</a> \| (./index.php.md)\]

Contains a complete record of all effective [INCAR](../input-files/INCAR.md)
parameters, including those not set explicitly (with their default
values). The block is organized into named `<separator>` subsections
corresponding to groups of related tags, for example:

- `general`
- `electronic` (with sub-separators: `smearing`, `projectors`,
  `startup`, `spin`, `exchange-correlation`, `convergence`, `mixer`,
  `dipolcorrection`)
- `grids`
- `ionic` and `ionic md`
- `symmetry`
- `dos`
- `writing`
- `performance`
- `miscellaneous`
- `orbital magnetization`
- `response functions` (GW/BSE calculations)
- `vdW DFT`

There are several other groups that we have not included here. The full
documentation for each tag is found on its individual tag page.

### Atom info\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Atom info">edit</a> \| (./index.php.md)\]

Contains the atomic species and per-ion type information.


     <atominfo>
       <atoms> 2 </atoms>               <!-- total number of ions -->
       <types> 1 </types>               <!-- number of distinct species -->
       <array name="atoms">             <!-- per-ion element label and type index -->
         <dimension dim="1">ion</dimension>
         <field type="string">element</field>
         <field type="int">atomtype</field>
         <set>
           <rc><c>Si </c><c>   1</c></rc>
           <rc><c>Si </c><c>   1</c></rc>
         </set>
       </array>
       <array name="atomtypes">         <!-- per-species data -->
         <dimension dim="1">type</dimension>
         <field type="int">atomspertype</field>
         <field type="string">element</field>
         <field>mass</field>            <!-- atomic mass in u -->
         <field>valence</field>         <!-- number of valence electrons -->
         <field type="string">pseudopotential</field>   <!-- PAW potential label -->
         <set>
           <rc><c>   2</c><c>Si </c><c>     28.08500000</c><c>      4.00000000</c><c>PAW_PBE Si 05Jan2001</c></rc>
         </set>
       </array>
     </atominfo>


### Initial structure\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Initial structure">edit</a> \| (./index.php.md)\]

The ionic positions at the start of the run, read from
[POSCAR](../input-files/POSCAR.md). For
[molecular-dynamics](../categories/Category-Molecular_Dynamics.md)
runs, this block also contains the initial ionic velocities.


     <structure name="initialpos">
       <crystal>
         <varray name="basis">            <!-- lattice vectors in A -->
           <v>  5.43  0.00  0.00 </v>
           <v>  0.00  5.43  0.00 </v>
           <v>  0.00  0.00  5.43 </v>
         </varray>
         <i name="volume">   160.10 </i>  <!-- cell volume in A^3 -->
         <varray name="rec_basis">
           <v>  0.184  0.000  0.000 </v>
           <v>  0.000  0.184  0.000 </v>
           <v>  0.000  0.000  0.184 </v>
         </varray>
       </crystal>
       <varray name="positions">          <!-- fractional (direct) coordinates -->
         <v>  0.000  0.000  0.000 </v>
         <v>  0.250  0.250  0.250 </v>
       </varray>
       <!-- MD only: -->
       <varray name="velocities">         <!-- ionic velocities in A/fs -->
         <v>  0.0005 -0.0004  0.0002 </v>
         <v> -0.0009  0.0004  0.0005 </v>
       </varray>
     </structure>


### Ionic steps\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: Ionic steps">edit</a> \| (./index.php.md)\]

For runs with ionic motion
([relaxations](../categories/Category-Ionic_minimization.md),
[MD](../categories/Category-Molecular_Dynamics.md),
[NEB](https://vasp.at/wiki/index.php/Category:Transition_states)),
each ionic step is written as a sequence of flat blocks directly under
`<modeling>`. There is no enclosing `<calculation>` element; each step
contains:


     <!-- ionic step i (repeated for each step) -->
     <structure>
       <crystal>
         <varray name="basis"> ... </varray>
         <i name="volume"> ... </i>
         <varray name="rec_basis"> ... </varray>
       </crystal>
       <varray name="positions"> ... </varray>   <!-- fractional coordinates -->
     </structure>
     <varray name="forces">               <!-- Hellmann-Feynman forces in eV/A -->
       <v>  0.12 -0.03  0.00 </v>
       ...
     </varray>
     <varray name="stress">               <!-- stress tensor in kB -->
       <v> -0.16  0.00  0.11 </v>
       <v>  0.00  0.00  0.00 </v>
       <v>  0.11  0.00 -0.08 </v>
     </varray>
     <energy>
       <i name="e_fr_energy"> -53.93 </i>  <!-- free energy F = E - TS (eV) -->
       <i name="e_wo_entrp">  -53.93 </i>  <!-- energy without entropy (eV) -->
       <i name="e_0_energy">  -53.93 </i>  <!-- energy extrapolated to sigma->0 (eV) -->
       <!-- MD only: -->
       <i name="kinetic">       0.10 </i>  <!-- ionic kinetic energy (eV) -->
       <i name="lattice kinetic"> 0.00 </i> <!-- lattice kinetic energy, e.g. for NPT (eV) -->
       <i name="total">       -53.83 </i>  <!-- total energy E + E_kin, conserved in NVE (eV) -->
     </energy>
     <time name="totalsc"> 0.04 0.01 </time>   <!-- CPU and wall time for this step (s) -->


|  |
|----|
| **Mind:** For [IBRION](../incar-tags/IBRION.md)=0 ([MD](../categories/Category-Molecular_Dynamics.md)) with a large number of steps ([NSW](../incar-tags/NSW.md) \>\> 1), vasprun.xml can become very large. Consider using [vaspout.h5](Vaspout.h5.md) instead, or reading with a streaming XML parser (see [below](#Direct_XML_parsing)). |

### Electronic-structure calculation block\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Electronic-structure calculation block">edit</a> \| (./index.php.md)\]

For a [single-point electronic minimization
calculations](../tutorials/Setting_up_an_electronic_minimization.md)
([`NSW`](../incar-tags/NSW.md)` = 0`) and [post-DFT
methods](../categories/Category-Many-body_perturbation_theory.md)
(GW, BSE), a single `<calculation>` block instead of per-step ionic-step
blocks is written. It contains eigenvalues, the density of states (DOS),
the partial DOS ([LORBIT](../incar-tags/LORBIT.md)) and, for optical
calculations, the dielectric function
([LOPTICS](../incar-tags/LOPTICS.md)).

For <a href="/wiki/GW_calculations" class="mw-redirect"
title="GW calculations">GW calculations</a> (e.g.,
[ALGO](../incar-tags/ALGO.md)=EVGW0 or GW0), `<eigenvalues>` contains the
quasiparticle energies updated by the GW self-energy. Multiple
`<dielectricfunction>` blocks appear in the same `<calculation>`, each
labelled by its `comment` attribute.

### Final structure\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=12"
class="mw-editsection-visualeditor"
title="Edit section: Final structure">edit</a> \| (./index.php.md)\]

The ionic positions at the end of the run. For
<a href="/wiki/MD_runs" class="mw-redirect" title="MD runs">MD runs</a>,
this block also contains the final ionic velocities (also see
[VELOCITY](../incar-tags/VELOCITY.md) for
[vaspout.h5](Vaspout.h5.md) output), suitable for
restarting the trajectory.


     <structure name="finalpos">
       <crystal>
         <varray name="basis"> ... </varray>
         <i name="volume"> ... </i>
         <varray name="rec_basis"> ... </varray>
       </crystal>
       <varray name="positions"> ... </varray>
       <!-- MD only: -->
       <varray name="velocities"> ... </varray>
     </structure>


## Reading vasprun.xml\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=13"
class="mw-editsection-visualeditor"
title="Edit section: Reading vasprun.xml">edit</a> \| (./index.php.md)\]

### pymatgen\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=14"
class="mw-editsection-visualeditor"
title="Edit section: pymatgen">edit</a> \| (./index.php.md)\]

The <a href="https://pymatgen.org" class="external text"
rel="nofollow">pymatgen</a> library provides the `Vasprun` class:


    from pymatgen.io.vasp import Vasprun

    vr = Vasprun("vasprun.xml")

    print(vr.final_energy)        # total energy of the final ionic step (eV)

    # Iterate over ionic steps
    for step in vr.ionic_steps:
        e = step["electronic_steps"][-1]["e_fr_energy"]
        print(e)

    print(vr.final_structure)     # pymatgen Structure object
    dos = vr.complete_dos         # total and projected DOS


### ASE\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=15"
class="mw-editsection-visualeditor"
title="Edit section: ASE">edit</a> \| (./index.php.md)\]

The <a href="https://wiki.fysik.dtu.dk/ase/" class="external text"
rel="nofollow">Atomic Simulation Environment</a> (ASE) reads
vasprun.xml as a sequence of
`Atoms` objects:


    from ase.io import read

    images = read("vasprun.xml", index=":")   # all ionic steps
    atoms  = images[-1]                       # final structure

    print(atoms.get_potential_energy())       # total energy (eV)
    print(atoms.get_forces())                 # forces (eV/Å)


### Direct XML parsing\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=16"
class="mw-editsection-visualeditor"
title="Edit section: Direct XML parsing">edit</a> \| (./index.php.md)\]

#### ElementTree\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=17"
class="mw-editsection-visualeditor"
title="Edit section: ElementTree">edit</a> \| (./index.php.md)\]

For custom workflows, parse
vasprun.xml with Python's
standard library:


    import xml.etree.ElementTree as ET

    tree = ET.parse("vasprun.xml")
    root = tree.getroot()

    # Read INCAR tags
    for tag in root.find("incar"):
        print(tag.attrib.get("name"), "=", tag.text.strip())

    # Read forces from each ionic step
    for forces in root.iter("varray"):
        if forces.attrib.get("name") == "forces":
            data = [[float(x) for x in v.text.split()] for v in forces]
            print(data)


|  |
|----|
| **Mind:** For large MD trajectories, use `xml.etree.ElementTree.iterparse` to stream the file element by element and avoid loading it entirely into memory. |

#### lxml\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=18"
class="mw-editsection-visualeditor"
title="Edit section: lxml">edit</a> \| (./index.php.md)\]

There are also plenty of other Python packages that can be used to read
vasprun.xml, e.g., `lxml`:


    from lxml import etree

    # Parse XML
    tree = etree.parse("vasprun.xml")
    root = tree.getroot()

    # Read INCAR tags
    incar = root.find("incar")

    for tag in incar:
        name = tag.attrib.get("name")
        value = tag.text.strip() if tag.text else None
        print(name, "=", value)

    # Read the final energy
    energies = root.xpath(".//i[@name='e_0_energy']/text()")
    final_energy = float(energies[-1])

    print(final_energy)

    # Read forces from each ionic step
    forces_blocks = root.xpath(".//varray[@name='forces']")

    for forces in forces_blocks:
        data = [
            [float(x) for x in v.text.split()]
            for v in forces
        ]
        print(data)


There are plenty of other Python packages that can be used, or other
languages if you prefer, which we will not describe here.

### Terminal commands\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=19"
class="mw-editsection-visualeditor"
title="Edit section: Terminal commands">edit</a> \| (./index.php.md)\]

#### xmllint\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=20"
class="mw-editsection-visualeditor"
title="Edit section: xmllint">edit</a> \| (./index.php.md)\]

The <a href="https://xmllint.com/" class="external text"
rel="nofollow">xmllint</a> tool can be used to view the contents of the
vasprun.xml file based from
command line. E.g.,


     xmllint --xpath '//dos/partial' vasprun.xml


will print the partial density of states to terminal.

#### xmlstarlet\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=21"
class="mw-editsection-visualeditor"
title="Edit section: xmlstarlet">edit</a> \| (./index.php.md)\]

Alternatively, the
<a href="https://xmlstar.sourceforge.net/" class="external text"
rel="nofollow">xmlstarlet</a> tool can be used
vasprun.xml, e.g.,


     xmlstarlet sel -t -c '//dos/partial' vasprun.xml


will print the partial density of states to terminal.

There are several other command line tools that can be used for
analysis, e.g.,
<a href="https://pymatgen.org/#pmg-command-line-interface"
class="external text" rel="nofollow">mpg</a> that we will not go into
detail in here.

## Related tags and articles\[<a
href="/wiki/index.php?title=Vasprun.xml&amp;veaction=edit&amp;section=22"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [OUTCAR](OUTCAR.md) — the human-readable logfile.
- [vaspout.h5](Vaspout.h5.md) — the HDF5 alternative to
  vasprun.xml, preferred for
  large runs and newer features.


