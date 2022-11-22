# from tkinter import *

# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)

# maison01 = Label(window, text="Hello")
# maison01.grid(column=0, row=0)

# Canvas(maison01, width=100, height=100, bg="red").grid(column=0, row=0)
# window.mainloop()

# class Maison(nombre_de_maisons, nombre_de_maisons_max):
#     def __init__(self, modele, lat, lon, surface):
#         self.modele = modele
#         self.lat = lat
#         self.lon = lon
#         self.surface = surface

#         print(f"{self.modele} : {self.lat} : {self.lon} : {self.surface}")



# from tkinter import *

# root = Tk()
# canvas=Canvas() # where did you save this? It's very important to keep it!

# def changeBlock( event=None ): 
#         # Here, I'm just making a rectangle of size 10. Make it as big as you want
#         # notice though that you're "self.canvas" will need to reference the
#         # the right thing
#         canvas.create_rectangle(event.x-25,event.y-25,event.x+25,event.y+25,fill='red')

# for row in range(10):
#     for column in range(10):
#         canvas.
#         canvas.create_rectangle(10+(row*53),10+(column*53),60+(row*53),60+(column*53),fill='green')

# # Here, I'm binding to the Canvas. Bind to the widget where the event occurs
# # canvas.bind('<Button-1>',changeBlock)  

# # make sure you add the widget somehow, or else it won't appear
# canvas.grid()  

# root.mainloop()



from tkinter import Tk, Canvas

# window = Tk()

# c = Canvas(window, width=550, height=550)

# def clear():
#     canvas.delete(ALL)

# def clicked(*args):
#     print(f"{args[0].x} : {args[0].y}")
#     print("shit worked!")
#     # c.create_rectangle(10+(row*53),10+(column*53),60+(row*53),60+(column*53),fill='red')

# # playbutton = c.create_rectangle(75, 25, 225, 75, fill="red",tags="playbutton")
# # playtext = c.create_text(150, 50, text="Play", font=("Papyrus", 26), fill='blue',tags="playbutton")

# for row in range(10):
#     for column in range(10):
#         c.create_rectangle(10+(row*53),10+(column*53),60+(row*53),60+(column*53),fill='green', tags="asd")
#         print(f"{row}:{column}")
#         c.tag_bind(f"asd", "<Button-1>", clicked)

# # c.tag_bind("playbutton","<Button-1>",clicked)

# c.pack()

# window.mainloop()


 
from tkinter import *
 
button_list = ['dummy']
class button_box :
    def __init__ (self, button, ID_number, color) :
        self.ID_number = ID_number
        self.button = button
        self.color = color
 
    def clicked (self, event) :
        print (f'You pressed button number {self.ID_number}')
        button.grid_forget()

 
root = Tk()
 
button_number = 1
for y in range(5) :
    for x in range(9) :
        button = Button(width = 5, height = 3, text = button_number)
        button.config(relief = 'solid', borderwidth = 1)
        button.grid(row = y, column = x)
        button_list.append(button_box(button, button_number, "green"))
        button.bind('<Button-1>', button_list[button_number].clicked)
        button_number += 1
 
root.mainloop()