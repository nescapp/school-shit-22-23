# Converts my big brain code to a simple version for your little brain, retard
import tkinter as tk
from tkinter import filedialog
import os

print("\033[92;1mStarting, please select a file in the window...\033]0m")

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
if file_path[-3:] == ".py":
    print(file_path)
    file_name = file_path.split("/")[-1]
    print(f"\n\033[1m{file_name}\033[0m selected")
    file = open(file_path, "r")
    file_content = file.read().splitlines()
    file.close()

    new_file_content = ""
    removed_comments_count = 0
    removed_color_codes_count = 0
    variables = []

    for line in range(len(file_content)):
        # store variables if found
        if file_content[line].find("=") != -1 and file_content[line].find("==") == -1:
            variables.append(file_content[line].split("=")[0].split(".")[-1].strip())

        # changes
        if file_content[line].find("#") != -1:
            index = file_content[line].find("#")
            file_content[line] = file_content[line][:index]
            removed_comments_count += 1

        if file_content[line].find(r'"""') != -1:
            index1 = file_content[line].find(r'"""')
            index2 = file_content[line].find(r'"""', index1+3)
            file_content[line] = file_content[line][:index1] + file_content[line][index2+3:]
            removed_comments_count += 1
        
        while file_content[line].find(r"\t") != -1:
            index = file_content[line].find(r"\t")
            file_content[line] = file_content[line][:index] + file_content[line][index+2:]
        
        while file_content[line].find(r"\033[") != -1:
            index1 = file_content[line].find(r"\033[")
            index2 = file_content[line].find("m", index1)
            file_content[line] = file_content[line][:index1] + file_content[line][index2+1:]
            removed_color_codes_count += 1

        new_file_content += file_content[line]
        new_file_content += "\n"

    print(f"\033[1m{len(variables)}\033[0m variables found")
    print(f"\033[1m{removed_comments_count}\033[0m comments removed")
    print(f"\033[1m{removed_color_codes_count}\033[0m color codes removed")

    # remove doubles from list
    variables = list(dict.fromkeys(variables))


    # rename variables by asking the user
    for variable in variables:
        new_variable = input(f"rename \033[1m{variable}\033[0m: ")
        if new_variable != "":
            print(f"\033[2;3mrenamed {variable} to {new_variable}\033[0m")
            new_file_content = new_file_content.replace(variable, new_variable)
        else:
            print(f"\033[2;3mkept {variable}\033[0m")

    # save file
    new_file = open(f"{file_path[:-3]}_version_simple.py", "w")
    new_file.write(new_file_content)
    new_file.close()



else:
    print("\033[91;1mPlease select a .py file\033[0m")

