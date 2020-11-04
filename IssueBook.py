from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

issueBtn = str()
labelFrame = str()
lb1 = str()
inf1 = str()
inf2 = str()
inf3 = str()
quitBtn = str()
root = str()
Canvas1 = str()
status = str()


# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="library_management"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "issued_books" 
bookTable = "books"
    
#List To store all Book IDs
allBid = [] 

def issue():
    
    global issueBtn,labelFrame,lb1,inf1,inf2,quitBtn,root,Canvas1,status
    
    bid = inf1.get()
    issueto = inf2.get()
    date = inf3.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    inf3.destroy()
    
    
    extractBid = "select bid from "+bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])
        
        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
                
            if check == 'avail':
                status = True
            else:
                status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book IDs")
    
    issueSql = "insert into "+issueTable+" values ('"+bid+"','"+issueto+"','"+date+"')"
    show = "select * from "+issueTable
    
    updateStatus = "update "+bookTable+" set status = 'issued' where bid = '"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success',"Book Issued Successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message',"Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error","The value entered is wrong, Try again")
    
    print(bid)
    print(issueto)
    
    allBid.clear()
    
def issueBook(): 
    
    global issueBtn,labelFrame,lb1,inf1,inf2,inf3,quitBtn,root,Canvas1,status
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("{0}x{1}+0+0".format((int(root.winfo_screenwidth()*0.999)), int((root.winfo_screenheight()*0.999))))
    
    Canvas1 = Canvas(root)
    Canvas1.config(bg="orange")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Arial',18,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)  
        
    # Book ID
    lb1 = Label(labelFrame,text="Book ID : ", bg='black', fg='white',font=('Arial',15,'bold'))
    lb1.place(relx=0.05,rely=0.2)
        
    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    # Issued To Student name 
    lb2 = Label(labelFrame,text="Issued To : ", bg='black', fg='white',font= ('Arial',15,'bold'))
    lb2.place(relx=0.05,rely=0.4)
        
    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4, relwidth=0.62)

    # Date
    lb3 = Label(labelFrame,text= "Date : ",bg='black', fg= 'white',font=('Arial',15,'bold'))
    lb3.place(relx = 0.05,rely = 0.6)

    inf3 = Entry(labelFrame)
    inf3.place(relx= 0.3,rely= 0.6,relwidth= 0.62)
    
    
    #Issue Button
    issueBtn = Button(root,text="Issue",bg='#d1ccc0', fg='black',command=issue,font=('Arial',15,'bold'))
    issueBtn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#aaa69d', fg='black', command=root.destroy,font=('Arial',15,'bold'))
    quitBtn.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)
    
    root.mainloop()

if __name__ == "__main__":
    issueBook()