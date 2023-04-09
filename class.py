class Person:
    name="Shreejith"
    occupation ="Hacker"
    networth="10$"
    def info(self):
        print(f'{self.name}is a {self.occupation}')
    
a= Person()
b=Person()
c=Person()
a.name="Subham"
a.occupation="Software Dev"
a.networth="100$"
#print(a.name,a.occupation)
a.info()
# self is an object om which it is called
b.name ="Sruti"
b.occupation="Accountant"
b.occupation="1$"
b.info()
c.info()