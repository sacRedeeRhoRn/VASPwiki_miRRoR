<!-- Source: https://vasp.at/wiki/index.php/Sampling_phonon_spectra_from_molecular-dynamics_simulations | revid: 35856 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Sampling phonon spectra from molecular-dynamics simulations


<figure typeof="mw:File/Thumb">
<a href="/wiki/File:PhononDOS.png" class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/4/49/PhononDOS.png/500px-PhononDOS.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/4/49/PhononDOS.png 1.5x" width="500"
height="375" /></a>
<figcaption>Fig. 1: <strong>Left:</strong> Shows convergence analysis of
normalized velocity-autocorrelation function. <strong>Right:</strong>
Convergence analysis of phonon DOS.</figcaption>
</figure>

[Phonon](../categories/Category-Phonons.md) spectra can be
obtained as the power spectrum of the normalized
velocity-autocorrelation function
<sup>[\[1\]](#cite_note-reissland:book:1973-1)[\[2\]](#cite_note-lahnsteiner:prb:2022-2)</sup>.
The velocities of the ions and hence the velocity-autocorrelation
function are recorded during a [molecular dynamics (MD)
simulation](https://vasp.at/wiki/index.php/Category:Molecular_dynamics).
Fig. 1 shows the example of CsPbBr\$_3\$ which is discussed in more
detail below.

In contrast to [the phonon DOS computed by Fourier interpolation of the
force-constant
matrix](Computing_the_phonon_dispersion_and_DOS.md),
analyzing the power spectrum does not rely on mapping to a model
Hamiltonian. It naturally accounts for anharmonic contributions, as well
as temperature dependence.


## Contents


- [1 Phonon spectra
  step-by-setp](#Phonon_spectra_step-by-setp)
  - [1.1 Step 1:
    Generate thermalized initial
    structures](#Step_1:_Generate_thermalized_initial_structures)
  - [1.2 Step 2:
    Sample velocities from NVE simulations for each initial
    structure](#Step_2:_Sample_velocities_from_NVE_simulations_for_each_initial_structure)
  - [1.3 Step 3:
    Compute normalized velocity autocorrelation function for each NVE
    simulation](#Step_3:_Compute_normalized_velocity_autocorrelation_function_for_each_NVE_simulation)
  - [1.4 Step 4:
    Compute the power spectrum for each normalized velocity
    autocorrelation
    function](#Step_4:_Compute_the_power_spectrum_for_each_normalized_velocity_autocorrelation_function)
  - [1.5 Step 5:
    Compute averages and check for
    convergence](#Step_5:_Compute_averages_and_check_for_convergence)
- [2
  Example](#Example)
  - [2.1 Setup and
    auxilary scripts](#Setup_and_auxilary_scripts)
  - [2.2 Anharmonic
    ratteling in
    CsPbBr\$_{3}\$](#Anharmonic_ratteling_in_CsPbBr$_%7B3%7D$)
- [3
  References](#References)
- [4 Related tags
  and articles](#Related_tags_and_articles)


## Phonon spectra step-by-setp\[<a
href="/wiki/index.php?title=Sampling_phonon_spectra_from_molecular-dynamics_simulations&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Phonon spectra step-by-setp">edit</a> \| (./index.php.md)\]

For the setup of the
<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">MD simulation</a> and choice of
[ensemble](../categories/Category-Ensembles.md), two aspects
need to be taken into account:

1.  To have a well-defined reciprocal space, the simulation has to be
    done at constant volume.
2.  To probe the velocity-autocorrelation function, no thermostat should
    interfere with the recorded velocities.

Hence, the following describes how to compute the **phonon spectra** by
sampling an [NVE ensemble](../misc/NVE_ensemble.md) starting
from thermalized structures.

### Step 1: Generate thermalized initial structures\[<a
href="/wiki/index.php?title=Sampling_phonon_spectra_from_molecular-dynamics_simulations&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: Step 1: Generate thermalized initial structures">edit</a> \| (./index.php.md)\]

Run an [NVT simulation](../misc/NVT_ensemble.md) using the
[Langevin thermostat](Langevin_thermostat.md)
to generate thermalized initial structures. The choice of thermostat is
crucial. The [Langevin
thermostat](Langevin_thermostat.md) is
well-suited because it is a stochastic
<a href="/wiki/Thermostat" class="mw-redirect"
title="Thermostat">thermostat</a> and populates all available
<a href="/wiki/Phonon" class="mw-redirect" title="Phonon">phonon</a>
modes of our system uniformly, as white noise is added to the velocity
autocorrelation due to random forces in each time step. The size of the
system must be chosen such that the dimensions of the supercell are
large enough to accommodate the
<a href="/wiki/Phonon" class="mw-redirect" title="Phonon">phonon</a>
modes. Ideally, the time step ([POTIM](../incar-tags/POTIM.md)) is chosen
such that the frequency of the fastest phonon mode of interest can still
be resolved. Run the [NVT simulation](../misc/NVT_ensemble.md)
until the system is thermalized. Then, sample approximately 10
structures from the MD trajectory with a spacing of one or two times the
self-correlation time and store the initial structures as
[POSCAR](../input-files/POSCAR.md) files.

### Step 2: Sample velocities from NVE simulations for each initial structure\[<a
href="/wiki/index.php?title=Sampling_phonon_spectra_from_molecular-dynamics_simulations&amp;veaction=edit&amp;section=3"
class="mw-editsection-visualeditor"
title="Edit section: Step 2: Sample velocities from NVE simulations for each initial structure">edit</a> \| (./index.php.md)\]

For each initial structure, perform an [NVE
simulation](../misc/NVE_ensemble.md) with
[VELOCITY](../incar-tags/VELOCITY.md) = True . The minimum simulation
time requires roughly two slowest phonon cycles, which is dictated by
the decay time of a preliminary trajectory's normalized velocity
autocorrelation function to zero. The velocities are written to
[vaspout.h5](../output-files/Vaspout.h5.md) and can be accessed using
<a href="https://vasp.at/py4vasp/latest/index.html"
class="external text" rel="nofollow">py4vasp</a> with


    import py4vasp as pv
    calc = pv.Calculation.from_path("path/to/calc")
    velocity_dict = calc.velocity[:].read()


### Step 3: Compute normalized velocity autocorrelation function for each NVE simulation\[<a
href="/wiki/index.php?title=Sampling_phonon_spectra_from_molecular-dynamics_simulations&amp;veaction=edit&amp;section=4"
class="mw-editsection-visualeditor"
title="Edit section: Step 3: Compute normalized velocity autocorrelation function for each NVE simulation">edit</a> \| (./index.php.md)\]

The **normalized velocity autocorrelation function** for an
\$N\$-particle system is given by \begin{equation}
f(t)=\sum\_{s=1}^{types}f\_{s}(t)=\frac{\langle
\sum\_{s=1}^{types}\sum\_{i=1}^{N\_{s}}\mathbf{v}\_{i}(\Delta
T)\mathbf{v}\_{i}(\Delta T+t) \rangle}{\mathbf{v}\_{i}(\Delta
T)\mathbf{v}\_{i}(\Delta T)}. \end{equation} The brackets \$\langle
,\rangle\$ denote a thermal average which has to be computed over
different MD trajectories and starting times \$\Delta T\$ within each
trajectory. The sum over \$i\$ runs over the atoms within each species,
and the sum \$s\$ is over all atomic species contained in the simulated
system.

### Step 4: Compute the power spectrum for each normalized velocity autocorrelation function\[<a
href="/wiki/index.php?title=Sampling_phonon_spectra_from_molecular-dynamics_simulations&amp;veaction=edit&amp;section=5"
class="mw-editsection-visualeditor"
title="Edit section: Step 4: Compute the power spectrum for each normalized velocity autocorrelation function">edit</a> \| (./index.php.md)\]

The phonon spectral function is the power spectrum of \$f_{s}(t)\$ and
is obtained by performing the following Fourier transformation:
\begin{equation} g(\omega)=\sum\_{s=1}^{types}g\_{s}(\omega)=\left\|
\sum\_{s=1}^{types}\int\_{-\infty}^{\infty}f\_{s}(t)e^{-i\omega
t}\right\|^{2}. \end{equation}

### Step 5: Compute averages and check for convergence\[<a
href="/wiki/index.php?title=Sampling_phonon_spectra_from_molecular-dynamics_simulations&amp;veaction=edit&amp;section=6"
class="mw-editsection-visualeditor"
title="Edit section: Step 5: Compute averages and check for convergence">edit</a> \| (./index.php.md)\]

To check for convergence, \$f(t)\$ and \$g(\omega)\$ obtained for each
[NVE trajectory](../misc/NVE_ensemble.md) can be successively
averaged. To this end, plot a single trajectory, compared to an average
over 2 trajectories, and so on. If needed, the above steps can be
repeated to generate additional data to reach the desired accuracy.

|  |
|----|
| **Tip:** For further information on phonon signal analysis Ref<sup>[\[2\]](#cite_note-lahnsteiner:prb:2022-2)</sup> might be a helpful source. |

## Example\[<a
href="/wiki/index.php?title=Sampling_phonon_spectra_from_molecular-dynamics_simulations&amp;veaction=edit&amp;section=7"
class="mw-editsection-visualeditor"
title="Edit section: Example">edit</a> \| (./index.php.md)\]

### Setup and auxilary scripts\[<a
href="/wiki/index.php?title=Sampling_phonon_spectra_from_molecular-dynamics_simulations&amp;veaction=edit&amp;section=8"
class="mw-editsection-visualeditor"
title="Edit section: Setup and auxilary scripts">edit</a> \| (./index.php.md)\]

First, create thermalized initial structures. A simple
[INCAR](../input-files/INCAR.md) file, which will perform an [NVT
simulation](../misc/NVT_ensemble.md) could look as follows

    # INCAR molecular-dynamics tags NVE ensemble 
    IBRION = 0                   # choose molecular-dynamics 
    ISIF = 0                     # save time. No stress tensor. Box shape fixed.
    MDALGO = 3                   # using Langevin thermostat
    TEBEG = 500                  # set temperature 
    LANGEVIN_GAMMA = 0.5 0.5 0.5 # Langevin friction coefficient for 3 atomic species
    NSW = 10000                  # number of time steps 
    POTIM = 2.0                  # time step in femto seconds 

A bash script to produce 10 starting configurations in the form of
[POSCAR](../input-files/POSCAR.md) files could look as follows

    # Equilibrate.sh script to generate POSCAR_1 to POSCAR_10 
    for i in {1..10}; do
       cp POSCAR POSCAR_$i
       mpirun -np 32 vasp_std
       cp CONTCAR CONTCAR_$i
       cp CONTCAR POSCAR
    done

This bash script will create [POSCAR](../input-files/POSCAR.md)\_i where
\$i\$ runs from 1 to 10. These serve as initial structures including
inital velocities for the [NVE
simulations](../misc/NVE_ensemble.md).

Secondly, sample velocities from [NVE
simulations](../misc/NVE_ensemble.md) for each initial
structure. An [INCAR](../input-files/INCAR.md) file can look as follows:

    # INCAR molecular-dynamics tags NVE ensemble 
    IBRION = 0                   # choose molecular-dynamics
    ISIF = 0                     # save time. No stress tensor. Box shape fixed. 
    MDALGO = 1                   # using Andersen thermostat
    ANDERSEN_PROB = 0.0          # setting Andersen collision probability to zero to get NVE ensemble
    TEBEG = 500                  # set temperature 
    NSW = 10000                  # number of time steps 
    POTIM = 2.0                  # time step in femto seconds 
    VELOCITY = T                 # make sure to write velocities to vaspout.h5

Again, it is advisable to use a script to generate NVE trajectories. The
following bash script will assume a base folder containing
[POSCAR](../input-files/POSCAR.md) files named
[POSCAR](../input-files/POSCAR.md)\_1 to
[POSCAR](../input-files/POSCAR.md)\_10, an [INCAR](../input-files/INCAR.md)
file, a [KPOINTS](../input-files/KPOINTS.md) file and an
[POTCAR](../input-files/POTCAR.md) file. The script will create folders
`Run1` to `Run10`. Each folder will contain a
[vaspout.h5](../output-files/Vaspout.h5.md) file after script execution.
These [vaspout.h5](../output-files/Vaspout.h5.md) files will be needed
for the analysis scripts of the next section.

    # Run NVE MD simulation for each inital configuration
    for i in {1..10}; do
       mkdir Run$i
       cd Run$i
       cp ../INCAR .
       cp ../KPOINTS .
       cp ../POSCAR_${i} POSCAR
       vasp_std
       cd ..
    done

The following Python script can be used to compute normalized
velocity-autocorrelation functions


**Click to show ComputeCorrelation.py**


    import numpy as np
    class AutoCorrelation:
        """
        A class to compute the velocity auto-correlation function for a given set of velocity data.

        Attributes:
        -----------
        delta : int, optional
            The step size for time intervals in the computation (default is 1).

        Methods:
        --------
        velocity_auto_correlation(velos):
            Computes the velocity auto-correlation function for the input velocity data.
        """
        def __init__( self, delta = 1 ):
            """
            Initializes the AutoCorrelation object with a specified time step size.

            Parameters:
            -----------
            delta : int, optional
                The step size for time intervals in the computation (default is 1).
            """
            self.delta = delta
        def velocity_auto_correlation( self, velos ):
            """
            Computes the velocity auto-correlation function for the given velocity data.

            Parameters:
            -----------
            velos : numpy.ndarray
                A 3D array of shape (Nt, Nx, Ndim) representing the velocity data, where:
                - Nt is the number of time steps,
                - Nx is the number of particles,
                - Ndim is the number of spatial dimensions.

            Returns:
            --------
            numpy.ndarray
                A 2D array of shape (Nt // 2, Nx) representing the velocity auto-correlation function
                for each particle over time.

            Notes:
            ------
            - The function normalizes the correlation values using the squared norm of the initial velocities.
            - The computation is performed for time intervals up to Nt // 2.
            """
            Nt, Nx, Ndim = velos.shape
            deltaT = self.delta
            corr_func = np.zeros( [ Nt // 2, Nx ] )
            counter   = np.zeros( [ Nt // 2, 1 ] )
            for dt in range( 0, Nt//2, deltaT ):
                v0   = velos[ dt, :, : ]
                norm = np.asarray( [ np.linalg.norm( v0[ i, : ] )**2 for i in range( Nx ) ] )
                for t in range( dt, Nt//2 ):
                    vt = velos[ t, :, : ]
                    value = np.asarray( [ np.dot( vt[i,:], v0[ i, : ] ) for i in range( Nx ) ] )
                    corr_func[ t-dt, : ] += value / norm
                    counter[ t-dt ] += 1
            return corr_func / counter


The following python script can be used to obtain the phonon density of
states by computing the power spectra of the normalized velocity auto
correlation functions.


**Click to show PhononDOS.py**


    import sys
    import py4vasp
    import numpy as np
    import matplotlib.pyplot as plt


    import ComputeCorrelation
        
    class ComputePhonons:
        """
        @brief Class to compute phonon-related properties such as autocorrelation, power spectra, and averages.
        
        This class provides methods to compute velocity autocorrelation, power spectra, and averages for atomic systems 
        based on velocity data. It also includes functionality to write the computed data to files.
        
        @class ComputePhonons
        """
        def __init__( self, fname, dt = 1.0, timeShift=50 ):
            """
            @brief Constructor to initialize the ComputePhonons object.
            @param fname Path to the input file for the calculation.
            @param dt Time step in femtoseconds (default: 1.0).
            @param timeShift Time shift for autocorrelation computation (default: 50).
            """
            self.fname  =  fname
            self.calc   =  py4vasp.Calculation.from_path( self.fname )
            self.velos  =  self.calc.velocity[:].read()
            self.time_step =  dt /1000 # thz output
            self.timeShift = timeShift

        def compute_ac( self ):
            """
            @brief Compute the velocity autocorrelation function.
            This method calculates the velocity autocorrelation function using the provided velocity data.
            """
            dos     =  ComputeCorrelation.AutoCorrelation( self.timeShift )
            self.ac =  dos.velocity_auto_correlation( self.velos["velocities"] )

        def compute_averages( self ):
            """
            @brief Compute averages of the autocorrelation function for total and per-atom contributions.
            This method calculates the total autocorrelation and groups the autocorrelation by atomic species.
            """
            unique, counts = np.unique_counts( self.velos["structure"]["elements"] )
            self.total_ac = np.sum( self.ac, axis=1 )
            labels = self.velos["structure"]["elements"]
            unique_labels, inverse = np.unique(labels, return_inverse=True)
            result = np.zeros((self.ac.shape[0], len(unique_labels)), dtype=self.ac.dtype)
            np.add.at(result, (slice(None), inverse), self.ac )
            self.atom_ac = {label: result[:, i] for i, label in enumerate(unique_labels)}

        def compute_power_spectra( self ):
            """
            @brief Compute the power spectra for total and per-atom contributions.
            This method calculates the power spectra using the Fourier transform of the autocorrelation functions.
            """
            self.ps_total = np.abs( np.fft.fft( self.total_ac ) )**2
            self.ps_atom  = {}
            for key in self.atom_ac.keys():
                self.ps_atom[key] = np.abs( np.fft.fft( self.atom_ac[key] ) )**2
            
            freqs = np.fft.fftfreq( self.ps_total.shape[0], self.time_step )
            self.ps_total = np.vstack( [freqs, self.ps_total/np.max(self.ps_total)] ).T
            self.ps_total = self.ps_total[ :self.ps_total.shape[0]//2, : ]
            for key in self.ps_atom.keys():
                self.ps_atom[key] = np.vstack( [freqs, self.ps_atom[key]/np.max( self.ps_atom[key] )] ).T
                self.ps_atom[key] = self.ps_atom[key][ :self.ps_atom[key].shape[0]//2, : ] 

        def write_total_ps( self, fname="total_ps.dat" ):
            """
            @brief Write the total power spectrum to a file.
            @param fname Name of the output file (default: "total_ps.dat").
            """
            np.savetxt( fname, self.ps_total )

        def write_total_ac( self, fname="total_ac.dat" ):
            """
            @brief Write the total autocorrelation function to a file.
            @param fname Name of the output file (default: "total_ac.dat").
            """
            x = np.linspace( 0, self.time_step*self.total_ac.shape[0], self.total_ac.shape[0] )
            result = np.vstack( [x, self.total_ac] ).T
            np.savetxt( fname, result )
        
        def write_atom_ac( self ):
            """
            @brief Write the per-atom autocorrelation functions to files.
            Each atomic species' autocorrelation function is written to a separate file.
            """
            for key in self.ps_atom.keys():
                np.savetxt( f"{key}_ps.dat", self.ps_atom[key] )
     
         def write_atom_ps( self ):
             """
             @brief Write the per-atom power spectra to files.
             Each atomic species' power spectrum is written to a separate file.
             """
             for key in self.ps_atom.keys():
                 np.savetxt( f"{key}_ps.dat", self.ps_atom[key] )
     
     
     if __name__=="__main__":
         x = ComputePhonons( sys.argv[1], float(sys.argv[2]) )
         x.compute_ac()
         x.compute_averages()
         x.compute_power_spectra()
         x.write_total_ps()
         x.write_total_ac()
         x.write_atom_ps()
         x.write_atom_ac()


The **PhononDOS.py** script can be used to compute the phonon spectral
function for a given [NVE simulation](../misc/NVE_ensemble.md)
folder containing an [vaspout.h5](../output-files/Vaspout.h5.md) file
created with the aforementioned [INCAR](../input-files/INCAR.md) file. The
script will create a file called `total_ps.dat` containing the total
phonon spectral function. The partial phonon spectra of the atomic
species are written to files `ElementKey_ps.dat`. As input, the script
needs a folder name containing a
[vaspout.h5](../output-files/Vaspout.h5.md) file, and the second input
argument has to be the simulation time step of your simulation in fs.
The written files will contain the frequency in `THz` as the first
column. The second column will contain the phonon spectra computed as
the power spectrum of the velocity autocorrelation function.

### Anharmonic ratteling in CsPbBr\$\_{3}\$\[<a
href="/wiki/index.php?title=Sampling_phonon_spectra_from_molecular-dynamics_simulations&amp;veaction=edit&amp;section=9"
class="mw-editsection-visualeditor"
title="Edit section: Anharmonic ratteling in CsPbBr$_{3}$">edit</a> | (./index.php.md)\]

<figure typeof="mw:File/Thumb">
<a href="/wiki/File:CsPbBr3PhononDOS.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/8/85/CsPbBr3PhononDOS.png/140px-CsPbBr3PhononDOS.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/8/85/CsPbBr3PhononDOS.png/210px-CsPbBr3PhononDOS.png 1.5x, /wiki/images/thumb/8/85/CsPbBr3PhononDOS.png/280px-CsPbBr3PhononDOS.png 2x"
width="140" height="153" /></a>
<figcaption>Fig. 2: Snapshot of a $2 \times 2 \times 2$ CsPbBr$_{3}$
simulation box at 500K as used in the simulations for the convergence
analysis.</figcaption>
</figure>

In the following the convergence of the phonon DOS will be exemplified
on the CsPbBr\$\_{3}\$ in the cubic phase at 500K. A snapshot of the
used simulation box is shown in Fig. 2. The CsPbBr\$\_{3}\$ consists of
a cubic lead bromide framework which is covalently bonded. The cavities
formed by the cubic lead-bromide framework are filled with weakly bonded
Cs\$^{+}\$ cations. This makes the CsPbBr\$\_{3}\$ a good example to
test methods for anharmonic phonons.

The convergence of the phonon spectral function of CsPbrBr\$\_{3}\$ is
visualized in a single plot shown in Fig. 1. The yellow line shows an
average over a single trajectory. The more red the lines are, the more
trajectories have been used for computing the average. The dark red line
shows the average computed over all 10 trajectories. Based on the plot
in Fig. 1, it is possible to conclude that enough data was obtained to
properly converge the phonon spectral function.

Fig. 3 shows the atom-resolved normalized autocorrelations and phonon
spectra. A peak in the Cs\$^{+}\$ cation phonon spectral function is
visible around 1THz. This peak can be assigned to Cs\$^{+}\$ rattling
frequencies coupling to optical phonon modes formed by the oscillations
of the lead bromide framework.

For further information it is advised to take a look at
Ref<sup>[\[2\]](#cite_note-lahnsteiner:prb:2022-2)</sup>
or
Ref<sup>[\[3\]](#cite_note-lahnsteiner:jpcc:2024-3)</sup>
in which Cs\$^{+}\$ rattling modes were tuned to adjust the thermal
conductivity of the material.

<figure class="mw-halign-center" typeof="mw:File/Thumb">
<a href="/wiki/File:AtomReslovedPhononDOS.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/1/17/AtomReslovedPhononDOS.png/500px-AtomReslovedPhononDOS.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/1/17/AtomReslovedPhononDOS.png 1.5x" width="500"
height="375" /></a>
<figcaption>Fig. 3: <strong>Left:</strong> Shows atom-resolved
normalized velocity autocorrelation function for CsPbBr$_{3}$ at 500K.
<strong>Right:</strong> Atom-resolved phonon DOS for CsPbBr$_{3}$ at
500K.</figcaption>
</figure>

  

## References\[<a
href="/wiki/index.php?title=Sampling_phonon_spectra_from_molecular-dynamics_simulations&amp;veaction=edit&amp;section=10"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  [↑](#cite_ref-reissland:book:1973_1-0)
    <a
    href="https://www.abebooks.com/9780471715856/Physics-Phonons-J.A-Reissland-0471715859/plp"
    class="external text" rel="nofollow">J. A. <em>Reissland The Physics of
    Phonons</em></a>
2.  ↑
    <sup>[a](#cite_ref-lahnsteiner:prb:2022_2-0)</sup>
    <sup>[b](#cite_ref-lahnsteiner:prb:2022_2-1)</sup>
    <sup>[c](#cite_ref-lahnsteiner:prb:2022_2-2)</sup>
    <a href="https://doi.org/10.1103/PhysRevB.105.024302"
    class="external text" rel="nofollow">J. Lahnsteiner and M. Bokdam, Phys.
    Rev. B <strong>105</strong>, 024302 (2022).</a>
3.  [↑](#cite_ref-lahnsteiner:jpcc:2024_3-0)
    <a href="https://doi.org/10.1021/acs.jpcc.3c06590" class="external text"
    rel="nofollow">J. Lahnsteiner, M. Rang, and M. Bokdam, J. Phys. Chem. C
    <strong>128</strong>, 1341 (2024).</a>


  

## Related tags and articles\[<a
href="/wiki/index.php?title=Sampling_phonon_spectra_from_molecular-dynamics_simulations&amp;veaction=edit&amp;section=11"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/Molecular_dynamics_calculations" class="mw-redirect"
title="Molecular dynamics calculations">Molecular-dynamics
calculations</a>,

[Computing the phonon dispersion and
DOS](Computing_the_phonon_dispersion_and_DOS.md)

[Langevin thermostat](Langevin_thermostat.md)

<a href="/wiki/Ensembles" class="mw-redirect"
title="Ensembles">Ensembles</a>


