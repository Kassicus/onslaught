import pygame

import lib

class Tile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int) -> pygame.sprite.Sprite:
        super().__init__(self)

        self.pos = pygame.math.Vector2(x, y)

        self.image = pygame.Surface([32, 32])
        self.image.fill(lib.color.MEDIUM_GRAY)

        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos

    def update(self) -> None:
        pass

class Tileset():
    def __init__(self, width: int, height: int) -> object:
        self.tiles = pygame.sprite.Group()

        self.create_tiles(width, height)

    def create_tiles(self, width: int, height: int) -> None:
        for x in range(width):
            for y in range(height):
                t = Tile(x * 32, y * 32)
                self.tiles.add(t)

    def draw(self, surface: pygame.Surface) -> None:
        self.tiles.draw(surface)

    def update(self) -> None:
        self.tiles.update()