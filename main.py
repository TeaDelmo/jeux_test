import pygame
import math
from jeu import Game
pygame.init()

# generation de la fenetre du jeu
pygame.display.set_caption("jeu test")
screen = pygame.display.set_mode((1080, 720))

#arrière plan
background = pygame.image.load('PygameAssets-main/bg.jpg')

#jeu
game = Game()

running = True

#boucle tant que c'est vrai
while running:

    #appliquer l'arrière plan 
    screen.blit(background, (0,-200))

    #appliquer le joueur
    screen.blit(game.player.image, game.player.rect)

    #recuperer les projectiles si joueur
    for projectil in game.player.all_projectiles:
        dx = game.monster.rect.x - projectil.rect.x
        dy = game.monster.rect.y - projectil.rect.y
        xy = math.sqrt(math.pow(dx,2) + math.pow(dy,2))
        dx = dx/xy
        dy = dy/xy
        projectil.move(dx,dy)

    #recupérer les monstres de notre jeux
    for monster in game.all_monsters:
        dx = game.player.rect.x - monster.rect.x
        dy = game.player.rect.y - monster.rect.y 
        xy = math.sqrt(math.pow(dx,2) + math.pow(dy,2))
        dx = dx/xy
        dy = dy/xy
        monster.forward(dx,dy)
 #     monster.forward()
 #     print("diretion monstre ("+str(dx)+","+str(dy)+")")

    #appliquer l'ensemble des images des projectiles
    game.player.all_projectiles.draw(screen)

    #appliquer l'ensbles des images du grouep de monstres
    game.all_monsters.draw(screen)

    #vérifier ou le joueur veux aller
    if game.pressed.get(pygame.K_d) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_a) and game.player.rect.x > 0:
        game.player.move_left()
    elif game.pressed.get(pygame.K_w) and game.player.rect.y > 0:
        game.player.move_up()
    elif game.pressed.get(pygame.K_s) and game.player.rect.y + 20 + game.player.rect.height < screen.get_height():
        game.player.move_down()

#   print(game.player.rect.x)

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