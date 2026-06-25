<!-- Source: https://vasp.at/wiki/index.php/IRC_MINSTEP | revid: 22781 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IRC_MINSTEP


IRC_MINSTEP = real  
Default: **IRC_MINSTEP** = 0.0250 

Description: Lower limit for the step size (in fs).

------------------------------------------------------------------------

The damped-velocity-Verlet algorithm for the
<a href="/wiki/IRC_calculations" class="mw-redirect"
title="IRC calculations">IRC calculations</a> uses an adaptively varying
size of the time step. It depends on the estimated accuracy of the
previous step. IRC_MINSTEP
defines the lower limit for the step size in fs.

## Related tags and articles\[<a
href="/wiki/index.php?title=IRC_MINSTEP&amp;veaction=edit&amp;section=1"
class="mw-editsection-visualeditor"
title="Edit section: Related tags and articles">edit</a> \| (./index.php.md)\]

<a href="/wiki/IRC_calculations" class="mw-redirect"
title="IRC calculations">IRC calculations</a>,
[IRC_DIRECTION](IRC_DIRECTION.md) ,
[IRC_STOP](IRC_STOP.md),
[IRC_DELTA0](IRC_DELTA0.md),
[IRC_MAXSTEP](IRC_MAXSTEP.md),
[IRC_VNORM0](IRC_VNORM0.md)


