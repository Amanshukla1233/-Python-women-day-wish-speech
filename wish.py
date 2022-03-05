from tkinter import *
import pyttsx3


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')# geting details of current voice

engine.setProperty('voice',voices[0].id)
volume=engine.getProperty('volume')
engine.setProperty('volume',volume-0.25)



def speak (audio):
    engine.say(audio)
    engine.runAndWait()# without this command , speech will not be audible to us

if __name__=="__main__":
    speak("Happy women's day ")

def hello():

    engine = pyttsx3.init('sapi5')
    sound = engine.getProperty('voices')  # geting details of current voice
    engine.setProperty('voice', sound[0].id)

    rate = engine.getProperty('rate')# control speed
    engine.setProperty('rate',110)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()  # without this command , speech will not be audible to us

    if __name__ == "__main__":
        speak(''' happy womean's day The international occasion of Women’s Day is the best day to acknowledge the hard efforts and contributions of women in society.
         The courage and strength which they have shown on the personal as well as professional front makes them true she-roes in every way.
          Be it your mother, sister, grandmother, wife, female colleagues, teachers, or anyone else, they are definitely the biggest source of inspirations for you in some way or the other.
           Make these beautiful ladies feel elated with your love and affection through your hearty messages for Women’s Day in 2022. ''')

def hello1():

    engine = pyttsx3.init('sapi5')
    sound = engine.getProperty('voices')  # geting details of current voice
    engine.setProperty('voice', sound[0].id)

    rate = engine.getProperty('rate')# control speed
    engine.setProperty('rate',110)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()  # without this command , speech will not be audible to us

    if __name__ == "__main__":
        speak(''' As I stand before you all on an occasion so special and worthy of celebrations,
         I feel immense happiness that we, as a whole, are making progress and women are getting the kind of respect they deserve.

More than a decade from today, International women’s day wasn’t celebrated this much and on such big scales.
 But slowly and steadily, people are understanding the importance of observing and celebrating Women’s Day. 
 Socialist Party of America organised the first Women’s Day on February 28, 1909, in New York City.
  With more points in the coming year, it changed to 8th of March.''')



def hello2():

    engine = pyttsx3.init('sapi5')
    sound = engine.getProperty('voices')  # geting details of current voice
    engine.setProperty('voice', sound[0].id)

    rate = engine.getProperty('rate')# control speed
    engine.setProperty('rate',110)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()  # without this command , speech will not be audible to us

    if __name__ == "__main__":
        speak('''The world celebrated and recognise the social, political, economical and cultural 
        achievement on women on this day. This is celebrated the struggle of generations to recognise this day.  ''')




from PIL import Image, ImageTk


aman_root=Tk()

"""def page2():
    label=tk.Label(frame,text="This is second page")
    label.place(relx=0.3,rely=0.4)"""


aman_root.title(" Aman Shukla")
aman_root.geometry("1000x700")
aman_root.config(bg="blue")

frame=Frame(aman_root,bg="grey",width=7,height=5)
frame.pack(side=BOTTOM)

b1=Button(frame,fg="red",bg="yellow",text="SPEECH ", command=hello)
b1.pack(side=LEFT,padx=5,pady=2)



b3=Button(frame,fg="black",bg="yellow",text="IMPORTANT WOMEN'S DAY ", command=hello2)
b3.pack(side=LEFT,padx=5,pady=2)

b3.pack(side=LEFT,padx=5,pady=2)
#bt1=tk.Button(aman_root,text="page 2",command=page2)
#bt1.grid(column=1,row=0)
b2=Button(frame, fg="black",bg="green",text="SPEECH 1 ", command=hello1)
b2.pack(side=RIGHT,padx=0,pady=2)

# for jpg
image=Image.open("Happyw.jpg")
photo= ImageTk.PhotoImage(image)
varun_label=Label(image=photo)
varun_label.pack()


aman_root.mainloop()