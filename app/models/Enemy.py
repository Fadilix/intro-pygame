import pygame


class Enemy:
    walkRight = [
        pygame.image.load("R1E.png"),
        pygame.image.load("R2E.png"),
        pygame.image.load("R3E.png"),
        pygame.image.load("R4E.png"),
        pygame.image.load("R5E.png"),
        pygame.image.load("R6E.png"),
        pygame.image.load("R7E.png"),
        pygame.image.load("R8E.png"),
        pygame.image.load("R9E.png"),
        pygame.image.load("R10E.png"),
        pygame.image.load("R11E.png"),
    ]
    walkLeft = [
        pygame.image.load("L1E.png"),
        pygame.image.load("L2E.png"),
        pygame.image.load("L3E.png"),
        pygame.image.load("L4E.png"),
        pygame.image.load("L5E.png"),
        pygame.image.load("L6E.png"),
        pygame.image.load("L7E.png"),
        pygame.image.load("L8E.png"),
        pygame.image.load("L9E.png"),
        pygame.image.load("L10E.png"),
        pygame.image.load("L11E.png"),
    ]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3

    def draw(self, win):
        self.move()
        pass

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel *= -1
                self.walkCount = 0

        pass