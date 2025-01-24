#########################################################################
##  main.py
#########################################################################

#########################################################################
##  IMPORT
#########################################################################

from GenerateurMDP import PasswordGenerator
from passphrase import PassphraseGenerator

#########################################################################
##  FONCTION MAIN
#########################################################################

def main():
    print("\nGENERATEUR DE MOT DE PASSE !!!")
    
    while True:
        print("\n1. Générer un mot de passe")
        print("2. Générer une passphrase")
        print("3. Quitter")
        
        choice = input("Choisissez une option : ")
        
        # MDP Aleatoires
        if choice == "1":
            # Demander les criteres du mot de passe
            lc = int(input("Nombre de lettres minuscules : "))
            uc = int(input("Nombre de lettres majuscules : "))
            digits = int(input("Nombre de chiffres : "))
            specials = int(input("Nombre de caracteres specials : "))
            
            password = PasswordGenerator.generate_password(lc, uc, digits, specials)
            
            print(f"Mot de passe generé : {password}")

        # Passphrase
        elif choice == "2":
            word_count = int(input("Nombre de mots dans la passphrase : "))
            passphrase = PassphraseGenerator.generate_passphrase(word_count)
            print(f"Passphrase générée : {passphrase}")
        
        # Sortie du script
        elif choice == "3":
            print("FIN")
            break
        else:
            print("ERREUR")

if __name__ == "__main__":
    main()


#########################################################################
##  FIN main.py
#########################################################################