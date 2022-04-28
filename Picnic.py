from tkinter import *
import random
root = Tk()
root.geometry("400x400")
root.title("Picnic")
root.configure(background  = 'cyan')


random_number = Label(root)
items = ["Bottle", "Tiffin Box", "Handkerchief", "Chips", "Chocolates", "ID Card"]
show_item = Label(root)
show_item["text"] = str(items)


def show():
    list = random.randint(1, 6)
    random_number["text"] = "Put item no " + str(list) + " in bag"
   
    

btn = Button(root, command = show, text = "Which Item to put in bag?", bg = 'gold')

random_number.place(relx = 0.5, rely = 0.6, anchor = CENTER)
show_item.place(relx = 0.5, rely = 0.3, anchor = CENTER)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()