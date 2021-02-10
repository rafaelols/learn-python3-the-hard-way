WORD_TYPES = {
    'north': 'direction',
    'south': 'direction',
    'east': 'direction',
    'west': 'direction',
    'go': 'verb',
    'kill': 'verb',
    'eat': 'verb'
}

def scan(sentence):
    words = sentence.split()
    result = []
    for word in words:
        tuple = (WORD_TYPES[word], word)
        result.append(tuple)
    return result