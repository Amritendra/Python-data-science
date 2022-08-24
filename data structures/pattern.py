#patternprinting

for i in range(1,7):
    print(i*"*")

for i in range(6,0,-1):
    print(i*"*")

#right alighnment
for i in range(1,6):
    print((i*"A").rjust(15))

for i in range(1,6):
        print((i*"Amrit").center(30))
        for i in range(6,1,-1):
            print((i*"Amrit").center(30))

#PATTERN1
p='*0'
for i in range(1,13,2):
    print((i*"*").center(30))
    print((i*"0").center(30))


#slice example
n="satya saurabh singh"
fn=n[:5]
ln=n[-5:]
mn=n[7:14]
print(fn,ln,mn)

#reversed
rev_name=n[::-1]
print(rev_name)
mn_rev=n[6:-8][::-1]
print(mn_rev)

#every even index character
even_n=n[::2]

#every odd index chgarcter
odd_n=n[1::2]
print(even_n,odd_n)