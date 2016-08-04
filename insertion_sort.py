def run_insertion(items):
    """
    insertions sort
    """
    cards_len = len(cards)
    for j in range(1, cards_len):
        element = cards[j]
        previous_index = j-1
        previous_element = cards[previous_index]
        while previous_index > -1 and previous_element > element:
            cards[previous_index+1] = cards[previous_index]
            previous_index = previous_index-1
        cards[previous_index+1] = element
    return cards


if __name__ == '__main__':
    cards = [12, 11, 13, 5, 6]
    print "input {0}".format(cards)
    run_insertion(cards)
    print "output {0}".format(cards)
