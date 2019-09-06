#!/usr/bin/python

import csv
import random
import sys
import getopt

def help(argv):
   inputfile = ''
   try:
      opts, args = getopt.getopt(argv,"hi:",["ifile="])
   except getopt.GetoptError:
      print("test.py -i <inputfile>")
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print("test.py -i <inputfile>")
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg

   return inputfile

def ploufPlouf(length):
    return random.randint(0, length)

def storeDataFromCSV(filename):
    cities = []
    countries = []

    with open(filename) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            countries.append(row[0])
            cities.append(row[1])

    return cities, countries

def main():  
  print("Starting hostname generation")
  inputfile = help(sys.argv[1:])
  print("Reading from file: "+ inputfile)
  cities, countries = storeDataFromCSV(inputfile)
  i = ploufPlouf(len(cities))
  print("A new hostname has been found: " + cities[i] + ", " +  countries[i])

  
if __name__== "__main__":
  main()








