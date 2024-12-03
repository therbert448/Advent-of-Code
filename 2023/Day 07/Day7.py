"""
Advent of Code
2023 Day 7

@author: Tom Herbert
"""

day = 7

def open_file(day):
    filename = "Day" + str(day) + "inputs.txt"
    with open(filename) as file:
        inputs = [line.strip().split() for line in file.readlines()]
    hands = {line[0]: int(line[1]) for line in inputs}
    return hands    

def find_counts(hand, part):
    counts = {}
    for char in hand:
        if char in counts:
            continue
        counts[char] = hand.count(char)
    joker = 0
    if 'J' in counts and part == "Two": 
        joker = counts['J'] % len(hand)
        if joker: del counts['J']
    sortVal = sorted(counts.values(), reverse=True)
    sortVal[0] += joker
    score = "".join([str(v) for v in sortVal])
    return score

def play_cards(hands, types, cards, part):
    ranks = {t: [] for t in types}
    for hand in hands:
        rank = find_counts(hand, part)
        ranks[rank].append(hand)
    sortedRanks = []
    for hands in ranks.values():
        if not hands:
            continue
        hands = sorted(hands, key = lambda h: [cards.index(c) for c in h])
        sortedRanks += hands
    return sortedRanks

def part_one_and_two(hands, types, cards, part="One"):
    ranks = play_cards(hands, types, cards, part)
    total = 0
    for i, hand in enumerate(ranks):
        bid = hands[hand]
        total += bid * (i+1)
    print(f"Part {part} = {total}")

hands = open_file(day)

types = ['11111', '2111', '221', '311', '32', '41', '5']
cards = '23456789TJQKA'

part_one_and_two(hands, types, cards)
cards = 'J23456789TQKA'
part_one_and_two(hands, types, cards, "Two")