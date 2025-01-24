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
        Question("Combien font 1 + 1 ?", ["1", "2", "3"], 1),
        Question("Combien font 5 - 2 ?", ["3", "2", "4"], 0),
        Question("Combien font 3 x 3 ?", ["6", "9", "12"], 1),
        Question("Combien font 10 ÷ 2 ?", ["4", "5", "6"], 1),
        Question("Combien font 7 + 3 ?", ["9", "10", "11"], 1),
        Question("Combien font 12 - 4 ?", ["8", "7", "9"], 0),
        Question("Combien font 6 x 2 ?", ["12", "14", "10"], 0),
        Question("Combien font 15 ÷ 3 ?", ["4", "5", "6"], 1),
        Question("Combien font 8 + 2 x 3 ?", ["30", "14", "10"], 1),
        Question("Combien font 9 - 3 + 1 ?", ["5", "7", "6"], 2),
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
