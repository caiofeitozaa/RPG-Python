import pygame
from player import Player
import config
from game_state import GameState

class Game:
  def __init__(self,screen):
    self.screen = screen
    self.objects = []
    self.game_state= GameState.NONE
    self.map = []

  def set_up(self):
    player=Player(1,1)
    self.player = player
    self.objects.append(player)
    print("configure")
    self.game_state= GameState.RUNNING

    self.load_map("01")

   
  
  def update(self):
    self.screen.fill(config.BLACK)
    print("atualizando")
    self.handle_events()

    self.render_map(self.screen)
    

    for object in self.objects:
      object.render(self.screen)

  def handle_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.game_state= GameState.ENDED
        #eventos de chave
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          self.game_state= GameState.ENDED
        elif event.key == pygame.K_w:
          self.player.update_position(0,-1) 
        elif event.key == pygame.K_s:
          self.player.update_position(0,1)
        elif event.key == pygame.K_a:
          self.player.update_position(-1,0)
        elif event.key == pygame.K_d:
          self.player.update_position(1,0)

  def load_map(self,file_name):
    with open ('maps/'+file_name+".txt") as map_file:
      for line in map_file:
        tiles = []

        for i in range(0,len(line)-1,2):
          tiles.append(line[i])
        self.map.append(tiles)
      print(self.map)   
          
  def render_map(self,screen):
    y_pos = 0
    for line in self.map:
      x_pos = 0
      for tile in line:
          image = map_tile_image [tile]
          rect = pygame.Rect(x_pos * config.SCALE, y_pos * config.SCALE, config.SCALE, config.SCALE)
          screen.blit(image,rect)
          x_pos = x_pos + 1
        
      y_pos = y_pos + 1
    

map_tile_image = {
  "G":pygame.transform.scale(pygame.image.load("imgs/grass1.png") , (config.SCALE,config.SCALE)),
"W":pygame.transform.scale(pygame.image.load("imgs/grass2.png") , (config.SCALE,config.SCALE)),
"J":pygame.transform.scale(pygame.image.load("imgs/grass3.png") , (config.SCALE,config.SCALE)),
  "K":pygame.transform.scale(pygame.image.load("imgs/grass4.png") , (config.SCALE,config.SCALE)),
  "L":pygame.transform.scale(pygame.image.load("imgs/grass5.png") , (config.SCALE,config.SCALE)),
  "Z":pygame.transform.scale(pygame.image.load("imgs/grass6.png") , (config.SCALE,config.SCALE)),
  "X":pygame.transform.scale(pygame.image.load("imgs/grass7.png") , (config.SCALE,config.SCALE)),
  "C":pygame.transform.scale(pygame.image.load("imgs/grass8.png") , (config.SCALE,config.SCALE)),
  "V":pygame.transform.scale(pygame.image.load("imgs/grass8.png") , (config.SCALE,config.SCALE)) , 
  "B":pygame.transform.scale(pygame.image.load("imgs/grass10.png") , (config.SCALE,config.SCALE)),
  "N":pygame.transform.scale(pygame.image.load("imgs/grass11.png") , (config.SCALE,config.SCALE)),
  "M":pygame.transform.scale(pygame.image.load("imgs/grass12.png") , (config.SCALE,config.SCALE)),
  "Q":pygame.transform.scale(pygame.image.load("imgs/grass13.png") , (config.SCALE,config.SCALE)),
"R":pygame.transform.scale(pygame.image.load("imgs/grass14.png") , (config.SCALE,config.SCALE)),
"E":pygame.transform.scale(pygame.image.load("imgs/grass15.png") , (config.SCALE,config.SCALE)),
  "T":pygame.transform.scale(pygame.image.load("imgs/grass16.png") , (config.SCALE,config.SCALE)),
  "Y":pygame.transform.scale(pygame.image.load("imgs/grass18.png") , (config.SCALE,config.SCALE)),
  "U":pygame.transform.scale(pygame.image.load("imgs/grass17.png") , (config.SCALE,config.SCALE))
  
}
    



     
