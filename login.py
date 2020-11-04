from tkinter import *
from tkinter import messagebox
import main as mp


username = []
passcode = {}

username.append("admin")
passcode['admin'] = 'admin'

root_login = str()
root_register = str()


def login_check(a,b):
    global username,passcode
    if a.get() in username and b.get() == passcode[a.get()]:
        messagebox.showinfo(message='Login Successfully  !!!')
        global root_login
        root_login.destroy()
        mp.main_frame()

    else:
        messagebox.showinfo(message='Wrong Entry!!!\nTry Again')


def register(a,b):
    global username,passcode

    if a.get() is None or b.get() is None:
        messagebox.showinfo(message='Fill the required fields')

    elif a.get() in username or b.get() in passcode.values():
        messagebox.showwarning(message='Existing password or username')

    else:
        username.append(a.get())
        passcode[a.get()] = b.get()
        messagebox.showinfo(message = 'Registerd Successfully !')
        root_register.destroy()
        login_frame()    
        

def back():
    root_register.destroy()
    login_frame()


'''
canvas = Canvas(root)
canvas.config(bg = 'orange')
canvas.pack(fill='both',expand = True)
'''

def login_frame():
    global root_login
    root_login = Tk()
    root_login.title("Login Page")
    root_login.minsize(width=400,height=400)
    root_login.geometry("{0}x{1}+0+0".format((int(root_login.winfo_screenwidth()*0.999)), int((root_login.winfo_screenheight()*0.999))))


    frame = Frame(root_login,bg='Orange',width=700,height=400)
    frame.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

    label = Label(frame,text='Log In',bg='Orange',font=('Georgia',36,'bold'))
    name = Label(frame,text='User_Name: ', bg='Orange', font=('Arial',18,'bold'))

    namee_text=StringVar()
    namee = Entry(frame,textvariable=namee_text,fg='gray',width=25,font=('Arial',16,'bold'))

    password1 = Label(frame,text='Enter Password : ',bg='Orange', fg='Green',font=('Arial',18,'bold'))

    password1e_text=StringVar()

    password1e = Entry(frame,textvariable=password1e_text,bg='White',fg='gray',width=25,font=('Arial',16,'bold'),show='*')

    buttonlogin = Button(frame,text='LOG IN',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2',command = lambda : login_check(namee_text,password1e_text))
    
    buttonregister = Button(frame,text='REGISTER',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2',command = register_frame)



    label.place(x=40,y=40,width=200,height=80)
    name.place(x=100,y=140,width=240,height=60)

    namee.place(x=380,y=150,width=200,height=30)

    password1.place(x=85,y=220,width=240,height=30)

    password1e.place(x=380,y=215,width=200,height=30)



    buttonlogin.place(x=180,y=300,width=140,height=50)
    buttonregister.place(x = 400,y = 300,width = 140,height = 50)

    frame.pack(expand = True,fill='both')

    root_login.mainloop()


def register_frame():
    root_login.destroy()

    global root_register
    root_register = Tk()

    root_register.title("Login Page")
    root_register.geometry("{0}x{1}+0+0".format((int(root_register.winfo_screenwidth()*0.999)), int((root_register.winfo_screenheight()*0.999))))
    
    
    frame = Frame(root_register,bg='Orange',width=700,height=400)

    label = Label(frame,text='SIGN UP',bg='Orange',font=('Georgia',32,'bold'))
    name = Label(frame,text='User_Name: ', bg='Orange', font=('Arial',18,'bold'))

    namee_text=StringVar()
    namee = Entry(frame,textvariable=namee_text,fg='gray',width=25,font=('Arial',16,'bold'))

    password1 = Label(frame,text='Create Password : ',bg='Orange', fg='Green',font=('Arial',18,'bold'))

    password1e_text=StringVar()

    password1e = Entry(frame,textvariable=password1e_text,bg='White',fg='gray',width=25,font=('Arial',16,'bold'),show='*')

    buttonback = Button(frame,text='BACK',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2',command = back)

    buttonregister = Button(frame,text='REGISTER',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2',command = lambda : register(namee_text,password1e_text))



    label.place(x=40,y=40,width=200,height=80)
    name.place(x=100,y=140,width=240,height=60)

    namee.place(x=380,y=150,width=200,height=30)

    password1.place(x=85,y=220,width=240,height=30)

    password1e.place(x=380,y=215,width=200,height=30)



    buttonback.place(x=180,y=300,width=140,height=50)
    buttonregister.place(x = 400,y = 300,width = 140,height = 50)

    frame.pack()

    root_register.mainloop()

    

if __name__ == "__main__":
    login_frame()
