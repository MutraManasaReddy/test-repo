class Person:
    def __init__(self,name,color,height):
        self.name = "name",
        self.color = "color",
        self.height ="height"
        pass
    def to_dict(self):
        return{
         "name":self.name,
        "color":self.color,
        "height":self.height
        }
    def __str__(self):
        return f"Person(name={self.name},color= {self.color},height={self.height})"
        pass 

list_of_person =[]

# 1. add method
def add_person(name:str,color:str,height:float):
    person = Person(name,color,height)
    list_of_person.append(person)
    return list_of_person

# 2. show all
def list_person():
    return list_of_person

#3. get method
def get_person(name:str):
    for person in list_of_person:
        if person.name == name:
            return list_of_person

# 4.update method
def update_person(name:str,color:str=None,height:float=None):
    for person in list_of_person:
        if person.name == name:
            if color:
                Person.color = color
                if height is not None:
                    Person.height = height
                    return Person
                return None
    
# 5. remove method
def remove_person(name:str):
    Person = get_person(name)
    if Person is None:
        return None
    list_of_person.remove(name)
    return Person

print(add_person("manasa","white",5.4))
print(add_person("manu","black",5.5))
print(list_person())
print(get_person("manasa"))
print(update_person("manasa",color="white"))
print(update_person("manu",color="black"))
print(list_person)
print(remove_person("removing person with name "))
print(remove_person("manasa"))
print(list_person())    
                  


        