def score(v):
    score = 0
    for i in range(len(v) - 1):
        score += abs(ord(v[i]) - ord(v[i + 1]))
    return score


v = input("Entrez une chaine:")
print(score(v))
