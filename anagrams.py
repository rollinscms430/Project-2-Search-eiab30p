#Possibly a breadth first search since we are checking each words sort
# before going down its childrean 

#Setting Dictionary up
words = {}

# We are opening the file using with it will close it when it ends no need to 
# do any extra stuff
with open("words.txt") as text:
    for line in text:
        # We are seperating the words by a space to then sort and rejoin together
        #  removing that space
        key = ''.join(sorted(line))
        # We are cleaning the word from extra spaces or new lines 
        val = line.strip()
        # We are setting the key with a value. The setdefault will assign a default
        # value of nothing first if a value does not append to it otherwise it will
        # appened the value associated with the key
        words.setdefault(key,[]).append(val)
            
# We are soring the keys in the dictionary and then finding the key key with more
# than two values then printing those values

for key in sorted(words.iterkeys()):
    if len(words[key]) > 1:
        print  words[key]
        