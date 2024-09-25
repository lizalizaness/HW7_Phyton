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
    