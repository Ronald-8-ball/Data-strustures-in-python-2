set1 = {1,2,4,2,3,5,6,4,5}
set2 = {1,3,5,7,9}
set3 = {2,4,6,8}
print(set1)
set1.add(7)
print(set1)

inter = set1.intersection(set2)
print(inter)

dif = set1.difference(set2)
print(dif)

sdif = set1.symmetric_difference(set3)
print(sdif)

u = set2.union(set3)
print(u)