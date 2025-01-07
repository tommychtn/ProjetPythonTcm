#########################################################################
##  question.py
#########################################################################

#########################################################################
##  CLASS
#########################################################################

class Question:

    ## initialise la question
    def __init__(self, text, choices, correct_choice):
        self.text = text
        self.choices = choices
        self.correct_choice = correct_choice

    ## verifie si le choix est une bonne reponse ou non 
    def is_correct(self, user_choice):
        return user_choice.lower() in ['a', 'b', 'c'] and \
               self.choices['abc'.index(user_choice.lower())] == self.choices[self.correct_choice]

#########################################################################
##  FIN question.py
#########################################################################