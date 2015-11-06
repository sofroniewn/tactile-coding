# Tactile coding

[![Binder](http://mybinder.org/badge.svg)](http://mybinder.org/repo/sofroniewn/tactile-coding)

Interactive notebooks to accompany Sofroniew\*, NJ, Vlasov\*, YA, Hires, SA, Freeman, J, Svoboda, K -
Neural coding in barrel cortex during whisker-guided locomotion. (Submitted 2015)


The data anlaysis is split into 5 notebooks, three for the calcium imaging analsis, and two for the electrophysiology analysis. There is one additional helper module located inside the helper folder. All the data lives in an S3 bucket on Amazon.

The notebooks are as follows:

imagingRaw - which loads in the raw pixels from the calcium imaging for each experiment , the manually drawn sources (ROIs/neurons) and the behavioural covariates. The notebook takes you through loading the data, a pixelwise regression analysis, and computing the normalized activity (DF/F) traces for each neuron. Running this notebook in interactive mode is currently not supported

imagingTraces - loads in the activity traces of each neuron and the behavioural covariates and computes tuning curves and summary statistics for each neurons. The results get saved in a table. 

imagingTable - loads in the summary table and plots results.

ephysTraces - loads in the spike times of each neuron, after spike sorting, and the behavioural covariates and computes tuning curves and summary statistics for each neurons. The results get saved in a table.

ephysTable - loads in the summary table and plots results