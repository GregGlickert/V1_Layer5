#!/bin/bash

#Usage: ./batch_gamma.sh 1
#does a run of short/baseline titled (run_type)_1

RUN_NUM=$1

echo $RUN_NUM

OUTPUT_DIR=../Run-Storage/Greg-runs/baseline-runs/baseline_1 sbatch batch_baseline.sh 
OUTPUT_DIR=../Run-Storage/Greg-runs/short-runs/short_1 sbatch batch_short.sh 


