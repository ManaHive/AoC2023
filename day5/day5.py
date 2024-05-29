import re
import time
start_time = time.time()

test = False
if test:
    folder = "test input"
else:
    folder = "real input"

INPUT = ("seeds.txt","seed-to-soil.txt","soil-to-fertilizer.txt","fertilizer-to-water.txt","water-to-light.txt","light-to-temperature.txt", "temperature-to-humidity.txt", "humidity-to-location.txt")

seeds = []
mapList = []
location = []

realSeeds = []
realLocation = []
for inp in INPUT:
    with open(folder + "/" + inp) as i:
        input_nl = i.readlines()
    input = [l.strip('\n\r') for l in input_nl]
    if inp == "seeds.txt":
        seeds = input[0].split(" ")
    else:
        mapList.append(input)

for s in seeds:
    curr = int(s)
    for m in mapList:
        for row in m:
            row_split = row.split(" ")
            dest = int(row_split[0])
            source = int(row_split[1])
            rnge = int(row_split[2])

            if curr >= source and curr <= source + rnge - 1:
                curr = dest + (curr - source)
                break
    location.append(curr)

#part 2 this doesn't work
cd = 0
lowestLoc = -1
for s in range(0,len(seeds)):
    if cd == 0:
        seedStart = int(seeds[s])
        seedRange = int(seeds[s+1])
        cd = 1
        print(f"Seed Start: {seedStart} Seed Range: {seedRange}")
        for i in range(seedStart, seedStart + seedRange):
            curr = i
            for m in mapList:
                for row in m:
                    row_split = row.split(" ")
                    dest = int(row_split[0])
                    source = int(row_split[1])
                    rnge = int(row_split[2])

                    if curr >= source and curr <= source + rnge - 1:
                        #print(f"Current is: {curr}")
                        curr = dest + (curr - source)
                        break
            if lowestLoc == -1:
                lowestLoc = curr
            
            failCount = 0
            if curr < lowestLoc:
                print(f"Lowest is {curr}")
                lowestLoc = curr
                print("Did we hit a low?")
                break
            else:
                failCount = failCount + 1
            if failCount == 5:
                break
    else:
        #print("COOLDOWNNN")
        cd = cd - 1

print("----------")
print("FOR PART 1")
print(f"Locations: {location}")
lowToHigh_location = location.sort()
print(f"Lowest is {location[0]}")

print("----------")
print("FOR PART 2")
print(f"Lowest is {lowestLoc}")

print("----------")
print(f"{time.time() - start_time} seconds")