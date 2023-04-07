# class bcolors:
#     """Class for colors in the terminal."""
#     HEADER = '\033[95m'
#     OKBLUE = '\033[94m'
#     OKCYAN = '\033[96m'
#     OKGREEN = '\033[92m'
#     WARNING = '\033[93m'
#     FAIL = '\033[91m'
#     ENDC = '\033[0m'
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'

# # green text
# print(f"{bcolors.OKGREEN}Hello World !{bcolors.ENDC}")
# print(f"{bcolors.WARNING}Hello World !{bcolors.ENDC}")

# # print most frequent element in a list
# liste = [1, 2, 2, 2, 2, 3, 4, 4, 4]
# print(max(set(liste), key=liste.count))

# # round to 2 decimals
# print(round(1.525252, 2))

# # or do this
# price_val = 6.12658

# print(f'{price_val:.2f}') # 6.13

# # print a list 
# t = [1, 2, 3, 4, 5]
# print(*t)

# # print large numbers with commas
# a = 1_000_000_000
# print(f'{a:,}')

# # print number with leading zeros
# print(f'{123:05}')

# # list comprehension
# numbers = [i for i in range(100)]
# print(numbers)

# get the name of a variable from a string
variable = '        something = "another_variable"'

variables_and_values = {}

# print(variable.split("=")[0].split(".")[-1].strip())
# if the character after the = is not another =, then it is a variable
if variable.find("=") != -1 and variable.find("==") == -1:
    print(variable.split("=")[0].split(".")[-1].strip())
    # get the value | example: "text"
    # print(variable.split("=")[1].strip().strip('"'))
    # make sure the value assigned to the variable is not another variable (example: "text" and not another_variable)
    # todo so, check if it is inside quotes, if it is a number, ignore arrays and dictionaries as well as tuples etc
    # if it is, print "variable assigned to variable"

    if variable.split("=")[1].strip().strip('"').isnumeric() == False:
        print("variable assigned to variable")
    else:
        print("variable assigned to value")
    

        

    # variables_and_values[variable.split("=")[0].split(".")[-1].strip()] = variable.split("=")[1].strip().strip('"')

# print(variables_and_values)