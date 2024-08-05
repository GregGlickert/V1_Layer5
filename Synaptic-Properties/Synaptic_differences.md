# Overview
Synaptic properties defined by the Allen Institute fall into 2 main categories:
* Single trial PSP properties (designated as ST)
* Multiple trial PSP properties (designatd as MT)
* The tables are divided based on the presynaptic cell and show the percentage difference from Exp2Syn->New Syn.
* A 0 means they are the same up to at least 3 decimal places.

#### Abbreviations/Legend:
* ST = Single Trial PSP
* MT = Multi Trial PSP
* Induc = Induction
*  \* = The new synapse's value is at 0, or sufficiently close to it.

## AMPA_NMDA Synapses

### CP Synapses
|Synapse| Latency | Rise Time | Decay Time | Half-Width | ST Induc | ST Recovery | ST Rest Amp | ST Max Amp | MT Induc | MT Recovery | MT Rest Amp | MT Max Amp |
|:------|:--------|:----------|:-----------|:-----------|:---------|:------------|:------------|:-----------|:---------|:------------|:------------|:-----------|
|CP2CP| 0| +1.95%| +6.58%| +3.21%| +10.44%| +100.65%*| +5.55%| +5.97%| +7.81%| +101.449%*|+5.55% | +5.64% |
|CP2CS| 0| +2.06%| +8.30%| +3.32%| +11.22%| +22.8%| 0| +10%| +1.99%| +11.80%| 0| 0|
|CP2FSI|0| +2.74%| +23.28%| +4.68%| +6.32%| +100%*| +4.43%| +4.43%| +6.21| +100%*| +4.43%| +4.43%|
|CP2LTS|0| +1.76%| +5.08%| +2.65%| +0.38%| -100%*| +4.63%| +9.42%| +0.56%| -100%*| +4.63%| +7.41%|



### CS Synapses
|Synapse| Latency | Rise Time | Decay Time | Half-Width | ST Induc | ST Recovery | ST Rest Amp | ST Max Amp | MT Induc | MT Recovery | MT Rest Amp | MT Max Amp |
|:------|:--------|:----------|:-----------|:-----------|:---------|:------------|:------------|:-----------|:---------|:------------|:------------|:-----------|
|CS2CP| 0| +2.32%| +12.73%| +5.62%| +202.5%| +101.54%*| +5.13%| +11.43%| +44.74%| +100%*| +5.13%| +7.69%|
|CS2CS| 0| +2.62%| 13.49%| +5.46%| +23.67%| +14.14%| 0| +11.11%| +4.12%| +7.03%| 0| 0|
|CS2FSI|0| +3.57%| +34.75%| +6.06%| -16.25%| +100%*| +4.10%| -18.3%| -8.2%| -100%*| +4.10%| -4.83%|
|CS2LTS|0| +3.61%| +16.04%| +6.88%| +1.72%| -100%*| +5.80%| +21.53%| +9.25%| -100%| +5.80%| -0.06%|

### Notes
* The biggest changes are consistently found in the recovery, both in ST and MT. 
* AMPA_NMDA synapses tend to have a recovery of 0. 

## GABA_AB Synapses
These are for the PVs.

### FSI Synapses
|Synapse| Latency | Rise Time | Decay Time | Half-Width | ST Induc | ST Recovery | ST Rest Amp | ST Max Amp | MT Induc | MT Recovery | MT Rest Amp | MT Max Amp |
|:------|:--------|:----------|:-----------|:-----------|:---------|:------------|:------------|:-----------|:---------|:------------|:------------|:-----------|
|FSI2CP| 0| 0| 0| 0| 0| +100%*| 0| 0| 0| +106.67%*| 0| 0|
|FSI2CS| 0| 0| 0| 0| +17.69%| +500%| 0| +21.06%| +5.56%| +24.92%| 0| 0|
|FSI2FSI| 0| 0| 0| 0| 0| +100%*| 0| 0| 0| +100%*| 0| 0|
|FSI2LTS| 0| 0| 0| 0| 0| +100%*| 0| 0| 0| +100%*| 0| 0|
### LTS Synapses
|Synapse| Latency | Rise Time | Decay Time | Half-Width | ST Induc | ST Recovery | ST Rest Amp | ST Max Amp | MT Induc | MT Recovery | MT Rest Amp | MT Max Amp |
|:------|:--------|:----------|:-----------|:-----------|:---------|:------------|:------------|:-----------|:---------|:------------|:------------|:-----------|
|LTS2CP| 0| 0| 0| 0| +2.70%| -100%*| 0| -3.05%| +5.80%| -100%*| 0| 0|
|LTS2CS| 0| 0| 0| 0| -4.67%| -46.55%| 0| +4.92%| +2.60%| -26.26%| 0| 0|
|LTS2FSI| 0| 0| 0| 0| -67.25%| -100%*| 0| -40%| +6.48%| -100%*| 0| -9.38%|
|LTS2LTS| 0| 0| 0| 0| 0| +100%*| 0| +0.14%| 0| +100%*| 0| 0|

### Notes
* GABA_AB synapses are more similar to exponential synapses.
* Synapses starting from FSI cells are extremely similar. 
* Once again, the biggest changes are consistently found in the recovery, both in ST and MT.
* GABA_AB synapses also tend to have a recovery of 0, with some exceptions.

