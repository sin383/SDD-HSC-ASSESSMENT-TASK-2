from tkinter import *
import customtkinter as ctk
from PIL import *
import PIL
from os import path
import os
import pyttsx3
import threading

DIR_NAME = path.dirname(path.abspath(__file__))
root = ctk.CTk()
root.geometry("1000x600")
root.title("Miss Chilla Gaming")
root.resizable(width=True, height=True)

#image
L1image2path = path.join(DIR_NAME, "assets", "8.png")
L1image2 = Image.open(L1image2path)


# Load the second image
L1image1path = path.join(DIR_NAME, "assets", "j.png")
L1image1 = Image.open(L1image1path)

yespath = path.join(DIR_NAME, "assets", "back.png")
yes = Image.open(yespath)
yesimage=ctk.CTkImage(yes, size=(700,700))

#load lesson 2 images
L2imagepath = path.join(DIR_NAME, "assets", "numberline.png")
L2 = Image.open(L2imagepath)
L2image = ctk.CTkImage(L2, size=(350,350))

#load lesson 3 images
L3imagepath = path.join(DIR_NAME, "assets", "same.png")
L3 = Image.open(L3imagepath)
L3image = ctk.CTkImage(L3, size=(450,230))

#load lesson 4 images
L4imagepath = path.join(DIR_NAME, "assets", "samed.png")
L4 = Image.open(L4imagepath)
L4image = ctk.CTkImage(L4, size=(450,230))

#load lesson 5 images
L5imagepath = path.join(DIR_NAME, "assets", "mixed.png")
L5 = Image.open(L5imagepath)
L5image = ctk.CTkImage(L5, size=(500,200))

#load lesson 6 images
L6imagepath = path.join(DIR_NAME, "assets", "multiplying.png")
L6 = Image.open(L6imagepath)
L6image = ctk.CTkImage(L6, size=(450,250))

#load lesson 7 images
L7imagepath = path.join(DIR_NAME, "assets", "dividing.png")
L7 = Image.open(L7imagepath)
L7image = ctk.CTkImage(L7, size=(450,300))


# Create CTkImage objects
thefirstimage = ctk.CTkImage(L1image2, size=(400,150))
thesecondimage = ctk.CTkImage(L1image1, size=(70,105))

# Creating a separate frame for the image
image_frame = ctk.CTkFrame(root, corner_radius=0)
image_frame.place(x=0, y=0, relwidth=1, relheight=1)  


mylabel = ctk.CTkLabel(image_frame, text="", image=yesimage)  #image
mylabel.place(x=0, y=0, relwidth=1, relheight=1)

#Creating a frame for labels with rounded edges
label_frame = ctk.CTkFrame(image_frame, corner_radius=100, fg_color="transparent", bg_color="transparent")  # round edges 
label_frame.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)  #relative width and height from the edges so it leaves a small gap so miss chilla can see the background 

TitleLabel = ctk.CTkLabel(label_frame, text= "Fractions made easy", font=('Helvetica', 18, 'bold'))
TitleLabel.place(x=370, y=10)  
root.resizable(width=False, height=False)

engine = pyttsx3.init()
engine.setProperty('rate', 50)


