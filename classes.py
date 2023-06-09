

from settings import *
from random import choice


class Snake:
    start_x, start_y = gridCetnre
    movex = 0
    movey = 0

    countBlocks = 0
    gameOver = False

    def __init__(self):
        self.x = Snake.start_x
        self.y = Snake.start_y
        self.colour = [189, 0, 255]
        self.body = [[self.x, self.y]]

    def block_move(self):
        self.x += self.movex
        self.y += self.movey
        #self.colour = (choice(range(255)), choice(range(255)), choice(range(255)))
        # if self.x > windowX - sizeX or self.y > windowY - sizeY or self.x < 0 or self.y < 0: #конец поля
        #     self.game_over() # удар о стенки

        if self.x > windowX - sizeX:
            self.x = -self.movex
        elif self.y > windowY - sizeY:
            self.y = -self.movey
        elif self.x < 0:
            self.x = windowX
        elif self.y < 0:
            self.y = windowY

            # замыкание змейки
        elif [self.x, self.y] in self.body[1:]:
            self.game_over()

            # перемещение
        else:
            for i in reversed(range(len(self.body))):
                self.body[i][0], self.body[i][1] = self.body[i - 1][0], self.body[i - 1][1]
            self.body[0][0], self.body[0][1] = self.x, self.y
            self.block = [pygame.draw.rect(dis, self.colour, [i[0], i[1], sizeX, sizeY]) for i in self.body]  # работает

    def right(self):
        self.movex = sizeX
        self.movey = 0

    def left(self):
        self.movex = -sizeX
        self.movey = 0

    def down(self):
        self.movex = 0
        self.movey = sizeY

    def up(self):
        self.movex = 0
        self.movey = -sizeY

    def addBlock(self):
        self.countBlocks += 1
        self.body.append([self.x, self.y])
        print(self.body)

    def game_over(self):
        self.countBlocks = 1
        self.gameOver = True
        dis.fill('white')
        dis.blit(image, (25, 137))

    def new_game(self):
        self.gameOver = False
        self.x = Snake.start_x
        self.y = Snake.start_y
        self.countBlocks = 1
        self.body = [[self.x, self.y]]
        self.movex = 0
        self.movey = 0


class Apple:
    onScreen = False

    def __init__(self):
        self.colour = (158, 0, 255)
        self.x, self.y = choice(appleX), choice(appleY)

    def newApple(self):
        # self.onScreen = True
        self.block = pygame.draw.circle(dis, self.colour, [self.x, self.y], radius)

    def death(self):
        self.x, self.y = choice(appleX), choice(appleY)

        # self.onScreen = False
