import re
with open('input.txt') as i:
    input_nl = i.readlines()
input = [l.strip('\n\r') for l in input_nl]

LINE_LENGTH = len(input[0])

def combine(value): # combines numbers in a list into int
    if len(value) == 3:
        return int(value[0])*100+int(value[1])*10+int(value[2])
    elif len(value) == 2:
        return int(value[0])*10+int(value[1])
    else:
        return int(value[0])

class Number:
    def __init__(self, x, y, value):
        self.positions = (x,y)
        self.value = combine(value)
        self.length = len(value)
        self.occupiedPostions = []
        for i in range(0, self.length):
            self.occupiedPostions.append((x+i,y))

    def __str__(self):
        return f"Left most pos: {self.positions} Value: {self.value} Occupied Position: {self.occupiedPostions}"
    
    def getAdjPos(self):
        lstAdjPost = []
        xPos = self.positions[0]
        yPos = self.positions[1]
        xCurr = xPos - 1
        yCurrUp = yPos - 1
        yCurrDown = yPos + 1

        if (xCurr > 0):
            lstAdjPost.append((xCurr, yPos))
        if (xCurr + self.length + 1 < LINE_LENGTH):
            lstAdjPost.append((xCurr + self.length + 1, yPos))

        for l in range(self.length + 2):
            if (yCurrUp >= 0):
                if (xCurr >= 0 and xCurr < LINE_LENGTH):
                    lstAdjPost.append((xCurr, yCurrUp))
            if (yCurrDown < LINE_LENGTH):
                if (xCurr >= 0 and xCurr < LINE_LENGTH):
                    lstAdjPost.append((xCurr, yCurrDown))
            xCurr = xCurr + 1

        return lstAdjPost
    
    def getPosition(self):
        return self.positions
    def getValue(self):
        return self.value
    def getOccPos(self):
        return self.occupiedPostions
    
class Gear(Number):
    def __init__(self, x, y, value):
        self.positions = (x,y)
        self.value = value
        self.length = 1
        self.adjNums = []
    def __str__(self):
        return f"Position: {self.positions} Value: {self.value}"
    def getAdjNums(self):
        return self.adjNums
    def addAdjNums(self, num):
        self.adjNums.append(num)

                
def getNumber(index, list, numList): # returns a list of the number from input, starting from the index
    if list[index].isdigit():
        numList.append(list[index])
    if index >= len(list) - 1 or not(list[index].isdigit()):
        return numList
    else:
        getNumber(index+1, list, numList)
    return numList

def commonMember(a, b): # returns true if two lists have a common element, else false
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return(True) 
    return(False)   

            
totalNumList = []
symbolPosList = []
gearList = []
index = 0
for i in input:
    cooldown = 0
    for c in range(len(i)):
        if cooldown > 0:
            cooldown = cooldown - 1 # cd for calling getNumber, based on length of numlist

        if cooldown == 0 and i[c].isdigit():
            numList = getNumber(c, i, [])
            totalNumList.append(Number(c,index,numList))
            cooldown = len(numList)
        if not i[c].isdigit() and i[c] != ".":
            symbolPosList.append((c, index))
        if i[c] == "*":
            gearList.append((c, index))
    index = index + 1

validPartNumList = []
hasGearNextList = []
validGearRatioList = []

for t in totalNumList:
    adjPos = t.getAdjPos()
    if commonMember(adjPos, symbolPosList): # is valid part number if adjacent to any symbol
        validPartNumList.append(t)
    if commonMember(adjPos, gearList): # for part 2, filtering out numbers that have * adjacent
        hasGearNextList.append(t)

for g in gearList:
    currGear = Gear(g[0],g[1],"*")
    gPos = currGear.getPosition()
    xGear = gPos[0]
    yGear = gPos[1]
    for h in hasGearNextList:
        pos = h.getPosition()
        xNum = pos[0]
        yNum = pos[1]
        if yNum - yGear < -2: # continue if y level is too behind
            continue
        if yNum - yGear > 2: # break if number is ahead y level now
            break
        if commonMember(currGear.getAdjPos(), h.getOccPos()):
           currGear.addAdjNums(h)
        if len(currGear.getAdjNums()) == 2: # if there are two part nums adjacent, append, break, move on
            validGearRatioList.append(currGear)
            break
    
partNumSum = 0
gearRatioSum = 0
for v in validPartNumList:
    #print(v)
    partNumSum = partNumSum + v.getValue()
for vG in validGearRatioList:
    #print(vG)
    partNums = vG.getAdjNums()
    gearRatioSum = gearRatioSum + partNums[0].getValue() * partNums[1].getValue()

# print(symbolPosList)
print(f"Part Number Sum: {partNumSum}")
print(f"Gear Ratio Sum: {gearRatioSum}")

    

    