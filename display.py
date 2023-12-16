import pygame
from colours import Colours

class Display:
  def __init__(self, screen):
    self.screen = screen
    self.font1 = pygame.font.SysFont("dejavuserif", 65)
    self.font2 = pygame.font.SysFont("dejavusansmono", 100)
    self.font3 = pygame.font.SysFont("dejavusansmono", 25)
    self.buttons = []

  def title_scrn(self):
    #Backround Obstacles
    pygame.draw.rect(self.screen, Colours.LIGHT_GREEN, ((175, 0), (75, 100)))
    pygame.draw.rect(self.screen, Colours.LIGHT_GREEN, ((175, 250), (75, 200)))
    pygame.draw.rect(self.screen, Colours.LIGHT_GREEN, ((450, 0), (75, 250)))
    pygame.draw.rect(self.screen, Colours.LIGHT_GREEN, ((450, 400), (75, 50)))
    pygame.draw.rect(self.screen, Colours.LIGHT_GREEN, ((700, 0), (75, 175)))
    pygame.draw.rect(self.screen, Colours.LIGHT_GREEN, ((700, 325), (75, 125)))

    #Title Text
    self.text_box(self.font2, "JUMPY", (190, 125), Colours.PURPLE, Colours.BLACK)
    self.text_box(self.font3, "Click to Start!", (235, 260), Colours.BLACK, Colours.PURPLE)

    #Character
    pygame.draw.rect(self.screen, Colours.BLACK, ((560, 150), (120, 120)))
    pygame.draw.rect(self.screen, Colours.PURPLE, ((572, 162), (36, 36)))
    pygame.draw.rect(self.screen, Colours.PURPLE, ((632, 162), (36, 36)))
    pygame.draw.rect(self.screen, Colours.RED, ((560, 270), (42, 42)))
    pygame.draw.rect(self.screen, Colours.RED, ((638, 270), (42, 42)))
    
  def score(self, points):
    self.text_box(self.font1, str(points), (0,0), Colours.WHITE, Colours.BLACK)

  def end_scrn(self, score):
    self.text_box(self.font2, "Game Over", (130, 100), Colours.PURPLE, Colours.BLACK)
    self.text_box(self.font1, f"Score: {str(score)}", (260, 260), Colours.BLACK, Colours.PURPLE)
  
  def text_box(self, font, txt, location: tuple, txt_clr, box_clr):
    txt = font.render(txt, True, txt_clr)
    txt_rect = txt.get_rect()
    txt_rect.topleft = location
    pygame.draw.rect(self.screen, box_clr, txt_rect)
    self.screen.blit(txt, txt_rect)