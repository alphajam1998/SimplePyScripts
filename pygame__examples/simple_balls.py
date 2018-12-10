#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


from random import randint

# pip install pygame
import pygame


class Ball:
    def __init__(self, x, y, r, v_x, v_y, color):
        self.x = x
        self.y = y
        self.r = r
        self.v_x = v_x
        self.v_y = v_y
        self.color = color

    def update(self):
        self.x += self.v_x
        self.y += self.v_y

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.r)

        # Нарисуем поверх первого, прозрачный второй с границей (параметр width)
        pygame.draw.circle(surface, (0, 0, 0), self.center, self.r, 1)

    @property
    def center(self):
        return self.x, self.y

    @property
    def top(self):
        return self.y - self.r

    @property
    def bottom(self):
        return self.y + self.r

    @property
    def left(self):
        return self.x - self.r

    @property
    def right(self):
        return self.x + self.r


class Game:
    def __init__(self, width: int, height: int, caption='Balls!', background_color=(255, 255, 255), frame_rate=60):
        self.width = width
        self.height = height
        self.frame_rate = frame_rate

        self.surface = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

        self.caption = caption
        self.background_color = background_color

        self.game_active = False

        self.balls = []

        pygame.init()

        self.update_caption()

    def update_caption(self):
        pygame.display.set_caption("{} [{} fps]".format(self.caption, int(self.clock.get_fps())))

    def update(self):
        for o in self.balls:
            o.update()

    def draw(self):
        for o in self.balls:
            o.draw(self.surface)

    def run(self):
        self.game_active = True

        while True:
            for event in pygame.event.get():  # получение всех событий
                if event.type == pygame.QUIT:  # проверка события "Выход"
                    self.game_active = False
                    break

            is_pressed = pygame.key.get_pressed()
            if is_pressed[pygame.K_ESCAPE]:
                self.game_active = False

            if not self.game_active:
                break

            self.surface.fill(self.background_color)

            for ball in self.balls:
                ball.draw(self.surface)
                ball.update()

                # Условия отскакивания шарика от левого и правого края
                if ball.left <= 0 or ball.right >= self.width:
                    ball.v_x = -ball.v_x

                # Условия отскакивания шарика верхнего и нижнего края
                if ball.top <= 0 or ball.bottom >= self.height:
                    ball.v_y = -ball.v_y

            self.update_caption()
            pygame.display.update()

            self.clock.tick(self.frame_rate)
            pygame.event.pump()

    def append_random_ball(self):
        def get_random_vector():
            pos = 0, 0
            # Если pos равен (0, 0), пересчитываем значения, т.к. шарик должен двигаться
            while pos == (0, 0):
                pos = randint(-3, 3), randint(-3, 3)

            return pos

        def get_random_color():
            return randint(0, 255), randint(0, 255), randint(0, 255)

        x = self.width // 2 + randint(-self.width // 4, self.width // 4)
        y = self.height // 2 + randint(-self.height // 4, self.height // 4)
        r = randint(10, 20)
        v_x, v_y = get_random_vector()
        color = get_random_color()

        ball = Ball(x, y, r, v_x, v_y, color)
        self.balls.append(ball)


if __name__ == '__main__':
    WIDTH = 600   # ширина экрана
    HEIGHT = 600  # высота экрана
    BALL_NUMBER = 100

    game = Game(WIDTH, HEIGHT)

    for i in range(BALL_NUMBER):
        game.append_random_ball()

    game.run()
