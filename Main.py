stats = {"hp 30", "pow 12", "def 10"}

character = ["Torch Head", "Mr. Frost", "Lightning Rod", "Vine Master"]
for x in character:
    print(x)
chosen = input("Select your character")
for x in character:
    if chosen == x:
        chosen = x
enemy = input("Chose your opponent")
for x in character:
    if enemy == x:
        enemy = x
print(chosen + " Encounters " + enemy)
Action = ["Attack", "Items", "Run"]
input(print("Select Action"))
Items = ["Potion", "Pow Up", "Def Up"]
input(print("Select Items"))

