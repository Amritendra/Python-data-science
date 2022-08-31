f=[]
f.append("apple")
f.append("mango")
f.append('ashmit')
f.append(67)
f.append(89.87)
f.append(True)
print(f)

#insert function
fruits=["apple",'palm','cherry']
fruits.insert(2,'orange')
print(fruits)
dry_fruits=['almond','cashew','walnut']
fruits.extend(dry_fruits)
print(fruits)
friends=['amrit','gaurav','parth']
friends.append("parth")
print(friends)
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
fruits.remove("cherry")
print(fruits)
fruits.sort(reverse=True)
fruits[::-1]
print(fruits)
x=[1,3,5,7,4,2,2,2,4,4,5,5,6,7,]
x.reverse()

print(x)
x.sort(reverse=True)
print(x)
print(x.count(2))
