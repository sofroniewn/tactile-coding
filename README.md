
[![DOI](https://zenodo.org/badge/41120150.svg)](https://zenodo.org/badge/latestdoi/41120150) [![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/sofroniewn/tactile-coding)


# Tactile coding

Interactive Jupyter notebooks to accompany 

***NJ Sofroniew\*, YA Vlasov\*, SA Hires, J Freeman, & K Svoboda (2015) Neural coding in barrel cortex during whisker-guided locomotion, eLife, 10.7554/eLife.12559***

Read the published [article](http://elifesciences.org/content/4/e12559v1) on eLife

Download the supporting [data](https://doi.org/10.5281/zenodo.2949959) from Zenodo

Launch interactive notebooks by clicking the binder badge

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/sofroniewn/tactile-coding)

The data anlaysis is split into 5 notebooks, three for the calcium imaging analsis, and two for the electrophysiology analysis, representing progressively refined stages of preprocessing and analysis. There is one additional helper module located inside the helper folder. All the raw data is stored and made publicly available on Amazon S3 in the bucket `neuro.datasets` under the directory `svoboda.lab/tactile.coding`. See the notebooks for examples of accessing the data.


### Contents
--------

#### imaging-raw

Loads in the raw pixels from the calcium imaging for each experiment , the manually drawn sources (ROIs/neurons) and the behavioural covariates. The notebook takes you through loading the data, a pixelwise regression analysis, and computing the normalized activity (DF/F) traces for each neuron. Running this notebook in interactive mode is currently not supported

#### imaging-traces
Loads in the activity traces of each neuron and the behavioural covariates and computes tuning curves and summary statistics for each neurons. The results get saved in a table. 

#### imaging-table
Loads in the summary table for imaging data and plots results.

#### ephys-traces
Loads in the spike times of each neuron, after spike sorting, and the behavioural covariates and computes tuning curves and summary statistics for each neurons. The results get saved in a table.

#### ephys-table
Loads in the summary table for ephys data and plots results.
