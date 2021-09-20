from math import sqrt
from decimal import Decimal

def count_distance(alphabetLength, firstRelativeFrequencies, secondRelativeFrequencies):
    firstFrequencySums = [sum(firstRelativeFrequencies[:i]) for i in range(1, alphabetLength+1)]
    secondFrequencySums = [sum(secondRelativeFrequencies[:i]) for i in range(1, alphabetLength+1)]
    difference = [abs(firstFrequencySums[i]-secondFrequencySums[i]) for i in range(0, alphabetLength)]
    distance = Decimal(max(difference) * sqrt(alphabetLength/2))

  #  for i in range(alphabetLength):
  #      print(firstRelativeFrequencies[i], " | ", firstFrequencySums[i], "  | ", secondRelativeFrequencies[i], " | ", secondFrequencySums[i], "  | ", difference[i])

  #   print("относит частота 1")
  #   for i in range(alphabetLength):
  #       print(firstRelativeFrequencies[i])
  #   print("-----------------------------")
  #
  #   print("относит частота 2")
  #   for i in range(alphabetLength):
  #       print(secondRelativeFrequencies[i])
  #   print("-----------------------------")
  #
  #   print("итеративная расчёт частёт1")
  #   for i in range(alphabetLength):
  #       print(firstFrequencySums[i])
  #   print("-----------------------------")
  #
  #   print("итеративная расчёт частёт2")
  #   for i in range(alphabetLength):
  #       print(secondFrequencySums[i])
  #   print("-----------------------------")
  #
  #   print("модуль разности")
  #   for i in range(alphabetLength):
  #       print(difference[i])
  #   print("-----------------------------")
  #   print("максимум: ", max(difference), "  *  ",  sqrt(alphabetLength/2))
  #   print("result:  ",distance)

    return distance