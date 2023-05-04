# Example file showing a basic pygame "game loop"
import pygame
import os

# pygame setup
pygame.init()
WIDTH, HEIGHT = 1280, 720
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60


def draw_window():
    # fill the screen with a color to wipe away anything from last frame
    WIN.fill("white")

    # RENDER YOUR GAME HERE

    pygame.display.update()


def main():
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)  # limits FPS to 60
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        draw_window()

    pygame.quit()

if __name__ == '__main__':
    main()


