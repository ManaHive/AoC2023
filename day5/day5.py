import re
import time
start_time = time.time()

test = True
if test:
    folder = "test input"
else:
    folder = "real input"

with open(folder + "/seed-to-soil.txt") as i:
    input_nl = i.readlines()
input = [l.strip('\n\r') for l in input_nl]