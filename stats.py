def number_of_words(text):
    words = text.split()
    num_words = len(words)
    return num_words
    
def count_chars(text):
    # take the text from the book as a string
    lowered = text.lower()
    # create a dictionary for the keys (each individual ch) and their values (each time the ch appears)
    counts = {}
    # for each ch in the lowercase text (to avoid double counting based on case sensitivty)
    for ch in lowered:
        # if the ch is already in the counts
        if ch in counts:
            # ch counts is incremented.
            counts[ch] = counts[ch] + 1
            # if not already in the counts, then initialize at 1.
        else:
            counts[ch] = 1
    return counts

def sort_on(item):
    return item["num"]

def sorted_list(counts):
    char_list = []
    for ch in counts:
        char_list.append({"char": ch, "num": counts[ch]})
    char_list.sort(key=sort_on, reverse=True)
    return char_list

