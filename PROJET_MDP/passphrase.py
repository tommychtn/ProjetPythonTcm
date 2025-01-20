#########################################################################
##  passphrase.py
#########################################################################

#########################################################################
##  IMPORT
#########################################################################

import random
import os

#########################################################################
##  CLASS
#########################################################################

## Genere une passphrase
class PassphraseGenerator:
    
    @staticmethod
    def generate_passphrase(word_count):
        """
        Génère une passphrase à partir d'une liste de mots.
        """
        # Construire un chemin relatif basé sur le fichier actuel
        file_path = os.path.join(os.path.dirname(__file__), "eff_large_wordlist.txt")
        
        # Vérifier si le fichier existe
        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"Le fichier '{file_path}' est introuvable. Assurez-vous qu'il est dans le répertoire correct."
            )
        
        with open(file_path, "r") as f:
            words = [line.strip().split()[1] for line in f if line.strip()]
        
        passphrase = random.sample(words, word_count)
        return ' '.join(passphrase)

#########################################################################
##  passphrase.py
#########################################################################