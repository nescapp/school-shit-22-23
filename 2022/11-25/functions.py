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
    numbers = [i for i in range(N)]
    reverse_numbers = [i for i in reversed(range(N))]
    print("croissant :", *numbers)
    print("décroissant : ", *reverse_numbers)
    return numbers, reverse_numbers

def list_even_numbers(N:int):
    even_numbers = [i for i in range(N) if i % 2 == 0]
    return even_numbers

def longest_name(names:list):
    longest_name = names[0]
    longest_name = max(names, key=len)
    return longest_name

print(convert_temp(0))

print(mention_moyenne(15))

print(list_numbers(10))

print(list_even_numbers(10))

print(longest_name(["Jean", "Paul", "Jacques", "Marie", "Pierre"]))
