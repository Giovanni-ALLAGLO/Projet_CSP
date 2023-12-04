import random as rd
from ..csp import Csp

def gen_csp(name , taille:int, nb_var:int , dur_constr, dense ):
    """Summary : Generation aléatoire de CSP (1 <= variable <= taille) .

    
       Arguments
       ---------
       name :
        Nom de la Csp
       taille : int
        Taille des domaines
       nb_var : int
         Nombre de variable
       dense : float
        Compris entre 0 et 1, densité de la Csp
       dur_constr : float
        Compris entre 0 et 1, dureté des contraintes entre variables
       """

    modele = Csp( name ,nb_var ,taille , dur_constr , dense)
    for var in range (1,nb_var+1):
        #taille des domaines fixé > ensemble domaine > ajout de variable au csp
        modele.ajoutVariable(var,list(range(taille)))

    #tout les couples (arcs) possibles
    arcs_possibles = [(x,y) for x in range(1,nb_var) for y in range(x+1,nb_var+1)]
    #calcul du nombre de liens(densité)
    nb_arcs  = int(dense*nb_var*(nb_var-1)/2)
    #choix aleatoire de nb_link couples aleatoire deux a deux distincts
    arcs_choisis = rd.sample( arcs_possibles,nb_arcs )

    # dureté > nombre de contraintes sur l'arc courant (couple)
    nb_constraintes = int((taille**2)*(1-dur_constr))
    for couple in arcs_choisis:
        # toute les valeurs couples possibles sur l'arc 'couple'
        valeursCouple_possibles = [(x,y) for x in modele.domaines[couple[0]] for y in modele.domaines[couple[1]]]
        # selection aleatoire de nb_const couples > ajout des contraintes
        valeursCouple_choisies = rd.sample( valeursCouple_possibles,nb_constraintes)
        modele.ajoutContrainte(couple[0],couple[1],valeursCouple_choisies)

    return modele
