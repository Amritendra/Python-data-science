'''
def area():
    l=int(input('enter the lenth:'))
    b=int(input('enter the breadth:'))
    area=l*b
    print(f'{l}*{b}={area}')

#calling function/use
area()
'''
def primenumber():
    p=int(input('enter the number:'))
    for i in range(2,p):
        if p%i==0:
            break
    else:
        print(f'{p} is primenumber')
primenumber()

ans=len('hello')+len('xaidsir')
print(ans)