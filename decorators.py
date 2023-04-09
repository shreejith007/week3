
 
def greet(fx):
    def mfx(*args, **kwargs):          #modified fx
     print("Good morning")
     fx(*args,**kwargs)
     print("Thank u for using this function")
    return mfx
@greet
def hello():
    print("Hello world")
def add(a,b):
    print(a+b)
    
hello()
#greet(add)(1,12)
add(1,2)