from src.core.config import resource_path

ROOT = "./src"
ROOT_ASSETS = f"{ROOT}/assets"

# --- Player ---

PLAYER_WALK_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/player/normal/player_walk_1.png"
)
PLAYER_WALK_2 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/player/normal/player_walk_2.png"
)
PLAYER_JUMP_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/player/normal/jump.png"
)
PLAYER_STAND_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/player/normal/player_stand.png"
)

PLAYER_IMMUNITY_WALK_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/player/immunity/player_walk_1.png"
)
PLAYER_IMMUNITY_WALK_2 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/player/immunity/player_walk_2.png"
)
PLAYER_IMMUNITY_JUMP_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/player/immunity/jump.png"
)

PLAYER_KILLER_WALK_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/player/killer/player_walk_1.png"
)
PLAYER_KILLER_WALK_2 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/player/killer/player_walk_2.png"
)
PLAYER_KILLER_JUMP_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/player/killer/jump.png"
)

# --- Snail ---

SNAIL_ANIMATION_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/obstacles/snail/snail1.png"
)
SNAIL_ANIMATION_2 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/obstacles/snail/snail2.png"
)

# --- Bat ---

BAT_ANIMATION_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/obstacles/bat/bat1.png"
)
BAT_ANIMATION_2 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/obstacles/bat/bat2.png"
)

# --- Grounder ---

GROUNDER_ANIMATION_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/obstacles/grounder/grounder1.png"
)
GROUNDER_ANIMATION_2 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/obstacles/grounder/grounder2.png"
)
GROUNDER_ANIMATION_3 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/obstacles/grounder/grounder3.png"
)
GROUNDER_ANIMATION_4 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/obstacles/grounder/grounder4.png"
)
GROUNDER_ANIMATION_5 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/obstacles/grounder/grounder5.png"
)
GROUNDER_ANIMATION_6 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/obstacles/grounder/grounder6.png"
)

# --- Power ---

POWER_MISTERY_ANIMATION_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/powers/mistery/mistery1.png"
)
POWER_MISTERY_ANIMATION_2 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/powers/mistery/mistery2.png"
)
POWER_MISTERY_ANIMATION_3 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/powers/mistery/mistery3.png"
)
POWER_MISTERY_ANIMATION_4 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/powers/mistery/mistery4.png"
)
POWER_MISTERY_ANIMATION_5 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/powers/mistery/mistery5.png"
)
POWER_MISTERY_ANIMATION_6 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/powers/mistery/mistery6.png"
)
POWER_MISTERY_ANIMATION_7 = resource_path(
    relative_path=f"{ROOT_ASSETS}/graphics/powers/mistery/mistery7.png"
)

POWER_PICK_SOUND_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/audio/powers/powerup.mp3"
)

# --- Audios ---

PLAYER_JUMP_SOUND_1 = resource_path(
    relative_path=f"{ROOT_ASSETS}/audio/player/jump.mp3"
)
BG_GAME_SOUND = resource_path(relative_path=f"{ROOT_ASSETS}/audio/general/music.wav")
GAME_OVER_GAME_SOUND = resource_path(
    relative_path=f"{ROOT_ASSETS}/audio/general/game_over.mp3"
)
OBSTACLE_KILL_SOUND = resource_path(
    relative_path=f"{ROOT_ASSETS}/audio/obstacles/kill_obstacle.mp3"
)

# --- Fonts ---

PRIMARY_FONT = resource_path(relative_path=f"{ROOT_ASSETS}/font/Pixeltype.ttf")

# --- Map ---

SKY = resource_path(relative_path=f"{ROOT_ASSETS}/graphics/map/sky.png")
GROUND = resource_path(relative_path=f"{ROOT_ASSETS}/graphics/map/ground.png")
