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
        Question("De quel pays est originaire la célèbre saucisse 'Bratwurst' ?", ["Allemagne", "Pologne", "Autriche"], 0),
        Question("Quelle est la principale viande utilisée dans les saucisses de Francfort ?", ["Porc", "Bœuf", "Poulet"], 0),
        Question("Comment appelle-t-on une saucisse sèche typique d'Espagne ?", ["Chorizo", "Salami", "Saucisson"], 0),
        Question("Quel ingrédient est typiquement ajouté à une saucisse de Toulouse ?", ["Sel", "Herbes de Provence", "Ail"], 2),
        Question("Dans quel plat britannique trouve-t-on des saucisses et de la purée ?", ["Bangers and Mash", "Shepherd's Pie", "Fish and Chips"], 0),
        Question("Quelle saucisse est utilisée dans un 'Hot Dog' classique ?", ["Frankfurter", "Andouillette", "Merguez"], 0),
        Question("La 'saucisse de Morteau' est une spécialité de quelle région française ?", ["Bourgogne", "Franche-Comté", "Alsace"], 1),
        Question("Quel est le nom de la saucisse italienne souvent assaisonnée de fenouil ?", ["Salami", "Salsiccia", "Pancetta"], 1),
        Question("Quelle est la particularité des saucisses 'vegan' ?", ["Elles sont faites de tofu", "Elles contiennent du poisson", "Elles n'ont pas de boyaux"], 0),
        Question("Dans quel pays trouve-t-on la 'Boerewors', une saucisse traditionnelle ?", ["Afrique du Sud", "Australie", "Argentine"], 0),
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
