#!/usr/bin/env python3

import os
import sys
import argparse
import re

def main():
  inputFile = sys.argv[1]
  print("hello world")
  listOne = []
  listTwo = []
  with open(inputFile) as my_file:
    for line in my_file:
      numbers = line.split()
      listOne.append(int(numbers[0]))
      listTwo.append(int(numbers[1]))
  listOne.sort()
  listTwo.sort()
  sumDistance = 0
  for i in range(len(listOne)):
    sumDistance += abs((listOne[i] - listTwo[i]))
  print(sumDistance)


if __name__ == '__main__':
  main()
