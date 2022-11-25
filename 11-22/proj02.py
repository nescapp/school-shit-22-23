import tkinter as tk
housesOwned = 1
class Grid:
    def __init__(self, master, rows, cols):
        self.master = master
        self.rows = rows
        self.cols = cols
        self.cells = []
        self.build_grid()

    def build_grid(self):
        for row in range(self.rows):
            current_row = []
            for col in range(self.cols):
                cell = tk.Canvas(self.master, width=50, height=50, bg="green")
                cell.grid(row=row, column=col)
                cell.bind("<Button-1>", self.change_color)
                current_row.append(cell)
            self.cells.append(current_row)

    def change_color(self, event):
        global housesOwned

        cell = event.widget
        if housesOwned <= 5:
            cell["bg"] = "white"
            housesOwned += 1
        else:
            print("Vous avez déjà 5 maisons")

root = tk.Tk()
grid = Grid(root, 10, 10)
root.mainloop()