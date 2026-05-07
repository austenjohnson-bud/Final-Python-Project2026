import json



class Character:
    def __init__(self, name, hp, pow, defence, move1, move2, move3, move1pow, move2pow, move3pow):
        self.name = name
        self.hp = hp
        self.pow = pow
        self.defence = defence
        self.moves = move1
        self.move2 = move2
        self.move3 = move3
        self.move1pow = move1pow
        self.move2pow = move2pow
        self.move3pow = move3pow

stats = ["hp", "attack", "defence"]
character = ["Torch Head", "Mr. Frost", "Lightning Rod", "Vine Master"]
for x in character:
    print(x)
Character1 = Character("TorchHead", 100, 25, 0, 'FireBlast', 'FirePunch', 'FlareBomb', 30, 35, 28 )
Character2 = Character("Mr. Frost", 100, 25, 0, 'FrostBreath', 'FrostPunch', 'Icicle', 29,  35, 30)
Character3 = Character("Lightning Rod", 100, 25, 0, 'Thundershock', 'ThunderPunch', 'Shockwave', 30, 36, 28)
Character4 = Character("Vine Master", 100, 25, 0, 'Grapple Vine', 'Life Drain', 'Thorn Attack', 28, 10, 32)
possible_characters = [Character1, Character2, Character3, Character4]
chosen = input("Select your character")
myCharacter = Character1
for x in possible_characters:
    if chosen == x.name:
        myCharacter = x
enemy = input("Chose your opponent")
for x in character:
    if enemy == x:
        enemy = x
print(chosen + " Encounters " + enemy)
Action = ["Attack", "Items", "Run"]
chosenAction = input("Select Action")
if chosenAction == "Attack":
    input("What will you use?")
elif chosenAction == "Items":
    Items = ["Potion", "Pow Up", "Def Up"]
    chosenItem = input("Select Items")
    if chosenItem == "Pow Up":
        myCharacter.hp += 5
elif chosenAction == "Run":
    print("You ran away")



