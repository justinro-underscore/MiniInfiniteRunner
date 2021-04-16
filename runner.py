import time

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

from player import Player
from ground import Ground
from cactus_container import CactusContainer
from constants import height, width, frame_rate_constant, ground_height

class InfiniteRunner:
  def __init__(self):
    # Setup display
    i2c = busio.I2C(SCL, SDA)
    self.oled = adafruit_ssd1306.SSD1306_I2C(width, height, i2c)

    # Clear display.
    self.oled.fill(0)
    self.oled.show()

    self.player = Player()
    self.ground = Ground()
    self.cactus_container = CactusContainer()

  def __udpate(self):
    self.player.update()
    self.ground.update()
    self.cactus_container.update()

  def __render(self, draw):
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Objects
    self.player.render(draw)
    self.ground.render(draw)
    self.cactus_container.render(draw)

  def run(self):
    # Create blank image for drawing.
    # Make sure to create image with mode '1' for 1-bit color.
    image = Image.new('1', (width, height))
    draw = ImageDraw.Draw(image)

    while True:
      self.__udpate()

      # Display image.
      self.__render(draw)
      self.oled.image(image)
      self.oled.show()
      time.sleep(frame_rate_constant)

infiniteRunner = InfiniteRunner()
infiniteRunner.run()
