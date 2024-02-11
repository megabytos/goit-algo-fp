def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)
    calories = 0
    selected = []
    for name, item in sorted_items:
        if budget >= item["cost"]:
            budget -= item["cost"]
            calories += item["calories"]
            selected.append(name)
    return selected, calories


def dynamic_programming(items, budget):
    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]
    for i, (_, item) in enumerate(items.items(), start=1):
        cost = item["cost"]
        ccal = item["calories"]
        for j in range(1, budget + 1):
            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + ccal)

    selected = []
    calories = 0
    i, j = len(items), budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected.append(list(items.keys())[i - 1])
            j -= items[list(items.keys())[i - 1]]["cost"]
            calories += items[list(items.keys())[i - 1]]["calories"]
        i -= 1

    return selected, calories


if __name__ == "__main__":
    money = 100
    print(f"Budget: {money}")

    food = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    selected_items, total_calories = greedy_algorithm(food, money)
    print(f"Greedy algorithm : {total_calories} ccal -> {selected_items}")

    selected_items, total_calories = dynamic_programming(food, money)
    print(f"Dynamic programming: {total_calories} ccal -> {selected_items}")
