import json
from chatGui import question
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded from by.py '{file}' successfully !")
        return json.load(bot_responses)


response_data = load_json("bot.json")

root = Tk()
root.title("Title")
root.geometry('600x600')

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo)
    label.image = photo #avoid garbage collection

""" def changeBg():
    input=question
    input=input.lower()
    print(input) """
"""     if(input.find('library')):
        Label("image ").pack() """

image = Image.open('maps.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(root, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

# changeBg()
root.mainloop()