import os 
os.system("cls")

class person:
    def __init__(self ,fname, lname):
        self.fname = fname
        self.lname =lname
    def printName(self):
        return f'{self.fname} {self.lname} ' 

class student(person):
    def __init__(self,fname,lname,year,course,mark):
        super().__init__(fname,lname)
        self.Graduationyear = year
        self.course = course
        self.mark = mark
    def printName(self):
        return super().printName()
    def __str__(self):
        return ( f' Name: {self.printName()},  Year: {self.Graduationyear}, ' f'Course: {self.course},  Mark: {self.mark}')   
student1 = student('Akullu Bella ','Prossy',2009,'Information Technology',60) 
print(student1)          
    
















     