'''all visual setup'''
import pygame
from ClassesInit import Buttons
pygame.init()

H, W = 600, 450

'''Screen setup'''
sc = pygame.display.set_mode((H, W))

'''files'''
path = r'C:\Users\User\Desktop\warships\Sprites'
p = open(path + r'\package.txt')
package = p.read()

'''____________menu images setup____________'''
BackGroundSurf = pygame.image.load(path + r'\mainFone.png')
sc.blit(BackGroundSurf, BackGroundSurf.get_rect())
BattleShipText = pygame.image.load(path + r'\menu\BATTLESHIPStext.png')
sc.blit(BattleShipText, BattleShipText.get_rect())

StartButton = Buttons(path + r'\menu\StartBotton.png',
    path + r'\menu\StartBottonPressed.png', (130, 280))
sc.blit(StartButton.Surf, StartButton.Rect)

ShopButton = Buttons(path + r'\menu\SHOPBotton.png',
    path + r'\menu\SHOPBotton.Pressed.png', (223, 330))
sc.blit(ShopButton.Surf, ShopButton.Rect)

SettingsButton = Buttons(
    path + r'\menu\SettingsButton.png',
    path + r'\menu\SettingsButtonPressed.png', (3, W - 3))
sc.blit(SettingsButton.Surf, SettingsButton.Rect)

'''____________Game images____________'''

'''texts'''


AIgettingReadyText = pygame.image.load(path + r'\game\AIisGettingReadyText.png')
AIgettingReadyTextRect = AIgettingReadyText.get_rect(center=(H // 2, W // 2))

textSpace = pygame.image.load(path + r'\game\Zones\textZone.png')
MenuQuestion = pygame.image.load(path + r'\game\Zones\backToMenu.png')
menuChoice = pygame.image.load(path + r'\game\menuQuestion.png')
menuChoiceRect = menuChoice.get_rect(topleft=(115, 55))
menuCustomChoiceRect = menuChoice.get_rect(topleft=(5, 313))

BOOMtext = pygame.image.load(path + r'\game\Zones\BOOM.png')
INJUREDtext = pygame.image.load(path + r'\game\Zones\INJURED.png')
ONELEFTtext = pygame.image.load(path + r'\game\Zones\ONELEFT.png')

AIscore = [
    pygame.image.load(path + r'\game\Zones\AIleft\\' + str(i) + '.png') for i in range(7)
]

CustomizationText = pygame.image.load(path + r'\customization\customizationText.png')
InstructionText = pygame.image.load(path + r'\customization\instructionText.png')
backMenuText = pygame.image.load(path + r'\customization\backMenuText.png')


'''other game stuff'''

# buttons
MenuButton = Buttons(
    path + r'\game\menuButton.png',
    path + r'\game\menuButtonPressed.png', (H - 124, 44))

DoneButton = Buttons(
    path + r'\customization\DoneButton.png',
    path + r'\customization\DoneButtonPressed.png', (40, 355))

# field in diffeent parts init
fieldGameCoor = (120, 120)
fieldCustomCoor = (269, 66)
fieldsmallCoor = (435, 285)
fieldCustom = pygame.image.load(path + r'\customization\fieldWithBackground.png')
field = pygame.image.load(path + r'\game\field.png')
fieldGameRect = field.get_rect(topleft=fieldGameCoor)
fieldCustomRect = fieldCustom.get_rect(topleft=fieldCustomCoor)
fieldsmall = pygame.image.load(path + r'\game\PLfield.png')
fieldsmallRect = fieldsmall.get_rect(topleft=fieldsmallCoor)

explosion = [pygame.image.load(path + r'\game\explosion\big' +'\\' + str(i) + '.png') for i in range(1, 7)]
smallExplosion = [pygame.image.load(path + r'\game\explosion\small' +'\\' + str(i) + '.png') for i in range(1, 7)]
NopeExplosion = [pygame.image.load(path + r'\game\nope\big' +'\\' + str(i) + '.png') for i in range(1, 4)]
smallNopeExplosion = [pygame.image.load(path + r'\game\nope\small' +'\\' + str(i) + '.png') for i in range(1, 4)]

# ships
shipPics = [{2: path + package + r'\2.png',  # usual
    3: path + package + r'\3.png',
    4: path + package + r'\4.png'},

    {2: path + package + r'\2.blank.png',  # just blank rectangles
    3: path + package + r'\3.blank.png',
    4: path + package + r'\4.blank.png'},

    {2: path + package + r'\2.shadow.png',  # only borders
    3: path + package + r'\3.shadow.png',
    4: path + package + r'\4.shadow.png'},
    
    {2: path + package + r'\small\2.png',  # small ones for the map
    3: path + package + r'\small\3.png',
    4: path + package + r'\small\4.png'}]

shipsPlace = pygame.image.load(path + r'\customization\shipsPlace.png')


def menuSetUp():  # everything in menu
    sc.blit(BackGroundSurf, BackGroundSurf.get_rect())
    sc.blit(BattleShipText, BattleShipText.get_rect())
    sc.blit(StartButton.Surf, StartButton.Rect)
    sc.blit(ShopButton.Surf, ShopButton.Rect)
    sc.blit(SettingsButton.Surf, SettingsButton.Rect)

p.close()