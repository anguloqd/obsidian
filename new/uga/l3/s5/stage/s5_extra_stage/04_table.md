# 04 // Table

| BFAST | BEAST |
| --- | --- |
| Y value | Y value |
| h : minimum separation interval of two CP | sseg.min and tseg.min |
| season : dummy, harmonic, none | season : dummy, harmonic, svd, none |
| breaks : max n° breaks | scp.minmax : n° season cp
tcp.minmax : n° trend cp |
|  | start : date of start |
|  | deltat : data time resolution |
|  | period : units of time (years) to complete one cycle. period = deltat * freq. |
| hpc : “high performance computing”. Default is none, can also be “foreach” (instalation required) |  |
| level : threshold value of breakpoints ?  |  |
| decomp : stl or stlplus |  |
| type : argument to efp |  |
|  | detrend |
|  | deseasonalize |
|  | mcmc.seed : id for reproducibility |
|  | mcmc.thin : “a factor to thin chains” |
|  | mcmc.burnin : n° of burn-in samples discarded |
|  | mcmc.samples : n° samples collected per MCMC chain |
|  | ci : compute credible intervals |
|  | precValue : “the hyperparameter of the precision prior” |
|  | precPriorType : constant, uniform, componentWise, orderWise |