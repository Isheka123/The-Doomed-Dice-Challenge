sum_count = [0] * 11  
Die1 = [1, 2, 3, 4, 5, 6]
Die2 = [1, 2, 3, 4, 5, 6]

for i in Die1:
    for j in Die2:
        sum_count[(i + j) - 2] += 1 

total_combinations = 6 * 6
probabilities = [count / total_combinations for count in sum_count]

for i, prob in enumerate(probabilities, 2):
    if i == 2:
        possibilities = [(1, 1)]
    else:
        possibilities = [(j, i - j) for j in range(1, 7) if 1 <= i - j <= 6]
    print(f"Probability of obtaining {i}: {prob:.2f} (possibilities = {possibilities})")

