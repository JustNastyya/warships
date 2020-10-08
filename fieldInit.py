from random import randint
from animations import explosionAnimation
from ImagesSetUp import fieldsmallCoor, smallExplosion, smallNopeExplosion


def AIgettingReady(ships):
    '''making enemy field and putting ships'''
    AIfield = [[0 for j in range(10)] for i in range(10)]

    for i in ships:
        fine = False
        while not(fine):
            x, y, Horiz = randint(0, 9), randint(0, 9), randint(0, 1)

            fine = Check(x, y, Horiz, AIfield, i)

        if Horiz:
            for j in range(i):
                AIfield[x + j][y] = 1
        else:
            for j in range(i):
                AIfield[x][y + j] = 1
        ships[ships.index(i)] = [i, Horiz, (x, y)] 
        
    return AIfield, ships


def PLayerFieldCheck(ships):
    '''Check if all the ships are placed by the rules'''
    field = [[0 for j in range(10)] for i in range(10)]
    for i in ships:
        stop = False
        x, y, Horiz = i.fieldCooor[0], i.fieldCooor[1], i.horiz

        stop = not(Check(x, y, Horiz, field, i.length))
        
        if Horiz:
            for j in range(i.length):
                field[x + j][y] = 1
        else:
            for j in range(i.length):
                field[x][y + j] = 1

        if stop:
            return 1, field
    return 0, field
    

def Check(x, y, Horiz, field, i):
    stop = False
    fine = True
    if Horiz and not field[x][y]:
        for j in range(i):  # cheching ship place
            try:
                if field[x + j][y]:
                    stop = True
            except IndexError:
                stop = True
        if stop:
            fine = False     
        for j in range(i + 2):  # checking borders aroud ship
            try:
                if field[x + j][y + 1]:
                    stop = True
                    break
            except IndexError:
                pass
            try:
                if field[x + j][y - 1]:
                    stop = True
                    break
            except IndexError:
                pass
        if stop:
            fine = False
        for j in range(3):  # checking top and bpttom borders
            try:
                if field[x - 1][y - 1 + j]:
                    stop = True
                    break
            except IndexError:
                pass
            try:
                if field[x + i][y - 1 + j]:
                    stop = True
                    break
            except IndexError:
                    pass
        if stop:
            fine = False

    elif not(field[x][y]):
        for j in range(i):
            try:
                if field[x][y + j]:
                    stop = True
            except IndexError:
                stop = True
        if stop:
            fine = False    
        for j in range(i + 2):
            try:
                if field[x + 1][y + j]:
                    stop = True
                    break
            except IndexError:
                pass
            try:
                if field[x - 1][y + j]:
                    stop = True
                    break
            except IndexError:
                pass
        if stop:
            fine = False
        for j in range(3):
            try:
                if field[x - 1 + j][y - 1]:
                    stop = True
                    break
            except IndexError:
                pass
            try:
                if field[x - 1 + i][y + j]:
                    stop = True
                    break
            except IndexError:
                pass
        if stop:
            fine = False

    if field[x][y]:
        return False
    return fine


def AIsturn(field, injured, sc):  # 0 - nothing 1 - ship 2 - already shot there 3 - shot ship
    if not(injured):
        stop = False
        while not(stop):
            x, y = randint(0, 9), randint(0, 9)
            if field[x][y] != 2 or field[x][y] != 3:
                stop = True
                if field[x][y] == 0:
                    field[x][y] = 2
                    print('AI ay', x, y)
                    return fieldsmallCoor[0] + x * 16 + 8, fieldsmallCoor[1] + y * 16 + 8, smallNopeExplosion
                elif field[x][y] == 1:
                    field[x][y] = 3
                    print('AI says', x, y)
                    return fieldsmallCoor[0] + x * 16 + 8, fieldsmallCoor[1] + y * 16 + 8, smallExplosion

'''
a, b = AIgettingReady([4, 3, 3, 2, 2,2])
for i in a:
    print(' '.join(str(j) for j in i))'''
