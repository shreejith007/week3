class Myclass:
    def __init__(self,value):
        self.value=value 
    def show(self):
        print(f"value is{self.value}")
    @property
    def ten_value(self):   #getter
        return 10*self.value
    @ten_value.setter
    def ten_value(self,new_value):   ##setter
        self.value=new_value/10
obj=Myclass(10)
print(obj.ten_value)
obj.show()