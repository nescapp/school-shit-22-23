# print most frequent element in a list
liste = [1, 2, 2, 2, 2, 3, 4, 4, 4]
print(max(set(liste), key=liste.count))

# round to 2 decimals
print(round(1.525252, 2))

# print a list 
t = [1, 2, 3, 4, 5]
print(*t)

# print large numbers with commas
print("{:,}".format(1000000000))