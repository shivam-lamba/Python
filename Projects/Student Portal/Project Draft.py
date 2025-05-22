import random

#class account:
#implements class account here

class Account:
    def __init__(self, username, password):
        self._accountUsername = username
        self._accountPassword = password
        
    def validateLength(self):
        if len(self._password) < 6:
            return False
        return True

    def validateDigit(self):
        if self._password.isalpha():
            return False
        return True

    def addUsername(self):
        self._username = input("Enter a username 6 characters long:")

        while len(self._username) != 6 and len(self._username) <=  6 :
            self._username = input("Enter a username 6 characters long:")
        return self._username

    def getUsername(self):
        return self._username

    def addPassword(self):
        self._password = input("Enter a 6 character long password having atleast 1 digit:")

        while not self.validateLength() or not self.validateDigit():
            self._password = input("Enter a password :")
        return self._password 

            
    
class course:
    def __init__(self, name, code, unit):
        self._courseName = name
        self._courseCode = code
        self._courseUnit = unit
        
    def getCourseName(self):
        return self._courseName
    
    def getCourseCode(self):
        return self._courseCode
    
    def getCourseUnit(self):
        return self._courseUnit
    
class TakenCourse(Course):
    #implements class TakenCourse
    def __init__(self, collegeCourse, semester, grade = 0):
        name = collegeCourse.getCourseName()
        code = collegeCourse.getCourseCode()
        unit = collegeCourse.getCourseUnit()
        super().__init__(name, code, unit)
        
        self._semester = semester
        self._grade = grade
        
    def printCourse(self):
        print("Course Name: %s || Course Code: % || Course Unit %d" % (self._courseName, self._courseCode, self._courseUnit))
        self._semester.printSemester()
        print("Grade %d \n" % (self._grade))
    def printCode(self):
        print(self._courseCode)
    def getGrade(self):
        return self._grade
        
class CollegeCourse(Course):
    #implements and completes class CollegeCourse
    def __init__(self, name, code, unit):
        super().__init__(name, code, unit)
        self._courseUnit = unit
        
        def printCourse(self):
            print("Course Name: %s | Course Code: %s | Course Unit %d \n" % (self._courseName, self._courseCode, self._courseUnit))
            
class Student:
    #implements class student here
    def __init__(self, studentProfile, admissionYear=2020):
        self._asmissionYear = admissionYear
        self._admissionSemester = 1
        #Suppose student starts in semester 1 of the admission year
        self._generalTranscript = GeneralTranscript()
        self._semesterTranscript = CurrentSemesterTranscript()
        self._studentProfile = studentProfile
        
        def getAdmissionYear(self):
            returnself._admissionYear
            
        def registerCourse(self, collegeCourse, semester, grade = 0):
            courseRegistrationYear = semester.getYear()
            courseRegistrationSemester = semester.getSemesterNo()
            
            course = TakenCourse(collegeCourse, semester, grade)
            
            if semester.isCurrentSemester():
                self._semesterTranscript.addCourse(course)
                self._generalTranscript.addCourse(course)
            else:
                self._generalTranscript.addCourse(course)
                
        def getGTranscript(self):
            return self._generalTranscript
        
class StudentProfile:
    #implements class student here
    def __init__(self,id,firstName,lastName,gender,address,country,age):
        self._studentId = id
        self._firstName = firstName
        self._lastName = lastName
        self._gender = gender
        self._address = address
        self._countryOfOrigin = country
        self._age = age

    def getStudentId(self):
        return self._studentId

    def getFirstName(self):
        self._firstName = input("Please enter your first name:")
        return self._firstName

    def getLastName(self):
        self._lastName = input("Please enter your last name:")
        return self._lastName

    def addGender(self):
        self._gender = input("Please enter your gender:")

    def getGender(self):
        return self._gender

    def getAddress(self):
        return self._address

    def addCountry(self):
        self._countryOfOrigin = input("Please enter your country of origin:")

    def getCountry(self):
        return self._countryOfOrigin

    def addAge(self):
        self._age = input("Please enter age:")

    def getAge(self):
        return self._age    
        
