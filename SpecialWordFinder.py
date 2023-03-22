from wordfinder import WordFinder

class SpecialWordFinder(WordFinder):
    """ returns random word while ignoring blank lines and lines that start with a # symbol """
    def parse(self, dict_file):
        """Parse dict_file into a list of words, excluding blank lines and comments"""
        return [word.strip() for word in dict_file if word.strip() and not word.startswith('#')]

sp_wf = SpecialWordFinder('specialwords.txt')
sp_wf.random()           