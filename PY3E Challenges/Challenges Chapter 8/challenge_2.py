# Challenge 2 Write a program that simulates a television by creating it as an object
# The user should be able to enter a channel number and raise or lower the volume.
# MAke sure that the channel number and volume level stay within valid ranges.


class Television:
    def __init__(self,channel = 1,volume = 1):
        self.channel = channel
        self.volume = volume

    def __volume_up(self):
        self.volume += 1

    def __volume_down(self):
        self.volume -= 1

    def change_channel(self):
        channel = int(input("Choose a channel to watch between 1-9: "))
        while channel < 1 or channel > 9:
            channel = int(input("That channel does not exist. Choose a channel to watch between 1-9: "))
        self.channel = channel
        if self.channel == 1:
            print("You turned on Fox News!")
        elif self.channel == 2:
            print("You turned on CNBC!")
        elif self.channel == 3:
            print("You turned on ESPN!")
        elif self.channel == 4:
            print("You turned on ABC!")
        elif self.channel == 5:
            print("You turned on CBS!")
        elif self.channel == 6:
            print("You turned on Nickelodeon!")
        elif self.channel == 7:
            print("You turned on CNN!")
        elif self.channel == 8:
            print("You turned on Cartoon Network!")
        elif self.channel == 9:
            print("You turned on TBS!")

    def volume_change(self):
        change = input("Raise or Lower the channel?").lower()
        if change == "raise":
            self.__volume_up()
            if self.volume >= 10:
                print("Volume at max")
                self.volume = 10
            else:
                print("Volume",self.volume)
        elif change == "lower":
            self.__volume_down()
            if self.volume <= 0:
                print("Volume muted")
                self.volume = 0
            else:
                print("Volume",self.volume)



tv = Television()

def main():

    while True:
        choice = input("""

        0 = Turn Off TV
        1 = Change Channel
        2 = Change Volume

        """)

        if choice == "0":
            print("TV is turned off")
            break


        if choice == "1":
            tv.change_channel()


        if choice == "2":
            tv.volume_change()



main()
