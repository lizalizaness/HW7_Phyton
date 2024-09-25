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

people_dataset = []
print("Imagine, that I'm collecting the dataset for my research about names popularity depending on regions.\n Please enter the name of all your friends here.")
while True:
    name = input("Enter name or print stop to leave: ")
    if name == 'stop':
        break
    age = input("Enter the age: ")
    city = input("Enter the city: ")
    person = {"name": name, "age": age,"city": city}
    people_dataset.append(person)
print("\nCollected people's Data:")
for person in people_dataset:
    print(person)
    
    import math
sqrt_result1 = math.sqrt(num1)
print(f"The square root of {num1} is: {sqrt_result1}")
sqrt_result2 = math.sqrt(num2)
print(f"The square root of {num2} is: {sqrt_result2}")