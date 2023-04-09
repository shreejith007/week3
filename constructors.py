class Person:
    
 def __init__(self,name,oc) : ## init is used for constructor 
        print("HELLO")
        self.name = name
        self.occ = oc
    
 def info(self):
    print(f"{self.name} is a {self.occ}")
    
    
    
a = Person("harry","Developer")
b=Person("Anonoumous","HACKER")
a.info()
b.info()
