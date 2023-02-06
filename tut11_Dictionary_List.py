#dictionary is nothing but key-value pairs
d1 ={}  # dictionay declartion
print(type(d1)) # simple print whole dictionary

d2={"Pune":"Narhe",
    "Solapur":"Sangola"}
print(d2["Pune"]) ## print dict

# dicitonary within dictionary
d3={"Pune":"Narhe",
    "Solapur":"Sangola",
    "Mumbai":{
        "east":"Andheri",
        "south":"KP"
    }}
d3["Kol"]="Rankla"  # add new item in dict
d3[100]="Pandhrpur"

print(d3)
print(d3["Mumbai"])
print(d3["Mumbai"]["south"])

#dictionary built in function
print(d3.copy())

d4={}
d4=d3
print(d4)

print(d3.keys()) # dictionary key function


