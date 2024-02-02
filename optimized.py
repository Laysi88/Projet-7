import time
import re


def extract_number(action_name):
    # Utilise une expression régulière pour extraire les chiffres du nom de l'action
    match = re.search(r"\d+", action_name)
    return int(match.group()) if match else float("inf")


def knapsack(actions, max_budget):
    start_time = time.time()  # Enregistrez le temps de début

    n = len(actions)
    dp = [[0] * (max_budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, max_budget + 1):
            if int(actions[i - 1][1]) <= j:
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

    included_actions = sorted(included_actions, key=extract_number)

    end_time = time.time()  # Enregistrez le temps de fin
    execution_time = end_time - start_time  # Calculez le temps d'exécution

    return max_profit, included_actions, execution_time


actions_data = [
    ("Action1", 20.0, 5.0),
    ("Action2", 30.0, 10.0),
    ("Action3", 50.0, 15.0),
    ("Action4", 70.0, 20.0),
    ("Action5", 60.0, 17.0),
    ("Action6", 80.0, 25.0),
    ("Action7", 22.0, 7.0),
    ("Action8", 26.0, 11.0),
    ("Action9", 48.0, 13.0),
    ("Action10", 34.0, 27.0),
    ("Action11", 42.0, 17.0),
    ("Action12", 110.0, 9.0),
    ("Action13", 38.0, 23.0),
    ("Action14", 14.0, 1.0),
    ("Action15", 18.0, 3.0),
    ("Action16", 8.0, 8.0),
    ("Action17", 4.0, 12.0),
    ("Action18", 10.0, 14.0),
    ("Action19", 24.0, 21.0),
    ("Action20", 114.0, 18.0),
]

max_budget = 500
result = knapsack(actions_data, max_budget)

print(
    "Budget total utilisé:",
    sum([float(actions_data[i][1]) for i in range(len(actions_data)) if actions_data[i][0] in result[1]]),
)
print("Profit maximal obtenu:", result[0])
print("Actions incluses dans la solution:", result[1])
print("Temps d'exécution:", result[2], "secondes")
