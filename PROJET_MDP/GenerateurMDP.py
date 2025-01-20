#########################################################################
##  generateurMDP.py
#########################################################################

#########################################################################
##  IMPORT
#########################################################################

import random
import string

#########################################################################
##  CLASS
#########################################################################

# Generation des MDP aleatoires
class PasswordGenerator:

    @staticmethod
    def generate_password(lowercase_count, uppercase_count, digit_count, special_count):

        # COndition / Criteres du MDP
        lowercase = random.choices(string.ascii_lowercase, k=lowercase_count)
        uppercase = random.choices(string.ascii_uppercase, k=uppercase_count)
        digits = random.choices(string.digits, k=digit_count)
        specials = random.choices("!@#$%^&*()-_=+<>?/|", k=special_count)
        
        # Chnage l'ordre d'apparition des caracteres
        password = lowercase + uppercase + digits + specials
        random.shuffle(password)
        
        return ''.join(password)

#########################################################################
##  FIN generateurMDP.py
#########################################################################