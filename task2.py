""" 2.	Find common items in 2
 lists without duplicates.
 Sort result list before output.
"""
list1 = list(map(int, input().split()))

list2 = list(map(int, input().split()))

duplicates = [x for x in list1 if x in list2]
duplicates = list(dict.fromkeys(duplicates))

duplicates.sort()

print(' '.join(map(str, duplicates)))
