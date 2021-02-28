""" 2.	Find common items in 2
 lists without duplicates.
 Sort result list before output.
"""
list1 = list(map(int, input().split()))
list1.sort()
list2 = list(map(int, input().split()))
list2.sort()
pst3 = []
for p1 in list1:
    if p1 in list2:
        pst3.append(p1)
print("Your input is for list 1 is:", list1)
print("Your input is for list 2 is:", list2)
duplicates = str(pst3)
print("Your input next duplicates is", duplicates)
