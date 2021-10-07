import pygame as pg
import numpy as np


class SnakeHead:
    def __init__(self, x, y, segment_size):
        self.size = segment_size
        self.head = pg.surfarray.make_surface(np.ones((segment_size, segment_size)) * 255)
        self.segments = []
        self.x = x
        self.y = y
        self.previous_x = 0
        self.previous_y = 0
        self.score = 0
        self.height = segment_size
        self.width = segment_size
        self.shape = pg.Rect(self.x, self.y, self.width, self.height)

    def draw_head(self, screen):
        screen.blit(self.head, (self.x, self.y))

    def move_x(self, move_dx):
        self.previous_x = self.x
        self.x = self.x + move_dx

    def move_y(self, move_dy):
        self.previous_y = self.y
        self.y = self.y + move_dy

    def update(self):
        self.shape = pg.Rect(self.x, self.y, self.width, self.height)


class SnakeSegment:
    def __init__(self, x, y, segment_size):
        self.head = pg.surfarray.make_surface(np.ones((segment_size, segment_size)) * 255)
        self.x = x
        self.y = y
        self.previous_x = 0
        self.previous_y = 0
        self.height = 10
        self.width = 10
        self.shape = pg.Rect(self.x, self.y, self.width, self.height)

    def draw_segment(self, screen):
        screen.blit(self.head, (self.x, self.y))

    def update(self):
        self.shape = pg.Rect(self.x, self.y, self.width, self.height)

    def collide(self, snake_head):
        if self.shape.colliderect(snake_head):
            return True
        else:
            return False


class Food:
    def __init__(self, x, y):
        self.food = pg.surfarray.make_surface(np.ones((5, 5)) * 255)
        self.x = x
        self.y = y
        self.height = 5
        self.width = 5
        self.shape = pg.Rect(self.x, self.y, self.width, self.height)

    def draw_food(self, screen):
        screen.blit(self.food, (self.x, self.y))

    def collide(self, snake_head):
        if self.shape.colliderect(snake_head):
            return True
        else:
            return False


class Wall:
    def __init__(self, x, y):
        self.wall = pg.surfarray.make_surface(np.ones((5, 5)) * 255)
        self.x = x
        self.y = y
        self.height = 3
        self.width = 3
        self.shape = pg.Rect(self.x, self.y, self.width, self.height)

    def draw_wall(self, screen):
        screen.blit(self.wall, (self.x, self.y))

    def collide(self, snake_object):
        if self.shape.colliderect(snake_object):
            return True
        else:
            return False
