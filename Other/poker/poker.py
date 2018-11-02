"""
High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
"""
global rank_conv
global data
rank_conv = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"A":14}

def read_file(filename):
    file = open(filename+".txt","r")
    lines = file.readlines()
    data = []
    for line in lines:
        line = line[:-1]
        line = line.split(" ")
        data.append(line)
    return data

data = read_file("poker")

def consecutive(numbers):    # Checks if numbers are consecutive
    return sorted(numbers) == range(min(numbers), max(numbers)+1)

def same_suit(suits):     # Checks if cards are the same suit
    return all(x==suits[0] for x in suits)

def same_value(numbers):     # Returns [number of occurrences, repeated value]
    counts = [0,0,0,0,0]
    for i in range(5):
        counts[i] = numbers.count(numbers[i])
    if max(counts) == 4:
        return [4,[numbers[counts.index(4)],numbers[counts.index(1)]]]
    elif max(counts) == 3 and counts.count(0) == 3:
        return [3,[numbers[counts.index(3)],numbers[counts.index(2)]]]
    elif max(counts) == 3:
        others = [value for value in numbers if value != numbers[counts.index(3)]]
        return [3,[numbers[counts.index(3)]]+sorted(others)]
    elif max(counts) == 2 and counts.count(2) == 2:
        pair1 = numbers[counts.index(2)]
        other = numbers[counts.index(1)]
        del(counts[counts.index(2)])
        return [2,[pair1,numbers[counts.index(2)+1],other]]
    elif max(counts) == 2:
        others = [value for value in numbers if value != numbers[counts.index(2)]]
        return [2,[numbers[counts.index(2)]]+sorted(others)]
    else:
        return [1,[]]

def process_hand(hand):     # Returns [rank, sorted list of highest value cards]
    numbers = []
    suits = []
    for card in hand:
        numbers.append(rank_conv[card[0]])
        suits.append(card[1])

    if consecutive(numbers) and same_suit(suits) and max(numbers) == 14:
        return [9]
    elif consecutive(numbers) and same_suit(suits):
        return [8,max(numbers)]
    elif same_value(numbers)[0] == 4:
        return [7,same_value(numbers)[1]]
    elif same_value(numbers)[0] == 3 and len(same_value(numbers)[1]) == 2:
        return [6,same_value(numbers)[1]]
    elif same_suit(suits):
        return [5,sorted(numbers)]
    elif consecutive(numbers):
        return [4,max(numbers)]
    elif same_value(numbers)[0] == 3:
        return [3,same_value(numbers)[1]]
    elif same_value(numbers)[0] == 2 and len(same_value(numbers)[1]) == 3:
        return [2,same_value(numbers)[1]]
    elif same_value(numbers)[0] == 2:
        return [1,same_value(numbers)[1]]
    else:
        return [0,sorted(numbers)]

p1_score = 0
p2_score = 0

for game in data:
    p1_hand = game[0:5]
    p2_hand = game[5:10]
    p1_processed = process_hand(p1_hand)
    p2_processed = process_hand(p2_hand)
    if p1_processed[0] > p2_processed[0]:
        p1_score += 1
    elif p1_processed[0] < p2_processed[0]:
        p2_score += 1
    else:
        for i in range(len(p1_processed[1])):
            if p1_processed[1][i] > p2_processed[1][i]:
                p1_score += 1
                break
            elif p1_processed[1][i] < p2_processed[1][i]:
                p2_score += 1
                break

print(p1_score,p2_score)


