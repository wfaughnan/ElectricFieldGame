import pygame
import math


class PointCharge:

    def __init__(self, charge, position):
        self.charge = charge
        self.position = position
        if self.charge > 0:
            self.color = (255, 0, 0)
        elif self.charge < 0:
            self.color = (0, 0, 255)
        else:
            self.color = (0, 0, 0)

    def display(self, surface):
        pygame.draw.circle(surface, self.color, self.position, 25)

    def exertForce(self, Puck):
        totalForceX = 0
        totalForceY = 0

        distance = Puck.distanceBetween(self)
        true_distance = math.sqrt(abs(distance[0]) ** 2 + abs(distance[1]) ** 2)
        angle = math.atan(distance[1] / distance[0])

        totalForce = 1/(0.1 * true_distance ** 2)
        if self.position[0] > Puck.position[0]:
            totalForceX = -self.charge * (totalForceX + (totalForce * math.cos(angle)))
            totalForceY = -self.charge * (totalForceY + (totalForce * math.sin(angle)))
        else:
            totalForceX = -self.charge * (totalForceX + (totalForce * math.cos(angle + math.pi)))
            totalForceY = -self.charge * (totalForceY + (totalForce * math.sin(angle + math.pi)))

        Puck.forceX = Puck.forceX + totalForceX
        Puck.forceY = Puck.forceY + totalForceY


class Puck:

    def __init__(self, position):
        self.position = position
        self.charge =   1
        self.forceX =   0
        self.forceY =   0
        self.accelX =   0
        self.accelY =   0
        self.veloX  =   0
        self.veloY  =   0
        self.left = (self.position[0] - 25, self.position[1])
        self.right = (self.position[0] + 25, self.position[1])
        self.top = (self.position[0], self.position[1] - 25)
        self.bottom = (self.position[0], self.position[1] + 25)
        self.rect = pygame.Rect(self.position[0] - 25, self.position[1] - 25, 50, 50)

    def display(self, surface):
        pygame.draw.circle(surface, (0, 0, 0), self.position, 25, 3)

    def distanceBetween(self, PointCharge):
        distanceX = (PointCharge.position[0] - self.position[0])
        distanceY = (PointCharge.position[1] - self.position[1])
        return distanceX, distanceY

    def updateAttributes(self, tickrate):
        self.accelX, self.accelY = self.forceX, self.forceY
        self.veloX, self.veloY = self.veloX+((1/tickrate) * self.accelX), self.veloY+((1/tickrate) * self.accelY)
        self.position = (self.position[0] + ((1/tickrate)*self.veloX), self.position[1] + ((1/tickrate)*self.veloY))
        self.left = (self.position[0] - 25, self.position[1])
        self.right = (self.position[0] + 25, self.position[1])
        self.top = (self.position[0], self.position[1] - 25)
        self.bottom = (self.position[0], self.position[1] + 25)
        self.rect = pygame.Rect(self.position[0] - 25, self.position[1] - 25, 50, 50)

    def updateVelocity(self, tickrate):
        self.position = (self.position[0] + ((1 / tickrate) * self.veloX), self.position[1] + ((1 / tickrate) * self.veloY))
        self.left = (self.position[0] - 25, self.position[1])
        self.right = (self.position[0] + 25, self.position[1])
        self.top = (self.position[0], self.position[1] - 25)
        self.bottom = (self.position[0], self.position[1] + 25)
        self.rect = pygame.Rect(self.position[0] - 25, self.position[1] - 25, 50, 50)

    def collideCheck(self, Obstacle):
        if pygame.Rect.collidepoint(Obstacle.rect, self.left) or pygame.Rect.collidepoint(Obstacle.rect, self.right):
            self.veloX = -self.veloX
        elif pygame.Rect.collidepoint(Obstacle.rect, self.top) or pygame.Rect.collidepoint(Obstacle.rect, self.bottom):
            self.veloY = -self.veloY
        self.updateVelocity(5)

    def resetAttributes(self, position):
        self.position = position
        self.veloX, self.veloY = 0, 0
        self.forceX, self.forceY = 0, 0
        self.accelX, self.accelY = 0, 0


class Obstacle:

    def __init__(self, position, color, width, height):
        self.position = position
        self.color = color
        self.height = height
        self.width = width
        self.rect = pygame.Rect(position, (width, height))

    def display(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)


class Button:

    def __init__(self, position, image):
        self.position = position
        self.image = image
        self.surface = pygame.image.load(self.image)
        self.rect = None

    def blit(self, surface):
        self.surface = pygame.image.load(self.image)
        self.rect = pygame.Surface.blit(surface, self.surface, self.position)

