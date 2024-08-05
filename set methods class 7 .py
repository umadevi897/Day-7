# union
set1={1,2,3}
set2={4,5,6}
print(set1.union(set2))

set1={1,2,3}
set2={4,5,6}
print(set1.intersection(set2))

set1={1,2,3}
set2={4,5,6}
print(set1.difference(set2))

set1={1,2,3}
set2={4,5,6}
print(set1.symmetric_difference(set2))


set1={1,2,3}
set2={5,6,7,2}
print(set1.isdisjoint(set2))


set1={1,2,3}
set2={5,6,7}
print(set1.issubset(set2))

# set1={1,2,3}
# set2={4,5,6,2}
# print(set1.issuperset(set2))

# set1={1,2,3,4,5}
# set2={1,2,3}
# print(set1.issuperset(set2))


# set1={1,2,3}
# set2={1,2,3,4,5}
# print(set1.issuperset(set2))

# adding for loop 

for j in{1,2,3,24,4,45}:
    if j==1:
        print("yes")
        break
    else:
        print("false")


# frozen set

h=[12,33,4,4]
print(type(h))
d=frozenset(h)
print(list(d))



