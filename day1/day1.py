import re
with open('inputReal.txt') as i:
    input_nl = i.readlines()
input = [l.strip('\n\r') for l in input_nl]

# QUESTION 1
list =[]
for i in input:
    temp = re.findall("\d",i)
    calValue = temp[0] + temp[-1]
    list.append(calValue)
print(list)

sum = 0
for n in list:
    sum += int(n)
print("Sum: " + str(sum))

# QUESTION 2
def combine(x,y):
        return x*10+y
numDict = {
    "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9
}
list =[]
sum = 0
for i in input:
    temp = re.findall("(?=(\d|one|two|three|four|five|six|seven|eight|nine))",i)
    valFirst = int(temp[0]) if len(temp[0]) == 1 else numDict[temp[0]]
    valLast = int(temp[-1]) if len(temp[-1]) == 1 else numDict[temp[-1]]
    calValue = combine(valFirst,valLast) #if len(temp) != 1 else valFirst
    sum = sum + calValue
print("Sum: " + str(sum))

