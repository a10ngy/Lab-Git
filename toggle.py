def toggle(value):
    """
    Fonction qui bascule la valeur booléenne donnée.

    Paramètres :
        value (bool) : La valeur à basculer (True ou False)

    Retour :
        bool : La valeur opposée
    """
    if isinstance(value, bool):
        return not value
    else:
        raise TypeError("Erreur : La valeur doit être de type booléen (True ou False).")


# ------------------------------------------------------------
# Exemple d'utilisation
# ------------------------------------------------------------
if __name__ == "__main__":
    # Valeur initiale
    etat = False
    print("État initial :", etat)

    # Première bascule
    etat = toggle(etat)
    print("Nouvel état :", etat)

    # Deuxième bascule
    etat = toggle(etat)
    print("État après une deuxième bascule :", etat)

    # Test d’erreur (à commenter si inutile)
    # toggle("True")  # Exemple d’erreur volontaire : non booléen