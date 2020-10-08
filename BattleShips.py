import pygame
from ClassesInit import *
from fieldInit import *
from ImagesSetUp import *
from animations import *

pygame.init()


# constans
H, W = 600, 450


'''____________________________main game_________________________________'''

def mainGame(playerfield, Player):
    sc.blit(BackGroundSurf, BackGroundSurf.get_rect())
    sc.blit(AIgettingReadyText, AIgettingReadyTextRect)
    pygame.display.update()

    shipListAI = [4, 3, 3, 2, 2, 2]
    AIfield, shipListAI = AIgettingReady(shipListAI)
    for i in range(len(shipListAI)):  # shipListAI = [length, Horiz, (x, y)]
        shipListAI[i] = AIship(shipListAI[i][0], shipPics[0][shipListAI[i][0]],
                        shipPics[1][shipListAI[i][0]],
                        shipListAI[i][2], shipListAI[i][1], fieldGameCoor)

    # game locals setup
    BackToMenu = False
    end = False
    AIteam = len(shipListAI)
    UserTeam = len(shipListAI)
    timeSinceText = 0

    pygame.time.delay(3000)  # wait 3 sec like smth is going on
    sc.blit(BackGroundSurf, BackGroundSurf.get_rect())
    sc.blit(field, fieldGameRect)
    for j in shipListAI:
        sc.blit(j.blankSurf, j.blankRect)
    sc.blit(MenuButton.Surf, MenuButton.Rect)
    sc.blit(AIscore[AIteam], AIscore[AIteam].get_rect(bottomleft=(0, W)))

    sc.blit(fieldsmall, fieldsmallRect)
    for i in Player:
        i.smallRect = i.smallImage.get_rect(topleft=(i.fieldCooor[0] * 16 + 2 + fieldsmallCoor[0], i.fieldCooor[1] * 16 + 2 + fieldsmallCoor[1]))
        sc.blit(i.smallImage, i.smallRect)

    pygame.display.update()
    while not(BackToMenu) and not(end):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
            elif i.type == pygame.MOUSEBUTTONDOWN and fieldGameRect.collidepoint(i.pos):
                x, y = (i.pos[0] - fieldGameCoor[0]) // 30, (i.pos[1] - fieldGameCoor[1]) // 30
                print(x, y)

                if x in range(0, 10) and y in range(0, 10) and AIfield[x][y] == 1:
                    explosionAnimation(fieldGameCoor[0] + x * 30  + 15, fieldGameCoor[1] + y * 30  + 15, explosion)
                    AIfield[x][y] = 2
                    allright = False  # temporar
                    for j in shipListAI:  # search for injured ship
                        if j.blankRect.collidepoint(i.pos):
                            smth = AIship.injured(j, sc)
                            if smth == 0:  # check if ship is dead or not
                                sc.blit(INJUREDtext, INJUREDtext.get_rect(topleft=(0, 0)))
                                timeSinceText = pygame.time.get_ticks()
                            else:
                                AIteam -= 1
                                if AIteam == 1:  # texts
                                    sc.blit(ONELEFTtext, ONELEFTtext.get_rect(topleft=(0, 0)))
                                    timeSinceText = pygame.time.get_ticks()
                                else:
                                    sc.blit(BOOMtext, BOOMtext.get_rect(topleft=(0, 0)))
                                    timeSinceText = pygame.time.get_ticks()
                                if AIteam == 0:
                                    end = True
                            sc.blit(AIscore[AIteam], AIscore[AIteam].get_rect(bottomleft=(0, W)))
                            pygame.display.update()
                            allright = True
                            break
                    if not(allright):
                        print('Shit here we go again')

                elif x in range(0, 10) and y in range(0, 10) and AIfield[x][y] == 0:
                    explosionAnimation(fieldGameCoor[0] + x * 30  + 15, fieldGameCoor[1] + y * 30  + 15, NopeExplosion)
                
                x, y, anim = AIsturn(playerfield, False, sc)
                explosionAnimation(x, y, anim)  # AIs turn
                #explosionAnimation(x, y, anim)  # AIs turn

            elif i.type == pygame.MOUSEBUTTONDOWN and MenuButton.Rect.collidepoint(i.pos):
                sc.blit(MenuButton.PressedSurf, MenuButton.Rect)
                pygame.display.update()

            elif i.type == pygame.MOUSEBUTTONUP and MenuButton.Rect.collidepoint(i.pos):
                sc.blit(MenuButton.Surf, MenuButton.Rect)
                sc.blit(MenuQuestion, MenuQuestion.get_rect(topleft=(0, 0)))
                sc.blit(menuChoice, menuChoiceRect)
                pygame.display.update()
                stop = False

                while not(stop):
                    for j in pygame.event.get():
                        if j.type == pygame.QUIT:
                            exit()
                        elif j.type == pygame.MOUSEBUTTONDOWN and\
                                menuChoiceRect.collidepoint(j.pos):
                            if j.pos[0] < 232:
                                end = True
                                stop = True
                            else:
                                stop = True
                                sc.blit(textSpace, textSpace.get_rect(topleft=(0, 0)))
                pygame.display.update()


        if timeSinceText != 0 and pygame.time.get_ticks() - timeSinceText > 3000:
            timeSinceText = 0
            sc.blit(textSpace, textSpace.get_rect(topleft=(0, 0)))
            pygame.display.update()
         
        pygame.time.delay(20)



