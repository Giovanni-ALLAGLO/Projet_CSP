#__author__      = "AG"

class Contrainte:
    """Summary : Classe définissant les contraintes d'une CSP.

    Parameters
    ----------
    l_couple : list
        Liste des couples possibles entre deux noeuds, [clé de contraintes(dict)] et [v_destination].
    v_destination: int
        Variable dont la valeur est en deuxieme position dans le couple.
    """
    def __init__(self,v_destination,couples:list):
        self.v_destination = v_destination
        self.l_couple = couples
        pass

class Csp:
    """Summary : Classe definisant un CSP(Constraint Satisfaction Problem).

    Parameters
    ----------
    name : str
        Nommer le CSP.
    nb_var : int
        Nombre de variable.
    nb_valeur : int
        Taille du domaine des varibales.
    densite : int
        Pourcentage de la densité des liaison entre deux variables.
    durete_contrainte : int
        Dureté _pourcentage entre 0 et 1_ sur les contraintes liant deux variables.
    contraintes : dict
        Dictionnaire etablissant les contraintes entre la variable clé et les variables id supérieur.
    domain : dict
        Dictionnaire associant chaque variable et une liste des élements de du domaine.
    """
    def __init__(self, name ="csp", nb_var = None ,nb_valeur= None, durete_contrainte = None , dense = None ):
        self.name = name
        self.nb_valeur = nb_valeur
        self.nb_var = nb_var
        self.durete_contrainte = durete_contrainte
        self.densite = dense
        self.contraintes = dict()
        self.domaines = dict()
        pass


    def ajoutVariable(self, v_id , v_domain:list)->None:
        """Summary : Ajout de la variable v_id au CSP.
                    Initialise la structure de données des contraintes. """
        if v_id not in self.domaines.keys(): # variable existe ?
            self.domaines[v_id] = v_domain
            self.contraintes[v_id] = []


    def ajoutContrainte(self, v_id1, v_id2, liste:list)->None:
        """Summary : Ajout de contrainte sur des variables existantes.

          Arguments
          ---------
          v_id1, v_id2 : type non-defini
            Variables telles que v_id1<v_id2
          liste : list
            Liste des valeurs permises entre v_id1 et v_id2
        """
        if v_id1 in self.domaines.keys() and v_id2 in self.domaines.keys(): #existence des variables ?
            verif = True
            for constr in liste:
                if not (constr[0] in self.domaines[v_id1] and  constr[1] in self.domaines[v_id2]): #valeur de variable valide?
                   #print (f"Incohérence au niveau de {constr}")
                   verif = False
                   break
            if verif:
                self.contraintes[v_id1].append(Contrainte(v_id2,liste))