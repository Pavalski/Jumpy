import pygame
from colours import Colours

class JumpMan:
  def __init__(self, screen):
    self.dimen = 20
    self.x = 165
    self.y = 215
    self.y_vel = -2
    self.screen = screen
    self.bottom = 450 - self.dimen
    self.top = 0
    self.is_jumping = False
    self.jump_dist = 0

  def draw(self):
    #Body
    pygame.draw.rect(self.screen, Colours.BLACK, ((self.x, self.y), (self.dimen, self.dimen)))
    #Eyes
    pygame.draw.rect(self.screen, Colours.PURPLE, ((self.x + 2, self.y + 2), (6, 6)))
    pygame.draw.rect(self.screen, Colours.PURPLE, ((self.x + 12, self.y + 2), (6, 6)))
    
    if self.is_jumping:
      #Boosters
      pygame.draw.rect(self.screen, Colours.RED, ((self.x, self.y + 20), (7, 7)))
      pygame.draw.rect(self.screen, Colours.RED, ((self.x + 13, self.y + 20), (7, 7)))
      
      if self.jump_dist <= 50:
        self.y -= 2
        if self.y < self.top:
          self.y = self.top
        self.jump_dist += 2
      else:
        self.is_jumping = False
    else:
      self.y -= self.y_vel
      if self.y > self.bottom:
        self.y = self.bottom

  def jump(self):
    self.jump_dist = 0
    self.is_jumping = True
    # self.y -= 10
    # if self.y < self.top:
    #   self.y = self.top

  @property
  def rect(self):
    return pygame.Rect(self.x, self.y, self.dimen, self.dimen)
          
          