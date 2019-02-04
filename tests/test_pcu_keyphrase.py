import unittest
import json

from pcu_keyphrase.pcu_keyphrase import extractKeyphrases
from pcu_keyphrase.pcu_keyphrase import serializeKeyphrases

class test_pcu_keyphrase(unittest.TestCase):

	def test_extractKeyphrase(self):
		try:
			filename = "data/test.txt"
			file = open(filename, "r") # read test file
		except IOError:
			print('cannot open')
		else:
			text = file.read() # content of the test file
			print("- - - - - Text - - - - -")
			print(text)
			print("- - - - - Keyphrases - - - - -")
			self.assertIn('Information extraction', text)
			keyphrases = extractKeyphrases(text)
			self.assertNotEqual(keyphrases, []) # keyphrases not empty
			jsonfilename = filename.replace('.txt','.json')
			print("- - - - - Serialization - - - - -")
			print(jsonfilename)
			serializeKeyphrases(keyphrases, jsonfilename)
			file.close()

if __name__ == '__main__':
	unittest.main()