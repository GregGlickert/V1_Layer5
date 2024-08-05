from bmtool.SLURM import SimulationBlock, SequentialBlockRunner,seedSweep, multiSeedSweep


# Define simulation cases
# simulation_cases (dict): Dictionary of simulation cases and their corresponding commands.
simulation_cases = {
    "baseline": "mpirun ./components/mechanisms/x86_64/special -mpi -python run_network.py simulation_config_baseline.json True",
    "short": "mpirun ./components/mechanisms/x86_64/special -mpi -python run_network.py simulation_config_short.json True",
    "long": "mpirun ./components/mechanisms/x86_64/special -mpi -python run_network.py simulation_config_long.json True"
}

# Define block parameters
# could add other params like account to allow working on Expanse
block_params = {
    'time': '02:00:00',
    'partition': 'shared',
    'nodes': 1,
    'ntasks': 24,
    'mem': '96G',
    'output_base_dir': '../Run-Storage/EXPANSE-TEST',
    'account':'umc113'
}

# Define the parameter to be changed and its values
param_name = 'initW'
param_values = [0.156,0.2,0.3] 

# Define JSON file path and create seedSweep instance
json_file_path = '/home/gglick9/V1/Network-Parameters/components/synaptic_models/synapses_STP/CP2CP.json'
json_editor = seedSweep(json_file_path, param_name)

# didnt test the multiSeedSweep yet but should work like this check out the bmtool SLURM.py module
# the seedSweep does work tho!
#syn_dict_list = []
#syn_dict_list.append({'json_file_path': '/home/gglick9/V1/Network-Parameters/components/synaptic_models/synapses_STP/CS2CP', 'ratio': 2.3})
#json_editor = multiSeedSweep(json_file_path,param_name,syn_dict_list,base_ratio=4.6) 

# Define the number of blocks to create
num_blocks = len(param_values)

# Create a list to hold the blocks
blocks = []

# commands you want to run in the script before bmtk starts useful for HPCs
additional_commands = [
    "module purge",
    "module load slurm",
    "module load cpu/0.17.3b",
    "module load gcc/10.2.0/npcyll4",
    "module load openmpi/4.1.1",
    "export HDF5_USE_FILE_LOCKING=FALSE"
]

# Create blocks with the defined simulation cases
for i in range(1, num_blocks + 1):
    block_name = f'block{i}'
    block = SimulationBlock(block_name, **block_params, simulation_cases=simulation_cases,additional_commands=additional_commands,
                            status_list = ['COMPLETED', 'RUNNING'])
    blocks.append(block)


# Create a SequentialBlockRunner with the blocks and parameter changes
runner = SequentialBlockRunner(blocks, json_editor, param_values,check_interval=200)
#runner = SequentialBlockRunner(blocks,check_interval=60)

# Submit the blocks sequentially
runner.submit_blocks_sequentially()