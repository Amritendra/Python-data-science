x=2
while x<8:
    print("run")
    x+=1
print("stop")

#break and continue

for i in range(1,11):
    if (i==8):
        print('out of loop')
        break
    else:
        print(i)

#continue
for i in range(1,11):
    if (i==8):
        continue
    else:
        print(i)