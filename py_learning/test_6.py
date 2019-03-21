class thing():
    pass

example = thing()

print(thing)
print(example)
class Thing_2():
    letter = 'abc'

print(Thing_2.letter)
class Thing_3():
    def __init__(self):
        self.letter = 'xyz'

aa = Thing_3()

print(aa.letter)

class Element():
    def __init__(self,name,symbol,number):
        self.name = 'hydrogen'
        self.symbol = 'H'   
        self.number = 1
