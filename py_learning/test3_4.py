import numpy
###--------------------ch.3-------------------
years_list = [1996 ,1997 ,1998 ,1999 ,2000]
print("----------------ch3----------------------------")
print("3.1:",years_list)
print("-----------------------------------------------")
print("3.2:",years_list[2])
print("-----------------------------------------------")
print("3.3:",years_list[-1])
print("-----------------------------------------------")
thing = ["mozzarella" , "cinderella" ,"salmonella"]
print("3.4:",thing)
print("-----------------------------------------------")
print("3.5:",thing[1].capitalize())
print("-----------------------------------------------")
thing[0].capitalize()

thing[0] = thing[0].upper()

print("3.6:",thing)
print("-----------------------------------------------")
del thing[2]
print("3.7:",thing)
print("-----------------------------------------------")
surprise = ["Croucho","Chico","Harpo"]
print("3.8:",surprise)
print("-----------------------------------------------")

def reverse(str):
    out = '' 
    li = list(str)
    for i in range(len(li), 0, -1):
        out += ''.join(li[i-1])
    return out
surprise[2] =surprise[2].lower()
surprise[2] =reverse(surprise[2])
surprise[2]= surprise[2].capitalize()
print("3.9:",surprise)
print("-----------------------------------------------")
e2f = {"dog": 'chien', "cat": 'chat', "walrus": 'morse'}
print("3.10:",e2f)
print("-----------------------------------------------")
print("3.11:",e2f["walrus"])
print("-----------------------------------------------")

f2e = {v: k for k, v in e2f.items()}

print("3.12:",e2f.items())
print("-----------------------------------------------")
print("3.13:",f2e["chien"])

print("-----------------------------------------------")
print("3.14:",e2f.keys())
print("-----------------------------------------------")
life = {"animals": {'cats':["Henri","Grumpy","Lucy"],'octopi':None,'emus':None},"plants": None, "other": None,  } 

print("3.15:",life)
###--------------------ch.4------------------
print("-----------------ch4---------------------------")
guess_me = 7
print("4.1:")
if guess_me < 7 :
    print("too low")
elif guess_me >7:
    print("too high")
elif guess_me == 7:
    print("just righ")

print("-----------------------------------------------")
print("4.2:")
start = 1

while(1):
    if start < guess_me:
        print("too low")
    elif start == guess_me:
        print("found it")
        break
    elif start > guess_me:
        print("Oops!!")
        break
    start += 1
print("-----------------------------------------------")
num = [3,2,1,0]
for i in  range(len(num)):

    print("4.3:",num[i]) 
print("-----------------------------------------------")
number_list = [i for i in range(0,10) if i%2==0]
print("4.4:",number_list)
print("-----------------------------------------------")
word = 'squares'
letter_count = {letter:pow(word.count(letter),2) for letter in set(word)}
print("4.5:", letter_count)
print("-----------------------------------------------")
set1 = {number for number in range(10) if number%2 == 1}
print("4.6:", set1)
print("-----------------------------------------------")
def good():
    list_a = ['Harry','Ron','hermione']
    return(list_a)

print("4.8:",good())