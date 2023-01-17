import tkinter as tk
from tkinter import messagebox
import random
# temp variables until we figure out how to use Maisons class
temp_houses_owned = 0
temp_houses = []

class Maisons:
    """Class method to create a Maison object. Currently not used"""
    def __init__(self, model, latitude, longitude, surface):
        self.model = model
        self.latitude = latitude
        self.longitude = longitude
        self.surface = surface
        Maisons.nb_maison += 1
        if Maisons.nb_maison > Maisons.nb_max_maison:
            raise Exception("Nombre de maison maximum atteint")

    nb_maison = 0
    nb_max_maison = 5


class Grid:
    """Class to build and modify the grid."""
    def __init__(self, master, rows, cols):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cells = []
        self.build_grid()

    def build_grid(self):
        """Method to build the grid."""
        for row in range(self.rows):
            current_row = []
            for col in range(self.cols):
                # create a cell
                # add the cell to the grid
                # bind the cell to the add_house method
                # add the cell to the current row
                # 50% chance of a tree
                cell = tk.Canvas(self.master, width=60, height=60, bg="#33AA33", highlightthickness=3 , highlightbackground="#555555")
                cell.grid(row=row, column=col, padx=5, pady=5)
                cell.bind("<Button-1>", self.add_house)
                current_row.append(cell)
                if random.randint(0, 1) == 1:
                    cell.create_text(30, 30, text="🌳", font=("Arial", 30), fill="#228822")                
            self.cells.append(current_row)
            
    def add_house(self, event):
        """Method to create a house."""
        global temp_houses_owned

        cell = event.widget
        if temp_houses_owned < 5:
            cell["bg"] = "#999999"
            temp_houses_owned += 1
            cell.bind("<Button-1>", self.remove_house)
            # delete everything in the cell
            cell.delete("all") 
            cell.create_text(30, 30, text="🏠", font=("Arial", 30), fill="#555555") # add a house
            # cell.create_text(30, 30, text="🏠", font=("Arial", 20), fill="#"+("%06x"%random.randint(0,16777215))) # random color
            temp_houses.append(cell)
        else:
            messagebox.showinfo("Error", "You can only own 5 houses")
    
    def remove_house(self, event):
        """Method to remove a house."""
        global temp_houses_owned

        cell = event.widget
        if temp_houses_owned > 0:
            cell["bg"] = "#33AA33"
            temp_houses_owned -= 1
            cell.bind("<Button-1>", self.add_house)
            # delete everything in the cell
            cell.delete("all")
            if random.randint(0, 1) == 1: # 50% chance of a tree
                    cell.create_text(30, 30, text="🌳", font=("Arial", 30), fill="#228822")
            temp_houses.remove(cell)

        
# initialize the window
# create the window, set the title, prevent resizing and set the background color
root = tk.Tk() 
root.title("Plan")
root.resizable(False, False)
root.configure(bg="#333333")

# call the Grid class to create the grid and create a confirm button
grid = Grid(root, 10, 10)
confirmButton = tk.Button(root, text="✓ Confirmer",font=("Arial", 12), command=root.destroy)
confirmButton.grid(row=10, column=0, columnspan=10, sticky="we")

# start the tkinter main loop
root.mainloop()

# print info
print(temp_houses)