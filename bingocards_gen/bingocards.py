from PIL import Image, ImageFile
from PIL import PSDraw
# with Image.open("Flevofissa drama.png") as im:
#     print(im)
#     im.show()
from PIL import Image
from PIL import PSDraw
from PIL import ImageFont
from PIL import ImageDraw
import random
import textwrap
import time

def bingocard(name):
    random.seed()
    # getting drama items
    drama_list = []
    with open("alvpredics.txt",encoding="utf8") as file:
        for line in file:
            drama_list.append(line[:-1])

    # getting random unique integer array
    integer_list = []
    while len(integer_list) < 25:
        int_to_add = random.randint(0,len(drama_list)-1)
        if int_to_add not in integer_list:
            integer_list.append(int_to_add)

    # Load image and drawing font
    im = Image.open("alvbingo2.png")
    idraw = ImageDraw.Draw(im)



    # edit text for each box
    index = 0
    for x in range(90, 1300, 260):
        for y in range(290, 1400, 230):
            drama_select = integer_list[index]
            drama_item = drama_list[drama_select]
            text = textwrap.fill(drama_item, 10)
            if len(text.split("\n"))>=6:
                font = ImageFont.truetype("arial.ttf", size=25)
                text = textwrap.fill(drama_item, 18)
            if len(text.split("\n"))<=2:
                font = ImageFont.truetype("arial.ttf", size=35)
                text = textwrap.fill(drama_item, 12)
            else:
                font = ImageFont.truetype("arial.ttf", size=30)

            idraw.text((x, y), text, font=font)
            index += 1

    im.save(name)
groupparticipant_string = ""
for i in range(30):
    groupparticipant_string = groupparticipant_string + ", " + str(i)
groupparticipant_string = str(list(range(0,30)))[1:-1]

print(groupparticipant_string)
participants = ["cards3/"+entry.title()+"_bingocard.png" for entry in groupparticipant_string.split(",")]

for participant in participants:
    bingocard(participant)
# for i in range(36):
#     bingocard(str(i)+".png")