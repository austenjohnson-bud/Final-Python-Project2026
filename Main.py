import json
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# WINDOW SETUP
root = tk.Tk()
root.title("Battle")

# LOAD BACKGROUND
background = Image.open(r"")
background = background.resize((800, 500))
bg_image = ImageTk.PhotoImage(background)

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
Character1 = Character("Torch Head", 100, 25, 0, 'FireBlast', 'FirePunch', 'FlareBomb', 30, 35, 28 )
Character2 = Character("Mr. Frost", 100, 25, 0, 'FrostBreath', 'FrostPunch', 'Icicle', 29,  35, 30)
Character3 = Character("Lightning Rod", 100, 25, 0, 'Thundershock', 'ThunderPunch', 'Shockwave', 30, 36, 28)
Character4 = Character("Vine Master", 100, 25, 0, 'Grapple Vine', 'Life Drain', 'Thorn Attack', 28, 10, 32)
possible_characters = [Character1, Character2, Character3, Character4]
chosen = input("Select your character")
myCharacter = Character1
hp = 100
ehp = 100
roll = random.randint(1, 9)
for x in possible_characters:
    if chosen == x.name:
        myCharacter = x
enemy = input("Chose your opponent")
for x in character:
    if enemy == x:
        enemy = x
print(chosen + " Encounters " + enemy)
while True:
    Action = ["Attack", "Items", "Run"]
    chosenAction = input("Select Action")
    if chosenAction == "Attack":
        move = input("What will you use?")
        TorchHeadattack = ["FireBlast", "FirePunch", "FlareBomb"]
        MrFrostattack = ["FrostBreath", "FrostPunch", "Icicle"]
        LightningRodattack = ["Thundershock", "ThunderPunch", "Shockwave"]
        VineMasterattack = ["Grapple Vine", "Life Drain", "Thorn Attack"]
        if chosen == "Torch Head":

            if move == "FireBlast":
                ehp -= 30
                print(enemy + "attack")
                if roll >= 1 and roll <= 3 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostBreath")
                    hp -= 29
                elif roll >= 4 and roll <= 6 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostPunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Mr.Frost":
                    print(enemy + "Used Icicle")
                    hp -= 30
                elif roll >= 1 and roll <= 3 and enemy == "Torch Head":
                    print(enemy + "Used FireBlast")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Torch Head":
                    print(enemy + "Used FirePunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Torch Head":
                    print(enemy + "Used FlareBomb")
                    hp -= 28
                elif roll >= 1 and roll <=3 and enemy == "Lightning Rod":
                    print(enemy + "Used Thundershock")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Lightning Rod":
                    print(enemy + "Used ThunderPunch")
                    hp -= 36
                elif roll >= 7 and roll <= 9 and enemy == "Lightning Rod":
                    print(enemy + "Used Shockwave")
                    hp -= 28
                elif roll >= 1 and roll <= 3 and enemy == "Vine Master":
                    print(enemy + "Used Grapple Vine")
                    hp -= 28
                elif roll >= 4 and roll <= 6 and enemy == "Vine Master":
                    print(enemy + "Used Life Drain")
                    hp -= 10
                    ehp += 10
                elif roll >= 7 and roll <= 9 and enemy == "Vine Master":
                    print(enemy + "Used Thorn Attack")
                    hp -= 32
            elif move == "FirePunch":
                ehp -= 35
                print(enemy + "attack")
                if roll >= 1 and roll <= 3 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostBreath")
                    hp -= 29
                elif roll >= 4 and roll <= 6 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostPunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Mr.Frost":
                    print(enemy + "Used Icicle")
                    hp -= 30
                elif roll >= 1 and roll <= 3 and enemy == "Torch Head":
                    print(enemy + "Used FireBlast")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Torch Head":
                    print(enemy + "Used FirePunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Torch Head":
                    print(enemy + "Used FlareBomb")
                    hp -= 28
                elif roll >= 1 and roll <=3 and enemy == "Lightning Rod":
                    print(enemy + "Used Thundershock")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Lightning Rod":
                    print(enemy + "Used ThunderPunch")
                    hp -= 36
                elif roll >= 7 and roll <= 9 and enemy == "Lightning Rod":
                    print(enemy + "Used Shockwave")
                    hp -= 28
                elif roll >= 1 and roll <= 3 and enemy == "Vine Master":
                    print(enemy + "Used Grapple Vine")
                    hp -= 28
                elif roll >= 4 and roll <= 6 and enemy == "Vine Master":
                    print(enemy + "Used Life Drain")
                    hp -= 10
                    ehp += 10
                elif roll >= 7 and roll <= 9 and enemy == "Vine Master":
                    print(enemy + "Used Thorn Attack")
                    hp -= 32
            elif move == "FlareBomb":
                ehp -= 28
                print(enemy + "attack")
                if roll >= 1 and roll <= 3 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostBreath")
                    hp -= 29
                elif roll >= 4 and roll <= 6 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostPunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Mr.Frost":
                    print(enemy + "Used Icicle")
                    hp -= 30
                elif roll >= 1 and roll <= 3 and enemy == "Torch Head":
                    print(enemy + "Used FireBlast")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Torch Head":
                    print(enemy + "Used FirePunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Torch Head":
                    print(enemy + "Used FlareBomb")
                    hp -= 28
                elif roll >= 1 and roll <=3 and enemy == "Lightning Rod":
                    print(enemy + "Used Thundershock")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Lightning Rod":
                    print(enemy + "Used ThunderPunch")
                    hp -= 36
                elif roll >= 7 and roll <= 9 and enemy == "Lightning Rod":
                    print(enemy + "Used Shockwave")
                    hp -= 28
                elif roll >= 1 and roll <= 3 and enemy == "Vine Master":
                    print(enemy + "Used Grapple Vine")
                    hp -= 28
                elif roll >= 4 and roll <= 6 and enemy == "Vine Master":
                    print(enemy + "Used Life Drain")
                    hp -= 10
                    ehp += 10
                elif roll >= 7 and roll <= 9 and enemy == "Vine Master":
                    print(enemy + "Used Thorn Attack")
                    hp -= 32
        elif chosen == "Mr. Frost":
            move = input("Select Mr. Frost's move")
            if move == "FrostBreath":
                ehp -= 29
                print(enemy + "attack")
                if roll >= 1 and roll <= 3 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostBreath")
                    hp -= 29
                elif roll >= 4 and roll <= 6 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostPunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Mr.Frost":
                    print(enemy + "Used Icicle")
                    hp -= 30
                elif roll >= 1 and roll <= 3 and enemy == "Torch Head":
                    print(enemy + "Used FireBlast")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Torch Head":
                    print(enemy + "Used FirePunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Torch Head":
                    print(enemy + "Used FlareBomb")
                    hp -= 28
                elif roll >= 1 and roll <=3 and enemy == "Lightning Rod":
                    print(enemy + "Used Thundershock")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Lightning Rod":
                    print(enemy + "Used ThunderPunch")
                    hp -= 36
                elif roll >= 7 and roll <= 9 and enemy == "Lightning Rod":
                    print(enemy + "Used Shockwave")
                    hp -= 28
                elif roll >= 1 and roll <= 3 and enemy == "Vine Master":
                    print(enemy + "Used Grapple Vine")
                    hp -= 28
                elif roll >= 4 and roll <= 6 and enemy == "Vine Master":
                    print(enemy + "Used Life Drain")
                    hp -= 10
                    ehp += 10
                elif roll >= 7 and roll <= 9 and enemy == "Vine Master":
                    print(enemy + "Used Thorn Attack")
                    hp -= 32
            elif move == "FrostPunch":
                ehp -= 35
                print(enemy + "attack")
                if roll >= 1 and roll <= 3 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostBreath")
                    hp -= 29
                elif roll >= 4 and roll <= 6 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostPunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Mr.Frost":
                    print(enemy + "Used Icicle")
                    hp -= 30
                elif roll >= 1 and roll <= 3 and enemy == "Torch Head":
                    print(enemy + "Used FireBlast")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Torch Head":
                    print(enemy + "Used FirePunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Torch Head":
                    print(enemy + "Used FlareBomb")
                    hp -= 28
                elif roll >= 1 and roll <=3 and enemy == "Lightning Rod":
                    print(enemy + "Used Thundershock")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Lightning Rod":
                    print(enemy + "Used ThunderPunch")
                    hp -= 36
                elif roll >= 7 and roll <= 9 and enemy == "Lightning Rod":
                    print(enemy + "Used Shockwave")
                    hp -= 28
                elif roll >= 1 and roll <= 3 and enemy == "Vine Master":
                    print(enemy + "Used Grapple Vine")
                    hp -= 28
                elif roll >= 4 and roll <= 6 and enemy == "Vine Master":
                    print(enemy + "Used Life Drain")
                    hp -= 10
                    ehp += 10
                elif roll >= 7 and roll <= 9 and enemy == "Vine Master":
                    print(enemy + "Used Thorn Attack")
                    hp -= 32
            elif move == "Icicle":
                ehp -= 30
                print(enemy + "attack")
                if roll >= 1 and roll <= 3 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostBreath")
                    hp -= 29
                elif roll >= 4 and roll <= 6 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostPunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Mr.Frost":
                    print(enemy + "Used Icicle")
                    hp -= 30
                elif roll >= 1 and roll <= 3 and enemy == "Torch Head":
                    print(enemy + "Used FireBlast")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Torch Head":
                    print(enemy + "Used FirePunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Torch Head":
                    print(enemy + "Used FlareBomb")
                    hp -= 28
                elif roll >= 1 and roll <=3 and enemy == "Lightning Rod":
                    print(enemy + "Used Thundershock")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Lightning Rod":
                    print(enemy + "Used ThunderPunch")
                    hp -= 36
                elif roll >= 7 and roll <= 9 and enemy == "Lightning Rod":
                    print(enemy + "Used Shockwave")
                    hp -= 28
                elif roll >= 1 and roll <= 3 and enemy == "Vine Master":
                    print(enemy + "Used Grapple Vine")
                    hp -= 28
                elif roll >= 4 and roll <= 6 and enemy == "Vine Master":
                    print(enemy + "Used Life Drain")
                    hp -= 10
                    ehp += 10
                elif roll >= 7 and roll <= 9 and enemy == "Vine Master":
                    print(enemy + "Used Thorn Attack")
                    hp -= 32
        elif chosen == "Lightning Rod":
            move = input("Select Lightning Rod's move")
            if move == "Thundershock":
                ehp -= 30
                print(enemy + "attack")
                if roll >= 1 and roll <= 3 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostBreath")
                    hp -= 29
                elif roll >= 4 and roll <= 6 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostPunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Mr.Frost":
                    print(enemy + "Used Icicle")
                    hp -= 30
                elif roll >= 1 and roll <= 3 and enemy == "Torch Head":
                    print(enemy + "Used FireBlast")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Torch Head":
                    print(enemy + "Used FirePunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Torch Head":
                    print(enemy + "Used FlareBomb")
                    hp -= 28
                elif roll >= 1 and roll <=3 and enemy == "Lightning Rod":
                    print(enemy + "Used Thundershock")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Lightning Rod":
                    print(enemy + "Used ThunderPunch")
                    hp -= 36
                elif roll >= 7 and roll <= 9 and enemy == "Lightning Rod":
                    print(enemy + "Used Shockwave")
                    hp -= 28
                elif roll >= 1 and roll <= 3 and enemy == "Vine Master":
                    print(enemy + "Used Grapple Vine")
                    hp -= 28
                elif roll >= 4 and roll <= 6 and enemy == "Vine Master":
                    print(enemy + "Used Life Drain")
                    hp -= 10
                    ehp += 10
                elif roll >= 7 and roll <= 9 and enemy == "Vine Master":
                    print(enemy + "Used Thorn Attack")
                    hp -= 32
            elif move == "ThunderPunch":
                ehp -= 36
                print(enemy + "attack")
                if roll >= 1 and roll <= 3 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostBreath")
                    hp -= 29
                elif roll >= 4 and roll <= 6 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostPunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Mr.Frost":
                    print(enemy + "Used Icicle")
                    hp -= 30
                elif roll >= 1 and roll <= 3 and enemy == "Torch Head":
                    print(enemy + "Used FireBlast")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Torch Head":
                    print(enemy + "Used FirePunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Torch Head":
                    print(enemy + "Used FlareBomb")
                    hp -= 28
                elif roll >= 1 and roll <=3 and enemy == "Lightning Rod":
                    print(enemy + "Used Thundershock")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Lightning Rod":
                    print(enemy + "Used ThunderPunch")
                    hp -= 36
                elif roll >= 7 and roll <= 9 and enemy == "Lightning Rod":
                    print(enemy + "Used Shockwave")
                    hp -= 28
                elif roll >= 1 and roll <= 3 and enemy == "Vine Master":
                    print(enemy + "Used Grapple Vine")
                    hp -= 28
                elif roll >= 4 and roll <= 6 and enemy == "Vine Master":
                    print(enemy + "Used Life Drain")
                    hp -= 10
                    ehp += 10
                elif roll >= 7 and roll <= 9 and enemy == "Vine Master":
                    print(enemy + "Used Thorn Attack")
                    hp -= 32
            elif move == "Shockwave":
                ehp -= 28
                print(enemy + "attack")
                if roll >= 1 and roll <= 3 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostBreath")
                    hp -= 29
                elif roll >= 4 and roll <= 6 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostPunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Mr.Frost":
                    print(enemy + "Used Icicle")
                    hp -= 30
                elif roll >= 1 and roll <= 3 and enemy == "Torch Head":
                    print(enemy + "Used FireBlast")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Torch Head":
                    print(enemy + "Used FirePunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Torch Head":
                    print(enemy + "Used FlareBomb")
                    hp -= 28
                elif roll >= 1 and roll <=3 and enemy == "Lightning Rod":
                    print(enemy + "Used Thundershock")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Lightning Rod":
                    print(enemy + "Used ThunderPunch")
                    hp -= 36
                elif roll >= 7 and roll <= 9 and enemy == "Lightning Rod":
                    print(enemy + "Used Shockwave")
                    hp -= 28
                elif roll >= 1 and roll <= 3 and enemy == "Vine Master":
                    print(enemy + "Used Grapple Vine")
                    hp -= 28
                elif roll >= 4 and roll <= 6 and enemy == "Vine Master":
                    print(enemy + "Used Life Drain")
                    hp -= 10
                    ehp += 10
                elif roll >= 7 and roll <= 9 and enemy == "Vine Master":
                    print(enemy + "Used Thorn Attack")
                    hp -= 32
        elif chosen == "Vine Master":
            move = input("Select Vine Master's move")
            if move == "Grapple Vine":
                ehp -= 28
                print(enemy + "attack")
                if roll >= 1 and roll <= 3 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostBreath")
                    hp -= 29
                elif roll >= 4 and roll <= 6 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostPunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Mr.Frost":
                    print(enemy + "Used Icicle")
                    hp -= 30
                elif roll >= 1 and roll <= 3 and enemy == "Torch Head":
                    print(enemy + "Used FireBlast")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Torch Head":
                    print(enemy + "Used FirePunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Torch Head":
                    print(enemy + "Used FlareBomb")
                    hp -= 28
                elif roll >= 1 and roll <=3 and enemy == "Lightning Rod":
                    print(enemy + "Used Thundershock")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Lightning Rod":
                    print(enemy + "Used ThunderPunch")
                    hp -= 36
                elif roll >= 7 and roll <= 9 and enemy == "Lightning Rod":
                    print(enemy + "Used Shockwave")
                    hp -= 28
                elif roll >= 1 and roll <= 3 and enemy == "Vine Master":
                    print(enemy + "Used Grapple Vine")
                    hp -= 28
                elif roll >= 4 and roll <= 6 and enemy == "Vine Master":
                    print(enemy + "Used Life Drain")
                    hp -= 10
                    ehp += 10
                elif roll >= 7 and roll <= 9 and enemy == "Vine Master":
                    print(enemy + "Used Thorn Attack")
                    hp -= 32
            elif move == "Life Drain":
                ehp -= 10
                hp += 10
                print(enemy + "attack")
                if roll >= 1 and roll <= 3 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostBreath")
                    hp -= 29
                elif roll >= 4 and roll <= 6 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostPunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Mr.Frost":
                    print(enemy + "Used Icicle")
                    hp -= 30
                elif roll >= 1 and roll <= 3 and enemy == "Torch Head":
                    print(enemy + "Used FireBlast")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Torch Head":
                    print(enemy + "Used FirePunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Torch Head":
                    print(enemy + "Used FlareBomb")
                    hp -= 28
                elif roll >= 1 and roll <=3 and enemy == "Lightning Rod":
                    print(enemy + "Used Thundershock")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Lightning Rod":
                    print(enemy + "Used ThunderPunch")
                    hp -= 36
                elif roll >= 7 and roll <= 9 and enemy == "Lightning Rod":
                    print(enemy + "Used Shockwave")
                    hp -= 28
                elif roll >= 1 and roll <= 3 and enemy == "Vine Master":
                    print(enemy + "Used Grapple Vine")
                    hp -= 28
                elif roll >= 4 and roll <= 6 and enemy == "Vine Master":
                    print(enemy + "Used Life Drain")
                    hp -= 10
                    ehp += 10
                elif roll >= 7 and roll <= 9 and enemy == "Vine Master":
                    print(enemy + "Used Thorn Attack")
                    hp -= 32
            elif move == "Thorn Attack":
                ehp -= 32
                print(enemy + "attack")
                if roll >= 1 and roll <= 3 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostBreath")
                    hp -= 29
                elif roll >= 4 and roll <= 6 and enemy == "Mr.Frost":
                    print(enemy + "Used FrostPunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Mr.Frost":
                    print(enemy + "Used Icicle")
                    hp -= 30
                elif roll >= 1 and roll <= 3 and enemy == "Torch Head":
                    print(enemy + "Used FireBlast")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Torch Head":
                    print(enemy + "Used FirePunch")
                    hp -= 35
                elif roll >= 7 and roll <= 9 and enemy == "Torch Head":
                    print(enemy + "Used FlareBomb")
                    hp -= 28
                elif roll >= 1 and roll <=3 and enemy == "Lightning Rod":
                    print(enemy + "Used Thundershock")
                    hp -= 30
                elif roll >= 4 and roll <= 6 and enemy == "Lightning Rod":
                    print(enemy + "Used ThunderPunch")
                    hp -= 36
                elif roll >= 7 and roll <= 9 and enemy == "Lightning Rod":
                    print(enemy + "Used Shockwave")
                    hp -= 28
                elif roll >= 1 and roll <= 3 and enemy == "Vine Master":
                    print(enemy + "Used Grapple Vine")
                    hp -= 28
                elif roll >= 4 and roll <= 6 and enemy == "Vine Master":
                    print(enemy + "Used Life Drain")
                    hp -= 10
                    ehp += 10
                elif roll >= 7 and roll <= 9 and enemy == "Vine Master":
                    print(enemy + "Used Thorn Attack")
                    hp -= 32
    elif chosenAction == "Items":
        Items = ["Potion", "Pow Up", "Def Up"]
        chosenItem = input("Select Items")
        if chosenItem == "Pow Up":
            myCharacter.pow += 5
        elif chosenItem == "Def Up":
            myCharacter.defence += 5
        elif chosenItem == "Potion":
            hp += 30
    elif chosenAction == "Run":
        print("You ran away")
    if ehp <= 0:
        print( chosen + "Wins")
    elif hp <= 0:
        print( enemy + "Wins")


