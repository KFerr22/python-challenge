#import from source file and read csv file
import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)

# create list
    vote_list = []
    candidates = []
    percent_candidate = []
    count_candidate = []

# create count
    total_vote = 0

    for row in csvreader:
        vote_list.append(row[2])
        total_vote = len(vote_list)

# find candidates 
for name in vote_list:
   if name not in candidates:
        candidates.append(name)
        i = name

# total votes counter
count = 0
# loop to set candidate from vote_list
candidate = vote_list[0]

last_count = 0
# print election results total votes
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_vote}")
print("-------------------------")

for candidate in candidates:
    for vote in vote_list:
        if candidate == vote:
            count += 1
    percent = count / len(vote_list)
    percent_candidate.append(percent)
    count_candidate.append(count)
    
    if last_count < count:
        winner = candidate    
    print(f"{candidate}: {percent:.3%} ({count})")
    
    # reset vote count to zero
    last_count = count
    count = 0

# print winner
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# save the output file path as a txt file to Analysis folder
output = os.path.join("Analysis", 'output.txt')
with open(output,"w") as new:
    new.write("Election Results")
    new.write("\n")
    new.write("-------------------------")
    new.write("\n")
    new.write(f"Total Votes: {total_vote}")
    new.write("\n")
    new.write("-------------------------")
    new.write("\n")
    for candidate in candidates:
        index = candidates.index(candidate)
        new.write(f"{candidate}: {percent_candidate[index]:.3%} ({count_candidate[index]})\n")
    new.write("-------------------------")
    new.write("\n")
    new.write(f"Winner: {winner}")
    new.write("\n")
    new.write("-------------------------")
