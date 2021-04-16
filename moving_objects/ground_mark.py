from random import random
from math import floor

from moving_object import MovingObject
from constants import height, width, ground_height, ground_mark_probability, max_ground_mark_length

class GroundMark(MovingObject):
  def __init__(self):
    y = height - floor(random() * (ground_height - 2)) - 1
    MovingObject.__init__(self, y, max_ground_mark_length, 1)