class Transcript:
    #implements class transcipts here
    _totalCourses = 0
    def __init__(self,courses,names,code,grade,unit,semester):
        Transcript._totalCourses = Transcript._totalCourses + 1
        self._courses = courses
        self._name = names
        self._code = code
        self._grade = grade
        self._unit = unit
        self._semester = semester
        self._totalCourses = Transcript._totalCourses
        self.allTakenCourses = []
        
    def addCourse(self, takenCourse):
        self._allTakenCourses.append(takenCourse)
        #complete this method
        
    def getTranscript(self):
            return self._semesterTranscript
        
    def printTranscript(self):
        for c in self._allTakenCourses:
            c.printCourse()
    
    def getCourses(self):
        return self._courses

    def getName(self):
        return self._name

    def getCode(self):
        return self._code

    def getGrade(self):
        return self._grade

    def getUnit(self):
        return self._unit

    def getSemester(self):
        return self._semester

    def getTotalCourses(self):
        return self._totalCourses       
class GeneralTranscript(Transcript):
    #implements class GeneralTranscript here
    def __init__(self):
        super().__init__()


        
class CurrentSemesterTranscript(Transcript):
    #implements class CurrentSemesterTranscript here
    def __init__(self):
        super().__init__()
        
#class Manager:
#implements class Manager here
class Manager:
    def __init__(self,firstName,lastName,title):
        self._Managerftname = firstName
        self._Managerltname = lastName
        self._title = title
        
    def getMangerFirstName(self):
        return self._Managerftname
    
    def getManagerLastName(self):
        return self._Managerltname
    
    def getTitle(self):
        return self._title
        
class semester:
    #implements class Semester here
    def __init__(self, semesterNo, year):
        self._semesterNo = semesterNo
        self._year = year
        self._setIfCurrentSemester()
        
        def getYear(self):
            return self._year
        
        def getSemesterNo(self):
            return self._semesterNo
        
        #checks whether the semester object is representing current semester or not. Suppose, current semester is year = 2019, semester = 2
        def _setIfCurrentSemester(self):
            currentSemster = 2
            currentYear = 2019
            
            if (self._semesterNo == currentSemester) and (self._year == currentYear):
                self._isCurrentSemester = True
            else:
                self._isCurrentSemester = False
                
        def isCurrentSemester(self):
            return self._isCurrentSemester
        def printSemester(self):
            print("year: %d Semester%d isCurrent %d" %(self._year,  self._semesterNo, self._isCurrentSemester))
            
#class Menu:
#implements class Menu here
    
class Portal:
    
    #_currentsemester = Semester(2019, 2) #Static/class property. Suppose the current semester is second semester 2019
    def __init__(self):
        self._collegeCourses = []
        self._registerdStudents = []
        
        #use this method to register a student
        def registerStudent(self, student):
            self._registeredStudents.append(student)
            
        def addCourse(self, collegeCourse):
            self._collegeCourses.append(collegeCourses)
        #class this method to add some random courses to a student - You don't need to unnderstand how this method works. Just call it and it will add some courses
        #to the student and differnt semesters
        
        def addRandomCoursesToStudent(self, student):
            for course in self._collegeCourses:
                rand = random.uniform(0, 1)
                admissionYear = student.getAdmissionYear()
                currentSemester = Portal.getCurrentSemester()
                
                if currentSemester.getYear() == admissionYear:
                    numberOfSemstersBetweenCurrentSemesterAndAdmission = currentSemester.getSemesterNo()
                else:
                    numberOfSemstersBetweenCurrentSemesterAndAdmission = 2*(currentSemester.getYear() - admissionYear) + currentSemester.getSemesterNo()
                    
                randomSemester = random.randit(1, numberOfSemstersBetweenCurrentSemesterAndAdmission - 1)
                
                year = randomSemester//2
                SemesterNo = (randomSemester % 2) + 1
                semester = SemesterSemester(semesterNo, student.getAdmisson() + year)
                
                randomGrade = random.randint(30, 100)
                
                if rand <= .5:
                    student.registerCourse(course, semester, randomGrade)
                    
        # static/class method
        def getCurrentSemester():
            currentSemester = Semester(2, 2020) # static/class property suppose the current semester is second semester 2020  
            
            
        #Static/class property. Suppose the current semester is second semester 2019
            return currentSemester
        
        def getCollegeCourse(self, name):
            for item in self._collegeCourses:
                if item.getCourseName()==name:
                    return item
                return
