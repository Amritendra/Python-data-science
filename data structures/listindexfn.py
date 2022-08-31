#index function
movie=['udariya:jaoud','prem che:achhaji',"kal ho na ho:srk king"]
print(movie.index('prem che:achhaji'))

#copy function
fruits=["apple",'palm','cherry']
dup_fruits=fruits.copy()
print(dup_fruits)
val=fruits
val.append("cherry")
print(val)
print(fruits)

#clear function
fruits.clear()
print(fruits)

#by list.pop() functiion
fruits=["apple",'palm','cherry']
v=fruits.pop()
print(v)
#by ;ist.pop(idx)
print(fruits.pop(0))

