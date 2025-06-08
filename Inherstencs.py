#class person:
 #   def __init__(self,fname,lnmae):
  #      self.fname = fname
   #     self.lname = lnmae
    #def myfunc(self):
     #   print(self.fname,self.lname) 
#class student(person):
 #       def __init__(self, fname, lnmae):
  #           super().__init__(fname, lnmae)
#x = student("mutra", "manasa")
#print(x.fname,x.lname)

#class person:
 #    def __init__(self,fname,lname):
  #        self.fname = fname
   #       self.lname = lname
    # def myunc(self):
     #     return("self.fname","self.lname")
#class student(person):
 #   def __init__(self, fname, lname):
  #        super().__init__(fname, lname)
   #       self.finalyear = 2019
#x = student("mutra","manasa") 
#print(x.finalyear)   

#class student:
   #  def __init__(self,name ,rollno):
    #      self.name = name
   #       self.rollno = rollno
  #   def student(person):
 #         print(person.name,person.rollno)
#class students(student):
     #     def __init__(self, fname, lname, year):
    #           super().__init__(fname, lname)
   #            self.year = "year"
  #        def welcome(self):
 #                   print("welcome to the singapore",self.fname,self.lname,self.year)
#x = students ("mutra","manasaa",2019)
#print(x.fname,x.lname,x.year)

#x = 3.7
#y = 3

#a = float(y)
#b = int(x)
 
#print(a)
#print(b)

#age = input("enter your age")
#print("your are"+age+"years old")

#list = ["green","blue","yellow"]
#print(list[1])

#list = [1,2,3]
#list[1] = 5
#print(list)     


#fruits = ("apple", "banana", "cherry")
#fruits[1] = "orange"
 #TypeError : tuple object does not support item assignment

class person:
    def __init__(self,name,age):
        self.naame = name
        self.age = age
p1 =person("manasa",25) 
print(p1.naame)
print(p1.age)

class person:
    def __init__(self,name ,id):
        self.name = name
        self.id = id
    def __str__(self):
         return "{self.name}({self.id})"     
p1 = person("manasa",10)
print(p1.name)
print(p1.id)
         

class person:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def myfunc(self):
        print("hello wolrd"+ self.name)
p1 =person("manasa",20)
print(p1.name)
print(p1.rollno)     

class person:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def myfunc (self):
        print(self.name,self.id)
class student (person):
        def __init__(self, name, id):
            super().__init__(name, id)
x = student("manasa",29)
print(x.name) 
print(x.id)


class person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
    def printname(self):
        print(self.fname,self.lname) 
class student (person):           
        pass
x = student("mutra","manasa")
x.printname()

class person:
     def __init__(self,fname,lname):
          self.fname = fname
          self.lname = lname
     def printname(self):
          print(self.fname,self.lname)
class student(person) :
    def __init__(self, fname, lname):
         person.__init__(self,fname, lname)
x = student("mutra","manasa")
x.printname()


           