#cfreate alist of10 numbers and then
#genrate alist which hokds the square of original list
#generate a list which holds the cubes vals of original list

l=[34,12,45,65,87,98,87,54,98,67]
l2=[]
l3=[]

for i in l:
    sqr=i**2
    l2.append(sqr)
print(l)
print(l2)

for i in l:
    cube=i**3
    l3.append(cube)
print(l3)
