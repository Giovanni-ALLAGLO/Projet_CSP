from .utilsFonctions import consistent_assignment
import copy

def backjumping(csp,parents):
    '''Summary : Determine si le csp est Satisfiable ou non

       Arguments
       ---------
       csp : Csp
       parents: dict

       Return
       ------
       (tuple)
            ("UNSAT",None) ou ("SAT",first solution)
    '''
    alpha= None
    current_id =1
    domain_list = copy.deepcopy(csp.domaines)
    parents_list = copy.deepcopy(parents)
    liste = []
    while(current_id<=csp.nb_var and current_id>=1):
        verrou = False
        while not(verrou) and len(domain_list[current_id])!=0:
            alpha = domain_list[current_id].pop()
            verrou = consistent_assignment(csp.contraintes,liste,alpha)
        if not(verrou):
            current_id, previous_current_id = max(parents_list[current_id]),current_id
            if current_id == 0:
                return "UNSAT",None
            i_extract = previous_current_id - current_id
            liste = liste[:-i_extract]
            parents_list[current_id]=list(set(parents_list[current_id]+[i for i in parents_list[previous_current_id] if i!=current_id]))
            for i in range(current_id+1,previous_current_id+1):
                domain_list[i] = (csp.domaines[i])[:]

        else:
            liste.append(alpha)
            current_id+=1
            if current_id<=csp.nb_var:
                parents_list[current_id] = parents[current_id][:]
    return "SAT",liste

def backjumping_allsolution(csp,parents):
    '''Summary : Determine l'ensemble solution

       Arguments
       ---------
       csp : Csp
       parents: dict

       Return
       ------
       (tuple)
            (nombre de solution,liste de solution)
    '''
    counter =0
    liste_s=[]
    current_id =1
    alpha= None
    domain_list = copy.deepcopy(csp.domaines)
    parents_list = copy.deepcopy(parents)
    liste = []
    print("Search starts...\n")
    while(current_id<=csp.nb_var and current_id>=1):
        counter+=1
        verrou = False
        while not(verrou) and len(domain_list[current_id])!=0:
            alpha = domain_list[current_id].pop()
            verrou = consistent_assignment(csp.contraintes,liste,alpha)
        #print(f"    Current iteration : choix de la variable id={current_id}")
        if not(verrou):
            current_id, previous_current_id = max(parents_list[current_id]),current_id
            if current_id == 0:
                t=len(liste_s)
                if t==0:
                    #print("tour de boucle : ",counter)
                    return (0,[])
                else:
                    return(t,liste_s)
            i_extract = previous_current_id - current_id
            liste = liste[:-i_extract]
            parents_list[current_id]=list(set(parents_list[current_id]+[i for i in parents_list[previous_current_id] if i!=current_id]))
            #print(f"\t<--Backjumping: choix de la variable id={current_id}\n")
        else:
            liste.append(alpha)
            #print("\tSolution search: in progress ...")
            current_id+=1
            if current_id<=csp.nb_var:
                domain_list[current_id] = (csp.domaines[current_id])[:]
                parents_list[current_id] = parents[current_id][:]
            if current_id>csp.nb_var:
                #print("tour de boucle : ",counter)
                liste_s.append(liste[:])
                current_id-=1
                liste.pop()
    return -1 # Error
