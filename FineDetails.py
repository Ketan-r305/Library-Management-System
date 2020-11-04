from tkinter import *
from tkinter import messagebox
import pymysql
import datetime as dt


total_days = int()
mylistbox = str()
reg = str()

def details():
    global total_days
    global reg

    mypass = "root"
    mydatabase="library_management"
    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()
    
    # Enter Table Names here
    issueTable = "issued_books"

    dateDetails = "select issued_to,date from "+issueTable

    try:
        cur.execute(dateDetails)
        con.commit()
    except:
        messagebox.showinfo("Error","Can't fetch data from  Database")

    dates = {}
    today_date = dt.date.today()
    row = cur.fetchall()
    print(row)
    
    for i in row:
        dates[i[0]] = []
    
    for i in row:
        dates[i[0]].append(i[1])

    if reg.get() not in dates.keys() : 
        messagebox.showinfo('Error','Reg_No not found !!')
    required_dates = dates[reg.get()]
    
    if required_dates == [] :
        mylistbox.insert(END,("    "+reg.get() + "                                            " + str(0)))
    else:
        for i in range(len(required_dates)) :
            required_dates[i] = (today_date - required_dates[i]).days
        total_fine = sum(required_dates)
        mylistbox.insert(END,("    "+reg.get() + "                                             " + str(total_fine)))


def fine_frame():
    global mylistbox,reg

    root = Tk()
    root.title('Fine Details')
    root.minsize(width=400,height=400)
    root.geometry("{0}x{1}+0+0".format((int(root.winfo_screenwidth()*0.999)), int((root.winfo_screenheight()*0.999))))

    frame = Frame(root,bg='Orange')

    label = Label(frame,text='Fine Details',bg='Orange',font=('Georgia',15,'bold'))

    name = Label(frame,text='Reg_No  : ', bg='Orange', font=('Arial',18,'bold'))
    reg = Entry(frame,fg='gray',width=25,font=('Arial',16,'bold'))

    mylistbox=Listbox(root,width=50,height=10,font=('Georgia',13))
    mylistbox.place(x = 700,y = 170)
    mylistbox.insert(END,('    Registration No.                                       Fine'))

    buttonSubmit = Button(frame,text='SUBMIT',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2',command = details)
    buttonQuit = Button(frame,text='QUIT',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2',command = root.destroy)


    label.place(x=40,y=40,width=200,height=80)
    name.place(x=100,y=140,width=240,height=60)
    reg.place(x=380,y=150,width=200,height=30)
    buttonSubmit.place(x=180,y=300,width=140,height=50)
    buttonQuit.place(x = 400,y = 300,width = 140,height = 50)
    frame.pack(expand = True,fill='both')

    root.mainloop()

if __name__ == "__main__":
    fine_frame()