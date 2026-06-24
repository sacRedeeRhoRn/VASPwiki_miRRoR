<!-- Source: https://vasp.at/wiki/index.php/IRC_STOP | revid: 22772 | retrieved: 2026-06-24 -->
<!-- © VASP wiki contributors. Licensed under GNU Free Documentation License 1.2 (GFDL 1.2). -->

# IRC_STOP
IRC_STOP = integer  
Default: **IRC_STOP** = 20 

Description: Sets the number of steps in which the energy must
monotonously increase before an [IRC
calculation](../redirects/IRC_calculations.md) terminates.

------------------------------------------------------------------------

Along the IRC pathway, from a higher energy state, i.e., the transition
state or the excited state, towards a lower energy state, i.e.,
reactants or products, the energy generally decreases. In some cases,
the IRC pathway may encounter regions with relatively constant energy
(plateaus) or fluctuations due to numerical noise or complex
interactions, particularly in the vicinity of transition states.

IRC_STOP sets the number of time steps with increasing energy, after
which the damped-velocity-Verlet algorithm in an [IRC
calculation](../redirects/IRC_calculations.md) terminates. In
order to avoid a premature termination, especially close to transition
states, IRC_STOP should always be greater than 1.

## Related tags and articles
[IRC calculations](../redirects/IRC_calculations.md),
[IRC_DIRECTION](IRC_DIRECTION.md) ,
[IRC_DELTA0](IRC_DELTA0.md),
[IRC_MINSTEP](IRC_MINSTEP.md),
[IRC_MAXSTEP](IRC_MAXSTEP.md),
[IRC_VNORM0](IRC_VNORM0.md)
