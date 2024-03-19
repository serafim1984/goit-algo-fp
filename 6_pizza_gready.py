# Adjusting the code to use a dictionary for items instead of a list of tuples.

# Define the items with their cost and calorie value.
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# Greedy approach
def greedy_algorithm(items, budget):

    # Sort items by the ratio of calories to cost
    items_sorted = sorted(items.items(), key = lambda x: x[1]['calories'] / x[1]['cost'], reverse = True)

    total_calories = 0
    remaining_budget = budget
    chosen_items = []
    for item, details in items_sorted:
        if details['cost'] <= remaining_budget:
            chosen_items.append(item)
            total_calories += details['calories']
            remaining_budget -= details['cost']
    return total_calories, budget - remaining_budget, chosen_items

# Dynamic Programming approach
def dynamic_programming(items, budget):
    # retrieve item names
    item_names = list(items.keys())

    # Create a DP table where rows represent up to the i-th item and columns represent budget
    dp_table = [[0 for x in range(budget + 1)] for y in range(len(items) + 1)]

    #TODO Реалізація побудови таблиці оптимального блюда по калоріям для всіх бюджетів
    for i in range(1, len(items) + 1):
        item_name = item_names[i - 1]
        item_cost = items[item_name]['cost']
        item_calories = items[item_name]['calories']

        for w in range(1, budget + 1):
            # if the current item can be added
            if item_cost <= w:
                # Max value between adding the current item or not
                dp_table[i][w] = max(item_calories + dp_table[i - 1][w - item_cost], dp_table[i - 1][w])
            else:
                # if the current item can't be added, inherit the value from the previous item
                dp_table[i][w] = dp_table[i - 1][w]
                
    #TODO Реалізація отримання оптимального набору страв через використання обчисленої таблиці
    chosen_items = []
    w = budget
    for i in range(len(items), 0, -1):
        item_name = item_names[i - 1]
        item_cost = items[item_name]['cost']

        if dp_table[i][w] != dp_table[i - 1][w]: # if the value comes from the inclusion of the ith item
            chosen_items.append(item_name) # include this item
            w -= item_cost # reduce the budget accordingly

    return dp_table[len(items)][budget], budget - w, chosen_items


if __name__ == '__main__':
    # Execute both algorithms
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print(greedy_result, dp_result)