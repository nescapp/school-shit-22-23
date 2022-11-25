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
                cell = tk.Canvas(self.master, width=50, height=50, bg="green", highlightthickness=2)
                cell.grid(row=row, column=col, padx=5, pady=5)
                cell.bind("<Button-1>", self.change_color)
                current_row.append(cell)
                cell.create_text(25, 25, text="🌳", font=("Arial", 20), fill="darkgreen")
                # color text green
            self.cells.append(current_row)

    def change_color(self, event):
        global housesOwned

        cell = event.widget
        if housesOwned <= 5:
            cell["bg"] = "lightgrey"
            housesOwned += 1
            cell.unbind("<Button-1>")
            # remove the tree
            cell.delete("all")
            cell.create_text(25, 25, text="🏠", font=("Arial", 20), fill="grey")
        else:
            print("Vous avez déjà 5 maisons")

        
    

root = tk.Tk()
root.title("Plan")
root.resizable(False, False)
# change background color
root.configure(bg="#8a8780")
grid = Grid(root, 10, 10)
confirmButton = tk.Button(root, text="Confirmer", command=root.destroy)
confirmButton.grid(row=10, column=0, columnspan=10, sticky="we")
root.mainloop()