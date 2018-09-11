import kleis.resources.dataset as kl
from operator import itemgetter
from itertools import combinations
import nltk

nltk.download('averaged_perceptron_tagger')

class Keyphrase: 
    def __init__(self, keyphrase_id, keyphrase_label, start, end, keyphrase_str):
        self.keyphrase_id = keyphrase_id # id
        self.keyphrase_label = keyphrase_label # label
        self.start = start # start position in the original text
        self.end = end # end position in the original text
        self.keyphrase_str = keyphrase_str # text segment
    def __repr__(self): # representation of a keyphrase
        return repr((self.keyphrase_id, self.keyphrase_label, self.start, self.end, self.keyphrase_str)) #

def getKeyphrases(text):
    """Get keyphrases of a text.
    Parameter :
    text -- text
    Return :
    keyphrases -- keyphrases of the text 
    """
    default_corpus = kl.load_corpus() # load default corpus
    default_corpus.training(filter_min_count=3) # recomended filter_min_count=3
    keyphrases = default_corpus.label_text(text) # label text
    for keyphrase in keyphrases:
        print("- - - - - Keyphrase - - - - -")
        keyphrase_id, (keyphrase_label, (start, end)), keyphrase_str = keyphrase # representation of a keyphrase 
        print("Start : ", start)
        print("End : ", end) 
        print("Text : ", keyphrase_str)
    return keyphrases

def sortKeyphrases(keyphrases):
    """Sort keyphrases.
    Parameter :
    keyphrases -- keyphrases
    Return :
    sorted_keyphrases -- sorted keyphrases
    """
    keyphrases_obj=[]
    for keyphrase in keyphrases: # for each keyphrase
        keyphrase_id, (keyphrase_label, (start, end)), keyphrase_str = keyphrase # representation of a keyphrase
        keyphrases_obj.append(Keyphrase(keyphrase_id, keyphrase_label, start, end, keyphrase_str)) # create a Keyphrase and add it to the list
    return sorted(keyphrases_obj, key=lambda keyphrase:keyphrase.end) # sort the list of keyphrases according to the end position in the text

def extractKeyphrases(text):
    """Extract keyphrases of a text.
    Parameter :
    text -- original text
    Return :
    sorted_keyphrases -- keyphrases of a text in order of appearance in the original text 
    """
    keyphrases=getKeyphrases(text) # get keyphrases
    sorted_keyphrases=sortKeyphrases(keyphrases) # sort them in order of appearance in the original text
    return sorted_keyphrases 
