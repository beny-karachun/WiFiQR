from tkinter import *
from tkinter import ttk
from tkinter import CURRENT
import subprocess
import tkinter
         
      

 
      
meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = meta_data.decode('utf-8', errors ="backslashreplace")

# splitting data by line by line
data = data.split('\n')

# creating a list of profiles
profiles = []

# traverse the data
for i in data:
    
    # find "All User Profile" in each item
    if "All User Profile" in i :
        
        # if found
        # split the item
        i = i.split(":")
        
        # item at index 1 will be the wifi name
        i = i[1]
        
        # formatting the name
        # first and last character is use less
        i = i[1:-1]
        
        # appending the wifi name in the list
        profiles.append(i)

master = Tk()
master.geometry("500x500")
def printname():
    newWindow = Toplevel(master)
    newWindow.geometry("200x200")
    newWindow.title("test")
    Label(newWindow,text=variable.get()).grid(row=0,column=0)
    # newWindow.mainloop()
    # return(variable.get())
variable = tkinter.StringVar(master)
variable.set("Choose your Wi-Fi")
w = OptionMenu(master,variable,*profiles).grid(row=61,column=0)

d = ttk.Combobox(master,value=[variable.get()]).grid(row=10,column=0)

label1 = Label(master, text = "Get a QR code for your local Wi-Fi network").grid(row=0,column=0)
label2 = Label(master, text = "Never have your guests asking for your Wi-Fi code again!").grid(row=1,column=0)
button = Button(master, text = "Generate QR code",command=printname).grid(row=2,column=0)
exit = Button(master,text = "Exit", command=master.destroy).grid(row=4,column=0)



mainloop()
