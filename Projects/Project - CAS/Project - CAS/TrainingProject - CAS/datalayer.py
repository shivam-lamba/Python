import pyodbc
from abc import ABC
from components import Course, Session, Subject, Student, SemesterSubjects, SubjectNames, AttendanceRecord

class DBOperations(ABC):
    def __init__(self):
        self.con = pyodbc.connect("DRIVER={SQL SERVER};SERVER=LAPTOP-NDCIJ33J\SQLEXPRESS;database=ProjectDB;username=sa;pwd=ankush")
        
class DBCourse(DBOperations):
    def __init__(self):        
        DBOperations.__init__(self)
        
    def AddCourse(self, c):
        
        cur = self.con.cursor()
        
        query = "Insert into Courses values (?,?)"
        row = (c.CourseName, c.Description)
        
        cur.execute(query, row)
        self.con.commit()
        
    def GetCourse(self):
        cur = self.con.cursor()
        cur.execute("Select * from Courses")
        
        records = cur.fetchall()
        AllCourses = []
        
        for record in records:
            pro = Course()
            pro.CourseId = record[0]
            pro.CourseName = record[1]
            pro.Description = record[2]
            
            AllCourses.append(pro)
            
        return AllCourses
    
    def DeleteCourse(self, c):
        cur = self.con.cursor()
        
        query = "Delete from Courses where CourseId = ?"
        row = (c.CourseId)
        
        cur.execute(query,row)
        self.con.commit()
        

