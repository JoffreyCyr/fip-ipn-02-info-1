from argparse import ArgumentTypeError
from enum import Enum

class Taille(Enum) :
	Petit = 0
	Moyen = 0.5
	Grand = 1
	# Valeur du surcoût


class Commande():
	_jus = None
	_taille = None
	_quantite = 0
	_prix = 0

	def __init__(self, jus, quantite, taille) :
		if isinstance(jus,Jus) : self._jus=jus
		else : raise ArgumentTypeError

		if isinstance(quantite,int) : self._quantite=quantite
		else : raise ArgumentTypeError

		if isinstance(taille,Taille) : self._taille=taille
		else : raise ArgumentTypeError

		self._prix = ( jus.prix + taille.value ) * quantite

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
			#if all( isinstance(cles,Ingredient) for cles in ingredients.keys ) :
			self._ingredients=ingredients
			#else : raise ArgumentTypeError
		else : raise ArgumentTypeError

		if isinstance(prix,float) or isinstance(prix,int): self._prix=prix
		else : raise ArgumentTypeError

	@property
	def nom(self) :
		return self._nom

	@property
	def ingredients(self) :
		return self._ingredients

	@property
	def prix(self) :
		return self._prix


class Ingredient():
	_nom = ""
	_quantite = 0.0

	def __init__(self,nom,quantite=1.0):
		if isinstance(nom,str) : self._nom=nom
		else : raise ArgumentTypeError

		if isinstance(quantite,float) or isinstance(quantite,int) : self._quantite=quantite
		else : raise ArgumentTypeError

	@property
	def nom(self):
		return self._nom

	@property
	def quantite(self):
		return self._quantite

	def setQuantite(self,qte) :
		self._quantite=qte


class Barman() :
	_listeJus = list()
	_listeCommande = list()
	_note = 0

	def __init__(self,listeJus):
		if isinstance(listeJus,list):
			if all( isinstance(elem,Jus) for elem in listeJus ) :
				self._listeJus = listeJus
			else :
				raise ArgumentTypeError
		else :
			raise ArgumentTypeError

	@property
	def note(self):
		return self._note

	@property
	def listeCommande(self):
		return self._listeCommande

	def demanderBoissons(self) :
		return self._listeJus

	def verifierQuantite(self, commande):
		if not isinstance(commande, Commande): raise ArgumentTypeError
		for i in commande.jus.ingredients :
			if i.quantite - commande.jus.ingredients[i] * commande.quantite < 0 : return False
		return True

	def ajouterCommande(self, commande) :
		if not isinstance(commande,Commande) : raise ArgumentTypeError

		if self.verifierQuantite(commande) :
			self._listeCommande.append(commande)
			self._note += commande.prix
			for i in commande.jus.ingredients :
				i.setQuantite(i.quantite - commande.jus.ingredients[i] * commande.quantite)
			return True
		return False

	def payer(self, somme):
		if not (isinstance(somme,float) or isinstance(somme,int)) : raise ArgumentTypeError
		self._note -= somme
		return self._note

	def terminer(self, texte="terminée"):
		self._listeCommande.clear()
		self._note = 0
		print(f"Commande {texte}")

if __name__ == '__main__' :

	mangue = Ingredient("Mangue",10)
	orange = Ingredient("Orange",10)
	guajana = Ingredient("Guajana",10)
	pomme = Ingredient("Pomme",10)
	gingembre = Ingredient("Gingembre",10)
	citron = Ingredient("Citron",10)
	goyave = Ingredient("Goyave",10)
	ananas = Ingredient("Ananas",10)
	banane = Ingredient("Banane",10)
	carotte = Ingredient("Carotte",10)
	celeri = Ingredient("Celeri",10)
	betterave = Ingredient("Betterave",10)


	listeJus = [
		Jus("The Boost",{mangue:0.5,orange:2,guajana:1},5),
		Jus("The Fresh",{pomme:3,gingembre:1,citron:1},4),
		Jus("The Fusion",{goyave:1,ananas:0.25,banane:0.5},5),
		Jus("The Detox",{carotte:3,celeri:1,betterave:1},3.5)
	]

	barman = Barman(listeJus)


	carte = barman.demanderBoissons()
	for c in carte :
		print(f"{c.nom} : {c.prix}$")

	# True si quantité d'ingrédients suffisante, False si quantité insuffisante
	print(barman.ajouterCommande( Commande(carte[0],5,Taille.Moyen) ))
	#print(barman.ajouterCommande( Commande(carte[0],6,Taille.Petit) ))

	#barman.terminer("annulée")

	while barman.note > 0 :
		print(f"Reste à payer : {barman.note}")
		barman.payer(int(input("somme : ")))

	if barman.note < 0 :
		print(f"Rendu : {abs(barman.note)}")

	barman.terminer()