class StudentsInCollege:
    def __init__(self, nameOfStudent, idOfStudent):
        self._nameOfStudent = nameOfStudent
        self._idOfStudent = idOfStudent
        
    def getStudentName(self):
        returnself._nameOfStudent
        
    def getidOfStudent(self):
        return self._idOfStudent
    
def testCollegeStudent():
    students1 = StudentsInCollege("Shivang Lamba", 825964)
    students2 = StudentsInCollege("Gaurav", 809118)
    
    nameOne = students1.getStudentName()
    nameTwo = students2.getStudentName()
    
    idOne = students1.getidOfStudent()
    idTwo = students2.getidOfStudent()
    
    print( nameOne,":", idOne)
    print( nameTwo, ":", idTwo)
    
def testAccount():
    print("*"*50)
    print("Please enter your account to login")
    print("*"*50)
    account = Account("login","Password")
    account.addUsername()
    acc = account.getUsername()
    account.validateLength()
    acc1 = account.validateDigit()
    psd = account.addPassword()
    print("Not registerd yet?")
    user = input("Type 'Register' and press enter to start the registration process!")
    
def menu():
    print("*"*50)
    print("Select from the options:")
    print("*"*50)
    print("[1] -Print my enrollment certificate")
    print("[2] -Print my courses")
    print("[3] -Print my transcript")
    print("[4] -Print my GPA")
    print("[5] -Print my ranking among all students in the college")
    print("[6] -List of all available courses")
    print("[7] -List all students")
    print("[8] -Show My Profile")
    print("[9] -Logout")
    print("[10]-Exit")
    print("*"*50)
    
