import pygame
from pygame.locals import *
import sys
def hello_world():
   pygame.init()
   pygame.display.set_mode((640,480))
   pygame.display.set_caption("hello world")
   while True:
       for event in pygame.event.get():
           if event.type==QUIT:
                pygame.quit()
                sys.exit()
           pygame.display.update()
if __name__=="__main__":
   hello_world()
