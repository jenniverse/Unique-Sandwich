from os import listdir, path
from pprint import pprint

SOURCE = "/Users/jennykim/Desktop/Unique-Sandwich/"

all_file = listdir(SOURCE)

print(all_file)

combination_stack = []

for file in all_file:
    if file.startswith("."):
        continue
    if path.isdir(file):
        print(f"{file} is directory!")
        combination_stack.append(path.join(SOURCE, file))

print(combination_stack)

combination_map = {}

for combination_type in combination_stack:
    all_items_in_one_type = listdir(combination_type)
    if combination_type.split("/")[-1].startswith("_"):
        continue
    all_items_in_one_type = list(filter(lambda x: x.startswith(".") == False, all_items_in_one_type))
    if not all_items_in_one_type:
        continue
    combination_map[combination_type.split("/")[-1]] = all_items_in_one_type

pprint(combination_map)
 
for i, (k, v) in enumerate(sorted(combination_map.items())):
    print(f"{i}: key is {k} and value is {v}")