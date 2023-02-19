import pygame
import random


#creer une classe qui va gerer la notion de monstre dans notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load("PygameAssets-main/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 550 
        self.velocity = random.randint(1, 5)

    def damage(self, amount):
        #infliger les degats
        self.health -= amount

        #verifier si son nouveau nombre de point de vie est inferieur ou egale a 0
        if self.health <= 0:
            #reapparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1,5)
            self.health = self.max_health

    def update_health_bar(self, surface):
        #definir une couleur pour la jaufe de vie
        bar_color = (11, 100, 10)
       # definir une couleur pour l'arrière plan de la jauge
        back_bar_color = (60, 63, 60)

        #définir la position de la jauge et sa largeur et epaisseur
        bar_position = [self.rect.x + 10, self.rect.y - 10, self.health, 5]
        #definnir la position de l'arrere plan de la jauge de vie
        back_bar_position = [self.rect.x + 10, self.rect.y - 10, self.max_health, 5]

        #dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)

    def forward(self,dx,dy):
        #le deplacement se fait si y a pas de collision avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x += dx*self.velocity
            self.rect.y += dy*self.velocity
        #si le monstre est en collision avec le jouer
        else:
           # infliger des degats
           self.game.player.damage(self.attack)