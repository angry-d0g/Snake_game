import pygame

# Окно программы
pygame.init()
windowX = 500
windowY = 500
delay = 100
dis = pygame.display.set_mode((windowX, windowY))
pygame.display.set_caption('Змейка')

# FPS
# pygame.time.delay(1000)
# clock = pygame.time.Clock()
# FPS = 10

# Картинка
image = pygame.image.load('game_over.webp')

# Размеры одной клетки змейки
sizeX, sizeY = (20, 20)  # ТОЛЬКО ЧЕТНЫЕ ЧИСЛА!

# Радиус яблока
radius = 9

# нахождение центральной ячейки для змейки
gridCountX = int(windowX // sizeY)  # 500//20 == 25 -количество ячеек
gridCountY = int(windowY // sizeY)
gridCetnre = (int(gridCountX // 2) * sizeX, int(gridCountY // 2) * sizeY)
print(gridCetnre)

# нахождение центров ячеек для яблок
appleX = [i for i in range(sizeX // 2, windowX, sizeX)]
appleY = [i for i in range(sizeY // 2, windowY, sizeY)]

# сетка
gray = (50, 50, 50)


def grid():
    
    for i in range(0, windowX, sizeX):
        pygame.draw.aaline(dis, gray, [i, 0], [i, windowY])
    for j in range(0, windowY, sizeY):
        pygame.draw.aaline(dis, gray, [0, j], [windowX, j])
