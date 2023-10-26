import pygame
from mandelbrot_engine import *

xmin, xmax = -2, 1 # -2, 0.5
ymin, ymax = -1.5, 1.5 # -1.5, 1.5
xres, yres = 15000, 15000
maxDepth = 100

img_data = bytes(generate(xmin, xmax, ymin, ymax, xres, yres, 80))


pygame.init()
data_surface = pygame.image.frombytes(img_data, (xres, yres), "RGB")

pygame.image.save(data_surface, "output.png")