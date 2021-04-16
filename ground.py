from random import random
from math import floor

from constants import height, width, ground_height, ground_mark_probability, max_ground_mark_length, ground_speed

class GroundMark:
  def __init__(self, x=width):
    self.x = x
    self.y = height - floor(random() * (ground_height - 2)) - 1
    self.length = max_ground_mark_length

  # Returns true if it has fully gone offscreen
  def move(self):
    self.x -= ground_speed
    return (self.x + self.length - 1) < 0


class Ground:
  def __init__(self):
    self.ground_marks = [GroundMark()]
    self.curr_ground_length = 0
    self.generating_ground_marks = False

  def __move_ground_marks(self):
    pop = False # Defines if we should pop the first ground mark off the queue (if it's gone offscreen)
    for ground_mark in self.ground_marks:
      if ground_mark.move():
        pop = True
    if pop:
      self.ground_marks.pop()

  def __generate_ground_marks(self):
    # If not currently generating a ground mark...
    if not self.generating_ground_marks:
      # Move the ground mark length to what is currently shown on screen
      self.curr_ground_length += ground_speed
      # Use linear interpolation to see if we should cut off the ground mark at its current length
      probability = self.curr_ground_length / max_ground_mark_length
      end_mark = random() < probability
      # If we should cut off the mark...
      if end_mark:
        # Set the ground mark's length to its current length
        self.ground_marks[0].length = self.curr_ground_length
        # Reset to prepare for generating a new ground mark
        self.curr_ground_length = 0
        self.generating_ground_marks = True

    # If currently generating a ground mark and we should place a new ground mark
    if self.generating_ground_marks and random() < ground_mark_probability:
      # Append a new ground mark to the front of the queue
      self.ground_marks = [GroundMark()] + self.ground_marks
      self.generating_ground_marks = False

  def update(self):
    self.__move_ground_marks()
    self.__generate_ground_marks()

  def render(self, draw):
    draw.line((0, height - ground_height, width, height - ground_height), fill=255, width=1)
    for ground_mark in self.ground_marks:
      draw.line((ground_mark.x, ground_mark.y, ground_mark.x + ground_mark.length - 1, ground_mark.y), fill=255, width=1)
