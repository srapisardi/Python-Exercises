# Challenge 3 Create a simple, one-player game of pong, where a player controls a paddle
# and the ball bounces off three walls. If the balls get by the player's paddel, the game is over.

from superwires import games, color
import random

games.init(screen_width = 800, screen_height = 600, fps = 60)

class Player(games.Sprite):
    image = games.load_image("player_one.png")

    def __init__(self):
        super(Player, self).__init__(image = Player.image,
                                     x = games.mouse.x,
                                     bottom = games.screen.height)

    def update(self):
        self.x = games.mouse.x

        if self.left < 0:
            self.left = 0

        if self.right > games.screen.width:
            self. right = games.screen.width

class WallOne(games.Sprite):
    image = games.load_image("wall_one.png")

    def __init__(self):
        super(WallOne, self).__init__(image = WallOne.image,
                                      x = 100,
                                      top = 5)

class WallTwo(games.Sprite):
    image = games.load_image("wall_two.png")

    def __init__(self):
        super(WallTwo, self).__init__(image = WallTwo.image,
                                      x = 700,
                                      top = 5)

class WallThree(games.Sprite):
    image = games.load_image("wall_three.png")

    def __init__(self):
        super(WallThree, self).__init__(image = WallThree.image,
                                        x = 400,
                                        top = 5)

class Ball(games.Sprite):
    image = games.load_image("ball.png")

    def __init__(self):
        super(Ball, self).__init__(image = Ball.image,
                                   x = random.randint(1,games.screen.width),
                                   y = random.randint(1,games.screen.height),
                                   dy = 4,
                                   dx = 4)

    def update(self):
        if self.bottom > games.screen.height:
            game_over = games.Message(value="Game Over!",
                                      size=100,
                                      color = color.blue,
                                      x = games.screen.width/2,
                                      y = games.screen.height/2,
                                      lifetime = 5 * games.screen.fps,
                                      after_death = games.screen.quit)

            games.screen.add(game_over)

        for ball in self.overlapping_sprites:
            self.dy = -self.dy

        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx

        if self.top < 0:
            self.dy = -self.dy



def main():
    bg = games.load_image("bg.jpg", transparent = False)
    games.screen.background = bg

    p = Player()
    games.screen.add(p)

    w_one = WallOne()
    games.screen.add(w_one)

    w_two = WallTwo()
    games.screen.add(w_two)

    w_three = WallThree()
    games.screen.add(w_three)

    b = Ball()
    games.screen.add(b)

    games.mouse.is_visible = False
    games.mouse.event_grab = True

    games.screen.mainloop()

main()
