import tkinter as tk
from datalayer import DBMarks

class UpdateMarksForm:
    def __init__(self,regid,sessid,cid,sem,name, Marks):
        self.root = tk.Toplevel()
        self.root.geometry("455x400")
        self.root.title("Add Marks")
        
        self.regID = regid
        self.y = 130
        self.reg = tk.StringVar()
        self.nam = tk.StringVar()
        
        self.lbl1 = tk.Label(self.root, text = "RegistrationId")
        self.lbl1.place(x = 10 , y = 40)
        self.ent1 = tk.Entry(self.root, textvariable = self.reg, state = "readonly", width = 10)
        self.ent1.place(x = 110, y = 40)
        self.reg.set(self.regID)
        
        self.lbl3 = tk.Label(self.root, text = "Name")
        self.lbl3.place(x = 270 , y = 40)
        self.ent2 = tk.Entry(self.root, textvariable = self.nam, state = "readonly", width = 10)
        self.ent2.place(x = 370, y = 40)
        self.nam.set(name)

        self.lbl5 = tk.Label(self.root, text = "Subject")
        self.lbl5.place(x = 110 , y =100)
        self.lbl6 = tk.Label(self.root, text = "Marks")
        self.lbl6.place(x = 200 , y = 100)

        dbsubjects = DBMarks()
        self.AllSubjects = dbsubjects.GetSubjects(sessid,cid,sem)
        self.MarksList = []
        
        for a,m in zip(self.AllSubjects,Marks):
            listvar = tk.StringVar()
            self.MarksList.append((listvar,a.SemesterSubjectId))
            lbl = tk.Label(self.root, text = a.Subject)
            lbl.place(x = 110, y = self.y)
            ent = tk.Entry(self.root, textvariable = listvar)
            ent.place(x = 200, y = self.y)
            self.y += 40
            listvar.set(m)
         
        self.AddButton = tk.Button(self.root, text = "Update", command = self.UpdateMarks, width = 12)
        self.AddButton.place(x = 150, y = self.y + 20)
    
    def UpdateMarks(self):
        db = DBMarks()
        for marks in self.MarksList:
            mark = marks[0].get()
            ssid = marks[1]
            regid = self.regID
    
            db.UpdateMarks(regid,ssid,mark)
            
    def showDialog(self):
        self.root.mainloop()