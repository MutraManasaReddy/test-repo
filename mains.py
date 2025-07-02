from fastapi import FastAPI
#from pydantic import BaseModel

app = FastAPI()


#class Student(BaseModel):
   # name :str
  #  rollno:int
 #   schoolname:str

students =[]

@app .post("/Student")
def add_student():
    students.append(students)
    return students
#@app.get("/")
#def root():
  #  return{"hello":"students"}

#@app.post("/students")
#def add_student(student_name:str):
  #  students.append(student_name)
 #   return students
#@app.get("/student")
#def list_all_student():
 #   return students
#@app.put("/student_name")
#def update_student(student_id:int):
    #if student_name is None:
   #     return students
  #  if school_name is not None:
 #       return students
#@app.delete("/students")
#def remove_student(student_name:str):
    #students.remove(student_name)
   # return students

    






