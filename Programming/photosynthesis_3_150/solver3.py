from PIL import Image

a = open('photosynthesis3.txt','r').read().split('\n')[1:-1]

width = len(a)
print width
height = 1
mode = 'RGB'
newWidth = width/369 # 216*369
newHeight = int(width*height/newWidth) + 1

out = Image.new(mode, (newWidth,newHeight), "white")
pixels = out.load()
i = 0
for line in a:
    pixel = tuple([int(z) for z in line.split('\t')])
    ch = i//newWidth
    cw = i%newWidth
    pixels[cw,ch] = pixel
    i = i + 1

out.save('out.png')
