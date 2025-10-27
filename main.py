import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Platformer")
running = True

parallax_layers = [
    {"image": pygame.transform.scale(pygame.image.load("assets/background/night/1.png"), (1066, 600)), "speed": 0.01, "x": 0},
    {"image": pygame.transform.scale(pygame.image.load("assets/background/night/2.png"), (1066, 600)), "speed": 0.05, "x": 0},
    {"image": pygame.transform.scale(pygame.image.load("assets/background/night/4.png"), (1066, 600)), "speed": 0.3, "x": 0},
    {"image": pygame.transform.scale(pygame.image.load("assets/background/night/3.png"), (1066, 600)), "speed": 0.1, "x": 0},
    {"image": pygame.transform.scale(pygame.image.load("assets/background/night/5.png"), (1066, 600)), "speed": 0.5, "x": 0},
]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    for layer in parallax_layers:
        layer["x"] -= layer["speed"]
        if layer["x"] <= -layer["image"].get_width():
            layer["x"] = 0
        screen.blit(layer["image"], (layer["x"], 0))
        screen.blit(layer["image"], (layer["x"] + layer["image"].get_width(), 0))
    pygame.display.update()


        

pygame.quit()