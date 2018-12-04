#!/usr/bin/python

__author__ = "Dick van Viegen"
__copyright__ = "Copyright 2018, Dick van Viegen"
__credits__ = ["Dick van Viegen"]
__license__ = "CC"
__version__ = "1.0.1"
__maintainer__ = "Dick van Viegen"
__email__ = "dickv.viegen@gmail.com"
__status__ = "Development"

import csv
import sys
import io
import datetime

# Get the filename to read from the command line argument
inputFileName = str(sys.argv[1])

# Get the filename to output from the command line argument
outputFileName = str(sys.argv[2])
outputFile = io.open(outputFileName, 'wb')
outputWriter = csv.writer(outputFile, delimiter=',')

# Open up the file and print all lines for testing purposes
# inputFileReader = csv.reader(inputFile, delimiter=',',quotechar='|')

specials = '"'

with io.open(inputFileName, 'rb') as inputFile:
    inputReader = csv.reader(inputFile, delimiter=',',quotechar='"')
    firstLine = True
    for row in inputReader:
        row = [value.replace(specials, '') for value in row]
        if firstLine:
            newRow = []
            newRow.append('Date')
            newRow.append('Payee')
            newRow.append('Category')
            newRow.append('Memo')
            newRow.append('Outflow')
            newRow.append('Inflow')
            firstLine = False
            outputWriter.writerow(newRow)
            continue
        date = row[0]
        payee = row[1]
        category = row[7]
        memo = row[8]
        inflow = ''
        outflow = ''
        if row[5] == 'Af':
            outflow = row[6]
        else:
            inflow = row[6]
        nRow = []
        nRow.append(datetime.datetime.strptime(date, '%Y%m%d').strftime('%d/%m/%Y'))
        nRow.append(payee)
        nRow.append(category)
        nRow.append(memo)
        nRow.append(outflow)
        nRow.append(inflow)

        print(nRow)

        outputWriter.writerow(nRow)
