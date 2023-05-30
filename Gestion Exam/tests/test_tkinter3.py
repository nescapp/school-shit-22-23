from typing import Optional, Tuple, Union
import customtkinter
from PIL import Image
from tkinter import messagebox
from functools import partial

# set appearance mode and default color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class ScrollableFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, command=None, **kwargs):
        super().__init__(master, **kwargs)

        # # self.command = command
        self.label_list = []
        # for i, item in enumerate(item_list):
        #     self.add_item(item)

    def add_item(self, item, command=None):
        # Label = customtkinter.CTkLabel(
        #     self, text=item, font=customtkinter.CTkFont(size=20, weight="bold")
        # )
        # Label.grid(row=len(self.label_list), column=0, padx=30, pady=30)
        # self.label_list.append(Label)
        button_item = customtkinter.CTkButton(
            self, text=item, font=customtkinter.CTkFont(size=20, weight="bold"), height=120, command=command
        )
        button_item.grid(row=len(self.label_list), column=0, padx=10, pady=10, sticky="nsew")
        self.label_list.append(button_item)


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
        self.frame_main = customtkinter.CTkFrame(self, width=200, height=200, border_color="#FF0000", border_width=5)
        self.frame_main.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.frame_main.grid_columnconfigure(0, weight=1)
        self.frame_main.grid_rowconfigure(1, weight=1)

        # create main frame widgets
        self.label_heading = customtkinter.CTkLabel(
            self.frame_main,
            text="Show all QCMs",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label_heading.grid(row=0, column=0, padx=30, pady=30)

        self.scrollable_frame = ScrollableFrame(
            master=self.frame_main, border_color="#0000FF", border_width=2 # item_list=[f"QCM {i}" for i in range(10)]
        )
        # print item_list
        self.scrollable_frame.grid(row=1, column=0, padx=15, pady=15, sticky="nesw")
        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.scrollable_frame.add_item("QCM 1", lambda: self.show_qcm_frame(1))
        for i in range(2, 10):
            print(i)
            action_with_arg = partial(self.show_qcm_frame, i)
            self.scrollable_frame.add_item(f"QCM {i}", action_with_arg)

        # create qcm frame
        self.frame_qcm = customtkinter.CTkFrame(self, width=200, height=200, border_color="#FF0000", border_width=5)
        
        
        # create qcm frame widgets
        self.label_heading = customtkinter.CTkLabel(
            self.frame_qcm,
            text="Show QCM",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label_heading.grid(row=0, column=0, padx=30, pady=30)

        self.button_back = customtkinter.CTkButton(
            self.frame_qcm,
            text="Back",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.show_main_frame
        )
        self.button_back.grid(row=1, column=0, padx=30, pady=30)

    def show_qcm_frame(self, qcm_id):
        self.frame_main.grid_forget()
        self.label_heading.configure(text=f"QCM {qcm_id}")
        self.frame_qcm.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def show_main_frame(self):
        self.frame_qcm.grid_forget()
        self.frame_main.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
