#Detects the color of the tower and saves it to variables

from PIL import Image

path = "C:/Users/brand/Desktop/fulldark.jpg"
im = Image.open(path)

baseBox = (670,208,755,372)         #Bounding box for the base of the tower, img size is 85x164
baseRegion = im.crop(baseBox)   
baseX = 85
baseY = 164

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
R = R/totalPix
G = G/totalPix
B = B/totalPix
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
R = R/totalPix
G = G/totalPix
B = B/totalPix
topColor = (R,G,B)

#Prints outputs to console
print("Color of tower base")
print(baseColor)
print("\n")
print("Color of tower top")
print(topColor)

####################
##Expected Outputs##
####################

#Orange Base:   (107,92,87)
#Orange Top:    (235,127,114)

#White Base:    (207,206,204)
#White Top:     (239,244,244)

#Dark Base:     (73,62,64)
#Dark Top:      (56,44,49)

#What to do next:
    #Change the base box so it gets values from a section of the tower instead of the whole thing
    #Add color detection to output *Tower is Orange today*
    #Yeet loud and proud
    #Add error detection in case there is no image file present
    #Add the ability to download the image file, maybe create new py file and call it here
    #Turn into a twitter bot that uploads a cropped image of the tower and says the state
    #Implement into the discord server somehow (MUCH LATER LOL)