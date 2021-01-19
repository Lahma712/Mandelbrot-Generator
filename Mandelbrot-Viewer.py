from PIL import Image
from PIL import ImageDraw
import getpass
from io import BytesIO

maxIt = int(input("Iteration depth: "))
Q = input("Colors? y/n ")

if Q == "y":
    offset = int(input("Background color (Red:0-15|Yellow:15-50|Green:50-110|Blue:110-170|Violet:170-240|Red:240-250): "))
    light = int(input("Lightness (0-255) : "))
    glow = int(input("White glow (positive integer between 0-20 f.ex): "))
else:
    Q2 = (input("Options:\n-White outlines on black background (wout) \n-Black outlines on white background (bout) \n-Black on white background (b)\n-White on black background (w)\n")).lower()
    glow = int(input("glow (positive integer between 1-10 f.ex): "))
    if glow == 0:
        glow = 1

W = int(input("Width of resolution (pixels): "))
H = int(input("Height of resolution (pixels): "))
ratio = float(H/W)
xStart = float(input("Start value for X: ")) #starting x coord
xEnd = float(input("End value for X: ")) #ending x coord
xDist = abs(xStart -xEnd) #distance between xstart and xend (distance of x axis)
yDist = xDist * ratio #calculates correct y axis distance based on ratio of H and W (if not, picture will be distorted)
yvalue = float(input("Y value (= will be the middle of the screen): ")) #y coord at which the image will be at 
img = Image.new('HSV', (W, H))
draw = ImageDraw.Draw(img)


def mandelbrot(c,maxIt): #mandelbrot function
    z = 0
    n = 0
    while abs(z) <= 2 and n < maxIt:
        z = z * z + c
        n += 1
    return n


def Draw(W, H, xStart, xDist, yvalue, yDist, maxIt, draw, hue, saturation, value, glow, a, b, Qcolor):
    for x in range(0, W):
        for y in range(0, H):
            c = complex(xStart + abs(xDist) * (x / W), (yvalue + (yDist/2)) - yDist * (y / H))
            cIt = mandelbrot(c,maxIt)
            color = int((255 * cIt) / maxIt)

            if Qcolor == True:
                if color + offset > 255:
                    hue = (color+offset)-255
                else:
                    hue = color + offset
                    saturation = 255 - glow * color

            draw.point([x, y], (hue, saturation, value if cIt == maxIt else a+b*glow * color))

    bytes_io = BytesIO()
    img.convert('RGB').save(bytes_io, 'PNG')
    img.show()



if Q == "n":
    if Q2 == "wout":
        Draw(W, H, xStart, xDist, yvalue, yDist, maxIt, draw, 0, 0, 0, glow, 0, 1, False)
    elif Q2 == "bout":
        Draw(W, H, xStart, xDist, yvalue, yDist, maxIt, draw, 0, 0, 255, glow, 255, -1, False)
    elif Q2 == "b":
        Draw(W, H, xStart, xDist, yvalue, yDist, maxIt, draw, 0, 0, 0, glow, 255, -1,  False)
    elif Q2 == "w":
        Draw(W, H, xStart, xDist, yvalue, yDist, maxIt, draw, 0, 0, 255, glow,0, 1, False)
        
else:
    Draw(W, H, xStart, xDist, yvalue, yDist, maxIt, draw, 0, 0, 0, light, True)




        