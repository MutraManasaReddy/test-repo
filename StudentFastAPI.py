from fastapi import FastAPI

app = FastAPI

students = []

#@app.get("/")
#def root():
    #return {"welcome":"students"}


#@app.get("/")
#def root():
   #return{"hello":"students"}

@app.post("/creating_students")
def add_student(student_name:str):
    students.append(student_name)
    return students
#@app.get("/student")
#def list_all_student():
 #   return students