from password_generator import PasswordGenerator
from password_tester import PasswordTester
from passphrase_generator import PassphraseGenerator

def main():
    print("=== Générateur et Testeur de mots de passe ===")
    
    while True:
        print("\n1. Générer un mot de passe")
        print("2. Tester la force d'un mot de passe")
        print("3. Générer une passphrase")
        print("4. Quitter")
        
        choice = input("Choisissez une option : ")
        
        if choice == "1":
            # Demander les critères du mot de passe
            lc = int(input("Nombre de lettres minuscules : "))
            uc = int(input("Nombre de lettres majuscules : "))
            digits = int(input("Nombre de chiffres : "))
            specials = int(input("Nombre de caractères spéciaux : "))
            
            password = PasswordGenerator.generate_password(lc, uc, digits, specials)
            entropy = PasswordTester.calculate_entropy(password)
            strength = PasswordTester.evaluate_strength(entropy)
            
            print(f"Mot de passe généré : {password}")
            print(f"Entropie : {entropy:.2f} bits - Force : {strength}")
        
        elif choice == "2":
            password = input("Entrez un mot de passe à tester : ")
            entropy = PasswordTester.calculate_entropy(password)
            strength = PasswordTester.evaluate_strength(entropy)
            
            print(f"Entropie : {entropy:.2f} bits - Force : {strength}")
        
        elif choice == "3":
            word_count = int(input("Nombre de mots dans la passphrase : "))
            passphrase = PassphraseGenerator.generate_passphrase(word_count)
            print(f"Passphrase générée : {passphrase}")
        
        elif choice == "4":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Réessayez.")

if __name__ == "__main__":
    main()
