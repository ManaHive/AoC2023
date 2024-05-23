import re
with open('input.txt') as i:
    input_nl = i.readlines()
input = [l.strip('\n\r') for l in input_nl]

print(input)

def validate(red, green, blue):
    if red > 12 or green > 13 or blue > 14:
        return False
    else:
        return True
index = 1
listIdx = []
listPower = []
for i in input:
    maxRed = 0
    maxGreen = 0
    maxBlue = 0
    remNum = i.replace("Game " + str(index) + ": ", "")
    cubeSetList = remNum.split("; ")
    for sets in cubeSetList:
        cubeList = sets.split(", ")
        for cube in cubeList:
            #print(cube)
            cubeSep = cube.split(" ")
            match(cubeSep[1]):
                case "red":
                    maxRed = int(cubeSep[0]) if int(cubeSep[0]) > maxRed else maxRed
                case "green":
                    maxGreen = int(cubeSep[0]) if int(cubeSep[0]) > maxGreen else maxGreen
                case "blue":
                    maxBlue = int(cubeSep[0]) if int(cubeSep[0]) > maxBlue else maxBlue
                case _:
                    print("error")
    if validate(maxRed,maxGreen,maxBlue):
            print("Game " + str(index) + " is valid!")
            listIdx.append(index)
    listPower.append(maxRed*maxGreen*maxBlue)
    index += 1

print("Index Sum")
print(sum(listIdx))
print("Power")
print(sum(listPower))




            
                    
            