import json
x = '{"name": "manasa","age":"26","place":"singaapore"}'
y = json.loads(x)
print(y["age"])

import json
x = '{"name":"manasa","place":"singapore"}'
y = json.loads(x)
print(y["place"])

import json
x ={
    "name" :"manasa",
    "plane":"indian",
    "age": 26
}
y= json.dumps(x)
print(y)

import json
x = {
    "name":"manu",
    "age":25,

}
y = json.dumps(x)
print(y)

import json

print(json.dumps({"name":"manasa","age":"26"}))
print(json.dumps(["apple","banana"]))
print(json.dumps(("apple","banana")))
print(json.dumps("manasa"))
print(json.dumps(10))
print(json.dumps(10.5))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

