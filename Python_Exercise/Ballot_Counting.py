# You have a list of unordered votes
# Find votes for each candidate
# Find winners (possibly 2 or more)
# Minimal use of built-in functions
polls = ["Ban" , "Andy", "Ban", "Andy", "Carol", "Carol", "Carol", "Andy",
         "Ban", "Andy", "Carol", "Andy", "Carol", "Carol"]
# candidate list to store new condidate
candidates = []
# votes of candidate of the same index
votes = []
for person in polls:
    if person not in candidates:
        candidates.append(person)
        votes.append(1)
    else:
        candidate_index = candidates.index(person)
        votes[candidate_index] += 1
max_vote = 0
max_candidates = []

for i in range(len(votes)):
    if votes[i] > max_vote:
        max_vote = votes[i]
        candidate = candidates[i]
        # overwrite original list with just 1 candidate
        max_candidates = []
        max_candidates.append(candidate)
    elif votes[i] == max_vote:
        candidate = candidates[i]
        max_candidates.append(candidate)
        
print("The highest vote goes to: ")
print(max_candidates, sep="\n")
print("Each person has " + str(max_vote) + " votes.")
