import csv
import time


def load_data(filename):
    """
    charge les données olympiques
    """
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)

    n_items = len(data)
    print(f"{filename} loaded into data ({n_items} items)")

    return data


def calcul_nb_medailles(data, year, country):
    """
    Calcul le nb de médailles d'Or gagné 
    par un pays donné `country` 
    lors d'une olympiade donnée `year`
    """
    selection = []
    for e in data:
        if e['Year'] == year and e['Country'] == country and e['Medal'] == 'Gold':
            selection.append(e)
    reponse = len(selection)
    
    return reponse



def trouve_liste_medailles_or_2012(data):
# Effectuer une première sélection “liste_gold_2012” 
# pour ne retenir que les médailles d’Or 2012
# on passe de 31k items à 636 items

    # Suggestion snippet Izak 
    liste_medailles_or = []
    for md in data:
        if md["Year"] == '2012' and md["Medal"] == "Gold":
            liste_medailles_or.append(md)
    return liste_medailles_or


def trouve_liste_pays(liste_resulats):    
# Ensuite, à partir de la première sélection, 
# rechercher tous les pays présent et ajouter 
# cela dans la liste “liste_pays”
    liste_pays = []
    for e in liste_resulats:
        if e["Country"] not in liste_pays:
            liste_pays.append(e["Country"])
    return liste_pays
    
    
# Programme principal
ts = time.time()


year = '2012'
filename = 'data/summer-olympics.csv'
data = load_data(filename)

liste_medailles_or = trouve_liste_medailles_or_2012(data)

# liste_pays = trouve_liste_pays(liste_medailles_or)
liste_pays = trouve_liste_pays(data)

liste_pays_unique = set(liste_pays)

for pays in liste_pays_unique:
    n = calcul_nb_medailles(liste_medailles_or, year, pays)
    print(year, pays, n)

te = time.time()
print(f"done in {te - ts:.2f} s.")
