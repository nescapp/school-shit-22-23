from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox


# root
root = Tk()
root.title("Gestion des examens")
root.geometry("800x600")
root.minsize(800, 600)
root.config(background='#41B77F')
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

# pages
page_main = Frame(root, bg='#41B77F')
page_main.grid_columnconfigure(0, weight=1)
page_main.grid_rowconfigure(0, weight=1)
page_main.grid_rowconfigure(1, weight=1)
page_student = Frame(root, bg='#5E5E5E')
page_student.grid_columnconfigure(0, weight=1)
page_student.grid_rowconfigure(1, weight=1)

# load images
image_teacher = Image.open("images/teacher.png")
image_teacher = image_teacher.resize((200, 200), Image.LANCZOS)
image_teacher = ImageTk.PhotoImage(image_teacher)
image_student = Image.open("images/student.png")
image_student = image_student.resize((200, 200), Image.LANCZOS)
image_student = ImageTk.PhotoImage(image_student)
image_hand = Image.open("images/hand.png")
image_hand = image_hand.resize((200, 200), Image.LANCZOS)
image_hand = ImageTk.PhotoImage(image_hand)

def main_page():
    page_main.tkraise()
    # frames
    frame_heading = Frame(page_main, bg='#FF0000')
    frame_heading.grid_columnconfigure(0, weight=1)
    frame_heading.grid_rowconfigure(0, weight=1)
    frame_buttons = Frame(page_main, bg='#0000FF')
    frame_buttons.grid_columnconfigure(0, weight=1)
    frame_buttons.grid_columnconfigure(1, weight=1)
    frame_buttons.grid_columnconfigure(2, weight=1)
    frame_buttons.grid_rowconfigure(0, weight=1)

    # widgets
    heading = Label(frame_heading, text="Gestion des examens", font=("Helvetica", 30), bg='#FF0000', fg='white')

    button_student_mode = Button(frame_buttons, text="Mode étudiant", font=("Helvetica", 20), bg='#41B77F', fg='white', borderwidth=0, relief="solid", command=student_page)
    button_teacher_mode = Button(frame_buttons, text="Mode enseignant", font=("Helvetica", 20), bg='#41B77F', fg='white', borderwidth=0, relief="solid")
    button_quit = Button(frame_buttons, text="Quitter", font=("Helvetica", 20), bg='#41B77F', fg='white', borderwidth=0, relief="solid", command=root.quit)

    imageLabel_teacher = Label(frame_buttons, image=image_teacher, bg='#0000FF')
    imageLabel_student = Label(frame_buttons, image=image_student, bg='#0000FF')
    imageLabel_hand = Label(frame_buttons, image=image_hand, bg='#0000FF')

    # add frames to root
    frame_heading.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    frame_buttons.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)

    # add widgets to frames
    heading.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

    imageLabel_student.grid(row=0, column=0, sticky="nsew")
    imageLabel_teacher.grid(row=0, column=1, sticky="nsew")
    imageLabel_hand.grid(row=0, column=2, sticky="nsew")
    button_student_mode.grid(row=1, column=0, padx=40, pady=40)
    button_teacher_mode.grid(row=1, column=1, padx=40, pady=40)
    button_quit.grid(row=1, column=2, padx=40, pady=40)

def student_page():
    page_student.tkraise()
    # frames
    frame_back = Frame(page_student, bg='#DD0000')
    frame_back.grid_columnconfigure(0, weight=1)
    frame_from = Frame(page_student, bg='#0000FF')
    frame_from.grid_columnconfigure(0, weight=1)

    # widgets

    label_username = Label(frame_from, text="Nom d'utilisateur", font=("Helvetica", 20), bg='#0000FF', fg='white', anchor=CENTER)
    label_password = Label(frame_from, text="Mot de passe", font=("Helvetica", 20), bg='#0000FF', fg='white', anchor=CENTER)

    entry_username = Entry(frame_from, font=("Helvetica", 20), bg='#41B77F', fg='white', borderwidth=0, relief="solid")
    entry_password = Entry(frame_from, font=("Helvetica", 20), bg='#41B77F', fg='white', borderwidth=0, relief="solid")

    button_login = Button(frame_from, text="Se connecter", font=("Helvetica", 20), bg='#41B77F', fg='white', borderwidth=0, relief="solid")
    button_back = Button(frame_back, text="Retour", font=("Helvetica", 20), bg='#41B77F', fg='white', borderwidth=0, relief="solid", command=main_page)

    # add frames to root
    frame_back.grid(row=0, column=0, padx=20, pady=20)
    frame_from.grid(row=1, column=0, padx=20, pady=20)

    label_username.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
    label_password.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
    entry_username.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
    entry_password.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)
    button_login.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=20, pady=20)

    button_back.grid(row=0, column=0, sticky="nw")



# add pages to root
page_main.grid(row=0, column=0, sticky="nsew")
page_student.grid(row=0, column=0, sticky="nsew")

# open main page
main_page()

# mainloop
root.mainloop()