import pygame
import math
from jeu import Game
pygame.init()

# generation de la fenetre du jeu
pygame.display.set_caption("jeu test")
screen = pygame.display.set_mode((1080, 720))

#arrière plan
background = pygame.image.load('PygameAssets-main/bg.jpg')

#importer charger la bannière
banner = pygame.image.load('PygameAssets-main/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)

# importer charger le bonton pour lancer la partie
play_button = pygame.image.load('PygameAssets-main/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)
#jeu
game = Game()

running = True

#boucle tant que c'est vrai
while running:

    #appliquer l'arrière plan 
    screen.blit(background, (0,-200))

    #verifier si le jeu a commence ou non
    if game.is_playing:
        # declencher les instrucions de la partie
        game.update(screen)
    #verifier si notre jeu n'a pa commencer
    else:
        #ajouter l'ecran de bienvenue
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    #mettre a jour l'écran
    pygame.display.flip()

    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        #evenement fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeu")

         #si le joueur lache la touche du clavier 
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
         
            #lancer le projectil si espace est appuiee
            if event.key == pygame.K_SPACE:
                game.player.launch_projectil()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #la souris esr en collision avec le buuton
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lance
                game.start()