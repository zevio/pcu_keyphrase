import unittest

from pcu_keyphrase.pcu_keyphrase import getKeyphrases

class test_pcu_keyphrase(unittest.TestCase):

	def test_getKeyphrase(self):
		try:
			file = open("data/test.txt", "r") # read test file
		except IOError:
			print('cannot open')
		else:
			text = file.read() # content of the test file
			print(text)
			self.assertIn('Information extraction', text)
			keyphrases = getKeyphrases(text)
			self.assertNotEqual(keyphrases, []) # keyphrases not empty
			file.close()

if __name__ == '__main__':
	unittest.main()