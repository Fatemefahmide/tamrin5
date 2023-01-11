class Time:
    def __init__(self,h,m,s):
        self.h=h
        self.m=m
        self.s=s

    def show(self):
        print(self.h,":",self.m,":",self.s)


    def sub(self,t2):
        result=Time(None, None, None)
        result.h =self.h - t2.h
        result.m =self.m - t2.m
        result.s =self.s - t2.s

        if result.s < 0 :
            result.s += 60
            result.m -= 1

        if result.m < 60 :
            result.m += 60
            result.h -= 1

        return result


time1= Time(10, 20, 25)
time1.show()
time2= Time(8, 30, 40)
time2.show()


m = time1.sub(time2)
print("sub: ")
m.show()
