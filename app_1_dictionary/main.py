# -*- coding: utf-8 -*-

""" This is the main file of the dictionary app

"""


from translator import Translator

if __name__ == '__main__':
	dic = Translator('data.json')
#	print (dic.translate(input('Enter the word\n>>>')) )
	dic.translate(input('Enter the word\n>>>'))