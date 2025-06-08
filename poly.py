class car:
    def __init__(self, carname, year):
        self.carname = carname
        self.year = year
        pass
    def move(self):
        print("drive")
class bloat:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
        pass        
    def move (self):
        print("drive")
class fly:
    def __init__(self,flybrand,manufacture):
        self.flybrand = flybrand
        self.manufacture = manufacture
        pass        
    def move(self):
        print("drive")
car1 = car("kiya","2005")
bloat1 = bloat("lyer","2004")
fly1 = fly("airindia","1995")

for x in (car1, bloat1,fly1):
    x.move()


class home:
    def __init__(self,masterroom,singleroom):
        self.masterroom = masterroom
        self.singleroom =singleroom
        pass
    def keys(self):
        print("masterroom keys")
class kitechen(home):
    pass    
class washroom(home):
    pass  
    def keys(self):
        print("room")
myhome = home("sweethome","beatiful home")
washrooms = washroom("kaveri water","mysoresandle soap") 
for x in (myhome,washrooms):
    print(x.masterroom)
    print(x.singleroom) 
    x.keys()


set1 ={"111","3232","324","111"}
print(set1)

set ={"apple","banna","cherry"}
for x in set:
    print(x)

set ={"apple","banana","cherry"}
set1 = {"apple","mango","cherry"}
set3 = set.difference(set1)
print(set3)

set = {1,2,3,4,5,5}
set1 ={3,21,34,45,65,63}

set3 = set.union(set1)
print(set3)

set = {12,32,43,54,56,67}
set1 = {21,32,43,54,76,7,87}
set3 = set.intersection(set1)
print(set3)

set  ={23,43,54,65,76,87}
set1 = {32,23,43,54,76,78}
set3 = set.symmetric_difference(set1)
print(set3)

set1 ={1,2,34,45,65,87,}
set2 = {32,54,65,76,1,2,56,76}
set3 = set1.symmetric_difference(set2)
print(set3)

#find the uinon
set1 ={1,2,3,43,54,5}
set2 ={21,34,54,56,76}
set3 = set1.union(set2)
print(set3)

#find the intersection
set1 ={12,3,43,56,65}
set2 = {23,4,43,12,65,24}
set3 = set1.intersection(set2)
print(set3)

#find the differnce
set1 = {23,43,54,56,78,8}
set2 = {32,23,45,65,67,56}
set3 = set1.difference(set2)
print(set3)

#ffind the symmtric differnce
set1 = {21,43,45,56,76,87}
set2 ={12,21,42,45,56,79,0}
set3 =set1.symmetric_difference(set2)
print(set3)

#all the common elements between three sets
set1 ={1,2,3,4,5,6,76,7}
set2 = {21,32,43,54,65,2,3,4}
set3 = {21,32,43,4,5,65,76}

set4 = set1.intersection(set2,set3)
print(set4)

# remove all elements of one set
set1 ={12,32,43,54,15,56}
set2 ={21,12,43,45,65,76 }
set3= set1.difference_update(set2)
print(set3)

thisdic = {
    "brand" :"kiya",
    "year":2005,
    "manufacture":1999

}
x= thisdic.get("brand")
print(x)

    