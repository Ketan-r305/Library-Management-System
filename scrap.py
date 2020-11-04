from selenium import webdriver
from tkinter import *
from tkinter import messagebox
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import os

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if os.name == 'nt':
        import winreg
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            location = winreg.QueryValueEx(key, downloads_guid)[0]
        return location
    else:
        return os.path.join(os.path.expanduser('~'), 'downloads')

d_path = get_download_path()


#option = webdriver.ChromeOptions()
#option.add_argument('headless')

driver = str()
driver2 = str()

# driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe') # ,options = option)
# driver2 = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe') #,options = option)
book_name = []
book_url = {}
value = str()
root = str()
mylistbox = str()
namee_text = str()



def download_link(file,link):
    driver2.get(link)
    time.sleep(15)
    t = driver2.find_element_by_xpath("//a[@class='btn btn-primary btn-user']")
    t.click()
    return



def download():
    global value 
    print(value)
    
    if value != "":
        download_link(value,book_url[value])
        messagebox.showinfo(message = 'Downloading in \n' +d_path +  '!!!')
        root.destroy()
    else:
        messagebox.showinfo(message='Error !\n select from listbox')




def util(choice):

    global driver,driver2

    driver = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe') # ,options = option)
    driver2 = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe') #,options = option)

    ch = 1
    link= {}

    driver.get("https://www.pdfdrive.com")
    driver.find_element_by_id("q").send_keys(choice+"\n")
    url = driver.current_url
    uClient = uReq(url)
    page_html = uClient.read()
    page_soup = BeautifulSoup(page_html, "html.parser")
    uClient.close()
    container1 = page_soup.findAll("div", {"class": "file-left"})
    container2 = page_soup.findAll("div", {"class": "file-right"})
        
    for x in range(0,len(container1)):
        fake = container2[x].a["href"]
        index = -1
        while(True):
            if fake[index] == 'e':
                fake = fake[:index]+'d'+fake[index+1:]
                break
            else:
                index-=1
        link[container1[x].img['title']] = "https://www.pdfdrive.com"+fake
            
    return (container1,link)




def serch():
    #global mylistbox
    global namee_text
    global book_name,book_url

    book_name,book_url = util(namee_text.get())
    print(namee_text.get())

    for x in range(len(book_name)):
        mylistbox.insert(END,(str(x+1) + "    " + book_name[x].img['title']))



def CurSelet(evt):
    global value 
    value=str((mylistbox.get(mylistbox.curselection())))
    value = value[5:]
    

def scrap_frame():
    global root
    global mylistbox,namee_text
    global driver,driver2
    
    root = Tk()

    root.title('Download book')

    root.minsize(width=400,height=400)
    root.geometry("{0}x{1}+0+0".format((int(root.winfo_screenwidth()*0.999)), int((root.winfo_screenheight()*0.999))))


    frame = Frame(root,bg='Orange')

    label = Label(frame,text='Book Download',bg='Orange',font=('Georgia',18,'bold'))
    label_info = Label(frame,text = 'Select one item from Listbbox:',bg = 'Orange',font = ('Georgia',12,'bold'))
    name = Label(frame,text='Topic Name: ', bg='Orange', font=('Arial',18,'bold'))

    #namee_text=StringVar()
    namee_text = Entry(frame,fg='gray',width=25,font=('Arial',16,'bold'))

    mylistbox=Listbox(root,width=90,height=20,font=('times',13))
    mylistbox.place(x = 700,y = 170)

    mylistbox.bind('<<ListboxSelect>>',CurSelet)

    buttonsearch = Button(frame,text='SEARCH',bg='gray',fg='gray12',font=('Georgia',18,'bold'),cursor='hand2',command = serch)
        
    buttondownload = Button(frame,text='DOWNLOAD',bg='gray',fg='gray12',font=('Georgia',15,'bold'),cursor='hand2',command = download)



    label.place(x=40,y=40,width=200,height=80)
    label_info.place(x=700,y=150)
    name.place(x=100,y=140,width=240,height=60)

    namee_text.place(x=380,y=150,width=200,height=30)

    buttonsearch.place(x=180,y=300,width=140,height=50)
    buttondownload.place(x = 400,y = 300,width = 140,height = 50)

    frame.pack(expand = True,fill='both')

    root.mainloop()
    driver.close()
    driver2.close()

if __name__ == "__main__":
    scrap_frame()