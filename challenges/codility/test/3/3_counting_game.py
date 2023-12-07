def solution(X):
    # alright, this test I suppose is more simple than the others
    # if the number is 7, then it and all multiples are invalid
    # and so, numbers multiples of 7 are also invalid
    # hmmmmm to resolve that, well we need to check the validation of the numbers, right?

    # check if the number is valid
    # find the next valid number

    n = X  # our given number

    def has_seven(num):
        return '7' in str(num)

    def is_invalid(num):
        if has_seven(num) or num % 7 == 0:
            return True

        for i in range(1, num + 1):
            if has_seven(i) and num % i == 0:
                return True

        return False

    if is_invalid(n):
        return -1

    n += 1
    while is_invalid(n):
        n += 1

    return n


print(solution(7))