from typing import Optional, Tuple, Union
import customtkinter
from PIL import Image
from tkinter import messagebox

# set appearance mode and default color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("images/color_theme.json")


class App(customtkinter.CTk):
    # window size
    width = 1000
    height = 700

    def __init__(self, *args, **kwargs):
        # call super constructor
        super().__init__(*args, **kwargs)

        # configure root
        self.title("Gestion des examens")
        self.geometry(f"{self.width}x{self.height}")
        self.minsize(800, 600)
        # self.config(background="#4c4f69")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # create main frame
        self.frame_main = customtkinter.CTkFrame(self)
        self.frame_main.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)
        self.frame_main.grid_columnconfigure(0, weight=1)
        self.frame_main.grid_columnconfigure(1, weight=1)
        self.frame_main.grid_columnconfigure(2, weight=1)

        # create main frame widgets
        self.label_heading = customtkinter.CTkLabel(
            self.frame_main,
            text="Choisisez votre mode",
            font=customtkinter.CTkFont(size=40, weight="bold"),
        )
        self.label_heading.grid(row=0, column=0, padx=30, pady=30, columnspan=3)

        self.image_eleve = Image.open("images/student.png")
        self.image_eleve = customtkinter.CTkImage(self.image_eleve, size=(100, 100))
        self.image_label = customtkinter.CTkLabel(
            self.frame_main, image=self.image_eleve
        )

        self.button_eleve = customtkinter.CTkButton(
            self.frame_main,
            text="Mode étudiant",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.show_frame_login,
            image=self.image_eleve,
            compound="top",
            width=200,
            height=300,
        )
        self.button_eleve.grid(row=2, column=0, padx=30, pady=15, sticky="nsew")

        self.image_prof = Image.open("images/teacher.png")
        self.image_prof = customtkinter.CTkImage(self.image_prof, size=(100, 100))
        self.image_label = customtkinter.CTkLabel(
            self.frame_main, image=self.image_prof
        )

        self.button_prof = customtkinter.CTkButton(
            self.frame_main,
            text="Mode professeur",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.show_frame_prof,
            image=self.image_prof,
            compound="top",
            width=200,
            height=300,
        )
        self.button_prof.grid(row=2, column=1, padx=30, pady=15, sticky="nsew")

        self.image_quit = Image.open("images/hand.png")
        self.image_quit = customtkinter.CTkImage(self.image_quit, size=(100, 100))
        self.image_label = customtkinter.CTkLabel(
            self.frame_main, image=self.image_quit
        )

        self.button_quit = customtkinter.CTkButton(
            self.frame_main,
            text="Quitter",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.quit,
            image=self.image_quit,
            compound="top",
            width=200,
            height=300,
        )
        self.button_quit.grid(row=2, column=2, padx=30, pady=15, sticky="nsew")

        # create eleve frame
        self.frame_eleve = customtkinter.CTkFrame(self)
        self.frame_eleve.grid_columnconfigure(0, weight=1)

        self.label_heading = customtkinter.CTkLabel(
            self.frame_eleve,
            text="Eleve",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label_heading.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.button_back = customtkinter.CTkButton(
            self.frame_eleve,
            text="Retour",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.back_event,
        )
        self.button_back.grid(row=1, column=0, padx=30, pady=15)

        # create prof frame
        self.frame_prof = customtkinter.CTkTabview(self, width=250)
        self.frame_prof.add("Créer un QCM")
        self.frame_prof.add("Créer un élève")
        self.frame_prof.add("Corriger un QCM")

        self.label_heading = customtkinter.CTkLabel(
            self.frame_prof.tab("Créer un QCM"),
            text="Créer un QCM",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label_heading.grid(row=2, column=0, padx=30, pady=30)

        self.label_heading = customtkinter.CTkLabel(
            self.frame_prof.tab("Créer un élève"),
            text="Créer un élève",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label_heading.grid(row=2, column=0, padx=30, pady=30)

        self.label_heading = customtkinter.CTkLabel(
            self.frame_prof.tab("Corriger un QCM"),
            text="Corriger un QCM",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label_heading.grid(row=2, column=0, padx=30, pady=30)

        self.button_back = customtkinter.CTkButton(
            self.frame_prof,
            text="Retour",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.back_event,
        )
        self.button_back.grid(row=3, column=0, padx=30, pady=15)

        # create login frame
        self.frame_login = customtkinter.CTkFrame(self)
        self.frame_login.grid_columnconfigure(0, weight=1)

        self.label_heading = customtkinter.CTkLabel(
            self.frame_login,
            text="Login",
            font=customtkinter.CTkFont(size=20, weight="bold"),
        )
        self.label_heading.grid(row=0, column=0, padx=30, pady=(150, 15))

        self.button_login = customtkinter.CTkButton(
            self.frame_login,
            text="Login",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.show_frame_eleve,
        )
        self.button_login.grid(row=1, column=0, padx=30, pady=15)

        self.button_back = customtkinter.CTkButton(
            self.frame_login,
            text="Retour",
            font=customtkinter.CTkFont(size=20, weight="bold"),
            command=self.back_event,
        )
        self.button_back.grid(row=0, column=0, padx=30, pady=15)

    def back_event(self):
        # hide eleve frame
        self.frame_eleve.grid_forget()
        self.frame_prof.grid_forget()
        self.frame_login.grid_forget()
        # show main frame
        self.frame_main.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

    def show_frame_login(self):
        # hide main frame
        self.frame_main.grid_forget()
        # show login frame
        self.frame_login.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def show_frame_eleve(self):
        # hide main frame
        self.frame_login.grid_forget()
        # show eleve frame
        self.frame_eleve.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    def show_frame_prof(self):
        # hide main frame
        self.frame_main.grid_forget()
        # show prof frame
        self.frame_prof.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
