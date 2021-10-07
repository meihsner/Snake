from SnakeMechanics import *


def main():
    pg.init()
    size = width, height = 320, 480
    pg.display.set_caption('Snake')
    screen = pg.display.set_mode(size)

    game_state = "menu"
    snake = SnakeHead(100, 100, 10)
    food = Food(random.randint(10, width-10), random.randint(50, height-10))
    fps_number = 20

    game(screen, snake, fps_number, width, height, game_state, food)


if __name__ == "__main__":
    main()
