# Challenge 2 Write a game where the player controls a character that must avoid falling debris.
# The player controls the character with the mouse and objects fall from the sky.

from superwires import games, color
import random

games.init(screen_width=800, screen_height=600, fps=60)

class Spaceship(games.Sprite):
    image = games.load_image("spaceship_sprite.png")

    def __init__(self):
        super(Spaceship, self).__init__(image=Spaceship.image,
                                        x = games.mouse.x,
                                        bottom = games.screen.height)

    def update(self):
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self.right = games.screen.width

        self.check_crash()


    def check_crash(self):
        for alien in self.overlapping_sprites:
            game_over = games.Message(value = "Game Over!",
                                      size = 90,
                                      color = color.red,
                               x = games.screen.width/2,
                              y = games.screen.height/2,
                        lifetime = 5 * games.screen.fps,
                         after_death = games.screen.quit)

            games.screen.add(game_over)


class Alien(games.Sprite):
    image = games.load_image("alien.png")

    speed = 1.5


    def __init__(self, x = games.screen.width/2, y = 90):
        super(Alien,self).__init__(image=Alien.image,
                                   x = x, y = y,
                                   dy = Alien.speed)

    def update(self):
        self.check_dodge()

    def check_dodge(self):
        if self.bottom > games.screen.height:
            self.destroy()


class Boss(games.Sprite):
    image = games.load_image("boss.gif")

    def __init__(self, y = 55, speed = 3, odds_change = 200):
        super(Boss, self).__init__(image = Boss.image,
                                      x = games.screen.width / 2,
                                      y = y,
                                      dx = speed)

        self.odds_change = odds_change
        self.time_til_drop = 0

    def update(self):
        if self.left == -100 or self.right == 900:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.check_drop()

    def check_drop(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_alien = Alien(x = self.x)
            games.screen.add(new_alien)
            self.time_til_drop = int(new_alien.height * 1.3 / Alien.speed) + 1


def main():
    space = games.load_image("galaxy.jpg",transparent=False)
    games.screen.background = space

    ship = Spaceship()
    games.screen.add(ship)

    enemy = Alien()
    games.screen.add(enemy)

    new_alien = Boss()
    games.screen.add(new_alien)

    games.mouse.is_visible = False
    games.screen.event_grab = True

    games.screen.mainloop()


main()
