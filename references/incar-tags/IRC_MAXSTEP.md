<!-- Source: https://vasp.at/wiki/index.php/IRC_MAXSTEP | revid: 22783 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IRC_MAXSTEP
IRC_MAXSTEP = real  
Default: **IRC_MAXSTEP** = 3.000 

Description: Upper limit for the step size (in fs).

------------------------------------------------------------------------

The damped-velocity-Verlet algorithm for the [IRC
calculations](../redirects/IRC_calculations.md) uses an
adaptively varying size of the time step. It depends on the estimated
accuracy of the previous step. IRC_MAXSTEP defines the upper limit for
the step size in fs.

## Related tags and articles
[IRC calculations](../redirects/IRC_calculations.md),
[IRC_DIRECTION](IRC_DIRECTION.md) ,
[IRC_STOP](IRC_STOP.md),
[IRC_DELTA0](IRC_DELTA0.md),
[IRC_MINSTEP](IRC_MINSTEP.md),
[IRC_VNORM0](IRC_VNORM0.md)
