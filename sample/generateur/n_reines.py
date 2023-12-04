from ..csp import Csp

def csp_N_reine(N)->Csp:
    """
    Summary : Generateur de CSP pour le probleme des N-reines.
    """
    modele = Csp(f"{N}-reines" , N, N)
    for var in range (1,N+1):
        #taille des domaines fixé > ensemble domaine > ajout de variable au csp
        modele.ajoutVariable(var,list(range(1,N+1)))
    for id1 in range(1,N):
        for id2 in range(id1+1,N+1):
            liste = []
            for val in modele.domaines[id1]:
                for j in modele.domaines[id2]:
                    if j!=val and j!=(val+(id2-id1)) and j!=((val-(id2-id1))):
                        liste.append((val,j))
            modele.ajoutContrainte(id1,id2,liste)
    modele.densite=1
    modele.durete_contrainte= 0.5
    return modele