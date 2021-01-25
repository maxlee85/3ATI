#adding some comments to test git commands
#add more comments

from PIL import Image, ImageDraw

# size of image
canvas = (1440, 960)

# rectangles (width, height, left position, top position)
#frames = [(50, 50, 5, 5), (60, 60, 100, 50), (100, 100, 205, 120)]

# init canvas
#im = Image.new('RGBA', canvas, (255, 255, 255, 255))
#draw = ImageDraw.Draw(im)
#im2 = Image.new('RGBA', canvas, (255, 255, 255, 255))
#draw2 = ImageDraw.Draw(im2)
#im3 = Image.new('RGBA', canvas, (255, 255, 255, 255))
#draw3 = ImageDraw.Draw(im3)
im4 = Image.new('RGBA', canvas, (255, 255, 255, 255))
draw4 = ImageDraw.Draw(im4)

# draw vertical lines
#x=0
#while x <= 480:
#    draw.line((x,0, x,480), fill=1)
#    x+=2

# draw horizontal lines
#y=0
#while y <= 480:
#    draw2.line((0,y, 480,y), fill=1)
#    y+=2

# draw grid
#x=0
#y=0
#while y <= 480:
#    draw3.line((x,0, x,480), fill=1)
#    draw3.line((0,y, 480,y), fill=1)
#    y+=2
#    x+=2

# draw rectangles
#x=0
#y=1
#while x <= 480:
#    draw4.line([x, 0, x, 480], fill=(0,0,y))
#    x+=1
#    y+=1

draw4.rectangle([(0,0),(1440,960)],fill='Red')

# show image
#im.show()
#im2.show()
#im3.show()
im4.show()
#im.save("/Users/maxwell/Downloads/ImageTest/Vert.gif")
#im2.save("/Users/maxwell/Downloads/ImageTest/Hori.gif")
#im3.save("/Users/maxwell/Downloads/ImageTest/Grid.gif")
im4.save("/Users/maxwell/Downloads/ImageTest/Red.gif")
