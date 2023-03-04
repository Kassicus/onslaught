import pygame

import lib

class Player(pygame.sprite.Sprite):
    def __init__(self) -> pygame.sprite.Sprite:
        super().__init__()

        self.pos = pygame.math.Vector2(lib.SCREEN_SIZE.x / 2, lib.SCREEN_SIZE.y / 2)
        self.vel = pygame.math.Vector2()

        self.max_speed = 200
        self.accel = 20
        self.friction = 5

        self.image = pygame.Surface([25, 35])
        self.image.fill(lib.color.CYAN)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def physics(self) -> None:
        if self.vel.x > 0:
            self.vel.x -= self.friction
            if self.vel.x > self.max_speed:
                self.vel.x = self.max_speed
        elif self.vel.x < 0:
            self.vel.x += self.friction
            if self.vel.x < -self.max_speed:
                self.vel.x = -self.max_speed

    def event_handler(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.vel.x -= self.accel
        elif keys[pygame.K_d]:
            self.vel.x += self.accel

    def update(self) -> None:
        self.pos += self.vel * lib.delta_time
        self.rect.center = self.pos

        self.event_handler()
        self.physics()
        