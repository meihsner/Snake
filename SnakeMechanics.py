from SnakeObjects import *
import random
import os
import copy


def type_text(text, x, y, font_size, color, screen):
    font = pg.font.SysFont("Arial", font_size)
    rend = font.render(text, True, color)
    screen.blit(rend, (x, y))


def game(screen, snake, fps_number, width, height, game_state, food):
    up = False
    down = False
    right = False
    left = False
    dx = 0
    dy = 0
    clock = pg.time.Clock()
    high_score = 0

    wall_list = []
    for i in range(0, width):
        wall_list.append(Wall(i, 0))
        wall_list.append(Wall(i, 40))
        wall_list.append(Wall(i, height - 5))
    for j in range(0, height):
        wall_list.append(Wall(0, j))
        wall_list.append(Wall(width - 5, j))

    while True:
        clock.tick(fps_number)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if game_state == "menu":
                        game_state = "game"
                    if game_state == "game_over":
                        food = Food(random.randint(10, width - 10), random.randint(50, height - 10))
                        dx = 0
                        dy = 0
                        game_state = "game"
                elif event.key == pg.K_UP:
                    if game_state == "game":
                        if down is False:
                            dy = -4
                            dx = 0
                            up = True
                            down = False
                            right = False
                            left = False
                elif event.key == pg.K_DOWN:
                    if game_state == "game":
                        if up is False:
                            dy = 4
                            dx = 0
                            up = False
                            down = True
                            right = False
                            left = False
                elif event.key == pg.K_RIGHT:
                    if game_state == "game":
                        if left is False:
                            dx = 4
                            dy = 0
                            up = False
                            down = False
                            right = True
                            left = False
                elif event.key == pg.K_LEFT:
                    if game_state == "game":
                        if right is False:
                            dx = -4
                            dy = 0
                            up = False
                            down = False
                            right = False
                            left = True

        if game_state == "menu":
            screen.fill((0, 0, 0))
            type_text("SNAKE", 100, 100, 50, (255, 255, 255), screen)
            type_text("Press space, to continue...", 70, 350, 20, (255, 255, 255), screen)
            logo = pg.image.load(os.path.join('snake.png'))
            screen.blit(logo, (130, 200))

        elif game_state == "game":
            screen.fill((0, 0, 0))
            type_text("Score: " + str(snake.score), 240, 10, 20, (255, 255, 255), screen)
            type_text("High score: " + str(high_score), 10, 10, 20, (255, 255, 255), screen)
            for i in range(0, len(wall_list)):
                wall_list[i].draw_wall(screen)
            food.draw_food(screen)
            snake.draw_head(screen)
            if len(snake.segments) != 0:
                for i in range(0, len(snake.segments)):
                    if i == 0:
                        snake.segments[i].draw_segment(screen)
                        tmp_x = copy.deepcopy(snake.segments[i].x)
                        tmp_y = copy.deepcopy(snake.segments[i].y)
                        snake.segments[i].previous_x = tmp_x
                        snake.segments[i].previous_y = tmp_y
                        snake.segments[i].x = snake.previous_x
                        snake.segments[i].y = snake.previous_y
                        snake.segments[i].update()

                    else:
                        snake.segments[i].draw_segment(screen)
                        tmp_x = copy.deepcopy(snake.segments[i].x)
                        tmp_y = copy.deepcopy(snake.segments[i].y)
                        snake.segments[i].previous_x = tmp_x
                        snake.segments[i].previous_y = tmp_y
                        snake.segments[i].x = snake.segments[i - 1].previous_x
                        snake.segments[i].y = snake.segments[i - 1].previous_y
                        snake.segments[i].update()

            snake.move_x(dx)
            snake.move_y(dy)
            snake.update()
            if food.collide(snake.shape):
                snake.score = snake.score + 1
                if high_score < snake.score:
                    high_score = snake.score
                if snake.score % 2 == 0:
                    fps_number = fps_number + 1
                if len(snake.segments) == 0:
                    snake.segments.append(SnakeSegment(snake.previous_x, snake.previous_y, snake.size))
                else:
                    snake.segments.append(SnakeSegment(snake.segments[len(snake.segments) - 1].previous_x,
                                                       snake.segments[len(snake.segments) - 1].previous_y, snake.size))

                food = Food(random.randint(5, width - 5), random.randint(45, height - 5))

            for wall in wall_list:
                if wall.collide(snake.shape):
                    game_state = "game_over"

            if len(snake.segments) > 0:
                for i in range(0, len(snake.segments)):
                    if i > 3:
                        if snake.segments[i].collide(snake.shape):
                            game_state = "game_over"

        elif game_state == "game_over":
            screen.fill((0, 0, 0))
            type_text("GAME OVER", 30, 100, 50, (255, 255, 255), screen)
            type_text("Your score: " + str(snake.score), 120, 180, 20, (255, 255, 255), screen)
            type_text("High score: " + str(high_score), 120, 240, 20, (255, 255, 255), screen)
            type_text("Press space, to try again...", 70, 350, 20, (255, 255, 255), screen)

        pg.display.update()
