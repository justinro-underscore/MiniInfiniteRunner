from constants import width, ground_speed

# Abstract class
class MovingObject:
  def __init__(self, y, length, height, moving_speed=ground_speed):
    self.x = width
    self.y = y
    self.length = length
    self.height = height
    self.moving_speed = moving_speed

  def move(self):
    self.x -= self.moving_speed

  # Returns true if it has fully gone offscreen
  def is_offscreen(self):
    return (self.x + self.length - 1) < 0

  def render(self, draw):
    if self.height == 1:
      draw.line((self.x, self.y, self.x + self.length - 1, self.y), fill=255, width=1)
    else:
      draw.rectangle((self.x, self.y - self.height, self.x + self.length - 1, self.y - 1), outline=255, fill=0)
