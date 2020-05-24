import os
import csv
from statistics import mode


poll_csv = os.path.join('Resources', 'election_data.csv')

# create lists to store the values needed
vote_count = []
candidates = []

with open(poll_csv) as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=',')
    # Create header
    header = next(csv_reader)

    for row in csv_reader:
        vote_count.append(row[0])
        candidates.append(row[2])

# use print(set(candidates)) to find out the unique candidate names
# in this case it is {"Khan", "Correy", "Li", "O'Tooley"}
# I am commenting this out so the values dont show in the terminal
# but needed to find out these values in order to count the votes

total_votes = (len(vote_count))

# count total number of votes and percentage of votes by candidate name
Khan_votes = candidates.count("Khan")
Khan_percent = "{0:.0%}".format(Khan_votes/total_votes)

Correy_votes = candidates.count("Correy")
Correy_percent = "{0:.0%}".format(Correy_votes/total_votes)

Li_votes = candidates.count("Li")
Li_percent = "{0:.0%}".format(Li_votes/total_votes)

OTooley_votes = candidates.count("O'Tooley")
OTooley_percent = "{0:.0%}".format(OTooley_votes/total_votes)

# find winner by using mode


def winner(candidates):
    return mode(candidates)


election_winner = winner(candidates)

print("ELECTION RESULTS")
print("--------------------")
print(f"Total Votes: {total_votes}")
print("--------------------")
print(f"Khan: {Khan_percent} {Khan_votes}")
print(f"Correy: {Correy_percent} {Correy_votes}")
print(f"Li: {Li_percent} {Li_votes}")
print(f"O'Tooley: {OTooley_percent} {OTooley_votes}")
print("--------------------")
print(f"Winner: {election_winner}")


# Output to txt file
PyPoll = open("PyPoll.txt", "w")

PyPoll.writelines("ELECTION RESULTS")
PyPoll.writelines("\n--------------------")
PyPoll.writelines(f"\nTotal Votes: {total_votes}")
PyPoll.writelines("\n--------------------")
PyPoll.writelines(f"\nKhan: {Khan_percent} {Khan_votes}")
PyPoll.writelines(f"\nCorrey: {Correy_percent} {Correy_votes}")
PyPoll.writelines(f"\nLi: {Li_percent} {Li_votes}")
PyPoll.writelines(f"\nO'Tooley: {OTooley_percent} {OTooley_votes}")
PyPoll.writelines("\n--------------------")
PyPoll.writelines(f"\nWinner: {election_winner}")