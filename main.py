import math
import pygame 
from sys import exit
from random import randint, choice

# Iniciamos pygame
pygame.init()

# Creamos una ventana
screen = pygame.display.set_mode((800, 400))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
        player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
        self.player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()
        self.player_walk = [player_walk_1, player_walk_2]
        self.player_index = 0

        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80, 300))
        self.gravity = 0

        self.jump_sound = pygame.mixer.Sound("audio/jump.mp3")
        self.jump_sound.set_volume(0.2)
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.jump_sound.play()
            self.gravity = -20

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300

    def animation_state(self):

        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]

    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        
        if type == "fly":
            fly_frame_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
            fly_frame_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210
        elif type == "snail":
            snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
            snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom = (randint(900, 1100), y_pos))

    def animation_state(self):
        self.animation_index += 0.1

        if self.animation_index >= len(self.frames): self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]

    def update(self):
        self.animation_state()
        self.rect.x -= 6 
        self.destroy()

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

# player_gravity = 0
game_active = False
start_time = 0
score = 0
bg_Music = pygame.mixer.Sound("audio/music.wav")
bg_Music.set_volume(0.2)
bg_Music.play(loops = -1)

player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

def display_score():
    current_time = pygame.time.get_ticks() - start_time
    current_time = math.floor(current_time / 1000)
    score_surf = principal_font.render(f" Score: {current_time}", False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)

    return current_time

def collision_sprite():
    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        return False
    return True

#def obstacle_movement(obstacle_list):
#    if obstacle_list:
#        for obstacle in obstacle_list:
#            obstacle.x -= 5
#
#            if obstacle.bottom == 300:
#                screen.blit(snail_surface, obstacle)
#            else:
#                screen.blit(fly_surf, obstacle)
#
#        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
#        return obstacle_list
#    return []

#def collisions(player, obstacles):
#    if obstacles:
#        for obstacle in obstacles:
#            if player.colliderect(obstacle): return False
#    return True

#def player_animation():
#    global player_surface, player_index
#
#    if player_rect.bottom < 300:
#        player_surface = player_jump
#    else:
#        player_index += 0.1
#        if player_index >= len(player_walk): player_index = 0
#        player_surface = player_walk[int(player_index)]

# Cambiamos el nombre
pygame.display.set_caption("Runner")

# Definimos clock para los frames por segundo
clock = pygame.time.Clock()

# Asignamos el tipo de fuente que vamos a usar
principal_font = pygame.font.Font("./font/Pixeltype.ttf", 50)

# De esta manera integramos imagenes -> Surface.. ademas le agregamos el metodo convert para que convierta las imagenes PNG a algo que pygame pueda leer
sky_surface = pygame.image.load("./graphics/Sky.png").convert()
ground_surface = pygame.image.load("./graphics/ground.png").convert()

# Creamos un texto. En base al tipo de fuente que elijamos. Texto - AA - Color 
#score_surface = principal_font.render(f"Score: {score_game}", False, (64, 64, 64))
#score_rect = score_surface.get_rect(center = (100, 50))

# Creacion de rectangulos y ademas a las imagenes que se ven mal se usa el convert_alpha
##snail_frame_1 = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
##snail_frame_2 = pygame.image.load("graphics/snail/snail2.png").convert_alpha()
##snail_frames = [snail_frame_1, snail_frame_2]
##snail_frame_index = 0
##snail_surface = snail_frames[snail_frame_index]
#snail_rect = snail_surface.get_rect(bottomright = (600, 300))

#fly_frame_1 = pygame.image.load("graphics/fly/fly1.png").convert_alpha()
#fly_frame_2 = pygame.image.load("graphics/fly/fly2.png").convert_alpha()
#fly_frames = [fly_frame_1, fly_frame_2]
#fly_frame_index = 0
#fly_surf = fly_frames[fly_frame_index]

# obstacle_rect_list = []

# player_walk_1 = pygame.image.load("graphics/player/player_walk_1.png").convert_alpha()
# player_walk_2 = pygame.image.load("graphics/player/player_walk_2.png").convert_alpha()
# player_jump = pygame.image.load("graphics/player/jump.png").convert_alpha()
# player_walk = [player_walk_1, player_walk_2]
# player_index = 0

# player_surface = player_walk[player_index]
# player_rect = player_surface.get_rect(midbottom = (80, 300))

player_stand = pygame.image.load("graphics/player/player_stand.png").convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center=(400,200))

game_title_surf = principal_font.render("Pixel Runner", False, (111,196,169))
game_title_rect = game_title_surf.get_rect(center = (400, 50))

reset_game_surf = principal_font.render("Reset game with SPACE", False, (111,196,169))
reset_game_rect = reset_game_surf.get_rect(center = (400, 350))

