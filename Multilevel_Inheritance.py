class GrandParent:
    def __init__(self,gname):
        self.gname = gname
        print(f"I'm he grandparent & my name is {self.gname}")

class Parent(GrandParent):
    def __init__(self,pname,gname): 
        super().__init__(gname)
        self.pname = pname
        print(f"I'm the sone of {self.gname} & my name is {self.pname}")

class Child(Parent):
    def __init__(self,cname,gname,pname):
        super().__init__(pname, gname)
        self.cname = cname
        print(f"I'm the grandchild of {self.gname} & child of {self.pname}. My name is {self.cname}")


c = Child("Shubhi","Ram","Anju")
