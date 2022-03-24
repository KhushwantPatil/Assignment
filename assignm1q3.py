
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Even = []
odd = []
for i in numbers:
    if i%2==0:
        Even.append(i)
    else:
        odd.append(i)
print("Number of Even number is ",len(Even))
print("Number of odd number is ",len(odd))
