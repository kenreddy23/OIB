# Recursive Fibonacci function using recursion for each term
def fibonacci_recursive(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    sequence = fibonacci_recursive(n - 1)  # Recursively build the sequence
    sequence.append(sequence[-1] + sequence[-2])  # Add the next Fibonacci term
    return sequence

# Iterative Fibonacci function
def fibonacci_iterative(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    
    return sequence

# Main program
n = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Ask for the type of calculation method
method = int(input("Enter 1 for recursive or 2 for non-recursive: "))

if method == 1:
    fib_sequence = fibonacci_recursive(n)
    print("Recursive Fibonacci sequence:")
    for num in fib_sequence:
        print(num)  # Print each number vertically
elif method == 2:
    fib_sequence = fibonacci_iterative(n)
    print("Iterative Fibonacci sequence:", fib_sequence)  # Print entire list horizontally
else:
    print("Invalid input. Please enter 1 for recursive or 2 for non-recursive.")

