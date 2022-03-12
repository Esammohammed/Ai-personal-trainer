from tkinter import *

def Home():
    userInfo.destroy()
    import home

userInfo=Tk()



userInfo.title('Home Page ')
userInfo.geometry('1120x920')
userInfo.configure(bg='#09c')

HomePage2=Label(userInfo,text='user Info Page',font=('bold',35),bg="#09c").place(relx=.5, rely=.2,anchor= CENTER)
Home=Button(userInfo,text="Back home",pady=20,padx=20,width=12,borderwidth = 10,command=Home).place(relx=.5,rely=.3,anchor=CENTER)
