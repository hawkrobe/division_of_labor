Core simulations
===========

## Getting started

* Install [webppl](https://github.com/probmods/webppl)

```
npm install -g webppl
```

* Install local dependencies

```
npm install
```

## Contents

* Resource-rational simulations in Section 2 are implemented in `RR_simulations.wppl` and can be re-produced by running

```
parallel --bar --colsep ',' "sh ./run_RR_grid.sh {1} {2} {3} {4}" :::: input/fine-grid.csv
```

* Model of listener adaptation dynamics in Appendix B is implemented in `dynamics_simulations.wppl` and can be re-produced by running

```
parallel --bar --colsep ',' "sh ./run_dynamics_grid.sh {1} {2}" :::: input/dynamics_grid.csv
```

* Bayesian data analysis and model comparison in Appendix C is implemented in `BDA.wppl`. To get parameter posteriors for a particular model, run

```
webppl BDA.wppl --require ./refModule/ -- --model occlusionSensitive
webppl BDA.wppl --require ./refModule/ -- --model egocentric
webppl BDA.wppl --require ./refModule/ -- --model mixture
```

To get marginal likelihoods via annealed importance sampling, run

```
parallel --bar --colsep ',' "sh ./run_AIS.sh {1} {2}" :::: input/BF_grid.csv
```

Note: for each of the parallelized command-line processes, the results must be collated into a single CSV before being read into the RNotebook for analyses. 