import random

class PassphraseGenerator:
    """Classe pour générer une passphrase sécurisée."""
    
    @staticmethod
    def generate_passphrase(word_count):
        """
        Génère une passphrase à partir d'une liste de mots.
        """
        with open("eff_large_wordlist.txt", "r") as f:
            words = [line.strip().split()[1] for line in f if line.strip()]
        
        passphrase = random.sample(words, word_count)
        return ' '.join(passphrase)
