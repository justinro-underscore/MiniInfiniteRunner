from random import random

from moving_objects.ground_mark import GroundMark
from moving_objects.cactus import Cactus
from constants import height, width, ground_height, init_ground_speed, ground_mark_probability, max_ground_mark_length, cactus_space

class Ground:
  def __init__(self):
    self.ground_speed = init_ground_speed

    self.ground_marks = [GroundMark()]
    self.curr_ground_length = 0
    self.generating_ground_marks = False

    self.cacti = []
    self.cactus_wait_count = cactus_space

  def __move_objects(self):
    for moving_object in self.ground_marks + self.cacti:
      moving_object.move(self.ground_speed)

    if len(self.ground_marks) > 0 and self.ground_marks[0].is_offscreen():
      self.ground_marks = self.ground_marks[1:]
    if len(self.cacti) > 0 and self.cacti[0].is_offscreen():
      self.cacti = self.cacti[1:]

  def __generate_ground_marks(self):
    # If not currently generating a ground mark...
    if not self.generating_ground_marks:
      # Set the ground mark length to what is currently shown on screen
      self.curr_ground_length += self.ground_speed
      # Use linear interpolation to see if we should cut off the ground mark at its current length
      probability = self.curr_ground_length / max_ground_mark_length
      end_mark = random() < probability
      # If we should cut off the mark...
      if end_mark:
        # Set the ground mark's length to its current length
        self.ground_marks[len(self.ground_marks) - 1].length = self.curr_ground_length
        # Reset to prepare for generating a new ground mark
        self.generating_ground_marks = True

    # If currently generating a ground mark and we should place a new ground mark
    if self.generating_ground_marks and random() < ground_mark_probability:
      # Append a new ground mark to the front of the queue
      self.ground_marks += [GroundMark()]
      self.curr_ground_length = 0
      self.generating_ground_marks = False

  def __generate_cacti(self):
    self.cactus_wait_count -= self.ground_speed
    if self.cactus_wait_count < 0:
      self.cacti += [Cactus()]
      self.cactus_wait_count = cactus_space

  def update(self):
    self.__move_objects()
    self.__generate_ground_marks()
    self.__generate_cacti()

  def render(self, draw):
    draw.line((0, height - ground_height, width, height - ground_height), fill=255, width=1)
    for ground_mark in self.ground_marks:
      ground_mark.render(draw)
    for cactus in self.cacti:
      cactus.render(draw)
