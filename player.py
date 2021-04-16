from gpiozero import Button

from constants import height, init_jump_velocity, gravity_accel, player_height, ground_height, max_air_time

class Player:
  def __init__(self):
    # Setup controller
    self.jump_button = Button(21)
    # This can cause multiple events while display sleeps, but that won't be a problem here
    self.jump_button.when_pressed = self.__jump

    # Setup game variables
    self.y = height - ground_height # Bottom y position
    self.y_vel = 0
    self.in_air = False
    self.air_time = 0

  def __jump(self):
    if not self.in_air:
      self.in_air = True
      self.y_vel = init_jump_velocity
      self.air_time = 0

  def update(self):
    if self.in_air:
      self.y -= self.y_vel
      if self.y_vel == 0 and self.jump_button.is_pressed and self.air_time < max_air_time:
        self.air_time += 1
      else:
        self.y_vel -= gravity_accel

      if self.y > height - ground_height:
        self.y = height - ground_height
        self.y_vel = 0
        self.in_air = False
  
  def render(self, draw):
    draw.rectangle((2, self.y - player_height, 4, self.y), outline=255, fill=255)
