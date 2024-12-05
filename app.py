def fibonacci(n):
    # Starting values for the Fibonacci series
    a, b = 0, 1
    series = []
    
    # Generate the Fibonacci series up to 'n' numbers
    for _ in range(n):
        series.append(a)
        a, b = b, a + b  # Update a and b to the next two numbers in the series
    
    return series

# Example usage
n = 10  # Number of terms you want to generate
print(f"First {n} terms of the Fibonacci series: {fibonacci(n)}")
