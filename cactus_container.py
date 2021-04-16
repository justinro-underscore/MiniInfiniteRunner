from random import random
from math import floor

from moving_objects.cactus import Cactus
from constants import height, width, ground_height, ground_speed, max_ground_mark_length, cactus_space, cactus_height

class CactusContainer:
  def __init__(self):
    self.cacti = [Cactus()]
    self.wait_count = cactus_space

  def __move_ground_marks(self):
    pop = False # Defines if we should pop the first ground mark off the queue (if it's gone offscreen)
    for cactus in self.cacti:
      if cactus.move():
        pop = True
    if pop:
      self.cacti.pop()

  def update(self):
    self.__move_ground_marks()
    self.wait_count -= ground_speed
    if self.wait_count <= 0:
      self.cacti = [Cactus()] + self.cacti
      self.wait_count = cactus_space

  def render(self, draw):
    for cactus in self.cacti:
      cactus.render(draw)