#First pip install random-word
from random_word import RandomWords
r = RandomWords()

# Return a single random word
print(r.get_random_word(hasDictionaryDef="true", includePartOfSpeech="noun,verb,adjective", minCorpusCount=5, maxCorpusCount=10, 
    minDictionaryCount=1, maxDictionaryCount=10, minLength=5, maxLength=5))
