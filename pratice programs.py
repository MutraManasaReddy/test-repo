#class person:
    #def __init__(self,nama,age):
    
   #      self.name = "manasa"
 #       self.age = 24
#p1 =person("manasa",24)
#print(p1.name)
#print(p1.age)

#class student:
   # def __str__(self,name,rollno):
  #      self.name = "manasa"
 #       self.rollno =20
#p1 = student("manasa",20)
#print(p1.name)
#print(p1.rollno)

#class person:
    #def __init__(self,name,age):
    #    self.name = name
   #     self.age = age
  #  def __str__(self):
 #       return  f"{self.name},({self.age})"
#p1 = person("manaas",25)
#print(p1)                         --------------------__str__

#class person:
    #def __init__(self,name,age):
    #     self.age = age
  #  def myfunc(self):
 #       print("my name is"+ self.name )
#p1 = person("manasa",25)
#p1.myfunc()

#class  student:
   # def __init__(self,name,rollno):
  #      self.name = name
 #       self.rollno = rollno
#p1 = student("manasa","60")
#print(p1.name)
#print(p1.rollno)        

#class student:
   # def __init__(self,name,rollno):
    #    self.name = name
   #     self.rollno = rollno
  #  def __str__(self):
 #       return f"{self.name}({self.rollno})"
#p1 = student("manasa",65)
#print(p1.name)
#print(p1.rollno)        

#class student:
    #def __init__(self,name,rollno):
    #    self.name = name
   #     self.rollno = rollno
  #  def myfunc(self):
 #       print("my name is "+self.name)
#p1 =student("manasa",67) 
#print(p1.name)
   
#class employe:
   # def __init__(self,name,id):
  #      self.name = name
 #       self.id = id
#p1 = employe("amar", 20)
#print(p1.name)
#print(p1.id)    
    
#class employe:
    #def __init__(self,name,id):
    #    self.name = name
   #     self.id = id
  #       return f"{self.name}({self.id})"
#p1 = employe("amar",67)
#print(p1.name)
#print(p1.id)

class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def myfunc(self):
        print("my name is "+ self.name)
p1 = employee("amar",887)
print(p1.name)
print(p1.id)
