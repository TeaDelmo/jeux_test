import pygame

#classe pour le projectil
class Projectile(pygame.sprite.Sprite):

    #constructeur de la classe
    def __init__(self, player):
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load('PygameAssets-main/projectile.png')
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 80
        self.origin_image = self.image
        self.angle = 0
   #     print("Projectile created at "+str(self.rect.x)+" "+str(self.rect.y))

    def rotate(self):
        #tourner le projectile
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self,dx,dy):
        self.rect.x += dx*self.velocity
        self.rect.y += dy*self.velocity 
  #      print("Projectile moved at "+str(self.rect.x)+" "+str(self.rect.y))
        self.rotate()

        #venir vérifier si l eprojectiles entre en collision avec un monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()
  #          infliger de dégats
            monster.damage(self.player.attack)

        #verifier si le projectile n'est plus présent sur l'ecran
        if self.rect.x > 1000:

            #supprimer le projectile
            self.remove()
   #         print("Projectile removed 2")