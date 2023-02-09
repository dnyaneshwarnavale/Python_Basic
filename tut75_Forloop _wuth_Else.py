## for loop with else
khana=["chicken","butter chicken","Roti","chawal"]
for item in khana:
    print(item)
    #break

else:
    print("This for loop ended properly")


for items in khana:
    if items=="paratha":
        break

else:
    print("This for loop ended properly")