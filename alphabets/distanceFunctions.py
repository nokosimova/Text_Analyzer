from math import sqrt
import numpy as np

def count_distance(alphabetLength, firstRelativeFrequencies, secondRelativeFrequencies):
    firstFrequencySums = [sum(firstRelativeFrequencies[:i]) for i in range(1, alphabetLength+1)]
    secondFrequencySums = [sum(secondRelativeFrequencies[:i]) for i in range(1, alphabetLength+1)]
    difference = [abs(firstFrequencySums[i]-secondFrequencySums[i]) for i in range(1, alphabetLength+1)]
    distance = np.Decimal(max(difference)/sqrt(alphabetLength/2))

    for i in alphabetLength:
        print(firstFrequencySums[i], "  | ", secondFrequencySums, "  | ", difference[i])
    print("result:  ",distance)
    return distance