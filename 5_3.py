class Date:
    def __init__(self,y,m,d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        print(self.y , "/" , self.m , "/" , self.d)


    def add(self,date2):
        result=Date(None, None, None)
        result.y= self.y + date2.y
        result.m = self.m +date2.m
        result.d = self.d + date2.d

        if result.d >= 30:
            result.d -= 30
            result.m += 1

        if result.m >= 12:
            result.m -= 12
            result.y += 1

        return result


        def sub(self,date2):
          result=Date(None, None, None)
          result.y= self.y - date2.y
          result.m = self.m - date2.m
          result.d = self.d - date2.d

        if result.d <0 :
            result.d += 30
            result.m -= 1

        if result.m < 12:
            result.m += 12
            result.y -= 1

        return result


date1 = Date(1383, 5, 3)
date2 = Date(1401, 10, 10)


print("date1: ")
date1.show()

print("date2: ")
date2.show()

a= date1.add(date2)
print("add: ")
a.show()

s= date1.sub(date2)
print("sub: ")
s.show()



