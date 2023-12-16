import pygame
from colours import Colours
from jump_man import JumpMan
from obstacles import Obstacles
from display import Display
import time

pygame.init()

class Game:
  def __init__(self):
    self.WIDTH = 800
    self.HEIGHT = 500

    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    pygame.display.set_caption("Jumpy")

    self.display = Display(self.screen)


  def play(self):
    self.setup()
    self.main()

  def setup(self):
    self.stage = "intro" # States what part of the game is running
    
    self.char = JumpMan(self.screen)

    self.obsts = Obstacles(self.screen, self.char)

    self.clock = pygame.time.Clock()
    self.run = True
  
  def main(self):
    while self.run:
      self.clock.tick(60) # Sets the FPS to 60
      self.update()
      self.draw()
      if self.obsts.collided:
        self.stage = "end"
        time.sleep(1) # A buffer to show the player how they lost
      
  def update(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
        
      if event.type == pygame.MOUSEBUTTONDOWN:
        left_clicked = pygame.mouse.get_pressed()[0]
        right_clicked = pygame.mouse.get_pressed()[2]
        if self.stage == "intro":
          if left_clicked:
            self.stage = "game"
        elif self.stage == "game":
          if left_clicked:
            self.char.jump()
          if right_clicked:
            self.obsts.points += 1

  def draw(self):
    self.screen.fill(Colours.LIGHT_BLUE)

    pygame.draw.rect(self.screen, Colours.LIGHT_GREEN, ((0, self.HEIGHT - 50), (self.WIDTH, 50))) #Draws the grass on the bottom of the screen

    if self.stage == "intro":
      self.display.title_scrn()
    elif self.stage == "game":
      self.obsts.main()
      
      self.char.draw()
  
      self.display.score(self.obsts.points)
    else:
      self.display.end_scrn(self.obsts.points)
      self.run = False
    
    pygame.display.update()

game = Game()
game.play()