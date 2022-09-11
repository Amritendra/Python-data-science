from PIL import Image,ImageFilter,ImageEnhance#
im=Image.open('computer.jpg')
im2=Image.open(r'C:\Users\lenovo\Documents\Python data science\scenes.jpg')
im2.filter(ImageFilter.EMBOSS).show()
im2.filter(ImageFilter.SHARPEN).show()
im2.filter(ImageFilter.SMOOTH).show()
im2.filter(ImageFilter.MaxFilter).show()
im2.filter(ImageFilter.MinFilter).show() #highlight whte
im2.filter(ImageFilter.MedianFilter).show()#highlights black
im2.filter(ImageFilter.GaussianBlur).save('scenes_blurred.jpg')

eim=ImageEnhance.color(im)
for i in range(-10,11,2):
    eim.enhance(i).show()

imc=im.copy()
im2_s=im2.resize((300,240))
imc.paste(im2_s,(0,0))
imc.paste(im2_s,(0,0))
imc.paste(im2_s,(700,0))
imc.show()