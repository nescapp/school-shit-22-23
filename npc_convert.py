# make the user select a .py file

import tkinter as tk
from tkinter import filedialog
import os

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()
# check if the file is a .py file
if file_path[-3:] == ".py":
    print(file_path)
    # get the file name
    file_name = file_path.split("/")[-1]
    print(f"\033[92m{file_name}\033[0m selected")
    # store the file content in a variable
    file = open(file_path, "r")
    file_content = file.read().splitlines()
    file.close()

    print(f"the file has \033[92m{len(file_content)}\033[0m lines")


    new_file_content = ""

    for line in range(len(file_content)):
        # print(f"\033[2m{line+1}\033[0m") # print line number

        # if file_content[line].startswith("#"):
        #     print(file_content[line])
        #     file_content[line] = ""
        #     print("removed comment")

        # print raw line
        # print(file_content[line])

        # if the line contains "#", pirnt yes
        if file_content[line].find("#") != -1:
            print("yes")
            # find index of "#"
            index = file_content[line].find("#")
            # add empty string to the line
            file_content[line] = file_content[line][:index]
            # remove the comment
            print("removed comment")

        
        while file_content[line].find("\033[") != -1:
            # find index of "\033["
            index1 = file_content[line].find("\033[")
            # find index of next "m" after "\033["
            index2 = file_content[line].find("m", index1)
            # remove the color code
            file_content[line] = file_content[line][:index1] + file_content[line][index2+1:]
            print("removed color code")

        new_file_content += file_content[line]
        new_file_content += "\n"

    # create a new file
    new_file = open(f"{file_name[:-3]}_converted.py", "w")
    new_file.write(new_file_content)
    new_file.close()



else:
    print("Please select a .py file")

