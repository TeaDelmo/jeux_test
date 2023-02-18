import pygame
from progectil import Projectile

#premiere classe pour le jouer
class Player(pygame.sprite.Sprite):


    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('PygameAssets-main/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 440
        self.rect.y = 500

    def launch_projectil(self):
        #nouvelle instance de progectile 
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity

    def move_up(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.y -= self.velocity
    
    def move_down(self):
        self.rect.y += self.velocity 