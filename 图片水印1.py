# coding=utf-8
import os
from PIL import Image,ImageDraw,ImageFont
#from watermarker.marker import add_mark
def drawtext(id1):
    #open image to RGBA layer for the font oppcity
    with Image.open(File_location+file).convert("RGBA") as base:
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
        
        def getfont():
            weight,height = txt.size
            if (weight > height):
                return weight // 60
            else:
                return height // 50

        fnt = ImageFont.truetype("C:\\11426.ttf", getfont())
        d = ImageDraw.Draw(txt)
        d.text((20, 20), 'pid:'+id1+' 侵删', font=fnt, fill=(255, 255, 255, 128))
        out = Image.alpha_composite(base, txt)
        out.save(File_location+'//temp//wt_'+id1+'.png')

def devide(id1):
    name = ''
    count = 0
    #get extension name, if not, break the program.
    ext = file[file.rfind(".") + 1:]
    if ext != 'png' and ext !='jpg' and ext !='webp':
        return None
    #get id, return 1 to start the draw process.
    while 1:
        i = file[count]
        if i != '_':
            name += i
            count +=1
        else:
            return name


    


File_location = input()
File_list = os.listdir(File_location)
for file in File_list:
    i = devide(file)
    if i:
        print(file+' '+i)
        drawtext(i)
