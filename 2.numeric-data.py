print("Python has three numeric types: int, float, and complex")


def repetitive_task(myValue):
    print(type(myValue))
    print(str(myValue))
    print(str(myValue) + " is of the data type " + str(type(myValue)))
    
myValue=1
print(myValue)
print(type(myValue))
print(str(myValue))


myValue=3.14
print(myValue)
print(type(myValue))
print(str(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=5j
repetitive_task(myValue)

myValue=True
repetitive_task(myValue)

myValue=False
repetitive_task(myValue)