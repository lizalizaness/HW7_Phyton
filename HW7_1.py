print("I would like to check your luck!\nPlease, follow the instructions")
import random
a = int(input("Enter value from 1 to 10: "))
while a < 1 or a > 11:
    print("Don't cheat! I would like to play fair!!!")
    a = int(input("Enter value from 1 to 10: "))
random_value = random.randint(1, 10)
if a>=random_value:
    print ("Wow, you're extra lucky today! Congrats")
else: print ("Oh no...You can try again")