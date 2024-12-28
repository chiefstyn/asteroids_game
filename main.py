import pygame

def main():

        pygame.init()
        
        game_clock = pygame.time.Clock() 
        dt = 0

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
                dt = game_clock.tick(60) / 1000

if __name__ == "__main__":
    main()



