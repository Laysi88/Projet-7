import csv
import sys
import time  # Ajout de l'import de la bibliothèque time


class Action:
    def __init__(self, name, price, profit):
        self.name = name
        self.price = float(price)
        self.profit = float(profit)


def select_data():
    try:
        filename = "data/" + sys.argv[1] + ".csv"
    except IndexError:
        print("No file name found")
        sys.exit(1)

    actions_data = read_csv(filename)
    return actions_data


def read_csv(filename):
    try:
        with open(filename) as csvfile:
            data_file = csv.reader(csvfile, delimiter=",")
            next(data_file)
            # Creer une liste d'objets Action
            actions_data = [
                Action(row[0], row[1], row[2]) for row in data_file if float(row[1]) > 0 and float(row[2]) > 0
            ]
            return actions_data
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)


def knapsack(actions):
    # initialiser les variables
    budgetmax = 500
    max_profit = 0
    liste_actions = []

    # Start time
    start_time = time.time()

    # trier les actions par profit décroissant
    actions.sort(key=lambda x: x.profit, reverse=True)
    # Tant qu'il reste de l'argent et des actions
    while actions and budgetmax > 0:
        # Choisir l'action avec le profit le plus élevé
        action = actions.pop(0)
        # Si l'action est abordable, l'ajouter à la liste
        if action.price <= budgetmax and action.price > 0:
            # Soustraire le prix de l'action du budget
            budgetmax -= action.price
            # Ajouter le profit de l'action au profit total
            max_profit += action.price * (action.profit / 100.0)
            # Ajouter l'action à la liste

            liste_actions.append(action)

    # Afficher le profit total
    print(f"Profit total : {max_profit}")
    # Afficher le budget utilisé
    print(f"Budget utilisé : {500 - budgetmax}")

    for action in liste_actions:
        print(action.name)

    # end time
    end_time = time.time()
    # print the time
    print("Time:", end_time - start_time)


if __name__ == "__main__":
    actions = select_data()
    knapsack(actions)
