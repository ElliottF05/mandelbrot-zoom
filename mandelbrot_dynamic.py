import pygame
from mandelbrot_engine import *
import decimal


# screen variables
screenWidth = 1500
screenHeight = 1500

# starting variables
xmin, xmax = -2, 1 # -2, 0.5
ymin, ymax = -1.5, 1.5
maxDepth = 255

# data variables
zoom = 1
zoomPerClick = 1.2
zoomStr = "1.00"
zoomPerClickStr = "{:.2f}".format(zoomPerClick)


# HELPER FUNCTIONS
def newPos(xmin, xmax, ymin, ymax):
    x_size = xmax - xmin
    y_size = ymax - ymin

    prevx = (xmax + xmin) / 2
    prevy = (ymax + ymin) / 2

    x = xmin + float(pygame.mouse.get_pos()[0] * x_size) / screenWidth
    y = ymin + float((screenHeight - pygame.mouse.get_pos()[1]) * y_size) / screenHeight

    xmin = x - (prevx - xmin) / zoomPerClick
    xmax = x - (prevx - xmax) / zoomPerClick
    ymin = y - (prevy - ymin) / zoomPerClick
    ymax = y - (prevy - ymax) / zoomPerClick

    return xmin, xmax, ymin, ymax


# pygame setup
pygame.init()
screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Mandelbrot Zoom")

font = pygame.font.Font("freesansbold.ttf", 16)
text = font.render("hello", True, "white", "black")

clock = pygame.time.Clock()
running = True

# initializing image
img_data = bytes(generate(xmin, xmax, ymin, ymax, screenWidth, screenHeight, maxDepth))
data_surface = pygame.image.frombytes(img_data, (screenWidth,screenHeight), "RGB")


pygame.image.save(data_surface, "output.png")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            xmin, xmax, ymin, ymax = newPos(xmin, xmax, ymin, ymax)
            img_data = bytes(generate(xmin, xmax, ymin, ymax, screenWidth, screenHeight, maxDepth))
            data_surface = pygame.image.frombytes(img_data, (screenWidth, screenHeight), "RGB")
            zoom *= zoomPerClick
            zoomStr = "{:.2f}".format(zoom) if (zoom >= 1 and zoom < 1000) else "{:.2e}".format(zoom)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                zoomPerClick = max(0.5, zoomPerClick - 0.1)
                zoomPerClickStr = "{:.2f}".format(zoomPerClick)
            if event.key == pygame.K_UP:
                zoomPerClick = min(2, zoomPerClick + 0.1)
                zoomPerClickStr = "{:.2f}".format(zoomPerClick)
            if event.key == pygame.K_RIGHT:
                maxDepth = int(maxDepth * 1.1 + 1)
                img_data = bytes(generate(xmin, xmax, ymin, ymax, screenWidth, screenHeight, maxDepth))
                data_surface = pygame.image.frombytes(img_data, (screenWidth, screenHeight), "RGB")
            if event.key == pygame.K_LEFT:
                maxDepth = max(1, int(maxDepth / 1.1))
                img_data = bytes(generate(xmin, xmax, ymin, ymax, screenWidth, screenHeight, maxDepth))
                data_surface = pygame.image.frombytes(img_data, (screenWidth, screenHeight), "RGB")


    # GAME UPDATES

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # RENDER YOUR GAME HERE
    screen.blit(data_surface, (0, 0))
    text = font.render(("zoom: " + zoomStr + "x     zoom per click: " + zoomPerClickStr + "     depth: " + str(maxDepth)), True, "white", "black")
    screen.blit(text, (0,0))

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()