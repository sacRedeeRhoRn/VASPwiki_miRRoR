<!-- Source: https://vasp.at/wiki/index.php/IRC_VNORM0 | revid: 22785 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IRC_VNORM0
IRC_VNORM0 = real  
Default: **IRC_VNORM0** = 0.002 

Description: The constant velocity vector (in Å/fs) in an [IRC
calculation](../redirects/IRC_calculations.md).

------------------------------------------------------------------------

In the damped-velocity-Verlet algorithm for [IRC
calculations](../redirects/IRC_calculations.md), the damping is
realized via rescaling the velocity vector to a constant value (in Å/fs)
defined via the parameter IRC_VNORM0.

## Related tags and articles
[IRC calculations](../redirects/IRC_calculations.md),
[IRC_DIRECTION](IRC_DIRECTION.md) ,
[IRC_STOP](IRC_STOP.md),
[IRC_DELTA0](IRC_DELTA0.md),
[IRC_MINSTEP](IRC_MINSTEP.md),
[IRC_MAXSTEP](IRC_MAXSTEP.md)
