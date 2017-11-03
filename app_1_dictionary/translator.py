# -*- coding: utf-8 -*-

""" This module is an app that works as a dictionary 

"""
import json
from difflib import get_close_matches#, SequenceMatcher

class Translator:
	"""This class is a dictionary of real english words

	"""
	def __init__(self, filename=''):
		self.data = json.load(open(filename,'r'))

	def getCloserWord(self, word=''):
		try:
			return get_close_matches(word, self.data.keys())[0]
		except:
			return "That word doesn't even exist, you moron :b"

	def printNiceMessage(self, word=''):
		print ("The word found was %s and has %d means:\n\n" % (word,len(self.data[word])))
		cont=1
		for meaning in self.data[word]:
			print ("%d > %s" % (cont, meaning))
			cont = cont+1

	def checkMatchedWord(self, word, matched_word):
		if word != matched_word:
			if matched_word == "That word doesn't even exist, you moron :b":
				print (matched_word)
			else:
				choice = input ("Did you mean '%s' ? Press yes or no\n>>>" % matched_word)
				if choice == 'yes':
					self.printNiceMessage(matched_word)
				elif choice == 'no':
					print ("Bye lala")
		else:
			#Call the method to print the word
			self.printNiceMessage(word)


	def translate(self, word=''):
		closest_word = self.getCloserWord(word.lower() )
		self.checkMatchedWord(word, closest_word)

	
