from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql


bookInfo1=str()
bookInfo2 = str()
bookInfo3 = str()
bookInfo4 = str()
Canvas1 = str()
con = str()
cur = str()
bookTable = str()
root = str()


# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase="library_management"

con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
cur = con.cursor()

# Enter Table Names here
issueTable = "books_issued" 
bookTable = "books" #Book Table


def deleteBook():
    
    bid = bookInfo1.get()
    
    deleteSql = "delete from "+bookTable+" where bid = '"+bid+"'"
    deleteIssue = "delete from "+issueTable+" where bid = '"+bid+"'"
    try:
        cur.execute(deleteSql)
        con.commit()
        cur.execute(deleteIssue)
        con.commit()
        messagebox.showinfo('Success',message="Book Record Deleted Successfully")
    except:
        messagebox.showinfo("Please check Book ID")
    

    print(bid)

    bookInfo1.delete(0, END)
    root.destroy()
    
def delete(): 
    
    global bookInfo1,bookInfo2,bookInfo3,bookInfo4,Canvas1,con,cur,bookTable,root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("{0}x{1}+0+0".format((int(root.winfo_screenwidth()*0.999)), int((root.winfo_screenheight()*0.999))))
    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="orange")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="black",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Delete Book", bg='black', fg='white', font=('Arial',18,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="Book ID : ", bg='black', fg='white',font=('Arial',18,'bold'))
    lb2.place(relx=0.05,rely=0.5)
        
    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3,rely=0.5, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=deleteBook,font=('Arial',18,'bold'))
    SubmitBtn.place(relx=0.28,rely=0.85, relwidth=0.18,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy,font=('Arial',18,'bold'))
    quitBtn.place(relx=0.53,rely=0.85, relwidth=0.18,relheight=0.08)
    
    root.mainloop()