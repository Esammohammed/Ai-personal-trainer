from tkinter import *

def Home():
    history.destroy()
    import home

history=Tk()



history.title('Home Page ')
history.geometry('1120x920')
history.configure(bg='#09c')

HomePage2=Label(history,text='history Page',font=('bold',35),bg="#09c").place(relx=.5, rely=.2,anchor= CENTER)

Home=Button(history,text="Back home",pady=20,padx=20,width=12,borderwidth = 10,command=Home).place(relx=.5,rely=.3,anchor=CENTER)
