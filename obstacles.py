import pygame
from colours import Colours
import random

class Obstacles:
  def __init__(self, screen, character):
    self.speed = 1 #1
    self.hole = 150 #150
    self.interval = 350 #350
    self.curr_interval = 350
    self.curr_obsts = []
    self.obst_points = []
    self.screen = screen
    self.screen_width = 800
    self.screen_height = 450
    self.char = character
    self.colour = Colours.GREEN
    self.collided = False
    self.points = 0

  def main(self):
    self.create_obsts()
    self.collide()
    self.point_checker()
    self.draw()
    if self.curr_obsts[0][0].x <= -75: # Removes an obstacle if it is off the screen
      self.curr_obsts.pop(0)
  
  def draw(self):
    for obst in self.curr_obsts:
      for rect in obst:
        pygame.draw.rect(self.screen, self.colour, rect)
        rect.x -= self.speed
    self.curr_interval += self.speed #Calculates how far away the previous obstacle is

  def create_obsts(self):
    if self.curr_interval >= self.interval:
      move_x = self.curr_interval - self.interval # If self.curr_interval is greater than self.interval it will add the difference to the x of the rectangles
      self.curr_interval = 0
      top_hole = random.randint(1, 449 - self.hole) #Creates a random int to be the top of the hole in the obstacle
      top_rect = pygame.Rect(self.screen_width - move_x, 0, 75, top_hole)
      bottom_rect = pygame.Rect(self.screen_width - move_x, top_hole + self.hole, 75, self.screen_height - (top_hole + self.hole))

      self.curr_obsts.append([top_rect, bottom_rect])
      self.obst_points.append(top_rect) # Only added the top rectangle because I just need to check the x-location and they have the same one

  def collide(self):
    for obst in self.curr_obsts:
      for rect in obst:
        if rect.colliderect(self.char.rect):
          self.collided = True

  def point_checker(self):
    prev_points = self.points
    for rect in self.obst_points:
      if rect.x <= 90:
        self.points += 1
        if self.points % 5 == 0:
          self.incr_diff()
    if prev_points != self.points:
      self.obst_points.pop(0)

  def incr_diff(self):
    while True:
      if self.speed == 3 and self.hole == 100 and self.interval == 315:
        break
      else:
        choice = random.randint(1, 3)
        if choice == 1:
          if self.speed < 3:
            self.speed += 0.5
            break
        elif choice == 2:
          if self.hole != 100:
            self.hole -= 10
            break
        else:
          if self.interval != 315:
            self.interval -= 7
            break