import json
import sys

def change_json(json_file_path, key, new_parameter):
    new_parameter = float(new_parameter)
    # Open the JSON file in read mode
    with open(json_file_path, 'r') as json_file:
        file_contents = json.load(json_file)
    
    # Update the value of the specified key
    if key in file_contents:
        file_contents[key] = new_parameter
    else:
        print(f"Key '{key}' not found in the JSON file.")
        return
    
    # Write the updated JSON back to the file
    with open(json_file_path, 'w') as json_file:
        json.dump(file_contents, json_file, indent=4)
    
    print(f"JSON file '{json_file_path}' modified successfully.")

if __name__ == '__main__':
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("NOT EDITING JSONS")
        sys.exit(1)
    
    # Extract command-line arguments
    json_file = sys.argv[1]
    key = sys.argv[2]
    new_parameter = sys.argv[3]

    # Call change_json only if all arguments are provided
    change_json(json_file, key, new_parameter)
