import re
import time
start_time = time.time()

with open('input.txt') as i:
    input_nl = i.readlines()
input = [l.strip('\n\r') for l in input_nl]

def formatCardNumIdx(strIdx):
    if len(strIdx) == 1:
        return " " + " " + strIdx  # for real input
        #return strIdx # for inputTest only
    elif len(strIdx) == 2:
        return " " + strIdx
    elif len(strIdx) == 3:
        return strIdx

def removeItems(lst, item):
    return [i for i in lst if i != item]

idx = 1
totalPts = 0
totalCard = 0
dupeQueue = []

for i in input:
    # getting valid winning numbers list
    remCardNum = i.replace("Card " + formatCardNumIdx(str(idx)) + ": ","")
    split = remCardNum.split(" | ")
    winNums = removeItems(split[0].split(" "),"")
    nums = removeItems(split[1].split(" "), "")

    # part 1 code for calculating pts
    validNums = set(winNums) & set(nums)
    pts = 2 ** (len(validNums) - 1) if len(validNums) - 1 >= 0 else 0

    totalPts = totalPts + pts

    # part 2 code for calculating number of scorecards
    for i in range(idx, len(validNums)+idx):
        dupeQueue.append(i+1)
        totalCard = totalCard + 1
    
    for d in dupeQueue:
        if (d < idx):
            continue
        if (d == idx):
            for i in range(idx, len(validNums)+idx):
                dupeQueue.append(i+1)
                totalCard = totalCard + 1
        else:
            break
    #print(dupeQueue)

    dupeQueue.sort()
    dupeQueue = removeItems(dupeQueue, idx)
    idx = idx + 1
    totalCard = totalCard + 1

    #print(totalCard)

print(f"Total Points: {totalPts}")
print(f"Total Number of Cards: {totalCard}")
print(f"{time.time() - start_time} seconds")