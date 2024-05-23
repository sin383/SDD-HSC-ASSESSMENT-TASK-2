from tkinter import *
import customtkinter as ctk
from PIL import Image
import PIL
from os import path
import os

root = ctk.CTk()
root.geometry("1000x600")
root.title("Miss Chilla Gaming")
root.resizable(width=True, height=True)

# Creating a separate frame for the image
image_frame = ctk.CTkFrame(root, corner_radius=0)
image_frame.place(x=0, y=0, relwidth=1, relheight=1)  # Place the image frame at the back


my_image=ctk.CTkImage(light_image=Image.open("C:/Users/ojaye/Downloads/77.png"), dark_image=Image.open("C:/Users/ojaye/Downloads/77.png"), size=(1000,1000))
mylabel = ctk.CTkLabel(image_frame, text="", image=my_image)  #image
mylabel.place(x=0, y=0, relwidth=1, relheight=1)

#Creating a frame for labels with rounded edges
label_frame = ctk.CTkFrame(image_frame, corner_radius=100, fg_color="transparent", bg_color="transparent")  # Set corner_radius to give the frame rounded edges
label_frame.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)  #relative width and height from the edges so it leaves a small gap at the back

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
    
    lessonframe = ctk.CTkFrame(image_frame)
    lessonframe.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)
    lessontypeframe = ctk.CTkScrollableFrame(lessonframe, corner_radius=10)
    lessontypeframe.place(x=0, y=0)
    Lessoncontentframe = ctk.CTkFrame(lessonframe, corner_radius=10)
    Lessoncontentframe.place(x=280, y=0, relwidth=0.7, relheight=1)
    label_frame.place_forget()
    def back1():
        label_frame.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)
        lessonframe.place_forget()

    lessonbackbutton = ctk.CTkButton(lessonframe, text="Back", command=back1)
    lessonbackbutton.place(x=750, y=500)
    tempbutton = ctk.CTkButton(Lessoncontentframe, text="Lol")
    tempbutton.place(x=350, y=10)
    tempbutton2 = ctk.CTkButton(lessontypeframe, text="7")
    tempbutton2.place(x=50, y=50)   
    def next1():
        label_frame.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)
        lessonframe.place_forget()
    lessonnext1button = ctk.CTkButton(lessonframe, text="Next", command=next1)
    lessonnext1button.place(x=600, y=500)

    #scrollable frame buttons
    option1 = ctk.CTkButton(master=lessontypeframe, text="7")
    option1.place(x=15, y=0)
    option2 = ctk.CTkButton(master=lessontypeframe, text="7")
    option2.place(x=15, y=50)
    option3 = ctk.CTkButton(master=lessontypeframe, text="7")
    option3.place(x=15, y=150)
    option4 = ctk.CTkButton(master=lessontypeframe, text="7")
    option4.place(x=15, y=250)
    option5 = ctk.CTkButton(lessontypeframe, text="7")
    option5.place(x=15, y=450)
    option6 = ctk.CTkButton(master=lessontypeframe, text="7")
    option6.place(x=15, y=650)
    option7 = ctk.CTkButton(master=lessontypeframe, text="7")
    option7.place(x=15, y=350)
    option8 = ctk.CTkButton(master=lessontypeframe, text="7")
    option8.place(x=5, y=50)





def Settingsmenu():
    global optionmenu_1
    label_frame.place_forget()
    Settingsframe = ctk.CTkFrame(image_frame)
    Settingsframe.place(x=250, y=30, relwidth=0.5, relheight=0.9)

    def backsettings():
        Settingsframe.place_forget()
        label_frame.place(relx=0.04, rely=0.04, relwidth=0.9, relheight=0.9)

    settingsbackbutton = ctk.CTkButton(Settingsframe, text="Back", command=backsettings)
    settingsbackbutton.place(x=340, y=500)

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
        elif selection == "150%":
            root.geometry("1400x800")
        elif selection == "75%":
            root.geometry("800x500")
        elif selection == "50%":
            root.geometry("500x350")

    optionmenu_1 = ctk.CTkOptionMenu(Settingsframe, values=["50%", "75%", "100%", "125%", "150%"], command=change_scaling_event)
    optionmenu_1.place(x=150, y=250)
    OptionLabel = ctk.CTkLabel(Settingsframe, text= "UI Scaling")
    OptionLabel.place(x=150, y=220)
    

# Creating lessons and settings button
mybutton = ctk.CTkButton(label_frame, width=450, height=64, border_width=0,corner_radius=8,text="Lessons", command=Lessonswindows)
mybutton.place(x=240, y=225) 

SettingsButton = ctk.CTkButton(label_frame, width=220, height=64, border_width=0,corner_radius=8,text="Settings", command=Settingsmenu)
SettingsButton.place(x=240, y=300) 

Quiz_Button = ctk.CTkButton(label_frame, width=220, height=64, border_width=0,corner_radius=8,text="Quizzes", command=Quizmenu)
Quiz_Button.place(x=470, y=300)

root.mainloop()