class DBSessions(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
        
    def AddSession(self, ses):
        cur = self.con.cursor()
        
        query = "Insert into Sessions values(?)"
        row = (ses.Session)
        
        cur.execute(query,row)
        self.con.commit()
        
    def GetSession(self):
        cur = self.con.cursor()
        cur.execute("Select * from Sessions")
        
        records = cur.fetchall()
        AllSessions = []
        
        for record in records:
            pro = Session()
            pro.SessionId = record[0]
            pro.Session = record[1]
            
            AllSessions.append(pro)

        return AllSessions
    
    def DeleteSessions(self, c):
        cur = self.con.cursor()
        
        query = "Delete from Sessions where SessionId = ?"
        row = (c.SessionId)
        
        cur.execute(query,row)
        self.con.commit()
        
        
class DBSubjects(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
    
    def AddSubject(self, sub):
        cur = self.con.cursor()
        
        query = "Insert into Subjects values(?,?)"
        row = (sub.Subject, sub.Description)
        
        cur.execute(query,row)
        self.con.commit()
        
    def GetSubjects(self):
        cur = self.con.cursor()
        cur.execute("Select * from Subjects")
        
        records = cur.fetchall()
        AllSubjects = []
        
        for record in records:
            pro = Subject()
            pro.SubjectId = record[0]
            pro.Subject = record[1]
            pro.Description = record[2]
            
            AllSubjects.append(pro)
            
        return AllSubjects
    
    def DeleteSubjects(self, c):
        cur = self.con.cursor()
        
        query = "Delete from Subjects where SubjectId = ?"
        row = (c.SubjectId)
        
        cur.execute(query,row)
        self.con.commit()
        
class DBStudents(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
        
        
    def AddStudent(self, stud):
        cur = self.con.cursor()
        
        query = "Insert into Students values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        #row =(stud.RollNo, stud.RegistrationDate, stud.Name, stud.Dob, stud.Gender, stud.FatherName, stud.MotherName, stud.Address, stud.City, stud.ContactNo, stud.EmailId, stud.Nationality, stud.CourseId, stud.SessionID)
        row=(stud.RollNo, stud.RegistrationDate,stud.Name,stud.Dob, stud.Gender,stud.FatherName,stud.MotherName,stud.Address, stud.City, stud.ContactNo,stud.EmailId,stud.Nationality,stud.CourseId,stud.SessionID)
        cur.execute(query,row)
        self.con.commit()
        
    def ViewStudents(self, cid , sid):
        cur = self.con.cursor()
        
        query="Select RegistrationId,Name,RollNo,RegistrationDate,Dob,ContactNo from Students where CourseId = ? and SessionId = ?"
        row = (cid,sid)
        
        cur.execute(query, row)
        records = cur.fetchall()
        StudentDetailsList = []
        
        for record in records:
            comp = Student()
            comp.RegistrationId = record[0]
            comp.Name = record[1]
            comp.RollNo = record[2]
            comp.RegistrationDate = record[3]
            comp.Dob = record[4]
            comp.ContactNo = record[5]
            
            StudentDetailsList.append(comp)
        
        return StudentDetailsList
    
    def FindStudent(self,sessid,cid,sem):
        cur = self.con.cursor()
        
        query = "select * from students where CourseId=? and SessionId=? and RegistrationId IN (Select RegistrationId From Enrollments Where Semester=? and IsCurrent=1)"
        row = (cid,sessid,sem)
        
        cur.execute(query,row)
        records = cur.fetchall()
        
        AllDetails = []
        
        for record in records:
            st = Student()
            st.RegistrationId = record[0]
            st.RollNo = record[1]
            st.RegistrationDate = record[2]
            st.Name = record[3]
            st.Dob = record[4]
            st.Gender = record[5]
            st.FatherName = record[6]
            st.MotherName = record[7]
            st.Address = record[8]
            st.City = record[9]
            st.ContactNo = record[10]
            st.EmailId = record[11]
            st.Nationality = record[12]
            st.CourseId = record[13]
            st.SessionID = record[14]
        
            AllDetails.append(st)
        
        return AllDetails
    
    
class DBSemesterSubjects(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
        
    def StoreValues(self, val):
        cur = self.con.cursor()
        
        query = "Insert into SemesterSubjects values (?,?,?,?)"
        row = (val.Semester, val.CourseId, val.SubjectId, val.SessionId)
        
        cur.execute(query,row)   
        self.con.commit()
        
    def Getdata(self, val):
        cur = self.con.cursor()
        
        query = "Select ss.SemesterSubjectId, ss.Semester, sub.Subject from SemesterSubjects as ss,Sessions as sess, Courses as c,Subjects as sub where ss.CourseId = c.CourseId and ss.SubjectId = sub.SubjectId and ss.SessionId = sess.SessionId and ss.CourseId = ? and ss.SessionId = ? and ss.Semester = ?"
        row = (val.CourseId, val.SessionId , val.Semester)
        
        cur.execute(query, row)
        
        records = cur.fetchall()
        SemesterSubjectsList = []
        
        for record in records:
            ss = SemesterSubjects()
            ss.SemesterSubjectId = record[0]
            ss.Semester = record[1]
            ss.SubjectId = record[2]
            
            SemesterSubjectsList.append(ss)
        return SemesterSubjectsList
    
class DBEnrollment(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
        
    def FindRoll(self, roll):
        cur = self.con.cursor()
        
        query = "Select RegistrationId,RollNo,RegistrationDate,Name,Dob,Gender,FatherName,MotherName,Address,City,ContactNo,EmailId,Nationality,c.courseName, s.session from Students as st ,Courses as c ,Sessions as s where st.CourseId = c.CourseId and st.SessionId = s.SessionId and RollNo = ?"
        row = roll
        
        cur.execute(query, row)
        records = cur.fetchall()
        AllData = []
        
        for record in records:
            st = Student()
            st.RegistrationId = record[0]
            st.RollNo = record[1]
            st.RegistrationDate = record[2]
            st.Name = record[3]
            st.Dob = record[4]
            st.Gender = record[5]
            st.FatherName = record[6]
            st.MotherName = record[7]
            st.Address = record[8]
            st.City = record[9]
            st.ContactNo = record[10]
            st.EmailId = record[11]
            st.Nationality = record[12]
            st.CourseId = record[13]
            st.SessionID = record[14]
            
            AllData.append(st)
        return AllData
    
    def Register(self,date,sem,rid):
        cur = self.con.cursor()
        
        cur.execute("Update Enrollments set IsCurrent=0 where RegistrationId=?",(rid))
        
        cur.execute("Insert into Enrollments values(?,?,?,?)",(date,sem,rid,1))
        self.con.commit()
        
class DBMarks(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
        
    def CheckMarks(self,rid,sem):
        cur = self.con.cursor()
        
        cur.execute("select Marks from Marks as [M] , SemesterSubjects[SS] where M.SemesterSubjectId = SS.SemesterSubjectId and RegistrationId = ? and SS.Semester = ?",(rid,sem))
        dbMarks = cur.fetchall()
        MarksList = []
        for marks in dbMarks:
            MarksList.append(marks[0])
        
        return MarksList
        
    def GetSubjects(self, sessid,cid,sem):
        cur = self.con.cursor()
        
        query = "Select SS.SemesterSubjectId, S.Subject From SemesterSubjects as [SS], Subjects as [S] Where SS.SubjectId=S.SubjectId and SS.SessionId = ? and SS.CourseId = ? and SS.Semester = ?"
        row = (sessid,cid,sem)
        
        cur.execute(query, row)
        records = cur.fetchall()
        
        AllSubjects = []
        
        for record in records:
            sn = SubjectNames()
            sn.SemesterSubjectId = record[0]
            sn.Subject = record[1]
            
            AllSubjects.append(sn)
            
        return AllSubjects
    
    def AddMarks(self, ssid, rid, marks,date):
        cur = self.con.cursor()
        
        query = "Insert into Marks values (?,?,?,?)"
        row = (date,ssid,rid,marks)
        
        cur.execute(query,row)
        self.con.commit()
        
    def UpdateMarks(self, rid,ssid, marks):
        cur = self.con.cursor()
        
        query = "Update Marks set Marks = ? where RegistrationId = ? and SemesterSubjectId = ?"
        row = (marks, rid, ssid)
        
        cur.execute(query,row)
        self.con.commit()
        
class DBAttendance(DBOperations):
    def __init__(self):
        DBOperations.__init__(self)
        
    def SaveAttendance(self,rid, eid, att,date):
        cur = self.con.cursor()
        
        query = "Insert into Attendance values(?,?,?,?)"
        row = (date, rid, eid, att)
        
        cur.execute(query,row)
        self.con.commit()
        
    def GetEnrollmentId(self, regid):
        cur = self.con.cursor()
        
        cur.execute("Select EnrollmentId from Enrollments where RegistrationId = ?  and IsCurrent = 1", (regid))
        records = cur.fetchall()
        EnrollmentIdList = []
    
        for record in records:
            EnrollmentIdList.append(record[0])
            
        return EnrollmentIdList
    
    def GetAttendance(self, sem, cid, sid):
        cur = self.con.cursor()
        
        query = "select S.RegistrationId, S.Name, DatePart(Day, A.Date) as [Day], A.Attendance From Attendance as [A], Students as [S] Where A.RegistrationId=S.RegistrationId and A.RegistrationId IN (Select RegistrationId From Enrollments where Semester=? and IsCurrent=1) and S.CourseId = ? and S.SessionId = ? Order by A.RegistrationId, [Day]"
        row = (sem, cid, sid)
        
        cur.execute(query, row)
        records = cur.fetchall()
        AttendanceList = []
        
        
        for record in records:
            Att = AttendanceRecord()
            Att.RegistrationId = int(record[0])
            Att.Name = record[1]
            Att.Day = record[2]
            Att.Attendance = record[3]
            
            AttendanceList.append(Att)
            
        return AttendanceList