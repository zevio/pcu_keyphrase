import kleis.resources.dataset as kl
from operator import itemgetter
from itertools import combinations
import nltk
import json
from json import JSONEncoder

nltk.download('averaged_perceptron_tagger')

class Keyphrase: 
    def __init__(self, keyphrase_id, keyphrase_label, keyphrase_start, keyphrase_end, keyphrase_str):
        self.keyphrase_id = keyphrase_id # id
        self.keyphrase_label = keyphrase_label # label
        self.keyphrase_start = keyphrase_start # start position in the original text
        self.keyphrase_end = keyphrase_end # end position in the original text
        self.keyphrase_str = keyphrase_str # text segment
    def __repr__(self): # representation of a keyphrase
        return repr((self.keyphrase_id, self.keyphrase_label, self.keyphrase_start, self.keyphrase_end, self.keyphrase_str)) #

class KeyphraseEncoder(JSONEncoder):
    def default(self, object):
        if isinstance(object, Keyphrase):
            return object.__dict__
        else:
            return json.JSONEncoder.default(self, object)

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
        keyphrase_id, (keyphrase_label, (keyphrase_start, keyphrase_end)), keyphrase_str = keyphrase # representation of a keyphrase 
        print("Start : ", keyphrase_start)
        print("End : ", keyphrase_end) 
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
        keyphrase_id, (keyphrase_label, (keyphrase_start, keyphrase_end)), keyphrase_str = keyphrase # representation of a keyphrase
        keyphrases_obj.append(Keyphrase(keyphrase_id, keyphrase_label, keyphrase_start, keyphrase_end, keyphrase_str)) # create a Keyphrase and add it to the list
    return sorted(keyphrases_obj, key=lambda keyphrase:keyphrase.keyphrase_end) # sort the list of keyphrases according to the end position in the text

def serializeKeyphrases(keyphrases, filename): 
    """Serialize keyphrases in a JSON file.
    Parameter :
    keyphrases -- keyphrases
    filename -- path to the JSON file
    """
    with open(filename, "w", encoding="utf-8") as file:
        jsonString = ""
        keyphrases_obj=[]
        for keyphrase in keyphrases : 
            jsonString = KeyphraseEncoder().encode(keyphrase)
            keyphrases_obj.append(jsonString)
        json.dump(keyphrases_obj, file)
    file.close()

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

