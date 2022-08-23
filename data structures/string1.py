#accessing string charactersn in python
from operator import index


#first char 0 index
#last char -1 index

str="digipodium"
print('str=',str)

#first charcter
print('str[0]=',str[0])
print('str[1]=',str[1])
print('str[-4]=',str[-4])
print('str[-6]=',str[-6])
print('str[7]=',str[7])

#slicing
a="amritsingh"
s1=a[3:7]
print(s1)
s2=a[2:8]
print(s2)
s3=a[-1:]

s4=a[4:len(a)]
s5=a[4:]
s6=a[:4]
print(s4)
print(s5)
print(s6)
print(s3)


