from gpiozero import Button

from constants import height, player_height, player_width, player_x_offset, init_jump_velocity, gravity_accel, max_air_time, ground_height

class Player:
  def __init__(self):
    # Setup controller
    self.jump_button = Button(21)
    # This can cause multiple events while display sleeps, but that won't be a problem here
    self.jump_button.when_pressed = self.__jump

    # Setup game variables
    self.y = height - ground_height # Bottom y position, feet should be in the ground line
    self.y_vel = 0
    self.in_air = False
    self.air_time = 0

  def __jump(self):
    if not self.in_air:
      self.in_air = True
      self.y_vel = init_jump_velocity
      self.air_time = 0

  def get_collider(self):
    return (player_x_offset, self.y - player_height, player_x_offset + player_width - 1, self.y - 1) # Move player model up 1 so on the ground

  def update(self):
    if self.in_air:
      self.y -= self.y_vel
      if self.jump_button.is_pressed and self.air_time < max_air_time:
        self.air_time += 1
      else:
        self.y_vel -= gravity_accel

        if self.y > height - ground_height:
          self.y = height - ground_height
          self.y_vel = 0
          self.in_air = False
  
  def render(self, draw):
    draw.rectangle(self.get_collider(), outline=255, fill=255)


# Unfinished implementation of jump then hold 

# def __init__(self):
#   ...
#   self.falling = False
#   self.air_hold_time = 0
#   self.air_hold_hold_time = 0

# def __jump(self):
#   if not self.in_air:
#     self.in_air = True
#     self.y_vel = init_jump_velocity
#     self.falling = False
#     self.air_time = 0
#     self.air_hold_hold_time = 0

# ...

# def update(self):
#   if self.in_air:
#     if self.jump_button.is_pressed and not self.falling:
#       if self.air_time < max_air_time:
#         self.y -= self.y_vel
#         self.y_vel = init_jump_velocity - 2
#         self.air_time += 1

#     if falling:
#       self.falling = True # Makes it so you can't click the jump button again
#       if self.y == 0 or (self.y < 0 and (self.y - self.y_vel) > 0):
#         self.y = 0
#       else:
#         self.y -= self.y_vel
#       self.y_vel -= gravity_accel

#       if self.y > height - ground_height:
#         self.y = height - ground_height
#         self.y_vel = 0
#         self.in_air = False
