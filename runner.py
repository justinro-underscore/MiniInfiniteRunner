import time

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

from player import Player
from ground import Ground
from hi_score import HiScore

from physics import is_touching
from constants import height, width, frame_rate_constant, ground_height

class InfiniteRunner:
  def __init__(self):
    # Setup display
    i2c = busio.I2C(SCL, SDA)
    self.oled = adafruit_ssd1306.SSD1306_I2C(width, height, i2c)

    # Clear display.
    self.oled.fill(0)
    self.oled.show()

    self.game_over = False

    self.player = Player()
    self.ground = Ground()
    self.hi_score = HiScore()

  def __check_for_game_over(self):
    if len(self.ground.cacti) > 0:
      front_cactus = self.ground.cacti[0]
      if is_touching(self.player.get_collider(), front_cactus.get_collider()):
        self.game_over = True

  def __udpate(self):
    self.ground.update()
    self.player.update()
    self.hi_score.update()

    if self.hi_score.increase_speed():
      self.ground.increase_speed()
    self.__check_for_game_over()

  def __render(self, draw):
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Objects
    self.ground.render(draw)
    self.player.render(draw)
    self.hi_score.render(draw)

  def run(self):
    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)

    while not self.game_over:
      self.__udpate()

      # Display image.
      self.__render(draw)
      self.oled.image(image)
      self.oled.show()
      time.sleep(frame_rate_constant)

infiniteRunner = InfiniteRunner()
infiniteRunner.run()
