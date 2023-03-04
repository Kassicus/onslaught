import pygame

import lib
import player

pygame.init()

class Game():
    def __init__(self) -> object:
        self.screen = pygame.display.set_mode(lib.SCREEN_SIZE)
        pygame.display.set_caption("ONSLAUGHT")

        self.running = True
        self.clock = pygame.time.Clock()
        lib.events = pygame.event.get()

        self.player = pygame.sprite.Group()
        self.player.add(player.Player())
        
    def run(self) -> None:
        while self.running:
            self.event_loop()
            self.draw()
            self.update()

    def event_loop(self) -> None:
        lib.events = pygame.event.get()
        
        for event in lib.events:
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def draw(self) -> None:
        self.screen.fill(lib.color.BLACK)

        self.player.draw(self.screen)

    def update(self) -> None:
        self.player.update()

        pygame.display.update()
        lib.delta_time = self.clock.tick(lib.fps_limit) / 1000

if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()