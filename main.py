from menu import Button
from classes import *
from settings import *

player = Snake()
food = Apple()
ng_batton = Button(450, 300, 35, 10, 'New Game')


gamePause = False
runGame = True
while runGame:
    for event in pygame.event.get():
        # Для закрытия программы
        if event.type == pygame.QUIT:
            #runGame = False
            pygame.quit()
            quit()

        # mouse = pygame.mouse.get_pos()
        # click = pygame.mouse.get_pressed()
        #
        # if ng_batton.x < mouse[0] < ng_batton.width and ng_batton.y < mouse[1] < ng_batton.height:
        #     pygame.draw.rect(dis, ng_batton.active_clr, [ng_batton.x, ng_batton.y, ng_batton.width, ng_batton.height])
        #     if click[0] == 1:
        #         pass
        # else:
        #     pygame.draw.rect(dis, ng_batton.inactive_clr, [ng_batton.x, ng_batton.y, ng_batton.width, ng_batton.height])

        # Передвижение по стрелкам
        if event.type == pygame.KEYDOWN:
            gamePause = False
            if event.key == pygame.K_RIGHT and player.movex != -sizeX:
                player.right()
            elif event.key == pygame.K_LEFT and player.movex != sizeX:
                player.left()
            elif event.key == pygame.K_DOWN and player.movey != -sizeY:
                player.down()
            elif event.key == pygame.K_UP and player.movey != sizeY:
                player.up()
            elif event.key == pygame.K_SPACE and not player.gameOver:  # Постановка на паузу
                gamePause = True
            elif event.key == pygame.K_SPACE:  # начало новой игры
                player.new_game()



    if not gamePause and not player.gameOver:

        # if not food.onScreen:
        food.newApple()

        grid()
        player.block_move()
        if player.x + sizeX // 2 == food.x and player.y + sizeY // 2 == food.y:
            food.death()
            if[food.x + sizeX//2, food.y + sizeY//2] in player.body:
                while [food.x + sizeX//2, food.y + sizeY//2] in player.body:
                    food.death()
                    print(3482093482)
            player.addBlock()

        pygame.display.update()

    dis.fill('black')
    pygame.time.delay(delay)  # clock.tick(FPS)

pygame.quit()
