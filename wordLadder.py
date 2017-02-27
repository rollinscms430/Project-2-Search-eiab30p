import collections

def creatGraph(dictionary, start, goal):
    graph=collections.defaultdict(list)
    letters='abcdefghijklmnopqrstuvwxyz'
    for word in dictionary:
        for i in range(len(word)):
            for k in letters:
                newword = list(word)
                newword[i] = k
                if ("".join(newword) in dictionary and "".join(newword) != word):
                    graph[word].append("".join(newword))
    return graph
    
def createDict(length, start_word):
    dictionary = {}
    length_of_start = len(start_word)
    with open("words.txt") as text:
        for line in text:
            length_of_line = len(line.strip())
            if length_of_start == length_of_line:
                key = line.strip()
                dictionary[key] = 0
    return dictionary


def findpath(graph, start, goal):
    paths=collections.deque([ [start] ])
    extended=set()
 
    while len(paths)!=0:
        currentPath=paths.popleft()
        currentWord=currentPath[-1]
        if currentWord==goal:
            return currentPath
        elif currentWord in extended:
            #already extended this word
            continue
 
        extended.add(currentWord)
        transforms=graph[currentWord]
        for word in transforms:
            if word not in currentPath:
                paths.append(currentPath[:]+[word])
 
    #no transformation
    return []

    
start_word = raw_input('Enter Start Word: ')
end_word = raw_input('Enter End Word: ')   

dictionary = createDict(range(len(start_word)), start_word)

graph = creatGraph(dictionary,start_word, end_word)

#print(graph)
print(findpath(graph,start_word, end_word))