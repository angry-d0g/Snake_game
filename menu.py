import pygame
from settings import dis


class Button:
    def __init__(self, x, y, width, height, massage):
        self.width = width
        self.height = height
        self.massage = massage
        self.inactive_clr = (255, 255, 255)
        self.active_clr = (192, 192, 192)
        self.x = x
        self.y = y

    def print_text(self, font_size=30):
        font_color = (0, 0, 0)
        font_type = 'PingPong.ttf'
        font_type = pygame.font.Font(font_type, font_size)
        text = font_type.render(self.massage, True, font_color)
        dis.blit(text, (self.x + 5, self.y + 5))

    # def draw(self, text, font_size = 30):
    #     self.print_text(font_size)
    #     mouse = pygame.mouse.get_pos()
    #     click = pygame.mouse.get_pressed()
    #
    #
    #     if self.x < mouse[0] < self.width and self.y < mouse[1] < self.height:
    #         pygame.draw.rect(dis, self.active_clr, self.x, self.y, self.width, self.height)
    #         if click[0] == 1:
    #
    #     else:
    #         pygame.draw.rect(dis, self.inactive_clr, self.x, self.y, self.width, self.height)


def show_menu():
    backgrond = pygame.image.load('menu_background.jfif')

    ng_batton = Button(450, 300, 20, 5, 'New Game')
    show = True
    while show:
        for event in pygame.event.get():
            # Для закрытия программы
            if event.type == pygame.QUIT:
                show = False
