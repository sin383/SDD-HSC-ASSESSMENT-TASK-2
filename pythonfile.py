from tkinter import *
import customtkinter as ctk
from PIL import *
import PIL
from os import path
import os

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

yespath = path.join(DIR_NAME, "assets", "77.png")
yes = Image.open(yespath)
yesimage=ctk.CTkImage(yes, size=(1800,1600))

# Create CTkImage objects
thefirstimage = ctk.CTkImage(L1image2, size=(400,150))
thesecondimage = ctk.CTkImage(L1image1, size=(50,70))

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






def Quizmenu():
    global Quizframe
    label_frame.place_forget()
    Quizframe = ctk.CTkFrame(image_frame)
    Quizframe.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)
    Quizexample = ctk.CTkEntry(Quizframe)
    Quizexample.place(x=5, y=10)
    def back1():
        label_frame.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)
        Quizframe.place_forget()

    lessonbackbutton = ctk.CTkButton(Quizframe, text="Back", command=back1)
    lessonbackbutton.place(x=750, y=500)

def Lessonswindows():
    global current_frame
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

    def next1():
        global current_frame
        Lesson_2contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        Lessoncontentframe.place_forget()
        current_frame = Lesson_2contentframe

    lessonnext1button = ctk.CTkButton(Lessoncontentframe, text="Next", command=next1)
    lessonnext1button.place(x=465, y=500)

    #Lessons

    
    #Lesson 1
    L1label = ctk.CTkLabel(Lessoncontentframe, text="What is a Fraction?")
    L1label2 = ctk.CTkLabel(Lessoncontentframe, text=("A fraction is a part of a whole,\nFor example “one half” is represented as ½" ))
    L1label.place(x=200, y=20)
    L1label2.place(x=150, y=90)
    image_label1 = ctk.CTkLabel(Lessoncontentframe, image=thefirstimage, text="")
    image_label1.place(x=100, y=300)
    image_label2 = ctk.CTkLabel(Lessoncontentframe, image=thesecondimage, text="")
    image_label2.place(x=300, y=200)






    #lesson changing commands

    def coption1():
        global current_frame
        current_frame.place_forget()
        Lessoncontentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        current_frame = Lessoncontentframe


    #Title Label 
    Lessontitle = ctk.CTkLabel(master=lessonframe, text="Lessons", height=70, width=235,font=('Helvetica', 18, 'bold'))
    Lessontitle.place(x=20,y=0)
    #scrollable frame buttons
    option1 = ctk.CTkButton(master=lessontypeframe, text="What Is A Fraction?", height=70, width=235, command=coption1)
    option1.pack(pady=7)
    option2 = ctk.CTkButton(master=lessontypeframe, text="Fractions On A Number Line", height=70, width=235)
    option2.pack(pady=7)
    option3 = ctk.CTkButton(master=lessontypeframe, text="Adding Fractions", height=70, width=235)
    option3.pack(pady=7)
    option4 = ctk.CTkButton(master=lessontypeframe, text="Adding Fractions Extended", height=70, width=235)
    option4.pack(pady=7)
    option5 = ctk.CTkButton(master=lessontypeframe, text="Mixed Numerals", height=70, width=235)
    option5.pack(pady=7)
    option6 = ctk.CTkButton(master=lessontypeframe, text="Multiplying Fractions", height=70, width=235)
    option6.pack(pady=7)
    option7 = ctk.CTkButton(master=lessontypeframe, text="Dividing Fractions", height=70, width=235)
    option7.pack(pady=7)
    option8 = ctk.CTkButton(master=lessontypeframe, text="Word Problems", height=70, width=235)
    option8.pack(pady=7)




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


    themes = ["Light", "Dark", "System"]
    optionmenu_2 = ctk.CTkOptionMenu(Settingsframe, values=themes, command=Appearance)
    optionmenu_2.place(x=150, y=170)
    optionmenu_2.set("System")

    OptionLabel2 = ctk.CTkLabel(Settingsframe, text= "Appearance Mode")
    OptionLabel2.place(x=150, y=130)   
    Settingstitlelabel = ctk.CTkLabel

    current_theme = ctk.get_appearance_mode()

    def change_scaling_event(selection):
        scale = int(selection.strip('%')) / 100
        ctk.set_widget_scaling(scale)
        if selection == "125%":
            root.geometry("1300x750")
        elif selection == "100%":
            root.geometry("1000x600")
        elif selection == "140%":
            root.geometry("1450x850")
        elif selection == "75%":
            root.geometry("800x500")
        elif selection == "50%":
            root.geometry("500x350")

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