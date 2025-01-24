#########################################################################
##  qcm.py
#########################################################################

#########################################################################
##  IMPORT
#########################################################################

import random
from question import Question

#########################################################################
##  CLASS
#########################################################################

class QCM:

    # initialisation du QCM avec une liste dse questions
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.responses = []

    # melange l'ordre des questions
    def ordre_questions(self):
        random.shuffle(self.questions)

    # pose les questions à l'user
    def demande_questions(self):
        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i + 1}: {question.text}")
            for j, choice in enumerate(question.choices):
                print(f"  {'abc'[j]}) {choice}")
            
            user_answer = input("Choisir entre la reponse (a, b, c) : ").strip().lower()
            while user_answer not in ['a', 'b', 'c']:
                user_answer = input("Choisir entre la reponse a, b ou c : ").strip().lower()

            correct = question.is_correct(user_answer)
            self.responses.append((question, correct))
            if correct:
                self.score += 1

    # affiche le score et la correction
    def Resultats(self):
        print("\n\n#########################################")
        print("##")
        print("## Résultats")
        print("##")
        print("#########################################")

        print(f"\nScore final : {self.score} / {len(self.questions)}\n")

        print("#########################################")
        print("##")
        print("## Correction")        
        print("##")
        print("#########################################\n")

        for i, (question, correct) in enumerate(self.responses):
            correct_answer = question.choices[question.correct_choice]
            print(f"Question {i + 1}: {question.text}")
            print(f"  Votre reponse : {'VRAI ✅' if correct else 'FAUX ❌'}")
            print(f"  Bonne reponse : {correct_answer}\n")


#########################################################################
##  FIN qcm.py
#########################################################################