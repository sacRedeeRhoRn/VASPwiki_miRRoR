<!-- Source: https://vasp.at/wiki/index.php/LSINGLES | revid: 24262 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# LSINGLES


LSINGLES = .TRUE. \| .FALSE.  
Default: **LSINGLES** = .FALSE. 

Description: Switch on singles contribution to correlation energy for
[GW
algorithms](../methods/Practical_guide_to_GW_calculations.md).[^klimes:jcp:143-1]

------------------------------------------------------------------------

LSINGLES enables the
calculation of the singles contributions to the correlation energy that
can be represented by the following Feynman (time-ordered)
diagrams:[^kaltak:thesis2015-2][^klimes:jcp:143-1]

<a href="/wiki/File:SinglesDiagrams.png"
class="mw-file-description"><img
src="https://vasp.at/wiki/images/thumb/e/eb/SinglesDiagrams.png/320px-SinglesDiagrams.png"
class="mw-file-element" decoding="async"
srcset="/wiki/images/thumb/e/eb/SinglesDiagrams.png/480px-SinglesDiagrams.png 1.5x, /wiki/images/thumb/e/eb/SinglesDiagrams.png/640px-SinglesDiagrams.png 2x"
width="320" height="97" /></a>

LSINGLES is used in
combination with the [low-scaling
ACFDT/RPA](../methods/ACFDT__RPA_calculations.md)
and
[GW](../methods/Practical_guide_to_GW_calculations.md)
algorithms.

If the [ACFDT/RPA
algorithm](../methods/ACFDT__RPA_calculations.md)
is selected with [ALGO](ALGO.md)=RPAR\|ACFDTR and
LSINGLES
is set, the code calculates two singles contributions and writes
following lines to [OUTCAR](../output-files/OUTCAR.md)

    HF single shot energy change        -1.23182672
    renormalized HF singles             -1.23310555

Here, **renomalized HF singles** corresponds to the renormalized singles
contribution suggested by Ren and
coworkers:[^ren:prb:88-3]

$E^{rSE}_c = -\sum_{a\in virt, i\in occ} \frac{|\langle i| V^{HF} -
V_0^{KS}|a\rangle|^2 }{\epsilon_a-\epsilon_i}$

This contribution accounts for the change of the mean-field exchange
energy and can be derived consistently within the AC-FDT framework as
described in Sec. II D Eq. (28) of Klimeš et
al.[^klimes:jcp:143-1]

In contrast, the **HF single shot energy change** line contains the
somewhat simpler
contribution[^klimes:jcp:143-1]

$E_c^{rSE} = \mathrm{Tr}\left\[ (\gamma_{HF} - \gamma_{DFT})\hat
h_{HF} \right\],$

where $\gamma_{HF}$
is the Hartree-Fock density matrix, determined for the Hartree-Fock
Hamiltonian $\hat h_{HF}$
and $\gamma_{DFT}$ is the Kohn-Sham density matrix. In all practical
calculations, we found that both values, the single-shot HF and
renormalized singles contributions, are exceedingly close to each other.

If the [GW
algorithm](../methods/Practical_guide_to_GW_calculations.md)
is selected with [ALGO](ALGO.md)=G0W0R, the
[OUTCAR](../output-files/OUTCAR.md) contains also the singles contribution
beyond the Hartree-Fock level

$E_c^{GWSE} = \mathrm{Tr}\left\[ (\gamma_{RPA} - \gamma_{DFT})\hat
h_{HF} \right\],$

where $\gamma_{RPA}$ is the RPA density
matrix.[^klimes:jcp:143-1]
For versions \<= 6.4.2, this contribution is not directly printed to
file. However, the first and second term is printed to
[OUTCAR](../output-files/OUTCAR.md):

    Energies using frozen KS orbitals
    Hartree-Fock free energy of the ion-electron system (eV)
     ...
     eigenvalues         EBANDS =       -88.61789695   <--------Tr{ gam_DFT h_HF}---------
     ... 
    Energies after update of density matrix 
    Hartree-Fock free energy of the ion-electron system (eV) 
     ...
     eigenvalues         EBANDS =       -89.68870320   <--------Tr{ gam_RPA h_HF}---------
     ...

Version \>6.4.2 writes the GWSE singles contribution to
[OUTCAR](../output-files/OUTCAR.md):

     GWSE singles contribution:        -1.07080625

|  |
|----|
| **Mind:** The singles contribution is calculated correctly only for the default [NATURALO](NATURALO.md)=2. |

The [ACFDT total
energy](../methods/ACFDT__RPA_calculations.md)
in the limit of [infinite energy
cutoff](../methods/ACFDT__RPA_calculations.md)
is then obtained by adding the singles contribution to the value of

`HF+E_corr(extrapolated)    =      -153.98810072 eV`

## Related tags and articles\[<a href="/wiki/index.php?title=LSINGLES&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [NATURALO](NATURALO.md) natural orbital selection for
  *RPA* and *GW* calculations
- [ALGO](ALGO.md) for response functions and *RPA*
  calculations
- for an overview on total energies using the [ACFDT/RPA
  formalism](../methods/ACFDT__RPA_calculations.md)
- for a practical guide to
  <a href="/wiki/GW_calculations" class="mw-redirect"
  title="GW calculations">GW calculations</a>
- [Basis set
  convergence](../methods/ACFDT__RPA_calculations.md)
  of ACFDT/RPA calculations

## References\[<a href="/wiki/index.php?title=LSINGLES&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]

------------------------------------------------------------------------

[^klimes:jcp:143-1]: [J. Klimeš, M. Kaltak, and G. Kresse, J. Chem. Phys. **143**, 102816 (2015).](https://doi.org/10.1063/1.4929346)
[^kaltak:thesis2015-2]: [M. Kaltak, Thesis: Merging GW with DMFT (2015).](https://utheses.univie.ac.at/detail/33771#)
[^ren:prb:88-3]: [X. Ren, P. Rinke, G. E. Scuseria, and M. Scheffler, Phys. Rev. B **88**, 035120 (2013).](http://doi.org/10.1103/PhysRevB.88.035120)
