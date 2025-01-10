import math

class PasswordTester:
    """Classe pour tester la force d'un mot de passe."""
    
    @staticmethod
    def calculate_entropy(password):
        """
        Calcule l'entropie d'un mot de passe selon sa longueur et ses caractères.
        """
        charset_size = 0
        if any(c.islower() for c in password):
            charset_size += 26
        if any(c.isupper() for c in password):
            charset_size += 26
        if any(c.isdigit() for c in password):
            charset_size += 10
        if any(c in "!@#$%^&*()-_=+<>?/|" for c in password):
            charset_size += len("!@#$%^&*()-_=+<>?/|")
        
        entropy = len(password) * math.log2(charset_size)
        return entropy

    @staticmethod
    def evaluate_strength(entropy):
        """
        Évalue la force d'un mot de passe selon son entropie.
        """
        if entropy < 28:
            return "Faible"
        elif 28 <= entropy < 36:
            return "Moyenne"
        elif 36 <= entropy < 60:
            return "Forte"
        else:
            return "Très forte"
