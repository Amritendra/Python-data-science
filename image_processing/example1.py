from PIL import Image
im=Image.open('computer.jpg')#relative addr
im2=Image.open(r'C:\Users\lenovo\Documents\Python data science\scenes.jpg')#absolute address
im.show()
print(im)
print(im2)

im.rotate(45).show()
im2.rotate(90).show()