from math import sqrt

OEUIL = (150, 5, 90)

def distance(a, b):
    """calcule la distance entre le point a et b"""
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)

def fusion_points(L1: list, L2: list) -> list:
    """fusion du tri : essayer d'enlever les copies pour accelerer le schmilblick"""
    i1 = 0
    i2 = 0
    lst = []
    
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1][0] > L2[i2][0]:
            lst.append(L2[i2])
            i2 += 1
        else:
            lst.append(L1[i1])
            i1 += 1

    return lst + L1[i1:] + L2[i2:]

def tri_fusion_points(lst:list) -> list:
    """Trie les points par fusion (a ameliorer pour enlever les copies)"""
    if len(lst) == 1:
        return lst
    
    moitie = len(lst)//2
    
    return fusion_points(tri_fusion_points(lst[:moitie]), tri_fusion_points(lst[moitie:]))

def mettre_dans_l_ordre(points: list) -> list:
    """Trie les points du plus proche au plus loin."""
    # on mesure les distances
    lst = []
    for point in points:
        lst.append((distance(OEUIL, point), point))
    
    # On trie
    lst = tri_fusion_points(lst)

    # On enlève les distances pour laisser que les points
    res = []
    for point in lst:
        res.append(point[1])
    
    return res


def charger_donnee(nom_fichier: str) -> list:
    """Charge les données du fichier nom_fichier"""

    # On lit le fichier
    f = open(nom_fichier, "r")
    data_brut = f.read().split("\n")
    data = []
    for ligne in data_brut:
        j = ligne.split(", ")
        data.append((int(j[0]), int(j[1]), int(j[2])))
    
    # on les met dans l'ordre du plus loin au plus proches
    data = mettre_dans_l_ordre(data)
    print(data)
    
    return data

def bleu_vers_rouge(v: float) -> tuple:
    """
    Renvoie une couleur RGB allant du bleu (0) au rouge (100)
    """
    if v < 0: 
        v = 0
    if v > 100: 
        v = 100
    
    r = int((v / 100) * 255)
    g = 0
    b = int((1 - v / 100) * 255)
    
    return (r, g, b)

def calculer_pos_points(points: list) -> list:
    res = []
    for point in points:

        """
        L'équation de la droite qui va de l'oeuil jusqu'au point est:
        x = OEUIL[0] + (OEUIL[0]-point[0])*t       (1)
        y = OEUIL[1] + (OEUIL[1]-point[1])*t
        z = OEUIL[2] + (OEUIL[2]-point[2])*t
        
        Le plan a pour équation (on changera) :
        x = 100
        """

        #    Cherchons le point d'intersection de cette droite et du plan
        # Cherchons donc t avec x = 100
        t = (100 - OEUIL[0])/(OEUIL[0]-point[0])           # d'après (1)
        
        # Avec t on calcule y et z
        y = OEUIL[1] + (OEUIL[1]-point[1])*t
        z = OEUIL[2] + (OEUIL[2]-point[2])*t


        # Et on met une couleur en fonction de la hauteur
        couleur = bleu_vers_rouge(point[2])

        res.append((y, z, couleur))

    return res
