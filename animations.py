import pygame
pygame.init()
from ImagesSetUp import *


def beginningANimation():
    '''animation before the game starts'''
    sc.blit(BackGroundSurf, BackGroundSurf.get_rect())
    sc.blit(ShopButton.Surf, ShopButton.Rect)
    sc.blit(BattleShipText, BattleShipText.get_rect())
    sc.blit(StartButton.Surf, StartButton.Rect)
    pygame.display.update()
    pygame.time.delay(500)

    sc.blit(BackGroundSurf, BackGroundSurf.get_rect())
    sc.blit(BattleShipText, BattleShipText.get_rect())
    sc.blit(StartButton.Surf, StartButton.Rect)
    pygame.display.update()
    pygame.time.delay(500)

    sc.blit(BackGroundSurf, BackGroundSurf.get_rect())
    sc.blit(StartButton.Surf, StartButton.Rect)
    pygame.display.update()
    pygame.time.delay(500)


def explosionAnimation(x, y, anim):
    '''x and y are central coordinates, anim - mass of pictures'''
    for i in anim:
        sc.blit(i, i.get_rect(center=(x, y)))
        pygame.display.update()
        pygame.time.delay(50)
