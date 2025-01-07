#########################################################################
##  main.py
#########################################################################

#########################################################################
##  IMPORT
#########################################################################

from qcm import QCM
from question import Question

#########################################################################
##  FONCTION MAIN
#########################################################################

def main():

    print("\n#########################################")
    print("##")
    print("##   QUESTION QCM")        
    print("##")
    print("#########################################\n")

    # Creation des questions
    questions = [
        Question("Quelle est la capitale de la France ?", ["Paris", "Lyon", "Marseille"], 0),
        Question("Combien font 2 + 2 ?", ["3", "4", "5"], 1),
        Question("Quelle est la couleur du ciel ?", ["Bleu", "Vert", "Rouge"], 0),
    ]
    
    # Initialisation du QCM
    qcm = QCM(questions)
    qcm.ordre_questions()
    qcm.demande_questions()
    qcm.Resultats()

if __name__ == "__main__":
    main()

#########################################################################
##  FIN main.py
#########################################################################
