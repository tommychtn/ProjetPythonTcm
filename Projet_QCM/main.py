#########################################################################
##  main.py
#########################################################################

#########################################################################
##  IMPORT
#########################################################################

from Projet_QCM.qcm import QCM
from Projet_QCM.question import Question

#########################################################################
##  FONCTION MAIN
#########################################################################

def main():

    # Création des questions
    questions = [
        Question("Quelle est la capitale de la France ?", ["Paris", "Lyon", "Marseille"], 0),
        Question("Combien font 2 + 2 ?", ["3", "4", "5"], 1),
        Question("Quelle est la couleur du ciel ?", ["Bleu", "Vert", "Rouge"], 0),
    ]
    
    # Initialisation du QCM
    qcm = QCM(questions)
    qcm.shuffle_questions()
    qcm.ask_questions()
    qcm.show_results()

if __name__ == "__main__":
    main()

#########################################################################
##  FIN main.py
#########################################################################
