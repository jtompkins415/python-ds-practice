def multiple_letter_count(phrase):
    # """Return dict of {ltr: frequency} from phrase.

    #     >>> multiple_letter_count('yay')
    #     {'y': 2, 'a': 1}

    #     >>> multiple_letter_count('Yay')
    #     {'Y': 1, 'a': 1, 'y': 1}
    # """

    freq = {}

    for ltr in phrase:
        if ltr in freq:
            freq[ltr] +=1
        else:
            freq[ltr] = 1

    return freq

    