import csv
import time


def load_data(filename):
    """
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


ts = time.time()

filename = 'data/summer-olympics.csv'
data = load_data(filename)

year = '1984'
country = 'FRA'
nd_medals = calcul_nb_medailles(data, year, country)
print(year, country, nd_medals)

te = time.time()
print(f"done in {te - ts:.2f} s.")
