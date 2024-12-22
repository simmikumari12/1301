import sys

def read_input(fname):  
    with open(fname) as f:
        data = f.read().splitlines()
        f.close()
    return data

# hand = "as:4c:5h:ks:9s"
# takes as input, hand, and returns True if hand is "valid",
# and False otherwise
def valid_hand(hand):
    # check if hand has 5 cards
    cards = hand.split(":")
    if len(cards) != 5:
        return False
    for card in cards:
        if len(card) != 2:
            return False
        else:
            if card[0] not in ['2','3','4','5','6','7','8','9','t','j','q','k','a']:
                return False
            if card[1] not in ['c','d','h','s']:
                return False
    return True
    
# takes as input, hand, and returns a "dictionary" whose keys are
# the ranks and the values are the number of cards in the hand for 
# the given rank
def process_ranks(hand):
    drank = {}
    for n in range(2,15):
        drank[n] = 0
    cards = hand.split(":")
    convert = {'2':2, '3':3, '4': 4, '5': 5, '6':6, '7':7, '8':8, '9':9, 't':10, 'j':11, 'q':12, 'k':13, 'a':14}
    for card in cards:
        rank = card[0]
        drank[convert[rank]] = drank[convert[rank]] + 1 #double dictionary
    return drank

# takes as input, hand, and returns a "dictionary" whose keys are
# the suits and the values are the number of cards in the hand for 
# the given suit
def process_suits(hand):
    dsuit = {'c':0, 'd':0, 'h':0, 's':0}
    cards = hand.split(":")
    for card in cards:
        dsuit[card[1]] = dsuit[card[1]] + 1
    return dsuit

# takes the ranks_dict for a particular hand as input and returns True 
# if the hand contains a "straight"
def check_straight(ranks_dict):
    ranks = []
    for rank, count in ranks_dict.items():
        if count > 0:
            ranks.append(rank)
    ranks.sort()
    for i in range(len(ranks) - 4):
        if ranks[i] + 4 == ranks[i + 4]:
            return True
    return False

# takes the suits_dict for a particular hand as input and returns True 
# if the hand contains a "FLUSH"
def check_flush(process_suit):
    for suit, count in process_suit.items():
        if count == 5:
            return True
    return False

# takes the ranks_dict for a particular hand as input and returns True 
# if the hand contains a "FOURS"
def check_fours(ranks_dict):
    for rank, count in ranks_dict.items():
        if count ==4:
            return True
    return False

# takes the ranks_dict for a particular hand as input and returns True 
# if the hand contains a "THREES"
def check_threes(ranks_dict):
	for ranks, count in ranks_dict.items():
            if count == 3:
                return True
         
# takes the ranks_dict for a particular hand as input and returns the 
# number of "PAIRS".
def check_pairs(ranks_dict):
    count_pair =0
    for ranks, count in ranks_dict.items():
            if count == 2:
                count_pair = count_pair +1
    return count_pair
            
# takes boolean inputs straight, flush, four, three, pair for a hand
# and returns the highest hand classification.
def hand_type(straight,flush,four,three,pairs):
    if straight and flush:
        return "Straight flush"
    elif straight:
        return "Straight"
    elif four:
        return "Four of a kind"
    elif three:
        return "Three of a kind"
    elif pairs == 1:
        return "Pair"
    elif pairs == 2:
        return "Two pairs"
    elif flush:
        return "Flush"
    elif pairs ==1 and three:
        return "Full house" 
    else:
        return "High card"

# takes the ranks_dict for a particular hand as input and returns True 
# if the hand contains a "straight"
# def check_straight(ranks_dict):
    
def main():
    data = read_input(sys.argv[1])
    for hand in data:
        if valid_hand(hand):
            ranks_dict = process_ranks(hand)
            suits_dict = process_suits(hand)
            straight = check_straight(ranks_dict)
            flush = check_flush(suits_dict)
            four = check_fours(ranks_dict)
            three = check_threes(ranks_dict)
            pairs = check_pairs(ranks_dict)
            classification = hand_type(straight,flush,four,three,pairs)
            print(hand, classification)
        else:
            print(hand,"Invalid Card!")

main()