def Quizmenu():
    global Quizframe
    label_frame.place_forget()
    Quizframe = ctk.CTkFrame(image_frame)
    Quizframe.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)

    # Define the questions and the correct answers
    questions = {
        "add_same_denominator": [("What is 1/2 + 1/2?", ["1"]), ("What is 1/4 + 2/4?", ["3/4"]), ("What is 1/9 + 7/9?", ["8/9"]), ("What is 1/7 + 6/7?", ["1", "7/7"]), ("What is 3/5 + 1/5?", ["4/5"]), ("What is 2/6 + 3/6?", ["5/6"]), ("What is 10/100 + 50/100?", ["60/100", "6/10", "3/5"]), ("What is 1/3 + 1/3?", ["2/3"]), ("What is 2/11 + 7/11?", ["9/11"]), ("What is 2/11 + 7/11?", ["9/11"])], 
        "add_diff_denominator": [("What is 1/2 + 1/3?", ["5/6"]), ("What is 1/4 + 1/3?", ["7/12"]), ("What is 1/4 + 1/6?", ["1/2", "3/6"]), ("What is 1/7 + 1/3?", ["10/21"]), ("What is 1/9 + 1/3?", ["4/9"]), ("What is 3/4 + 1/8?", ["7/8"]), ("What is 1/6 + 1/5?", ["11/30"]), ("What is 1/4 + 1/6 + 1/3?", ["8/12", "2/3"]), ("What is 1/6 + 1/3?", ["1/2"])],  
        "add_mixed_improper": [("What is 1 1/2 + 2/3?", ["2 1/6", "13/6"]), ("What is 2 1/4 + 1 2/3?", ["3 11/12", "47/12"]), ("What is 1/4 + 1?", ["5/4", "1 1/4"]), ("What is 1/2 + 4/2?", ["5/2", "2 1/2"]), ("What is 3/4 + 2/3?", ["17/12", "1 5/12"]), ("What is 3/5 + 8/10?", ["7/5", "14/10", "1 2/5"]), ("What is 1/4 + 1/3 + 5/6?", ["17/12", "1 5/12"])],  
        "subtract": [("What is 1/2 - 1/4?", ["1/4"]), ("What is 3/4 - 1/4?", ["1/2"]), ("What is 3/4 - 1/3?", ["5/12"]), ("What is 3/5 - 1/5?", ["2/5"]), ("What is 7/4 - 1/4?", ["6/4", "3/2", "1 1/2"]), ("What is 9/2 - 7/2?", ["1"]), ("What is 3 - 1/4?", ["11/4", "2 3/4"]), ("What is 1/4 - 1/8?", ["1/8"]), ("What is 3/4 - 3/4?", ["0"]), ("What is 7/4 - 3/4?", ["1"])],  
        "multiply": [("What is 1/2 * 1/2?", ["1/4"]), ("What is 1/4 * 2?", ["1/2"]), ("What is 2/3 * 3/4?", ["1/2"]), ("What is 1/5 * 2/3?", ["2/15"]), ("What is 3/4 * 4/5?", ["3/5"]), ("What is 5/6 * 2/3?", ["10/18", "5/9"]), ("What is 7/8 * 1/3?", ["7/24"]), ("What is 2/5 * 3/4?", ["6/20", "3/10"]), ("What is 1/2 * 3/5?", ["3/10"]), ("What is 5/6 * 1/2?", ["5/12"])],  
        "divide": [("What is 1/2 / 1/4?", ["2"]), ("What is 3/4 / 1/2?", ["1 1/2", "3/2"]), ("What is 2/3 / 1/3?", ["2"]), ("What is 5/6 / 1/2?", ["1 1/3", "4/3"]), ("What is 7/8 / 1/4?", ["3 1/2", "7/2"]), ("What is 2/5 / 1/5?", ["4"]), ("What is 1/2 / 1/3?", ["1 1/2", "3/2"]), ("What is 3/4 / 2/3?", ["1 1/8", "9/8"]), ("What is 5/6 / 1/3?", ["2 1/2", "5/2"]), ("What is 7/8 / 1/2?", ["1 3/4", "7/4"])],  
    }

    # Create buttons for each question type
    buttons = []
    for i, question_type in enumerate(questions.keys()):
        button = ctk.CTkButton(Quizframe, text=f"Start {question_type.replace('_', ' ')} quiz", command=lambda question_type=question_type: start_quiz(question_type))
        button.place(relx=0.5, rely=0.1 + i*0.12, anchor='center')  # Place the button in the middle
        button.configure(width=200, height=50)  # Make the button bigger
        buttons.append(button)

    # starting the quiz
    def start_quiz(question_type):
        # Remove the buttons
        for button in buttons:  
            button.place_forget()

        question_list = questions[question_type]
        current_question = 0

        # Function to check the answer
        def check_answer():
            question, correct_answers = question_list[current_question-1] #the thing starts at 0 so you have to subtract 1
            user_answer = answer_entry.get()
            if user_answer in correct_answers:
                result = "Correct!"
                next_button.configure(state="normal")  # Enable the "Next" button
            else:
                result = "Incorrect. The correct answer is one of: " + ', '.join(correct_answers)
                next_button.configure(state="disabled")  # Disable the "Next" button
            result_label.configure(text=result)

        # Function to load the next question
        def load_question():
            nonlocal current_question
            if current_question < len(question_list) - 1: #-1 to match the questions
                question, _ = question_list[current_question]
                question_label.configure(text=question)
                answer_entry.delete(0, 'end') #deletes all the 
                submit_button.configure(command=check_answer)
                next_button.configure(state="disabled")  # Disable the "Next" button initially
                current_question += 1
            else:
                Quizframe.place_forget()
                Quizmenu()  # Go back to the topic selection menu

        # Create a label to display the question
        question_label = ctk.CTkLabel(Quizframe)
        question_label.place(x=5, y=10)

        # Create an entry to input the answer
        answer_entry = ctk.CTkEntry(Quizframe)
        answer_entry.place(x=5, y=40)
        answer_entry.bind('<Return>', lambda event: check_answer())  # Bind the Enter key to the check answer function

        # Create a label to display the result
        result_label = ctk.CTkLabel(Quizframe, text="")
        result_label.place(x=5, y=70)

        # Create a button to submit the answer
        submit_button = ctk.CTkButton(Quizframe, text="Submit", command=check_answer)
        submit_button.place(x=5, y=100)

        # Create a button to go to the next question
        next_button = ctk.CTkButton(Quizframe, text="Next", command=load_question, state="disabled")  # Disable the next button initially
        next_button.place(x=150, y=100)

        # Load the first question
        load_question()
    #back button
    def back1():
        label_frame.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)
        Quizframe.place_forget()

    lessonbackbutton = ctk.CTkButton(Quizframe, text="Back", command=back1)
    lessonbackbutton.place(x=750, y=500)













