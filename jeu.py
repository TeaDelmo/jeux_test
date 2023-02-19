import pygame
import math
from joueur import Player
from monster import Monster

#deuxieme classe pour le jeu 
class Game:

    def __init__(self):
        #definir ai le jeu a commencer
        self.is_playing = False
        #générer le joueur 
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.monster = Monster(self)
        self.pressed = {}
       

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
    
    def game_over(self):
        #remettre le jeu a neuf, retirer les montres, remetttre le jouer a 100 de vie et le jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
            #appliquer le joueur
        screen.blit(self.player.image, self.player.rect)

        #acctualiser la barre de vie du joueur
        self.player.update_health_bar(screen)


        #recuperer les projectiles si joueur
        for projectil in self.player.all_projectiles:
            if self.monster.rect.y < self.player.rect.y:
                dx = self.monster.rect.x - projectil.rect.x
                dy = self.monster.rect.y - projectil.rect.y - 20

            if self.monster.rect.y >= self.player.rect.y:
                dx = self.monster.rect.x - projectil.rect.x
                dy = self.monster.rect.y - projectil.rect.y

            xy = math.sqrt(math.pow(dx,2) + math.pow(dy,2))
            dx = dx/xy
            dy = dy/xy
            projectil.move(dx,dy)

        #recupérer les monstres de notre jeux
        for monster in self.all_monsters:
            dx = self.player.rect.x - monster.rect.x
            dy = self.player.rect.y - monster.rect.y + 40
            xy = math.sqrt(math.pow(dx,2) + math.pow(dy,2))
            dx = dx/xy
            dy = dy/xy
            monster.forward(dx,dy)
            monster.update_health_bar(screen)
    #     monster.forward()
    #     print("diretion monstre ("+str(dx)+","+str(dy)+")")

        #appliquer l'ensemble des images des projectiles
        self.player.all_projectiles.draw(screen)

        #appliquer l'ensbles des images du grouep de monstres
        self.all_monsters.draw(screen)

        #vérifier ou le joueur veux aller
        if self.pressed.get(pygame.K_d) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_a) and self.player.rect.x > 0:
            self.player.move_left()
        elif self.pressed.get(pygame.K_w) and self.player.rect.y > 0:
            self.player.move_up()
        elif self.pressed.get(pygame.K_s) and self.player.rect.y + 20 + self.player.rect.height < screen.get_height():
            self.player.move_down()


       
    def check_collision(self,sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
         monster = Monster(self)
         self.all_monsters.add(monster)
         