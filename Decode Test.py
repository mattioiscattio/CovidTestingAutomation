"""import os
import pygame
from PIL import Image

screen = pygame.display.set_mode((1920,1080), pygame.RESIZABLE)
Image.open(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "Encoded_Image.jpg")).resize((1920, 1080)).save("Encoded_Image.jpg")
screen.blit(pygame.image.load(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "Encoded_Image2.jpg")), (0, 0))
pygame.display.update()

print(screen.get_at((0, 0)))
"""

import pygame
from PIL import Image
import os
screen = pygame.display.set_mode((1920, 1080))
screen.blit(pygame.image.load(os.path.join("D:/Coding/PyCharm_Projects/Text Hider In Image/", "Encoded_Image.jpg")), (0, 0))
pygame.display.update()
print(screen.get_at((0,0)))



