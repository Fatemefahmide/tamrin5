class fraction:
    def __init__(self,s,m):
        self.soorat = s
        self.maKhraj = m

        def show(self):
            print(self.soorat ,"/", self.makhraj)

        def sum(self,f2):
            result=fraction(None, None)
            result.soorat=self.soorat*f2.maKhraj + f2.soorat*self.maKhraj
            result.maKhraj=self.maKhraj*f2.maKhraj
            return result

        def sub(self,f2):
            result=fraction(None, None)
            result.soorat=self.soorat*f2.maKhraj - f2.soorat*self.maKhraj
            result.maKhraj=self.maKhraj*f2.maKhraj
            return result

        def div(self,f2):
            result=fraction(None,None)
            result.soorat=self.soorat*f2.maKhraj
            result.maKhraj=self.maKhraj*f2.soorat
            return result


fraction1 = fraction(2,3)
print("f1: ")
fraction1.show()

fraction2 = fraction(3, 4)
print("f2: ")
fraction2.show()

sum=fraction2.sum(fraction1)
print("sum: ")
sum.show()

sub=fraction2.sub(fraction1)
print("sub: ")
sub.show()

div=fraction2.div(fraction1)
print("div: ")
div.show()