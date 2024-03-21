def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]  # Initializing the sequence with the first two terms
    for i in range(2, n):
        next_term = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
        fibonacci_sequence.append(next_term)
    return fibonacci_sequence # Return only the first n terms

# Asking the user to input the value of n
n = int(input("Enter the value of n: "))
fibonacci_sequence= generate_fibonacci(n)

# Generate the Fibonacci sequence
print(fibonacci_sequence)

