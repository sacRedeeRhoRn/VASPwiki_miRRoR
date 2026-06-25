<!-- Source: https://vasp.at/wiki/index.php/NATURALO | revid: 27413 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# NATURALO


NATURALO = \[integer\]  
Default: **NATURALO** = 0; for low scaling GW type calculations the
default is 4 

Description: calculate RPA natural orbitals.

------------------------------------------------------------------------

This flag should be used in combination with [ALGO](ALGO.md) =
G0W0R or [ALGO](ALGO.md) = scGW0R. The VASP code diagonalizes
the RPA density matrix and writes the final natural orbitals to the
[WAVECAR](../input-files/WAVECAR.md) file. The one-electron occupancies on
the [WAVECAR](../input-files/WAVECAR.md) file can also be updated to the
eigenvalues of the RPA density matrix. For [ALGO](ALGO.md) =
G0W0R, the interacting Green's function is approximated as

$G
= G_0 + G_0 \Sigma G_0$

whereas for [ALGO](ALGO.md) = scGW0R the Dyson equation is
solved

$G
= G_0 + G \Sigma G_0.$

In both cases, the RPA density matrix is determined as
$\gamma= \lim_{\tau \to 0^-} G(\tau)$. More details on
the use of RPA natural orbitals can be found in Ref.
<sup>[\[1\]](#cite_note-ramberger2019rpa-1)</sup>.

The following settings are currently supported

- NATURALO=0 calculate the
  density matrix, diagonalize the matrix and write the natural orbitals
  and eigenvalues of the density matrix to
  [WAVECAR](../input-files/WAVECAR.md). The eigenvalues of the density
  matrix are stored in the occupancy entries of the
  [WAVECAR](../input-files/WAVECAR.md) file, whereas the one-electron DFT
  eigenvalues remain untouched. This setting is usually not particularly
  useful for practical calculations and should be used only by experts.
  Furthermore,
  [LFINITE_TEMPERATURE](LFINITE_TEMPERATURE.md)
  should not be combined with this setting.

<!-- -->

- NATURALO=1 calculate the
  density matrix, diagonalize the matrix only in the sub-block of
  unoccupied states, and write the occupied Kohn Sham orbitals, as well
  as the natural orbitals corresponding to unoccupied states to the file
  [WAVECAR](../input-files/WAVECAR.md). The unoccupied orbitals are
  ordered according to their occupancies in the RPA density matrix. The
  one-electron occupancies and KS-DFT eigenvalues are not updated from
  their KS values (the occupancies will remain 1 for occupied Kohn-Sham
  orbitals and 0 for natural orbitals representing the virtual
  manifold). This setting has been used in Ref.
  <sup>[\[1\]](#cite_note-ramberger2019rpa-1)</sup>.
  See also Ref.
  <sup>[\[2\]](#cite_note-GruneisNO-2)</sup>
  for further information. Note that all orbitals- even those with a
  tiny fractional occupancy -are treated as occupied orbitals and not
  updated: the algorithm should hence even work for metallic systems.

<!-- -->

- NATURALO\<0. Similar to
  NATURALO=1 but additionally
  conserves ABS\|NATURALO\|
  unoccupied Kohn-Sham states. This is expedient, for subsequent GW and
  BSE calculations to conserve few unoccupied orbitals to their
  Kohn-Sham states.

<!-- -->

- If 10 is added (e.g.
  NATURALO=10,
  NATURALO=11) the density
  matrix is diagonalizes using a perturbative Loewdin algorithm that
  attempts to keep the orbital order strictly conserved: E.g. the
  natural orbital matching closest to each Kohn-Sham orbital will be
  determined and stored. Use this tag for metals.

<!-- -->

- NATURALO=2 (or 12) is
  similar to 0, but the one-electron occupancies are not updated. In
  rare cases this might lead to inconsistencies, if the orbital order
  changes between DFT and the RPA density matrix (i.e. a previously
  occupied DFT orbitals posses a smaller occupation in the RPA density
  matrix than some unoccupied Kohn-Sham orbitals and are moved into the
  unoccupied block). This problem can be reduced using
  NATURALO=12, as described
  above. This flag, in combination with [ALGO](ALGO.md) =
  scGW0R, can be used to evaluate the GW-singles contribution to the
  correlation
  energy.<sup>[\[3\]](#cite_note-Klimessingles-3)</sup>
  One can deduct the HF singles and the GW singles energies from the
  energies after

<!-- -->

        Energies after diagonalization of HF Hamiltonian (single shot)
        Hartree-Fock free energy of the ion-electron system (eV)

        Energies after update of density matrix
        Hartree-Fock free energy of the ion-electron system (eV)

Experience has shown that there is very little difference between the
natural orbitals obtained using [ALGO](ALGO.md) = G0W0R and
[ALGO](ALGO.md) = scGW0R. We strongly recommend to use the
more efficient and better tested algorithm [ALGO](ALGO.md) =
G0W0R (with the exception of GW-singles) to determine natural orbitals.
Furthermore, perform careful tests for [NOMEGA](NOMEGA.md):
the RPA total energy converges much faster then the natural orbitals.
Using a too small [NOMEGA](NOMEGA.md) can yield natural
orbitals that are non-optimal, leading to very slow convergence of
correlated calculations with respect to the number of natural orbitals.
A crucial test is that the following line

    correlated contrib. to density matrix         0.0000004037        0.0000000000

in the stdout and OUTCAR file shows values close to zero (for
[ALGO](ALGO.md) = G0W0R). The above value is perfectly
acceptable and the value decreases as [NOMEGA](NOMEGA.md)
increases.

- NATURALO=4 preserves
  original (DFT) orbitals but updates the eigenvalues in the
  [WAVECAR](../input-files/WAVECAR.md) file to the QP energies. This mode
  is useful if only quasi-particle energies are corrected with the GW
  method, for instance when selecting
  [ALGO](ALGO.md)=<a href="/wiki/GW_calculations#gw0" class="mw-redirect"
  title="GW calculations">EVGW0R</a>.

|  |
|----|
| **Mind:** available as of VASP.6.4: |

## Related tags and articles\[<a href="/wiki/index.php?title=NATURALO&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

- [ALGO](ALGO.md) for response functions and *RPA*
  calculations
- for an overview on total energies using the [ACFDT/RPA
  formalism](../methods/ACFDT__RPA_calculations.md)
- for a practical guide to
  <a href="/wiki/GW_calculations" class="mw-redirect"
  title="GW calculations">GW calculations</a>

## References\[<a href="/wiki/index.php?title=NATURALO&amp;veaction=edit&amp;section=2"
class="mw-editsection-visualeditor"
title="Edit section: References">edit</a> \| (./index.php.md)\]


1.  ↑
    <sup>[a](#cite_ref-ramberger2019rpa_1-0)</sup>
    <sup>[b](#cite_ref-ramberger2019rpa_1-1)</sup>
    <a href="https://doi.org/10.1063/1.5128415" class="external text"
    rel="nofollow">B. Ramberger, Z. Sukurma, T. Schäfer, G. Kresse, J. Chem.
    Phys. 151, 214106 (2019).</a>
2.  [↑](#cite_ref-GruneisNO_2-0)
    
    <a href="https://doi.org/10.1021/ct200263g" class="external text"
    rel="nofollow">A. Grüneis et al. J. Chem. Theory Comput. 7, 2780
    (2011).</a> 
3.  [↑](#cite_ref-Klimessingles_3-0)
    <a href="https://doi.org/10.1063/1.4929346" class="external text"
    rel="nofollow">Jiří Klimeš et al., J. Chem. Phys. 143, 102816
    (2015).</a>


------------------------------------------------------------------------


