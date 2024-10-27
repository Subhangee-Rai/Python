class Vidyarthi:
    # here 'a' is a class variable, and if instance variable is not found then this will be printed
    a = 100
    def __init__(self, name):
        self.name = name
        # here money is an instance variable
        self.money = 100
    def display(self):
        print(f"Money left with {self.name} is {self.money} and he should get Rs {self.a}")


# Without giving instance variable value
s1 = Vidyarthi("Rohan")
s1.display()

# giving instance variable values
s2 = Vidyarthi("Sohan")
s2.money = 50
s2.a = 200
s2.display()

# but giving the value will not change the class variable value
print(f"The value of class variable a is: {Vidyarthi.a}")