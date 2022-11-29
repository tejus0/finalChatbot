import json
import os
import random
import re
import sys
from tkinter import *
import tkinter as tk
import pyttsx3
import random_responses as random_res
from PIL import Image, ImageTk
import sqlite3


def load_json(file):
    with open(file) as bot_responses:
        print(f"Loaded '{file}' successfully !")
        return json.load(bot_responses)


response_data = load_json("bot.json")


def get_response(input_string):
    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required scoreṇ
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user has typed
            for word in split_message:
                # If the worṇd is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    global response_index
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]
    return random_res.random_string()


def textToSpeech(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def botReply():
    global question
    question = questionField.get()
    question = question.lower()
    # print(question)
    # input=question
    answer = get_response(question)
    textToSpeech(answer)
    # answer = bot.get_response(question)
    textarea.insert(END, "YOU:"+question+"\n\n")
    # textarea.insert(END, "Bot: "+str(answer)+'\n\n')
    textarea.insert(END, "Bot: "+str(answer)+'\n\n')
    #engine = pyttsx3.init()
    #engine.say('Hello sir, how may I help you, sir.')
    #pyttsx3.speak("Hello,My name is Gautam")
    questionField.delete(0, END)


root = tk.Tk()


def img_bg1():
    # print(question)
    global img
    if (question.find('library') != -1):
        image = Image.open('library.png')
        new_image = image.resize((800, 800))
        new_image.save('library.png')
        img = PhotoImage(file="library.png")
    elif (question.find('electronics department') != -1):
        image = Image.open('electronics_department.png')
        new_image = image.resize((800, 800))
        new_image.save('electronics_department.png')
        img = PhotoImage(file="electronics_department.png")
    elif (question.find('computer department') != -1):
        image = Image.open('computer_department.png')
        new_image = image.resize((800, 800))
        new_image.save('computer_department.png')
        img = PhotoImage(file="computer_department.png")
    elif (question.find('administrative') != -1):
        image = Image.open('administration.png')
        new_image = image.resize((800, 800))
        new_image.save('administration.png')
        img = PhotoImage(file="administration.png")
    elif (question.find('boys hostel') != -1):
        image = Image.open('Boys_hostel.png')
        new_image = image.resize((800, 800))
        new_image.save('Boys_hostel.png')
        img = PhotoImage(file="Boys_hostel.png")
    elif (question.find('civil department') != -1):
        image = Image.open('civil_department.png')
        new_image = image.resize((800, 800))
        new_image.save('civil_department.png')
        img = PhotoImage(file="civil_department.png")
    elif (question.find('mechanical department') != -1):
        image = Image.open('mechanical_department.png')
        new_image = image.resize((800, 800))
        new_image.save('mechanical_department.png')
        img = PhotoImage(file="mechanical_department.png")
    elif (question.find('canteen') != -1):
        image = Image.open('canteen.png')
        new_image = image.resize((800, 800))
        new_image.save('canteen.png')
        img = PhotoImage(file="canteen.png")
    elif (question.find('shakuntalam') != -1):
        image = Image.open('shakuntalam.png')
        new_image = image.resize((800, 800))
        new_image.save('shakuntalam.png')
        img = PhotoImage(file="shakuntalam.png")
    elif (question.find('girls hostel') != -1):
        image = Image.open('girls_hostel.png')
        new_image = image.resize((800, 800))
        new_image.save('girls_hostel.png')
        img = PhotoImage(file="girls_hostel.png")
    elif (question.find('dispensary') != -1):
        image = Image.open('dispensary.png')
        new_image = image.resize((800, 800))
        new_image.save('dispensary.png')
        img = PhotoImage(file="dispensary.png")
    elif (question.find('vice chancellor') != -1):
        image = Image.open('VC_OFFICE.png')
        new_image = image.resize((800, 800))
        new_image.save('VC_OFFICE.png')
        img = PhotoImage(file="VC_OFFICE.png")
    elif (question.find('playground') != -1):
        image = Image.open('Playground.png')
        new_image = image.resize((800, 800))
        new_image.save('Playground.png')
        img = PhotoImage(file="Playground.png")


def newwindow():
    newWindow = Toplevel(root)
    newWindow.title("Maps of Departments")
    newWindow.geometry("800x800+100+30")
    img_bg1()
    canvas1 = Canvas(newWindow, width=400, height=400)
    canvas1.pack(fill="both", expand=True)
    canvas1.create_image(0, 0, image=img, anchor="nw")  # Display image
    print(question)


root.geometry('500x570+100+30')
root.title('YMCA ROBO')
root.config(bg='brown')

# Create databse
conn = sqlite3.connect('history.db')

# create cursor
c = conn.cursor()

# create table
# c.execute(""" CREATE TABLE ALL_SEARCHES (
#     category text,
#     question text
#     ) """)

# inserting values to database


def submit():
    # Create databse
    conn = sqlite3.connect('history.db')

    # create cursor
    c = conn.cursor()
    c.execute("INSERT INTO ALL_SEARCHES VALUES (:category,:question )",
              {'category': response_data[response_index]["response_type"],
               'question': question
               })
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


def show():
    # Create databse
    conn = sqlite3.connect('history.db')

    # create cursor
    c = conn.cursor()

    c.execute("SELECT *,oid FROM ALL_SEARCHES")
    records = c.fetchall()
    print(records)

    # Loop through records
    print_records = ''
    for record in records:
        print_records += str(record[0]) + '\n'

    query_label = Label(root, text=print_records)
    query_label.pack()
    # Commit changes
    conn.commit()

    # Close connection
    conn.close()


# Commit changes
conn.commit()

# Close connection
conn.close()

image_logo = Image.open('logo.png')
resize_image = image_logo.resize((120, 100))
logoPic = ImageTk.PhotoImage(resize_image)

logoPicLabel = Label(root, image=logoPic, bg='black')
logoPicLabel.pack(pady=5)

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame, font=('times new roman', 20, 'bold'),
                height=5, yscrollcommand=scrollbar.set, wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)


def clear(event):
    questionField.configure(state=NORMAL)
    questionField.delete(0, END)
    questionField.unbind('<Button-1>', clicked)


prewrite = StringVar()
questionField = Entry(root, textvariable=prewrite,
                      font=('verdana', 20, 'bold'))
questionField.insert(0, 'Ask your question here .')
questionField.pack(fill='x', expand=True, padx=45, pady=10)
clicked = questionField.bind('<Button-1>', clear)
textarea.config()

askPic = PhotoImage(file='ask.png')
button_frame = Frame(root, height=10)
button_frame.pack()
askButton = Button(button_frame, text='Ask', command=botReply)
askButton.pack(side=LEFT)

direction = Button(button_frame, text='Locate on map', command=newwindow)
direction.pack(side=RIGHT)

submit_btn = Button(root, text="Add to Records", command=submit)
submit_btn.pack()

""" show_btn=Button(root,text="Add to Records",command=show)
show_btn.pack() """


def click(event):
    askButton.invoke()


root.bind('<Return>', click)
root.mainloop()
