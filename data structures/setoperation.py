A={3,4,5,6,7,8,9,4,2,45}
B={4,2,3,5,6,7,8,9,4,3,45,7,81,1,98}
print(A|B)  # | operator denotes union
print(A.union(B))
print(B.union(A))

print(A&B)   # & operator denotes intersection
print(A.intersection(B))

# set difference (-)
print(A-B)
print(A.difference(B))

print(B-A)
print(B.difference(A))

#set symmetric difference
print(B^A)
print(A.symmetric_difference(B))