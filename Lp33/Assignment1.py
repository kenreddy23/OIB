def fibonacci_Recursive(n):
    sequence = []
    for i in range(n):
        if i == 0:
            sequence.append(0)
        elif i == 1:
            sequence.append(1)
        else:
            sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence


def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]

    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

n = int(input("Enter the Number:"))  # Change this value for a different length of the sequence
# fib_sequence = fibonacci_Recursive(n)
# for num in fib_sequence:
#     print(num)

print("Iterative Fibonacci sequence:", fibonacci_iterative(n))



