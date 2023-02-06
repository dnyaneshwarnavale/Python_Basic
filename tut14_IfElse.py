
# Example file for working with conditional statement
var1 =6
var2 =56

print("enter value for compare:")
var3= int(input())
if var3>var2:
 print("Value is Greater")
else:
 print("Value is Lesser")


# second example
print("Enter value shipping:")
total = int(input())
country = "US"
country = "AU"
if country == "US":
    if total <= 50:
        print("Shipping Cost is  $50")
    elif total <= 100:
        print("Shipping Cost is $25")
    elif total <= 150:
	    print("Shipping Costs $5")
    else:
        print("FREE - Inside If .. else block")
else:
    print("FREE- outside the main If condtion")

#from list
list1=[1,2,3]
if 2 in list1:
    print("yes, its in list")

