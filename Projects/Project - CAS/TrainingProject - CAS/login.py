import tkinter as tk
from tkinter import messagebox
from gateway import Gateway
from datalayer import DBLogin

class Login():
    def __init__(self):
        self.root = tk.Tk()
        self.user = tk.StringVar()
        self.password = tk.StringVar()
        self.count = 0

        self.show = tk.PhotoImage(file = r"Images\hide1.png")
        self.hide = tk.PhotoImage(file = r"Images\hide1.png")
        
        self.welcome = tk.Label(self.root, text = "CAS", font=(28))
        self.welcome.place(x = 120, y = 10)
        
        self.accLabel = tk.Label(self.root, text = "Enter Usename")
        self.accLabel.place(x = 10, y = 50)
        self.accEntry = tk.Entry(self.root, textvariable = self.user)
        self.accEntry.place(x = 110 , y = 50)
        self.errorLabel1 = tk.Label(self.root, text = "" ,fg = 'red') 
        self.errorLabel1.place(x = 110, y =70)
        
        self.passLabel = tk.Label(self.root, text = "Enter password")
        self.passLabel.place(x = 10, y = 90)
        self.passEntry = tk.Entry(self.root, textvariable = self.password , show = "*")
        self.passEntry.place(x = 110 , y = 90)
        self.errorLabel2 = tk.Label(self.root, text = "" ,fg = 'red') 
        self.errorLabel2.place(x = 110, y =110)
        self.shButton = tk.Button(self.root, image = self.show , command =self.showhidePassword)
        self.shButton.place(x = 250 , y = 85)
        
        self.logButton = tk.Button(self.root, text = "LogIn" , command = self.loginClicked, width = 10)
        self.logButton.place(x = 40, y = 140)
        self.eButton = tk.Button(self.root, text = "Exit" , command = self.exitClicked, width = 10)
        self.eButton.place(x = 180, y = 140)
        
        self.root.geometry("295x180")
        self.root.title("LogIn")
        self.root.resizable('false','false')
    
    def loginClicked(self):
        check = self.validate()
        if check == True:
            if self.user.get() == 'cas' and int(self.password.get()) == 1234 :
                obj = Gateway(self.user.get())
                obj.showDialog()
        
            else:
                messagebox.showerror("LogIn", "Wrong username or password.Please Try Again")
            
    def exitClicked(self):
        a = messagebox.askyesno("LogIn", "Do you want to exit?")
        if a == True:
            self.root.destroy()
    
    def validate(self):
        val = True
        
        self.errorLabel1.config(text = "")
        self.errorLabel2.config(text = "")
        
        if self.password.get().isdigit() == False:
            val = False
            self.errorLabel2.config(text = "*Alphabets not allowed")
        
        if len(self.user.get()) == 0:
            val = False
            self.errorLabel1.config(text = "*Field Required")
            
        if len(self.password.get()) == 0:
            val = False
            self.errorLabel2.config(text = "*Field Required")
            
        return val
            
    def showhidePassword(self):
        if self.count % 2 ==0:
            self.passEntry.config(show = "")
            self.shButton.config(image = self.hide)
            
        else:
            self.passEntry.config(show = "*")
            self.shButton.config(image = self.show)
        self.count += 1
        
    def showDialog(self):
        self.root.mainloop()
    
obj = Login()
obj.showDialog()