import random
import string

class PasswordGenerator:
    """Classe pour générer des mots de passe aléatoires."""
    
    @staticmethod
    def generate_password(lowercase_count, uppercase_count, digit_count, special_count):
        """
        Génère un mot de passe avec les critères donnés.
        """
        lowercase = random.choices(string.ascii_lowercase, k=lowercase_count)
        uppercase = random.choices(string.ascii_uppercase, k=uppercase_count)
        digits = random.choices(string.digits, k=digit_count)
        specials = random.choices("!@#$%^&*()-_=+<>?/|", k=special_count)
        
        # Mélanger les caractères pour plus de sécurité
        password = lowercase + uppercase + digits + specials
        random.shuffle(password)
        
        return ''.join(password)