# Timer
obstacle_timer = pygame.USEREVENT
pygame.time.set_timer(obstacle_timer, 1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer, 500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer, 500)

# Se ejecutara siempre
while True:

    # Para eventos del juego
    for event in pygame.event.get():
        # Este evento comprueba si el usuario cerro el juego y no tira error
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            # Este evento permite ver cuando el jugador mueve el mouse y agarra las coordenadas del mouse con event.pos
            #if event.type == pygame.MOUSEMOTION:
                # Si el player_rect es colisionado por las coordenadas del mouse hara eso
                #if player_rect.collidepoint(event.pos):
                #    print("Hover")
            # En este caso lee cuando el mouse hace click, en caso de soltarse sera UP
            #if event.type == pygame.MOUSEBUTTONDOWN:
                #if player_rect.collidepoint(event.pos):
                #    player_gravity = -20
            if event.type == pygame.KEYDOWN:
                print("Key down")
                #if event.key == pygame.K_SPACE and player_rect.bottom == 300:
                   # player_gravity = -20
            #if event.type == pygame.KEYUP:
               # print("Key up")
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True 
                #snail_rect.left = 800 
                start_time = pygame.time.get_ticks()

        if event.type == obstacle_timer and game_active:
            obstacle_group.add(Obstacle(choice(["fly", "snail", "snail", "snail"])))
            # if randint(0, 2):
            #     obstacle_rect_list.append(snail_surface.get_rect(bottomright = (randint(900, 1100), 300)))
            # else:
            #     obstacle_rect_list.append(fly_surf.get_rect(bottomright = (randint(900, 1100), 210)))

        # if event.type == snail_animation_timer:
        #     if snail_frame_index == 0: snail_frame_index = 1
        #     else: snail_frame_index = 0
        #     snail_surface = snail_frames[snail_frame_index]

        # if event.type == fly_animation_timer:
        #     if fly_frame_index == 0: fly_frame_index = 1
        #     else: fly_frame_index = 0
        #     fly_surf = fly_frames[fly_frame_index]

    if game_active:
        # Ubicamos las imagenes en la pantalla con las coordenadas
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        #player_animation()
        #pygame.draw.rect(screen, '#c0e8ec', score_rect)
        # Vamos a dibujar y luego especificamos que dibujar, en este caso un rect. En la docu hay mas. 4to arg 6 -> border witdth / 5to arg 20 -> border radius
        #pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        #screen.blit(score_surface, score_rect)
        #pygame.draw.ellipse(screen, "Brown", pygame.Rect(50, 200, 100, 100))
        # pygame.draw.line(screen, "Pink", (0,0), pygame.mouse.get_pos(), 10)
        score = display_score()

        # Cada 1 segundo el caracol se movera -5 a left
        #snail_rect.x += -5

        # Si es menor a 0 se restartea la posicion del caracol
        #if snail_rect.right <= 0:
        #    snail_rect.left = 800

        # Para imprimir la imagen mas su rectangulo
        #screen.blit(snail_surface, snail_rect)

        #keys = pygame.key.get_pressed()

        #if keys[pygame.K_SPACE]:
        #    print("jump")

        # Detecta collisiones entre rectangulos. rectanguloquequeremoscheckear.colliderect(por el rect que va a colision con el que estamos checkeando)
        #if player_rect.colliderect(snail_rect):
        #    collision = True

        # Obtenemos la posicion del mouse con esta funcion
        #mouse_pos = pygame.mouse.get_pos()

        # checkeamos de otra manera si el mouse esta collsionando con el player
        #if player_rect.collidepoint(mouse_pos):
        # Checkeamos si esta siendo presionado el mouse
        #    print(pygame.mouse.get_pressed())

        player_gravity += 1
        # player_rect.left += 1
        # player_rect.y += player_gravity
        # if player_rect.bottom >= 300:
        #     player_rect.bottom = 300
        # screen.blit(player_surface, player_rect)
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        #obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collision
        #if snail_rect.colliderect(player_rect):
        #    start_time = pygame.time.get_ticks()
        #    game_active = False
        #game_active = collisions(player_rect, obstacle_rect_list)
        game_active = collision_sprite()
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title_surf, game_title_rect)
        screen.blit(reset_game_surf, reset_game_rect)
        #obstacle_rect_list.clear()
        #player_rect.midbottom = (80, 300)
        player_gravity = 0

        final_score_surf = principal_font.render(f"Score: {score}", False, (111,196,169))
        final_score_rect = game_title_surf.get_rect(center = (400, 80))
        if score:    
            screen.blit(final_score_surf, final_score_rect)



    # Updatea todo lo anterior
    pygame.display.update()
    # 60 imagenes por segundo
    clock.tick(60)