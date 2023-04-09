class Employee:
 def __init__(self,name,id):
        self.name=name
        self.id=id
 def showDetails(self):
        print(f"The name of the Employee is {self.id} is {self.name}")

class Progranmer(Employee):
    def showLanguages(self):
        print("The defauolt language is Python")
        
e1=Progranmer("HARRY","100023")
e1.showDetails()
e1.showLanguages()
