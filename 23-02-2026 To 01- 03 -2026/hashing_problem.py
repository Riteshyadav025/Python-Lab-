def winner(arr):
    vote_count = {}

    # Count votes
    for name in arr:
        vote_count[name] = vote_count.get(name, 0) + 1

    max_votes = 0
    winner_name = ""

    # Find winner with tie-breaking (lexicographically smallest)
    for name in vote_count:
        if (vote_count[name] > max_votes) or \
           (vote_count[name] == max_votes and name < winner_name):
            max_votes = vote_count[name]
            winner_name = name

    return [winner_name, str(max_votes)]

arr = ["john", "johnny", "jackie", "johnny", "john", "jackie",
       "jamie", "jamie", "john", "johnny", "jamie", "johnny", "john"]

print(winner(arr))
