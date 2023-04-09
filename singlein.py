class Parent:
    def fu1(self):
        print("parent class.")

 
 
class Child(Parent):
    def fu(self):
        print(" child class.")
 
 

o = Child()
o.fu1()
o.fu()