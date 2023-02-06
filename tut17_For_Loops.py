###### FOR LOOP #############

list1 =["aa","bb","cc","dd","ee"]
for item in list1:
    print(item)

list2 = [["aa",1], ["bb",2], ["cc",3], ["dd",4], ["ee",5]]
for item, numcount in list2:
    print(item,numcount)
    #print(item,"number count is", numcount)

dict1=dict(list2)
for item, numcount in dict1.items():
    print(item,numcount)


####### WHile Loop  ##############

