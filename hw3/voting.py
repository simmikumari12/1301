import sys

def read_ballots(filename):
    with open(filename, 'r') as file:
        ballots = []
        for line in file:
            preferences = [candidate.strip() for candidate in line.strip().split(',')]
            ballots.append(preferences)
    return ballots # returns the list of the items in the files

def count_first_choice_votes(ballots, remaining_candidates):
    vote_count = {candidate: 0 for candidate in remaining_candidates}
    for ballot in ballots:
        for candidate in ballot:
            if candidate in remaining_candidates:
                vote_count[candidate] += 1
                break
    return vote_count

def eliminate_candidates(vote_count):
    min_votes = min(vote_count.values())
    candidates_to_eliminate = {candidate for candidate, votes in vote_count.items() if votes == min_votes}
    return candidates_to_eliminate

def run_ranked_voting(ballots):
    all_candidates = []
    for ballot in ballots:
        for candidate in ballot:
            if candidate not in all_candidates:  # Avoid duplicates
                all_candidates.append(candidate)
    remaining_candidates = all_candidates.copy()
    while len(remaining_candidates) > 1:
        vote_count = count_first_choice_votes(ballots, remaining_candidates) # Calling count_first_choice_votes and passing ballots and remaining candidates asparameter
        print(f"Vote count: {vote_count}")
        candidates_to_eliminate = eliminate_candidates(vote_count)
        remaining_candidates = [candidate for candidate in remaining_candidates if candidate not in candidates_to_eliminate]
        if not remaining_candidates:
            return sorted(all_candidates)  
    return remaining_candidates[0]


def main():
    if len(sys.argv) != 2:
        print("Incorect number of argument!")
        sys.exit(1)
    filename = sys.argv[1]
    ballots = read_ballots(filename)
    print(f"Ballots: {ballots}")
    winner = run_ranked_voting(ballots)
    print(f"Winner: {winner}")

main()
