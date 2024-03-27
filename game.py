#from local version game4, uploaded 27/3/24
colourLookup = ["N","R","G"]
class Tile:
    def __init__(self,type):
        self.colour = 0 #assigned colour 0,, no colour
        self.n = 0 #no particles to begin with
        self.type = type #1 is corner, 2 is edge, 3 is center 
    def __str__(self):
        return str(colourLookup[self.colour])+str(self.n)+" "

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
    gameState[pos[0]][pos[1]].colour = colour
    gameState[pos[0]][pos[1]].n += 1

def getTile(pos):
    return gameState[pos[0]][pos[1]]

def setTileN(pos,n):
    gameState[pos[0]][pos[1]].n = n

def setTileColour(pos,colour):
    gameState[pos[0]][pos[1]].colour = colour

def resolve(i,j):
    setTileN([i,j],0)
    propagatingColour = getTile([i,j]).colour #find what the colour is 
    try:
        addParticle([i+1,j],propagatingColour) #increas all adjacent tiles ki balls and change colour to that
    except IndexError:                          #if its a corner or edge this should take care of it 
        pass
    try:
        addParticle([i-1,j],propagatingColour)
    except IndexError:
        pass
    try:
        addParticle([i,j+1],propagatingColour)
    except IndexError:
        pass
    try:
        addParticle([i,j-1],propagatingColour)
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

#showing program off
generateBoard(5,5)
printState()
for i in range(0,10):
    addParticle([4,2],1)
    tick()
    printState()



