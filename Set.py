#fruit = {"apple","banana","cherry","orange"}
#print(fruit)   -----------------------print the items

fruit = {"apple","banana","orange","mango","apple"}
print(fruit)   

#fruit = {"apple","mango","orange","kiwi"}
#print(len(fruit)) -------------------length


#fruit = {"apple","banana","cherry","orange","true" , 1,2,}
#print(fruit)  -------------
#fruit= set(("apple","banana","cherry"))
#print(fruit)   -------------------------set constructor

#fruit = {"apple","banana","cherry"}
#print(type(fruit))   -------------------data types

#fruit ={"apple","banana","cherry","orange"}
#vegies = {"tomato","beans",}
#fruit.update(vegies)
#print(fruit)  ----------------------updates items

#fruit  = {"apple","banana","cherry"}
#fruit.add("orange")
#print(fruit)   ---------------------------add items

#fruit ={"apple","banana","cherry"}
#fruit.remove("banana")
#print(fruit) --------------------------remove items

#fruit ={"apple","orange","mango","banana"}
#fruit.discard("banana")
#print(fruit)     ------------------discard item

#fruit = {"apple","banana","mango","orange",}
#fruit.clear()
#print(fruit)      --------------------clear item   output =  set()

#fruit = {"apple","banana","orange","mango"} 
#del fruit
#print (fruit)


#fruit = {"apple","mango","banana"}
#for x in fruit:
    #print(fruit)   -------forloop


#set1 = {"aa","bb","cc"}
#set2 = {"1","2","3"}
#set = set1.union(set2)
#print(set) -------------------union method

#set1 = {"aa","bb","cc"}
#set2 = {"1","2","3"}
#set = set1|set2
#print(set)
        
#set1 = {"aa","bb","c"}
#set2 = {"1","2","3"}
#set3 = {"ab","abc","abcd"}
#set = set1.union(set2,set3)
#print(set)    -----------------------multipule union methods 


#set1 ={"A","b","c"}
#set2 ={"1","2","3"}
#set1.update(set2)
#print(set1)  -----------------------------update method

#set1 ={"aaa","bbb","ccc"}
#set2 = {"aaa","bbb","ccc","ddd"}
#set = set1.intersection(set2)
#print(set)          ------------------------Intersection method

#set1 ={"aa","bb","cc"}
#set2 = {"aa","bb","cc","dd"}
#set = set1&set2
#print(set)

#set1  = {"aaa","bbb","ccc"}
#set2 = {"aaa","ccc","ddd"}
#set = set1.difference(set2)
#print(set)            --------------------------difference method


#set1 = {"aaa","bbb","ccc","eee"}
#set2 = {"aaa","bbb","ccc","Ddd"}
#set = set1.difference_update(set2)
#print(set)        -----------------------------difference_update

#set1 ={"aaa","bbb","ccc"}
#set2 = {"aaa","ccc","ddd","eee"}
#set = set1.symmetric_difference(set2)
#print(set)          -----------------------------symmetric _difference


set1 ={"aaa","bbb","ccc"}
set2 = {"aaa","nnn","xxx"}
set = set1^(set2)
print(set)