def Lessonswindows():
    
    global current_frame, lessonframe, lessontypeframe, Lessoncontentframe, label_frame, Lesson_2contentframe, Lesson_3contentframe, Lesson_4contentframe, Lesson_5contentframe, Lesson_6contentframe, Lesson_7contentframe, Lesson_8contentframe, L1label, L1label2, L1label3, L1label4, L1label5, L1label6, image_label1, image_label2, L2label, L2label1, L2image1, L3label, L3label1, L3label2, L3label3, L3image1, L4label, L4label1, L4label2, L4label3, L4image1, L5label, L5label1, L5label2, L5label3, L5label4, L5image1, L6label, L6label1, L6label2, L6image1, L7label, L7label1, L7label2, L7image1, Lessontitle, option1, option2, option3, option4, option5, option6, option7

    #making a lesson frame
    lessonframe = ctk.CTkFrame(image_frame)
    lessonframe.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)
    #making the left side frame for choosing lessons
    lessontypeframe = ctk.CTkScrollableFrame(lessonframe, corner_radius=10)
    lessontypeframe.place(x=0, y=70, relwidth=0.3, relheight=0.87)
    #making the right side frame for displaying content
    Lessoncontentframe = ctk.CTkFrame(lessonframe, corner_radius=10)
    Lessoncontentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
    #hiding the menu frame
    label_frame.place_forget()
    current_frame = Lessoncontentframe
    def back1(): #back button
        global current_frame
        label_frame.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)
        lessonframe.place_forget()  
        current_frame = label_frame


    lessonbackbutton = ctk.CTkButton(Lessoncontentframe, text="Back", command=back1)
    lessonbackbutton.place(x=315, y=500)

    #second lesson frame
    Lesson_2contentframe = ctk.CTkFrame(lessonframe, corner_radius=10)
    Lesson_3contentframe = ctk.CTkFrame(lessonframe, corner_radius=10)
    Lesson_4contentframe = ctk.CTkFrame(lessonframe, corner_radius=10)
    Lesson_5contentframe = ctk.CTkFrame(lessonframe, corner_radius=10)
    Lesson_6contentframe = ctk.CTkFrame(lessonframe, corner_radius=10)
    Lesson_7contentframe = ctk.CTkFrame(lessonframe, corner_radius=10)
    Lesson_8contentframe = ctk.CTkFrame(lessonframe, corner_radius=10)





    #Lessons

    
    #Lesson 1
    L1label = ctk.CTkLabel(Lessoncontentframe, text="What is a Fraction?", font=('Helvetica', 15, 'bold'))
    L1label2 = ctk.CTkLabel(Lessoncontentframe, text=("A fraction is a part of a whole,\nFor example “one half” is represented as ½" ))
    L1label.place(x=240, y=20)
    L1label2.place(x=170, y=70)

    L1label3 = ctk.CTkLabel(Lessoncontentframe, text="A fraction has a numerator and a denominator")
    L1label3.place(x=170, y=120)

    L1label4 = ctk.CTkLabel(Lessoncontentframe, text="The numerator is the number \n on the top and shows how many \n parts of the whole there are")
    L1label4.place(x=70, y=205)

    L1label5 = ctk.CTkLabel(Lessoncontentframe, text="The denominator is the number \n on the bottom, and shows how many \n equal parts make up the whole")
    L1label5.place(x=370, y=205)

    L1label6 = ctk.CTkLabel(Lessoncontentframe, text="If the number at the top stays the same, the bigger the number at the bottom is, the smaller the fraction")
    L1label6.place(x=10, y=300)

    image_label1 = ctk.CTkLabel(Lessoncontentframe, image=thefirstimage, text="")
    image_label1.place(x=100, y=330)
    image_label2 = ctk.CTkLabel(Lessoncontentframe, image=thesecondimage, text="")
    image_label2.place(x=280, y=180)


    #lesson2
    L2label = ctk.CTkLabel(Lesson_2contentframe, text="Fractions On A Number Line", font=('Helvetica', 15, 'bold'))
    L2label1 = ctk.CTkLabel(Lesson_2contentframe, text="Fractions can be represented on a number line. \n Remember that the larger the denominator, the smaller the fraction is")
    L2image1 = ctk.CTkLabel(Lesson_2contentframe, image=L2image, text="")

    #Lesson3 
    L3label = ctk.CTkLabel(Lesson_3contentframe, text="Adding Fractions with the Same Denominator", font=('Helvetica', 15, 'bold'))
    L3label1 = ctk.CTkLabel(Lesson_3contentframe, text="Just like with normal numbers, fractions can also be added to each other")
    L3label2 = ctk.CTkLabel(Lesson_3contentframe, text="If two fractions have the same denominator, they are like fractions and can be added easily")
    L3label3 = ctk.CTkLabel(Lesson_3contentframe, text="These two fractions can be added by adding the numbers at the top \n of the fraction (the numerator), while keeping the denominator the same")
    L3image1 = ctk.CTkLabel(Lesson_3contentframe, image=L3image, text="")

    #Lesson4
    L4label = ctk.CTkLabel(Lesson_4contentframe, text="Adding Fractions with a Different Denominator", font=('Helvetica', 15, 'bold'))
    L4label1 = ctk.CTkLabel(Lesson_4contentframe, text="When fractions have different denominators, an extra step is needed to add them")
    L4label2 = ctk.CTkLabel(Lesson_4contentframe, text="The LCM (Lowest common multiple) of the denominators needs to be found first")
    L4label3 = ctk.CTkLabel(Lesson_4contentframe, text="Then add the numerators of these fractions together")
    L4image1 = ctk.CTkLabel(Lesson_4contentframe, image=L4image, text="")

    #Lesson5
    L5label = ctk.CTkLabel(Lesson_5contentframe, text="Mixed Numerals and Improper Fractions", font=('Helvetica', 15, 'bold'))
    L5label1 = ctk.CTkLabel(Lesson_5contentframe, text="Fractions can also be represented as mixed numerals and improper fractions \n when the numerator is greater than the denominator")
    L5label2 = ctk.CTkLabel(Lesson_5contentframe, text="A mixed numeral has a whole number and a proper fraction")
    L5label3 = ctk.CTkLabel(Lesson_5contentframe, text="An improper fraction has a numerator that is larger than the denominator e.g. 3 ½ = 7/2")
    L5label4 = ctk.CTkLabel(Lesson_5contentframe, text="To convert an improper fraction to a mixed numeral, divide the numerator by the denominator, \n and the amount of times the denominator goes into the numerator becomes the whole number,\n and the remainder becomes the new numerator")
    L5image1 = ctk.CTkLabel(Lesson_5contentframe, image=L5image, text="")

    #Lesson6
    L6label = ctk.CTkLabel(Lesson_6contentframe, text="Multiplying fractions", font=('Helvetica', 15, 'bold'))
    L6label1 = ctk.CTkLabel(Lesson_6contentframe, text="Fractions can be multiplied with each other similar to normal numbers")
    L6label2 = ctk.CTkLabel(Lesson_6contentframe, text="To multiply 2 fractions together, multiply the numerators of both fractions to get the new numerator \n then multiply the two denominators to get the new denominator")
    L6image1 = ctk.CTkLabel(Lesson_6contentframe, image=L6image, text="")

    #Lesson7
    L7label = ctk.CTkLabel(Lesson_7contentframe, text="Dividing Fractions", font=('Helvetica', 15, 'bold'))
    L7label1 = ctk.CTkLabel(Lesson_7contentframe, text="For fractions, division works similarly to multiplication")
    L7label2 = ctk.CTkLabel(Lesson_7contentframe, text="To divide 2 fractions, flip the second fraction and change \n the division symbol to a multiplication symbol and then multiply the two numbers")
    L7image1 = ctk.CTkLabel(Lesson_7contentframe, image=L7image, text="")

    #lesson changing commands
    

    #lessontts

    

    def speak1():
        def tts():
            engine = pyttsx3.init()
            engine.stop()
            phrases = [
                "What is a Fraction?",
                "A fraction is a part of a whole, For example one half is represented as one over two",
                "A fraction has 2 parts, a numerator and a denominator, where the numerator is on the top and the denominator is on the bottom",
                "A bigger denominator means a smaller fraction, so one seventh is smaller than one half"
            ]
            for phrase in phrases:
                engine.say(phrase)
                engine.runAndWait()
    
    # Run the tts function in a separate thread
        threading.Thread(target=tts).start()
    speakbutton = ctk.CTkButton(Lessoncontentframe, width=20, height=20, text="🗣️", command=speak1)
    speakbutton.place(x=550, y=10)

    
    def speak2():
        def tts():
            engine = pyttsx3.init()
            engine.stop()
            phrases = [
                "Fractions On A Number Line.",
                "Fractions can be represented on a number line.",
                "Remember that the larger the denominator, the smaller the fraction is."
            ]
            for phrase in phrases:
                engine.say(phrase)
                engine.runAndWait()

    # Run the tts function in a separate thread
        threading.Thread(target=tts).start()
    speakbutton2 = ctk.CTkButton(Lesson_2contentframe, width=20, height=20, text="🗣️", command=speak2)

    def speak3():
        def tts():
            engine = pyttsx3.init()
            engine.stop()
            phrases = [
                "Adding Fractions with the Same Denominator.",
                "Just like with normal numbers, fractions can also be added to each other.",
                "If two fractions have the same denominator, they are like fractions and can be added easily.",
                "These two fractions can be added by adding the numbers at the top of the fraction (the numerator), while keeping the denominator the same"
            ]
            for phrase in phrases:
                engine.say(phrase)
                engine.runAndWait()

        # Run the tts function in a separate thread
        threading.Thread(target=tts).start()
    speakbutton3 = ctk.CTkButton(Lesson_3contentframe, width=10, height=20, text="🗣️", command=speak3)

    def speak4():
            engine = pyttsx3.init()
            engine.stop()
            engine.say("Adding Fractions with a Different Denominator.")
            engine.runAndWait()
            engine.say("When fractions have different denominators, an extra step is needed to add them.")
            engine.runAndWait()
            engine.say("The LCM (Lowest common multiple) of the denominators needs to be found first.")
            engine.runAndWait()
            engine.say("Then add the numerators of these fractions together to get the result.")
            engine.runAndWait()
    speakbutton4 = ctk.CTkButton(Lesson_4contentframe, width=10, height=20, text="🗣️", command=speak4)


    def speak5():
            engine = pyttsx3.init()
            engine.stop()
            engine.say("Mixed Numerals and Improper Fractions")
            engine.runAndWait()
            engine.say("Fractions can also be represented as mixed numerals and improper fractions when the numerator is greater than the denominator")
            engine.runAndWait()
            engine.say("A mixed numeral has a whole number and a proper fraction")
            engine.runAndWait()
            engine.say("An improper fraction has a numerator that is larger than the denominator for exampel 3 and a half = 7 over 2")
            engine.runAndWait()
            engine.say("To convert an improper fraction to a mixed numeral, divide the numerator by the denominator, and the amount of times the denominator goes into the numerator becomes the whole number, and the remainder becomes the new numerator")
            engine.runAndWait()
    speakbutton5 = ctk.CTkButton(Lesson_5contentframe, width=10, height=20, text="🗣️", command=speak5)

    def speak6():
            engine = pyttsx3.init()
            engine.stop()
            engine.say("Multiplying fractions")
            engine.runAndWait()
            engine.say("Fractions can be multiplied with each other similar to normal numbers.")
            engine.runAndWait()
            engine.say("To multiply 2 fractions together, multiply the numerators of both fractions to get the new numerator then multiply the two denominators to get the new denominator")
            engine.runAndWait()
    speakbutton6 = ctk.CTkButton(Lesson_6contentframe, width=10, height=20, text="🗣️", command=speak6)

    def speak7():
            engine = pyttsx3.init()
            engine.stop()
            engine.say("Dividing Fractions")
            engine.runAndWait()
            engine.say("For fractions, division works similarly to multiplication")
            engine.runAndWait()
            engine.say("To divide 2 fractions, flip the second fraction and change the division symbol to a multiplication symbol and then multiply the two numbers")
            engine.runAndWait()
    speakbutton7 = ctk.CTkButton(Lesson_2contentframe, width=10, height=20, text="🗣️", command=speak7)

    


    def coption1():
        global current_frame
        current_frame.place_forget()
        Lessoncontentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        current_frame = Lessoncontentframe

    def coption2():
        global current_frame
        current_frame.place_forget()
        Lesson_2contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        L2label.place(x=200, y=20)
        L2label1.place(x=100, y=100)
        L2image1.place(x=130, y=140)
        speakbutton2.place(x=550, y=10)
        current_frame = Lesson_2contentframe

    def coption3():
        global current_frame
        current_frame.place_forget()
        Lesson_3contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        L3label.place(x=160, y=20)
        L3label1.place(x=80, y=100)
        L3label2.place(x=60, y=150)
        L3label3.place(x=80, y=200)
        L3image1.place(x=80, y=250)
        speakbutton3.place(x=550, y=10)
        current_frame = Lesson_3contentframe

    def coption4():
        global current_frame
        current_frame.place_forget()
        Lesson_4contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        L4label.place(x=160, y=20)
        L4label1.place(x=80, y=100)
        L4label2.place(x=60, y=150)
        L4label3.place(x=150, y=200)
        L4image1.place(x=80, y=250)
        speakbutton4.place(x=550, y=10)
        current_frame = Lesson_4contentframe

    def coption5():
        global current_frame
        current_frame.place_forget()
        Lesson_5contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        L5label.place(x=180, y=20)
        L5label1.place(x=80, y=100)
        L5label2.place(x=150, y=150)
        L5label3.place(x=80, y=170)
        L5label4.place(x=50, y=210)
        L5image1.place(x=80, y=280)
        speakbutton5.place(x=550, y=10)
        current_frame = Lesson_5contentframe
    
    def coption6():
        global current_frame
        current_frame.place_forget()
        Lesson_6contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        L6label.place(x=250, y=20)
        L6label1.place(x=80, y=100)
        L6label2.place(x=30, y=150)
        L6image1.place(x=80, y=220)
        speakbutton6.place(x=550, y=10)
        current_frame = Lesson_6contentframe

    def coption7():
        global current_frame
        current_frame.place_forget()
        Lesson_7contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        L7label.place(x=250, y=20)
        L7label1.place(x=130, y=80)
        L7label2.place(x=80, y=130)
        L7image1.place(x=80, y=180)
        speakbutton7.place(x=550, y=10)
        current_frame = Lesson_7contentframe


    

    #next buttons
    lessonnext1button = ctk.CTkButton(Lessoncontentframe, text="Next", command=coption2)
    lessonnext1button.place(x=465, y=500)

    lessonnext2button = ctk.CTkButton(Lesson_2contentframe, text="Next", command=coption3)
    lessonnext2button.place(x=465, y=500)

    lessonnext3button = ctk.CTkButton(Lesson_3contentframe, text="Next", command=coption4)
    lessonnext3button.place(x=465, y=500)

    lessonnext4button = ctk.CTkButton(Lesson_4contentframe, text="Next", command=coption5)
    lessonnext4button.place(x=465, y=500)

    lessonnext5button = ctk.CTkButton(Lesson_5contentframe, text="Next", command=coption6)
    lessonnext5button.place(x=465, y=500)

    lessonnext6button = ctk.CTkButton(Lesson_6contentframe, text="Next", command=coption7)
    lessonnext6button.place(x=465, y=500)

    lessonnext7button = ctk.CTkButton(Lesson_7contentframe, text="Next", command=coption1)
    lessonnext7button.place(x=465, y=500)





    
    #back buttons
    lessonback2button = ctk.CTkButton(Lesson_2contentframe, text="Back", command=coption1)
    lessonback2button.place(x=315, y=500)

    lessonback3button = ctk.CTkButton(Lesson_3contentframe, text="Back", command=coption2)
    lessonback3button.place(x=315, y=500)

    lessonback4button = ctk.CTkButton(Lesson_4contentframe, text="Back", command=coption3)
    lessonback4button.place(x=315, y=500)

    lessonback5button = ctk.CTkButton(Lesson_5contentframe, text="Back", command=coption4)
    lessonback5button.place(x=315, y=500)

    lessonback6button = ctk.CTkButton(Lesson_6contentframe, text="Back", command=coption5)
    lessonback6button.place(x=315, y=500)

    lessonback7button = ctk.CTkButton(Lesson_7contentframe, text="Back", command=coption6)
    lessonback7button.place(x=315, y=500)


    #Title Label 
    Lessontitle = ctk.CTkLabel(master=lessonframe, text="Lessons", height=70, width=235,font=('Helvetica', 18, 'bold'))
    Lessontitle.place(x=20,y=0)
    #scrollable frame buttons
    option1 = ctk.CTkButton(master=lessontypeframe, text="What Is A Fraction?", height=70, width=235, command=coption1)
    option1.pack(pady=7)
    option2 = ctk.CTkButton(master=lessontypeframe, text="Fractions On A Number Line", height=70, width=235, command=coption2)
    option2.pack(pady=7)
    option3 = ctk.CTkButton(master=lessontypeframe, text="Adding Fractions", height=70, width=235, command=coption3)
    option3.pack(pady=7)
    option4 = ctk.CTkButton(master=lessontypeframe, text="Adding Fractions Extended", height=70, width=235, command=coption4)
    option4.pack(pady=7)
    option5 = ctk.CTkButton(master=lessontypeframe, text="Mixed Numerals", height=70, width=235, command=coption5)
    option5.pack(pady=7)
    option6 = ctk.CTkButton(master=lessontypeframe, text="Multiplying Fractions", height=70, width=235, command=coption6)
    option6.pack(pady=7)
    option7 = ctk.CTkButton(master=lessontypeframe, text="Dividing Fractions", height=70, width=235, command=coption7)
    option7.pack(pady=7)
