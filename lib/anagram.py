# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        
    def match(self, list):
        matches = [string for string in list if sorted(string) == sorted(self.word)]
        return matches
        # for string in list:
        #     if sorted(string) == sorted(self.word):
        #         return string
        