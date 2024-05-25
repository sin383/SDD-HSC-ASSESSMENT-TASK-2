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
    image_label1.place(x=100, y=340)
    image_label2 = ctk.CTkLabel(Lessoncontentframe, image=thesecondimage, text="")
    image_label2.place(x=280, y=180)


    #lesson2
    L2label = ctk.CTkLabel(Lesson_2contentframe, text="Fractions On A Number Line", font=('Helvetica', 15, 'bold'))
    L2label1 = ctk.CTkLabel(Lesson_2contentframe, text="Fractions can be represented on a number line. \n Remember that the larger the denominator, the smaller the fraction is")

    #Lesson3 
    L3label = ctk.CTkLabel(Lesson_3contentframe, text="Fractions On A Number Line", font=('Helvetica', 15, 'bold'))
    L3label1 = ctk.CTkLabel(Lesson_3contentframe, text="Just like with normal numbers, fractions can also be added to each other")
    L3label2 = ctk.CTkLabel(Lesson_3contentframe, text="If two fractions have the same denominator, they are like fractions and can be added easily")
    L3label3 = ctk.CTkLabel(Lesson_3contentframe, text="These two fractions can be added by adding the numbers at the top \n of the fraction (the numerator), while keeping the denominator the same")

    #Lesson4

    #lesson changing commands

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
        current_frame = Lesson_2contentframe

    def coption3():
        global current_frame
        current_frame.place_forget()
        Lesson_3contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        L3label.place(x=200, y=20)
        L3label1.place(x=80, y=100)
        L3label2.place(x=60, y=150)
        L3label3.place(x=80, y=200)
        current_frame = Lesson_3contentframe

    def coption4():
        global current_frame
        current_frame.place_forget()
        Lesson_4contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        current_frame = Lesson_4contentframe

    def coption5():
        global current_frame
        current_frame.place_forget()
        Lesson_5contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        current_frame = Lesson_5contentframe
    
    def coption6():
        global current_frame
        current_frame.place_forget()
        Lesson_6contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        current_frame = Lesson_6contentframe

    def coption7():
        global current_frame
        current_frame.place_forget()
        Lesson_7contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        current_frame = Lesson_7contentframe

    def coption8():
        global current_frame
        current_frame.place_forget()
        Lesson_8contentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
        current_frame = Lesson_8contentframe
    


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

    lessonnext7button = ctk.CTkButton(Lesson_7contentframe, text="Next", command=coption8)
    lessonnext7button.place(x=465, y=500)

    lessonnext8button = ctk.CTkButton(Lesson_8contentframe, text="Next", command=coption1)
    lessonnext8button.place(x=465, y=500)

    
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

    lessonback8button = ctk.CTkButton(Lesson_8contentframe, text="Back", command=coption7)
    lessonback8button.place(x=315, y=500)

    #Title Label 
    Lessontitle = ctk.CTkLabel(master=lessonframe, text="Lessons", height=70, width=235,font=('Helvetica', 18, 'bold'))
    Lessontitle.place(x=20,y=0)
    #scrollable frame buttons
    option1 = ctk.CTkButton(master=lessontypeframe, text="What Is A Fraction?", height=70, width=235, command=coption1, fg_color="red", hover_color="crimson")
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
    option8 = ctk.CTkButton(master=lessontypeframe, text="Word Problems", height=70, width=235, command=coption8)
    option8.pack(pady=7)
# have if statements for when the program is at max or min scaling for lesson content



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