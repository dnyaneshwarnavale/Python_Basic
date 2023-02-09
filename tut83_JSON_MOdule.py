import json

data='{"var1":"harry","var2":56}'
parsed=json.loads(data)
print(parsed)
print(parsed['var1'])

## json.load
data2 ={
    "chaneel_name":"codewithharry",
    "cars":['bmw','audi'],
    "fridge":('roti','chicken')
}
jscomp=json.dumps(data2)  # convert into JSOn format
print(jscomp)