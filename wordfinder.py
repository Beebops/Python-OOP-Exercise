"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """ Returns a random word from dictionary
    >>> wf = WordFinder("words.txt")
    3 words read.

    >>> wf.rand() in ['Python', 'JavaScript', 'Rust']
    True

    >>> wf.rand() in ['Python', 'JavaScript', 'Rust']
    True
    """

    def __init__(self, path):
       """Reads dictionary and returns number of words read"""
       dict_file = open(path, 'r')
       self.words = self.parse(dict_file)
       print(f"{len(self.words)} words read.")

    def parse(self, dict_file):
        """ Parse dict_file into a list of words"""
        return [word.strip() for word in dict_file]   

    def random(self):
        """returns a random word from dict_file"""
        return random.choice(self.words)
        
wf = WordFinder('words.txt')
print(wf.random())
