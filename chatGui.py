from tkinter import *
from PIL import ImageTk,Image
# import json
import os
import sys
# imporVt cv2
import json
import re
import random_responses


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

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # print(required_score == len(required_words))
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to list
        score_list.append(response_score)
        # Debugging: Find the best phrase
        # print(response_score, response["user_input"])

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one.
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_responses.random_string()

def botReply():
    global question
    question = questionField.get()
    question = question.lower()
    # print(question)
    # input=question
    answer=get_response(question)
    # answer = bot.get_response(question)
    textarea.insert(END, "YOU:"+question+"\n\n")
    # textarea.insert(END, "Bot: "+str(answer)+'\n\n')
    textarea.insert(END, "Bot: "+answer+'\n\n')
    # pyttsx3.speak(answer)
    questionField.delete(0, END)


root = Tk()

def img_bg1():
    # print(question)
    global img
    if(question.find('library')!=-1):
        print("yes")
        image=Image.open('maps.jpg')
        new_image = image.resize((800,800)) 
        new_image.save('map1000.png')
        img=PhotoImage(file= "map1000.png")
    elif(question.find('admission')!=-1):
        print("reached")
        image=Image.open('pic.png')
        new_image = image.resize((800,800)) 
        new_image.save('map10001.png')
        img=PhotoImage(file= "map10001.png")
    elif(question.find('computer department')!=-1):
        print("reached computer")
        image=Image.open('ask.png')
        new_image = image.resize((800,800)) 
        new_image.save('map100001.png')
        img=PhotoImage(file= "map100001.png")
    elif(question.find('administration')!=-1):
        print("reached administration")
        image=Image.open('canteen.png')
        new_image = image.resize((800,800)) 
        new_image.save('map1000001.png')
        img=PhotoImage(file= "map1000001.png")
    elif(question.find('vc')!=-1):
        print("reached vc")
        image=Image.open('boysHostel.png')
        new_image = image.resize((800,800)) 
        new_image.save('map10000001.png')
        img=PhotoImage(file= "map10000001.png")

def newwindow():
    newWindow = Toplevel(root) 
    newWindow.title("Maps of Departments")
    newWindow.geometry("800x800+100+30")
    img_bg1()
    canvas1 = Canvas(newWindow, width = 400,height=400)
    canvas1.pack(fill = "both", expand = True)
    canvas1.create_image( 0, 0, image =img, anchor = "nw")# Display image
    print(question)
    # os.system('python bg.py')

root.geometry('500x570+100+30')
root.title('SAMARPAN CHATBOT')
root.config(bg='deep pink')

# logoPic = ImageTk.PhotoImage(file="samarpan_logo.png")
""" logoPic=ImageTk.PhotoImage(Image.open('samarpan_logo.png').resize(50,100))

logoPicLabel = Label(root, image=logoPic, bg='deep pink')
logoPicLabel.image=logoPic
logoPicLabel.pack(pady=5) """

centerFrame = Frame(root)
centerFrame.pack()

scrollbar = Scrollbar(centerFrame)
scrollbar.pack(side=RIGHT)

textarea = Text(centerFrame, font=('times new roman', 20, 'bold'),
                height=10, yscrollcommand=scrollbar.set, wrap='word')
textarea.pack(side=LEFT)
scrollbar.config(command=textarea.yview)

questionField = Entry(root, font=('verdana', 20, 'bold'))
questionField.pack(pady=15, fill=X)

askPic = PhotoImage(file='ask.png')
picPic=PhotoImage(file='pic.png')

askButton = Button(root, image=askPic, command=botReply)
askButton.pack()

direction = Button(root,image=picPic,command=newwindow)
direction.pack(side='right')
def click(event):
    askButton.invoke()
root.bind('<Return>', click)
root.mainloop()
