import pygame
def main():
        print("Starting asteroids!")
        print("Screen width: 1280")
        print("Screen height: 720")
pygame.init
from constants import *
screen = pygame.display.set_mode((1280, 720))

if __name__ == "__main__":
    main()

def main():
        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return
                screen.fill((0, 0, 0))
                pygame.display.flip()

main()
        