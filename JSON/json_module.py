import json
import os

# the dump and load work with json files

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, 'states.json')

with open(file_path, 'r') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'], state['abbreviation'])
    state.pop('area_codes')

file_path = os.path.join(BASE_DIR, 'new_states.json')
with open(file_path, 'w') as f:
    json.dump(data, f, indent=2, sort_keys=True) # this dump takes a file pointer as an arguement