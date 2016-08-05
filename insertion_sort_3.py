def run_insertion(items):
    """
    insertions sort non-incressing order

    start from end of a loop
    """
    cards_len = len(cards)
    j = cards_len - 1
    while j > -1:
        i = j - 1
        key = cards[j]
        while i > -1 and cards[i] < cards[j]:
            cards[i+1] = cards[i]
            i = i - 1
        cards[i+1] = key
        j = j - 1

if __name__ == '__main__':
    cards = [12, 11, 13, 5, 6]
    run_insertion(cards)
    print cards
