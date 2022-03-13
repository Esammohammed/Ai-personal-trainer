from tkinter import *
from PIL import ImageTk, Image


def show_frame(frame):
    frame.tkraise()


app=Tk()
app.title('Home Page')
app.geometry('1120x920')
app.configure(bg='#C0C0C0')


exercises = Frame(app, width=1050, height=750, bg='#FFFFFF', padx=5, pady=5, border=5)
history = Frame(app, width=1050, height=750, bg='#FFFFFF', padx=5, pady=5, border=5)
userInfo = Frame(app, width=1050, height=750, bg='#FFFFFF', padx=5, pady=5, border=5)
achievements = Frame(app, width=1050, height=750, bg='#FFFFFF', padx=5, pady=5, border=5)

for frame in (exercises, achievements,history,userInfo):
    frame.place(relx=0.2, rely=0.03,width=1050, height=750)


frame1_title=Label(exercises, text='Exercises Page', font='times 35')
frame1_title.pack(fill='both')
frame1_title=Label(achievements, text='Achievements Page', font='times 35')
frame1_title.pack(fill='both')
frame1_title=Label(history, text='History Page', font='times 35')
frame1_title.pack(fill='both')
frame1_title=Label(userInfo, text='UserInfo Page', font='times 35')
frame1_title.pack(fill='both')
class Example(Frame):
    def __init__(self, master, *pargs):
        Frame.__init__(self, master, *pargs)



        self.image = Image.open("bkGround.jpg")
        self.img_copy= self.image.copy()


        self.background_image = ImageTk.PhotoImage(self.image)

        self.background = Label(self, image=self.background_image)
        self.background.pack(fill=BOTH, expand=YES)
        self.background.bind('<Configure>', self._resize_image)

    def _resize_image(self,event):

        new_width = event.width
        new_height = event.height

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image =  self.background_image)

e = Example(app)
e.pack(fill=BOTH, expand=TRUE)





frame = Frame(app,width=300,height=920,bg='#708090')
frame.place(x=0,y=0)

def btn(x,y,text,bcolor,fcolor,cmd):
    def on_entera(e):
        button1['background'] = bcolor #ffcc66
        button1['foreground'] = '#FFFFFF'  #000d33

    def on_leavea(e):
        button1['background'] = fcolor
        button1['foreground'] = '#FFFFFF'
    button1 = Button(frame,text=text,width=42,
                     height=2,fg='#FFFFFF',border=0,
                     bg=fcolor,activeforeground='#262626',activebackground=bcolor,command=cmd
                )
    button1.bind("<Enter>", on_entera)
    button1.bind("<Leave>", on_leavea)
    button1.place(x=x,y=y)

btn(0,80,'Exercises','#0f9d9a','#708090',lambda:show_frame(exercises))
btn(0,117,'Show User Info','#0f9d9a','#708090',lambda:show_frame(userInfo))
btn(0,154,'History','#0f9d9a','#708090',lambda:show_frame(history))
btn(0,191,'Achievements','#0f9d9a','#708090',lambda:show_frame(achievements))
btn(0,228,'Exit','#0f9d9a','#708090',app.destroy)

#button1 = Button(frame,text="Exit",width=42,height=2,border=0,bg='#0f9d9a',app.destroy)


#button1.place(x=0,y=230)


app.attributes('-fullscreen', True)
app.mainloop()
