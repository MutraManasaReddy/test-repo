#class myclass:
 #   x = 5
#print(myclass)     -------- class   

#class  MyClass():
 #   x = 5
#p1 = MyClass()
#print(p1.x)          ----------------create object

#class person:
   # def __init__(self,name,age):
  #      self.name ="manasa"
 #       self.age = 26
#p1 = person("manasa",26)
#print(p1.name)
#print(p1.age)
        
#class person:
   # def __init__(self,namee,age):
  #      self.name  ="manas"
 #       self.age = 25
#p1 = person("manas",25)
#print(p1.name)
#print(p1.age)


class person:
    def __str__(self,name,age):
        self.name = name
        self.age = age
p1 = person("manasa",21)
print(p1)
       

