import pygame


#creer une classe qui va gerer la notion de monstre dans notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load("PygameAssets-main/mummy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 550
        self.velocity = 1/100


    def forward(self,dx,dy):
        #le deplacement se fait si y a pas de collision avec un groupe de joueur
         if not self.game.check_collision(self, self.game.all_players):
            self.rect.x += dx*self.velocity
            self.rect.y += dy*self.velocity

#        print("direction ("+str(self.rect.x)+","+str(self.rect.y)+")")