class PortalManager:
    def __init__(self):
        self._portal = Portal()
        
    def createPortalSampleDatabase(self):
        #create all courses offered
        self._createAllCollegeCourses()
            
        #create student1
        student1Profile = studentProfile("William", "Byer", "M", "Canada")
        student1 = Student(student1Profile, 2019)
        #register the sample student
        self._portal.registerStudent(student1)
            
        #create student2
        student2Profile = StudentProfile("Zech", "Dempsy", "F", "Korea")
        student2 = Student(studentProfile, 2018)
        # register the sample student
        self._portal.registerStudent(student2)
            
        #create student3
        student3Profile = StudentProfile("Clay", "Jensen", "M", "United Kingdom")
        student3 = Student(studentProfile, 2019)
        # register the sample student
        self._portal.registerStudent(student3)
        
        #create student4
        student4Profile = StudentProfile("Neha", "Sharma", "F", "India")
        student4 = Student(studentProfile, 2019)
        # register the sample student
        self._portal.registerStudent(student4)
        
        #create student5
        student5Profile = StudentProfile("Katherine", "Langford", "F", "Australia")
        student5 = Student(studentProfile, 2018)
        #register the sample student
        self._portal.registerStudent(student5)
        
        #create TakenCourse
            
        sem2019_1 = Semester(2019, 1)
        sem2019_2 = Semester(2019, 2)
        sem2020_1 = Semester(2020, 1)
            
        crs1 = self._portal.getCollegeCourse("Python")
        crs2 = self._portal.getCollegeCourse("Object-Oriented Programming")
        crs3 = self._portal.getCollegeCourse("Problem Solving")
        crs4 = self._portal.getCollegeCourse("Project Management")
        crs5 = self._portal.getCollegeCourse("Java Programming")
            
        #takenCourseStudent1_Python = TakenCourse(cc1, sem2019_1,80)
        #takenCourseStudent1_OOP = TakenCourse(cc2, sem2019_2, 76)
        #takenCourseStudent1_ProblemSolving = TakenCourse(cc3, sem2020_1, 67)
        #takenCourseStudent1_ProjectManagement = TakenCourse(cc4, sem2019_1, 82)
        #takenCourseStudent1_JavaProgramming = TakenCourse(cc5, sem2019_2, 73)
            
            
        student1.registerCourse(crs1, sem2019_1, 80)
        student1.registerCourse(crs2, sem2019_1, 76)
        student1.registerCourse(crs3, sem2019_1, 67)
        student1.registerCourse(crs4, sem2019_1, 82)
        student1.registerCourse(crs5, sem2019_1, 73)
        
    def createATestPortal(self):
        
        #create all courses offered
        self._createAllCollegeCourses()
        #self._portal.printAllCollegeCourses()
        
        #create a sample student
        sampleStudentProfile = StudentProfile("Peter", "Brown", "M", "Canada")
        sampleStudent1 = Student(sampleStudentProfile, 2017)
        
        #register the sample student
        self._portal.registerStudent(sampleStudent1)
        
        #add some random courses with grades to the student
        
        self._portal.addRandomCoursesToStudent(sampleStudent1)
        
        
        firstName = sampleStudentProfile.getFirstName
        lastName = sampleStudentProfile.getLastName
        print(firstName)
        print(lastName)
        name = firstName + " " + lastName
        
        sampleStudentProfile.addGender()
        gender = sampleStudentProfile.getGender()
        print(gender)
        sampleStudentProfile.addCountry()
        country = sampleStudentProfile.getCountry()
        print(country)
        sampleStudentProfile.addAge
        age = sampleStudentProfile.getAge()
        studentId = sampleStudentProfile.getStudentId()
        address = sampleStudentProfile.getAddress()
        year = sampleStudentProfile.getAYear()
        print(Year)
        
        account = Acccount()
        account.addUsername()
        account1 = account.getUsername()
        account.checkLenght()
        account2 = account.checkDigit()
        password = account.addPassword()
        
        print("Username:",account1)
        print("password:",password2)
        
        print("Thanks, your account has been created successfully. Welcome abroad.")
        print(name)
        print(input())
        menu()
        
        coursenm1=Transcript.addCourse("Python")
        coursenm2=Transcript.addCourse("Project Management")
        coursenm3=Transcript.addCourse("Java Programming")
        coursenm4=Transcript.addCourse("Android Programming")
        
        
        
        trans1 = Transcript("CSCI101", "Python", 101, 86, 3, 1)
        trans2 = Transcript("CSCI202", "Project Management", 202, 82, 3, 1)
        trans3 = Transcript("CSCI301", "Java Programming", 301, 64, 3, 2)
        trans4 = Transcript("CSCI401", "Android Programming", 401, 76, 2,3 )
        
        gd1 = trans1.getGrade()
        gd2 = trans2.getGrade()
        gd3 = trans3.getGrade()
        gd4 = trans4.getGrade()
        
        un1 = trans1.getUnit()
        un2 = trans2.getUnit()
        un3 = trans3.getUnit()
        un4 = trans4.getUnit()
        
        gpa = (gd1*un1 + gd2*un2 + gd3*un3 + gd4*un4)/(un1+un2+un3+un4)
        currentGPA = (gd4*un4) /un4
        
        
        allcourses=Transcript.printTranscript()
        
        
        samplestudent1.getGTranscript()
        
        manager = Manager("Peter", "Jackson", "Manager")
        firstnm = manager.getMangerFirstName()
        lastnm = manager.getManagerLastName()
        fullName = firstnm + "" + lastnm   
        title = manager.getTitle()
        
        choice = input("please enter a key:")
        while enterNumber!="10":
            
            if choice =="1":
                print("Dear Sir/Madam,")
                print("This is to certify that",name ,"with studentId",studentId," is a student in semester 2 at Columbia college.")
                print("He has taken addmission in college in Columbia College in", year, "and has taken courses so far")
                print("He currently resides at", address,".")
                menu()
                choice = input("Press another key:")
                
            elif choice == "2":
                print("Hi Mr.",name,",")
                print("You have taken the following courses so far:")
                student.getGTranscript().printTranscript()
                menu()
                choice = input("Press another key:")
                
            elif choice == "3":
                print("Hi Mr.",name,",")
                print("Here is your current semester Transcript:")
                student.getTranscript().printTranscript()
                print("Your current semester GPA is:")
                menu()
                choice = input("Press another key:")

            elif choice == "4":
                print("Hi Mr.",name,",")
                
                if gpa>=90:
                    rank = "1"
                    
                elif gpa<90 and gpa>=80:
                    rank = "2"
                    
                elif gpa<80 and gpa>=70:
                    rank = "3"
                    
                else:
                    rank = "4"
                    
                print("Your overall GPA is",gpa,"and your rank is",rank)
                choice = input("Press another key:")
                
            elif choice == "6":
                print("The following courses are offered in Columbia College")
                self._portal._collegeCourses()
                
                menu()
                choice = input("Press another key:")
                
            elif choice == "7":
                print("There are 4 Students in Columbia College as following:")
                print(name,":", studentId)
                testCollgeStudent()
                menu()
                choice = input("Press another key:")
                
            elif choice =="8":
                print("Name: Mr.",name)
                print("Student Id:", studentId)
                print("Gender:", gender )
                print("Address:", student.getAddress())
                print("Country Of Origin:", country)
                print("Age:", age )
                print("Year Of Admission:", year)
                print("Overall GPA:", gpa)
                                
               
                
            elif choice =="9":
                account.addUsername()
                account3 = account.getUsername()
                account.checkLenght()
                account4 = account.checkDigit()
                password3 = account.addPassword()
                if account3 == account1 and password3 ==password2:
                    print("*"*50)
                    print("Welcome to Columbia College")
                    print("*"*50)
                    menu()
                    choice = input("Press another key:")
                else:
                    print("*"*50)
                    print("your account does not exist")
                    print("Welcome to Columbia College Please Register")
                    test()
                    choice = input("Press another key:")
                    
                return
                
                
        
        #create college courses
        def _createAllCollegeCourses(self):
            python = CollegeCourse("Python", "CSCI101", 3)
            objectOrientedProgramming =  CollegeCourse("Object-Oriented Programming", "CSCI102", 2)
            problemSolving = CollegeCourse("Problem Solving", "CSCI201", 1)
            projectManagement = CollegeCourse("Project Management", "CSCI202", 3)
            javaProgramming = CollegeCourses("Java Programming", "CSCI301", 3)
            webDevelopment = CollegeCourses("Web Development", "CSCI302", 2)
            androidProgramming = CollegeCourses("AndroidProgramming", "CSCI401", 2)
            iOSApplication = CollegeCourses("iOSApplication", "CSCI402", 3)
            
            self._portal.addcourse(python)
            
            self._portal.addCourse(objectOrientedProgramming)
            self._portal.addCourse(problemSolving)
            self._portal.addCourse(projectManagement)
            self._portal.addCourse(javaProgramming)
            self._portal.addCourse(webDevelopment)
            self._portal.addCourse(androidProgramming)
            self._portal.addCourse(iOSApplication)
            
def main():
    portalManager = PortalManager()
    portalManager.createATestPortal()
    
main()