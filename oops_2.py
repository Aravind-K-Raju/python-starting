class student:
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_grade(self,name):
        return (self.name,self.grade)
    
    def __str__(self):
        return f"{self.name}, {self.age}, {self.grade}"
    
class course:
    def __init__(self,cname,max_stu):
        self.name = cname
        self.max_stu = max_stu
        self.students = []

    def add_student(self,student):
        if len(self.students)< self.max_stu:
            self.students.append(student)
            return True
        return False
    
    def studentList(self):
        for i in range(0,self.max_stu):
            print(self.students[i])
    
    def get_avg_marks(self):
        pass

s1 = student("Arjun",19,75)
s2 = student("Tim",19,87)
s3 = student("jill",19,65)

c1 = course("science",3)
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)
c1.add_student(s1)

c2 = course("commerce",2)
c2.add_student(s2)
c2.add_student(s1)
c2.add_student(s3)

print(s1.get_grade(s1))
print(s2.get_grade(s2))
print(s3.get_grade(s3))

c1.studentList()
c2.studentList()