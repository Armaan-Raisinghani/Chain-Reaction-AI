#from local version 5, uploaded 31/3/24
colourLookup = ["N","R","G"]
class Tile:
    def __init__(self,type):
        self.colour = 0 #assigned colour 0,, no colour
        self.n = 0 #no particles to begin with
        self.type = type #1 is corner, 2 is edge, 3 is center 
    def __str__(self):
        return str(colourLookup[self.colour])+str(self.n)+" "
    def __int__(self):
        if self.colour == 0:
            return 0
        if self.colour == 1:
            return self.n
        elif self.colour == 2:
            return -self.n
        else:
            return -999

def generateRow(w,notEdge): #notEdge = 0 when generating edge row, 1 when generating center row 
    row = []
    row.append(Tile(1+notEdge))
    for i in range(1,w-1):
        row.append(Tile(2+notEdge))
    row.append(Tile(1+notEdge))
    return row

def generateBoard(h,w):
    global gameState
    gameState = []
    gameState.append(generateRow(w,0))
    for i in range(1,h-1):
        gameState.append(generateRow(w,1))
    gameState.append(generateRow(w,0))

def printState():
    print("")
    for row in gameState:
        for tile in row:
            print(tile, end="")
        print("")

def addParticle(pos,colour):
    gameState[pos[1]][pos[0]].colour = colour
    gameState[pos[1]][pos[0]].n += 1

def getTile(pos):
    return gameState[pos[1]][pos[0]]

def setTileN(pos,n):
    gameState[pos[1]][pos[0]].n = n

def setTileColour(pos,colour):
    gameState[pos[1]][pos[0]].colour = colour

def resolve(i,j):
    setTileN([i,j],0)
    propagatingColour = getTile([i,j]).colour #find what the colour is 
    setTileColour([i,j],0)
    try:
        addParticle([i+1,j],propagatingColour) #increas all adjacent tiles ki balls and change colour to that
    except IndexError:                          #if its a corner or edge this should take care of it 
        pass
    try:
        addParticle([i,j+1],propagatingColour)
    except IndexError:
        pass
    if j-1 >= 0:
        try:
            addParticle([i,j-1],propagatingColour)
        except IndexError:
            pass
    if i-1 >= 0:
        try:
            addParticle([i-1,j],propagatingColour)
        except IndexError:
            pass

def tick():
    height = len(gameState)
    width = len(gameState[0])
    for i in range(0,height):
        for j in range(0,width):
            if getTile([i,j]).n >getTile([i,j]).type: #if the number of balls in a tile is more than the amount it can support 
                resolve(i,j)
                tick()

#what armaan gotta type 
generateBoard(5,5)
printState()
for i in range(0,10):
    addParticle([0,0],1)
    tick()
    printState()



