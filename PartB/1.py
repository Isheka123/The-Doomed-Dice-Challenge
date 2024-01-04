def generateDiceACombinations(elements, length, current, allCombinations):
    if len(current) == length:
        allCombinations.append(list(current))
        return
 
    for element in elements:
        current.append(element)
        generateDiceACombinations(elements, length, current, allCombinations)
        current.pop()   

def generateDiceBCombinations(elements, length, start, current, allCombinations):
    if len(current) == length:
        allCombinations.append(list(current))
        return
    for i in range(start, len(elements)):
        current.append(elements[i])
        generateDiceBCombinations(elements, length, i + 1, current, allCombinations)
        current.pop()   

def probSum(arr1, arr2):
    psum1 = [0.0] * 12
    for i in arr1:
        for j in arr2:
            k = i + j
            psum1[k - 1] += 1
    for i in range(len(psum1)):
        if psum1[i] != 0:
            psum1[i] /= 36
    return psum1

def transform(dieA, dieB):
    elements1 = [1, 2, 3, 4]
    length = 6
    current = []
    combo1 = []
    generateDiceACombinations(elements1, length, current, combo1)
   
    elements2 = [1, 2, 3, 4, 5, 6, 7, 8]
    start = 0
    combo2 = []
    generateDiceBCombinations(elements2, length, start, current, combo2)

    psum = [0.0, 1.0 / 36, 2.0 / 36, 3.0 / 36, 4.0 / 36, 5.0 / 36, 6.0 / 36, 5.0 / 36, 4.0 / 36, 3.0 / 36, 2.0 / 36, 1.0 / 36]

    for i, prob in enumerate(psum[1:12], 2):
        possibilities = [(j, i - j) for j in range(1, 7) if 1 <= i - j <= 6]
        print(f"Probability of obtaining {i}: {prob:.2f} (possibilities = {possibilities})")

    flag = False
    for i in combo1:
        for j in combo2:
            if probSum(i, j) == psum:
                print("\nNew dice combinations:")
                print("New die_a:", *i)
                print("New die_b:", *j)
                flag = True
                break
        if flag:
            break
 
dieA = [1, 2, 3, 4, 5, 6]
dieB = [1, 2, 3, 4, 5, 6]
transform(dieA, dieB)
