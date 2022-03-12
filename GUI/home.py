from tkinter import *

def exersises():
    app.destroy()
    import Exersises

def achievements():
    app.destroy()
    import achievements

def userInfo():
    app.destroy()
    import userInfo

def history():
    app.destroy()
    import history

app=Tk()



app.title('Home Page ')
app.geometry('1120x920')
app.configure(bg='#09c')

HomePage2=Label(app,text='Home Page',font=('bold',35),bg="#09c").place(relx=.5, rely=.2,anchor= CENTER)

Exersises=Button(app,text="Exersises",pady=20,padx=20,width=12,borderwidth = 10,command=exersises).place(relx=.5,rely=.3,anchor=CENTER)
Achievements=Button(app,text="Achievements",pady=20,padx=20,width=12,borderwidth = 10,command=achievements).place(relx=.5,rely=.4,anchor=CENTER)
userInfo=Button(app,text="User Info",pady=20,padx=20,width=12,borderwidth = 10,command=userInfo).place(relx=.5,rely=.5,anchor=CENTER)
History=Button(app,text="History",pady=20,padx=20,width=12,borderwidth = 10,command=history).place(relx=.5,rely=.6,anchor=CENTER)

app.mainloop()