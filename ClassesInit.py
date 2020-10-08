import pygame
pygame.init()

H, W = 600, 450


class Buttons:
    def __init__(self, image, pressedImage, coordinates):
        self.Surf = pygame.image.load(image)
        self.Surf.set_colorkey((255, 255, 255))
        self.Rect = self.Surf.get_rect(bottomleft=coordinates)
        self.PressedSurf = pygame.image.load(pressedImage)

    def InsideButton(self):
        pass

    def InsideButtonClose(self):
        pass


class Ship(pygame.sprite.Sprite):
    def __init__(self, length, image, blankImage, Horiz):
        pygame.sprite.Sprite.__init__(self)
        self.length = length
        self.image = pygame.image.load(image)
        self.blankSurf = pygame.image.load(blankImage)
        self.horiz = Horiz
        if Horiz:
            self.image = pygame.transform.rotate(self.image, 90)
            self.blankSurf = pygame.transform.rotate(self.blankSurf, 90)
        self.health = length

    def injured(self, sc):
        self.health -= 1
        print('injured ship ' + str(self.length))
        if self.health == 0:
            print('boom')
            sc.blit(self.image, self.rect)
            return 1
        return 0
        

class AIship(Ship):
    def __init__(self, length, image, blankImage, xy, Horiz, fieldGameCoor):
        Ship.__init__(self, length, image, blankImage, Horiz)
        self.coordinates = (fieldGameCoor[0] + xy[0] * 30 + 4, fieldGameCoor[1] + xy[1] * 30 + 2)
        self.rect = self.image.get_rect(topleft=self.coordinates)
        self.blankRect = self.blankSurf.get_rect(topleft=self.coordinates)


def PlayerShipInit(coord, ships, images, shipGroup):
    for i in range(len(ships)):
        ships[i] = PlayerShip(coord[i], ships[i], images[0][ships[i]],
        images[1][ships[i]], images[2][ships[i]], images[3][ships[i]], shipGroup)
    return ships


class PlayerShip(Ship):
    def __init__(self, coord, length, image, blankImage, shadowImage, smallImage, shipGroup):
        Ship.__init__(self, length, image, blankImage, True)
        self.coord = coord
        self.rect = self.image.get_rect(topleft=self.coord)

        self.smallImage = pygame.image.load(smallImage)
        self.smallImage = pygame.transform.rotate(self.smallImage, 90)
        self.smallRect = self.smallImage.get_rect(topleft=self.coord) 

        self.shadow = pygame.image.load(shadowImage)
        self.shadow = pygame.transform.rotate(self.shadow, 90)
        self.shadowRect = self.shadow.get_rect(topleft=self.coord)

        self.fieldCooor = (-1, -1)
        self.turnChange = 0
        shipGroup.add(self)
    
    def turn(self):
        self.turnChange += 90
        self.horiz = not(self.horiz)
        self.shadow = pygame.transform.rotate(self.shadow, 90)
        self.shadowRect = self.shadow.get_rect(topleft=self.shadowRect.topleft)
    
    def Customchange(self, x, y, fieldCoord):
        self.fieldCooor = (x, y)
        self.turnChange = self.turnChange % 360
        self.image = pygame.transform.rotate(self.image, self.turnChange)
        self.rect = self.image.get_rect(topleft=(x * 30 + fieldCoord[0] + 5, y * 30 + fieldCoord[1] + 5))
        self.smallImage = pygame.transform.rotate(self.smallImage, self.turnChange)
        #self.smallRect = self.smallImage.get_rect(topleft=())
        self.turnChange = 0
        


    