<!-- Source: https://vasp.at/wiki/index.php/Including_the_Spin-Orbit_Coupling | revid: 36611 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# Including the Spin-Orbit Coupling


Description: Spin-Orbit Coupling (SOC) included self-consistently

The Magnetocrystalline Anisotropy Energy is determined by rotating all
spins according to different directions. To modify the orientation of
the spins in the crystal, we consider the second approach described
[here](../incar-tags/SAXIS.md). For the
[MAGMOM](../incar-tags/MAGMOM.md)-tag, the total local magnetic moment is
written according to the z-direction (necessarily, the x and
y-directions are equal to 0). The spin orientation
$(u,v,w)$ is defined by the
[SAXIS](../incar-tags/SAXIS.md)-tag in the Cartesian frame. The
Magnetocrystalline Anisotropy Energy is calculated by orientating the
spins in different directions and the following equation

$E_{\text{MAE}} = E_{(u,v,w)} - E_0$

with $E_0$ the
energy of the most stable spin orientation.

More details are available in the [SAXIS](../incar-tags/SAXIS.md) and
[LSORBIT](../incar-tags/LSORBIT.md) pages.

*<u>Exercise :</u>* Determine the total magnetic moment by adding the
orbital moment of the Ni atoms. Calculate the Magnetocrystalline
Anisotropy Energy of NiO by orientating the spins along the following
path : (2,2,2) --\> (2,2,1) --\> (2,2,0) --\> ... --\> (2,2,-6).
Identify the most stable spin orientation according to this path.

------------------------------------------------------------------------

- [INCAR](../input-files/INCAR.md)

<!-- -->

    NiO GGA+U SOC
     SYSTEM    = "NiO"
        
    Electronic minimization
      ENCUT     = 450
      EDIFF     = 1E-7
      LORBIT    = 11
      LREAL     = .False.
      ISTART    = 0
      ISYM      = -1
      NELMIN    = 6
      LSORBIT   = .True.
      LWAVE     = .False.
      LCHARG    = .False.
        
    DOS
      ISMEAR    = -5
         
    Magnetism
      ISPIN     = 2
      MAGMOM    = 0 0 2 0 0 -2 6*0
      SAXIS     = 2 2 2
         
    Orbital Moment
      LORBMOM   = T 
         
    Mixer
      AMIX      = 0.2
      BMIX      = 0.00001
      AMIX_MAG  = 0.8
      BMIX_MAG  = 0.00001
        
    GGA+U
      LDAU      = .TRUE.
      LDAUTYPE  = 2
      LDAUL     = 2 -1
      LDAUU     = 5.00 0.00
      LDAUJ     = 0.00 0.00
      LDAUPRINT = 1
      LMAXMIX   = 4 

- [KPOINTS](../input-files/KPOINTS.md)

<!-- -->

    k-points
     0
    gamma
     4  4  4 
     0  0  0

- [POSCAR](../input-files/POSCAR.md)

<!-- -->

    NiO
     4.17
     1.0 0.5 0.5
     0.5 1.0 0.5
     0.5 0.5 1.0
     2 2
    Cartesian
     0.0 0.0 0.0
     1.0 1.0 1.0
     0.5 0.5 0.5
     1.5 1.5 1.5

## Download\[<a
href="/wiki/index.php?title=Including_the_Spin-Orbit_Coupling&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Download">edit</a> \| (./index.php.md)\]

<a href="/wiki/images/3/38/Nio_SOC.tgz" class="internal"
title="Nio SOC.tgz">nio_SOC.tgz</a>

------------------------------------------------------------------------


