from tkinter import *
def Home():
    achievements.focus(False)
    import home


achievements=Tk()



achievements.title('Home Page ')
achievements.geometry('1120x920')
achievements.configure(bg='#09c')

HomePage2=Label(achievements,text='achievements Page',font=('bold',35),bg="#09c").place(relx=.5, rely=.2,anchor= CENTER)
Home=Button(achievements,text="Back home",pady=20,padx=20,width=12,borderwidth = 10,command=Home).place(relx=.5,rely=.3,anchor=CENTER)
