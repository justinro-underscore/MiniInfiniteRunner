from PIL import ImageFont

height = 32 # Height of the OLED
width = 128 # Width of the OLED
frame_rate_constant = 0.01 # How long between frames

player_height = 5 # Height of the player (in pixels)
player_width = 3 # Width of the player (in pixels)
player_x_offset = 2 # Offset of the player's starting position

init_jump_velocity = 8 # Initial jump velocity
gravity_accel = 2 # Acceleration due to gravity
max_air_time = 10 # For how many frames the player is allowed to stay in the air

ground_height = 5 # Height of the ground (in pixels)
init_ground_speed = 2 # How fast the ground should be moving at the start

ground_mark_probability = 0.2 # Probability of if a ground mark should be generated
max_ground_mark_length = 6 # Longest ground mark that can be made

cactus_height = 10
init_cactus_space = 50
cactus_space_increment = 20

score_speed_increases = [
  300,
  500,
  700,
  800,
  900,
  950,
  1000,
  1050,
  1100
]

font = ImageFont.load_default()