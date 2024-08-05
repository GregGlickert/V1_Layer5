#!/bin/bash

# Usage: ./batch_seedSweep.sh RUN_NUM JSON_FILE KEY START_VALUE END_VALUE STEP
# Example: ./batch_seedSweep.sh 1 test.json initW 2.0 5.0 0.5

RUN_NUM=$1
JSON_FILE=$2     # path to json file
KEY=$3           # parameter in json file you want to edit
START_VALUE=$4   # starting value for parameter
END_VALUE=$5     # ending value for parameter
STEP=$6          # step for parameter

echo "Starting seedSweep with parameters:"
echo "RUN_NUM: $RUN_NUM"
echo "JSON_FILE: $JSON_FILE"
echo "KEY: $KEY"
echo "START_VALUE: $START_VALUE"
echo "END_VALUE: $END_VALUE"
echo "STEP: $STEP"

# Initialize current value to start value
current_value=$START_VALUE

# Initialize variable to track job ID of the previous job
PREV_JOB_ID=""

# Loop while current value is less than or equal to end value
while (( $(echo "$current_value <= $END_VALUE" | bc -l) ))
do
    sleep 5  # Add delay to ensure JSON file is saved
    echo "Submitting job for NEW_PARAMETER=$current_value to $OUTPUT_DIR"

    # Submit job with dependency on previous job (if exists) will use last job submited in the 
    # if statement to tell when to start next block of jobs
    if [ -n "$PREV_JOB_ID" ]; then
        # Submit job with dependency on previous job
        OUTPUT_DIR="../Run-Storage/Greg-runs/baseline-runs/baseline_${RUN_NUM}_${current_value}"
        JOB_ID=$(sbatch --dependency=afterok:$PREV_JOB_ID batch_baseline.sh $JSON_FILE $KEY $current_value | awk '{print $4}')
        OUTPUT_DIR="../Run-Storage/Greg-runs/baseline-runs/short_${RUN_NUM}_${current_value}"
        JOB_ID=$(sbatch --dependency=afterok:$PREV_JOB_ID batch_short.sh $JSON_FILE $KEY $current_value | awk '{print $4}')
        #add more jobs here, will wait to final job is done to start next blocks
    else
        # Submit job without dependency (first block in sequence)
        OUTPUT_DIR="../Run-Storage/Greg-runs/baseline-runs/baseline_${RUN_NUM}_${current_value}"
        JOB_ID=$(sbatch batch_baseline.sh $JSON_FILE $KEY $current_value | awk '{print $4}')
        OUTPUT_DIR="../Run-Storage/Greg-runs/baseline-runs/short_${RUN_NUM}_${current_value}"
        JOB_ID=$(sbatch batch_short.sh $JSON_FILE $KEY $current_value | awk '{print $4}')
    fi

    # Update PREV_JOB_ID to current job ID for next iteration
    PREV_JOB_ID=$JOB_ID

    # Increment current value by the step size
    current_value=$(echo "$current_value + $STEP" | bc)
done
