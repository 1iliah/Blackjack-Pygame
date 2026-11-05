import random

cartes = [

    # Piques
    ("As", "Pique", [1, 11]),
    ("2", "Pique", 2),
    ("3", "Pique", 3),
    ("4", "Pique", 4),
    ("5", "Pique", 5),
    ("6", "Pique", 6),
    ("7", "Pique", 7),
    ("8", "Pique", 8),
    ("9", "Pique", 9),
    ("10", "Pique", 10),
    ("valet", "Pique", 10),
    ("dame", "Pique", 10),
    ("roi", "Pique", 10),

    # Coeur
    ("As", "coeur", [1, 11]),
    ("2", "coeur", 2),
    ("3", "coeur", 3),
    ("4", "coeur", 4),
    ("5", "coeur", 5),
    ("6", "coeur", 6),
    ("7", "coeur", 7),
    ("8", "coeur", 8),
    ("9", "coeur", 9),
    ("10", "coeur", 10),
    ("valet", "coeur", 10),
    ("dame", "coeur", 10),
    ("roi", "coeur", 10),

    # Carreau
    ("As", "carreau", [1, 11]),
    ("2", "carreau", 2),
    ("3", "carreau", 3),
    ("4", "carreau", 4),
    ("5", "carreau", 5),
    ("6", "carreau", 6),
    ("7", "carreau", 7),
    ("8", "carreau", 8),
    ("9", "carreau", 9),
    ("10", "carreau", 10),
    ("valet", "carreau", 10),
    ("dame", "carreau", 10),
    ("roi", "carreau", 10),

    # Trèfle
    ("As", "Trèfle", [1, 11]),
    ("2", "Trèfle", 2),
    ("3", "Trèfle", 3),
    ("4", "Trèfle", 4),
    ("5", "Trèfle", 5),
    ("6", "Trèfle", 6),
    ("7", "Trèfle", 7),
    ("8", "Trèfle", 8),
    ("9", "Trèfle", 9),
    ("10", "Trèfle", 10),
    ("valet", "Trèfle", 10),
    ("dame", "Trèfle", 10),
    ("roi", "Trèfle", 10)
]


def creer_paquet():

    paquet = cartes.copy()

    random.shuffle(paquet)

    return paquet
    print("ton total reste :",total )
    break
  else :
      print("appuie sur t pour tirer une autre carte ou n pour laisser")
      
