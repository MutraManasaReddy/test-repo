class Student:
    def __init__(self,name:str,rollno:int,schoolname:str):
        self.name= name,
        self.rollno = rollno,
        self.school_name = schoolname
        pass
    def __str__(self):
        return f"Student(name={self.name},rollno={self.rollno},school={self.school_name})"
        pass


list_of_students= []
# 1.To add a student

def add_student(name:str,rollno:int,schoolname:str):
    student = Student(name, rollno, schoolname) 
    list_of_students.append(student) # type: ignore
    return list_of_students

# 2. show all list of studentmanagement
def list_students():
        return list_of_students

# 3.to get a student by its rolln
def get_student(rollono:int):
     for student in list_of_students:
          if rollono == rollono:
               return student
          return None
     
# 4.update 
def update_student(rollno:int,name:str=None,schoolname:str=None):
     student = get_student(rollno)
     if student is None:
          return None
     if name is not None:
          student.name = name
     if schoolname is not None:
          student.schoolname = schoolname
          return student
     
# 5.remove
def remove_student(rollno:int):
     student = get_student(rollno)
     if student is None:
          return None
     list_of_students.remove(student)
     return student
         
print(add_student("manasa",10,"z.p.h.school"))
print(add_student("yoji",20,"golden valley"))
print(list_students())
print(get_student(10))

print(update_student(10,schoolname= "z.p.h.school"))
print(update_student(20,schoolname="golden balley"))
print(list_students())

print(remove_student("removing student with rollno 10"))
print(remove_student(10))
print(list_students())
       
        
                    






