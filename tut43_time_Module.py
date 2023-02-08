import time

initial =time.time()
print(initial)
k=0

print("While strat:",time.time())
while(k<45):
    print("This is while loop")
    k+=1
print("Total time took While Loop",time.time()-initial)

initial2=time.time()
for i in range(45):
    print("THis is for loop")
print("Total time took For loop",time.time()-initial2)

localtime=time.asctime() ## convert into local time
print(localtime)
