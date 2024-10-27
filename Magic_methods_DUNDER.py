class Employee:
    name = "shubhi"
    def __len__(self):
        i=0
        for c in self.name:
            i = i + 1
        return i
    def __str__(self):
        return f"The name of employee is {self.name}"
    def __repr__(self):
        return f"The name of employee is {self.name}"
    def __call__(self):
        print("Used to execute e() i.e. e as a function")

e = Employee()
print(e)    # due to __str__ method
print(len(e))
e()