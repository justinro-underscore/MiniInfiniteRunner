from constants import width, score_speed_increases, font, font_width

class HiScore:
  def __init__(self):
    self.score = 0
    self.points_per_frame = 1

    self.text_padding_index = 1

  def update(self):
    self.score += self.points_per_frame
    if self.score // (10 ** self.text_padding_index):
      self.text_padding_index += 1

  def increase_speed(self):
    if self.points_per_frame <= len(score_speed_increases) and self.score >= score_speed_increases[self.points_per_frame - 1]: 
      self.points_per_frame += 1
      return True
    return False

  def render(self, draw):
    draw.text((width - 2 - (self.text_padding_index * font_width), 2), str(self.score), font=font, fill=255)
