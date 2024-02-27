import math
import pygame 

from sys import exit
from random import choice, randint
from models.player import Player
from models.obstacle import Obstacle
from models.power import Power
from utils import utils


pygame.init()

screen = pygame.display.set_mode((800, 400))

# Variables
game_active = False
start_time = 0
score = 0

bg_music = pygame.mixer.Sound("./src/audio/music.wav")
bg_music.set_volume(0.1)

game_over_music = pygame.mixer.Sound("./src/audio/game_over.mp3")

obstacle_kill = pygame.mixer.Sound("./src/audio/kill_obstacle.mp3")

# Groups
player = pygame.sprite.GroupSingle()

player_structure = utils.player_structure()
player_object = Player(
   player_jump = player_structure["jump_frame"],
   player_walk_frames = player_structure["frames"],
   jump_sound = player_structure["jump_sound"]
)
player_object.init_player()

player.add(player_object)
character = player.sprites()[0]

power_coin = pygame.sprite.GroupSingle()
power = None

obstacle_group = pygame.sprite.Group()


def display_score() -> int:
    current_time = pygame.time.get_ticks() - start_time
    current_time = math.floor(current_time / 1000)
    score_surf = principal_font.render(f" Score: {current_time}", False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400, 50))
    screen.blit(score_surf, score_rect)

    return current_time


def collision_sprite() -> bool:

    if power:
        if power.immunity:
            power.power_stop(score)
            return True
        if power.killer:
            power.power_stop(score)

            if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
                for obstacle in obstacle_group:
                    if pygame.sprite.collide_rect(player.sprite, obstacle):
                        obstacle_kill.play()
                        obstacle.kill()
                        return True

    if pygame.sprite.spritecollide(player.sprite, obstacle_group, False):
        obstacle_group.empty()
        power_coin.empty()
        game_over_music.play()
        bg_music.stop()
        return False

    return True


pygame.display.set_caption("Runner")
clock = pygame.time.Clock()

principal_font = pygame.font.Font("./src/font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("./src/graphics/Sky.png").convert()
ground_surface = pygame.image.load("./src/graphics/ground.png").convert()

# Lose Screen
player_stand = pygame.image.load("./src/graphics/player/player_stand.png").convert_alpha()
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

power_timer = pygame.USEREVENT + 4
pygame.time.set_timer(power_timer, randint(15000, 30000))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if not game_active:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True 
                character.rect.x = 80
                start_time = pygame.time.get_ticks()
                bg_music.play(loops = -1)
                game_over_music.stop()

        if event.type == obstacle_timer and game_active:
            if score >= 0 and score <= 10:
                list_of_obstacles = ["snail"]
            if score == 10:
                list_of_obstacles.append("fly")
            if score == 20:
                list_of_obstacles.append("grounder")

            chosen_obstacle = choice(list_of_obstacles)
            obstacle_values = utils.get_obstacle_type(chosen_obstacle)

            obstacle = Obstacle(
                type = chosen_obstacle,
                frames = obstacle_values["frames"],
                y_pos = obstacle_values["y_pos"],
            )

            obstacle_group.add(obstacle)
            obstacle.init_obstacle()

        if event.type == power_timer and game_active and not power_coin:
            power_structure = utils.power_structure()
            power_object = Power(
                frames = power_structure["frames"],
                y_pos = power_structure["y_pos"],
                power_sound = power_structure["power_sound"]
            )
            power_object.init_power()
            power_coin.add(power_object)
            power = power_coin.sprites()[0]

    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))

        score = display_score()

        #player_gravity += 1 # ??

        # Draw
        player.draw(screen)
        player.update()
        
        if power:
            character.change_skin_player(power)

        obstacle_group.draw(screen)
        obstacle_group.update(score)

        power_coin.draw(screen)
        power_coin.update(player)

        # Si sigue activo
        game_active = collision_sprite()
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand, player_stand_rect)
        screen.blit(game_title_surf, game_title_rect)
        screen.blit(reset_game_surf, reset_game_rect)

        player_gravity = 0

        final_score_surf = principal_font.render(f"Score: {score}", False, (111,196,169))
        final_score_rect = game_title_surf.get_rect(center = (400, 80))
        if score:    
            screen.blit(final_score_surf, final_score_rect)


    pygame.display.update()
    # Frames. 60 FPS
    clock.tick(60)