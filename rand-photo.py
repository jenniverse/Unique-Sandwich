from genericpath import exists
from sre_constants import SUCCESS
from PIL import Image, ImageFilter
import random
import os
import os.path
import glob

# get random acc from folder
accpath = "/Users/jennykim/Desktop/Unique-Sandwich/acc"
# get random body from folder
bodypath = "/Users/jennykim/Desktop/Unique-Sandwich/body"
# get random clothes from folder
clothespath = "/Users/jennykim/Desktop/Unique-Sandwich/clothes"
# save path
savepath = "/Users/jennykim/Desktop/Unique-Sandwich/result"

# the max number of files it can create
howMany = 5000
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

for i in range(howMany):
    # read acc
    accfiles = os.listdir(accpath)
    acc = random.choice(accfiles)
    if acc == '.DS_Store':
        continue
    accName = acc[:len(acc) - 4]

    # read body
    bodyfiles = os.listdir(bodypath)
    body = random.choice(bodyfiles)
    if body == '.DS_Store':
        continue
    bodyName = body[:len(body) - 4]

    # read clothes
    clothesfiles = os.listdir(clothespath)
    clothes = random.choice(clothesfiles)
    if clothes == '.DS_Store':
        continue
    clothesName = clothes[:len(clothes) - 4]

    # name the property
    thisProperty = accName + " " + bodyName + " " + clothesName

    # thisProperty would be in [acc body #num] format
    if thisProperty in createdFoxes:
        continue
    success = success + 1
    createdFoxes.append(thisProperty)
    allCreatedFoxes.append(thisProperty + " #" + str(startNum + success))

    acc_image = Image.open("acc/" + acc)
    body_image = Image.open("body/" + body)
    clothes_image = Image.open("clothes/" + clothes)

    body_image.paste(acc_image, (0,0), acc_image)
    body_image.paste(clothes_image, (0,0), clothes_image)
    # body_image.show()
    filename = os.path.join(savepath, "#" + str(startNum + success) + ".png")
    while exists(filename):
        startNum += 1
        filename = os.path.join(savepath, "#" + str(startNum + success) + ".png")
    body_image.save(filename)

else:
    print("Done!")
    with open('properties.txt', 'a') as f:
        for fox in allCreatedFoxes:
            f.write(fox + "\n")