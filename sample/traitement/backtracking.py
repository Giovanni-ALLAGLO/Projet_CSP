#__author__      = "AG"
from .utilsFonctions import consistent_assignment


def backtracking(csp):
    """Summary : Determine si le csp est Satisfiable ou non.

    Arguments
    =========
    csp : Csp

    Return
    ======
    (tuple)
        La reponse ("UNSAT",None) ou ("SAT",first solution)
    """
    counter = 0
    alpha= None
    current_id = 1
    domain_list= dict()
    for i in range(1,len(csp.domaines)+1):
        domain_list[i]= (csp.domaines[i])[:]
    liste = []
    while(current_id<=csp.nb_var and current_id>=1):
        counter+=1
        verrou = False
        while not(verrou) and len(domain_list[current_id])!=0:
            alpha = domain_list[current_id].pop()
            verrou = consistent_assignment(csp.contraintes,liste,alpha)
        if not(verrou):
            domain_list[current_id] = (csp.domaines[current_id])[:]
            current_id-=1
            if current_id == 0: # or if len(liste)==0:
                return "UNSAT",None
            liste.pop()
        else:
            liste.append(alpha)
            current_id+= 1

    return "SAT",liste


def backtracking_allsolution(csp):
    """Summary :    Determine le nombre de solution .

       Arguments
       ---------
       csp : Csp

       Return
       ------
       (tuple)
            (nombre de solution,liste de solution)
    """
    counter =0
    liste_s = []
    alpha= None
    current_id =1
    domain_list= dict()
    for i in range(1,len(csp.domaines)+1):
        domain_list[i]= (csp.domaines[i])[:]
    liste = []
    while(current_id<=csp.nb_var and current_id>=1):
        counter+=1
        verrou = False
        while not(verrou) and len(domain_list[current_id])!=0:
            alpha = domain_list[current_id].pop()
            verrou = consistent_assignment(csp.contraintes,liste,alpha)
        if not(verrou):
            domain_list[current_id] = (csp.domaines[current_id])[:]
            current_id-=1
            if current_id == 0:
                t=len(liste_s)
                if t==0:
                    return (0,[])
                else:
                    return(t,liste_s)
            liste.pop()
        else:
            liste.append(alpha)
            current_id+=1
            if current_id>csp.nb_var:
                liste_s.append(liste[:])
                current_id-=1
                liste.pop()
    return -1 # error