# Challenge 4 Create your own adventure game.

import random

class Player(object):
    def __init__(self,name,hp=20, gold = 0, potions=0):
        self.name = name
        self.hp = hp
        self.gold = gold
        self.potions = potions

    def __str__(self):
        hp = str(self.hp)
        gold = str(self.gold)
        pots = str(self.potions)
        return str(print("HP:",hp,"Gold:",gold,"Potions",pots))

    def heal(self):
        if self.hp == 20:
            print("Already at full health")
        elif self.potions:
            self.hp += 5
            if self.hp > 20:
                self.hp == 20
            print("HP:",self.hp)
            self.potions -= 1
        else:
            print("No more potions")


    def pick_up(self, item):
        self.item = item
        if self.item == "gold":
            gold = random.randint(1,5)
            self.gold += gold
            print("You found",gold,"gold.")
        elif self.item == "potion":
            self.potions += 1
            print("You found a potion")


    def attack(self, enemy):
        hit_chance = random.randint(1,2)
        if hit_chance == 2:
            enemy.hit()
            print("You hit the Goblin.")
            if enemy.hp == 0:
                enemy.die()
        else:
            print("You missed!")

    def hit(self):
        self.hp -= 1
        return self.hp

    def die(self):
        if self.hp == 0:
            print("You are dead.")

    def run(self, run_chance):
        self.run_chance = run_chance
        if run_chance == 2:
            print("You successfully ran.")
        else:
            print("Unable to run.")


class Goblin(object):
    def __init__(self,name="Goblin",hp=10):
        self.name = name
        self.hp = hp
        print("A Goblin appeared!")

    def attack(self, player):
        hit_chance = random.randint(1,2)
        if hit_chance == 2:
            player.hit()
            print("Goblin hit you.")
            if player.hp == 0:
                player.die()
        else:
            print("Goblin missed!")

    def hit(self):
        self.hp -= 1
        return self.hp

    def die(self):
        if self.hp == 0:
            print("The Goblin is dead.")

    def drop(self):
        item = random.choice("potion","gold")
        if item == "potion":
            player.pick_up("potion")
            print("Goblin dropped a potion!")
        elif item == "gold":
            player.pick_up("gold")
            print("Goblin dropped gold!")


def main():
    print("Welcome to CavePY!")
    name = input("Name your hero: ")
    hero = Player(name)

    while hero.hp > 0:
        AREAS = ("empty","gold","enemy","potion")
        random_event = random.choice(AREAS)
        move = input("Press 1. to Move Forward in the cave, 2. to check your status or 3. to heal. Type 'q' to quit").lower()
        if move == "2":
            print(hero)
            continue
        if move == "3":
            hero.heal()
            continue
        elif move == "q":
            print("Exit")
            break

        if random_event == "gold":
            hero.pick_up(random_event)
        elif random_event == "potion":
            hero.pick_up(random_event)
        elif random_event == "empty":
            print("You've entered an empty area")
        elif random_event == "enemy":
            enemy = Goblin()
            while enemy.hp > 0:
                battle = input("Press 1 to attack ot 2 to run")
                if battle == "1":
                    hero.attack(enemy)
                    enemy.attack(hero)
                elif battle == "2":
                    run = random.randint(1,2)
                    hero.run(run)
                    if run == "2":
                        break
                    else:
                        enemy.attack(hero)



main()
