class Question:
    def __init__(self, text, choices, correct_choice):
        """
        Initialise une question.
        
        :param text: Texte de la question.
        :param choices: Liste des trois choix de réponse.
        :param correct_choice: Indice de la bonne réponse (0, 1 ou 2).
        """
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    def is_correct(self, user_choice):
        """
        Vérifie si le choix de l'utilisateur est correct.
        
        :param user_choice: Indice choisi par l'utilisateur (a, b ou c).
        :return: True si correct, sinon False.
        """
        return user_choice.lower() in ['a', 'b', 'c'] and \
               self.choices['abc'.index(user_choice.lower())] == self.choices[self.correct_choice]
