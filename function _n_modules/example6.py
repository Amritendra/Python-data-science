lambda a,b:a+b

adder=lambda a,b:a+b
adder(69,225)

def exp(power):
    return lambda l:[a**power for a in l ]
four=exp(4)
four([2,4,6,8,10])

print(adder)

x=[1,2,3,4,5,6,7,7,8,4,3,2]
o=list(map(lambda i:i**2,x))
print(o)

x=[2,2,5,6,3,6,7,5,8,5,7]
x2=list(map(lambda i:i-5,x))
print(x2)

y=[2,2,5,6,3,7,5,8,5,7,8,5,3,4,3,2]
xy=list(map(lambda a,b:a+b,x,y))
print(xy)
y2=list(filter(lambda i:i>3,x))
print(y2)

name=['amrit singh','ashmita pandey','pratham singh',
'gaurav verma','parth singh']
name_singh=list(filter(lambda n:n.endswith('singh'),name))
print(name_singh)
name_a=list(filter(lambda n:n.startswith('a'),name))
print(name_a)
print(range(1,10))