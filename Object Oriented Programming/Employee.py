class Employee:
    raise_amount=1.4
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay

    @classmethod
    def raise_amount_change(cls, amount):
        cls.raise_amount=amount

    def raise_pay(self):
        self.pay*=Employee.raise_amount

    @staticmethod
    def just_say_hi():
        print "Hi"
        Employee.raise_amount=1.6



emp_1= Employee("Jigna", "Reshamwala", 4000)

print emp_1.pay
emp_1.raise_pay()
print emp_1.pay
Employee.raise_amount_change(2)




emp_1.raise_pay()
print emp_1.pay

Employee.just_say_hi()
emp_1.raise_pay()
print emp_1.pay

