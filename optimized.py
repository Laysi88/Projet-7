import time
import re
import csv
import sys


def select_data():
    try:
        filename = "data/" + sys.argv[1] + ".csv"
    except IndexError:
        print("No file name found")
        sys.exit(1)

    actions_data = read_csv(filename)
    return actions_data  # Ajoutez cette ligne pour retourner actions_data


def read_csv(filename):
    try:
        with open(filename) as csvfile:
            data_file = csv.reader(csvfile, delimiter=",")
            next(data_file)  # Saute la première ligne (en-têtes)
            actions_data = []
            for row in data_file:
                if float(row[1]) <= 0 or float(row[2]) <= 0:
                    pass
                else:
                    actions_data.append((row[0], float(row[1]), float(row[2])))
            return actions_data
    except FileNotFoundError:
        print("File not found")
        sys.exit(1)


def knapsack(actions, max_budget):
    start_time = time.time()  # Enregistrez le temps de début

    n = len(actions)
    dp = [[0] * (max_budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, max_budget + 1):
            if float(actions[i - 1][1]) <= j:
                profit = float(actions[i - 1][1]) * (float(actions[i - 1][2]) / 100.0)
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - int(actions[i - 1][1])] + profit)
            else:
                dp[i][j] = dp[i - 1][j]

    max_profit = dp[n][max_budget]
    included_actions = []
    i, j = n, max_budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            included_actions.append(actions[i - 1][0])
            j -= int(actions[i - 1][1])
        i -= 1

    included_actions = sorted(included_actions)

    end_time = time.time()  # Enregistrez le temps de fin
    execution_time = end_time - start_time  # Calculez le temps d'exécution

    return max_profit, included_actions, execution_time


# Appel de select_data pour obtenir actions_data
actions_data = select_data()

max_budget = 500
result = knapsack(actions_data, max_budget)

used_budget = sum([float(actions_data[i][1]) for i in range(len(actions_data)) if actions_data[i][0] in result[1]])
final_used_budget = min(used_budget, max_budget)  # Assurez-vous que le budget utilisé n'excède pas le budget maximum

print("Budget total utilisé:", final_used_budget)
print("Profit maximal obtenu:", result[0])
print("Actions incluses dans la solution:", result[1])
print("Temps d'exécution:", result[2], "secondes")
