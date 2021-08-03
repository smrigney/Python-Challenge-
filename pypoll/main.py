# the total number of votes cast
# a complete list of candidates who received votes
# the total number of votes each candidate won
# the Winner of the election based on Popular vote 

import csv
 
#open the csv doc
csvfile = open("onedrive/desktop/python-challenge/pypoll/resources/election_data.csv")
reader = csv.reader(csvfile)

# Total Number of Votes Cast
totalvotes = 0 
for i in reader:
    totalvotes = totalvotes + 1

#print(totalvotes) #answer1

csvfile.close()

csvfile = open("onedrive/desktop/python-challenge/pypoll/resources/election_data.csv")
reader = csv.reader(csvfile)

#List candidates who received votes 
#creating holding list for duplicate list 
allnames = []
#moving all names into list 
for col in reader:
    allnames.append(col[2])
#removing duplicates 
shortlist = []
for i in allnames:
    if i not in shortlist:
        shortlist.append(i)
#deleting header
del shortlist[0]
#print check
#print(shortlist)

# the total number of votes each candidate won

#tallying votes for all candidates 
khanvote = allnames.count(shortlist[0])
correyvote = allnames.count(shortlist[1])
livote = allnames.count(shortlist[2])
otooleyvote = allnames.count(shortlist[3])
#printcheck
#print(khanvote,correyvote,livote,otooleyvote)

#Find percentages
sumvote = khanvote + correyvote + livote + otooleyvote

#sum %
khanper = khanvote / sumvote
correyper = correyvote / sumvote
liper = livote / sumvote
otooleyper = otooleyvote / sumvote
#format %
#print("{:.0%}".format(khanper))
#print("{:.0%}".format(correyper))
#print("{:.0%}".format(liper))
#print("{:.0%}".format(otooleyper))

#display winner's name 

tally = [khanvote,correyvote,livote,otooleyvote]

if max(tally) is khanvote:
    winner = "Khan"
if max(tally) is correyvote:
    winner = "Correy"
if max(tally) is livote:
    winner = "Li"
if max(tally) is otooleyvote:
    winner = "O'Tooley" 

#print(winner)


#export answers to txt doc
khan = str(shortlist[0])
correy = shortlist[1]
li = shortlist[2]
otooley = shortlist[3]

#answer1 = totalvotes
#answer2 = (khan),  (khanper),  (khanvote)
#answer3 = (correy), (correyper), (correyvote)
#answer4 = (li), (liper), (livote)
#answer5 = (otooley), (otooleyper), ((otooleyvote)

#print(khan,correy,li,otooley)

#print to python
print("Election Results")
print("--------------------------")
print("Total Votes: ", totalvotes)
print("--------------------------")
print(khan,":", "{:.0%}".format(khanper), "(", khanvote, ")" )
print(correy,":", "{:.0%}".format(correyper), "(", correyvote, ")" )
print(li,":", "{:.0%}".format(liper), "(", livote, ")" )
print(otooley,":", "{:.0%}".format(otooleyper), "(", otooleyvote, ")" )
print("--------------------------")
print("Winner: ", winner)
print("--------------------------")

#print to txt file 
import sys

sys.stdout = open("onedrive/desktop/python-challenge/pypoll/analysis/pypoll_analysis.txt","w")

print("Election Results")
print("--------------------------")
print("Total Votes: ", totalvotes)
print("--------------------------")
print(khan,":", "{:.0%}".format(khanper), "(", khanvote, ")" )
print(correy,":", "{:.0%}".format(correyper), "(", correyvote, ")" )
print(li,":", "{:.0%}".format(liper), "(", livote, ")" )
print(otooley,":", "{:.0%}".format(otooleyper), "(", otooleyvote, ")" )
print("--------------------------")
print("Winner: ", winner)
print("--------------------------")