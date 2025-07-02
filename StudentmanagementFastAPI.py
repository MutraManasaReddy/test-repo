from fastapi import FastAPI

app = FastAPI()

list_of_student = []

@app.get("/")
def read_root ():
    return("Welcome to student management")

@app.post("/ creating_student")
def add_student(name: str, rollno: int, school_name: str):
    student = student(name,rollno,school_name)
    list_of_student.append(student)
    return list_of_student 

#@app.get("list_of_students")
#def list_students():
 #   return list_of_student

#@app.get("get-student/{rollno}")
#def get_student(rollno :int):
    #for student in list_of_student:
   #     if student.rollno == rollno:
  #          return student
 #   return None

#@app.patch("update-student/{rollno}")
#def update_student(rollno:int, name:str = None, school_name:str = None):
    #student = get_student(rollno)
    #if student is None:
     #   return None
    #if name is not None:
    #    student.name ==name
   # if school_name is not None:
  #      student.school_name == school_name
 #       return list_of_student
    
    
#@app.delete("delete-student/{rollno}")
#def remove_student(rollno:int):
    #student = get_student(rollno)
    #if student is None:
     #   return None
    #list_of_student.remove(rollno)
   # return student

        
    
    


