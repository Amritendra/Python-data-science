#create a fibonacci series in a list of size n

fib=[0,1,]
for i in range(10):
    fib.append(fib[-1]+fib[-2])
print(fib)