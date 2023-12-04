# test FC sur random csp
from sample.generateur.genRandom_csp import gen_csp
from sample.traitement.forward_checking import fd_checking
import time

csp1 = gen_csp("Randomcsp_1",10,7,0.3,0.7)
csp2 = gen_csp("Randomcsp_2",12,21,0.2,0.8)
csp3 = gen_csp("Randomcsp_3",17,23,0.2,0.8)
csp4 = gen_csp("Randomcsp_4",16,32,0.1,0.6)
exemple = [csp1,csp2,csp3,csp4]

print("Traitement en cours...")
file = "solutionForwardCheck_2.txt"
with open(file, "w") as filout:    
    filout.write("      ##Benchmark sur les solutions avec le forward_checking##")
    for csp_data in exemple:
        filout.write("\n\n-------------------------------------------------------")
        filout.write(f"\nResolution du csp suivant : {csp_data.name}\n")
        start = time.perf_counter()
        resultat = fd_checking(csp_data)
        end= time.perf_counter()
        filout.write("Probleme "+str(resultat[0])+f" : resolu en {end-start} secondes.\n")
        filout.write("solution : "+ str(resultat[1]))
print(f"Traitement terminé\nConsultez le fichier '{file}'")
n= input()