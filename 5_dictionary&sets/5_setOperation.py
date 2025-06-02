# set operations 
A={ 1, 3, 5, 6, 8, 9}
B= {2, 4, 6, 7, 10, 11}
C={35, 67}

# union operation 
print(A|B)
print(A.union(B))

# insection operation 
print(A&B)
print(A.intersection(B))


# difference operation 
print(A-B)
print(A.difference(B))


#symmetric difference operation 
print(A^B)
print(A.symmetric_difference(B))

# subset and superset operation 
print(A.issubset(B))
print(A.issuperset(B))

# disjoint sets operation
print(A.isdisjoint(C))

