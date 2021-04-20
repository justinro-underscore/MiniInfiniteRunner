from constants import score_speed_increases, font

class HiScore:
  def __init__(self):
    self.score = 0
    self.points_per_frame = 1

  def update(self):
    self.score += self.points_per_frame

  def increase_speed(self):
    if self.points_per_frame <= len(score_speed_increases) and self.score >= score_speed_increases[self.points_per_frame - 1]: 
      self.points_per_frame += 1
      return True
    return False

  def render(self, draw):
    draw.text((2, 2), str(self.score), font=font, fill=255)
