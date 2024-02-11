import random
from collections import defaultdict
import matplotlib.pyplot as plt

def two_dices_probabilities(nums):
    counts = defaultdict(int)
    for _ in range(nums):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        counts[dice1 + dice2] += 1

    probabilities = {key: count / nums for key, count in counts.items()}
    probabilities = dict(sorted(probabilities.items()))
    return probabilities


probabilities_mc_10k = two_dices_probabilities(10_000)
probabilities_mc_10m = two_dices_probabilities(10_000_000)

probabilities_calc = {i: (i - 1) / 36 if i < 8 else (13 - i) / 36 for i in probabilities_mc_10m}

print(f"{'| Dice': <4} | {'Probability 10k': <15} | {'Probability 10M': <15} | {'Probability Calculated': <24}")
print(f"| {'-'*4} | {'-'*15} | {'-'*15} | {'-'*24}")
for dice, prob in probabilities_calc.items():
    print(f"| {dice:>4} | {probabilities_mc_10k[dice]:15.4%} | {probabilities_mc_10m[dice]:15.4%} | {prob:15.8%}")


plt.bar(probabilities_mc_10m.keys(), probabilities_mc_10m.values())
plt.title('Two dices sum probability by Monte Carlo method (10M attempts)')
plt.show()
