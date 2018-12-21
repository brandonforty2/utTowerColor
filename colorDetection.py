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

#topRegion.show()

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
print("Color of tower base")
print(baseColor)
print("\n")
print("Color of tower top")
print(topColor)

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

writeData(baseColor)
writeData(topColor)


####################
##Expected Outputs##
####################

#Orange Base:   (159,77,74)
#Orange Top:    (235,127,114)

#White Base:    (211,211,207)
#White Top:     (239,244,244)

#Dark Base:     (57,47,50)
#Dark Top:      (56,44,49)

#What to do next:
    #Add color detection to output *Tower is Orange today*
    #Yeet loud and proud
    #Turn into a twitter bot that uploads a cropped image of the tower and says the state
    #Implement into the discord server somehow (MUCH LATER LOL)