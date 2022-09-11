#variable arguments - args
#keywords arguments - kwargs

def total(*values):
    t=0
    for i in values:
        if isinstance(i,(int,float)):
            t+=i
    return t

o=total(1,2,3,4)
print(o)
o=total()
print(o)
o=total(1,6,6556,86,43,76,77,325,567,876,34,76)
print(o)
o=total(1,2,321,'a',312,312,'c',65,878,9897)
print(o)
