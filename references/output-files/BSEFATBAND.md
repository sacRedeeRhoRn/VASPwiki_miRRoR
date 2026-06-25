<!-- Source: https://vasp.at/wiki/index.php/BSEFATBAND | revid: 20498 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# BSEFATBAND


The BSEFATBAND file contains
the [NBSEEIG](../incar-tags/NBSEEIG.md) number of eigenvectors of the BSE
Hamiltonian.

The file has the following structure:

      rank of the BSE matrix                NBSEEIG
      1BSE eigenvalue    E_BSE      IP-eigenvalue:    E_IP
    Kx Ky Kz E_v E_c Abs(X_BSE)/W_k NB_v NB_c Re(X_BSE)+ i*Im(X_BSE)   
    ...
      2BSE eigenvalue    E_BSE      IP-eigenvalue:    E_IP
    Kx Ky Kz E_v E_c Abs(X_BSE)/W_k NB_v NB_c Re(X_BSE)+ i*Im(X_BSE)
    ...
       NBSEEIGBSE eigenvalue    E_BSE      IP-eigenvalue:    E_IP
    Kx Ky Kz E_v E_c Abs(X_BSE)/W_k NB_v NB_c Re(X_BSE)+ i*Im(X_BSE)   

where *E_BSE* and *E_IP* are the BSE and IP transition energies, *KX KY
KZ* the k-point coordinates, *E_v* and *E_c* the eigenvalues of the
valence and conduction band, respectively, *X_BSE* the component of the
eigenvector, *W_k* the weight of the k point, and *NB_v NB_c* the
valence and conduction orbital numbers.

## Related tags and articles\[<a
href="/wiki/index.php?title=BSEFATBAND&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

[NBSEEIG](../incar-tags/NBSEEIG.md),
<a href="/wiki/BSE_calculations" class="mw-redirect"
title="BSE calculations">BSE calculations</a>

------------------------------------------------------------------------


