from sample.generateur.n_reines import csp_N_reine
from sample.traitement.backjumping import backjumping
from sample.traitement.utilsFonctions import find_parents
import time

exemple =[5,15,21,25]
print("Traitement en cours...")
file = "solutionBackjump_1.txt"
with open(file, "w") as filout:
    filout.write("      ##Benchmark sur les solutions avec le backjumping##")
    for i in exemple:
        filout.write("\n\n-------------------------------------------------------")
        csp_data= csp_N_reine(i)
        parent = find_parents(csp_data) 
        filout.write(f"\nResolution du csp suivant : {csp_data.name}\n")
        start = time.perf_counter()
        resultat = backjumping(csp_data,parent)
        end= time.perf_counter()
        filout.write("Probleme "+str(resultat[0])+f" : resolu en {end-start} secondes.\n")
        filout.write("solution : "+ str(resultat[1]))
print(f"Traitement terminé\nConsultez le fichier '{file}'")
n= input()