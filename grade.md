# Grade

## Anagrams

Good work!

## Word Ladder

First time a ran it I got this errror:

```
write a start word: snakes
write an ending word: brains
Traceback (most recent call last):
  File "leetcode.py", line 59, in <module>
    print final_queue.get([0])
AttributeError: 'list' object has no attribute 'get'
```

I removed the offending line and ran it again. I let it run for about 5 minutes but it only printed `None` two times and never
finished or printed a solution.

Your approach looks like it could work; I don't see anythign obviously wrong.
I would point out, though, you aren't doing a BFS: you're doing a recursive depth-first search.

-15

## Boggle

Okay. The first time I ran it and tried to input `4 X 4`, following the input instructions, it crashed. It turns out I needed to input only
`4`. You don't need to have any input or random board generation anwyay, since I gave you a test board to use in the project description.

That said, it looks like your search algorithm works and prints out the words that exist on the random board. This is an efficient
depth-first search implementation.  Good work on that part.

## Total

85 / 100
