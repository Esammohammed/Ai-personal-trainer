from tkinter import *
def Home():
    Exersises.withdraw()
    import home


Exersises=Tk()



Exersises.title('Home Page ')
Exersises.geometry('1120x920')
Exersises.configure(bg='#09c')

HomePage2=Label(Exersises,text='Exersises Page',font=('bold',35),bg="#09c").place(relx=.5, rely=.2,anchor= CENTER)

Home=Button(Exersises,text="Back home",pady=20,padx=20,width=12,borderwidth = 10,command=Home).place(relx=.5,rely=.3,anchor=CENTER)
