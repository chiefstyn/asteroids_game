import pygame

def main():

        pygame.init()
        print("Starting asteroids!")
        print("Screen width: 1280")
        print("Screen height: 720")

        screen = pygame.display.set_mode((1280, 720))
        

        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return
                screen.fill((0, 0, 0))
                pygame.display.flip()

if __name__ == "__main__":
    main()