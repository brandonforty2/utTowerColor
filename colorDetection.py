#Detects the color of the tower and saves it to variables

from PIL import Image
from aquireImage import aquireImage
import time

aquireImage()   #Downloads the image file
#time.sleep(5)

try:
        path = "tower.jpg"
        im = Image.open(path)

#If there is no file, print error and exit
except IOError:
        print("File not found")
        raise SystemExit

baseBox = (718,217,731,358)         #Bounding box for the base of the tower
baseRegion = im.crop(baseBox)   
baseX = 731 - 718
baseY = 358 - 217

baseRegion.show()

baseColor = (42,42,42)
R = 0
G = 0
B = 0

#Check each pixel and see what color it is, then add it to a total for each color
for y in range(baseY):     
    for x in range(baseX):
        color = baseRegion.getpixel((x,y))

        R = R + color[0]
        G = G + color[1]
        B = B + color[2]

#Get average color for R,G,and B based on total from loop and amount of pixels in photo
totalPix = baseX * baseY
R = int(R/totalPix)
G = int(G/totalPix)
B = int(B/totalPix)
baseColor = (R,G,B)

topBox = (695,139,728,179)
topRegion = im.crop(topBox)
topX = 33
topY = 40

topRegion.show()

topColor = (42,42,42)

R = 0
B = 0
G = 0


for y in range(topY):
    for x in range(topX):
        color = topRegion.getpixel((x,y))

        R = R + color[0]
        G = G + color[1]
        B = B + color[2]
        #print((R,G,B))

totalPix = topX * topY
R = int(R/totalPix)
G = int(G/totalPix)
B = int(B/totalPix)
topColor = (R,G,B)

#Prints outputs to console

#print("Color of tower base")
#print(baseColor)
#print("\n")
#print("Color of tower top")
#print(topColor)

#Write outputs to a file with base being first and top being second
f = open("data.txt", "w")
#Write each data point to a new line, maybe make a csv file?
def writeData(colorTuple):
        commas = 2
        for c in colorTuple:
                #w = int(c)
                w = str(c)
                f.write(w)
                if (commas > 0):
                        f.write(",")
                        commas = commas - 1
                else:
                        f.write("\n")

#writeData(baseColor)
#writeData(topColor)

#Figure out the actual color of the tower

if (100 < baseColor[0] < 200):
        if (50 < baseColor[1] < 150):
                if (50 < baseColor[2] < 150):
                        baseColorName = "Orange"
                        baseColorNumber = "0"

elif (175 < baseColor[0] < 255):
        if (175 < baseColor[1] < 255):
                if (175 < baseColor[2] < 255):
                        baseColorName = "White"
                        baseColorNumber = "1"

elif (0 < baseColor[0] < 100):
        if (0 < baseColor[1] < 100):
                if (0 < baseColor[2] < 100):
                        baseColorName = "Dark"
                        baseColorNumber = "2"

else:
        baseColorName = "Unknown"
        baseColorNumber = "-1"

if (150 < topColor[0] < 255):
        if (100 < topColor[1] < 200):
                if (50 < topColor[2] < 150):
                        topColorName = "Orange"
                        topColorNumber = "0"

        elif (200 < topColor[1] < 255):
                topColorName = "White"
                topColorNumber = "1"

elif (0 < topColor[0] < 100):
        topColorName = "Dark"
        topColorNumber = "2"

else:
        topColorName = "Unknown"
        topColorNumber = "-1"

#print("The tower is " + baseColorName + " today!")

#Output the color of the tower to console and a file
if (topColorName == "White"):
        print("The tower is white today!")
        f.write("1,1")

if (topColorName == "Orange" and baseColorName == "White"):
        print("The tower is orange and white today!")
        f.write("0,1")

if (baseColorName == "Orange"):
        print("The tower is orange today!")
        f.write("0,0")

if (baseColorName == "Dark"):
        print("The tower is dark today")
        f.write("2,2")

####################
##Expected Outputs##
####################

#Orange Base:   (159,77,74)
#Orange Top:    (235,127,114)

#White Base:    (211,211,207)
#White Top:     (239,244,244)

#Dark Base:     (57,47,50)
#Dark Top:      (56,44,49)

#Tower can be:
        #White
        #White and Orange
        #Orange
        #Dark

#What to do next:
    #Yeet loud and proud
    #Turn into a twitter bot that uploads a cropped image of the tower and says the state
    #Implement into the discord server somehow (MUCH LATER LOL)