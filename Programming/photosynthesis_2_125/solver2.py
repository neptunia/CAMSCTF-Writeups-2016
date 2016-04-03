from PIL import Image

width = 172800

a = []
out = Image.new('RGB', (172800,1), "white")
pixels = out.load()
for f in range(width):
    p = Image.open("stupidimages/"+str(f)+'.png').getdata()[0]
    pixels[f,0] = p
    if f%100==0:print f

out.save('generatedimg.png')

im = Image.open("generatedimg.png")
width, height = im.size

#height = 1
mode = 'RGB'
newWidth = 172800/360 # 360 by 480
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
