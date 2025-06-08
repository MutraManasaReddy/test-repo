#x = lambda a : a+10
#print(x(5))         -------------------addition lambda

#x = lambda a, b : a* b
#print(x(5,2))         -------------------- multiplication lambda

#x = lambda a,b,c : a*b*c
#print(x(5,2,3))       ------------------multiplication three arguments 

#def myfunc(n):
 #   return lambda a: a*n
#mydoubler = myfunc(2)
#print(mydoubler(10))    

#def myfunc(n):
 #   return lambda a : a * n
#mydoubler = myfunc(2)
#print(mydoubler(20))

def myfunc(n):
    return lambda a :a*n
mydouble = myfunc(2)
mydouble = myfunc(2)
print(mydouble(10))
print(mydouble(20))
 
