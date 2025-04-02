import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()
    
    #GAME LOOP
    while True:
        #Check quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        # Fill background
        pygame.Surface.fill(screen, (0,0,0))
        
        #Update all objects positions
        updatable.update(dt)
        
        # Check if player has collided with asteroids
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                return
            for shot in shots:
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
            
        # Draw the items on the screen
        for item in drawable:
            item.draw(screen)
            
        # Update clock
        dt = clock.tick(60)/1000
        
        #Refresh screen
        pygame.display.flip()



if __name__ == "__main__":
    main()