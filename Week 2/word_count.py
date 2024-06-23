def word_count(text):
    text = text.lower()
    text = text.replace('.', '')
    text = text.replace(',', '')
    sentences = text.split()

    dictionary = {}

    for c in sentences:
        if c in dictionary:
            dictionary[c] += 1
        else:
            dictionary[c] = 1

    keys = list(dictionary.keys())
    keys.sort()
    sorted_dict = {i: dictionary[i] for i in keys}

    return sorted_dict
