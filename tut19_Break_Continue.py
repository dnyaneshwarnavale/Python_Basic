i=0
while (True):
    print(i,end=" ")
    if (i==5):
        break # stop the loop
    i=i+1


    ## continue
    i = 0
    while (True):
        if i+1<5:
            i=i+1
            continue
        print(i+1)
        if (i == 5):
            break  # stop the loop
        i = i + 1

