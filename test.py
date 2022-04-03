from genericpath import exists
from sre_constants import SUCCESS
from os import listdir, path
from PIL import Image, ImageFilter
import random
import os
import os.path
import glob

SOURCE = "/Users/jennykim/Desktop/Unique-Sandwich/"

# get random acc from folder
backgroundPath = "/Users/jennykim/Desktop/Unique-Sandwich/background"
# save path
savepath = "/Users/jennykim/Desktop/Unique-Sandwich/result"

# the max number of files it can create
howMany = 50
# start numbering from this number (should be the last file #)
startNum = 0
# for txt file
allCreatedFoxes = []
# for this task
createdFoxes = []
success = 0

# read the data from properties.txt
with open('properties.txt') as file:
    for line in file:
        createdFoxes.append(line.split(" #")[0])

all_file = listdir(SOURCE)

combination_stack = []

for file in all_file:
    if file.startswith("."):
        continue
    if path.isdir(file):
        combination_stack.append(path.join(SOURCE, file))

combination_map = {}

for combination_type in combination_stack:
    all_items_in_one_type = listdir(combination_type)
    if combination_type.split("/")[-1].startswith("_"):
        continue
    if combination_type.split("/")[-1] == "body":
        continue
    if combination_type.split("/")[-1] == "background":
        continue
    all_items_in_one_type = list(filter(lambda x: x.startswith(".") == False, all_items_in_one_type))
    if not all_items_in_one_type:
        continue
    combination_map[combination_type.split("/")[-1]] = all_items_in_one_type
 
while success < howMany:
    # read background
    backgroundfiles = os.listdir(SOURCE + "background")
    background = random.choice(backgroundfiles)
    if background == '.DS_Store':
        continue
    backgroundName = background[:len(background) - 4]
    thisProperty = backgroundName

    # read body
    bodyfiles = os.listdir(SOURCE + "body")
    body = random.choice(bodyfiles)
    if body == '.DS_Store':
        continue
    bodyName = body[:len(body) - 4]
    thisProperty = thisProperty + " " + bodyName

    background_image = Image.open("background/" + background)
    body_image = Image.open("body/" + body)
    background_image.paste(body_image, (0,0), body_image)

    for i, (k, v) in enumerate(sorted(combination_map.items())):
        # read one of the folders
        thisfiles = os.listdir(SOURCE + k)
        this = random.choice(thisfiles)
        while this.endswith('.DS_Store'):
            this = random.choice(thisfiles)
        thisName = this[:len(this) - 4]
        # name the property
        thisProperty = thisProperty + " " + thisName

        this_image = Image.open(k + "/" + this)
        background_image.paste(this_image, (0,0), this_image)

    # thisProperty would be in [acc body #num] format
    if thisProperty in createdFoxes:
        continue
    success = success + 1
    createdFoxes.append(thisProperty)
    allCreatedFoxes.append(thisProperty + " #" + str(startNum + success))

    filename = os.path.join(savepath, "#" + str(startNum + success) + ".png")
    while exists(filename):
        startNum += 1
        filename = os.path.join(savepath, "#" + str(startNum + success) + ".png")
    background_image.save(filename)

else:
    print("Done!")
    with open('properties.txt', 'a') as f:
        for fox in allCreatedFoxes:
            f.write(fox + "\n")