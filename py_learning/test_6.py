import json

class thing():
    pass

example = thing()
print("-----------------------------------------------")
print("6.1:")
print(thing)
print(example)
print("-----------------------------------------------")
print("6.2:")
class Thing_2():
    letter = 'abc'

print(Thing_2.letter)
print("-----------------------------------------------")
print("6.3:")
class Thing_3():
    def __init__(self):
        self.letter = 'xyz'

aa = Thing_3()

print(aa.letter)
print("-----------------------------------------------")
print("6.4:")
class Element():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol  
        self.number = number
    def dump(self):
        print(self.name,self.symbol,self.number)
    def __str__(self):   # 定義物件的字串描述
        return str(self.name) + '/' + str(self.symbol) +'/'+ str(self.number)
    def get_name(self):
        print("Inside the getter.")
        return self.name
    def get_symbol(self):
        print("Inside the getter.")
        return self.symbol
    def get_number(self):
        print("Inside the getter.")
        return self.number
hydrogen = Element("hydrogen","H",1)
print(hydrogen.name)
print(hydrogen.symbol)
print(hydrogen.number)
print("-----------------------------------------------")
print("6.5:")
e2f = {"name": 'hydrogen', "symbol": 'H', "number": 1}
#hydrogen = Element(e2f["name"],e2f["symbol"],e2f["number"])
hydrogen = Element(**e2f)
print(hydrogen.name)
print("-----------------------------------------------")
print("6.6:")
class Element_2():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol  
        self.number = number
    def dump(self):
        print(self.name,self.symbol,self.number)

hydrogen = Element_2(**e2f)
hydrogen.dump()

print("-----------------------------------------------")
print("6.7:")
class Element_3():
    def __init__(self,name,symbol,number):
        self.name = name
        self.symbol = symbol  
        self.number = number
    def dump(self):
        print(self.name,self.symbol,self.number)
    def __str__(self):   # 定義物件的字串描述
        return str(self.name) + '/' + str(self.symbol) +'/'+ str(self.number)
print(hydrogen)
hydrogen = Element_3(**e2f)
hydrogen.__str__()
print("-----------------------------------------------")
print("6.8:")
print(Element.get_name,Element.get_symbol,Element.get_number)
print("-----------------------------------------------")
print("6.9:")
class Bear():
    def __init__(self,eats):
        self.eats = eats
    def eat(self):
        return(self.eats)
class Rabbit():
    def __init__(self,eats):
        self.eats = eats
    def eat(self):
        return(self.eats)
class Octothorpe():
    def __init__(self,eats):
        self.eats = eats
    def eat(self):
        return(self.eats)
B = Bear('berries')
print(B.eat())
R = Bear('clover')
print(R.eat())
O = Bear('campers')
print(O.eat())
print("-----------------------------------------------")
print("6.10:")
class Laser():
    def __init__(self,tool1):
        self.tool1 = tool1
    def does(self):
        return(self.tool1)
class Claw():
    def __init__(self,tool2):
        self.tool2 = tool2
    def does(self):
        return(self.tool2)
class SmartPhone():
    def __init__(self,tool3):
        self.tool3 = tool3
    def does(self):
        return(self.tool3)
class Robot():
    def __init__(self,robot1,robot2,robot3):
        self.robot1 = robot1
        self.robot2 = robot2
        self.robot3 = robot3
    def does(self):
        print(self.robot1.tool1,' ',self.robot2.tool2,' ',self.robot3.tool3) 
L = Laser('distegrate')
R = Claw('crush')
S = SmartPhone('ring')
print(L.does())
print(R.does())
print(S.does())
rob = Robot(L,R,S)
print(rob.does())