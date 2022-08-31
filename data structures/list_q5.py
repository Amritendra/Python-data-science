#create a list if n numeric elemnt
# generate a list of only even number from existing list
#list of only odd number 
#list of only only numer>n from existing list,where n can be any value

l=[2,3,6,8,4,7,8,7,4,56,7,34,6,7,8,7,4,5,6,8,3,4,5,6,89,20,30]
xe=[]
xo=[]
x_greater=[]
for i in l:
    if i%2==0:
        xe.append(i)
    else:
        xo.append(i)

n=int(input("enter any value:"))
for i in l:
    if i > n:

        x_greater.append(i)



print(l)
print(xe)
print(xo)
print(x_greater)





