import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *



def main():

        pygame.init()
        
        
        game_clock = pygame.time.Clock() 
        dt = 0

        print("Starting asteroids!")
        print("Screen width: 1280")
        print("Screen height: 720")

        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        

        drawable = pygame.sprite.Group()
        updatable = pygame.sprite.Group()
        asteroids = pygame.sprite.Group()
        bullets = pygame.sprite.Group()

        Asteroid.containers = (asteroids, drawable, updatable)
        AsteroidField.containers = (updatable)
        asteroid_field = AsteroidField()

        Player.containers = (drawable, updatable)
        
        Shot.containers = (bullets, drawable, updatable)

        player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) 
        

        while True:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                return
                for obj in updatable:
                        obj.update(dt)

                for obj in asteroids:
                        if player.collides_with(obj):
                                print("Game over!")
                                return
                        
                for asteroid in asteroids:
                        for bullet in bullets:
                                if asteroid.collides_with(bullet):
                                        asteroid.split()
                                        bullet.kill()
                                        break

                screen.fill("black")

                for obj in drawable:
                        obj.draw(screen)

                pygame.display.flip()


                dt = game_clock.tick(60) / 1000

        

        

if __name__ == "__main__":
    main()



