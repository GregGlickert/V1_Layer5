#!/bin/bash

#SBATCH -J V1_H_short
#SBATCH -o  out_short.txt
#SBATCH -e  error_short.txt
#SBATCH -t 0-48:00:00  # days-hours:minutes


#SBATCH -N 1
#SBATCH -n 45 # used for MPI codes, otherwise leave at '1'
#SBATCH --mem-per-cpu=2G  # memory per core; default is 1GB/core

START=$(date)
echo "Started running at $START."

JSON_FILE=$1
KEY=$2
NEW_PARAMETER=$3

python edit_json.py $JSON_FILE $KEY $NEW_PARAMETER
sleep 5
mpirun nrniv -mpi -python run_network.py simulation_config_short.json

END=$(date)
echo "Done running simulation at $END"