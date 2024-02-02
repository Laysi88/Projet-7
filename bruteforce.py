import csv
import time

strart_time = time.time()  # Enregistrez le temps de début
# Charger les données depuis le CSV
with open("data/data_bruteforce.csv", "r", newline="", encoding="utf-8") as file:
    csv_reader = csv.reader(file, delimiter=";")
    headers = next(csv_reader)  # Récupérer les en-têtes
    headers = [header.strip() for header in headers]  # Supprimer les espaces autour des noms de colonnes
    headers[0] = headers[0].lstrip("\ufeff")  # Supprimer le caractère spécial '\ufeff' devant "name"

    data_lines = list(csv_reader)

# Convertir les données en une liste de dictionnaires
data = []
for line in data_lines:
    data.append({headers[i]: line[i] for i in range(len(line))})

# Initialiser les variables
max_profit = 0
selected_actions = []
total_price = 0  # Initialiser le prix total ici

# Générer toutes les combinaisons possibles d'actions
num_actions = len(data)
for i in range(2**num_actions):
    binary_representation = bin(i)[2:].zfill(num_actions)
    combination = [data[j] for j in range(num_actions) if binary_representation[j] == "1"]

    current_price = sum(int(combination[j]["price"]) for j in range(len(combination)))

    # Vérifier si la combinaison respecte la contrainte de prix
    if current_price <= 500:
        total_profit = sum(
            float(combination[j]["profit"]) * int(combination[j]["price"]) / 100 for j in range(len(combination))
        )

        # Mettre à jour la solution optimale si le profit est plus élevé
        if total_profit > max_profit:
            # Utiliser les indices au lieu des noms de colonnes
            selected_actions = [action["name"] for action in combination]
            max_profit = total_profit  # Mettre à jour le profit maximal
            total_price = current_price  # Mettre à jour le prix total

end_time = time.time()  # Enregistrez le temps de fin
execution_time = end_time - strart_time  # Calculez le temps d'exécution

# Afficher les résultats
print("Prix total :", total_price)
print("Actions sélectionnées :", selected_actions)
print("Profit maximal :", round(max_profit, 2))  # Arrondir le profit à deux décimales
print("Temps d'exécution :", round(execution_time, 5), "secondes")  # Arrondir le temps d'exécution à cinq décimales
