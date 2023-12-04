from sample.generateur.genRandom_csp import gen_csp
from sample.traitement.backjumping import backjumping
from sample.traitement.utilsFonctions import find_parents
import time


csp1 = gen_csp("Randomcsp_1",10,7,0.3,0.7)
csp2 = gen_csp("Randomcsp_2",12,21,0.2,0.8)
csp3 = gen_csp("Randomcsp_3",17,23,0.2,0.8)
csp4 = gen_csp("Randomcsp_4",8,32,0.1,0.6)
exemple = [csp1,csp2,csp3,csp4]

print("Traitement en cours...")
file = "solutionBackjump_2.txt"
with open(file, "w") as filout:

    filout.write("      ##Benchmark sur l'espace solution avec le backjumping ##")
    for csp_data in exemple:
        filout.write("\n\n-------------------------------------------------------")
        parent = find_parents(csp_data) 
        filout.write(f"\nResolution du csp suivant : {csp_data.name}\n")
        start = time.perf_counter()
        resultat = backjumping(csp_data,parent)
        end= time.perf_counter()
        filout.write("Probleme "+str(resultat[0])+f" : resolu en {end-start} secondes.\n")
        filout.write("solution : "+ str(resultat[1]))
print(f"Traitement terminé\nConsultez le fichier '{file}'")
n= input()