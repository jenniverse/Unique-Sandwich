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
# save path
savepath = "/Users/jennykim/Desktop/Unique-Sandwich/result"

# the max number of files it can create
howMany = 10
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

    thisProperty = accName + " " + bodyName

    # thisProperty would be in [acc body #num] format
    if thisProperty in createdFoxes:
        continue
    success = success + 1
    createdFoxes.append(thisProperty)
    allCreatedFoxes.append(thisProperty + " #" + str(startNum + success))

    acc_image = Image.open("acc/" + acc)
    body_image = Image.open("body/" + body)

    body_image.paste(acc_image, (0,0), acc_image)
    body_image.show()
    filename = os.path.join(savepath, "#" + str(startNum + success) + ".png")
    body_image.save(filename)
else:
    print("Done!")
    with open('properties.txt', 'a') as f:
        for fox in allCreatedFoxes:
            f.write(fox + "\n")
