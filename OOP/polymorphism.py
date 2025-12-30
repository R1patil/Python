#function name is same 
#1)compile time-polymorphism 2) Run time polymorphism
#Method Overloading
"""Method overloading allows a class to have methods with same name but differnt parameters enbling flexibilytu in how methods are called and used within the class"""
#default Argument Method
class MathOperatio:
    def add(self,a,b=0,c=0):
        return a+b+c
    
obj=MathOperatio()
print(obj.add(5))
print(obj.add(3,4))

# in the Method Overloading we have 2 types 
'''  Default Argument assign the default value should be first '''
''' Using Keyword Argument upto to user input as possile'''
# Keyword Arguments
class Keywordclass:
    def add(self,*args):
        return sum(args)
ans=Keywordclass
print(ans.add(5,10))
print(ans.add(1,2,3,4,5,6,7))

# Operator Overloading in that method we are not defined with __(double underscores )
#MAgic method 
class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y

    def __add__(self,other):
        '''Overloading the opertor'''
        return Vector(self.x+other.x,self.y+other.y)
    
    def __sub__(self,another):
        return Vector(self.x-another.x,self.y-another.y)
    
    def __mul__(self,scalar):
        return Vector(self.x*scalar,self.y*scalar)
    
    def __str__(self):
        return f"Vector({self.x},{self.y})"
r1=Vector(3,4)
r2=Vector(2,4)

r3=r1+r2
r4=r1-r2
r5=r1*4

print(r3)
print(r4)
print(r5)
