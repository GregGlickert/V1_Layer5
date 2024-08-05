import sys
import os
import pathlib
import json
import warnings
import synapses
from bmtk.simulator import bionet
from bmtk.simulator.bionet.pyfunction_cache import add_weight_function
from neuron import h

pc = h.ParallelContext()
CONFIG = 'config.json'
USE_CORENEURON = False

def get_synaptic_params(path_to_syn_folder):
    """Gets values of all json files and puts them into one file"""
    combined_data = []
    # List all files in the input folder
    for filename in os.listdir(path_to_syn_folder):
        if filename.endswith('.json'):
            file_path = os.path.join(path_to_syn_folder, filename)
            
            # Open and read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)
                # Append the filename and its data
                combined_data.append({
                    'filename': filename,
                    'data': data
                })
    return combined_data

def save_synaptic_params(data,path_to_output_dir):
    """Saves combined json data into one file"""
    with open(path_to_output_dir, 'w') as output_file:
        json.dump(data, output_file, indent=4)

def run(config_file=CONFIG, use_coreneuron=USE_CORENEURON, json_file=None, key=None, new_parameter=None):
    warnings.simplefilter(action='ignore', category=FutureWarning)

    # register synaptic weight function
    synapses.load(randseed=1111)
    add_weight_function(synapses.lognormal_weight, name='lognormal_weight')

    with open(config_file, 'r') as json_file:
        conf_dict = json.load(json_file)
        if os.environ.get("OUTPUT_DIR"):
            output_dir = os.path.abspath(os.environ.get('OUTPUT_DIR'))
            pathlib.Path(output_dir).mkdir(parents=True, exist_ok=True)
            print(f"Output directory updated to {output_dir}")
            conf_dict['manifest']['$OUTPUT_DIR'] = output_dir
            
            synaptic_report_dir = output_dir + "/synaptic_report.json"
            syn_data = get_synaptic_params('components/synaptic_models/synapses_STP')

        if use_coreneuron:
            import corebmtk
            conf = corebmtk.Config.from_json(conf_dict, validate=True)
        else:
            conf = bionet.Config.from_json(conf_dict, validate=True)

    pc.barrier()
    conf.build_env()
    graph = bionet.BioNetwork.from_config(conf)

    if use_coreneuron:
        sim = corebmtk.CoreBioSimulator.from_config(conf, network=graph, gpu=False)
    else:
        sim = bionet.BioSimulator.from_config(conf, network=graph)

    pc.barrier()
    sim.run()
    # must be run exactly right here
    if pc.id() == 0:
        save_synaptic_params(syn_data,synaptic_report_dir)
    bionet.nrn.quit_execution()


if __name__ == '__main__':
    for i, s in enumerate(sys.argv):
        if s in __file__:
            break

    if i < len(sys.argv) - 1:
        argv = sys.argv[i + 1:]
        for i in range(1, len(argv)):
            argv[i] = eval(argv[i])
        print(*argv)
        run(*argv)
    else:
        run()
