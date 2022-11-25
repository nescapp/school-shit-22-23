def convert_temp(temperature:float):
    return temperature * 9/5 + 32

def mention_moyenne(moyenne:float):
    if moyenne < 10:
        return "Insuffisant"
    elif moyenne < 12:
        return "Passable"
    elif moyenne < 14:
        return "Assez bien"
    elif moyenne < 16:
        return "Bien"
    elif moyenne < 18:
        return "Très bien"
    else:
        return "Excellent"
    
def list_numbers(N:int):
    numbers = []
    reverse_numbers = []
    print("croissant : ", end=" ")
    for i in range(N):
        print(i, end=" ")
        numbers.append(i)
    print("\n", end="")
    print("décroissant : ", end=" ")
    for i in reversed(range(N)):
        print(i, end=" ")
        reverse_numbers.append(i)
    print("\n", end="")
    return numbers, reverse_numbers

def list_even_numbers(N:int):
    even_numbers = []
    for i in range(N):
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

def longest_name(names:list):
    longest_name = names[0]
    for name in names:
        if len(name) > len(longest_name):
            longest_name = name
    return longest_name

print(convert_temp(0))

print(mention_moyenne(15))

print(list_numbers(10))

print(list_even_numbers(10))

print(longest_name(["Jean", "Paul", "Jacques", "Marie", "Pierre"]))
