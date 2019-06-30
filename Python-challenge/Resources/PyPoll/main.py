# Homework completed by Mohammad Zahid Shiwani, Adrian William Vojvodic, Wyatt Carnes
# First we'll import the os module
import os

# Module for reading CSV files
import csv
# election_data.csv
# joining the path
csvpath = os.path.join("..","PyPoll","election_data.csv")

# Defining variables, lists and dictionary
Candidate = []
candidate_info = {}
total_votes = 0
candidate_votes = []
candidate_names = []

# open csv file
with open(csvpath, newline='') as csvfile:
   # CSV reader specifies delimiter and variable that holds contents
   election_Data = csv.reader(csvfile, delimiter=',')
   # Read the header row first (skip this step if there is now header)
   csv_header = next(election_Data)

   # list of votes for all candidates
   for row in election_Data:
       cand.append(row[2])
   for i in cand:
       if i not in candidate_info:
           candidate_info[i] = 1
       else:
           candidate_info[i] += 1
       total_votes = total_votes + 1

   for key, value in candidate_info.items():
       candidate_names.append(key)
       candidate_votes.append(value)
   # Alternate
   # for row in election_Data:
   #     if row[2] not in candidate_info:
   #         candidate_info[row[2]] = 1
   #     else:
   #         candidate_info[row[2]] += 1
   #     total_votes = total_votes + 1

# print(candidate_info)
# print(total_votes)
# print(candidate_names)
# print(candidate_votes)
# print(max(candidate_votes))

pct_of_votes = [(a*100) / total_votes for a in (candidate_votes)]
#     #print(pct_of_votes)
print("Election Results \n------------------------------")
print(f"Total Votes: {total_votes} \n------------------------------")
for i in range(len(candidate_names)):
   print(f"{candidate_names[i]}: {round(pct_of_votes[i],3)}% ({candidate_votes[i]})")
print(f"------------------------------\n Winner: {candidate_names[candidate_votes.index(max(candidate_votes))]}\n------------------------------")