#!/usr/bin/env python3
import csv
import crayons

def main():
    #dict_from_csv = {}

    with open('animal_riddle.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

  # print crayons.red('red string')
  
main()
