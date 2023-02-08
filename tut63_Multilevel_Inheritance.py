class Dad:
    basketball=1

class Son(Dad):
    dance=1
    def isdance(self):
        return f"Yes I dance{self.dance} no of times"

class Grandson(Son):
    dance=5
    def isdance(self):
        return f"Yes I dance{self.dance} no of times"

darry=Dad()
larry=Son()
Harry=Grandson()

print (Harry.isdance())
print (Harry.basketball)