from argparse import ArgumentTypeError
from enum import Enum


class Taille(Enum) :
	Petit : 0
	Moyen : 0.5
	Grand : 1
	# Valeur du surcoût


class Commande():
	_jus = None
	_taille = None
	_quantite = 0
	_prix = 0

	def __init__(self, jus, quantite, taille=Taille.Petit) :
		if isinstance(jus,Jus) : self._jus=jus
		else : raise ArgumentTypeError

		if isinstance(quantite,int) : self._quantite=quantite
		else : raise ArgumentTypeError

		if isinstance(taille,Taille) : self._taille=taille
		else : raise ArgumentTypeError

		self._prix = ( jus.prix + taille ) * quantite

	@property
	def jus(self):
		return self._jus

	@property
	def taille(self):
		return self._taille

	@property
	def quantite(self):
		return self._quantite

	@property
	def prix(self):
		return self._prix



class Jus():
	_nom = ""
	_ingredients = dict()
	_prix = 0.0

	def __init__(self, nom, ingredients, prix) :
		if isinstance(nom,str) : self._nom=nom
		else : raise ArgumentTypeError

		if isinstance(ingredients,dict) :
			if all( isinstance(cles,Ingredient) for cles in ingredients.keys ) :
				self._ingredients=ingredients
			else : raise ArgumentTypeError
		else : raise ArgumentTypeError

		if isinstance(prix,float) : self._prix=prix
		else : raise ArgumentTypeError

	@property
	def nom(self) :
		return self._nom

	@property
	def ingredients(self) :
		return self._ingredients

	@property
	def prix(self) :
		return self.prix


class Ingredient():
	_nom = ""
	_quantite = 0.0

	def __init__(self,nom,quantite=1.0):
		if isinstance(nom,str) : self._nom=nom
		else : raise ArgumentTypeError

		if isinstance(nom,float) : self._quantite=quantite
		else : raise ArgumentTypeError

	@property
	def nom(self):
		return self._nom

	@property
	def quantite(self):
		return self._quantite


class Barman() :
	_listeJus = list()
	_listeCommande = list()
	_chiffreAffaires = 0
	_note = 0

	def __init__(self,listeJus):
		if isinstance(listeJus,list):
			if all( isinstance(elem,Jus) for elem in listeJus ) :
				self._listeJus = listeJus
			else :
				raise ArgumentTypeError
		else :
			raise ArgumentTypeError

	def demanderBoissons(self) :
		return self._listeJus

	def verifierQuantite(commande):
		if not isinstance(commande, Commande): raise ArgumentTypeError
		return all( i.key.quantite - i.value * commande.jus.quantite for i in commande.jus.ingredients )

	def ajouterCommande(self, commande) :
		if not isinstance(commande,Commande) : raise ArgumentTypeError

		if self.verifierQuantite(commande) :
			self._listeCommande.append(commande)
			self._note += commande.prix
			for i in commande.jus.ingredients :
				i.key.quantite = i.key.quantite - i.value * commande.jus.quantite

	def payer(self, somme):
		if not isinstance(somme,float) : raise ArgumentTypeError
		self._note -= somme
		return self._note

	def terminer(self, texte="terminée"):
		self._listeCommande.clear()
		print(f"Commande {texte}")