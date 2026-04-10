class parent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def intro(self):
        return f"the child name is {self.name} and its age is {self.age}"
a=parent("Shree", 21)
a.intro()    
b=parent("Sneha",23)
b.intro()


