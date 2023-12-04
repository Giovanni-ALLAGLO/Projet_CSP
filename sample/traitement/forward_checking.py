from .utilsFonctions import revise
import copy

def fd_checking(csp):
    """Summary : Determine si le csp est Satisfiable ou non.

    Arguments
    =========
    csp : Csp

    Return
    ======
    (tuple)
        La reponse ("UNSAT",None) ou ("SAT",first solution)
    """
    alpha= None
    current_id =1
    domain_list = (csp.nb_var+2)*[None]
    domain_list [1] = copy.deepcopy(csp.domaines)
    liste = []
    while(current_id<=csp.nb_var and current_id>=1):
        verrou = False
        while not(verrou) and len(domain_list[current_id][current_id])!=0:
            alpha = domain_list[current_id][current_id].pop()
            is_emptyDomain = False
            tmp_domain = copy.deepcopy(domain_list[current_id])
            for k in range(current_id+1,csp.nb_var+1):
                revise_list = revise(csp.contraintes,current_id,alpha,k)
                if revise_list!= None: #Aucune contrainte
                    tmp_domain[k]= [ i for i in domain_list[current_id][k] if i in revise(csp.contraintes,current_id,alpha,k)]
                if len(tmp_domain[k])==0:
                    is_emptyDomain = True
                    break
            if not(is_emptyDomain):
                domain_list[current_id+1]=tmp_domain
                verrou = True

        if not(verrou):
            current_id-=1
            if current_id == 0:
                return "UNSAT",None
            liste.pop()
        else:
            liste.append(alpha)
            current_id+=1

    return "SAT",liste

def fd_checking_allsolution(csp):
    """Summary :    Determine le nombre de solution .

       Arguments
       ---------
       csp : Csp

       Return
       ------
       (tuple)
            (nombre de solution,liste de solution)
    """
    counter = 0
    liste_s = []
    current_id =1
    alpha= None
    domain_list = (csp.nb_var+2)*[None]
    domain_list [1] = copy.deepcopy(csp.domaines)
    liste = []
    while(current_id<=csp.nb_var and current_id>=1):
        counter+=1
        verrou = False
        while not(verrou) and len(domain_list[current_id][current_id])!=0:
            alpha = domain_list[current_id][current_id].pop()
            is_emptyDomain = False
            tmp_domain = copy.deepcopy(domain_list[current_id])
            for k in range(current_id+1,csp.nb_var+1):
                revise_list = revise(csp.contraintes,current_id,alpha,k)
                if revise_list!= None: # non-aucune contrainte?
                    tmp_domain[k]= [ i for i in domain_list[current_id][k] if i in revise(csp.contraintes,current_id,alpha,k)]
                if len(tmp_domain[k])==0:
                    is_emptyDomain = True
                    break
            if not(is_emptyDomain):
                domain_list[current_id+1]=tmp_domain
                verrou = True
        if not(verrou):
            current_id-=1
            if current_id == 0:
                t=len(liste_s)
                if t==0:
                    #print("tour de boucle : ",counter)
                    return (0,[])
                else:
                    return(t,liste_s)
            liste.pop()
        else:
            liste.append(alpha)
            current_id+=1
            if current_id>csp.nb_var:
                #print("tour de boucle : ",counter)
                current_id-=1
                liste_s.append(liste[:])
                liste.pop()
    return -1   #Error