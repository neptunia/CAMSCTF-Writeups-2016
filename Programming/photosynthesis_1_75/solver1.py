from PIL import Image

im = Image.open("photosynthesis1.png")
width, height = im.size

print width

mode = 'RGB'
newWidth = 55440/240*4/3
newHeight = int(width*height/newWidth) + 1

out = Image.new(mode, (newWidth,newHeight), "white")
pixels = out.load()
i = 0
for pixel in im.getdata():
    ch = i//newWidth
    cw = i%newWidth
    pixels[cw,ch] = pixel
    i = i + 1

out.save('out.png')
