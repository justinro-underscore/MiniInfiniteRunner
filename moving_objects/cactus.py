from moving_object import MovingObject
from constants import height, width, ground_height, max_ground_mark_length, cactus_height

class Cactus(MovingObject):
  def __init__(self):
    y = height - ground_height
    # TODO Make a bounding box for collisions
    MovingObject.__init__(self, y, max_ground_mark_length, cactus_height)
