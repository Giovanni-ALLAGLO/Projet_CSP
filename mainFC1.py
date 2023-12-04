#test FC sur csp n-reines
from sample.generateur.n_reines import csp_N_reine
from sample.traitement.forward_checking import fd_checking
import time

exemple =[5,15,21,25]
print("Traitement en cours...")
file = "solutionForwardCheck_1.txt"
with open(file, "w") as filout:
    
    filout.write("      ##Benchmark sur les solutions avec le forward_checking##")
    for i in exemple:
        filout.write("\n\n-------------------------------------------------------")
        csp_data= csp_N_reine(i)
        filout.write(f"\nResolution du csp suivant : {csp_data.name}\n")
        start = time.perf_counter()
        resultat = fd_checking(csp_data)
        end= time.perf_counter()
        filout.write("Probleme "+str(resultat[0])+f" : resolu en {end-start} secondes.\n")
        filout.write("solution : "+ str(resultat[1]))
print(f"Traitement terminé\nConsultez le fichier '{file}'")
n= input()