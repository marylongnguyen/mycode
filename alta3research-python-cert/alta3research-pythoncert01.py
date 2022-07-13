#!/usr/bin/env python3
import csv
import crayons

def main():
  dict_from_csv = {}

  with open('animal_riddle.csv', mode='r') as riddle_file:
    reader = csv.reader(riddle_file)
    dict_from_csv = {rows[0]:rows[1] for rows in reader}

  print(dict_from_csv)
  # print crayons.red('red string')
  
main()