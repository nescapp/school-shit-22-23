from typing import Optional, Tuple, Union
import customtkinter
from PIL import Image
from tkinter import messagebox

# set appearance mode and default color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class ScrollableFrame(customtkinter.CTkFrame):
    def __init__(self, master, item_list, command=None, **kwargs):
        super().__init__(master, **kwargs)

        self.command = command
        self.radiobutton_list = []
        for i, item in enumerate(item_list):
            self.add_item(item)

    def add_item(self, item):
        Label = customtkinter.CTkLabel(
            self, text=item, font=customtkinter.CTkFont(size=20, weight="bold")
        )
        Label.grid(row=len(self.radiobutton_list), column=0, pady=(0, 10))
        self.radiobutton_list.append(Label)


class App(customtkinter.CTk):
    # window size
    width = 800
    height = 600

    def __init__(self, *args, **kwargs):
        # call super constructor
        super().__init__(*args, **kwargs)

        # configure root
        self.title("Show all QCMs")
        self.geometry(f"{self.width}x{self.height}")
        self.minsize(self.width, self.height)
        self.config(background="#41B77F")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # create main frame
        self.frame_main = customtkinter.CTkFrame(self, width=200, height=200)
        self.frame_main.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.frame_main.grid_columnconfigure(0, weight=1)

        # create main frame widgets
        self.label_heading = customtkinter.CTkLabel(
            self.frame_main,
            text="Show all QCMs",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label_heading.grid(row=0, column=0, padx=30, pady=30)

        self.scrollable_frame = ScrollableFrame(
            master=self, width=200, item_list=[f"item {i}" for i in range(50)]
        )
        self.scrollable_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")
        self.scrollable_frame.add_item("new item")


if __name__ == "__main__":
    app = App()
    app.mainloop()
