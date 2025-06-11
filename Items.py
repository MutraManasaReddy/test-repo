class Items:
    def __init__(self,name:str,color:str,kgs:int):
        self.name = "name",
        self.color = "color",
        self.kgs = "kgs"
        pass
    def __str__(self):
        return f"Items(name={self.name},color={self.color},kgs={self.kgs})"
        pass

list_of_items =[]
 
# 1. added method
def add_items(name:str,color:str,kgs:int):
    items = Items(name,color,kgs)
    list_of_items.append(items)
    return list_of_items

# 2. show all list of items method
def list_items():
        return list_of_items

# 3. get a item by its color method
def get_items(color:str):
    for items in list_of_items:
        if color == color:
            return items
        return items
    
# 4. updated method
def update_items(color=str,name=None,kgs=None):
    items =get_items(color)
    if items is None:
        return None
    if name is not None:
        items.name = name
    if kgs is not None:
        items.kgs = kgs
        return items

# 5. remove method    
def remove_items(color:str):
    items = get_items(color)
    if items is None:
        return None
    list_of_items.remove(items)
    return(items)


print(add_items("beans","green",5))
print(add_items("redchelli","red",10))
print(list_items())
print(get_items("green"))

print(update_items("green",kgs=5))
print(update_items("redchelli",kgs=10))
print(list_items())

print("removing items with color green")
print(remove_items("green"))
print(list_items())


    
    

