from tkinter import *
import PIL as pil
import pymysql
from tkinter import messagebox
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from IssueBook import *
from ReturnBook import *
#import login as lg
import scrap as sc
import FineDetails as fd

def main_frame() :
    # Add your own database name and password here to reflect in the code
    mypass = "root"
    mydatabase="library_management"

    con = pymysql.connect(host="localhost",user="root",password=mypass,database=mydatabase)
    cur = con.cursor()

    root = Tk()
    root.title("Library")
    root.minsize(width=400,height=400)
    root.geometry("{0}x{1}+0+0".format((int(root.winfo_screenwidth()*0.999)), int((root.winfo_screenheight()*0.999))))

    # Take n greater than 0.25 and less than 5
    same=True
    n=0.50

    # Adding a background image
    background_image =pil.Image.open("./lib1.jpg")
    [imageSizeWidth, imageSizeHeight] = background_image.size

    newImageSizeWidth = int(imageSizeWidth*n)
    if same:
        newImageSizeHeight = int(imageSizeHeight*n) 
    else:
        newImageSizeHeight = int(imageSizeHeight/n) 
            
    background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),pil.Image.ANTIALIAS)
    img = pil.ImageTk.PhotoImage(background_image)

    Canvas1 = Canvas(root)

    Canvas1.create_image(300,340,image = img)      
    Canvas1.config(bg="orange",width = newImageSizeWidth, height = newImageSizeHeight)
    Canvas1.pack(expand=True,fill=BOTH)


    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.2,rely=0.02,relwidth=0.6,relheight=0.16)

    headingLabel = Label(headingFrame1, text="Welcome to \n SMIT Library", bg='orange', fg='black', font=('Arial',18,'bold'))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    btn1 = Button(root,text="Add Book Details",bg='orange', fg='black', command=addBook,font=('Arial',18,'bold'))
    btn1.place(relx=0.28,rely=0.2, relwidth=0.45,relheight=0.1)
            
    btn2 = Button(root,text="Delete Book",bg='orange', fg='black', command=delete,font=('Arial',18,'bold'))
    btn2.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
            
    btn3 = Button(root,text="View Book List",bg='orange', fg='black', command=View,font = ('Arial',18,'bold'))
    btn3.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
            
    btn4 = Button(root,text="Issue Book to Student",bg='orange', fg='black', command = issueBook,font = ('Arial',18,'bold'))
    btn4.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
            
    btn5 = Button(root,text="Return Book",bg='orange', fg='black', command = returnBook,font=('Arial',18,'bold'))
    btn5.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)

    btn6 = Button(root,text="Download Books",bg='orange', fg='black', command = sc.scrap_frame,font=('Arial',18,'bold'))
    btn6.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

    btn7 = Button(root,text="Fine Details",bg='orange', fg='black', command = fd.fine_frame,font=('Arial',18,'bold'))
    btn7.place(relx=0.28,rely=0.8, relwidth=0.45,relheight=0.1)

    root.mainloop()
