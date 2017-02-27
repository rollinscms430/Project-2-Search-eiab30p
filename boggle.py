import random

def createBoard():
    """ This is return the dictionary called board with a key letter pair """
    return {(x, y): random.choice('abcdefghijklmnopqrstuvwxyz') for x in range(n) for y in range(n)}

def neighborhood():
    neigh = {}

    """ getting the keys in the board to then pull the letters from dictionary
        called board
    """
    for position in board:
        
        x, y = position
        
        """ This looks for letters around a selected cell on the board """
        positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                     (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
                     
        """ Makes sure letters viewed are not beyond the board we don't wrap around """
        neigh[position] = [p for p in positions if 0 <= p[0] < n and 0 <= p[1] < n]
        
    return neigh

def cell_list(path):
    """ This is taking the list of keys (x,y) taking the letters and return a
        word to each in the dictionary """
    #print([board[p] for p in path])
    return ''.join([board[p] for p in path])

def search(path):
    """ We have a list of possible words as well as a dictionary 
        to check if the word is an actual word. we will then 
        put those in the path to get the next word
    """
    word = cell_list(path)
    if word not in possible:
        return
    if word in dictionary:
        paths.append(path)
    for next_pos in neighbours[path[-1]]:
        if next_pos not in path:
            search(path + [next_pos])

def dictionary():
    """ Creates the word text and add it to 
        the dictionary like in prior projects. 
        Then we will look for all of the other words that is 
        before that word plus itself
    """
    possible, dictionary = set(), set()
    with open('words.txt') as text:
        for word in text:
            word = word.strip()
            dictionary.add(word)

            for i in range(len(word)):
                possible.add(word[:i + 1])

    return dictionary, possible

def get_words():
    """ get the letters and show the word"""
    match_word = []
    for position in board:
        search([position])
    for p in paths:
        found = 1
        for word in match_word:
            if cell_list(p) == word:
                found = 0
        if found:
            match_word.append(cell_list(p))

    return match_word

def print_board(board):
    s = ''
    for y in range(n):
        for x in range(n):
            s += board[x, y] + ' '
        s += '\n'
    print s

n = int(raw_input('Enter Size of Board n X n: '))

board = createBoard()

neighbours = neighborhood()
dictionary, possible = dictionary()
paths = []
print_board(board)
matches =  get_words()
print get_words()

            