#!/usr/bin/env python

import collections

input_file = "input"

cards_order = "AKQT98765432"
data = [(cards, int(bid)) for cards, bid in [line.split() for line in open(input_file).read().splitlines()]]


def get_hand_rank(cards, use_joker=False):
    card_counts = collections.Counter(cards)
    if use_joker and 0 < card_counts["J"] < 5:
        most_common, _ = collections.Counter(card_counts | {"J": 0}).most_common(1)[0]
        return get_hand_rank(cards.replace("J", most_common), use_joker=False)

    counts = sorted(card_counts.values())
    match counts:
        case [5]:
            return 1
        case [1, 4]:
            return 2
        case [2, 3]:
            return 3
        case [1, 1, 3]:
            return 4
        case [1, 2, 2]:
            return 5
        case [1, 1, 1, 2]:
            return 6
        case [1, 1, 1, 1, 1]:
            return 7
        case _:
            raise ValueError("Invalid cards")


def get_winnings(hands, use_joker=False):
    order = "AKQT98765432J" if use_joker else "AKQJT98765432"
    ordered_hands = sorted(
        (([get_hand_rank(cards, use_joker)] + [order.index(card) for card in cards], bid) for cards, bid in hands),
        reverse=True,
    )
    return sum(rank * bid for rank, (_, bid) in enumerate(ordered_hands, start=1))


print(get_winnings(data))
print(get_winnings(data, use_joker=True))
