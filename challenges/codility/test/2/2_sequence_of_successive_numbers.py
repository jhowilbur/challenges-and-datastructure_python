def solution(X):
    # maybe moving point to point
    # start with p1 =1 and p2 =1

    p1, p2 = 1, 1
    total = p1 ** 2
    sequences = []
    n = X

    # if sum less than n move p2 to the right or if sum greater than n move p1 to right

    while p1 <= (2 * n) ** 0.5:
        if total == n:
            sequences.append(list(range(p1, p2 + 1)))
            total -= p1 ** 2
            p1 += 1

        elif total < n:
            p2 += 1
            total += p2 ** 2

        else:
            total -= p1 ** 2
            p1 += 1

    sequences.sort(key=len, reverse=True)
    formatted = [str(len(sequences))]
    for seq in sequences:
        formatted.append('{} {}'.format(len(seq), ' '.join(map(str, seq))))

    return formatted


print(solution(2030))
