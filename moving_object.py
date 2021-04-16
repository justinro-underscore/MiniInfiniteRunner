from constants import width

# Abstract class
class MovingObject:
  def __init__(self, y, length, height):
    self.x = width
    self.y = y
    self.length = length
    self.height = height

  def move(self, speed):
    self.x -= speed

  # Returns true if it has fully gone offscreen
  def is_offscreen(self):
    return (self.x + self.length - 1) < 0

  def render(self, draw):
    if self.height == 1:
      draw.line((self.x, self.y, self.x + self.length - 1, self.y), fill=255, width=1)
    else:
      draw.rectangle((self.x, self.y - self.height, self.x + self.length - 1, self.y - 1), outline=255, fill=0)
