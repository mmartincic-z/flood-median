import pandas as pd
import numpy as np

# Load the CSV file without headers
data = pd.read_csv('out1.csv', header=None)

print("ucitano")
datalist = list(data[0])

# Define the threshold for flood alerts (more negative than -1 mA)
threshold = 1e-3  # -1 mA in scientific notation

print(f"Got data points:{len(datalist)}")

datalist = datalist[:1000000]

floodIntervals = []
windowSize = 5
startIdx = -1
for i, meas in enumerate(datalist[:-windowSize]) :
    if startIdx == -1 and max(datalist[i:i+windowSize]) > threshold :
        startIdx = i
    elif startIdx > -1 and max(datalist[i:i+windowSize]) < threshold :
        floodIntervals.append((startIdx, i))
        startIdx = -1

#print(f"Found flood intervals {len(floodIntervals)}")

idleIntervals = []
prevInterval = (0, 0)
for flood in floodIntervals :
    idleIntervals.append((prevInterval[1], flood[0]))
idleIntervals.append((prevInterval[1], len(datalist)))

samplingPeriodS = 1/20.
cumSumFloodIntervals = 0
cumSumFloodDuration = 0
prevFloodS = 0
for flood in floodIntervals :
    floodStartS = flood[0]*samplingPeriodS
    cumSumFloodIntervals += floodStartS - prevFloodS
    cumSumFloodDuration += flood[1]*samplingPeriodS - floodStartS
    prevFloodS = floodStartS

avgFloodIntervalS = cumSumFloodIntervals / len(floodIntervals)
avgFloodDurationS = cumSumFloodDuration / len(floodIntervals)
print(f"Average sleep duration is {avgFloodIntervalS} s")
print(f"Average flood duration is {avgFloodDurationS} s")

floodConsumptions = []
for flood in floodIntervals :
    cumSumInterval = 0
    consumptionInterval = datalist[flood[0]:flood[1]]
    for measurement in consumptionInterval :
        cumSumInterval += measurement
    floodConsumptions.append(cumSumInterval / len(consumptionInterval))
idleConsumptions = []
for idle in idleIntervals :
    cumSumInterval = 0
    consumptionInterval = datalist[idle[0]:idle[1]]
    for measurement in consumptionInterval :
        cumSumInterval += measurement
    idleConsumptions.append(cumSumInterval / len(consumptionInterval))

avgFloodConsumptionA = sum(floodConsumptions) / len(floodConsumptions)
avgIdleConsumptionA = sum(idleConsumptions) / len(idleConsumptions)
print(f"Average current draw during flood is {avgFloodConsumptionA} A")
print(f"Average current draw in sleep is {avgIdleConsumptionA} A")
