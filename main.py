import pygame
import config
from game_state import GameState

from game import Game

#iniciar pygame
pygame.init()
#iniciar display
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

pygame.display.set_caption("Rpg-Python")

clock = pygame.time.Clock()
x= 50
y= 50 
width = 50
height = 50
speed = 2000


game = Game(screen)
game.set_up()

while game.game_state == GameState.RUNNING:
  clock.tick(80)
  game.update()
  pygame.display.flip()
