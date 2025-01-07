import random
from question import Question

class QCM:
    def __init__(self, questions):
        """
        Initialise un QCM avec une liste de questions.
        
        :param questions: Liste d'instances de Question.
        """
        self.questions = questions
        self.score = 0
        self.responses = []

    def shuffle_questions(self):
        """Mélange les questions dans un ordre aléatoire."""
        random.shuffle(self.questions)

    def ask_questions(self):
        """Pose les questions à l'utilisateur."""
        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i + 1}: {question.text}")
            for j, choice in enumerate(question.choices):
                print(f"  {'abc'[j]}) {choice}")
            
            user_answer = input("Votre réponse (a, b, c) : ").strip().lower()
            while user_answer not in ['a', 'b', 'c']:
                user_answer = input("Veuillez choisir a, b ou c : ").strip().lower()

            correct = question.is_correct(user_answer)
            self.responses.append((question, correct))
            if correct:
                self.score += 1

    def show_results(self):
        """Affiche le score final et le corrigé."""
        print("\n--- Résultats ---")
        print(f"Score final : {self.score} / {len(self.questions)}\n")
        print("Corrigé :")
        for i, (question, correct) in enumerate(self.responses):
            correct_answer = question.choices[question.correct_choice]
            print(f"Question {i + 1}: {question.text}")
            print(f"  Votre réponse : {'Correcte' if correct else 'Incorrecte'}")
            print(f"  Bonne réponse : {correct_answer}\n")
