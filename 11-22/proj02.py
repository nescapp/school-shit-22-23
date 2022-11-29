import tkinter as tk
from tkinter import messagebox
import random
temp_houses_owned = 0
temp_houses = []

class Grid: # Class for the grid
    def __init__(self, master, rows, cols):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cells = []
        self.build_grid()

    def build_grid(self):
        for row in range(self.rows):
            current_row = []
            for col in range(self.cols): # loop to create the cells
                cell = tk.Canvas(self.master, width=50, height=50, bg="green", highlightthickness=2)
                cell.grid(row=row, column=col, padx=5, pady=5)
                cell.bind("<Button-1>", self.add_house) # bind the click event to the change_color method
                current_row.append(cell) # add the cell to the current row
                if random.randint(0, 1) == 1: # 50% chance of a tree
                    cell.create_text(25, 25, text="🌳", font=("Arial", 20), fill="darkgreen")
                # color text green
            self.cells.append(current_row)

    def add_house(self, event): # method to change the color of the cell
        global temp_houses_owned

        cell = event.widget
        if temp_houses_owned < 5:
            cell["bg"] = "lightgrey"
            temp_houses_owned += 1 # add 1 to temp_houses_owned
            cell.unbind("<Button-1>") # unbind the click event
            cell.bind("<Button-1>", self.remove_house)
            # remove the tree
            cell.delete("all") # delete all items in the cell
            cell.create_text(25, 25, text="🏠", font=("Arial", 20), fill="#555555") # add a house
            # cell.create_text(25, 25, text="🏠", font=("Arial", 20), fill="#"+("%06x"%random.randint(0,16777215))) # random color
            temp_houses.append(cell)
        else:
            messagebox.showinfo("Error", "You can only own 5 houses")
    
    def remove_house(self, event):
        global temp_houses_owned

        cell = event.widget
        if temp_houses_owned > 0:
            cell["bg"] = "green"
            temp_houses_owned -= 1
            cell.unbind("<Button-1>")
            cell.bind("<Button-1>", self.add_house)
            cell.delete("all")
            if random.randint(0, 1) == 1: # 50% chance of a tree
                    cell.create_text(25, 25, text="🌳", font=("Arial", 20), fill="darkgreen")



        
    

root = tk.Tk() # create the window
root.title("Plan") # set the title
root.resizable(False, False) # prevent resizing
root.configure(bg="#8a8780") # set the background color

grid = Grid(root, 10, 10) # create the grid with 10 rows and 10 columns
confirmButton = tk.Button(root, text="✓ Confirmer",font=("Arial", 12), command=root.destroy) # create the confirm button
confirmButton.grid(row=10, column=0, columnspan=10, sticky="we") # add the button to the window
root.mainloop() # start the program
print(temp_houses)