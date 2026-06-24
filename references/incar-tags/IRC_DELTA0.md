<!-- Source: https://vasp.at/wiki/index.php/IRC_DELTA0 | revid: 22773 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IRC_DELTA0
IRC_DELTA0 = real  
Default: **IRC_DELTA0** = 0.0015 

Description: Defines the tolerance factor $\Delta_0$ in Å used in the [IRC
calculations](../redirects/IRC_calculations.md).

------------------------------------------------------------------------

The smaller the value of IRC_DELTA0, the closer the computed IRC
trajectory follows the true IRC pathway. However, a small tolerance
factor $\Delta_0$ necessitates more time
steps and, thus, computational effort.

## Related tags and articles
[IRC calculations](../redirects/IRC_calculations.md),
[IRC_DIRECTION](IRC_DIRECTION.md) ,
[IRC_STOP](IRC_STOP.md),
[IRC_MINSTEP](IRC_MINSTEP.md),
[IRC_MAXSTEP](IRC_MAXSTEP.md),
[IRC_VNORM0](IRC_VNORM0.md)
