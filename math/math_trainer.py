import math
import random
from termcolor import colored
while 1==1:
    a = random.randint(0,10)
    b = random.randint(0,10)
    print("\n",a," + ",b)
    user = int(input("\nwhat is the answer : "))
    c = int(a) + int(b)
    if user == c:
        print("\n yes correct answer")
        print("\n the answer is : ",c)
    else:
        print("\n no incorrect answer")
        print("\n*************************")
        print("\n no incorrect answer")
        print("\n no incorrect answer")
        print("\n*************************")
        print("\n no incorrect answer")
        print(colored('hello', 'red'), colored('world', 'green'))
