from PIL import Image,ImageDraw,ImageFont# these classs help to draw images
im=Image.open('computer.jpg')
im2=Image.open(r'C:\Users\lenovo\Documents\Python data science\scenes.jpg')#absolute addressing
font=ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf',140)
font2=ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf',40)

imd=ImageDraw.Draw(im)
imd.text((200,100),'computerpict',fill=(255,150,0),font=font)
imd.text((700,700),'Rs. 100.00',fill=(0,0,0),font=font2)
im.save('edited_computer.jpg')