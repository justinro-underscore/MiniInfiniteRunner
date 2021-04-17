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

  def __get_render_collider(self):
    return (self.x, self.y - self.height + 1, self.x + self.length - 1, self.y)

  # Could be overwritten
  def get_collider(self):
    return self.__get_render_collider()

  def render(self, draw):
    if self.height == 1:
      draw.line(self.__get_render_collider(), fill=255, width=1)
    else:
      draw.rectangle(self.__get_render_collider(), outline=255, fill=0)