'''____________________________customization loop____________________________'''


def customizeUserField():
    # untouchable objects
    sc.blit(BackGroundSurf, BackGroundSurf.get_rect())
    sc.blit(InstructionText, InstructionText.get_rect(topleft=(0, 0)))
    sc.blit(CustomizationText, CustomizationText.get_rect(topleft=(0, 0)))
    sc.blit(shipsPlace, shipsPlace.get_rect(bottomright=(H, W)))
    sc.blit(DoneButton.PressedSurf, DoneButton.Rect)

    # sprites
    sc.blit(fieldCustom, fieldCustomRect)
    sc.blit(MenuButton.Surf, MenuButton.Rect)

    # field init
    shipsGroup = pygame.sprite.Group()
    playerfield = [[0 for i in range(10)] for j in range(10)]
    
    Player = PlayerShipInit([(465, 408), (362, 408), (262, 408),  # init all ships
                    (192, 408), (120, 408), (48, 408)],
                    [4, 3, 3, 2, 2, 2], shipPics, shipsGroup)

    for i in Player:
        sc.blit(i.image, i.rect)

    toMenu = False
    done = False
    chosen = None
    doneB = len(Player)
    
    pygame.display.update()
    while not(toMenu) and not(done):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit()
                
            elif chosen != None and i.type == pygame.MOUSEMOTION and\
                    fieldCustomRect.contains(Player[chosen].shadow.get_rect(topleft=(i.pos[0] - 15, i.pos[1] - 15))):
                sc.blit(fieldCustom, fieldCustomRect)  # ships moving animation
                shipsGroup.draw(sc)
                Player[chosen].shadowRect = Player[chosen].shadow.get_rect(topleft=(i.pos[0] - 15, i.pos[1] - 15))
                sc.blit(Player[chosen].shadow, Player[chosen].shadowRect)
                pygame.display.update()

            elif i.type == pygame.MOUSEBUTTONDOWN:
                if MenuButton.Rect.collidepoint(i.pos) and i.button == 1:  # menu button animation
                    sc.blit(MenuButton.PressedSurf, MenuButton.Rect)
                    pygame.display.update()

                elif (i.button == 4 or i.button == 5) and chosen != None:  # turning a ship
                    sc.blit(fieldCustom, fieldCustomRect)
                    shipsGroup.draw(sc)
                    PlayerShip.turn(Player[chosen])
                    if fieldCustomRect.contains(Player[chosen].shadowRect):
                        sc.blit(Player[chosen].shadow, Player[chosen].shadowRect)
                    pygame.display.update()
                
                elif i.button == 1 and chosen != None and fieldCustomRect.collidepoint(i.pos):
                    x, y= (i.pos[0] - fieldCustomCoor[0]) // 30, (i.pos[1] - fieldCustomCoor[1]) // 30
                    if x in range(0, 10) and y in range(0, 10): #and\
                            #fieldCustomRect.contains(pygame.transform.rotate(Player[chosen].image, Player[chosen].turnChange).get_rect(topleft=i.pos)):
                        PlayerShip.Customchange(Player[chosen], x, y, fieldCustomCoor)  # placing ship on the field
                        sc.blit(shipsPlace, shipsPlace.get_rect(bottomright=(H, W)))
                        sc.blit(fieldCustom, fieldCustomRect)
                        shipsGroup.draw(sc)
                        sc.blit(Player[chosen].image, Player[chosen].rect)
                        chosen = None

                        for i in Player:
                            if i.fieldCooor == (-1, -1):
                                doneB = 1
                                break
                            else:
                                doneB = 0
                        
                        if doneB == 0:
                            doneB, playerfield = PLayerFieldCheck(Player)
                            if doneB == 0:
                                sc.blit(DoneButton.Surf, DoneButton.Rect)
                        pygame.display.update()
                
                elif i.button == 1 and doneB == 0 and DoneButton.Rect.collidepoint(i.pos):
                    sc.blit(DoneButton.PressedSurf, DoneButton.Rect)
                    pygame.display.update()
                    pygame.time.delay(200)
                    done = True

                elif i.button == 1 and shipsPlace.get_rect(bottomright=(H, W)).collidepoint(i.pos) or\
                    fieldCustomRect.collidepoint(i.pos):  # choosing ships
                    for j in range(len(Player)):
                        if Player[j].rect.collidepoint(i.pos):
                            chosen = j
                            break 
    

            elif i.type == pygame.MOUSEBUTTONUP and i.button == 1:
                if MenuButton.Rect.collidepoint(i.pos):  # answer - go back to menu or not
                    sc.blit(MenuButton.Surf, MenuButton.Rect)
                    sc.blit(backMenuText, backMenuText.get_rect(topleft=(0, 0)))
                    sc.blit(menuChoice, menuCustomChoiceRect)
                    sc.blit(CustomizationText, CustomizationText.get_rect(topleft=(0, 0)))
                    pygame.display.update()
                    stop = False

                    while not(stop):
                        for j in pygame.event.get():
                            if j.type == pygame.QUIT:
                                exit()
                            elif j.type == pygame.MOUSEBUTTONDOWN and\
                                    menuCustomChoiceRect.collidepoint(j.pos):
                                if j.pos[0] < 121:
                                    stop = True
                                    toMenu = True
                                else:
                                    stop = True
                                    sc.blit(InstructionText, InstructionText.get_rect(topleft=(0, 0)))
                                    sc.blit(CustomizationText, CustomizationText.get_rect(topleft=(0, 0)))
                                    if doneB == 0:
                                        sc.blit(DoneButton.Surf, DoneButton.Rect)
                                    else:
                                        sc.blit(DoneButton.PressedSurf, DoneButton.Rect)
                    pygame.display.update()
    

        pygame.time.delay(20)


    if not(toMenu):
        for i in Player:
            if i.horiz:
                for j in range(i.length):
                    playerfield[i.fieldCooor[0] + j][i.fieldCooor[1]] = 1
            else:
                for j in range(i.length):
                    playerfield[i.fieldCooor[0]][i.fieldCooor[1] + j] = 1
        mainGame(playerfield, Player)



'''____________________________main menu_________________________________'''


clock = pygame.time.Clock()
pygame.display.update()

while True:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()

        elif i.type == pygame.MOUSEBUTTONDOWN:
            if StartButton.Rect.collidepoint(i.pos):
                sc.blit(StartButton.PressedSurf, StartButton.Rect)
            elif ShopButton.Rect.collidepoint(i.pos):
                sc.blit(ShopButton.PressedSurf, ShopButton.Rect)
            elif SettingsButton.Rect.collidepoint(i.pos):
                sc.blit(SettingsButton.PressedSurf, SettingsButton.Rect)
            pygame.display.update()

        elif i.type == pygame.MOUSEBUTTONUP:
            if StartButton.Rect.collidepoint(i.pos):  # beginning of the game
                beginningANimation()
                customizeUserField()
                menuSetUp()
                pygame.display.update()

    pygame.time.delay(20)
