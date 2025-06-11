class ElectricItems:
    def __init__(self,name:str,brand:str,warranty:str):
        self.name = "name",
        self.brand = "brand",
        self.warranty ="warranty"
        pass
    def __str__(self):
        return f"ElectricItems(name ={self.name},brand = {self.brand},warranty = {self.warranty})"
        pass 
    def to_dict(self):
        return {
            "name":self.name,
            "brand":self.brand,
            "warranty":self.warranty
        }
list_of_electricitems =[]


# 1. added method
def add_electricitem(name:str,brand:str,warranty:str):
    electricitems = ElectricItems(name,brand,warranty)
    list_of_electricitems.append(name)
    return list_of_electricitems

# 2. show all list of electricitems
def list_items():
    return list_of_electricitems

# 3. get the item by brand
def get_items(warranty:str):
    for electricitems in list_of_electricitems:
        if warranty == warranty:
            return electricitems
        return None
    
# 4. updated method
def update_items(warranty:str,name:str=None,brand:str=None):
    for electricitems in list_of_electricitems:
    #electricitems = get_items(warranty)
        if electricitems is None:
            #return None
    #if name is not None:
        #electricitems.name = name
          if brand:
             electricitems.brand = brand
             return electricitems
    return" items not found" 

# 5.remove method
def remove_item(warranty:str):
    electricitems = get_items(warranty)
    if electricitems is None:
        return None
    return electricitems

print(add_electricitem("hairdryer","philips","2 years"))
print(add_electricitem("microwave","panasonic","5 years"))
print(list_items())
print(get_items("2 years"))
print(update_items("2years",brand="philips"))
print(update_items("5 years",brand="panasonic"))
print(remove_item("removing electricitems with warranty 2 years" ))
print(remove_item("2 years"))

    

    
    




    