# have if statements for when the program is at max or min scaling for lesson content

#Settings

def Settingsmenu():
    global optionmenu_1
    label_frame.place_forget()
    Settingsframe = ctk.CTkFrame(image_frame)
    Settingsframe.place(x=250, y=30, relwidth=0.5, relheight=0.9)

    def backsettings():
        Settingsframe.place_forget()
        label_frame.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)

    settingsbackbutton = ctk.CTkButton(Settingsframe, text="Back", command=backsettings)
    settingsbackbutton.place(x=340, y=490)

    def Appearance(selection):
        choice_index = themes.index(optionmenu_2.get())
        if choice_index == 0 :
            ctk.set_appearance_mode("light")
        elif choice_index == 1:
            ctk.set_appearance_mode("dark")
        elif choice_index == 2:
            ctk.set_appearance_mode("system")



    
        
        
    #themes
    themes = ["Light", "Dark", "System"]
    optionmenu_2 = ctk.CTkOptionMenu(Settingsframe, values=themes, command=Appearance)
    optionmenu_2.place(x=150, y=170)
    optionmenu_2.set("System")

    OptionLabel2 = ctk.CTkLabel(Settingsframe, text= "Appearance Mode")
    OptionLabel2.place(x=150, y=130)   
    Settingstitlelabel = ctk.CTkLabel(Settingsframe, text="settings")
    Settingstitlelabel.place(x=250,y=30)

    current_theme = ctk.get_appearance_mode()
    #change geometry and scaling
    def change_scaling_event(selection):
        scale = int(selection.strip('%')) / 100
        ctk.set_widget_scaling(scale)
        if selection == "125%":
            root.geometry("1250x750")
        elif selection == "100%":
            root.geometry("1000x600")
        elif selection == "140%":
            root.geometry("1400x840")
        elif selection == "75%":
            root.geometry("750x450")
        elif selection == "50%":
            root.geometry("500x300")

    optionmenu_1 = ctk.CTkOptionMenu(Settingsframe, values=["50%", "75%", "100%", "125%", "140%"], command=change_scaling_event)
    optionmenu_1.place(x=150, y=250)
    OptionLabel = ctk.CTkLabel(Settingsframe, text= "UI Scaling")
    OptionLabel.place(x=150, y=220)
    optionmenu_1.set("Select Size")
    


# Creating lessons and settings button
mybutton = ctk.CTkButton(label_frame, width=450, height=64, border_width=0,corner_radius=8,text="Lessons", command=Lessonswindows)
mybutton.place(x=240, y=225) 

SettingsButton = ctk.CTkButton(label_frame, width=220, height=64, border_width=0,corner_radius=8,text="Settings", command=Settingsmenu)
SettingsButton.place(x=240, y=300) 

Quiz_Button = ctk.CTkButton(label_frame, width=220, height=64, border_width=0,corner_radius=8,text="Quizzes", command=Quizmenu)
Quiz_Button.place(x=470, y=300)

root.mainloop()