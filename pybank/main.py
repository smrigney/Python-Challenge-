# total number of months in data set (column 0)
# the net total amount of profit/losses over the entire period (column 1)
# calculate the changes in profit/losses over the entire period, then find average
# the greatest increase in profits (date and amount) over the entire period
# the greatest decrease in profits (date and amount) over the entire period

#find the cvs file

import csv

#find csv file
csvfile = open("onedrive/desktop/python-challenge/pybank/resources/budget_data.csv","r+")
reader = csv.reader(csvfile)
#count number of lines in csv file
lines=len(list(reader))
#remove header from lines count
linesfinal = lines - 1
print("Total Months: ", linesfinal) 
#send to word file
answer1 = str("Total Months: ") + str(linesfinal)
worddoc = open("onedrive/desktop/python-challenge/pybank/analysis/pybank_analysis.txt","w")
worddoc.write(str(answer1) + '\n')

#close csvfile 
csvfile.close()

# add total profit / losses 
csvfile = open("onedrive/desktop/python-challenge/pybank/resources/budget_data.csv","r+")
#skip the header row
next(csvfile)
#set total to 0 
total = 0 
#sum column 1 
for row in csv.reader(csvfile):
    total +=int(row[1])
#print check 
print("Total: $", total) #Answer#2
#send to word file 
answer2 = str("Total: $") + str(total)
worddoc.write(str(answer2) + '\n')

csvfile.close() 

# calculate the changes in profit/losses over the entire period, 
# then find average
csvfile = open("onedrive/desktop/python-challenge/pybank/resources/budget_data.csv","r+") 

#create reader
diffile = csv.reader(csvfile)

#create list to store differences        
numlist = []

#pulling from csv to create list of profit/loss column
for col in diffile:
    numlist.append(col[1])
#print(numlist)

#remove header from list
del numlist[0]

#making numlist integers
numlist = list(map(int, numlist))

#setting new list for differences
numdiffs = []

#finding all differences and adding to new list
for i in range(len(numlist)):
    diff = numlist[i] - numlist[i -1]
    numdiffs.append(diff)

#removing first diff to ensure correct mean
del numdiffs[0]

#finding mean via statistics
import statistics
meandiff = statistics.mean(numdiffs)

#print check
print("Average Change: $ %0.2f" % (meandiff))#Answer#3

#write answer 3 to txt file 
answer3 = str("Average Change: $ ") + str( "%.02f" % meandiff)
worddoc.write(answer3 + '\n')
csvfile.close()

# the greatest increase in profits (date and amount) 
# over the entire period

csvfile = open("onedrive/desktop/python-challenge/pybank/resources/budget_data.csv","r+") 
maxminlist = csv.reader(csvfile)

#sort list 
maxdiff = max(numdiffs)
mindiff = min(numdiffs)
#print(maxdiff, mindiff)

#create month list 
monthlist = []
for col in maxminlist:
    monthlist.append(col[0])

i = 0 
countmaxdiff = 0
for i in numdiffs: 
    if i is not maxdiff:
        countmaxdiff = countmaxdiff + 1
    else:
        break

#account for header and add one month 
countmaxdiff = countmaxdiff + 2
#print check
print("Greatest Increase in Profits: ",monthlist[countmaxdiff], maxdiff) #Answer#4

#answer 4 to txt file 
answer4 = str("Greatest Increase in Profits: ") + str(monthlist[countmaxdiff] + "  " + str(maxdiff))
worddoc.write(answer4 + "\n")

i = 0 
countmindiff = 0
for i in numdiffs: 
    if i is not mindiff:
        countmindiff = countmindiff + 1
    else:
        break

#account for header and add one month 
countmindiff = countmindiff + 2
#print check
print("Greatest Decrease in Profits: ", monthlist[countmindiff], mindiff) #answer#5

#answer 5 into txt doc 
answer5 = str("Great Decrease in Profits: ") + str(monthlist[countmindiff]) + "  " + str(mindiff)
worddoc.write(str(answer5))

#close worddoc
worddoc.close()