set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

difference_set1 = set1.difference(set2)
print(difference_set1)

difference_set2 = set2.difference(set1)
print(difference_set2)

union_set = set1.union(set2)
print(union_set)

symdiff_set1 = set2.symmetric_difference(set1)
print(symdiff_set1)

symdiff_set2 = set1.symmetric_difference(set2)
print(symdiff_set2)

intersection_set1 = set1.intersection(set2)
print(intersection_set1)

intersection_set2 = set2.intersection(set1)
print(intersection_set2)