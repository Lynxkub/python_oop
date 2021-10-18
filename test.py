


"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start=0):
        self.start=self.next=start

    def __repr__(self):
        return f"SerialGenerator start={self.start} next={self.next}"

    def generate(self):
        self.next+=1
        return self.next-1
    def reset(self):
        self.next=self.start


"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
    def __init__(self,path):
        dict_file=open(path)
        self.words=self.parse(dict_file)
        print(f"{len(self.words)} words read")
    
    def parse(self, dict_file):
        return [w.strip() for w in dict_file]
    
    def random(self):
        return random.choice(self.words)
        

class SpecialWordFinder(WordFinder):
    def parse(self, dict_file):
        return [w.strip() for w in dict_file if w.strip() and not w.startswith("#")]