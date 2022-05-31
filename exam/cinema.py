from argparse import ArgumentError, ArgumentTypeError
from enum import Enum

#test

class TypeBillet(Enum):
    PleinTarif = 0
    Etudiant = 1
    UnderAge = 2


class Billet():
    _type = TypeBillet.PleinTarif

    def __init__(self, type):
        self._type = type

    @property
    def type(self):
        return self._type

class Film():
    _nom = ""
    _affiche = ""
    _listeHoraire = list()

    def __init__(self, nom, affiche, horaires):
        self._nom = nom
        self._affiche = affiche
        self._listeHoraire = horaires

    @property
    def nom(self):
        return self._nom

    @property
    def horaires(self):
        return self._listeHoraire

    @property
    def affiche(self):
        return self._affiche


class Borne():
    _listeSeance = list()
    _seanceSelectionnee = None
    _billetsSelectionnes = list()
    _estPayee = False
    _estValidee = False

    @property
    def facture(self):
        total = 0
        for billet in self._billetsSelectionnes:
            if billet.type == TypeBillet.PleinTarif:
                total += 15.50
            elif billet.type == TypeBillet.Etudiant:
                total += 10.50
            elif billet.type == TypeBillet.UnderAge:
                total += 7.50
            else:
                raise ArgumentTypeError("TypeBillet unknown!")

        return total

    @property
    def estAnnulee(self): 
        return self._seanceSelectionnee == None and self._billetsSelectionnes == []

    @property
    def estValide(self): 
        return self._seanceSelectionnee != None and len(self._billetsSelectionnes) > 0

    @property
    def estPayee(self): 
        return self._estPayee

    @property
    def estValidee(self): 
        return self._estValidee

    def __init__(self, listeSeance):
        if isinstance(listeSeance, list):
            if not all(isinstance(elem, Film) for elem in listeSeance):
              raise ArgumentTypeError("must be a list of Film!")
        else:
            raise ArgumentTypeError("must be a list!")

        self._listeSeance = listeSeance

    def consulterSeance(self):
        return self._listeSeance

    def selectionnerSeance(self, seance, horaire):
        if not isinstance(seance, Film):
            raise ArgumentTypeError("seance must be a Film!")
        if not isinstance(horaire, str):
            raise ArgumentTypeError("horaire must be a string!")

        self._seanceSelectionnee = (seance, horaire)
        return True

    def selectionnerBillet(self, billets):
        if isinstance(billets, list):
            if not all(isinstance(elem, Billet) for elem in billets):
              raise ArgumentTypeError("must be a list of Billets!")
        else:
            raise ArgumentTypeError("must be a list!")
        
        self._billetsSelectionnes = billets
        return True

    def valider(self):
        if self.estValide: 
            self._estValidee = True
        else:
            self._estValidee = False
        return self._estValidee

    def annulerCommande(self):
        self._billetsSelectionnes = list()
        self._seanceSelectionnee = None
        self._estPayee = False
        self._estValidee = False

    def payer(self, somme):
        if not self.estValidee:
            raise BaseException("command must be confirmed!")

        reste = somme - self.facture
        if reste < 0:
            self._estPayee = False
        else:
            self._estPayee = True
        return (self._estPayee, reste)

    def imprimer(self):
        if not self.estValidee or not self.estPayee:
            raise BaseException("command must be confirmed and payed!")

        return True


if __name__ == '__main__':
    initSeance = [
        Film("Die Hard", "affiche de die hard", ["12:40", "16:00", "20:30"]),
        Film("Maman j'ai rate l'avion", "affiche de maman j'ai rate l'avion", [
             "11:00", "13:10", "15:50", "19:00"])
    ]

    # init borne
    borne = Borne(initSeance)
    print("borne initialisee!")

    # consultation
    seances = borne.consulterSeance()
    print("consultation séances:")
    for seance in seances:
        print("- %s : %s" %(seance.nom, ", ".join(horaire for horaire in seance.horaires)))

    # selection seance
    seance = seances.pop(0)
    horaire = seance.horaires.pop()
    seanceSelectionnee = borne.selectionnerSeance(seance, horaire)
    print("seance selectionne ? %s" % seanceSelectionnee)

    # selection billet
    billets = list()
    billets.append(Billet(TypeBillet.PleinTarif))
    billets.append(Billet(TypeBillet.Etudiant))
    billetSelectionne = borne.selectionnerBillet(billets)
    print("billet(s) selectionne(s) ? %s" % billetSelectionne)

    # validation
    estValidee = borne.valider()
    print("commande validee ? %s" % estValidee)

    # payer
    (estPayee, reste) = borne.payer(26)
    print("commande payee (%d euros) ? %s" % (reste, estPayee))

    # imprimmer
    estImprimee = borne.imprimer()
    print("commande imprimee ? %s" % estImprimee)