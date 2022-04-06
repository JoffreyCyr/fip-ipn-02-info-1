from argparse import ArgumentTypeError
from enum import Enum


class Classification(Enum):
	POISSON = 0
	INSECTE = 1
	OISEAU = 2
	MAMMIFERE = 3
	AMPHIBIEN = 4
	REPTILE = 5
	INVERTEBRE = 6

class Animal():
	_classification = None
	_name = ""

	def __init__(self, classification, name):
		#if not isinstance(classification,int) or not isinstance(name,str) :
		#	raise ArgumentTypeError

		self._classification = classification
		self._name = name

	def getClassification(self):
		return self._classification
	
	def getName(self):
		return self._name
		

class Chat(Animal):

	isCute = False

	def __init__(self, name):
		#if not isinstance(name,str):
		#	raise ArgumentTypeError
		super().__init__(Classification.MAMMIFERE, name)


class Chien(Animal):

	isCute = True

	def __init__(self, name):
		#if not isinstance(name,str):
		#	raise ArgumentTypeError
		super().__init__(Classification.MAMMIFERE, name)

chien = Chien("Guimauve")
print(chien.getName())