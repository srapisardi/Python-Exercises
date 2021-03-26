from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Death(Scene):

    def enter(self):
        print("You have died! Game over!")
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
        The Gothons of Planet Percal #25 have invaded your ship and destroyed the entire crew
        You're running down the central corridor to the Weapons Armony from a Gothon jumps out. He's blocking the door
        to the armory and about to pull a weapon"""))

        action = input("> ")

        if action == "shoot":
            print("You shoot the Gothon but misses. The Gothon blast you repeatedly in the face")
            return 'death'

        elif action == "dodge":
            print("You attempt to dodge but bang your head and pass out. You wake up to a Gothon eating you and die.")
            return 'death'

        elif action == "tell joke":
            print("You tell a joke and it works. As the Gothon is laughing, you jump to the Armory room.")
            return 'laser_weapon_armory'
        else:
            print("Invalid move.")
            return 'central_corridor'


class LaserWeaponArmory(Scene):
    def enter(self):
        print("You dive into the weapon armory. There is a keypad to unlock the bomb.")
        print("You need a 3 digit code to unlock it.")
        code = int(f"{randint(1,9)}{randint(1,9)}{randint(1,9)}")
        guesses = 0
        guess = int(input("Enter code: "))

        while guess != code and guesses <= 10:
            if guess == 000:
                break
            else:
                print("Wrong!")
                guesses += 1
                guess = input("Enter code: ")

        if guess == code or guess == 000:
            print("Correct! You grab the bobm and run to the bridge!")
            return 'the_bridge'
        else:
            print("You ran out of attempts and the ship blows up.")
            return 'death'



class TheBridge(Scene):
    def enter(self):
        print("You've entered the bridge with 5 Gothons controlling the ship. They see the active bomb you are carrying.")

        action = input("> ")

        if action == "throw the bomb":
            print("You throw the bomb but a Gothon shoots you and kills you.")
            return 'death'
        elif action == "slowly place bomb":
            print("You slowly place the bomb down and run as quickly as you can to the escape pod.")
            return 'escape_pod'
        else:
            print("Invalid move")
            return 'the_bridge'

class EscapePod(Scene):
    def enter(self):
        print("You find the escape pods. There are 5 and must choose 1.")
        good_pod = randint(1,5)
        guess = input("> ")

        if int(guess) != good_pod:
            print("You chose a bad escape pod and it explodes")
            return 'death'
        else:
            print("You jump into",guess,"and exit safely. You win!")
            return 'finished'

class Finished(Scene):
    def enter(self):
        print("You won! Game over!")
        return 'finished'


class Map(object):
    scenes = {
    'central_corridor': CentralCorridor(),
    'laser_weapon_armory': LaserWeaponArmory(),
    'the_bridge': TheBridge(),
    'escape_pod': EscapePod(),
    'death': Death(),
    'finished': Finished()
    }

    def __init__(self, starting_scene):
        self.starting_scene = starting_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.starting_scene)


a_map = Map("central_corridor")
a_game = Engine(a_map)
a_game.play()
