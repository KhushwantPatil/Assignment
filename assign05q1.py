
class Powerofnum :
    def __init__(self,num,ponum):
        self.num = num
        self.ponum = ponum
    def pow(self,num,ponum):
         if ponum==1:
            return 1
         else:
            print(num*pow(num,ponum-1))

a = Powerofnum(10,2)
a.pow(10,2)
