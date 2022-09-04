movies={'m1':'sholay','m2':'devdas','m3':'splash'}
print(movies)
print(movies.keys())
print(movies.values())
#traversing a dictionary  style one gives only keys
print('style 1')
for name in movies:
    print(name)
#gives only values
print('style 2')
for key in movies:
    print(movies[key])

#gives keys and values

print('style 3')
for key in movies:
    print(key,movies[key])

#gives key and values
print('style 4')
for k,v in movies.items():
    print(k,v)



