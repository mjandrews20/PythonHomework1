import os
import csv
csvpath = os.path.join('election_data.csv')
def FindWinner(names, percents):
   win=float(percents[0])
   winner = names[0]
   for count in percents:
       if float(count) > win:
           winner = names[count.index()]
   return winner
count = 0
candidates = []
candcount= []
candpercent= []
with open (csvpath, newline="") as csvfile:
   csvreader = csv.reader(csvfile, delimiter=',')
   header = next (csvreader, None)
   for row in csvreader:
       count +=1
       if row[2] not in candidates:
           candidates.append(row[2])
           candcount.append(1)
       else:
           votefor = candidates.index(row[2])
           candcount[votefor] += 1
   for votes in candcount:
       percent = float(votes/count*100)
       candpercent.append(percent)
   winner= FindWinner(candidates,candcount)
   print("Election Results")
   print("----------------")
   print(f"Total Votes: {count}" )
   print(f"----------------")
   for i in range(len(candidates)):
       print (f"{candidates[i]}: {candpercent[i]},{candcount[i]}")
   print("-----------------------")
   print(f"{winner} is the winner.")
   f= open("Election.txt","w+")
   f.write("Election Results" "\n")
   f.write("---------------------" "\n")
   f.write(f"Total Votes: {count}" "\n")
   f.write(f"----------------" "\n")
   for i in range(len(candidates)):
       print (f"{candidates[i]}: {candpercent[i]},{candcount[i]}" "\n")
   f.write("-----------------------" "\n")
   f.write(f"{winner} is the winner." "\n")
   f.close

