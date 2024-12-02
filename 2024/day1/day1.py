#!/usr/bin/env python3

import os
import sys
import argparse
import re

def main():
  inputFile = sys.argv[1]
  listOne = []
  listTwo = []
  with open(inputFile) as my_file:
    for line in my_file:
      numbers = line.split()
      listOne.append(int(numbers[0]))
      listTwo.append(int(numbers[1]))
  listOne.sort()
  listTwo.sort()
  sumDistance(listOne, listTwo)
  simScoreBinarySearch(listOne, listTwo)

def sumDistance(listOne, listTwo):
  sumDistance = 0
  for i in range(len(listOne)):
    sumDistance += abs((listOne[i] - listTwo[i]))
  print("day1.1: " + str(sumDistance))

def simScoreBinarySearch(listOne, listTwo):
  simScore = 0
  h = {}
  for i in range(len(listTwo)):
    if listTwo[i] in h:
      h[listTwo[i]] += 1
    else:
      h.update({listTwo[i]: 1})
  for i in range(len(listOne)):
    if listOne[i] in h:
      simScore += (listOne[i]* h[listOne[i]])
  print("day1.2: "+str(simScore))


if __name__ == '__main__':
  main()
