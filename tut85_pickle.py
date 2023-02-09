import pickle
# pickling a oythin module
cars=["audi","bmw","maruthi","tata"]
file="mycar.pkl"
fileobj=open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close()


#import pickle module
file="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))

## pickle.loads()