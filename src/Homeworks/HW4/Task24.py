# In a special ranking system, each voter gives a rank from highest to lowest to all
# teams participating in the competition.
# The ordering of teams is decided by who received the most position-one votes. If two
# or more teams tie in the first position, we consider the second position to resolve the
# conflict, if they tie again, we continue this process until the ties are resolved. If two or
# more teams are still tied after considering all positions, we rank them alphabetically
# based on their team letter.
# You are given an array of strings votes which is the votes of all voters in the ranking
# systems. Sort all teams according to the ranking system described above.
# Return a string of all teams sorted by the ranking system.


def ranking(votes):
    number = len(votes[0])

    teams = {t: [0] * number + [t] for t in votes[0]}

    for vote in votes:
        for i in range(number):
            teams[vote[i]][i] -= 1

    return "".join(t[-1] for t in sorted(teams.values()))


votes = ['ABC', 'ACB', 'ABC', 'ACB', "ACB"]
votes2 = ['WXYZ', 'XYZW']
print(ranking(votes))
print(ranking(votes2))
