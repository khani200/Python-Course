class employee:
    raise_val=1.09

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+"."+last+"@smme.com"
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    def payrise(self):
        return int(self.pay*employee.raise_val)# it is same as return int(self.pay*self.raise_val)

emp_1=employee("Ali","Haider",9500)
emp_2=employee("Daud","Iqbal",10000)

'''print(emp_1.fullname())
employee.fullname(emp_1)#it works like same as the line above

print(emp_1.email)
print(emp_2.fullname())
print(emp_2.email)'''

print(emp_1.pay)
print(emp_1.payrise())