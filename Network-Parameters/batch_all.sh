#!/bin/bash

#You may need to do chmod 705 "filename" if it says Permission denied.
#Usage: RUN_NUM=1 ./batch_all.sh 
#does a run of long/short/baseline titled (run_type)_1

RUN_NUM="${RUN_NUM:-1}"
echo $RUN_NUM

OUTPUT_DIR=../Run-Storage/Greg-runs/baseline-runs/baseline_2 sbatch batch_baseline.sh
OUTPUT_DIR=../Run-Storage/Greg-runs/short-runs/short_2 sbatch batch_short.sh
OUTPUT_DIR=../Run-Storage/Greg-runs/long-runs/long_2 sbatch batch_long.sh