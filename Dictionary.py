#thisdic = {
   # "brand": "philips",
  #  "manufacture":"2005",
 #   "warinty":"2years"
#}
#print(thisdic)    ----------------------------print dictionary key:values


#thisdic = {
   # "brand" : "electric",
  #  "manufacture":"2004",
 #   "warinty" :"3years"

#}
#print(thisdic["brand"])     -----------------------print brand value

#thisdic = {
    #"brand" : "wood",
   # "manufacture" : "tables",
  #  "warinty" :"10 years",
 #   "warinty" :"10 years"
#}
#print(thisdic)         -----------------------------duplicated values not allowed 

#thisdic ={
   # "brand" : "wood",
  #  "manufacture" : "tables",
 #   "warinty" :  "20years"

#}
#x = thisdic["warinty"]
#print(x)        --------------------------------acees the item

#thisdic = {
   # "brand":"wood",
  #  "manufacture" : "tables",
 #   "warnty" :"10 years"

#}
#x = thisdic.get("warnty")
#print(x)          ---------------------------get values

#thisdic  ={
 #   "brand":"wood",
#    "manufacture" : "tables",
 #   "warinty" :"20 years"
#}
#x = thisdic.keys()
#print(x)               --------------------------key values


#thisdic = {
   # "brand": "wood",
  #  "manufacture" : "tables",
 #   "warinty"  :"30years"

#}
#x = thisdic.keys()
#print(x)
#thisdic["color"] = "white"
#print(x)                -----------------------------add item with key()

#thisdic = {
   # "brand":"wood",
  #  "manufacture":"tables",
 #   "warnty": "20 years"
#}
#thisdic["warnty"]="2 years"
#print(thisdic)     --------------------------------change values


#thisdic = {
   # "brand":"wood",
  #  "manufacture":"tables",
 #   "warnty" :"30 years"
#}
#thisdic.update({"brand":"plates"})
#print(thisdic)       -----------------------------update Value

thisdic = {
    "brand":"wood",
    "manufacture":"tables",
    "warnty":"3years"
}
thisdic["color"]="red"
print(thisdic)   

#thisdic ={
   # "brand":"wood",
  #  "manufacture":"tables",
 #   "warnty":"1year"
#}
#thisdic.pop("manufacture")
#print(thisdic)         --------------------------------remove item

#thisdic  ={
   # "brand":"wood",
  #  "manufacture":"tables",
 #   "warnty":"2 years"

#}
#for x in thisdic:
    #print(x)               -------------------forloop
#for x in thisdic:
    #print(thisdic[x])     ----------------forloop
#for x in thisdic.keys():
    #print(x)
#for x in thisdic.values():
    #print(x)

#thisdic ={
   # "brand":"wood",
  #  "manufacture":"tables",
 #   "warnty":"2 years"
#}    
#mydic = thisdic.copy()
#print(thisdic)
