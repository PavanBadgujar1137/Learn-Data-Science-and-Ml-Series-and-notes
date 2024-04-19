# JSON is a syntax for storing and exchanging the data, it is text which is written with javascript object notation

# converting from JSON to python
import json
x = '{"name": "Pavan","age":39,"city":"Jalgaon"}'

y=json.loads(x)


# The result will be in python dictionary
print(y["age"])

# converting from python to json
import json
x = {"name": "Pavan","age":39,"city":"Jalgaon"}
# converting into json
y=json.dumps(x)

# the result will be in string
print(y)

# you can covert the following object to json strings:
# dict , list , tuples, int ,float, true,flase,none

import json
print(json.dumps({"name":"pavan", "age":36}))
print(json.dumps(["apple","banana"]))
print(json.dumps(("sharad", "Patil")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(13.4))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

# Whe you convert python to json than python objects are converted into the javasceript object
import json
x= {"name":"Pavan","age":"34", "married":True,"divoced":False , "childer":("lichi","chicku"),"pets":None, "cars":[{"model":"bmw 230", "mog":22.5},{"model":"ford echo", "mpg":24.1}]}   

# converting into the json
y=json.dumps(x)
print(y)

# how to format the result
x= {"name":"Pavan","age":"34", "married":True,"divoced":False , "childer":("lichi","chicku"),"pets":None, "cars":[{"model":"bmw 230", "mog":22.5},{"model":"ford echo", "mpg":24.1}]}   
# using the 4 indets to make it easier to read
print(json.dumps(x, indent=4))

# you can also define the seperators meaning comma , colon anad space
x= {"name":"Pavan","age":"34", "married":True,"divoced":False , "childer":("lichi","chicku"),"pets":None, "cars":[{"model":"bmw 230", "mog":22.5},{"model":"ford echo", "mpg":24.1}]}   

print(json.dumps(x,indent=4, separators=(". ", " = ")))

# also you can get the result in specified order
x= {"name":"Pavan","age":"34", "married":True,"divoced":False , "childer":("lichi","chicku"),"pets":None, "cars":[{"model":"bmw 230", "mog":22.5},{"model":"ford echo", "mpg":24.1}]}   
print(json.dumps(x,indent=4,separators=(". ","= "),sort_keys=True))