def run_insertion(items):
    """
    insertions sort non-incressing order
    """
    cards_len = len(cards)
    for index in range(1, cards_len):
        key = cards[index]
        i = index - 1
        while i > -1 and key > cards[i]:
            cards[i+1] = cards[i]
            i = i - 1
        cards[i+1] = key

if __name__ == '__main__':
    cards = [12, 11, 13, 5, 6]
    print "in: {0}".format(cards)
    run_insertion(cards)
    print "out:{0}".format(cards)
