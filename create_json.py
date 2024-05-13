import json
import os

# Opening and loading texting file list into python variable test
'''
Testing opening a text file based list with each entry on a new line. No formatting in the list. 
'''
lines = []
text_file_path = os.sep.join(['data', 'inputs', 'test_list.txt'])
with open(text_file_path, mode='r') as text_file:
    for line in text_file:
        lines.append(line.strip())

print(lines)
# Previous Test Cases
'''
Here is the initial loading of json data and saving it to s file from python variables.
'''
name = "target"
id = 1234
squad = "unknown"
domain_values_input = "cabbage.com, sacrifice.com, potatoes.com, ilovesalad.com"
other_info = True

domain_values = [domain.strip() for domain in domain_values_input.split(",")]

this_json_raw = {
    "name": name,
    "id": id,
    "team":{
        "sqaud":squad,
        "domain_values": lines,
        "other_info": other_info
    }
}

json_file = json.dumps(this_json_raw, indent=4)

file_path = os.sep.join(['data', 'outputs', 'my_data_vars.json'])
with open(f"{file_path}", "w") as file:
    file.write(json_file)







# with open(file_path, 'w') as file:
#     file.write(this_json_raw)

# print("File Created?")