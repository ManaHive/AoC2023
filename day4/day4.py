import re
with open('inputTest.txt') as i:
    input_nl = i.readlines()
input = [l.strip('\n\r') for l in input_nl]

print(input)