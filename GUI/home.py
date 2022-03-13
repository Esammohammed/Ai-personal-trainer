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

frame1 = Frame(app,width=1000,height=700,highlightbackground='red',highlightthickness=3)
frame1.grid(row=0,column=0,padx=20,pady=20,ipadx=20,ipady=20)

HomePage2=Label(frame1,text='Home Page',font=('bold',35),bg="#09c").place(relx=.5, rely=.2,anchor= CENTER)

Exersises=Button(frame1,text="Exersises",pady=20,padx=20,width=12,borderwidth = 10,command=exersises).place(relx=.5,rely=.3,anchor=CENTER)
Achievements=Button(frame1,text="Achievements",pady=20,padx=20,width=12,borderwidth = 10,command=achievements).place(relx=.5,rely=.4,anchor=CENTER)
userInfo=Button(frame1,text="User Info",pady=20,padx=20,width=12,borderwidth = 10,command=userInfo).place(relx=.5,rely=.5,anchor=CENTER)
History=Button(frame1,text="History",pady=20,padx=20,width=12,borderwidth = 10,command=history).place(relx=.5,rely=.6,anchor=CENTER)

app.mainloop()