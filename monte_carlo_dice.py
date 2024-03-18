import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Симуляція кидків
    sum_counts = {i: 0 for i in range(2, 13)}

        #TODO Підрахунок кількості кидків для можливих значень сум
    
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum_counts[dice1 + dice2] += 1
    
    #TODO Обрахування ймовірності випаду кожної суми
    probabilities = {sum_val: count / num_rolls for sum_val, count in sum_counts.items()}
    
    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())
    
    # Створення графіка
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')
    
    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')
    
    plt.show()


if __name__ == "__main__":
    for accuracy in [100, 1000, 10000, 100000]:
        # Симуляція кидків і обчислення ймовірностей
        probabilities = simulate_dice_rolls(accuracy)

        # Відображення ймовірностей на графіку
        plot_probabilities(probabilities)