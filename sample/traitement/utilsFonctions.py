#fonctions utilitaires

def affich_csp(csp):
    """Summary : Fonction d'affichage de CSP ."""
    print(f"Cette struture de donnée est une csp \nNom : {csp.name} \nNombre de variables : {csp.nb_var} \nTaille des domaines : {csp.nb_valeur} \nDensité : {csp.densite} \nDureté des contraintes : {csp.durete_contrainte}\n")
    print("Domaines de définition")
    for id in range(1,csp.nb_var+1):
        print(f"Domaine de la variable {id} : {csp.domaines[id]}")
    print("\nEnsemble des contraintes")
    for id in range(1,csp.nb_var+1):
        for c in csp.contraintes[id]:
            print(f"Contrainte binaire C_{id}{c.v_destination} : {c.l_couple}")


def consistent_assignment(csp_contraintes,listeAssignment,X):
    """Summary : Verifiant la consistence de x en fonction de valeur des varibles presentes dans liste.

    Arguments
    =========
    csp_contraintes : dict
        Dictionnaires des contraintes du csp.
    listeAssignment : list
        Liste des valeurs coherentes (déjà trouvées) de sorte que variable id=i à la valeur liste[i-1].
    X : int
        Candidat potentiel pour assignation de la variable id= len(liste).

    Return
    ======
    (boolean)
        True si x est une assignation coherente.
        False sinon .
    """
    taille_listeAssignment = len(listeAssignment)
    X_id = taille_listeAssignment+1 # id de la variable de x
    if taille_listeAssignment == 0: #assignation de la première variable id =1
        for constr in csp_contraintes[X_id]:
            for c in constr.l_couple:
                if X == c[0]:
                    return True
        if len(csp_contraintes[X_id])==0: # variable independante?
            return True
        return False
    else:
        for i in range(taille_listeAssignment):
            for constr in csp_contraintes[i+1]:
                if constr.v_destination == X_id and not((listeAssignment[i],X) in constr.l_couple):
                    return False
        return True

def revise(csp_contraintes,id,x,k):
    """Summary : Verifiant la consistence de x en fonction du fait qu'il soit toujours possible ou non de trouver une solution.
                Cela se traduit par le fait que les domaines revisés soit non vides.

    Arguments
    ---------
    csp_contraintes : dict
        Dictionnaires des contraintes du csp.
    id : int
        variable en cours d'assignation
    x : int
        Candidat potentiel pour assignation de la variable id.
    k : int
        variable dont le domaine sera revisé en fonction des contraintes le liant à id

    Return
    ------
    (list)
        list du domaine revisé de la variable k en propageant les contraintes de la variable id
    """
    tmp_liste = None
    for val in csp_contraintes[id]:
        if val.v_destination == k:
            tmp_liste = [c[1] for c in val.l_couple if c[0]==x]
    return tmp_liste

def find_parents(csp):
    """Summary : Fournit les parents de chaque variable selon la structure du graphe.
                Convention -: Les parents ont toujours un id inférieur aux fils.

    Arguments
    =========
    csp : Csp

    Return
    ======
    (dict)
        la liste de parents de chaque variable-clé v .
    """
    parents = dict()
    for id in (csp.contraintes).keys():
        parents[id]=[]
    for id,value in (csp.contraintes).items():
        for constr in value:
            tmp = len(csp.domaines[id])*len(csp.domaines[constr.v_destination])
            if len(constr.l_couple)== tmp:
                break
            else:
                parents[constr.v_destination].append(id)
    for id,value in parents.items():
        if len(value)==0:
            parents[id]=[0]
    return parents
